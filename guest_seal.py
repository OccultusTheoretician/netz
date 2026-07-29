#!/usr/bin/env python3
"""
guest_seal.py — ingestion, run by CI only on the operator's `seal` label.

Defense in depth: re-parses and re-gates the issue exactly as guest_gate.py
did (the form may have been edited after the gate passed), then seals via the
one seal implementation (candidate_desk.seal, RPAS 4.02g) and appends to the
canonical ledger under arm guest/<login>, envelope written by kkr.save_ledger,
served copy synced. Prints the confirmation comment to seal_comment.md and the
sealed id to stdout. The workflow commits; this script does not touch git.

Env in: ISSUE_BODY, ISSUE_AUTHOR, ISSUE_NUMBER, AUTHOR_CREATED_AT,
OPEN_GUEST_COUNT (pass 0 at seal time; the open-cap governs submission, not
sealing).
"""

import json
import os
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

import guest_gate
import kkr
from candidate_desk import seal

HERE = Path(__file__).resolve().parent


def main() -> int:
    # Re-run the full gate on the current body. A post-gate edit fails here.
    rc = guest_gate.main()
    if rc != 0:
        return rc
    verdict = json.loads((HERE / "gate_verdict.json").read_text(
        encoding="utf-8"))
    if not verdict["accept"]:
        (HERE / "seal_comment.md").write_text(
            "**NOT SEALED.** The submission no longer passes the gate — it "
            "was edited after the gate verdict, or policy state moved. The "
            "gate's reasons are posted above this comment. Nothing was "
            "written.\n", encoding="utf-8")
        print("seal: REFUSED — gate no longer passes", file=sys.stderr)
        return 1

    p = verdict["parsed"]
    author = verdict["author"]
    issue = os.environ.get("ISSUE_NUMBER", "?")
    now = datetime.now(timezone.utc)

    data = kkr.load_ledger()
    rows = data["projections"]
    today_tag = now.strftime("%Y%m%d")
    n = 1 + sum(1 for e in rows
                if str(e.get("id", "")).startswith(f"GK-{today_tag}-"))
    entry = {
        "id": f"GK-{today_tag}-{n:02d}",
        "date_issued": now.strftime("%Y-%m-%d"),
        "deadline": p["deadline"],
        "statement": p["statement"],
        "resolution": p["resolution"],
        "probability": int(p["probability"]),
        "failure_condition": p["failure_condition"],
        "keyed_keyless": p["keyed_keyless"],
        "keyed_keyless_rationale": p["keyed_keyless_rationale"],
        "status": "open",
        "model": f"guest/{author}",
        "resolved_date": None,
        "audit": None,
        "notes": f"guest kall via issue #{issue}",
    }
    seal(entry)
    rows.append(entry)
    kkr.save_ledger(data)
    shutil.copy(HERE / "ledger.json", HERE / "docs" / "ledger.json")

    verify = ("python rpas_verify.py https://raw.githubusercontent.com/"
              "OccultusTheoretician/netz/main/docs/ledger.json")
    (HERE / "seal_comment.md").write_text(
        f"**SEALED.** `{entry['id']}` · arm `guest/{author}` · "
        f"p={entry['probability']}% · deadline {entry['deadline']} · "
        f"{entry['keyed_keyless']}\n\n"
        f"seal_sha256 `{entry['seal_sha256']}`\nsealed_at {entry['sealed_at']}"
        f"\n\nYour forecast is on the public record before its outcome "
        f"exists. Anyone verifies it, and every figure this desk publishes, "
        f"with:\n\n```\n{verify}\n```\n\nIt resolves on its stated basis at "
        f"the deadline — hit or miss, under your login, permanently. "
        f"Welcome to the record.\n", encoding="utf-8")
    print(entry["id"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
