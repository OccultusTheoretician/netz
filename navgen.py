#!/usr/bin/env python3
"""
navgen.py — one manifest, one nav, every served page.

THE DEFECT THIS RETIRES
Navigation was a flat 20-link bar copied by hand into 17 pages and embedded
separately in each generator's template — so kkr.html and ledger.html shipped
with no nav at all, and every manifest change meant editing N templates. This
tool makes nav_manifest.json the single source of truth and stamps the same
grouped nav onto every served page: replacing the bar where one exists,
inserting after <body> where none does.

KK30: the nav is the brand bar - crow monogram + NEBELKRAEHE in Cinzel
as the home link - and groups render as hover flyouts (CSS-only). Chrome
is monochrome; verdict colors stay on the pages. Desktop opens on :hover;
touch and keyboard open via :focus-within (the group container is
tabindex=0, so a tap or Tab focuses it). The group holding the current page
carries ng-here and its label reads brass. If instruments_map.json exists
beside this file, each link gains a title tooltip: an explicit blurb from
the map, else the first docstring line of the mapped module — the legend is
sourced from the tools themselves, never hand-copied.

MIRROR DISCIPLINE (why this cannot break desk verify)
desk.py asserts docs/kkr.html == forecasts/KKR_latest.html and
docs/ledger.html == forecasts/ledger.html. Whatever this tool does to a
mirrored docs page it does identically to its forecasts twin, so the mirror
invariant holds by construction.

Idempotent: its own output carries data-navgen="2" and is matched and replaced
whole on re-run. Zero external assets; nav carries translate="no" (instrument
names are proper nouns).

    python navgen.py            stamp every page (prints per-page action)
    python navgen.py --check    read-only drift report; exit 1 on drift
"""
import argparse
import ast
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
FC = HERE / "forecasts"
MANIFEST = HERE / "nav_manifest.json"
INSTRUMENTS = HERE / "instruments_map.json"

# forecasts twin -> docs page whose nav (and active state) it must share
MIRROR_TWINS = {
    "KKR_latest.html": "kkr.html",
    "ledger.html": "ledger.html",
}

NAV_RE = re.compile(
    r'(?:<style id="desknav-style">.*?</style>\s*)?'
    r'<nav class="desknav-unified".*?</nav>',
    re.S)
BODY_RE = re.compile(r"<body[^>]*>", re.I)
# the legacy generator bar (netz.py) — one per page, stripped so the
# manifest nav is the only site nav regardless of what any generator emits
LEGACY_NAV_RE = re.compile(r'<nav class="desknav">.*?</nav>', re.S)

STYLE = (
    '<style id="desknav-style">'
    '.desknav-unified{display:flex;flex-wrap:wrap;gap:.2rem 1.05rem;'
    'align-items:center;padding:.5rem 1.1rem;border-bottom:1px solid #26292f;'
    'background:rgba(7,9,12,.55);position:relative;z-index:40}'
    '.desknav-unified .ng-brand{display:inline-flex;align-items:center;'
    'gap:.6rem;text-decoration:none;margin-right:.9rem}'
    '.desknav-unified .ng-brand img{height:26px;width:auto;opacity:.95}'
    ".desknav-unified .ng-word{font:500 .8rem 'Cinzel',serif;"
    'letter-spacing:.28em;color:#e9e7e2}'
    '.desknav-unified .ng-brand:hover .ng-word{color:#ffffff}'
    '.desknav-unified .ng-drop{position:relative;display:inline-block;'
    'outline:none}'
    '.desknav-unified .ng-label{display:inline-block;color:#8b8b85;'
    "font:600 .62rem 'IBM Plex Mono',monospace;letter-spacing:.14em;"
    'text-transform:uppercase;cursor:pointer;user-select:none;'
    'padding:.25rem .1rem}'
    ".desknav-unified .ng-label::after{content:' \\25BE';color:#565650}"
    '.desknav-unified .ng-drop:hover .ng-label,'
    '.desknav-unified .ng-drop:focus-within .ng-label{color:#e9e7e2}'
    '.desknav-unified .ng-here .ng-label{color:#f2f0ea}'
    '.desknav-unified .ng-panel{display:none;position:absolute;left:0;'
    'top:100%;min-width:11rem;background:#0c0e11;border:1px solid #26292f;'
    'padding:.5rem .8rem;z-index:41;flex-direction:column;gap:.35rem}'
    '.desknav-unified .ng-drop:hover>.ng-panel,'
    '.desknav-unified .ng-drop:focus-within>.ng-panel{display:flex}'
    '.desknav-unified .ng-panel a{color:#8b8b85;text-decoration:none;'
    "font:600 .7rem 'IBM Plex Mono',monospace;letter-spacing:.1em;"
    'text-transform:uppercase;white-space:nowrap;padding:.05rem 0}'
    '.desknav-unified .ng-panel a:hover{color:#e9e7e2}'
    '.desknav-unified a[aria-current="page"]{color:#f2f0ea}'
    '.desknav-unified .ng-ext{color:#565650;text-decoration:none;'
    "font:600 .62rem 'IBM Plex Mono',monospace;letter-spacing:.14em;"
    'text-transform:uppercase;margin-left:auto}'
    '.desknav-unified .ng-ext:hover{color:#e9e7e2}'
    '</style>')


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8-sig"))


def load_titles():
    """href -> tooltip. Explicit 'blurb' wins; else first docstring line of
    the mapped 'module'. Absent map, unreadable module, or missing docstring
    all degrade to no tooltip — never to a guess."""
    if not INSTRUMENTS.exists():
        return {}
    try:
        m = json.loads(INSTRUMENTS.read_text(encoding="utf-8-sig"))
    except Exception:
        print("  WARN: instruments_map.json unreadable - tooltips skipped",
              file=sys.stderr)
        return {}
    out = {}
    for href, spec in m.items():
        if not isinstance(spec, dict):
            continue
        blurb = spec.get("blurb")
        if not blurb and spec.get("module"):
            mod = HERE / spec["module"]
            if mod.exists():
                try:
                    doc = ast.get_docstring(
                        ast.parse(mod.read_text(encoding="utf-8",
                                                errors="replace")))
                    if doc:
                        blurb = doc.strip().splitlines()[0].strip()
                except Exception:
                    blurb = None
        if blurb:
            out[href] = blurb
    return out


def _esc(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;")
             .replace("<", "&lt;").replace(">", "&gt;"))


def render_nav(manifest, active):
    titles = render_nav.titles
    parts = [STYLE,
             '<nav class="desknav-unified" data-navgen="2" '
             'aria-label="site" translate="no">',
             '<a class="ng-brand" href="index.html">'
             '<img src="brand/crow_mark_small_reverse.svg" alt="">'
             '<span class="ng-word">NEBELKR&Auml;HE</span></a>']
    for g in manifest.get("groups", []):
        here = any(ln["href"] == active for ln in g.get("links", []))
        cls = "ng-drop ng-here" if here else "ng-drop"
        parts.append(f'<div class="{cls}" tabindex="0">'
                     f'<span class="ng-label">{g["label"]}</span>'
                     '<div class="ng-panel">')
        for ln in g.get("links", []):
            cur = ' aria-current="page"' if ln["href"] == active else ""
            tip = titles.get(ln["href"])
            t = f' title="{_esc(tip)}"' if tip else ""
            parts.append(f'<a{cur}{t} href="{ln["href"]}">{ln["text"]}</a>')
        parts.append("</div></div>")
    for ln in manifest.get("external", []):
        parts.append(f'<a class="ng-ext" href="{ln["href"]}">{ln["text"]}</a>')
    parts.append("</nav>")
    return "".join(parts)


render_nav.titles = {}


def tracked_docs_pages():
    """Serve-scope discipline, same as site_audit: only tracked docs pages.
    A gitignored scratch page (warroom and its kin) is not a served surface
    and a generator has no business writing into it. Falls back to the raw
    glob only when git is unavailable, and says so."""
    try:
        r = subprocess.run(["git", "ls-files", "--", "docs/*.html",
                            ":!docs/**/*.html"],
                           cwd=str(HERE), capture_output=True, text=True,
                           timeout=15)
        if r.returncode == 0 and r.stdout.strip():
            return [HERE / line.strip() for line in r.stdout.splitlines()
                    if line.strip()]
    except Exception:
        pass
    print("  WARN: git scoping unavailable - falling back to disk glob; "
          "untracked scratch pages may be touched", file=sys.stderr)
    return [Path(f) for f in sorted(glob.glob(str(DOCS / "*.html")))]


def stamp(path, nav_html):
    """Return (action, new_text_or_None): 'replaced' | 'inserted' | 'current' | 'no-body'.
    Also strips the legacy generator nav so exactly one site nav remains."""
    s = path.read_text(encoding="utf-8")
    legacy = LEGACY_NAV_RE.search(s)
    if legacy:
        s = s[:legacy.start()] + s[legacy.end():].lstrip("\n")
    m = NAV_RE.search(s)
    if m:
        if m.group(0) == nav_html and not legacy:
            return "current", None
        new = s[:m.start()] + nav_html + s[m.end():]
        return "replaced", new
    b = BODY_RE.search(s)
    if not b:
        return "no-body", None
    return "inserted", s[:b.end()] + "\n" + nav_html + s[b.end():]


def manifest_hrefs(manifest):
    out = []
    for g in manifest.get("groups", []):
        out += [ln["href"] for ln in g.get("links", [])]
    out += [ln["href"] for ln in manifest.get("external", [])]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="read-only drift report; exit 1 on drift")
    ap.add_argument("--strip", metavar="FILE",
                    help="remove a navgen stamp from one file (undo for a page "
                         "that should never have been touched)")
    a = ap.parse_args()

    if a.strip:
        sp = Path(a.strip)
        if not sp.is_absolute():
            sp = HERE / a.strip
        if not sp.exists():
            print(f"--strip: {sp} not found", file=sys.stderr)
            return 1
        t = sp.read_text(encoding="utf-8")
        m = NAV_RE.search(t)
        if not m:
            print(f"--strip: no navgen stamp in {sp.name} - nothing to do")
            return 0
        sp.write_text(t[:m.start()] + t[m.end():].lstrip("\n"),
                      encoding="utf-8")
        print(f"--strip: stamp removed from {sp.name}")
        return 0

    if not MANIFEST.exists():
        print("nav_manifest.json not found beside navgen.py", file=sys.stderr)
        return 1
    if not DOCS.is_dir():
        print("docs/ not found beside navgen.py", file=sys.stderr)
        return 1

    manifest = load_manifest()
    render_nav.titles = load_titles()
    skip = set(manifest.get("skip", []))

    # sanity: every manifest link must point at a real served page
    missing = [h for h in manifest_hrefs(manifest)
               if not h.startswith("http") and not (DOCS / h).exists()]
    if missing:
        print("manifest points at pages that do not exist: "
              + ", ".join(missing), file=sys.stderr)
        return 1

    targets = []
    for p in sorted(tracked_docs_pages()):
        if p.name in skip:
            continue
        targets.append((p, p.name))
    for twin, active_as in MIRROR_TWINS.items():
        tp = FC / twin
        if tp.exists() and active_as not in skip:
            targets.append((tp, active_as))

    drift, wrote = 0, 0
    for path, active in targets:
        nav_html = render_nav(manifest, active)
        action, new = stamp(path, nav_html)
        # canonical-ensure (KK17): every stamped page carries one
        # <link rel="canonical"> derived from its basename, so
        # regenerated faces self-heal on the next ship like the nav.
        base = new if new is not None else path.read_text(encoding="utf-8")
        canon = ('<link rel="canonical" href="https://retroprescientaudit.com/'
                 + active + '">')
        if 'rel="canonical"' not in base and "</title>" in base:
            base = base.replace("</title>", "</title>\n" + canon, 1)
            if action == "current":
                action = "inserted"
            new = base
        elif new is not None:
            new = base
        # brand-ensure (KK30): every stamped page loads brand.css at end of
        # head, after its inline styles, so one file governs the palette.
        bcss = '<link rel="stylesheet" href="brand.css">'
        if 'href="brand.css"' not in base and "</head>" in base:
            base = base.replace("</head>", bcss + "\n</head>", 1)
            if action == "current":
                action = "inserted"
            new = base
        elif new is not None:
            new = base
        rel = path.relative_to(HERE)
        if a.check:
            if action != "current":
                drift += 1
                print(f"  DRIFT   {rel}  ({action})")
        else:
            if action in ("replaced", "inserted"):
                path.write_text(new, encoding="utf-8")
                wrote += 1
                print(f"  {action:8s} {rel}")
            elif action == "current":
                print(f"  current  {rel}")
            else:
                print(f"  SKIPPED  {rel}  (no <body> tag found)")

    if a.check:
        if drift:
            print(f"NAV · {drift} page(s) drifted from the manifest")
            return 1
        print(f"NAV · {len(targets)} page(s) match the manifest")
        return 0
    print(f"NAV · {wrote} page(s) stamped, {len(targets)-wrote} already current")
    if skip:
        print(f"NAV · skipped by manifest: {', '.join(sorted(skip))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
