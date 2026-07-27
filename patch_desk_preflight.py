#!/usr/bin/env python3
"""
patch_desk_preflight.py — stop the pre-flight crying wolf.

`desk.py ship` runs verify first, and verify warned on two conditions that are
the NORMAL state immediately before a ship: an uncommitted working tree and a
local HEAD ahead of the remote. Those are exactly what shipping resolves. A
checker that warns on every pass of the happy path trains its operator to
ignore warnings, and then it fails silently the day one is real.

After this, inside `ship` those two report as INFO. A tree that is BEHIND the
remote still warns, because that one matters. Standalone `verify` and `status`
are unchanged — there the warnings tell you something.

  python patch_desk_preflight.py [path-to-desk.py]     default C:\\netz\\desk.py

Idempotent.
"""
import shutil, sys
from datetime import datetime
from pathlib import Path

T = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz\desk.py")

OLD_A = '''def check_remote():
    rc, local, _ = git("rev-parse", "HEAD")
    rc2, ls, _ = git("ls-remote", "origin", "main")
    if rc or rc2 or not ls:
        return "skip", "remote unreachable"
    remote = ls.split()[0]
    return ("pass", f"in sync at {local[:7]}") if local == remote else \\
           ("warn", f"local {local[:7]} != remote {remote[:7]} — unpushed or behind")


def check_dirty():
    rc, out, _ = git("status", "--porcelain")
    if rc:
        return "skip", "git not available"
    n = len([l for l in out.splitlines() if l.strip()])
    return ("pass", "clean") if n == 0 else ("warn", f"{n} uncommitted change(s)")
'''
NEW_A = '''PREFLIGHT = False   # True only while ship() is checking itself


def check_remote():
    rc, local, _ = git("rev-parse", "HEAD")
    rc2, ls, _ = git("ls-remote", "origin", "main")
    if rc or rc2 or not ls:
        return "skip", "remote unreachable"
    remote = ls.split()[0]
    if local == remote:
        return "pass", f"in sync at {local[:7]}"
    # ahead is the normal pre-ship state; behind is not
    rc3, cnt, _ = git("rev-list", "--count", f"{remote}..{local}")
    ahead = cnt.isdigit() and int(cnt) > 0
    if PREFLIGHT and ahead:
        return "info", f"local {local[:7]} is ahead of origin — which is what shipping is for"
    return "warn", f"local {local[:7]} != remote {remote[:7]} — unpushed or behind"


def check_dirty():
    rc, out, _ = git("status", "--porcelain")
    if rc:
        return "skip", "git not available"
    n = len([l for l in out.splitlines() if l.strip()])
    if n == 0:
        return "pass", "clean"
    if PREFLIGHT:
        return "info", f"{n} change(s) staged for this ship"
    return "warn", f"{n} uncommitted change(s)"
'''

OLD_B = '''            mark = {"pass": ok("PASS"), "fail": bad("FAIL"),
                    "warn": warn("WARN"), "skip": dim("SKIP")}[state]'''
NEW_B = '''            mark = {"pass": ok("PASS"), "fail": bad("FAIL"),
                    "warn": warn("WARN"), "skip": dim("SKIP"),
                    "info": dim("INFO")}[state]'''

OLD_C = '''    if not msg:
        print(bad("FAIL — a commit message is required:  python desk.py ship -m \\"...\\""))
        return 1
    failed = run_verify()'''
NEW_C = '''    if not msg:
        print(bad("FAIL — a commit message is required:  python desk.py ship -m \\"...\\""))
        return 1
    globals()["PREFLIGHT"] = True
    failed = run_verify()
    globals()["PREFLIGHT"] = False'''

PATCHES = [("preflight-aware git checks", OLD_A, NEW_A),
           ("INFO row rendering", OLD_B, NEW_B),
           ("ship sets preflight", OLD_C, NEW_C)]


def main():
    if not T.exists():
        print(f"FAIL — no such file: {T}"); return 1
    with open(T, encoding="utf-8", newline="") as f:
        raw = f.read()
    crlf = "\r\n" in raw
    src = raw.replace("\r\n", "\n")
    if "PREFLIGHT" in src:
        print("ALREADY PATCHED — nothing written."); return 0
    missing = [n for n, o, _ in PATCHES if src.count(o) != 1]
    if missing:
        print("FAIL — anchors not found exactly once, nothing written:")
        for m in missing:
            print(f"  · {m}")
        return 1
    for n, o, x in PATCHES:
        src = src.replace(o, x, 1)
    compile(src, str(T), "exec")
    b = Path(__file__).resolve().parent / f"desk_BEFORE_preflight_{datetime.now():%Y-%m-%d_%H%M%S}.py"
    shutil.copy2(T, b)
    with open(T, "w", encoding="utf-8", newline="") as f:
        f.write(src.replace("\n", "\r\n") if crlf else src)
    for n, _, _ in PATCHES:
        print(f"  applied · {n}")
    print(f"\nbackup  → {b}\npatched → {T}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
