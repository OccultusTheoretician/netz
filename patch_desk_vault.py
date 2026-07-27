#!/usr/bin/env python3
"""
patch_desk_vault.py — teach desk.py that FogSim campaign files are vault-tier.

fogsim_campaign.json holds the seeds and salts of UNOPENED runs. Publishing it
before reveal lets anyone compute the outcomes of runs that have not been
disclosed, which destroys the hiding property of the whole campaign — the same
failure class as publishing a Kalls vault.

.gitignore covers it today. This adds it to the invariant, because a gitignore
is a convenience and `desk.py verify` is the check.

  python patch_desk_vault.py [path-to-desk.py]     default C:\\netz\\desk.py

Idempotent.
"""
import shutil, sys
from datetime import datetime
from pathlib import Path

T = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz\desk.py")

OLD = 'VAULT_PATTERNS = ["kalls_vault", "kalls_rescue", "_VAULT.md", "vault/"]'
NEW = ('# Anything holding opening material for something not yet revealed.\n'
       'VAULT_PATTERNS = ["kalls_vault", "kalls_rescue", "_VAULT.md", "vault/",\n'
       '                  "fogsim_campaign", "_campaign.json"]')


def main():
    if not T.exists():
        print(f"FAIL — no such file: {T}"); return 1
    with open(T, encoding="utf-8", newline="") as f:
        raw = f.read()
    crlf = "\r\n" in raw
    src = raw.replace("\r\n", "\n")
    if "fogsim_campaign" in src:
        print("ALREADY PATCHED — nothing written."); return 0
    if src.count(OLD) != 1:
        print("FAIL — VAULT_PATTERNS not found in the expected form, nothing written.")
        return 1
    src = src.replace(OLD, NEW, 1)
    compile(src, str(T), "exec")
    b = Path(__file__).resolve().parent / f"desk_BEFORE_vault_{datetime.now():%Y-%m-%d_%H%M%S}.py"
    shutil.copy2(T, b)
    with open(T, "w", encoding="utf-8", newline="") as f:
        f.write(src.replace("\n", "\r\n") if crlf else src)
    print("  applied · fogsim campaign files are vault-tier")
    print(f"\nbackup  → {b}\npatched → {T}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
