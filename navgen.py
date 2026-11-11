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

HEADER-2026-11-11: the stamped nav is the front page's header - the crow and
NEBELKRAEHE as the home link, a numbered contents line, and one "All pages"
disclosure (a <details> element, no script) holding the whole map. Links print
a plain name; the working name rides as a tag when the manifest gives one. A
group may name the health surface whose last move dates it (asof_path), read
at stamp time and omitted when unreadable. Each link keeps its title tooltip:
an explicit blurb from instruments_map.json, else the first docstring line of
the mapped module - the legend is sourced from the tools themselves, never
hand-copied. Every stamped page also loads fonts/fonts.css (fonts-ensure), so
the header's faces resolve on pages that never linked them.

MIRROR DISCIPLINE (why this cannot break desk verify)
desk.py asserts docs/kkr.html == forecasts/KKR_latest.html and
docs/ledger.html == forecasts/ledger.html. Whatever this tool does to a
mirrored docs page it does identically to its forecasts twin, so the mirror
invariant holds by construction.

Idempotent: its own output carries data-navgen="3" and is matched and replaced
whole on re-run (an older stamp is matched by the same pattern). Zero external
assets; the wordmark and the working-name tags carry translate="no".

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
    "ledger_full.html": "ledger_full.html",   # LEDGERVIEW-2026-09-02
}
# LEDGERVIEW-2026-09-02: a served page that is a companion of a manifest page
# lights that page's nav item rather than none.
ACTIVE_ALIAS = {"ledger_full.html": "ledger.html"}

NAV_RE = re.compile(
    r'(?:<style id="desknav-style">.*?</style>\s*)?'
    r'<nav class="desknav-unified".*?</nav>',
    re.S)
BODY_RE = re.compile(r"<body[^>]*>", re.I)
# the legacy generator bar (netz.py) — one per page, stripped so the
# manifest nav is the only site nav regardless of what any generator emits
LEGACY_NAV_RE = re.compile(r'<nav class="desknav">.*?</nav>', re.S)

# HEADER-2026-11-11: the stamped nav is the front page's header on every page -
# nameplate, numbered contents, and one "All pages" disclosure holding the whole
# map (plain names, working names as tags). CSS only. Every property a host page
# could leak into the nav through a bare element rule (nav, a, summary, details)
# is set here, so the header reads the same on all of them.
CROW = ('<svg class="ng-crow" viewBox="0 0 729 300" aria-hidden="true">'
        '<path d="M149 4 L258 29 L264 116 L268 125 L475 85 L602 149 L557 168 '
        'L609 189 L553 211 L582 234 L570 237 L725 296 L573 296 L456 257 L421 263 '
        'L271 219 L268 125 L234 138 L249 169 L202 163 L204 200 L164 159 L170 113 '
        'L186 109 L165 92 L4 53 Z" fill="#fff"></path>'
        '<path d="M269 132 L392 162 L326 188 L388 216 L336 227 L272 226 Z" '
        'fill="#000"></path>'
        '<path d="M271 219 L268 125 L234 138 L249 169 L202 163 L204 200 L164 159 '
        'L170 113" fill="none" stroke="#000" stroke-width="40" '
        'stroke-linejoin="miter" stroke-miterlimit="12"></path>'
        '<path d="M139.9 45.7 L160.5 45.3 L173.1 53.3 L156.6 53.5 Z" '
        'fill="#000"></path></svg>')

# The contents line when the manifest carries none.
DEFAULT_CONTENTS = [
    {"href": "ledger.html", "text": "Record"},
    {"href": "index.html#method", "text": "Method"},
    {"href": "findings.html", "text": "Findings"},
    {"href": "standards.html", "text": "Standards"},
    {"href": "instruments.html", "text": "Instruments"},
    {"href": "verify.html", "text": "Run the check"},
]

_N = ".desknav-unified"
STYLE = (
    '<style id="desknav-style">'
    + _N + '{display:block;position:relative;z-index:40;margin:0;padding:0;'
    'border:0;background:#000;color:#fff;text-align:left;'
    'container-type:inline-size;'
    "font:400 15px/1.3 'IBM Plex Sans',system-ui,sans-serif;"
    'letter-spacing:0;text-transform:none;-webkit-font-smoothing:antialiased}'
    + _N + ' *{box-sizing:border-box}'
    + _N + ' a,' + _N + ' summary,' + _N + ' details,' + _N + ' span,'
    + _N + ' div{margin:0;padding:0;border:0;background:none;float:none;'
    'font:inherit;letter-spacing:inherit;text-transform:inherit;'
    'text-decoration:none;clip-path:none}'
    + _N + ' a:focus-visible,' + _N + ' summary:focus-visible'
    '{outline:2px solid #fff;outline-offset:3px}'
    # the gutter a host page already gives the nav (a padded or narrow body) is
    # taken off the nav's own, so the header lines up with the page under it
    + _N + ' .ng-in{max-width:1240px;margin:0 auto;padding:0 max(0px,'
    'calc(clamp(16px,5cqi,72px) - (100vw - 100cqi)/2))}'
    + _N + ' .ng-top{display:flex;flex-wrap:wrap;align-items:center;'
    'justify-content:space-between;gap:2px 24px;padding:14px 0 10px}'
    + _N + ' .ng-brand{display:inline-flex;align-items:center;gap:14px;'
    'min-height:44px;color:#fff}'
    + _N + ' svg,' + _N + ' b{margin:0;padding:0;border:0;background:none;'
    'min-width:0;max-width:none;float:none}'
    + _N + ' .ng-crow{display:block;flex:none;width:58px;height:auto}'
    + _N + " .ng-word{font:500 17px/1 'Cinzel',serif;letter-spacing:.24em;"
    'color:#fff}'
    # FRESHLINE-2026-09-02: one freshness line per page, from docs/health.json
    + _N + ' .ng-fresh{display:flex;flex-wrap:wrap;gap:2px 12px;'
    "align-items:baseline;font:500 11px/1.5 'IBM Plex Mono',monospace;"
    'letter-spacing:.06em;text-transform:uppercase;color:#8d929b}'
    + _N + ' .ng-fresh b{font-weight:500;color:#c4c7cc}'
    + _N + ' .ng-fresh.ok b{color:#4E9E71}'
    + _N + ' .ng-fresh.late b{color:#c9a04a}'
    + _N + ' .ng-fresh.stale b{color:#C05149}'
    + _N + ' .ng-fresh a{color:#c4c7cc;text-decoration:underline;'
    'text-decoration-color:rgba(255,255,255,.35);text-underline-offset:3px}'
    + _N + ' .ng-fresh a:hover{color:#fff}'
    + _N + ' .ng-bar{position:relative;display:flex;flex-wrap:wrap;'
    'align-items:center;justify-content:space-between;gap:0 28px;'
    'border-top:2px solid #fff;border-bottom:1px solid rgba(255,255,255,.28)}'
    + _N + ' .ng-toc{display:flex;flex-wrap:wrap;gap:0 26px}'
    + _N + ' .ng-toc a{display:inline-flex;align-items:center;gap:8px;'
    'min-height:44px;color:#fff;font-size:13px;font-weight:500;'
    'letter-spacing:.04em;text-transform:uppercase}'
    + _N + " .ng-tn{font:400 11.5px 'IBM Plex Mono',monospace;color:#8d929b;"
    'letter-spacing:.04em}'
    + _N + ' .ng-toc a:hover{text-decoration:underline;text-underline-offset:6px}'
    + _N + ' .ng-toc a[aria-current="page"]{box-shadow:inset 0 -2px 0 #fff}'
    + _N + ' .ng-all>summary{display:inline-flex;align-items:center;gap:10px;'
    'min-height:44px;list-style:none;cursor:pointer;user-select:none;'
    'color:#fff;font-size:13px;font-weight:500;letter-spacing:.04em;'
    'text-transform:uppercase}'
    + _N + ' .ng-all>summary::-webkit-details-marker{display:none}'
    + _N + ' .ng-all>summary::before{content:none}'
    + _N + ' .ng-all>summary>span{display:inline-flex;align-items:baseline;gap:10px}'
    + _N + " .ng-all>summary::after{content:'+';"
    "font:400 16px/1 'IBM Plex Mono',monospace;color:#8d929b}"
    + _N + " .ng-all[open]>summary::after{content:'\\2212'}"
    + _N + ' .ng-all>summary:hover{text-decoration:underline;'
    'text-underline-offset:6px}'
    + _N + ' .ng-map{position:absolute;left:0;right:0;top:100%;z-index:41;'
    'display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px 28px;'
    'padding:18px 0 26px;background:#000;'
    'border-bottom:1px solid rgba(255,255,255,.28)}'
    + _N + " .ng-gl{display:block;padding:8px 0 8px;font:500 11px/1.4 "
    "'IBM Plex Mono',monospace;letter-spacing:.06em;text-transform:uppercase;"
    'color:#8d929b}'
    + _N + ' .ng-gd{display:block;color:#6f747d}'
    + _N + ' .ng-map a{display:flex;align-items:baseline;'
    'justify-content:space-between;gap:10px;padding:8px 0;color:#fff;'
    'font-size:14.5px;line-height:1.3;'
    'border-top:1px solid rgba(255,255,255,.14)}'
    + _N + ' .ng-map a:hover .ng-nm{text-decoration:underline;'
    'text-underline-offset:4px}'
    + _N + ' .ng-map a[aria-current="page"] .ng-nm{font-weight:500;'
    'box-shadow:inset 0 -1px 0 #fff}'
    + _N + " .ng-tg{flex:none;font:400 10.5px 'IBM Plex Mono',monospace;"
    'letter-spacing:.06em;text-transform:uppercase;color:#8d929b}'
    + _N + ' .ng-ext{display:inline-flex;align-items:center;min-height:34px;'
    'margin-top:10px;color:#c4c7cc;font-size:13px;text-decoration:underline;'
    'text-decoration-color:rgba(255,255,255,.35);text-underline-offset:4px}'
    '@container (max-width:1040px){'
    + _N + ' .ng-toc{gap:0 20px}'
    + _N + ' .ng-map{grid-template-columns:repeat(3,minmax(0,1fr))}}'
    '@container (max-width:880px){'
    + _N + ' .ng-toc{flex:1 1 100%;min-width:0;flex-wrap:nowrap;overflow-x:auto;'
    'scrollbar-width:none;gap:0 22px}'
    + _N + ' .ng-toc::-webkit-scrollbar{display:none}'
    + _N + ' .ng-toc a{flex:none}'
    + _N + ' .ng-all{flex:1 1 100%;border-top:1px solid rgba(255,255,255,.14)}'
    + _N + ' .ng-all>summary{display:flex;justify-content:space-between}'
    + _N + ' .ng-map{position:static;grid-template-columns:repeat(2,minmax(0,1fr));'
    'padding:4px 0 18px;border-bottom:0}}'
    '@container (max-width:600px){'
    + _N + ' .ng-top{padding:10px 0 8px}'
    + _N + ' .ng-crow{width:50px}'
    + _N + ' .ng-word{font-size:15px;letter-spacing:.2em}'
    + _N + ' .ng-fresh span:nth-child(2){display:none}'
    + _N + ' .ng-map{grid-template-columns:minmax(0,1fr)}'
    + _N + ' .ng-map a{padding:12px 0}}'
    '@media print{' + _N + ' .ng-bar,' + _N + ' .ng-fresh{display:none}}'
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


def _asof(health, path):
    """ARCHIVE date: the day a group's source of record last moved, read from
    the health face. Absent or unreadable -> '' and the line is omitted."""
    try:
        for s in (health or {}).get("surfaces") or []:
            if s.get("path") == path and s.get("last_moved_utc"):
                return str(s["last_moved_utc"])[:10]
    except Exception:
        pass
    return ""


def render_nav(manifest, active):
    titles = render_nav.titles
    health = render_nav.health
    parts = [STYLE,
             '<nav class="desknav-unified" data-navgen="3" aria-label="site">',
             '<div class="ng-in"><div class="ng-top">',
             '<a class="ng-brand" href="index.html" translate="no">' + CROW +
             '<span class="ng-word">NEBELKR&Auml;HE</span></a>']
    fresh = render_fresh(health)   # FRESHLINE-2026-09-02
    if fresh:
        parts.append(fresh)
    parts.append('</div><div class="ng-bar"><div class="ng-toc">')
    for i, ln in enumerate(manifest.get("contents") or DEFAULT_CONTENTS, 1):
        cur = ' aria-current="page"' if ln["href"] == active else ""
        parts.append(f'<a{cur} href="{ln["href"]}">'
                     f'<span class="ng-tn">{i:02d}</span>{ln["text"]}</a>')
    npages = sum(len(g.get("links", [])) for g in manifest.get("groups", []))
    parts.append('</div><details class="ng-all"><summary><span>All pages '
                 f'<span class="ng-tn">{npages}</span></span></summary>'
                 '<div class="ng-map">')
    ext = manifest.get("external", [])
    groups = manifest.get("groups", [])
    for gi, g in enumerate(groups):
        date = _asof(health, g["asof_path"]) if g.get("asof_path") else ""
        note = g.get("asof_note", "as of")
        gd = f'<span class="ng-gd">{_esc(note)} {date}</span>' if date else ""
        parts.append(f'<div class="ng-grp"><span class="ng-gl">{g["label"]}'
                     f'{gd}</span>')
        for ln in g.get("links", []):
            cur = ' aria-current="page"' if ln["href"] == active else ""
            tip = titles.get(ln["href"])
            t = f' title="{_esc(tip)}"' if tip else ""
            tag = (f'<span class="ng-tg" translate="no">{ln["tag"]}</span>'
                   if ln.get("tag") else "")
            parts.append(f'<a{cur}{t} href="{ln["href"]}">'
                         f'<span class="ng-nm">{ln["text"]}</span>{tag}</a>')
        if gi == len(groups) - 1:
            for ln in ext:
                parts.append(f'<a class="ng-ext" href="{ln["href"]}">'
                             f'{ln["text"]}</a>')
        parts.append("</div>")
    parts.append("</div></details></div></div></nav>")
    return "".join(parts)


render_nav.titles = {}
render_nav.health = None   # FRESHLINE-2026-09-02


def load_health():
    """FRESHLINE-2026-09-02: the health face, read at stamp time. Missing or
    unreadable -> None, and the line is omitted rather than guessed."""
    p = DOCS / "health.json"
    if not p.exists():
        print("  NOTE: docs/health.json absent - freshness line omitted",
              file=sys.stderr)
        return None
    try:
        h = json.loads(p.read_text(encoding="utf-8-sig"))
        if not h.get("as_of") or not isinstance(h.get("summary"), dict):
            raise ValueError("as_of or summary missing")
        return h
    except Exception as ex:
        print(f"  NOTE: docs/health.json unreadable ({type(ex).__name__}) - "
              "freshness line omitted", file=sys.stderr)
        return None


def render_fresh(h):
    """FRESHLINE-2026-09-02: the line itself. Worst state names the colour;
    the counts ride in the text and the tooltip; the link opens the face."""
    if not h:
        return ""
    s = h.get("summary") or {}
    worst = str(h.get("worst") or "").upper()
    cls = {"OK": "ok", "LATE": "late", "STALE": "stale"}.get(worst, "")
    asof = str(h.get("as_of"))[:16].replace("T", " ") + "Z"
    counts = " ".join(f"{int(s.get(k, 0) or 0)} {k}"
                      for k in ("OK", "LATE", "STALE", "EVENT") if k in s)
    nodate = int(s.get("NO-DATE", 0) or 0)
    tip = _esc(f"desk health as of {asof}: {counts}"
               + (f" {nodate} NO-DATE" if nodate else "")
               + f"; worst {worst or '-'}. health.py grades every served surface "
               "against the cadence the desk committed to in health_expect.json.")
    return (f'<span class="ng-fresh {cls}" title="{tip}">'
            f'<span>desk as of <b>{_esc(asof)}</b></span>'
            f'<span>{_esc(counts)}</span>'
            f'<span>worst <b>{_esc(worst or "-")}</b></span>'
            '<a href="health.html">health</a></span>')


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
            # NAVGONE-2026-11-10: a tracked page that has left the disk is on its way out
            # of the index (the publish stages the removal after this runs). It is no
            # served surface any more and there is nothing to stamp.
            return [p for p in (HERE / line.strip() for line in r.stdout.splitlines()
                                if line.strip()) if p.exists()]
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
    render_nav.health = load_health()   # FRESHLINE-2026-09-02
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
        targets.append((p, ACTIVE_ALIAS.get(p.name, p.name)))
    for twin, active_as in MIRROR_TWINS.items():
        tp = FC / twin
        _act = ACTIVE_ALIAS.get(active_as, active_as)
        if tp.exists() and active_as not in skip:
            targets.append((tp, _act))
        # LEDGERVIEW-2026-09-02: the served side of a twin is stamped here too,
        # tracked or not, so the pair cannot drift between add -A and verify on
        # the first publish that carries a new served page.
        dp = DOCS / active_as
        if dp.exists() and active_as not in skip and all(_p != dp for _p, _ in targets):
            targets.append((dp, _act))

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
        # fonts-ensure (HEADER-2026-11-11): the header names IBM Plex and Cinzel;
        # thirteen pages never linked the self-hosted faces. Same shape as the
        # brand-ensure below; @font-face carries no cascade, so order is free.
        fcss = '<link rel="stylesheet" href="fonts/fonts.css">'
        if 'fonts/fonts.css' not in base and "</head>" in base:
            base = base.replace("</head>", fcss + "\n</head>", 1)
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
