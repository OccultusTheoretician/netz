#!/usr/bin/env python3
r"""
tg_translate.py — NETZ War Desk · Module 1: Translation Pass

Takes a tg_wardesk_*.json pull, sends every non-English message through your
local Qwen3-30B (LM Studio, OpenAI-compatible endpoint at localhost:1234),
adds a `text_en` field to each message, writes an enriched output file.

After this runs, every message has text_en regardless of original language.
The cross-bias corroboration grader (Module 2) works on text_en only.

Usage:
    python tg_translate.py forecasts\tg_wardesk_2026-07-24_1850.json
    python tg_translate.py --latest          (auto-finds newest pull in forecasts\)

Requires LM Studio running with Qwen3-30B loaded (the model you already have).
No additional packages beyond what NETZ already uses.
"""
import os
import json, sys, pathlib, datetime, time, re, urllib.request, urllib.error

LM_URL = "http://localhost:1234/v1/chat/completions"
# A hardcoded model id is a silent trap: LM Studio rejects an unknown id with a
# bare HTTP 400, and the old handler printed only "Bad Request" — 420 messages
# failed for a name mismatch that took a /v1/models call to see. The id is now
# resolved from the server itself, overridable by NETZ_LM_MODEL, and any 400
# prints the server's own explanation.
MODEL  = os.environ.get("NETZ_LM_MODEL", "")   # blank = ask the server
MODELS_URL = "http://localhost:1234/v1/models"


def resolve_model() -> str:
    """Ask LM Studio what is actually loaded. Never guess a model id."""
    global MODEL
    if MODEL:
        return MODEL
    try:
        with urllib.request.urlopen(MODELS_URL, timeout=15) as r:
            ids = [m.get("id") for m in json.loads(r.read()).get("data", [])
                   if m.get("id")]
    except Exception as e:
        print("LM Studio is not answering at %s (%s).\n"
              "  Start it, load a model, and enable the local server "
              "(Developer tab -> Start Server)." % (MODELS_URL, e),
              file=sys.stderr)
        sys.exit(2)
    if not ids:
        print("LM Studio is running but has no model loaded — load one in the "
              "Chat or Developer tab, then rerun.", file=sys.stderr)
        sys.exit(2)
    pref = [i for i in ids if "qwen" in i.lower()]
    MODEL = (pref or ids)[0]
    print("LM model: %s%s" % (MODEL,
          "" if len(ids) == 1 else "  (of %d loaded: %s)" % (len(ids), ", ".join(ids))),
          file=sys.stderr)
    return MODEL
BATCH  = 8                     # messages per LM call — tune to your VRAM
RETRY  = 2

SKIP_LANGS = {"en"}            # langs that need no translation
# Even "ar/en" and "fa/en" channels often post fully non-English — translate all of them

def lm_translate(texts: list[str]) -> list[str]:
    """Send a batch of texts to local Qwen, get English translations back."""
    numbered = "\n".join(f"[{i+1}] {t[:600]}" for i,t in enumerate(texts))
    payload = {
        "model": resolve_model(),
        "temperature": 0.1,
        "max_tokens": 2048,
        "messages": [
            {"role": "system", "content":
             "You are a translator. Translate each numbered item to clear English. "
             "Return ONLY the translations, numbered the same way. "
             "If an item is already English, copy it unchanged. "
             "Preserve proper nouns, place names, and military unit designations. "
             "No commentary, no preamble, just the numbered translations."},
            {"role": "user", "content": numbered}
        ]
    }
    body = json.dumps(payload).encode()
    req  = urllib.request.Request(LM_URL, data=body,
                                  headers={"Content-Type":"application/json"})
    for attempt in range(RETRY):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                resp = json.loads(r.read())
                raw  = resp["choices"][0]["message"]["content"].strip()
                # parse "[N] translation" blocks back into list
                parts = re.split(r"\[\d+\]\s*", raw)[1:]   # drop empty head
                if len(parts) == len(texts):
                    return [p.strip() for p in parts]
                # fallback: split by newlines if regex misfired
                lines = [l for l in raw.splitlines() if l.strip()]
                return (lines + [""] * len(texts))[:len(texts)]
        except urllib.error.HTTPError as e:
            # The body carries the reason; without it a 400 is unreadable.
            try:
                detail = e.read().decode("utf-8", "replace")[:300]
            except Exception:
                detail = "(no body)"
            print(f"  LM HTTP {e.code}: {detail}", file=sys.stderr)
            if e.code == 400 and "model" in detail.lower():
                print("  -> the model id was rejected. Set the right one:\n"
                      "     $env:NETZ_LM_MODEL=\"<id from "
                      "http://localhost:1234/v1/models>\"", file=sys.stderr)
                return ["[TRANSLATION FAILED]"] * len(texts)
            if attempt < RETRY-1:
                print("  retrying in 3s...", file=sys.stderr)
                time.sleep(3)
                continue
            return ["[TRANSLATION FAILED]"] * len(texts)
        except Exception as e:
            if attempt < RETRY-1:
                print(f"  LM error ({e}); retrying in 3s...", file=sys.stderr)
                time.sleep(3)
            else:
                print(f"  LM failed after {RETRY} attempts: {e}", file=sys.stderr)
                return ["[TRANSLATION FAILED]"] * len(texts)

def needs_translation(msg: dict) -> bool:
    if not msg.get("text","").strip():
        return False
    lang = msg.get("lang","")
    # pure English channels
    if lang in SKIP_LANGS:
        return False
    # mixed channels still likely have non-English content — translate
    return True

def run(src: pathlib.Path):
    data = json.loads(src.read_text(encoding="utf-8"))
    msgs = data["messages"]

    to_translate = [(i,m) for i,m in enumerate(msgs) if needs_translation(m)]
    already_en   = len(msgs) - len(to_translate)
    print(f"{src.name}: {len(msgs)} messages, {len(to_translate)} to translate, "
          f"{already_en} already English or empty", file=sys.stderr)

    if not to_translate:
        print("Nothing to translate.", file=sys.stderr)
        return

    # mark English-only messages immediately
    for i,m in enumerate(msgs):
        if not needs_translation(m):
            m["text_en"] = m.get("text","")

    # batch-translate
    total = len(to_translate)
    done  = 0
    for b_start in range(0, total, BATCH):
        batch = to_translate[b_start : b_start+BATCH]
        idxs  = [i for i,_ in batch]
        texts = [m["text"] for _,m in batch]
        translations = lm_translate(texts)
        for idx, tr in zip(idxs, translations):
            msgs[idx]["text_en"] = tr
        done += len(batch)
        pct   = done*100//total
        bar   = "█"*(pct//5) + "░"*(20-pct//5)
        print(f"\r  [{bar}] {pct}% ({done}/{total})", end="", file=sys.stderr)

    print(file=sys.stderr)

    # write enriched file
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d_%H%M")
    out   = src.parent / f"tg_translated_{stamp}.json"
    data["_meta"]["translated"] = stamp+"Z"
    data["_meta"]["note"] = (data["_meta"].get("note","") +
        " Translation pass complete. text_en field available on all messages.")
    out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nenriched output: {out}", file=sys.stderr)
    print(f"sample (first translated):", file=sys.stderr)
    for i,m in enumerate(msgs):
        if m.get("text_en") and m.get("lang","") not in SKIP_LANGS:
            orig = m["text"][:80].replace("\n"," ")
            tren = m["text_en"][:80].replace("\n"," ")
            print(f"  [{m['zone']}|{m['lang']}] {orig}", file=sys.stderr)
            print(f"  → EN: {tren}", file=sys.stderr)
            if i > 5: break

if __name__ == "__main__":
    if "--latest" in sys.argv or len(sys.argv) < 2:
        pulls = sorted(pathlib.Path("forecasts").glob("tg_wardesk_*.json"))
        if not pulls:
            print("No pull files found in forecasts/. Run tg_fetch.py first.", file=sys.stderr)
            sys.exit(1)
        src = pulls[-1]
        print(f"Using latest pull: {src}", file=sys.stderr)
    else:
        src = pathlib.Path(sys.argv[1])
    if not src.exists():
        print(f"File not found: {src}", file=sys.stderr)
        sys.exit(1)
    run(src)
