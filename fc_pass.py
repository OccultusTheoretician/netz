#!/usr/bin/env python3
"""
fc_pass.py — the 4.02f content pass over open entries lacking a failure
condition. Two modes, review between them:

    python fc_pass.py --draft      write FC_REVIEW.md + fc_proposals.json
    python fc_pass.py --apply all              apply every proposal
    python fc_pass.py --apply KKR-...,KKR-...  apply named ids only

The proposal is always the mechanical negation of the row's own resolution
basis — no new facts, no invented specifics: "the named source does not report
the stated outcome by the deadline." Editing a proposal in fc_proposals.json
before applying is the intended workflow.

Applies ONLY empty -> value on OPEN rows (the 4.02f window the ledger's
disclosure grants and rpas_verify encodes). It never touches keyed_keyless:
the determination is a judgment about what priors the forecaster held, and a
script holds none. Rows write through kkr.save_ledger, so the envelope stamps
and the post-cutover seal hook run untouched; pre-cutover rows stay bare per
the finding.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import kkr

HERE = Path(__file__).resolve().parent
PROPOSALS = HERE / "fc_proposals.json"
REVIEW = HERE / "FC_REVIEW.md"


def source_clause(resolution: str) -> str:
    first = re.split(r"(?<=[.!?])\s", (resolution or "").strip())[0]
    first = re.sub(r"^resolved\s+(from|via|by|using)\s+", "", first,
                   flags=re.I).strip().rstrip(".")
    first = re.sub(r"\s+on\s+\d{4}-\d{2}-\d{2}$", "", first)
    return first or "the named source in the resolution basis"


def propose(e: dict) -> str:
    return (f"{source_clause(e.get('resolution',''))} does not show the "
            f"stated outcome on or before {e.get('deadline','the deadline')}; "
            f"absence at the deadline scores this entry a MISS.")


def cmd_draft() -> int:
    rows = kkr.load_ledger()["projections"]
    targets = [e for e in rows if e.get("status") == "open"
               and not str(e.get("failure_condition", "")).strip()]
    props = {e["id"]: propose(e) for e in targets}
    PROPOSALS.write_text(json.dumps(props, ensure_ascii=False, indent=2),
                         encoding="utf-8")
    lines = [f"# FAILURE-CONDITION REVIEW — {len(targets)} open entries, "
             f"drafted {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
             "",
             "Each proposal is the mechanical negation of the row's own "
             "resolution basis. Edit fc_proposals.json where a row needs a "
             "sharper miss, then `python fc_pass.py --apply all` (or a "
             "comma-list of ids). Keyed/keyless stays yours; this pass "
             "touches nothing else.", ""]
    for e in targets:
        lines += [f"## {e['id']} · {e.get('model')} · deadline "
                  f"{e.get('deadline')}",
                  f"**statement:** {e.get('statement','')[:160]}",
                  f"**proposed fc:** {props[e['id']]}", ""]
    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print(f"drafted {len(targets)} proposals → {PROPOSALS.name}, "
          f"{REVIEW.name}")
    return 0


def cmd_apply(which: str) -> int:
    props = json.loads(PROPOSALS.read_text(encoding="utf-8"))
    ids = set(props) if which == "all" else {i.strip()
                                            for i in which.split(",")}
    data = kkr.load_ledger()
    n = skipped = 0
    for e in data["projections"]:
        if e.get("id") not in ids:
            continue
        if e.get("status") != "open" or str(
                e.get("failure_condition", "")).strip():
            skipped += 1
            continue
        e["failure_condition"] = props[e["id"]]
        n += 1
    kkr.save_ledger(data)
    print(f"applied {n} failure condition(s); skipped {skipped} "
          f"(not open, or already filled). Envelope restamped by "
          f"save_ledger; copy to docs/ and commit both. Keyed/keyless "
          f"determinations remain undone — they are the operator's judgment "
          f"(RPAS 4.02f), and any row resolving without one is KEYED by "
          f"rule (4.03).")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--draft", action="store_true")
    g.add_argument("--apply")
    a = ap.parse_args()
    return cmd_draft() if a.draft else cmd_apply(a.apply)


if __name__ == "__main__":
    sys.exit(main())
