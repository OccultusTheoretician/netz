#!/usr/bin/env python3
"""register_build.py - THE REGISTER STOPS BEING A HAND-TYPED CLAIM.

docs/register.json is the conformance register: who has asserted conformance
to this desk's standards, under what scope, verified when. It has been
maintained by hand, and by 2026-08-09 it had drifted in the two ways a
hand-typed record always drifts:

  - it declared "9 records sealed 2026-07-25" while the hashlog held 10
  - it carried "verified 2026-07-27", thirteen days old, on a page whose
    entire subject is whether claims still hold

Neither is a lie; both are the ordinary decay of an assertion nobody
recomputed. The fix is not a fresher date typed in. It is to COMPUTE the
entry: this script runs knp_verify.py - the same third-party verifier the
site tells every visitor to run - against the live hashlog, and writes the
register from its actual verdict. The scope line, the record count, the
must/should tallies and the verification date all come from the run.

A register whose only entry is its own author is a house rule with a
table, and the entry says so in its own note. That does not change here.
What changes is that the house rule is now recomputed rather than
remembered.

EXTERNAL ENTRIES ARE PRESERVED. Any entry not marked assessed_by "self" is
carried across untouched - this script owns the self-assessment only. A
third party's claim is theirs to state and is never rewritten by the desk's
own build.

Read-only against the hashlog. Writes docs/register.json.
"""
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
REG = DOCS / "register.json"
HASHLOG = DOCS / "kalls_hashlog.json"

SELF_PARTY = "The Prescient Desk (NebelKraehe)"
SELF_NOTE = ("Issuer of the standards. Self-assessed, which is the weakest "
             "class on this page and is marked as such rather than presented "
             "as validation. A register whose only entry is its own author "
             "is a house rule with a table. This entry is recomputed by "
             "register_build.py from a live verifier run, not typed.")


def main():
    if not HASHLOG.exists():
        print("REGISTER - docs/kalls_hashlog.json absent - INDETERMINATE, "
              "register NOT rewritten", file=sys.stderr)
        return 1
    try:
        proc = subprocess.run(
            [sys.executable, str(HERE / "knp_verify.py"), str(HASHLOG),
             "--json"], capture_output=True, text=True, timeout=120)
        v = json.loads(proc.stdout)
    except Exception as exc:
        print(f"REGISTER - verifier did not return machine output ({exc}) - "
              f"INDETERMINATE, register NOT rewritten. An unverifiable "
              f"register is left as it stands rather than restamped with a "
              f"fresh date it did not earn.", file=sys.stderr)
        return 1

    musts = v.get("must_failures") or []
    shoulds = v.get("should_departures") or []
    n = v.get("records")
    conformant = bool(v.get("conformant"))
    when = str(v.get("verified_at") or
               datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    day = when[:10]

    entry = {
        "party": SELF_PARTY,
        "note": SELF_NOTE,
        "standard": "KNP-26 - first edition",
        "statement": "unmodified",
        "assessed_by": "self",
        "scope": f"Kraehe's Kalls clutch, {n} record(s) on the live hashlog",
        "verified": (f"{day} - {len(musts)} must, {len(shoulds)} should - "
                     + ("CONFORMANT" if conformant else "NONCONFORMANT")),
        "verified_at": when,
        "verifier": str(v.get("verifier", "knp_verify")),
        "recomputed_by": "register_build.py",
        "record": "https://retroprescientaudit.com/kalls_hashlog.json",
    }
    if not conformant:
        entry["nonconformance"] = musts[:8]
    if shoulds:
        entry["should_departures"] = [
            (s.get("message") if isinstance(s, dict) else str(s))
            for s in shoulds][:8]

    prior = {"schema": "kfk-register/1.0", "entries": []}
    if REG.exists():
        try:
            prior = json.loads(REG.read_text(encoding="utf-8"))
        except Exception:
            pass
    external = [e for e in prior.get("entries", [])
                if str(e.get("assessed_by", "")).lower() != "self"]

    out = {
        "schema": "kfk-register/1.0",
        "as_of": day,
        "note": prior.get("note", "Entries are listed with the verifier's "
                          "own output, unedited. Listing is not endorsement."),
        "build_note": ("The self-assessed entry is recomputed from a live "
                       "knp_verify run on every build; external entries are "
                       "carried across untouched, because a third party's "
                       "claim is theirs to state and is never rewritten by "
                       "this desk."),
        "entries": [entry] + external,
    }
    REG.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"REGISTER - self entry recomputed: {n} record(s), "
          f"{len(musts)} must, {len(shoulds)} should, "
          f"{'CONFORMANT' if conformant else 'NONCONFORMANT'}",
          file=sys.stderr)
    print(f"REGISTER - {len(external)} external entry/entries carried "
          f"untouched", file=sys.stderr)
    print(f"REGISTER - -> {REG}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
