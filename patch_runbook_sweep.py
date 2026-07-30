#!/usr/bin/env python3
"""
patch_runbook_sweep.py — stop the runbook publishing the terms it screens for.

THE DEFECT
NETZ_OPS_RUNBOOK.md section 10 documents the pre-publication sweep by inlining
its pattern. That pattern is a plaintext list of the descriptors the sweep
exists to catch — the same deny-list defect identity_guard.py was built to
avoid by storing hashes only. On the current tree those terms appear exactly
once each: inside the command that looks for them.

THE FIX (function preserved, terms off the remote)
The pattern moves to identity_sweep.local.txt, which is gitignored. The runbook
keeps the check and reads the pattern from that file, so the sweep still runs
and still documents itself without publishing its own targets.

Terms are NOT added to identity_guard.json. That guard blocks the ship on any
hit, and a place name appears legitimately in feed content — a weather alert
naming a county would block every push. A soft local sweep is the right
instrument for descriptors; the hashed guard stays for names.

Idempotent. Backup written to NETZ_OPS_RUNBOOK.md.bak once.
Run from C:\netz:  python patch_runbook_sweep.py
"""
import shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if not (HERE / "NETZ_OPS_RUNBOOK.md").exists():
    HERE = Path.cwd()

RB = HERE / "NETZ_OPS_RUNBOOK.md"
LOCAL = HERE / "identity_sweep.local.txt"
GI = HERE / ".gitignore"

if not RB.exists():
    sys.exit("NETZ_OPS_RUNBOOK.md not found beside this script or in cwd.")

src = RB.read_text(encoding="utf-8")

if "identity_sweep.local.txt" in src:
    sys.exit("already patched — nothing to do.")

# The line to replace, matched loosely on its distinctive parts so an escaping
# difference does not defeat the patch.
lines = src.split("\n")
hit = [i for i, l in enumerate(lines)
       if "Select-String" in l and "-Pattern" in l and "Select-Object" in l]
if not hit:
    sys.exit("sweep line not found in the runbook — patch by hand.")
if len(hit) > 1:
    sys.exit(f"{len(hit)} candidate sweep lines found — ambiguous, patch by hand.")

i = hit[0]
lines[i] = ('Select-String -Path docs\\*.html,docs\\*.md,*.html,*.md '
            '-Pattern (Get-Content identity_sweep.local.txt -Raw).Trim() '
            '| Select-Object -First 20')

# add a line explaining where the pattern lives, after the code fence that follows
for j in range(i + 1, min(i + 4, len(lines))):
    if lines[j].strip().startswith("```"):
        lines.insert(j + 1, "")
        lines.insert(j + 2,
                     "The pattern lives in `identity_sweep.local.txt`, which is gitignored: a "
                     "runbook that prints the descriptors it screens for publishes exactly what "
                     "it protects. Keep that file local; it is a soft sweep, not the hashed "
                     "guard, because a place name appears legitimately in feed content and "
                     "would block every ship if it entered `identity_guard.json`.")
        break

RB_backup = RB.with_suffix(".md.bak")
shutil.copy2(RB, RB_backup)
RB.write_text("\n".join(lines), encoding="utf-8")
print(f"patched NETZ_OPS_RUNBOOK.md (backup at {RB_backup.name})")

# write the local pattern file if absent
if not LOCAL.exists():
    LOCAL.write_text("Utah|Attila|C:\\\\Users\n", encoding="utf-8")
    print("wrote identity_sweep.local.txt (LOCAL ONLY — must stay gitignored)")
else:
    print("identity_sweep.local.txt already exists — left as is")

# ensure the gitignore rule exists
gi_txt = GI.read_text(encoding="utf-8") if GI.exists() else ""
if "identity_sweep.local.txt" not in gi_txt:
    with GI.open("a", encoding="utf-8") as f:
        if gi_txt and not gi_txt.endswith("\n"):
            f.write("\n")
        f.write("identity_sweep.local.txt\n")
        f.write("*.local.txt\n")
    print("added ignore rules: identity_sweep.local.txt, *.local.txt")
else:
    print("gitignore rule already present")

print()
print("VERIFY BEFORE SHIPPING:")
print('  git check-ignore -v identity_sweep.local.txt      (must print a rule)')
print('  git grep -inw "utah"                              (must print nothing)')
print()
print("COMMIT MESSAGE — do not name the terms; the message is the amplifier,")
print("not the diff. Suggested:")
print('  "runbook: the pre-publication sweep reads its pattern from a local')
print('   file instead of listing it inline - a checker that prints its own')
print('   targets publishes what it screens for"')
