#!/usr/bin/env python3
"""
patch_site_marks_fix.py - three ruled site fixes, exact-string edits.
Run from C:\\netz. Python 3.10+. Default mode REPORTS; --apply writes.

A. NEST RENAME (ruled 2026-07-30): docs/nest.html H1/title/og:title become
   Kraehe's Nest(TM); "The Prophet Board" survives as subtitle (kicker + H2,
   untouched). nest.html is hand-authored - no generator rewrites it.
B. DECC-26(TM): title + first visible use on the verifier page, applied to
   BOTH verify_disclosure.html (source) and docs/decc.html (render), so no
   decc_install rerun is needed and a rerun changes nothing.
C. CASING: entity-encoded NebelKr&auml;he -> Nebelkr&auml;he in the five
   GENERATOR sources (netz.py x2, banners.py, patch_site_visual.py,
   mark_apply.py). reports/*.html are printed record - deliberately NOT
   touched: the desk repairs generators, not published artifacts.

Every edit is an exact unique string; a target not found prints MISSING and
nothing else in that file is guessed at. Never stages, never commits.
"""
import argparse
import sys
from pathlib import Path

TM = "\u2122"
KN = "Kr\u00e4he's Nest"

EDITS = [
 ("docs/nest.html",
  "<title>The Nest \u2014 federation of committed forecasters</title>",
  f"<title>{KN}{TM} \u2014 federation of committed forecasters</title>"),
 ("docs/nest.html",
  '<meta property="og:title" content="The Prophet Board &middot; The Prescient Desk">',
  f'<meta property="og:title" content="{KN}{TM} &middot; The Prophet Board">'),
 ("docs/nest.html",
  "<h1>The Nest</h1>",
  f"<h1>{KN}{TM}</h1>"),
 ("verify_disclosure.html",
  "<title>Verify a Sealed Disclosure \u2014 DECC-26</title>",
  f"<title>Verify a Sealed Disclosure \u2014 DECC-26{TM}</title>"),
 ("verify_disclosure.html",
  '<div class="kick">DECC-26 \u00b7 Denominator-Committed Evidence</div>',
  f'<div class="kick">DECC-26{TM} \u00b7 Denominator-Committed Evidence</div>'),
 ("docs/decc.html",
  "<title>Verify a Sealed Disclosure \u2014 DECC-26</title>",
  f"<title>Verify a Sealed Disclosure \u2014 DECC-26{TM}</title>"),
 ("docs/decc.html",
  '<div class="kick">DECC-26 \u00b7 Denominator-Committed Evidence</div>',
  f'<div class="kick">DECC-26{TM} \u00b7 Denominator-Committed Evidence</div>'),
]

BAD = "NebelKr&auml;he"
GOOD = "Nebelkr&auml;he"
CASING_FILES = ["netz.py", "banners.py", "patch_site_visual.py", "mark_apply.py"]


def run(apply: bool):
    changed = set()
    print(("APPLYING" if apply else "PROPOSED (nothing written)") + "\n" + "-" * 56)
    for relpath, old, new in EDITS:
        p = Path(relpath)
        if not p.exists():
            print(f"MISSING FILE  {relpath}")
            continue
        t = p.read_text(encoding="utf-8")
        if new in t:
            print(f"ALREADY DONE  {relpath}: {new[:58]}...")
            continue
        n = t.count(old)
        if n == 0:
            print(f"MISSING STR   {relpath}: {old[:58]}...")
            continue
        if n > 1:
            print(f"NOT UNIQUE    {relpath} ({n}x): {old[:50]}... - skipped")
            continue
        if apply:
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            changed.add(relpath)
        print(f"{'EDITED' if apply else 'WILL EDIT':13s} {relpath}: -> {new[:58]}...")
    print()
    for relpath in CASING_FILES:
        p = Path(relpath)
        if not p.exists():
            print(f"MISSING FILE  {relpath}")
            continue
        t = p.read_text(encoding="utf-8")
        n = t.count(BAD)
        if n == 0:
            print(f"CLEAN         {relpath}")
            continue
        if apply:
            p.write_text(t.replace(BAD, GOOD), encoding="utf-8")
            changed.add(relpath)
        print(f"{'FIXED' if apply else 'WILL FIX':13s} {relpath}: {n} x {BAD}")
    print()
    if apply:
        print(f"{len(changed)} file(s) written: {sorted(changed)}")
        print("Renders regenerate from the fixed generators on their next run;")
        print("reports/*.html left as printed. Stage named files, verify, ship.")
    else:
        print("Apply with: python patch_site_marks_fix.py --apply")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
