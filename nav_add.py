#!/usr/bin/env python3
"""nav_add.py — put one link into the canonical nav on every served page, once.

The nav is baked into each page (19 copies, byte-identical by design, guarded by
site_audit's NAVDRIFT check). Hand-editing 19 files is how drift starts, so this
does it mechanically: same insertion, same position, every page, and it refuses
to run if the navs are not identical to begin with.

    python nav_add.py --after Konsole --label GlobalKaster --href globalkaster.html
    python nav_add.py --after Konsole --label GlobalKaster --href globalkaster.html --apply
"""
import argparse, pathlib, re, subprocess, sys

DOCS = pathlib.Path("docs")
NAV = re.compile(r'<nav class="desknav-unified".*?</nav>', re.S)


def served():
    out = subprocess.run(["git", "ls-files", "docs/"], capture_output=True,
                         text=True, check=True).stdout.splitlines()
    return sorted(DOCS / l.split("/")[-1] for l in out
                  if l.lower().endswith(".html") and l.count("/") == 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--after", required=True, help="link text to insert after")
    ap.add_argument("--label", required=True)
    ap.add_argument("--href", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    pages = [p for p in served() if p.exists()]
    navs = {}
    for p in pages:
        m = NAV.search(p.read_text(encoding="utf-8-sig"))
        if not m:
            print("NO NAV: %s — not a navigated page, skipped" % p.name)
            continue
        navs[p] = m.group(0)
    if not navs:
        sys.exit("no navs found")

    # normalise away the per-page current marker before comparing
    def norm(s):
        s = re.sub(r'\saria-current="page"', "", s)
        return s.replace("#dcb65e", "#8b8b85")
    shapes = {}
    for p, n in navs.items():
        shapes.setdefault(norm(n), []).append(p.name)
    if len(shapes) > 1:
        print("REFUSED — the navs are not identical; fix drift before adding:")
        for i, (_, names) in enumerate(sorted(shapes.items(),
                                              key=lambda kv: -len(kv[1])), 1):
            print("  shape %d (%d pages): %s" % (i, len(names),
                                                 ", ".join(sorted(names)[:6])))
        sys.exit(1)
    print("%d pages carry one identical nav." % len(navs))

    sample = next(iter(navs.values()))
    if 'href="%s"' % a.href in sample:
        sys.exit("%s is already in the nav — nothing to do." % a.href)
    anchors = re.findall(r'<a\b[^>]*>([^<]+)</a>', sample)
    if a.after not in anchors:
        sys.exit("--after %r not in the nav. Present: %s"
                 % (a.after, ", ".join(anchors)))

    STYLE = ("color:#8b8b85;text-decoration:none;font:600 .7rem 'IBM Plex Mono',"
             "monospace;letter-spacing:.1em;text-transform:uppercase")
    n_edit = 0
    for p, nav in navs.items():
        # find the anchor whose text is --after, insert immediately after it
        m = re.search(r'<a\b[^>]*>' + re.escape(a.after) + r'</a>', nav)
        if not m:
            print("SKIP %s — anchor text not found in its nav copy" % p.name)
            continue
        cur = ""
        if p.name == a.href:
            cur = ' aria-current="page"'
            style = STYLE.replace("#8b8b85", "#dcb65e")
        else:
            style = STYLE
        link = '<a%s style="%s" href="%s">%s</a>' % (cur, style, a.href, a.label)
        new_nav = nav[:m.end()] + link + nav[m.end():]
        s = p.read_text(encoding="utf-8-sig")
        s2 = s.replace(nav, new_nav, 1)
        if s2 == s:
            print("SKIP %s — replacement was a no-op" % p.name)
            continue
        n_edit += 1
        if a.apply:
            p.write_text(s2, encoding="utf-8")
    print(("APPLIED to %d pages." if a.apply else
           "DRY RUN — %d pages would change. Rerun with --apply.") % n_edit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
