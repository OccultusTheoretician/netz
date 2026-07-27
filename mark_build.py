#!/usr/bin/env python3
"""
mark_build.py — one geometry, every asset.

The Nebelkraehe mark exists in exactly one place: the vertex table below. Every
file the site serves is generated from it. Nothing is hand-edited downstream,
for the same reason docs/ledger.json is a build product and not a copy someone
remembers to make.

    python mark_build.py [outdir]

Emits
    crow_mark.svg           the mark, transparent, for the page
    crow_mark_square.svg    1:1 lockup for avatars and profile images
    crow_mark_512.png       raster fallback
    apple-touch-icon.png    180x180, opaque dark plate
    favicon.png             48x48
    og_nebelkraehe.png      1200x630 social card
"""

import json, math, sys
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

# ----------------------------------------------------------------------
# GEOMETRY — source coordinates, from the traced original. Frozen.
# ----------------------------------------------------------------------
BODY = [(147,2), (256,27), (262,114), (266,123), (473,83), (484,86),
        (600,147), (555,166), (607,187), (551,209), (580,232), (568,235),
        (569,238), (723,294), (571,294), (454,255), (419,261), (269,217),
        (266,123), (232,136), (247,167), (200,161), (202,198), (162,157),
        (168,111), (184,107), (183,104), (163,90), (135,78), (2,51)]

# the whole neck contour: body leading edge, apex, head underside, both feather
# spikes, chin, front slit
NECK = [(269,217),(266,123),(232,136),(247,167),(200,161),(202,198),(162,157),(168,111)]

SHOULDER = None   # filled from panels.json
BELLY = None

EYE_C   = (154.0, 48.0)
EYE_ANG = 13.0
EYE_HL  = 17.0
EYE_TH  = 5.0

INK   = "#0f1216"
GREY  = "#b3b9b3"
LIGHT = "#eef1f5"
PLATE = "#0e0f11"          # site background, for opaque plates
TRIM  = 22                 # stroke centred on the edge; half shows inside

FOG = [(0.00, (0x0f,0x12,0x16), 1.00),
       (0.60, (0x0f,0x12,0x16), 1.00),
       (0.73, (0x34,0x3b,0x42), 1.00),
       (0.84, (0x46,0x4e,0x56), 0.90),
       (0.93, (0x53,0x5b,0x63), 0.50),
       (1.00, (0x5d,0x65,0x6d), 0.00)]


# The slit as signed off, source coordinates, verbatim. Recomputing it from the
# angle/length parameters lands 0.5px away because of rounding order; the approved
# artwork is the artwork.
EYE_SLIT = [(137.9, 43.7), (158.5, 43.3), (171.1, 51.3), (154.6, 51.5)]


def eye_slit():
    return EYE_SLIT


def load_panels(path):
    global SHOULDER, BELLY
    d = json.loads(Path(path).read_text())
    SHOULDER = [tuple(p) for p in d["shoulder"]]
    BELLY = [tuple(p) for p in d["belly"]]


# ----------------------------------------------------------------------
def bbox():
    xs=[p[0] for p in BODY]; ys=[p[1] for p in BODY]
    return min(xs), min(ys), max(xs), max(ys)


def svg(pad=4, square=False, plate=None):
    minx,miny,maxx,maxy = bbox()
    w,h = maxx-minx+pad*2, maxy-miny+pad*2
    ox,oy = pad-minx, pad-miny
    if square:
        side = max(w,h)
        ox += (side-w)/2; oy += (side-h)/2; w=h=side
    T = lambda p:(round(p[0]+ox,1), round(p[1]+oy,1))
    d   = lambda pl:"M"+" L".join(f"{x} {y}" for x,y in pl)+" Z"
    dop = lambda pl:"M"+" L".join(f"{x} {y}" for x,y in pl)
    g1 = T(BODY[-1]); g2 = T(BODY[13])
    stops = "\n      ".join(
        f'<stop offset="{o:.2f}" stop-color="#{c[0]:02x}{c[1]:02x}{c[2]:02x}" stop-opacity="{a}"/>'
        for o,c,a in FOG)
    bg = f'\n  <rect width="{w}" height="{h}" fill="{plate}"/>' if plate else ""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Nebelkr&#228;he mark">
  <defs>
    <linearGradient id="fog" gradientUnits="userSpaceOnUse" x1="{g1[0]}" y1="{g1[1]}" x2="{g2[0]}" y2="{g2[1]}">
      {stops}
    </linearGradient>
    <clipPath id="body"><path d="{d([T(p) for p in BODY])}"/></clipPath>
  </defs>{bg}
  <path d="{d([T(p) for p in BODY])}" fill="url(#fog)"/>
  <g clip-path="url(#body)" fill="{GREY}" stroke="{GREY}" stroke-linejoin="miter" stroke-miterlimit="4">
    <path d="{d([T(p) for p in SHOULDER])}" stroke-width="0"/>
    <path d="{d([T(p) for p in BELLY])}" stroke-width="0"/>
    <path d="{dop([T(p) for p in NECK])}" fill="none" stroke-width="{TRIM}" stroke-linecap="butt"/>
  </g>
  <path d="{d([T(p) for p in eye_slit()])}" fill="{LIGHT}"/>
</svg>
'''


# ----------------------------------------------------------------------
def raster(px_w, pad_frac=0.06, plate=None, canvas=None, SS=4):
    """Render the mark. Supersampled, then downsampled — no library needed."""
    minx,miny,maxx,maxy = bbox()
    bw,bh = maxx-minx, maxy-miny
    cw,ch = canvas if canvas else (px_w, round(px_w*bh/bw))
    inner = min(cw*(1-2*pad_frac)/bw, ch*(1-2*pad_frac)/bh)
    s = inner*SS
    W,H = cw*SS, ch*SS
    ox = (W - bw*s)/2 - minx*s
    oy = (H - bh*s)/2 - miny*s
    T = lambda p:(p[0]*s+ox, p[1]*s+oy)

    mask = Image.new("L",(W,H),0); ImageDraw.Draw(mask).polygon([T(p) for p in BODY], fill=255)
    # fog gradient along the beak->tail axis
    a=T(BODY[-1]); b=T(BODY[13])
    vx,vy=b[0]-a[0], b[1]-a[1]; L2=vx*vx+vy*vy
    grad=Image.new("RGBA",(W,H),(0,0,0,0)); gp=grad.load()
    xsb=[p[0] for p in [T(q) for q in BODY]]; ysb=[p[1] for p in [T(q) for q in BODY]]
    for y in range(int(min(ysb)), int(max(ysb))+1):
        for x in range(int(min(xsb)), int(max(xsb))+1):
            t=((x-a[0])*vx+(y-a[1])*vy)/L2
            t=0 if t<0 else (1 if t>1 else t)
            for i in range(len(FOG)-1):
                o0,c0,a0=FOG[i]; o1,c1,a1=FOG[i+1]
                if t<=o1 or i==len(FOG)-2:
                    f=0 if o1==o0 else (t-o0)/(o1-o0); f=max(0,min(1,f))
                    gp[x,y]=(round(c0[0]+(c1[0]-c0[0])*f), round(c0[1]+(c1[1]-c0[1])*f),
                             round(c0[2]+(c1[2]-c0[2])*f), round(255*(a0+(a1-a0)*f)))
                    break
    img=Image.new("RGBA",(W,H),(0,0,0,0))
    img.paste(grad,(0,0),mask)
    lay=Image.new("L",(W,H),0); dl=ImageDraw.Draw(lay)
    dl.polygon([T(p) for p in SHOULDER], fill=255)
    dl.polygon([T(p) for p in BELLY], fill=255)
    dl.line([T(p) for p in NECK], fill=255, width=round(TRIM*s), joint="curve")
    lay=Image.composite(lay, Image.new("L",(W,H),0), mask)
    img.paste(Image.new("RGBA",(W,H),tuple(int(GREY[i:i+2],16) for i in (1,3,5))+(255,)),(0,0),lay)
    el=Image.new("L",(W,H),0); ImageDraw.Draw(el).polygon([T(p) for p in eye_slit()], fill=255)
    img.paste(Image.new("RGBA",(W,H),tuple(int(LIGHT[i:i+2],16) for i in (1,3,5))+(255,)),(0,0),el)
    img=img.resize((cw,ch), Image.LANCZOS)
    if plate:
        bgim=Image.new("RGBA",(cw,ch),tuple(int(plate[i:i+2],16) for i in (1,3,5))+(255,))
        bgim.alpha_composite(img); img=bgim
    return img


def main():
    load_panels(Path(__file__).with_name("panels.json"))
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/"crow_mark.svg").write_text(svg(), encoding="utf-8")
    (OUT/"crow_mark_square.svg").write_text(svg(pad=40, square=True), encoding="utf-8")
    raster(512).save(OUT/"crow_mark_512.png")
    raster(180, pad_frac=.12, plate=PLATE, canvas=(180,180)).save(OUT/"apple-touch-icon.png")
    raster(48,  pad_frac=.06, canvas=(48,48)).save(OUT/"favicon.png")
    raster(1200, pad_frac=.22, plate=PLATE, canvas=(1200,630)).save(OUT/"og_nebelkraehe.png")
    for f in sorted(OUT.iterdir()):
        print(f"  {f.name:24s} {f.stat().st_size:>8,} bytes")


if __name__ == "__main__":
    main()
