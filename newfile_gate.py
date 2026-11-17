#!/usr/bin/env python3
"""newfile_gate.py: stop a publish when a path the desk has never published before is staged.

Runs in publish.bat right after `git add -A`. Files already tracked pass untouched; only
paths that are NEW to the repository are checked. Each one must match a pattern in
newfile_allow.txt (fnmatch, case-sensitive). Anything else stops the publish and is named.

Why: `git add -A` stages whatever sits in the folder. This is the check on what is new.
Exit 0 = pass, exit 1 = stop. Prints paths only.
"""
import fnmatch, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOW = [l.strip() for l in (HERE / "newfile_allow.txt").read_text(encoding="utf-8").splitlines()
         if l.strip() and not l.lstrip().startswith("#")]
out = subprocess.run(["git", "diff", "--cached", "--no-renames", "--name-only", "--diff-filter=A", "-z"],
                     capture_output=True, cwd=HERE).stdout.decode("utf-8", "replace")
new = [p for p in out.split("\0") if p]
unknown = [p for p in new if not any(fnmatch.fnmatchcase(p, a) for a in ALLOW)]
if unknown:
    print("NEW-FILE GATE: these new paths match no known pattern:")
    for p in unknown:
        print("  " + p)
    print("If one belongs on the site, add its pattern to newfile_allow.txt and rerun publish.bat.")
    sys.exit(1)
print(f"NEW-FILE GATE: {len(new)} new path(s), all known.")
