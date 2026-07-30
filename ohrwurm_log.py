#!/usr/bin/env python3
"""
ohrwurm_log.py — the Ohrwurm register. Origin claims, anchored.

ohrwurm.py emits seal-ready origin claims (statement + SHA-256) onto the
served page — dated prose, but nothing append-only holds them. This appends
them to docs/ohrwurm_register.json, deduped by hash, so every first-appearance
claim carries a commit date a stranger can check against the repository
history. These are transparency records, not dark commitments: the statement
publishes in full beside its hash; the anchor supplies WHEN the claim existed,
which is the entire retro-prescient point applied to language.

    python ohrwurm_log.py            ingest the latest ohrwurm run's records
    python ohrwurm_log.py --show     print the register standing

Construction (printed here and in the register's envelope): SHA-256 over the
UTF-8 bytes of the statement, exactly as ohrwurm.seal_records emits it. The
limit rides every statement by design: FIRST IN THIS CORPUS IS NOT FIRST IN
THE WORLD.

The forward channel — crossing CALLS with a probability and a deadline
("this phrasing reaches the other side within N days") — issues into the main
ledger as arm ohrwurm/propagation through the same gate every arm faces, and
switches on when the operator names live phrases. This register is the
retrospective half; the ledger arm is the predictive half. Nothing here writes
the ledger.
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE / "docs" / "ohrwurm_register.json"

ENVELOPE = {
    "schema": "ohrwurm-register/1.0",
    "construction": "SHA-256 over the UTF-8 bytes of the statement, verbatim",
    "charter": "Origin claims from the Ohrwurm propagation instrument, "
               "append-only, deduped by hash. First in this corpus is not "
               "first in the world. Anchored by the public commit history of "
               "this repository (RPAS 4.04-shaped); the commit date is the "
               "claim's existence proof.",
    "forward_channel": "Crossing calls with probability and deadline issue "
                       "into ledger.json as arm ohrwurm/propagation via the "
                       "standard gate; see this file's generator docstring.",
}


def load() -> dict:
    if REGISTER.exists():
        return json.loads(REGISTER.read_text(encoding="utf-8"))
    return {**ENVELOPE, "records": []}


def save(doc: dict):
    doc["as_of"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    REGISTER.write_text(json.dumps(doc, ensure_ascii=False, indent=2),
                        encoding="utf-8")


def ingest() -> int:
    sidecar = HERE / "forecasts" / "ohrwurm_records_latest.json"
    if not sidecar.exists():
        print("no sidecar at forecasts/ohrwurm_records_latest.json — run an "
              "ohrwurm pass first (it writes the sidecar at seal_records). "
              "Nothing ingested, nothing guessed.", file=sys.stderr)
        return 1
    recs = json.loads(sidecar.read_text(encoding="utf-8"))
    doc = load()
    have = {r["sha256"] for r in doc["records"]}
    added = 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for r in recs:
        if r["sha256"] in have:
            continue
        stmt = r["statement"]
        if hashlib.sha256(stmt.encode("utf-8")).hexdigest() != r["sha256"]:
            print(f"hash mismatch on emitted record — refused: "
                  f"{r['sha256'][:16]}…", file=sys.stderr)
            continue
        doc["records"].append({"statement": stmt, "sha256": r["sha256"],
                               "logged_at": now})
        added += 1
    save(doc)
    print(f"register: +{added} origin claim(s), {len(doc['records'])} total "
          f"→ {REGISTER.relative_to(HERE)}. Commit it; the commit date is "
          f"the proof.")
    return 0


def show() -> int:
    doc = load()
    print(f"OHRWURM REGISTER — {len(doc['records'])} origin claim(s), "
          f"as of {doc.get('as_of', '—')}")
    for r in doc["records"][-8:]:
        print(f"  {r['sha256'][:16]}… · {r['logged_at']} · "
              f"{r['statement'][:90]}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--show", action="store_true")
    a = ap.parse_args()
    return show() if a.show else ingest()


if __name__ == "__main__":
    sys.exit(main())
