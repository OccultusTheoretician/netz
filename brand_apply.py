#!/usr/bin/env python3
"""
brand_apply.py — wire brand.css and brand.js into every served page.

Additive and idempotent. No page markup is rewritten beyond two lines in the
head; if either file fails to load the pages render exactly as they do today.
KriegForeKaster.html is skipped by design — it is a full-viewport instrument
with its own layout contract, and a fixed background layer underneath it would
fight the map.

  python brand_apply.py [repo-root]      default C:\\netz

Also patches netz.py so the generated faces (kkr, ledger, report) pick it up on
the next render, and reports any image in docs/ that nothing references.
"""

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz")
DOCS = ROOT / "docs"
# KriegForeKaster.html links brand.css itself and is no longer skipped: the
# field sits at z-index:-1 behind a full-viewport layout, which works.
# kkr.html, ledger.html and report.html are BUILD PRODUCTS of netz.py, which
# this script also patches. Wiring both ends makes the served copy differ from
# the canonical render until the next build — which is exactly the drift
# `desk.py verify` exists to catch, and it caught it. They inherit from netz.py.
SKIP = {"kkr.html", "ledger.html", "report.html"}

# documented in MARK.md as downloadable assets, not page references
INTENTIONAL = {"crow_mark_512.png", "crow_mark_square.svg", "og_nebelkraehe.png"}

BLOCK = ('<link rel="stylesheet" href="brand.css">\n'
         '<script defer src="brand.js"></script>')


def patch_html(p: Path):
    s = orig = p.read_text(encoding="utf-8")
    if "brand.css" in s:
        return False
    if "</head>" in s:
        s = s.replace("</head>", BLOCK + "\n</head>", 1)
    else:                                   # headless fragment: prepend
        s = BLOCK + "\n" + s
    if s != orig:
        p.write_text(s, encoding="utf-8")
        return True
    return False


def patch_netz(p: Path):
    s = orig = p.read_text(encoding="utf-8")
    if "brand.css" in s:
        return False
    anchors = [
        "f\"<link rel='icon' type='image/svg+xml' href='crow_mark.svg'>\"",
        "f\"<link rel='icon' type='image/png' href='crow.png'>\"",
    ]
    add = ("\n            f\"<link rel='stylesheet' href='brand.css'>\""
           "\n            f\"<script defer src='brand.js'></script>\"")
    for a in anchors:
        if a in s:
            s = s.replace(a, a + add, 1)
            break
    if s != orig:
        p.write_text(s, encoding="utf-8")
        return True
    return False


def orphan_images():
    if not DOCS.exists():
        return []
    text = ""
    for p in list(DOCS.glob("*.html")) + list(DOCS.glob("*.css")) + \
             list(DOCS.glob("*.js")) + list(DOCS.glob("*.md")):
        try:
            text += p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            pass
    for extra in (ROOT / "netz.py", ROOT / "kkr.py"):
        if extra.exists():
            text += extra.read_text(encoding="utf-8", errors="ignore")
    out = []
    for img in DOCS.iterdir():
        if img.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"):
            if img.name in INTENTIONAL:
                continue
            if img.name not in text:
                out.append((img.name, img.stat().st_size))
    return sorted(out, key=lambda t: -t[1])


def main():
    if not DOCS.exists():
        print(f"FAIL — no docs directory at {DOCS}")
        return 1
    for need in ("brand.css", "brand.js"):
        if not (DOCS / need).exists():
            print(f"FAIL — {need} is not in docs/ yet")
            return 1

    changed = []
    for p in sorted(DOCS.glob("*.html")):
        if p.name in SKIP:
            continue
        if patch_html(p):
            changed.append(p.name)
    netz = ROOT / "netz.py"
    if netz.exists() and patch_netz(netz):
        changed.append("netz.py")

    if changed:
        for c in changed:
            print(f"  wired · {c}")
    else:
        print("Nothing to change — already applied.")

    orphans = orphan_images()
    if orphans:
        print("\n  Images in docs/ that nothing references:")
        total = 0
        for name, size in orphans:
            print(f"    {name:26s} {size:>9,} bytes")
            total += size
        print(f"    {'':26s} {total:>9,} bytes served for nothing")
        print("  Assets documented in MARK.md as downloads are not listed here.")

    print("\n  Generated faces pick this up on the next: python kkr.py --score")
    return 0


if __name__ == "__main__":
    sys.exit(main())
