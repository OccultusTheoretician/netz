#!/usr/bin/env python3
"""
mark_package.py — the full Nebelkraehe graphics package.

Imports the geometry from mark_build.py. There is still exactly one vertex
table; this only renders it more ways. Nothing here duplicates a coordinate.

    python mark_package.py [outdir]        default: docs/brand

WHY VARIANTS EXIST, RATHER THAN JUST SCALING ONE FILE

The primary mark is tuned for 150px and up. Below roughly 64px two things fail:
the neck trim is an 11px stroke on a 729px canvas, which goes sub-pixel and the
lit edge — the best thing about the mark — simply disappears; and the tail's fog
gradient, which reads as dissolution at 512px, reads as grey mud at 32. So the
small sizes get a thickened trim and a solid tail. That is optical adjustment,
which is what a package is for, and it is the difference between a logo and a
file somebody scaled.

    crow_mark.svg              primary, 150px and up
    crow_mark_small.svg        optical variant, 64px and below
    crow_mark_ink.svg          one colour, print / stamp / embroidery
    crow_mark_reverse.svg      one colour light, for dark or photographic ground
    crow_mark_square.svg       1:1, avatars and app tiles
    lockup_horizontal.svg      mark + wordmark + rule
    lockup_stacked.svg         mark over wordmark, for narrow columns
    favicon_16/32/48.png       browser
    apple-touch-icon.png       180, opaque plate
    avatar_400.png             social
    crow_mark_512/1024.png     raster masters
    og_nebelkraehe.png         1200x630 card
    banner_1500x500.png        header
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import mark_build as M

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("docs/brand")
WORD = "NEBELKR\u00c4HE"
# Roman inscriptional capitals. The Atreides register is Homeric, not sci-fi —
# a House name is a thing cut into stone, and Cinzel is the free Trajan
# derivative that does that. Cormorant is a Garamond, which is why it read
# editorial and businesslike. Falls back through Trajan to a serif stack.
TYPE = "'Cinzel','Trajan Pro',Georgia,'Times New Roman',serif"
INK_TEXT = "#14181d"      # for light ground — the default
DIM_TEXT = "#5a6068"
REV_TEXT = "#eceef1"      # for dark ground
REV_DIM  = "#9aa0a8"
MONO = "ui-monospace,Menlo,Consolas,monospace"


def paths(pad=4, square=False, extra_w=0.0):
    minx, miny, maxx, maxy = M.bbox()
    w, h = maxx - minx + pad * 2, maxy - miny + pad * 2
    ox, oy = pad - minx, pad - miny
    if square:
        side = max(w, h)
        ox += (side - w) / 2
        oy += (side - h) / 2
        w = h = side
    T = lambda p: (round(p[0] + ox, 1), round(p[1] + oy, 1))
    d = lambda pl: "M" + " L".join(f"{x} {y}" for x, y in pl) + " Z"
    dop = lambda pl: "M" + " L".join(f"{x} {y}" for x, y in pl)
    return {"w": w + extra_w, "h": h, "T": T, "d": d, "dop": dop,
            "body": d([T(p) for p in M.BODY]),
            "sh": d([T(p) for p in M.SHOULDER]),
            "be": d([T(p) for p in M.BELLY]),
            "neck": dop([T(p) for p in M.NECK]),
            "eye": d([T(p) for p in M.eye_slit()]),
            "g1": T(M.BODY[-1]), "g2": T(M.BODY[13])}


def render(pad=4, square=False, mono=None, trim=None, fog=True, plate=None,
           word=None, tagline=None, stacked=False, reverse=False):
    extra = 0.0
    P = paths(pad, square)
    if word and not stacked:
        # THE BUG THIS REPLACES: x-position and canvas width were derived from the
        # mark's HEIGHT. The mark is 729 x 300 — aspect 2.43 — so the wordmark
        # started at 258, i.e. inside the bird, and ran off the right edge.
        # Position from the mark's WIDTH and size the canvas from the measured
        # text extent instead of a guessed multiple.
        fs = P["h"] * 0.30
        tw_est = len(WORD) * (fs * 0.70 + fs * 0.13)
        extra = P["h"] * 0.30 + tw_est + P["h"] * 0.14
    P = paths(pad, square, extra)
    tw = M.TRIM if trim is None else trim
    grey = mono or M.GREY
    light = mono or M.LIGHT
    fill = mono or ("url(#fog)" if fog else M.INK)
    W, H = P["w"], P["h"]
    if word and stacked:
        H = P["h"] * 1.42
    stops = "".join(
        f'<stop offset="{o:.2f}" stop-color="#{c[0]:02x}{c[1]:02x}{c[2]:02x}"'
        f' stop-opacity="{a}"/>' for o, c, a in M.FOG)
    grad = ("" if (mono or not fog) else
            f'<linearGradient id="fog" gradientUnits="userSpaceOnUse" '
            f'x1="{P["g1"][0]}" y1="{P["g1"][1]}" x2="{P["g2"][0]}" y2="{P["g2"][1]}">'
            f'{stops}</linearGradient>')
    bg = f'<rect width="{W}" height="{H}" fill="{plate}"/>' if plate else ""
    txt = ""
    if word:
        # A lockup with no plate lands on whatever ground it is placed on, and
        # that is white far more often than not. Default to dark type; the
        # reverse variants exist for dark ground and say so in the filename.
        ink = mono or (REV_TEXT if reverse else INK_TEXT)
        dim = mono or (REV_DIM if reverse else DIM_TEXT)
        if stacked:
            fs = P["h"] * 0.26
            txt = (f'<text x="{W/2:.1f}" y="{P["h"]*1.22:.1f}" text-anchor="middle" '
                   f'font-family="{TYPE}" font-size="{fs:.1f}" '
                   f'letter-spacing="{fs*0.16:.1f}" fill="{ink}">{WORD}</text>')
            if tagline:
                txt += (f'<text x="{W/2:.1f}" y="{P["h"]*1.36:.1f}" text-anchor="middle" '
                        f'font-family="{MONO}" font-size="{fs*0.26:.1f}" '
                        f'letter-spacing="{fs*0.12:.1f}" fill="{dim}">{tagline}</text>')
        else:
            mark_w = paths(pad, square)["w"]
            x0 = mark_w + P["h"] * 0.26
            fs = P["h"] * 0.30
            txt = (f'<line x1="{x0-P["h"]*0.13:.1f}" y1="{P["h"]*0.22:.1f}" '
                   f'x2="{x0-P["h"]*0.13:.1f}" y2="{P["h"]*0.78:.1f}" '
                   f'stroke="{dim}" stroke-width="1.5" opacity=".55"/>'
                   f'<text x="{x0:.1f}" y="{P["h"]*0.56:.1f}" font-family="{TYPE}" '
                   f'font-size="{fs:.1f}" letter-spacing="{fs*0.13:.1f}" '
                   f'fill="{ink}">{WORD}</text>')
            if tagline:
                txt += (f'<text x="{x0+2:.1f}" y="{P["h"]*0.74:.1f}" font-family="{MONO}" '
                        f'font-size="{fs*0.25:.1f}" letter-spacing="{fs*0.11:.1f}" '
                        f'fill="{dim}">{tagline}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} {H:.0f}" '
            f'width="{W:.0f}" height="{H:.0f}" role="img" '
            f'aria-label="Nebelkr&#228;he">'
            f'<defs>{grad}<clipPath id="body"><path d="{P["body"]}"/></clipPath></defs>'
            f'{bg}'
            f'<path d="{P["body"]}" fill="{fill}"/>'
            f'<g clip-path="url(#body)" fill="{grey}" stroke="{grey}" '
            f'stroke-linejoin="miter" stroke-miterlimit="4">'
            f'<path d="{P["sh"]}" stroke-width="0"/>'
            f'<path d="{P["be"]}" stroke-width="0"/>'
            f'<path d="{P["neck"]}" fill="none" stroke-width="{tw}" stroke-linecap="butt"/>'
            f'</g><path d="{P["eye"]}" fill="{light}"/>{txt}</svg>\n')


def small_raster(px):
    t, f = M.TRIM, M.FOG
    M.TRIM = 42
    M.FOG = [(0.0, (0x0f, 0x12, 0x16), 1.0), (1.0, (0x0f, 0x12, 0x16), 1.0)]
    img = M.raster(px, pad_frac=.04, canvas=(px, px))
    M.TRIM, M.FOG = t, f
    return img


def main():
    M.load_panels(Path(__file__).resolve().parent / "panels.json")
    OUT.mkdir(parents=True, exist_ok=True)
    W = lambda n, s: (OUT / n).write_text(s, encoding="utf-8")

    W("crow_mark.svg", render())
    W("crow_mark_small.svg", render(trim=40, fog=False))
    W("crow_mark_ink.svg", render(mono=M.INK, fog=False))
    W("crow_mark_reverse.svg", render(mono="#e8eaed", fog=False))
    W("crow_mark_square.svg", render(pad=40, square=True))
    W("lockup_horizontal.svg", render(word=True, tagline="THE PRESCIENT DESK"))
    W("lockup_horizontal_reverse.svg",
      render(word=True, tagline="THE PRESCIENT DESK", reverse=True))
    W("lockup_horizontal_ink.svg",
      render(fog=False, word=True, tagline="THE PRESCIENT DESK"))
    W("lockup_stacked.svg", render(word=True, stacked=True,
                                   tagline="THE PRESCIENT DESK"))
    W("lockup_stacked_reverse.svg",
      render(word=True, stacked=True, tagline="THE PRESCIENT DESK", reverse=True))
    W("lockup_stacked_ink.svg",
      render(fog=False, word=True, stacked=True, tagline="THE PRESCIENT DESK"))

    M.raster(512).save(OUT / "crow_mark_512.png")
    M.raster(1024).save(OUT / "crow_mark_1024.png")
    M.raster(400, pad_frac=.14, plate=M.PLATE, canvas=(400, 400)).save(OUT / "avatar_400.png")
    M.raster(180, pad_frac=.12, plate=M.PLATE, canvas=(180, 180)).save(OUT / "apple-touch-icon.png")
    for px in (16, 32, 48):
        small_raster(px).save(OUT / f"favicon_{px}.png")
    small_raster(48).save(OUT / "favicon.png")
    M.raster(1200, pad_frac=.22, plate=M.PLATE, canvas=(1200, 630)).save(OUT / "og_nebelkraehe.png")
    M.raster(1500, pad_frac=.30, plate=M.PLATE, canvas=(1500, 500)).save(OUT / "banner_1500x500.png")

    extras(OUT)

    for f in sorted(OUT.iterdir()):
        print(f"  {f.name:26s} {f.stat().st_size:>9,}")
    print(f"\n  {len(list(OUT.iterdir()))} files. One vertex table, no duplicated"
          f" coordinate.\n  Edit mark_build.py and regenerate; never edit an SVG by hand.")
    return 0




# ======================================================================
# THE REST OF THE PACKAGE — everything a press or media kit is asked for
# ======================================================================
PALETTE = [("ink", M.INK, "head, body, wing"),
           ("grey", M.GREY, "panels and neck trim"),
           ("light", M.LIGHT, "the eye slit, and nothing else"),
           ("plate", M.PLATE, "site ground"),
           ("brass", "#c9a227", "rules, ticks, the sweep"),
           ("brass lit", "#dcb65e", "hover and emphasis")]


def wordmark_only(reverse=False, mono=None, tagline=True):
    fs, H = 110, 260
    ink = mono or (REV_TEXT if reverse else INK_TEXT)
    dim = mono or (REV_DIM if reverse else DIM_TEXT)
    W = int(len(WORD) * (fs * 0.70 + fs * 0.13) + 80)
    t = (f'<text x="40" y="{fs*1.25:.0f}" font-family="{TYPE}" font-size="{fs}" '
         f'letter-spacing="{fs*0.13:.1f}" fill="{ink}">{WORD}</text>')
    if tagline:
        t += (f'<text x="44" y="{fs*1.80:.0f}" font-family="{MONO}" '
              f'font-size="{fs*0.24:.1f}" letter-spacing="{fs*0.11:.1f}" '
              f'fill="{dim}">THE PRESCIENT DESK</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'width="{W}" height="{H}" role="img" aria-label="Nebelkr&#228;he">{t}</svg>\n')


def monogram(reverse=False):
    """Head and eye only, tight. For sizes where the whole bird cannot resolve —
    app tiles, watch faces, embossing, a 12px inline glyph."""
    xs = [p[0] for p in M.BODY[:4] + M.BODY[18:]]
    ys = [p[1] for p in M.BODY[:4] + M.BODY[18:]]
    x0, y0, x1, y1 = min(xs) - 8, min(ys) - 8, max(xs) + 8, max(ys) + 8
    side = max(x1 - x0, y1 - y0)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = f"{cx-side/2:.0f} {cy-side/2:.0f} {side:.0f} {side:.0f}"
    P = paths(4)
    ink = "#eceef1" if reverse else M.INK
    grey = "#9aa0a8" if reverse else M.GREY
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" '
            f'width="{side:.0f}" height="{side:.0f}" role="img" '
            f'aria-label="Nebelkr&#228;he monogram">'
            f'<defs><clipPath id="b"><path d="{P["body"]}"/></clipPath></defs>'
            f'<path d="{P["body"]}" fill="{ink}"/>'
            f'<g clip-path="url(#b)"><path d="{P["neck"]}" fill="none" stroke="{grey}" '
            f'stroke-width="44" stroke-linejoin="miter"/></g>'
            f'<path d="{P["eye"]}" fill="{M.LIGHT}"/></svg>\n')


def brand_sheet():
    """One page a journalist or a design team can be handed: every variant, the
    palette with hex, the type specimen, the clear-space rule and the minimum
    size. This is the artifact that answers 'send us your brand assets'."""
    W, H = 1600, 1150
    P = paths(4)
    sw = ""
    for i, (name, hexv, use) in enumerate(PALETTE):
        x = 90 + i * 245
        sw += (f'<rect x="{x}" y="742" width="205" height="96" fill="{hexv}" '
               f'stroke="#2a2f36"/>'
               f'<text x="{x}" y="866" font-family="{MONO}" font-size="19" '
               f'fill="#cfd3d8">{name}</text>'
               f'<text x="{x}" y="890" font-family="{MONO}" font-size="17" '
               f'fill="#7d838c">{hexv}</text>'
               f'<text x="{x}" y="914" font-family="{MONO}" font-size="15" '
               f'fill="#5f656d">{use}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<rect width="{W}" height="{H}" fill="{M.PLATE}"/>
<text x="90" y="96" font-family="{TYPE}" font-size="54" letter-spacing="12" fill="#eceef1">{WORD}</text>
<text x="94" y="132" font-family="{MONO}" font-size="19" letter-spacing="7" fill="#8b8d92">BRAND SHEET &#183; THE PRESCIENT DESK</text>
<line x1="90" y1="168" x2="{W-90}" y2="168" stroke="#2a2f36"/>
<text x="90" y="212" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">PRIMARY</text>
<g transform="translate(90,236) scale(0.62)"><path d="{P["body"]}" fill="{M.INK}"/>
  <g clip-path="url(#bs)"><path d="{P["sh"]}" fill="{M.GREY}"/><path d="{P["be"]}" fill="{M.GREY}"/>
  <path d="{P["neck"]}" fill="none" stroke="{M.GREY}" stroke-width="{M.TRIM}" stroke-linejoin="miter"/></g>
  <path d="{P["eye"]}" fill="{M.LIGHT}"/></g>
<defs><clipPath id="bs"><path d="{P["body"]}"/></clipPath></defs>
<text x="640" y="212" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">SMALL &#183; 64px AND BELOW</text>
<g transform="translate(640,236) scale(0.30)"><path d="{P["body"]}" fill="{M.INK}"/>
  <g clip-path="url(#bs)"><path d="{P["neck"]}" fill="none" stroke="{M.GREY}" stroke-width="40" stroke-linejoin="miter"/></g>
  <path d="{P["eye"]}" fill="{M.LIGHT}"/></g>
<text x="1020" y="212" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">REVERSE</text>
<g transform="translate(1020,236) scale(0.30)"><path d="{P["body"]}" fill="#eceef1"/>
  <g clip-path="url(#bs)"><path d="{P["neck"]}" fill="none" stroke="#9aa0a8" stroke-width="40" stroke-linejoin="miter"/></g></g>
<line x1="90" y1="470" x2="{W-90}" y2="470" stroke="#2a2f36"/>
<text x="90" y="516" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">TYPE</text>
<text x="90" y="586" font-family="{TYPE}" font-size="62" letter-spacing="9" fill="#eceef1">ABCDEFGHIJKLM</text>
<text x="90" y="650" font-family="{TYPE}" font-size="62" letter-spacing="9" fill="#eceef1">NOPQRSTUVWXYZ</text>
<text x="900" y="560" font-family="{MONO}" font-size="20" fill="#cfd3d8">Cinzel &#183; inscriptional capitals</text>
<text x="900" y="590" font-family="{MONO}" font-size="17" fill="#7d838c">wordmark, headings</text>
<text x="900" y="628" font-family="{MONO}" font-size="20" fill="#cfd3d8">IBM Plex Mono</text>
<text x="900" y="658" font-family="{MONO}" font-size="17" fill="#7d838c">kickers, data, everything measured</text>
<line x1="90" y1="700" x2="{W-90}" y2="700" stroke="#2a2f36"/>
<text x="90" y="726" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">PALETTE</text>
{sw}
<line x1="90" y1="952" x2="{W-90}" y2="952" stroke="#2a2f36"/>
<text x="90" y="994" font-family="{MONO}" font-size="17" letter-spacing="5" fill="#c9a227">RULES</text>
<text x="90" y="1030" font-family="{MONO}" font-size="18" fill="#cfd3d8">Clear space on every side equals the height of the eye slit. Nothing enters it.</text>
<text x="90" y="1058" font-family="{MONO}" font-size="18" fill="#cfd3d8">Below 64px use the small variant. The primary&#8217;s trim goes sub-pixel and the fog turns to mud.</text>
<text x="90" y="1086" font-family="{MONO}" font-size="18" fill="#cfd3d8">Never stretch. Aspect is 729:300. Never recolour, never outline, never add a shadow inside the artwork.</text>
<text x="90" y="1114" font-family="{MONO}" font-size="18" fill="#7d838c">Every file is generated from one vertex table. Edit mark_build.py and regenerate; never edit an SVG by hand.</text>
</svg>
'''


def extras(out: Path):
    W = lambda n, s: (out / n).write_text(s, encoding="utf-8")
    W("wordmark.svg", wordmark_only())
    W("wordmark_reverse.svg", wordmark_only(reverse=True))
    W("wordmark_ink.svg", wordmark_only(mono=M.INK, tagline=False))
    W("monogram.svg", monogram())
    W("monogram_reverse.svg", monogram(reverse=True))
    W("brand_sheet.svg", brand_sheet())

    # social and application sizes, PNG plus JPG where a platform prefers it
    sizes = {"social_x_1600x900.png": (1600, 900, .26),
             "social_linkedin_1200x627.png": (1200, 627, .24),
             "social_square_1080.png": (1080, 1080, .16),
             "social_story_1080x1920.png": (1080, 1920, .10),
             "slide_title_1920x1080.png": (1920, 1080, .20),
             "email_strip_600x120.png": (600, 120, .30)}
    for name, (w, h, pf) in sizes.items():
        img = M.raster(max(w, h), pad_frac=pf, plate=M.PLATE, canvas=(w, h))
        img.save(out / name)
        img.convert("RGB").save(out / name.replace(".png", ".jpg"), quality=92)
    for n in ("og_nebelkraehe", "banner_1500x500", "avatar_400"):
        p = out / f"{n}.png"
        if p.exists():
            from PIL import Image
            Image.open(p).convert("RGB").save(out / f"{n}.jpg", quality=92)
    # PWA / app icons and a multi-size .ico
    for px in (192, 512):
        small_raster(px).save(out / f"icon_{px}.png")
    ico = small_raster(256)
    ico.save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])


if __name__ == "__main__":
    sys.exit(main())
