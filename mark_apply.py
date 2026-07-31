#!/usr/bin/env python3
"""
mark_apply.py — point every surface at the new mark. Idempotent; safe to re-run.

The mark previously existed in four incompatible forms: docs/crow.png referenced
by hand-written pages, a base64 PNG embedded inside netz.py's CROW_SVG constant
and baked into every generated page, a favicon link, and an og:image. Four copies
means four things that can drift, which is the failure this repo has now hit
three times on other files. After this, there is one file.

  python mark_apply.py [repo-root]      default C:\\netz

Changes
  docs/*.html   <img src="crow.png">            -> crow_mark.svg
                <link rel=icon href=crow.png>   -> crow_mark.svg, plus
                                                   apple-touch-icon
                og:image                        -> og_nebelkraehe.png
  netz.py       CROW_SVG base64 blob            -> <img src="crow_mark.svg">
                desknav crow.png                -> crow_mark.svg

crow.png is left on disk. It is the original artwork and nothing should delete it.
"""

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\netz")
DOCS = ROOT / "docs"

ICON_BLOCK = (
    '<link rel="icon" type="image/svg+xml" href="crow_mark.svg">\n'
    '<link rel="alternate icon" type="image/png" href="favicon.png">\n'
    '<link rel="apple-touch-icon" href="apple-touch-icon.png">'
)


def patch_html(p: Path):
    s = orig = p.read_text(encoding="utf-8")
    # masthead image
    s = s.replace('<img src="crow.png"', '<img src="crow_mark.svg"')
    s = s.replace("<img src='crow.png'", "<img src='crow_mark.svg'")
    s = re.sub(r'<img([^>]*?)src="crow\.png"', r'<img\1src="crow_mark.svg"', s)
    # favicon: replace the whole old link, once, with the full icon block
    if "apple-touch-icon" not in s:
        s = re.sub(r'<link rel="icon"[^>]*href="crow\.png"\s*/?>', ICON_BLOCK, s, count=1)
    # social card
    s = s.replace("https://retroprescientaudit.com/crow.png",
                  "https://retroprescientaudit.com/og_nebelkraehe.png")
    s = s.replace('name="twitter:card" content="summary"',
                  'name="twitter:card" content="summary_large_image"')
    if s != orig:
        p.write_text(s, encoding="utf-8")
        return True
    return False


def patch_netz(p: Path):
    s = orig = p.read_text(encoding="utf-8")
    # the embedded base64 mark: ~40 KB baked into every generated page
    s = re.sub(r"CROW_SVG = '''<img class=\"crow-mark\"[^\n]*?'''",
               "CROW_SVG = '''<img class=\"crow-mark\" alt=\"NebelKr&auml;he\" "
               "src=\"crow_mark.svg\"/>'''", s, count=1, flags=re.S)
    s = s.replace('<img src="crow.png" alt=""', '<img src="crow_mark.svg" alt=""')
    # the generated pages' own <head> icon link, single-quoted inside an f-string
    s = s.replace(
        "f\"<link rel='icon' type='image/png' href='crow.png'>\"",
        "f\"<link rel='icon' type='image/svg+xml' href='crow_mark.svg'>\"\n"
        "            f\"<link rel='apple-touch-icon' href='apple-touch-icon.png'>\"")
    if s != orig:
        p.write_text(s, encoding="utf-8")
        return True
    return False


def main():
    if not DOCS.exists():
        print(f"FAIL — no docs directory at {DOCS}")
        return 1
    need = ["crow_mark.svg", "crow_mark_square.svg", "favicon.png",
            "apple-touch-icon.png", "og_nebelkraehe.png", "crow_mark_512.png"]
    missing = [n for n in need if not (DOCS / n).exists()]
    if missing:
        print("FAIL — these assets are not in docs/ yet:")
        for m in missing:
            print(f"  · {m}")
        return 1

    changed = []
    for p in sorted(DOCS.glob("*.html")):
        if patch_html(p):
            changed.append(p.name)
    netz = ROOT / "netz.py"
    if netz.exists() and patch_netz(netz):
        changed.append("netz.py")

    if not changed:
        print("Nothing to change — already applied.")
    else:
        for c in changed:
            print(f"  updated · {c}")
    print("\nGenerated pages (kkr.html, ledger.html, report.html) carry the mark from "
          "netz.py, so they pick it up on the next render:\n  python kkr.py --score")
    return 0


if __name__ == "__main__":
    sys.exit(main())
