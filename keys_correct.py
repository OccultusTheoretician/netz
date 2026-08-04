#!/usr/bin/env python3
"""
keys_correct.py — CORRECT A DETERMINATION WITHOUT ERASING IT

    python keys_correct.py FILE.json            report, write nothing
    python keys_correct.py FILE.json --apply     write

WHY THIS IS NOT AN IMPORT

    `kkr.py --keys-import` refuses any row that already carries a
    determination: "already determined - sealed rows are not edited." That is
    the correct refusal. A determination that can be quietly re-imported is a
    determination that can be quietly retrofitted after seeing how a row was
    heading, which is the single attack the keyed/keyless split exists to make
    detectable.

    So a correction cannot be a re-import. It has to be an explicit act that
    leaves both values on the record. RPAS-26 5.07: where a defect is found
    after publication, the desk must "mark - never remove - the affected
    claims. Retractions stay in the record."

WHAT IT WRITES

    On each corrected row, alongside the new `keyed_keyless`:

        keyed_keyless_superseded    the ruling this replaces
        keyed_keyless_corrected     UTC date of the correction
        keyed_keyless_correction    why, in full
        keyed_keyless_authority     who ruled it and under what

    Nothing is deleted. A reader sees that the row was ruled one way, then
    another, and why — which is strictly more information than a row that was
    only ever ruled once.

CORRECTION FILE FORMAT

    {"issued": "2026-08-04",
     "authority": "...",
     "reason": "...",
     "rows": {"KKR-...": {"to": "keyed", "why": "..."}, ...}}
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"


def main():
    ap = argparse.ArgumentParser(description="correct keyed/keyless determinations")
    ap.add_argument("correction", help="correction JSON")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--ledger", default=str(LEDGER))
    a = ap.parse_args()

    cf = Path(a.correction)
    if not cf.exists():
        sys.exit(f"no correction file at {cf}")
    corr = json.loads(cf.read_text(encoding="utf-8"))
    led = Path(a.ledger)
    data = json.loads(led.read_text(encoding="utf-8"))
    index = {p["id"]: p for p in data["projections"]}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    errs, staged = [], []
    for rid, rec in corr.get("rows", {}).items():
        p = index.get(rid)
        to = str(rec.get("to", "")).strip().lower()
        why = str(rec.get("why", "")).strip()
        if p is None:
            errs.append(f"{rid}: not in the ledger"); continue
        if to not in ("keyed", "keyless"):
            errs.append(f"{rid}: '{to}' is not keyed or keyless"); continue
        if not why:
            errs.append(f"{rid}: no reason - a correction without a stated "
                        f"reason is an edit"); continue
        cur = str(p.get("keyed_keyless", "")).strip().lower()
        if cur == to:
            errs.append(f"{rid}: already {to} - nothing to correct"); continue
        if p.get("keyed_keyless_superseded"):
            errs.append(f"{rid}: already carries a correction "
                        f"({p['keyed_keyless_superseded']} -> "
                        f"{p['keyed_keyless']}). A second correction to one "
                        f"determination needs its own ruling, not this file.")
            continue
        staged.append((p, cur, to, why))

    if errs:
        print(f"\n{len(errs)} problem(s). NOTHING WRITTEN:\n", file=sys.stderr)
        for e in errs:
            print(f"  {e}", file=sys.stderr)
        return 2

    print(f"\n{'APPLY' if a.apply else 'REPORT ONLY'} — "
          f"{len(staged)} correction(s)\n")
    for p, cur, to, why in staged:
        print(f"  {p['id']:<18} {p.get('model','?'):<26} {cur} -> {to}")
    print(f"\n  issued    {corr.get('issued', today)}")
    print(f"  authority {corr.get('authority', '(unstated)')}")
    print(f"  reason    {corr.get('reason', '(unstated)')[:120]}")

    if not a.apply:
        print("\n  Nothing written. Re-run with --apply.")
        return 0

    shutil.copy2(led, led.with_suffix(".json.precorrection.bak"))
    for p, cur, to, why in staged:
        p["keyed_keyless_superseded"] = cur
        p["keyed_keyless"] = to
        p["keyed_keyless_corrected"] = today
        p["keyed_keyless_correction"] = why
        p["keyed_keyless_authority"] = corr.get("authority", "")
    led.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"\n  {len(staged)} corrected. Superseded values retained on every "
          f"row (5.07).")
    print(f"  backup -> {led.with_suffix('.json.precorrection.bak').name}")
    print(f"\n  Re-render the faces:  python kkr.py --score")
    return 0


if __name__ == "__main__":
    sys.exit(main())
