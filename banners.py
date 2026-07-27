#!/usr/bin/env python3
"""
banners.py — headers, quote cards and credential banners for the desk.

Everything here is SVG. Type is the point of a banner, and rasterising type
requires the actual font on the rasterising machine; an SVG carries the stack
and renders correctly in any browser at any size. `export.html` is written
alongside, showing every banner at its true pixel dimensions so a screenshot or
a print-to-PDF gives you the PNG at the exact size a platform wants.

    python banners.py [outdir]        default: docs/brand/banners

EDIT THESE, NOT THE ARTWORK
    NAME, CARRIER, SAYINGS at the top of this file. Everything downstream is
    generated. No banner is hand-composed, so a change to a line of copy is one
    edit rather than fourteen.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mark_build as M
import mark_package as K

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/brand/banners")

# ----------------------------------------------------------------------
# The name is NOT stored here. identity.local.json is gitignored; if it exists
# the personal banners use it, and if it does not they fall back to the brand.
# A repository that never holds the name cannot publish it by accident, and the
# banner that carries it is generated locally and never committed.
_ident = Path(__file__).resolve().parent / "identity.local.json"
_I = {}
if _ident.exists():
    import json as _j
    _I = _j.loads(_ident.read_text(encoding="utf-8"))
NAME = _I.get("name", "NEBELKR\u00c4HE")
CARRIER = _I.get("carrier",
                 "A public-finance and audit professional with a decade of state service")
BRAND = "THE PRESCIENT DESK\u2122"
WORD = "NEBELKR\u00c4HE"
SITE = "retroprescientaudit.com"

# His own lines, as they already appear on the site. Nothing invented here.
SAYINGS = [
    ("Calling our shots in the fog.\nSoaring through our misses.", "the tagline"),
    ("Die Kr\u00e4he sieht\ndurch den Nebel.", "the callsign"),
    ("No credential is offered.\nRecompute the hashes.", "the invitation"),
    ("A method for telling\nforesight from arithmetic.", "Retro-Prescient Audit\u2122"),
    ("Conformance certifies process,\nnever foresight.", "RPAS 1.06"),
    ("The stated, compared\nto the operational.", "the one method"),
    ("Sealed before the outcome.\nAdjudicated blind. Scored.", "the discipline"),
    ("A record that keeps\nits own misses.", "permanently, in public"),
]

PLATE = "#080B0F"
INK = "#eceef1"
DIM = "#8b8d92"
BRASS = "#c9a227"
BRASS2 = "#dcb65e"
LINE = "#242a31"
TYPE = K.TYPE
MONO = K.MONO


# ----------------------------------------------------------------------
def field(w, h, seed=20260727, n=34, op=0.055):
    """The same angular lattice the site runs, seeded so every banner in the set
    carries the identical field. Consistency across a package is what makes it
    read as one system rather than a folder of pictures."""
    s = seed
    def rnd():
        nonlocal s
        s = (s * 1103515245 + 12345) & 0x7FFFFFFF
        return s / 0x7FFFFFFF
    out = []
    for _ in range(n):
        x, y = rnd() * w * 1.2 - w * .1, rnd() * h * 1.3 - h * .15
        a = (32 if rnd() < .5 else -32) + (rnd() - .5) * 14
        L = h * (.5 + rnd() * 1.8)
        import math
        x2 = x + math.cos(math.radians(a)) * L
        y2 = y + math.sin(math.radians(a)) * L
        out.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y2:.0f}"/>')
    return (f'<g stroke="#b9c6d4" stroke-opacity="{op}" stroke-width=".9" '
            f'stroke-linecap="square">' + "".join(out) + "</g>")


def mark(x, y, scale, grey=M.GREY, ink=M.INK, uid="m"):
    P = K.paths(4)
    return (f'<g transform="translate({x},{y}) scale({scale})">'
            f'<defs><clipPath id="c{uid}"><path d="{P["body"]}"/></clipPath></defs>'
            f'<path d="{P["body"]}" fill="{ink}"/>'
            f'<g clip-path="url(#c{uid})"><path d="{P["sh"]}" fill="{grey}"/>'
            f'<path d="{P["be"]}" fill="{grey}"/>'
            f'<path d="{P["neck"]}" fill="none" stroke="{grey}" '
            f'stroke-width="{M.TRIM}" stroke-linejoin="miter"/></g>'
            f'<path d="{P["eye"]}" fill="{M.LIGHT}"/></g>')


def svg(w, h, body, bg=PLATE):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'width="{w}" height="{h}">'
            f'<rect width="{w}" height="{h}" fill="{bg}"/>{field(w,h)}{body}</svg>\n')


def rule(x1, y, x2, col=LINE, o=1.0):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{col}" stroke-opacity="{o}"/>'


def t(x, y, s, size, fam=TYPE, fill=INK, ls=0.0, anchor="start", op=1.0):
    return (f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size:.0f}" '
            f'letter-spacing="{ls:.1f}" fill="{fill}" fill-opacity="{op}" '
            f'text-anchor="{anchor}">{s}</text>')


# ----------------------------------------------------------------------
def header_x():                       # 1500 x 500
    w, h = 1500, 500
    b = (mark(96, 150, 0.26, uid="x")
         + t(96, 352, WORD, 62, ls=13)
         + t(100, 392, BRAND, 19, MONO, DIM, 7)
         + rule(96, 416, 690, BRASS, .5)
         + t(96, 452, "Calling our shots in the fog. Soaring through our misses.",
             25, TYPE, "#c2c6cb")
         + t(1404, 452, SITE, 18, MONO, DIM, 3, "end"))
    return svg(w, h, b)


def header_linkedin_personal():       # 1584 x 396, safe area is generous left
    w, h = 1584, 396
    b = (mark(88, 84, 0.20, uid="li")
         + t(88, 236, NAME, 52, ls=11)
         + rule(88, 262, 900, BRASS, .5)
         + t(90, 300, CARRIER, 22, TYPE, "#c2c6cb")
         + t(92, 340, BRAND + "   \u00b7   " + SITE, 17, MONO, DIM, 5))
    return svg(w, h, b)


def header_linkedin_company():        # 1128 x 191
    w, h = 1128, 191
    b = (mark(64, 46, 0.135, uid="lc")
         + t(360, 96, WORD, 40, ls=9)
         + t(362, 130, BRAND, 15, MONO, DIM, 6)
         + rule(360, 148, 900, BRASS, .45)
         + t(360, 174, "Sealed before the outcome. Adjudicated blind. Scored.",
             17, TYPE, "#b9bec4"))
    return svg(w, h, b)


def header_substack():                # 1200 x 600
    w, h = 1200, 600
    b = (mark(300, 150, 0.30, uid="sb")
         + t(600, 400, WORD, 58, ls=14, anchor="middle")
         + t(600, 438, BRAND, 18, MONO, DIM, 7, "middle")
         + rule(360, 464, 840, BRASS, .45)
         + t(600, 506, "A method for telling foresight from arithmetic.",
             27, TYPE, "#c2c6cb", 0, "middle"))
    return svg(w, h, b)


def youtube():                        # 2560 x 1440, safe area 1546 x 423 centred
    w, h = 2560, 1440
    cx, cy = w // 2, h // 2
    b = (mark(cx - 300, cy - 250, 0.30, uid="yt")
         + t(cx, cy + 60, WORD, 78, ls=18, anchor="middle")
         + t(cx, cy + 108, BRAND, 24, MONO, DIM, 9, "middle")
         + rule(cx - 380, cy + 140, cx + 380, BRASS, .45)
         + t(cx, cy + 190, "Calling our shots in the fog.", 32, TYPE,
             "#c2c6cb", 0, "middle"))
    return svg(w, h, b)


def lower_third():                    # 1920 x 300
    w, h = 1920, 300
    b = (mark(70, 96, 0.145, uid="l3")
         + t(340, 150, NAME, 46, ls=9)
         + t(342, 190, CARRIER, 19, TYPE, "#b9bec4")
         + rule(340, 214, 1180, BRASS, .5)
         + t(342, 246, BRAND + "   \u00b7   " + SITE, 16, MONO, DIM, 5))
    return svg(w, h, b)


def email_signature():                # 600 x 160
    w, h = 600, 160
    b = (mark(22, 44, 0.098, uid="es")
         + t(122, 68, NAME, 24, ls=4)
         + t(123, 92, BRAND, 12, MONO, DIM, 4)
         + rule(122, 104, 560, BRASS, .45)
         + t(123, 126, SITE, 13, MONO, "#9aa0a8", 2))
    return svg(w, h, b)


def quote_card(i, text, attrib, w=1080, h=1080):
    lines = text.split("\n")
    fs = 74 if max(len(x) for x in lines) < 30 else 62
    y0 = h // 2 - (len(lines) - 1) * fs * 0.62 - 30
    body = "".join(t(96, y0 + n * fs * 1.24, ln, fs, TYPE, INK)
                   for n, ln in enumerate(lines))
    body += (rule(96, y0 + len(lines) * fs * 1.24 + 6, 96 + 300, BRASS, .6)
             + t(96, y0 + len(lines) * fs * 1.24 + 52, attrib.upper(),
                 21, MONO, BRASS2, 7)
             + mark(w - 300, h - 210, 0.115, uid=f"q{i}")
             + t(96, h - 74, WORD + "   \u00b7   " + SITE, 19, MONO, DIM, 5))
    return svg(w, h, body)


def quote_wide(i, text, attrib):
    return quote_card(i, text, attrib, 1600, 900)


# ----------------------------------------------------------------------
def main():
    M.load_panels(Path(__file__).resolve().parent / "panels.json")
    OUT.mkdir(parents=True, exist_ok=True)
    W = lambda n, s: (OUT / n).write_text(s, encoding="utf-8")

    W("header_x_1500x500.svg", header_x())
    W("header_linkedin_personal_1584x396.svg", header_linkedin_personal())
    W("header_linkedin_company_1128x191.svg", header_linkedin_company())
    W("header_substack_1200x600.svg", header_substack())
    W("header_youtube_2560x1440.svg", youtube())
    W("lower_third_1920x300.svg", lower_third())
    W("email_signature_600x160.svg", email_signature())

    for i, (txt, att) in enumerate(SAYINGS, 1):
        W(f"quote_{i:02d}_square.svg", quote_card(i, txt, att))
        W(f"quote_{i:02d}_wide.svg", quote_wide(i, txt, att))

    files = sorted(p.name for p in OUT.iterdir() if p.suffix == ".svg")
    cards = "".join(
        f'<figure><figcaption>{f}</figcaption>'
        f'<img src="{f}" alt=""></figure>' for f in files)
    (OUT / "export.html").write_text(f"""<!doctype html><meta charset="utf-8">
<title>NebelKr&auml;he &middot; banner export</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>body{{margin:0;background:#15171a;color:#cfd3d8;
font:14px/1.6 ui-monospace,Menlo,Consolas,monospace;padding:2rem}}
h1{{font:600 1rem/1 ui-monospace,monospace;letter-spacing:.2em;color:#c9a227}}
p{{max-width:70ch;color:#8b8d92}}
figure{{margin:2.2rem 0}}figcaption{{font-size:.72rem;color:#8b8d92;margin-bottom:.4rem;
letter-spacing:.1em}}img{{display:block;max-width:100%;border:1px solid #242a31}}</style>
<h1>BANNER EXPORT</h1>
<p>Every banner at its true pixel size. To get a PNG at exactly the dimensions a
platform wants, right-click the image and save it, or open the SVG directly and
export. The type renders correctly here because Cinzel and IBM Plex Mono are
loaded above; rasterising on a machine without them substitutes a fallback,
which is why these ship as SVG.</p>
{cards}""", encoding="utf-8")

    for f in sorted(OUT.iterdir()):
        print(f"  {f.name:44s} {f.stat().st_size:>8,}")
    print(f"\n  {len(list(OUT.iterdir()))} files.")
    print("  Copy lives in NAME, CARRIER and SAYINGS at the top of banners.py.")
    print("  Open export.html to see them all at true size.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
