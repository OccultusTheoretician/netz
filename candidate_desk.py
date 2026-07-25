#!/usr/bin/env python3
"""
candidate_desk.py — draft NEW prediction-ledger entries that are born conformant
to RETRO-PRESCIENT AUDIT STANDARDS, First Edition (RPAS-26).

The migration tool (rpas_audit.py --migrate) reconciles the 67 legacy entries by
stamping UNSET placeholders. This tool does the opposite and better: it builds
entries that satisfy the seven seals (RPAS 4.02) AT CREATION, so they never need
migrating. Every design law that governs the seals is enforced by the workflow,
not left to discipline.

THE VEIL (RPAS 3.02) IS ENFORCED IN CODE.
  The machine drafts the question; the number is entered cold by the forecaster.
  This tool NEVER suggests, prefills, defaults, or displays a probability before
  the forecaster commits one. Loading a candidate clears the probability field.
  It will refuse to write an entry whose probability it supplied.

KEYED/KEYLESS BEFORE RESOLUTION (RPAS 4.02f, 4.03, 1.04 — the master law).
  The forecaster declares, at creation, the priors held and what would make a hit
  deducible from them. A determination is impossible to add later without it being
  KEYED by rule — so the tool forces it now, while the outcome is unknown.

    # interactive (the honest path — you type the number, blind):
    python candidate_desk.py --new --ledger ledger.json

    # from a drafted candidate file (question only, NO probability), then commit:
    python candidate_desk.py --from-candidate cand.json --ledger ledger.json

    # draft a skeleton for review (no probability field emitted, by design):
    python candidate_desk.py --skeleton "statement here" --domain geo/security

Writes append to the ledger's projections list; a .pre_candidate backup is made.
Nothing is committed to git by this tool — you review, then commit by hand.
"""
from __future__ import annotations
import argparse, json, sys, re, hashlib, datetime as dt
from pathlib import Path

SOURCE_HINT = re.compile(r"\b(reuters|ap|associated press|bbc|al jazeera|guardian|"
                         r"bloomberg|cnn|afp|nyt|new york times|official|filing|sec|"
                         r"repo|commit|hash|records?|gazette|register)\b", re.I)
KEYCLASS = {"keyed", "keyless"}


def load(path: Path):
    if not path.exists():
        return {"projections": []}, "projections"
    d = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(d, list):
        return {"projections": d}, "projections"
    for k in ("projections", "entries", "predictions"):
        if isinstance(d.get(k), list):
            return d, k
    raise SystemExit("could not locate entries list")


def next_id(entries, prefix="RPA"):
    today = dt.date.today().strftime("%Y%m%d")
    n = sum(1 for e in entries if today in str(e.get("id", ""))) + 1
    return f"{prefix}-{today}-{n:02d}"


def parse_date(s):
    try:
        return dt.datetime.strptime(s[:10], "%Y-%m-%d").date()
    except Exception:
        return None


def validate_seals(e: dict, probability_source: str) -> list[str]:
    """Return blocking errors. Empty list == conformant, may be sealed."""
    errs = []
    # 4.02a statement
    if not (e.get("statement") or "").strip():
        errs.append("4.02a: empty statement")
    elif len(e["statement"]) < 25:
        errs.append("4.02a: statement too thin — a hostile reader must not be able to stretch it")
    # 4.02b resolution, mechanical + sourced
    res = (e.get("resolution") or "").strip()
    if not res:
        errs.append("4.02b: no resolution criterion")
    elif not SOURCE_HINT.search(res):
        errs.append("4.02b: resolution names no concrete source/instrument (must be third-party adjudicable)")
    # 4.02c deadline
    d = parse_date(e.get("deadline", ""))
    if not d:
        errs.append("4.02c: deadline missing/unparseable (YYYY-MM-DD)")
    elif d <= dt.date.today():
        errs.append("4.02c: deadline is not in the future — cannot pre-register a resolved outcome")
    # 4.02d probability + THE VEIL
    p = e.get("probability")
    if p is None:
        errs.append("4.02d: no probability")
    elif not (isinstance(p, int) and 0 <= p <= 100):
        errs.append("4.02d: probability must be integer 0-100")
    if probability_source != "forecaster":
        errs.append("3.02 VEIL VIOLATION: probability was not entered cold by the forecaster — refusing to seal")
    # 4.02e failure condition, distinct
    fc = (e.get("failure_condition") or "").strip()
    if not fc:
        errs.append("4.02e/4.03: no failure condition — UNFALSIFIABLE, must not seal")
    elif fc.strip().lower() == res.strip().lower():
        errs.append("4.02e: failure condition identical to resolution — state the MISS outcome explicitly")
    # 4.02f keyed/keyless before resolution
    kk = (e.get("keyed_keyless") or "").strip().lower()
    if kk not in KEYCLASS:
        errs.append("4.02f/1.04: keyed/keyless must be declared now (keyed|keyless) — after resolution it is KEYED by rule")
    if not (e.get("keyed_keyless_rationale") or "").strip():
        errs.append("4.02f: keyed/keyless rationale required — name the priors held")
    return errs


def seal(e: dict) -> dict:
    """Attach 4.02g: timestamp + content hash. The hash covers the pre-registered
    fields only, so later administrative edits are detectable against it."""
    e.setdefault("date_issued", dt.date.today().isoformat())
    e["sealed_at"] = dt.datetime.now(dt.timezone.utc).isoformat()
    payload = json.dumps({k: e.get(k) for k in
                          ("statement", "resolution", "deadline", "probability",
                           "failure_condition", "keyed_keyless", "keyed_keyless_rationale",
                           "date_issued")},
                         sort_keys=True, ensure_ascii=False)
    e["seal_sha256"] = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    return e


def emit_skeleton(statement, domain):
    """A candidate skeleton — deliberately NO probability field (the veil)."""
    return {
        "statement": statement or "",
        "domain": domain or "",
        "resolution": "",              # fill: name at least one concrete source/instrument
        "deadline": "",                # fill: YYYY-MM-DD, future
        "failure_condition": "",       # fill: the exact outcome that scores this a MISS
        "keyed_keyless": "",           # fill BEFORE resolution: keyed | keyless
        "keyed_keyless_rationale": "", # fill: what priors you hold; what would make a hit deducible
        "citations": [],
        # NOTE: no 'probability' key by design. It is added only at commit,
        # entered cold. See RPAS 3.02.
    }


def interactive_new(entries):
    print("\nRPAS-26 CANDIDATE DESK — new entry under the veil\n"
          "The probability is asked LAST, and you enter it blind. "
          "Everything else is fixed before the number exists.\n")
    e = emit_skeleton("", "")
    e["statement"] = input("Statement (unstretchable): ").strip()
    e["domain"] = input("Domain: ").strip()
    e["resolution"] = input("Resolution criterion (NAME a source/instrument): ").strip()
    e["deadline"] = input("Deadline (YYYY-MM-DD, future): ").strip()
    e["failure_condition"] = input("Failure condition (the MISS outcome, explicit): ").strip()
    while True:
        kk = input("Keyed or keyless? [keyed/keyless]: ").strip().lower()
        if kk in KEYCLASS:
            e["keyed_keyless"] = kk
            break
        print("  must be 'keyed' or 'keyless' — this is the master law (1.04)")
    e["keyed_keyless_rationale"] = input("  rationale — what priors do you hold? ").strip()
    print("\n--- everything above is now fixed. the number does not yet exist. ---")
    while True:
        raw = input("Probability 0-100 (entered COLD): ").strip()
        try:
            p = int(raw)
            if 0 <= p <= 100:
                e["probability"] = p
                break
        except ValueError:
            pass
        print("  integer 0-100")
    e["id"] = next_id(entries)
    e["model"] = "forecaster/blind"
    return e, "forecaster"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", required=True)
    ap.add_argument("--new", action="store_true", help="interactive, veil-enforced")
    ap.add_argument("--from-candidate", help="candidate JSON WITHOUT a supplied probability")
    ap.add_argument("--skeleton", help="print a blank conformant skeleton for this statement")
    ap.add_argument("--domain", default="")
    a = ap.parse_args()

    if a.skeleton:
        print(json.dumps(emit_skeleton(a.skeleton, a.domain), ensure_ascii=False, indent=2))
        print("\n# Fill every field. Add NO probability here. Commit with --from-candidate,\n"
              "# which will ask for the number cold, or use --new for the guided path.")
        return

    path = Path(a.ledger)
    doc, key = load(path)
    entries = doc[key]

    if a.new:
        e, psource = interactive_new(entries)
    elif a.from_candidate:
        cand = json.loads(Path(a.from_candidate).read_text(encoding="utf-8"))
        if "probability" in cand:
            sys.exit("REFUSED (3.02): candidate file contains a probability. The number must be "
                     "entered cold at commit, not carried in the draft. Remove it and re-run.")
        e = cand
        e["id"] = e.get("id") or next_id(entries)
        while True:
            raw = input(f"[{e.get('statement','')[:50]}...]\nProbability 0-100 (entered COLD): ").strip()
            try:
                p = int(raw)
                if 0 <= p <= 100:
                    e["probability"] = p
                    break
            except ValueError:
                pass
            print("  integer 0-100")
        psource = "forecaster"
    else:
        sys.exit("choose --new, --from-candidate, or --skeleton")

    errs = validate_seals(e, psource)
    if errs:
        print("\nNOT SEALED — conformance failures:")
        for x in errs:
            print("  ✗ " + x)
        print("\nFix and re-run. No entry written.")
        sys.exit(1)

    seal(e)
    entries.append(e)
    bak = path.with_suffix(".json.pre_candidate")
    if path.exists():
        bak.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nSEALED and appended: {e['id']}")
    print(f"  seal_sha256: {e['seal_sha256'][:16]}…  ({e['sealed_at']})")
    print(f"  backup: {bak.name}")
    print("\nNEXT: commit ledger.json, then publish the seal hash to your external clock (4.05).")


if __name__ == "__main__":
    main()
