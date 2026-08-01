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
    '.desknav-unified{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;'
    'align-items:baseline;padding:.7rem 1.1rem;border-bottom:1px solid #26292f;'
    'background:rgba(7,9,12,.55);position:relative;z-index:20}'
    '.desknav-unified .ng-group{display:inline-flex;flex-wrap:wrap;'
    'gap:.15rem .85rem;align-items:baseline}'
    '.desknav-unified .ng-label{color:#565650;'
    "font:600 .58rem 'IBM Plex Mono',monospace;letter-spacing:.14em;"
    'text-transform:uppercase;margin-right:.15rem;user-select:none}'
    '.desknav-unified a{color:#8b8b85;text-decoration:none;'
    "font:600 .7rem 'IBM Plex Mono',monospace;letter-spacing:.1em;"
    'text-transform:uppercase}'
    '.desknav-unified a:hover{color:#c9c9c2}'
    '.desknav-unified a[aria-current="page"]{color:#dcb65e}'
    '</style>')


def load_manifest():
    return json.loads(MANIFEST.read_text(encoding="utf-8-sig"))


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


def render_nav(manifest, active):
    parts = [STYLE,
             '<nav class="desknav-unified" data-navgen="2" '
             'aria-label="site" translate="no">']
    for g in manifest.get("groups", []):
        parts.append('<span class="ng-group">'
                     f'<span class="ng-label">{g["label"]}</span>')
        for ln in g.get("links", []):
            cur = ' aria-current="page"' if ln["href"] == active else ""
            parts.append(f'<a{cur} href="{ln["href"]}">{ln["text"]}</a>')
        parts.append("</span>")
    ext = manifest.get("external", [])
    if ext:
        parts.append('<span class="ng-group">'
                     '<span class="ng-label">&nbsp;</span>')
        for ln in ext:
            parts.append(f'<a href="{ln["href"]}">{ln["text"]}</a>')
        parts.append("</span>")
    parts.append("</nav>")
    return "".join(parts)


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
