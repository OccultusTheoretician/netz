#!/usr/bin/env python3
r"""
dialektik_meter.py - public-figure position tracking. Verification only.

WHAT IT IS
The Dialektik Meter reads the SAME graded event artifact dialektik_feed reads
and follows the same law: it PROPOSES, the operator rules. Where the feed
scores a dyad's stated-vs-operational posture, the Meter tracks what named
public figures are RECORDED SAYING over time - positions taken, how often, and
where two dated statements on one topic diverge.

WHAT IT REFUSES, STRUCTURALLY (not by politeness)

  NO JUDGMENT LAYER. It never scores a position as good, bad, hypocritical,
  consistent or sincere. It records what was said, when, by whom, sourced.

  IT NEVER EMITS A "SWITCH". Claiming a real person reversed themselves is a
  factual claim about that person, and two channels summarising one speech
  differently is not a reversal. The Meter emits DIVERGENCE CANDIDATES -
  paired dated observations on one topic whose stances differ - printed side
  by side for OPERATOR adjudication. The word switch appears in no output.

  NO NAME FROM MEMORY. The figure register is operator-curated. --propose
  harvests candidate names FROM THE CORPUS with their counts and excerpts;
  a name never enters the register because a model recalled it. (The identifier
  finding of 2026-08-07 is the same failure class in a different uniform.)

  ECHO IS NOT CORROBORATION. An observation carried by one side only is marked
  echo and CANNOT form a divergence pair on its own; a pair needs at least one
  cross-side-corroborated member. Single-source statements are recorded and
  flagged, never suppressed.

  TRANSLATION-MEDIATED. Non-English statements pass through the local model.
  A stance difference may be the translator's word choice, not the speaker's.
  Every excerpt carries the flag; this is the ohrwurm_link lesson (lexical
  divergence 1.00 was measuring language, not framing).

  INDETERMINATE, NOT EMPTY. An unreadable input prints INDETERMINATE and
  returns nothing scored - it never becomes a clean empty result (KK31/F-b).

  PUBLIC FIGURES ONLY. The register is the boundary. A candidate that is not a
  public figure acting in a public role is dropped by the operator at curation,
  and the tool says so at every proposal.

USAGE
    python dialektik_meter.py --propose            harvest candidate figures
    python dialektik_meter.py --run                observations + divergences
    python dialektik_meter.py --run --figure "..."  one figure only

Register: dialektik_figures.json (operator-curated; --propose writes a
proposal file beside it and never edits it).
"""
import argparse, glob, json, re, sys, unicodedata
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
FORECASTS = HERE / "forecasts"
REGISTER = HERE / "dialektik_figures.json"

TITLES = ("president","prime minister","minister","secretary","chancellor",
          "ayatollah","general","admiral","commander","spokesman","spokesperson",
          "ambassador","chief of staff","foreign minister","defence minister",
          "defense minister","envoy","governor","premier")
NAME_RE = re.compile(r"\b([A-Z][a-z]+(?:\s+(?:(?:bin|al|de|van|der)\b|[A-Z][a-z]+)){1,3})\b")

# KK32-PROPOSER: titles are consumed as a PREFIX so the NAME survives intact.
# The old pattern counted title words inside the 3-word cap, which truncated
# "Iranian President Masoud <surname>" and "Brigadier General Hossein <surname>".
# NOTE: case-insensitivity is SCOPED to the title alternation. A global re.I
# made [A-Z] match lowercase, so name spans ran into the following words
# ("Masoud Pezeshkian addressed the") - caught in smoke, fixed here.
TITLE_PREFIX = re.compile(
    r"(?i:president|prime minister|foreign minister|defen[cs]e minister|minister|"
    r"secretary|chancellor|ayatollah|brigadier general|lieutenant general|"
    r"major general|general|admiral|commander|spokesman|spokesperson|"
    r"ambassador|envoy|senator|governor|premier)\s+"
    r"([A-Z][a-z]+(?:\s+(?:(?:bin|al|de|van|der)\b|[A-Z][a-z]+)){0,3})")

# Organisation nouns. A span carrying one of these is an institution, not a
# person; dropped with its reason printed, never silently (KK31 doctrine).
INSTITUTION_NOUNS = (
    "council","ministry","republic","forces","staff","committee","states",
    "nations","agency","command","army","navy","guard","corps","parliament",
    "assembly","department","bureau","office","service","authority","union",
    "organization","organisation","alliance","federation","government",
    "administration","press","media","report","news","pivot","summit")


def _is_institution(span):
    low = span.lower()
    return next((n for n in INSTITUTION_NOUNS if n in low), None)

# Topic keys are TOPIC WORDS, not claims about anyone. Operator-editable in
# the register under "topics".
DEFAULT_TOPICS = {
    "ceasefire": ["ceasefire","truce","cessation","armistice"],
    "negotiations": ["talks","negotiat","dialogue","summit","mediat"],
    "sanctions": ["sanction","embargo","export control","asset freeze"],
    "escalation": ["escalat","strike","retaliat","offensive","mobiliz"],
    "withdrawal": ["withdraw","pull out","pullback","disengage"],
    "nuclear": ["nuclear","enrich","centrifuge","iaea"],
    "aid": ["aid","humanitarian","corridor","convoy"],
}
# Stance cues are LINGUISTIC, deliberately coarse, and printed with every use.
STANCE = {
    "supports": ["support","agree","accept","welcome","back","endorse","commit to","ready to"],
    "opposes": ["reject","refuse","oppose","condemn","will not","rule out","never accept"],
}
EXCERPT = 220


def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii","ignore").decode().lower()


def newest_events(explicit=None):
    if explicit:
        p = Path(explicit); return p if p.exists() else None
    cands = []
    for base in (FORECASTS, HERE, Path.cwd()):
        cands += glob.glob(str(base / "tg_events_*.json"))
    return Path(sorted(set(cands))[-1]) if cands else None


def load_events(path):
    """F-b rule: unreadable input is INDETERMINATE and prints, never an empty pass."""
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    except Exception as e:
        print(f"  INDETERMINATE - dialektik_meter could not read {path}: {e}. "
              f"No observations were produced; this is NOT an empty result.",
              file=sys.stderr)
        return None
    evs = raw.get("events") if isinstance(raw, dict) else raw
    if evs is None and isinstance(raw, dict):
        evs = (raw.get("kinetic") or []) + (raw.get("statements") or [])
    return evs or []


def load_register():
    if not REGISTER.exists():
        return {"figures": [], "topics": DEFAULT_TOPICS}
    raw = REGISTER.read_text(encoding="utf-8-sig")  # KK32B-REGISTERREAD: Notepad BOM
    if not raw.strip():
        print("  register file exists but is EMPTY - paste the skeleton and save:\n"
              '    {"figures":[{"name":"...","role":"...","side":"...","variants":["..."]}]}',
              file=sys.stderr)
        return None
    try:
        d = json.loads(raw)
    except Exception as e:
        print(f"  INDETERMINATE - register unreadable ({e}). Refusing to run "
              f"against a register that may be partial.", file=sys.stderr)
        return None
    d.setdefault("topics", DEFAULT_TOPICS)
    return d


def statements(evs):
    return [e for e in evs if str(e.get("track","")) == "statement"]


def topic_of(text, topics):
    f = fold(text); hits = [k for k, ws in topics.items() if any(w in f for w in ws)]
    return hits


def stance_of(text):
    f = fold(text)
    got = [k for k, ws in STANCE.items() if any(w in f for w in ws)]
    return got[0] if len(got) == 1 else None   # ambiguous -> no stance, by rule


def cmd_propose(evs):
    """Harvest candidate figures FROM THE CORPUS. Never from recall."""
    counts, samples, conf, dropped = {}, {}, {}, {}
    for e in statements(evs):
        for s in (e.get("sources") or []):
            t = s.get("text_en") or ""
            if not t:
                continue
            titled = {m.group(1).strip() for m in TITLE_PREFIX.finditer(t)}
            bare = {n.strip() for n in NAME_RE.findall(t)} - titled
            for nm, c in [(n, "title-cued") for n in titled] + \
                         [(n, "no title cue") for n in bare]:
                if len(nm) < 6 or " " not in nm:
                    continue
                inst = _is_institution(nm)          # KK32-PROPOSER
                if inst:
                    dropped[nm] = f"institution noun '{inst}'"
                    continue
                counts[nm] = counts.get(nm, 0) + 1
                conf[nm] = "title-cued" if c == "title-cued" or conf.get(nm) == "title-cued" else c
                samples.setdefault(nm, t[:EXCERPT])
    if not counts:
        print("  no candidates - the statement track carries no title-cued names "
              "in this pull. That is a finding about the pull, not a failure.")
        return 0
    ranked = sorted(counts.items(), key=lambda kv: -kv[1])
    out = {"_meta": {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "rule": ("names appearing in statement-track source text that also "
                              "carries a title cue; corpus-derived only, never recalled"),
                     "operator_gate": ("PUBLIC FIGURES ONLY. Drop any candidate who is not "
                                       "a public figure acting in a public role. Add name "
                                       "variants and transliterations by hand - the matcher "
                                       "is strict and will miss what is not listed.")},
           "candidates": [{"name": n, "mentions": c, "confidence": conf.get(n, "?"),
                           "sample": samples[n]} for n, c in ranked],
           "dropped_as_institution": dropped}
    p = FORECASTS / f"dialektik_figures_proposed_{datetime.now(timezone.utc):%Y-%m-%d_%H%M}.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n  {len(ranked)} candidate figure(s) proposed -> {p.name}")
    print(f"  {'name':32s} {'mentions':>8s}  {'basis':s}")
    for n, c in ranked[:25]:
        print(f"  {n:32s} {c:>8d}  {conf.get(n, '?')}")
    if dropped:  # KK32-PROPOSER: drops are printed, never silent
        print(f"\n  dropped as institution ({len(dropped)}):")
        for n, why in list(dropped.items())[:12]:
            print(f"    {n:30s} {why}")
    print("\n  NOTHING REGISTERED. Curate into dialektik_figures.json by hand:")
    print('    {"figures":[{"name":"...","role":"...","side":"...","variants":["..."]}]}')
    print("  Public figures only. Add transliteration variants or the matcher misses them.")
    return 0


def cmd_run(evs, reg, only=None):
    figs = reg.get("figures") or []
    if not figs:
        print("  register empty - run --propose, then curate dialektik_figures.json.")
        return 0
    topics = reg.get("topics") or DEFAULT_TOPICS
    obs = []
    for e in statements(evs):
        sides = e.get("sides") or []
        cross = len(sides) >= 2
        for s in (e.get("sources") or []):
            t = s.get("text_en") or ""
            if not t:
                continue
            fl = fold(t)
            for f in figs:
                if only and f.get("name") != only:
                    continue
                names = [f.get("name","")] + list(f.get("variants") or [])
                if not any(fold(n) and fold(n) in fl for n in names):
                    continue
                tps = topic_of(t, topics)
                st = stance_of(t)
                obs.append({"figure": f.get("name"), "role": f.get("role",""),
                            "date": s.get("date") or e.get("first_seen"),
                            "topics": tps, "stance": st,
                            "channel": s.get("channel"), "side": s.get("side"),
                            "grade": e.get("grade"), "cross_side": cross,
                            "echo": not cross,
                            "excerpt": t[:EXCERPT],
                            "translation_mediated": True})
    obs.sort(key=lambda o: str(o.get("date")))
    # divergence candidates: same figure+topic, differing stance, >=1 corroborated
    div = []
    by = {}
    for o in obs:
        if not o["stance"]:
            continue
        for tp in o["topics"]:
            by.setdefault((o["figure"], tp), []).append(o)
    for (fig, tp), rows in by.items():
        stances = {r["stance"] for r in rows}
        if len(stances) < 2:
            continue
        if not any(r["cross_side"] for r in rows):
            continue  # echo-only pairs never form a candidate
        a = next(r for r in rows if r["stance"] == sorted(stances)[0])
        b = next(r for r in rows if r["stance"] == sorted(stances)[1])
        div.append({"figure": fig, "topic": tp, "a": a, "b": b,
                    "requires_operator_adjudication": True,
                    "not_a_switch": ("A divergence candidate is two dated observations "
                                     "whose stance cues differ. It is NOT a finding that "
                                     "this person changed position: summary, translation, "
                                     "context and channel framing all produce this shape.")})
    doc = {"_meta": {"generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                     "figures_tracked": len(figs), "observations": len(obs),
                     "divergence_candidates": len(div),
                     "stance_rule": STANCE,
                     "limits": ("stance is coarse lexical cueing on translated text; "
                                "ambiguous or absent cues yield NO stance and cannot "
                                "enter a pair. echo-only pairs are excluded. no judgment "
                                "layer: nothing here scores a position.")},
           "observations": obs, "divergence_candidates": div}
    p = FORECASTS / f"dialektik_meter_{datetime.now(timezone.utc):%Y-%m-%d_%H%M}.json"
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n  {len(obs)} observation(s) · {len(div)} divergence candidate(s) -> {p.name}")
    for d in div[:8]:
        print(f"\n  {d['figure']} · {d['topic']}  [CANDIDATE - operator adjudicates]")
        print(f"    {str(d['a']['date'])[:16]}  {d['a']['stance']:8s} {d['a']['excerpt'][:90]}")
        print(f"    {str(d['b']['date'])[:16]}  {d['b']['stance']:8s} {d['b']['excerpt'][:90]}")
    if div:
        print("\n  These are CANDIDATES, not findings. Two dated statements whose stance")
        print("  cues differ is not evidence a person changed position. Adjudicate by")
        print("  reading both sources in full before anything is recorded anywhere.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--propose", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--figure", default=None)
    ap.add_argument("--file", default=None)
    a = ap.parse_args()
    src = newest_events(a.file)
    if not src:
        print("  no tg_events_*.json found - run the daily first", file=sys.stderr)
        return 1
    print(f"  source: {src.name}")
    evs = load_events(src)
    if evs is None:
        return 1
    print(f"  {len(evs)} event(s), {len(statements(evs))} on the statement track")
    if a.propose:
        return cmd_propose(evs)
    if a.run:
        reg = load_register()
        if reg is None:
            return 1
        return cmd_run(evs, reg, a.figure)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
