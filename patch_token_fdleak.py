#!/usr/bin/env python3
"""patch_token_fdleak.py — report-only by default, --apply writes.

First live token run, first Windows-only defect: tempfile.mkstemp returns an
OPEN file descriptor alongside the path. The code kept the path, leaked the
descriptor, and Windows then refused the unlink (WinError 32) because the
process still held its own file open. Linux tolerates deleting an open file,
which is why the pattern survived every container test. The descriptor is now
closed before the file is used.
"""
import argparse
from pathlib import Path

OLD = (b'    tmp = Path(tempfile.mkstemp(suffix=".served.json")[1]); '
       b'tmp.write_bytes(served)')
NEW = (b'    _fd, _p = tempfile.mkstemp(suffix=".served.json")\n'
       b'    os.close(_fd)  # Windows: an open descriptor blocks the later unlink\n'
       b'    tmp = Path(_p); tmp.write_bytes(served)')
MARK = b'os.close(_fd)'

OLD_IMP = b'    import subprocess, tempfile, urllib.request, urllib.error\n'
NEW_IMP = b'    import os, subprocess, tempfile, urllib.request, urllib.error\n'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    p = Path("kalls.py")
    b = p.read_bytes()
    if MARK in b:
        print("OK    kalls.py \u2014 already applied"); return
    if OLD not in b or OLD_IMP not in b:
        print("MISS  kalls.py \u2014 target not found (source drifted?)"); return
    if a.apply:
        p.write_bytes(b.replace(OLD_IMP, NEW_IMP, 1).replace(OLD, NEW, 1))
        print("FIX   kalls.py \u2014 mkstemp descriptor closed before use; unlink now safe on Windows")
    else:
        print("WOULD kalls.py \u2014 close mkstemp descriptor \u2014 rerun with --apply")


if __name__ == "__main__":
    main()
