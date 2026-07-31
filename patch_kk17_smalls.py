#!/usr/bin/env python3
"""patch_kk17_smalls.py -- the two KK17 smalls. Report-only; --apply writes.

  1. F5 NAV RENAME -- the DECC-26 page's nav slot still reads "Verify Seal".
     One string in nav_manifest.json; the restamp across every served page
     rides desk.py ship, which runs navgen before verify by design.
  2. NOTHING-TO-SHIP GATE -- Claude_run.md at d77e59c: patch MISSed twice,
     tree clean, desk.py ship printed ok through a no-op and the only tell
     was the unchanged hash. A35 read the tells at the operator level; the
     shipper itself still tolerated the empty ship (the "nothing to commit"
     pass-through exists for legitimate push-only). The gate: clean tree +
     remote in sync = refuse before any git command runs. Clean but ahead
     = push-only, which the tolerant sequence already performs honestly.

CRLF law: needles normalize line endings on read and restore them on write.
FIX prints, or nothing ships.
"""
import argparse
from pathlib import Path

ROOT = Path(".").resolve()

DESK_OLD = (
    b'    globals()["PREFLIGHT"] = True\n'
    b'    failed = run_verify()\n'
)
DESK_NEW = (
    b'    # NOTHING-TO-SHIP GATE (KK17): a ship with no payload prints a\n'
    b'    # message describing work the commit does not contain - the\n'
    b'    # d77e59c class. Clean tree + remote in sync = refuse. Clean but\n'
    b'    # ahead = push-only, which the tolerant sequence below performs.\n'
    b'    _ds, _ = check_dirty()\n'
    b'    _rs, _ = check_remote()\n'
    b'    if _ds == "pass" and _rs == "pass":\n'
    b'        print(bad("\\n  NOTHING TO SHIP \\u2014 working tree clean, '
    b'remote in sync."))\n'
    b'        print(dim("  A message without a payload is the d77e59c '
    b'defect class."))\n'
    b'        print(dim("  Make the change first; FIX prints, or nothing '
    b'ships."))\n'
    b'        return 1\n'
    b'    globals()["PREFLIGHT"] = True\n'
    b'    failed = run_verify()\n'
)
DESK_MARK = b"NOTHING TO SHIP"

NAV_OLD = b'"text": "Verify Seal"'
NAV_NEW = b'"text": "DECC-26"'
NAV_MARK = b'"text": "DECC-26"'

EDITS = [
    ("desk.py", DESK_OLD, DESK_NEW, DESK_MARK,
     "ship refuses clean-tree-in-sync; the d77e59c class closes at the shipper"),
    ("nav_manifest.json", NAV_OLD, NAV_NEW, NAV_MARK,
     "DECC-26 named in its own nav slot; restamp rides the ship's navgen"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    misses = 0
    for path, old, new, mark, note in EDITS:
        p = ROOT / path
        if not p.exists():
            print(f"MISS  {path} - file absent - {note}"); misses += 1; continue
        raw = p.read_bytes()
        crlf = b"\r\n" in raw
        work = raw.replace(b"\r\n", b"\n") if crlf else raw
        if mark in work:
            print(f"OK    {path} - already applied - {note}"); continue
        if work.count(old) != 1:
            print(f"MISS  {path} - needle count {work.count(old)}, need "
                  f"exactly 1 - {note}"); misses += 1; continue
        if a.apply:
            out = work.replace(old, new, 1)
            if crlf:
                out = out.replace(b"\n", b"\r\n")
            p.write_bytes(out)
        print(f"{'FIX  ' if a.apply else 'WOULD'} {path} - {note}"
              + ("  [CRLF kept]" if crlf and a.apply else ""))
    if misses:
        print(f"\n{misses} MISS - a MISS gates the ship. Nothing ships on this.")
    elif not a.apply:
        print("\nreport only - rerun with --apply to write")


if __name__ == "__main__":
    main()
