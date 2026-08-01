#!/usr/bin/env python3
"""whatnow.py - the one status command. What needs YOU, and nothing else.

Three tiers, deliberately separated so the standing work does not read like
a daily chore:

  NEEDS YOU TODAY   things blocking, with the exact command
  STANDING          real backlog, no deadline pressure, reported not nagged
  CLEAR             what is already done, so the absence of a line means
                    "handled", not "forgotten"

Reads only. Writes nothing, resolves nothing, seals nothing.

    python whatnow.py
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEDGER = HERE / "ledger.json"
SEAL_CUTOVER = "2026-07-30"


def _git(*args):
    try:
        r = subprocess.run(["git", "-C", str(HERE)] + list(args),
                           capture_output=True, text=True, timeout=30)
        return r.stdout.strip() if r.returncode == 0 else None
    except Exception:
        return None


def main():
    today = datetime.now(timezone.utc).date()
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["projections"]

    def empty(v):
        v = str(v or "").strip()
        return not v or v.lower().startswith("unset")

    openr = [p for p in rows if p.get("status") == "open"]
    overdue, unsealed, nofc, nokeys = [], [], [], []
    for p in openr:
        try:
            if datetime.strptime(p["deadline"], "%Y-%m-%d").date() < today:
                overdue.append(p)
        except Exception:
            pass
        if empty(p.get("failure_condition")):
            nofc.append(p)
        if empty(p.get("keyed_keyless")):
            nokeys.append(p)
        if not p.get("seal_sha256") and str(p.get("date_issued", "")) >= SEAL_CUTOVER:
            unsealed.append(p)

    keysoon = sorted(
        (p for p in nokeys
         if (datetime.strptime(p["deadline"], "%Y-%m-%d").date() - today).days <= 30),
        key=lambda p: p["deadline"])

    dirty = _git("status", "--porcelain")
    local = _git("rev-parse", "HEAD")
    _git("fetch", "--quiet", "origin")
    remote = _git("rev-parse", "origin/main")
    ahead = local and remote and local != remote

    todo = []
    if nofc:
        todo.append((f"{len(nofc)} open row(s) have no failure condition - unsealable",
                     "python fc_pass.py --draft   (read FC_REVIEW.md)\n"
                     "     then: python fc_pass.py --apply all"))
    if overdue:
        ids = ", ".join(p["id"] for p in overdue[:6])
        todo.append((f"{len(overdue)} row(s) past deadline: {ids}",
                     "python kkr.py --jury-run        (or --resolve to rule alone)"))
    if keysoon:
        ids = ", ".join(p["id"] for p in keysoon[:6])
        todo.append((f"{len(keysoon)} row(s) resolve within 30 days with NO keyed/keyless - "
                     "each becomes KEYED by rule (4.03) if left",
                     f"decide and set: {ids}"))
    if dirty or ahead:
        what = "uncommitted changes" if dirty else "local commits not pushed"
        todo.append((f"{what} - the site is behind your work",
                     "publish.bat"))

    print()
    print("=" * 68)
    print(f"  WHAT NEEDS YOU - {today.isoformat()}")
    print("=" * 68)
    if todo:
        for i, (what, cmd) in enumerate(todo, 1):
            print(f"\n  {i}. {what}")
            for line in cmd.split("\n"):
                print(f"     {line}")
    else:
        print("\n  Nothing. The book is current and the site matches it.")

    print("\n" + "-" * 68)
    print("  STANDING (no deadline - not today's problem)")
    print("-" * 68)
    later = [p for p in nokeys if p not in keysoon]
    print(f"    keyed/keyless undetermined ...... {len(nokeys):>4} open row(s)"
          f"  ({len(later)} not due within 30d)")
    print( "                                        your judgment by rule - no script holds priors")
    if unsealed:
        print(f"    post-cutover rows unsealed ...... {len(unsealed):>4}")

    print("\n" + "-" * 68)
    print("  CLEAR")
    print("-" * 68)
    print(f"    ledger .......... {len(rows)} rows · {len(openr)} open · "
          f"{sum(1 for p in rows if p['status'] in ('hit','miss'))} resolved · "
          f"{sum(1 for p in rows if p['status']=='void')} void")
    if not nofc:
        print( "    failure conditions ....... every open row falsifiable")
    if not overdue:
        print( "    deadlines ................ nothing past due")
    if not dirty and not ahead:
        print( "    published ................ site matches the working tree")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
