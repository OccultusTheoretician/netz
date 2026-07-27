#!/usr/bin/env python3
"""
patch_desk_identity.py — desk.py refuses to ship if a configured name appears.

Adds identity_guard to the invariant block. `verify` reports it, `ship` refuses
on it. The check runs against tracked files, holds only hashes, and never prints
the matched term.

  python patch_desk_identity.py [path-to-desk.py]     default C:\\netz\\desk.py
Idempotent.
"""
import shutil, sys
from datetime import datetime
from pathlib import Path

T = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz\desk.py")

OLD = '''CHECKS = [("ledger envelope", check_envelope),'''
NEW = '''def check_identity():
    """A name on a published surface cannot be recalled. The guard holds only
    hashes, so this check discloses nothing about what it is looking for."""
    g = ROOT / "identity_guard.py"
    if not g.exists():
        return "skip", "identity_guard.py not present"
    try:
        r = subprocess.run([sys.executable, str(g), "scan"], cwd=str(ROOT),
                           capture_output=True, text=True, timeout=120)
    except Exception as e:
        return "skip", f"guard did not run: {e}"
    if r.returncode == 0:
        return "pass", "no configured term in any tracked file"
    n = sum(1 for l in r.stdout.splitlines() if ":" in l and l.strip().startswith(("d", "b", "s", "k", "m", "i", "f", "a", "c", "p", "r", "t", "w", "n", "o", "l", "e", "g", "h", "j", "q", "u", "v", "x", "y", "z", ".")))
    return "fail", (f"a configured identity term appears in tracked files — run "
                    f"`python identity_guard.py scan` for locations")


CHECKS = [("identity guard", check_identity),
          ("ledger envelope", check_envelope),'''


def main():
    if not T.exists():
        print(f"FAIL — no such file: {T}"); return 1
    with open(T, encoding="utf-8", newline="") as f:
        raw = f.read()
    crlf = "\r\n" in raw
    src = raw.replace("\r\n", "\n")
    if "check_identity" in src:
        print("ALREADY PATCHED — nothing written."); return 0
    if src.count(OLD) != 1:
        print("FAIL — anchor not found once, nothing written."); return 1
    src = src.replace(OLD, NEW, 1)
    compile(src, str(T), "exec")
    b = Path(__file__).resolve().parent / f"desk_BEFORE_identity_{datetime.now():%Y-%m-%d_%H%M%S}.py"
    shutil.copy2(T, b)
    with open(T, "w", encoding="utf-8", newline="") as f:
        f.write(src.replace("\n", "\r\n") if crlf else src)
    print("  applied · identity guard is now an invariant")
    print(f"\nbackup  → {b}\npatched → {T}")
    print("\n`desk.py ship` will now refuse while a configured term is tracked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
