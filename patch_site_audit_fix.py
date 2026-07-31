#!/usr/bin/env python3
"""
patch_site_audit_fix.py - hand-authored-page fixes from the 2026-07-30 audit.
Run from C:\\netz. Python 3.10+. Default REPORTS; --apply writes.

SCOPE: ONLY the pages a generator does NOT re-emit. Regenerate first
(desk.py ship) to clear casing/marks on the script-built pages; THIS handles
the hand-authored remainder so nothing waits on a manual next render.

  A. Casing  NebelKr&auml;he -> Nebelkr&auml;he on hand-authored pages +
             the JSON-LD alternateName on index (structured data, read
             literally by crawlers).
  B. Marks   first-use (TM) per page: kraehes_kalls.html "Krähe's Kalls",
             standards.html "Krähe's Nest".
  C. Social  decc.html gets og:image/og:url/og:title/twitter block (his
             auditor flagged og:image; the rest were also absent).
  D. Sitemap decc.html <url> block added.

Exact unique strings; a miss prints MISSING and guesses nothing. Casing pass
is a global replace on a fixed set of NAMED hand-authored files only. Never
stages, never commits. Idempotent (skips already-correct).
"""
import argparse
from pathlib import Path

TM = "\u2122"

# --- A: casing on hand-authored pages only (NOT the script-emitted ones) ---
CASING_PAGES = ["docs/index.html", "docs/register.html", "docs/fogsim.html",
                "docs/okk.html", "docs/KriegForeKaster.html",
                "docs/kraehes_kalls.html"]
# the literal (capital-K) casing also appears in index.html's JSON-LD as
# "NebelKrähe" (not entity-encoded) - fix both forms.
BAD_ENT, GOOD_ENT = "NebelKr&auml;he", "Nebelkr&auml;he"
BAD_LIT, GOOD_LIT = "NebelKr\u00e4he", "Nebelkr\u00e4he"

# --- B: first-use marks, context-anchored (the bare name recurs in title/og
# tags and repeated substrings, so anchor to the ONE body/heading occurrence
# that is the visible first use; blind first-replace would mark a <title>). ---
MARK_EDITS = [
 ("docs/kraehes_kalls.html",
  "class=\"lede\">Kr\u00e4he's Kalls is a",
  f"class=\"lede\">Kr\u00e4he's Kalls{TM} is a"),
 ("docs/standards.html",
  "KNM-26 \u2014 Kr\u00e4he's Nest Method",
  f"KNM-26 \u2014 Kr\u00e4he's Nest{TM} Method"),
 ("docs/standards.html",
  "KNP-26 \u2014 Kr\u00e4he's Nest Protocol",
  f"KNP-26 \u2014 Kr\u00e4he's Nest{TM} Protocol"),
]

# --- C: decc.html social block, inserted after its description meta ---
DECC_DESC = ('<meta name="description" content="Verify a denominator-committed '
             'disclosure bundle in your browser. Nothing is uploaded; '
             'verification runs entirely on your machine.">')
DECC_SOCIAL = DECC_DESC + "\n" + "\n".join([
 '<meta property="og:title" content="Verify a Sealed Disclosure \u2014 '
 f'DECC-26{TM}">',
 '<meta property="og:description" content="Verify a denominator-committed '
 'disclosure bundle in your browser. Nothing is uploaded.">',
 '<meta property="og:image" content="https://retroprescientaudit.com/'
 'og_nebelkraehe.png">',
 '<meta property="og:url" content="https://retroprescientaudit.com/'
 'decc.html">',
 '<meta name="twitter:card" content="summary_large_image">',
])

# --- D: sitemap entry for decc.html ---
SITEMAP_ANCHOR = "  <url>\n    <loc>https://retroprescientaudit.com/decc.html</loc>"
SITEMAP_FIRST_URL = "  <url>"  # insert before the first <url>
DECC_URL_BLOCK = ('  <url>\n'
                  '    <loc>https://retroprescientaudit.com/decc.html</loc>\n'
                  '    <lastmod>2026-07-30</lastmod>\n'
                  '    <changefreq>monthly</changefreq>\n'
                  '    <priority>0.7</priority>\n'
                  '  </url>\n')


def edit_exact(rel, old, new, apply, results):
    p = Path(rel)
    if not p.exists():
        results.append(f"MISSING FILE  {rel}"); return
    t = p.read_text(encoding="utf-8")
    if new in t and old not in t.replace(new, ""):
        results.append(f"ALREADY DONE  {rel}: {new[:52]}..."); return
    n = t.count(old)
    if n == 0:
        results.append(f"MISSING STR   {rel}: {old[:52]}..."); return
    if n > 1:
        results.append(f"NOT UNIQUE    {rel} ({n}x) {old[:44]}... skipped"); return
    if apply:
        p.write_text(t.replace(old, new, 1), encoding="utf-8")
    results.append(f"{'EDITED' if apply else 'WILL EDIT':13s} {rel}: {new[:52]}...")


def run(apply):
    print(("APPLYING" if apply else "PROPOSED (nothing written)") + "\n" + "-"*56)
    changed = set()
    res = []

    # A: casing
    for rel in CASING_PAGES:
        p = Path(rel)
        if not p.exists():
            res.append(f"MISSING FILE  {rel}"); continue
        t = p.read_text(encoding="utf-8")
        ne, nl = t.count(BAD_ENT), t.count(BAD_LIT)
        if ne + nl == 0:
            res.append(f"CLEAN         {rel}"); continue
        if apply:
            p.write_text(t.replace(BAD_ENT, GOOD_ENT).replace(BAD_LIT, GOOD_LIT),
                         encoding="utf-8")
            changed.add(rel)
        res.append(f"{'FIXED' if apply else 'WILL FIX':13s} {rel}: "
                   f"{ne} entity + {nl} literal")

    # B: marks
    for rel, old, new in MARK_EDITS:
        before = len(res)
        edit_exact(rel, old, new, apply, res)
        if apply and "EDITED" in res[before]:
            changed.add(rel)

    # C: decc social
    before = len(res)
    edit_exact("docs/decc.html", DECC_DESC, DECC_SOCIAL, apply, res)
    if apply and "EDITED" in res[before]:
        changed.add("docs/decc.html")

    # D: sitemap - insert decc block before the first <url> (idempotent)
    sp = Path("docs/sitemap.xml")
    if sp.exists():
        st = sp.read_text(encoding="utf-8")
        if "decc.html" in st:
            res.append("ALREADY DONE  docs/sitemap.xml: decc.html present")
        else:
            idx = st.find(SITEMAP_FIRST_URL)
            if idx == -1:
                res.append("MISSING STR   docs/sitemap.xml: no <url> anchor")
            else:
                if apply:
                    sp.write_text(st[:idx] + DECC_URL_BLOCK + st[idx:],
                                  encoding="utf-8")
                    changed.add("docs/sitemap.xml")
                res.append(f"{'EDITED' if apply else 'WILL EDIT':13s} "
                           f"docs/sitemap.xml: + decc.html url block")
    else:
        res.append("MISSING FILE  docs/sitemap.xml")

    for line in res:
        print(line)
    print()
    if apply:
        print(f"{len(changed)} file(s) written: {sorted(changed)}")
        print("Then: re-run site_audit.py, stage named files, desk.py ship, "
              "verify from remote.")
    else:
        print("Apply with: python patch_site_audit_fix.py --apply")
    print("\nNOTE: konsole social, canonicals (#6), missing H1s (#7), and the")
    print("translate-shield (#8) are GENERATOR edits (netz.py head/body")
    print("template) - not handled here so the render stays the source of truth.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
