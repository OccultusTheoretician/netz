#!/usr/bin/env python3
"""
patch_generators_seo.py - the four remaining site-audit findings, fixed in the
GENERATORS so they apply on every future emit. Run from C:\\netz. Python 3.10+.
Default REPORTS; --apply writes. Never stages, never commits.

WHY GENERATOR-LEVEL: the served pages are re-emitted by netz.py/kkr.py on every
ship. Patching docs/*.html directly is erased by the next render. These five
edits are permanent.

  A. CANONICAL (audit #6) - self-referencing <link rel=canonical> on every
     emitted page. netz.py already computes _slug and _site; this just uses
     them. Closes 19-of-20 pages missing canonicals.
  B. H1 (audit #7) - the dashboard pages (ledger/kkr/report/konsole) emit zero
     <h1>. The crest-title div is the natural document heading; converting it
     to <h1 class='crest-title'> keeps the existing class-selector CSS intact.
     A margin:0 is added to the CSS rule because <h1> carries a browser default
     margin that <div> does not.
  C. JSON-LD (audit #4, and the indexing finding) - a WebPage/Dataset block on
     the emitted pages. A search for "Retro-Prescient Audit" currently surfaces
     unrelated audit firms with similar names; structured data is how a crawler
     is told what this page actually is.
  D. XLATE (audit #8, his own auditor's one remaining finding) - kkr.py line
     ~287 emits a runnable command in reader-facing text outside translate="no".
     Machine translation rewrites the command and it verifies nothing.
  E. CASING, THIRD ENCODING - the sweeps caught NebelKrahe (literal) and
     NebelKr&auml;he (named entity). mark_build.py and mark_package.py carry a
     THIRD form, the numeric entity NebelKr&#228;he, in SVG aria-labels. Those
     aria-labels are the accessible name of the published mark artwork.

  python patch_generators_seo.py            # report
  python patch_generators_seo.py --apply    # write
"""
import argparse
from pathlib import Path

EDITS = []

# ---- A. canonical + C. JSON-LD (one edit; both go in the same head return) --
_OLD_HEAD = (
    "f\"<title>{html.escape(title)} \u00b7 Nebelkr\u00e4he</title>{_meta}"
    "<style>{HTML_CSS}</style></head>\""
)
_NEW_HEAD = (
    "f\"<link rel='canonical' href='{_site}/{_slug}'>\"\n"
    "            f\"<title>{html.escape(title)} \u00b7 Nebelkr\u00e4he</title>{_meta}\"\n"
    "            f\"{_jsonld}<style>{HTML_CSS}</style></head>\""
)
EDITS.append(("netz.py", _OLD_HEAD, _NEW_HEAD, "canonical + json-ld hook"))

# the _jsonld block itself, inserted right after _meta is built
_OLD_META_TAIL = (
    "        f'<meta name=\"twitter:card\" content=\"summary_large_image\">'\n"
    "    )\n"
)
_NEW_META_TAIL = (
    "        f'<meta name=\"twitter:card\" content=\"summary_large_image\">'\n"
    "    )\n"
    "    # Structured data: tells a crawler what this page IS. Without it a\n"
    "    # search for the desk's own name surfaces unrelated audit firms.\n"
    "    _jsonld = (\n"
    "        '<script type=\"application/ld+json\">{\"@context\":\"https://schema.org\",'\n"
    "        '\"@type\":\"WebPage\",\"name\":\"' + _ttl + '\",'\n"
    "        '\"description\":\"' + _desc.replace('\"', \"'\") + '\",'\n"
    "        '\"url\":\"' + _site + '/' + _slug + '\",'\n"
    "        '\"isPartOf\":{\"@type\":\"WebSite\",\"name\":\"Retro-Prescient Audit\",'\n"
    "        '\"url\":\"' + _site + '\"},'\n"
    "        '\"publisher\":{\"@type\":\"Organization\",\"name\":\"The Prescient Desk\"}}'\n"
    "        '</script>'\n"
    "    )\n"
)
EDITS.append(("netz.py", _OLD_META_TAIL, _NEW_META_TAIL, "json-ld block"))

# ---- B. H1 on the dashboard pages -------------------------------------------
EDITS.append((
    "netz.py",
    "f\"<div class='crest-title'>THE PRESCIENT DESK\\u2122 \u00b7 {doc_kind}</div>\"",
    "f\"<h1 class='crest-title'>THE PRESCIENT DESK\\u2122 \u00b7 {doc_kind}</h1>\"",
    "crest-title div -> h1",
))
EDITS.append((
    "netz.py",
    ".crest-title{font-family:'Spectral',Georgia,serif; font-size:1.65rem; font-weight:600;",
    ".crest-title{margin:0; font-family:'Spectral',Georgia,serif; font-size:1.65rem; font-weight:600;",
    "zero the h1 default margin",
))

# ---- D. translate-shield on the runnable command -----------------------------
EDITS.append((
    "kkr.py",
    "f\"({len(overdue)} past deadline \u2014 run `python kkr.py --resolve`). \"",
    "f\"({len(overdue)} past deadline \u2014 run \"\n"
    "               f\"<code translate=\\\"no\\\">python kkr.py --resolve</code>). \"",
    "translate-shield the command",
))

# ---- E. third-encoding casing ------------------------------------------------
CASING_FILES = ["mark_build.py", "mark_package.py"]
BAD_NUM, GOOD_NUM = "NebelKr&#228;he", "Nebelkr&#228;he"


def run(apply):
    print(("APPLYING" if apply else "PROPOSED (nothing written)") + "\n" + "-" * 60)
    changed = set()
    for rel, old, new, label in EDITS:
        p = Path(rel)
        if not p.exists():
            print(f"MISSING FILE  {rel}")
            continue
        t = p.read_text(encoding="utf-8")
        if new in t:
            print(f"ALREADY DONE  {rel}: {label}")
            continue
        n = t.count(old)
        if n == 0:
            print(f"MISSING STR   {rel}: {label}")
            continue
        if n > 1:
            print(f"NOT UNIQUE    {rel} ({n}x): {label} - skipped")
            continue
        if apply:
            p.write_text(t.replace(old, new, 1), encoding="utf-8")
            changed.add(rel)
        print(f"{'EDITED' if apply else 'WILL EDIT':13s} {rel}: {label}")

    print()
    for rel in CASING_FILES:
        p = Path(rel)
        if not p.exists():
            print(f"MISSING FILE  {rel}")
            continue
        t = p.read_text(encoding="utf-8")
        n = t.count(BAD_NUM)
        if n == 0:
            print(f"CLEAN         {rel}")
            continue
        if apply:
            p.write_text(t.replace(BAD_NUM, GOOD_NUM), encoding="utf-8")
            changed.add(rel)
        print(f"{'FIXED' if apply else 'WILL FIX':13s} {rel}: {n} x numeric-entity casing")

    print()
    if apply:
        print(f"{len(changed)} file(s) written: {sorted(changed)}")
        print("NEXT: regenerate (desk.py ship re-emits), then site_audit.py,")
        print("then stage named files. Renders inherit all of this.")
    else:
        print("Apply with: python patch_generators_seo.py --apply")
    print("\nNOT handled here (deliberate): konsole social tags - konsole is")
    print("emitted by a different path; and mark artwork already published")
    print("keeps its old aria-label. Generator fixed, printed record printed.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
