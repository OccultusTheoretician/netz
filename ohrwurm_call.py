#!/usr/bin/env python3
"""
ohrwurm_call.py — the Ohrwurm forward channel. Crossing calls, sealed.

The register (ohrwurm_log.py) holds the retrospective half: origin claims,
anchored. This issues the predictive half: a dated, probabilistic, sealed
forecast that a specific phrase crosses the side boundary of the watched
corpus by a deadline — the retro-prescient shape applied to language, in
the falsifiable form KNM 7.03 claims for it.

    python ohrwurm_call.py --phrase "..." --from-side A --to-side B \
        --window-days 21 --probability 30 --keyless \
        --rationale "No prior sufficient to deduce the crossing."

The call becomes a ledger row, arm ohrwurm/propagation, through the same
gate every arm faces (minus report-grounding, which a language call cannot
carry — its grounding is the corpus register) and is sealed explicitly under
the 4.02g construction at issue. The corpus-scoped limit rides every row by
design: FIRST IN THIS CORPUS IS NOT FIRST IN THE WORLD, and a crossing
recorded here is a crossing of the watched set, not of reality.

Nothing resolves here. Resolution reads the published Ohrwurm outputs at the
deadline via `kkr --resolve`, like every other row.
"""

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import kkr
from candidate_desk import seal
from kkr import validate_projection

HERE = Path(__file__).resolve().parent
REGISTER = HERE / "docs" / "ohrwurm_register.json"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phrase", required=True)
    ap.add_argument("--from-side", required=True)
    ap.add_argument("--to-side", required=True)
    ap.add_argument("--window-days", type=int, required=True)
    ap.add_argument("--probability", type=int, required=True)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--keyed", action="store_true")
    g.add_argument("--keyless", action="store_true")
    ap.add_argument("--rationale", required=True,
                    help="what priors the forecaster holds (RPAS 4.02f)")
    a = ap.parse_args()

    now = datetime.now(timezone.utc)
    deadline = (now + timedelta(days=a.window_days)).strftime("%Y-%m-%d")
    phrase = a.phrase.strip()

    in_register = False
    if REGISTER.exists():
        reg = json.loads(REGISTER.read_text(encoding="utf-8"))
        in_register = any(f"[{phrase}]" in r.get("statement", "")
                          for r in reg.get("records", []))
    if not in_register:
        print(f"NOTE: '{phrase}' has no origin claim in the register — a "
              f"call on an emerging phrase is legitimate, and this note is "
              f"why the row's statement says 'as tracked', not 'as "
              f"registered'.", file=sys.stderr)

    entry = {
        "id": None,  # assigned below
        "date_issued": now.strftime("%Y-%m-%d"),
        "deadline": deadline,
        "statement": (f'The phrase "{phrase}", as tracked on side '
                      f"{a.from_side} of the NETZ watched-channel corpus, "
                      f"appears on at least one watched channel of side "
                      f"{a.to_side} on or before {deadline}."),
        "resolution": (f"Resolved from the Ohrwurm instrument's published "
                       f"outputs (docs/ohrwurm_register.json and "
                       f"docs/ohrwurm_latest.json in this repository) read "
                       f"on {deadline}: YES if any run dated after issuance "
                       f"records the phrase on a side-{a.to_side} channel "
                       f"with an appearance timestamp on or before the "
                       f"deadline."),
        "probability": a.probability,
        "failure_condition": (f"No side-{a.to_side} appearance of the phrase "
                              f"is recorded in the published corpus outputs "
                              f"by {deadline}; absence in the corpus record "
                              f"at the deadline scores this entry a MISS. "
                              f"The claim is corpus-scoped by design — first "
                              f"in this corpus is not first in the world, "
                              f"and a crossing outside the watched set does "
                              f"not rescue a miss."),
        "keyed_keyless": "keyed" if a.keyed else "keyless",
        "keyed_keyless_rationale": a.rationale.strip(),
        "status": "open",
        "model": "ohrwurm/propagation",
        "resolved_date": None,
        "audit": None,
        "notes": f"crossing call, window {a.window_days}d, "
                 f"origin-registered={str(in_register).lower()}",
    }

    reasons = [r for r in validate_projection(
        {"statement": entry["statement"], "resolution": entry["resolution"],
         "deadline": entry["deadline"], "probability": entry["probability"],
         "domain": "propagation"})
        if r != "no grounding citations to the report record"]
    if reasons:
        print("NOT SEALED — the gate rejects, reasons printed:",
              file=sys.stderr)
        for r in reasons:
            print(f"  ✗ {r}", file=sys.stderr)
        return 1

    data = kkr.load_ledger()
    tag = now.strftime("%Y%m%d")
    n = 1 + sum(1 for e in data["projections"]
                if str(e.get("id", "")).startswith(f"OW-{tag}-"))
    entry["id"] = f"OW-{tag}-{n:02d}"
    seal(entry)
    data["projections"].append(entry)
    kkr.save_ledger(data)

    print(f"SEALED · {entry['id']} · ohrwurm/propagation · "
          f"p={entry['probability']}% · deadline {deadline} · "
          f"{entry['keyed_keyless']}")
    print(f"  seal_sha256 {entry['seal_sha256'][:16]}… · "
          f"{entry['sealed_at']}")
    print("  Copy ledger.json to docs\\, commit both — the commit is the "
          "anchor. Resolution at deadline via kkr --resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
