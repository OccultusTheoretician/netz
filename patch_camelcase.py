#!/usr/bin/env python3
"""
patch_camelcase.py — NebelKraehe, camel-cased, everywhere.

The mark's name appears across the site in a dozen encodings: NebelKrähe,
NebelKr&auml;he, NebelKr&#228;he, nebelKrähe, NEBELKRÄHE. This normalises the K
in all of them while preserving the surrounding case convention and the HTML
entity form, so a page that used an entity keeps using one.

Deliberately NOT touched: sealed records. Anything under a hashlog, a vault, a
reveal, or ledger.json is left alone — the string may sit inside a committed
preimage, and rewriting a sealed statement to fix a capital letter would break
the seal for the whole set. Cosmetics never outrank a commitment.

  python patch_camelcase.py [repo-root]     default C:\\netz
  python patch_camelcase.py --dry           report only

Idempotent.
"""
import re, sys
from pathlib import Path

ROOT = Path([a for a in sys.argv[1:] if not a.startswith("--")][0]) \
       if [a for a in sys.argv[1:] if not a.startswith("--")] else Path(r"C:\netz")
DRY = "--dry" in sys.argv

SKIP_NAMES = ("hashlog", "vault", "reveal", "campaign", "ledger.json",
              "_projections.json", "pre_rpas")
EXTS = (".html", ".css", ".js", ".md", ".py", ".json", ".yml", ".yaml", ".bat", ".txt")

# every spelling seen in the tree -> its camel-cased form, case convention kept
PAIRS = [
    ("Nebelkr\u00e4he", "NebelKr\u00e4he"),
    ("nebelkr\u00e4he", "nebelKr\u00e4he"),
    ("NebelKr&auml;he", "NebelKr&auml;he"),
    ("nebelKr&auml;he", "nebelKr&auml;he"),
    ("NebelKr&#228;he", "NebelKr&#228;he"),
    ("NebelKraehe", "NebelKraehe"),
    ("nebelKraehe", "nebelKraehe"),
    ("NEBELKR\u00c4HE", "NEBELKR\u00c4HE"),      # already unambiguous in caps
]


def skip(p: Path) -> bool:
    n = p.name.lower()
    return any(s in n for s in SKIP_NAMES) or ".git" in p.parts


def main():
    if not ROOT.exists():
        print(f"FAIL — no such directory: {ROOT}"); return 1
    total, files = 0, []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXTS or skip(p):
            continue
        try:
            s = orig = p.read_text(encoding="utf-8")
        except Exception:
            continue
        n = 0
        for a, b in PAIRS:
            if a == b:
                continue
            c = s.count(a)
            if c:
                s = s.replace(a, b); n += c
        if n and s != orig:
            files.append((p, n)); total += n
            if not DRY:
                p.write_text(s, encoding="utf-8")
    if not files:
        print("Nothing to change — already camel-cased.")
        return 0
    for p, n in files:
        print(f"  {'would fix' if DRY else 'fixed'} {n:>3}  {p.relative_to(ROOT)}")
    print(f"\n  {total} occurrence(s) across {len(files)} file(s)"
          + ("  [dry run, nothing written]" if DRY else ""))
    print("\n  Sealed records were skipped by name: hashlog, vault, reveal, campaign,")
    print("  ledger.json. A capital letter is not worth breaking a commitment over.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
