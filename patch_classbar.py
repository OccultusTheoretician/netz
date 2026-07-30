#!/usr/bin/env python3
r"""
patch_classbar.py — retire the classification-style banner.

WHY
`UNCLASSIFIED // OPEN SOURCES` reproduces the US classification banner
convention: marking, double slash, dissemination control. That format is used
by parties holding classification authority, applied to material an authorized
classifier has reviewed. This desk holds none, and the desk's own carrier rule
already forbids the prose version of exactly this — method only, never asserted
affiliation. A banner borrowing that authority sits directly above a standard
whose credibility comes from refusing to overclaim; the two cannot share a page.

REPLACEMENT
    NOTHING CLASSIFIED OR PRIVILEGED
A true scope statement, strictly more informative than the marking it replaces,
and it claims nothing the desk cannot demonstrate.

SCOPE
  kkr.py     4 occurrences (report + ledger headers and footers)
  netz.py    2 occurrences (classbar div, footbar div)
  docs/*.html, forecasts/*.html — already-emitted pages rewritten in place so
  the change is visible before the next generator run.

Idempotent. Backups written once per file. Run from C:\netz:
    python patch_classbar.py
    python patch_classbar.py --text "YOUR WORDING"
"""
import argparse
import shutil
import sys
from pathlib import Path

OLD_VARIANTS = [
    "UNCLASSIFIED // OPEN SOURCES",
    "UNCLASSIFIED//OPEN SOURCES",
    "UNCLASSIFIED &#47;&#47; OPEN SOURCES",
    "Unclassified \u00b7 Open Sources",
    "Unclassified &middot; Open Sources",
    "UNCLASSIFIED \u00b7 OPEN SOURCES",
]
DEFAULT_NEW = "NOTHING CLASSIFIED OR PRIVILEGED"


def patch_file(p: Path, new: str, tag: str):
    try:
        s = p.read_text(encoding="utf-8")
    except Exception:
        return 0
    orig = s
    n = 0
    for old in OLD_VARIANTS:
        if old in s:
            n += s.count(old)
            s = s.replace(old, new)
    if n and s != orig:
        b = p.with_name(p.name + f".bak_{tag}")
        if not b.exists():
            shutil.copy2(p, b)
        p.write_text(s, encoding="utf-8")
    return n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default=DEFAULT_NEW)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    root = Path.cwd()
    new = a.text.strip()

    targets = []
    for name in ("kkr.py", "netz.py"):
        p = root / name
        if p.exists():
            targets.append(p)
    targets += sorted((root / "docs").glob("*.html"))
    targets += sorted((root / "forecasts").glob("*.html"))
    targets += sorted(root.glob("*.md"))
    targets += sorted((root / "forecasts").glob("*.md"))

    if a.check:
        total = 0
        for p in targets:
            try:
                s = p.read_text(encoding="utf-8")
            except Exception:
                continue
            c = sum(s.count(o) for o in OLD_VARIANTS)
            if c:
                print(f"  {p.relative_to(root)}: {c}")
                total += c
        print(f"\n  {total} occurrence(s) of the classification banner")
        return 0

    total = 0
    for p in targets:
        n = patch_file(p, new, "classbar")
        if n:
            print(f"  [{n}] {p.relative_to(root)}")
            total += n

    print()
    if total:
        print(f"  replaced {total} occurrence(s) with: {new}")
        print("  generators patched, so it will not regenerate.")
        print("\n  next:  python navgen.py ; python desk.py verify")
    else:
        print("  nothing to replace — already patched, or the wording differs.")
        print("  run with --check to see what is present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
