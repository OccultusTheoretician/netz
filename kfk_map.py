#!/usr/bin/env python3
r"""
kfk_map.py - the KriegForeKaster overlay face: docs\kfk_map.html.

THE FACE'S HONESTY IS ITS CONTENT. The record's own doctrine renders
visibly instead of living in a comment:

  - COMMAND_PRECISION coordinates (headquarters, installation centroid)
    draw SOLID. STATE_PRECISION (capital centroid, approximate) draw
    HOLLOW-DASHED - a capital centroid locates a state, not a command,
    and the face says so per point instead of counting it as located.
  - Existence grade dims the point: SPECULATIVE (NEVER_ISSUE) renders
    near-ghost; DOCUMENTED/REPORTED lit. The board shows what the desk
    knows apart from what it merely lists.
  - Location half-life (14d) fades opacity past staleness; the claim
    that has outlived its half-life looks like it.
  - A brass ring marks formations sighted in the graded WarDesk stream
    within 72h (forecasts\kfk_sightings_latest.json, fail-open absent).

Zero external assets, no tiles, no scripts required for render: pure SVG
on the house tokens. Equirectangular world plot with a 30-degree
graticule; labels only above armed-forces echelon to keep the ghost
skeleton quiet and the real order-of-battle loud.

    python kfk_map.py            -> docs\kfk_map.html
After first generation: add {"href":"kfk_map.html","text":"Overlay"} to
nav_manifest.json (FORECASTING group, after ForeKaster), then
python navgen.py, then publish.
"""

import json
import sys
from datetime import date, datetime, timezone
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "KriegForeKaster.json"
SIGHT = HERE / "forecasts" / "kfk_sightings_latest.json"
OUT = HERE / "docs" / "kfk_map.html"

COMMAND = {"headquarters", "installation centroid"}
LOC_HALFLIFE_D = 14
SIGHT_RING_H = 72

W, H, PAD = 1200, 620, 28
FACTION_PALETTE = ["#DCB65E", "#8EB4D8", "#C97B7B", "#8FBF9F", "#B79BD8",
                   "#D8A87B", "#7BC9C1", "#C9C97B", "#A0A9B4"]
ECH_R = {"armed forces": 3.2, "service": 3.6, "theater": 4.2, "front": 4.2,
         "army group": 4.6, "army": 4.6, "command": 4.6, "corps": 5.2,
         "division": 4.6, "brigade": 4.0, "regiment": 3.6, "battalion": 3.2,
         "company": 2.8, "detachment": 2.8, "unit": 3.4}
LABEL_ECH = {"corps", "division", "brigade", "command", "unit", "army",
             "army group", "front", "theater"}


def xy(lat, lon):
    x = PAD + (lon + 180.0) / 360.0 * (W - 2 * PAD)
    y = PAD + (90.0 - lat) / 180.0 * (H - 2 * PAD)
    return round(x, 1), round(y, 1)


def days_since(iso, today):
    try:
        y, m, d = map(int, str(iso)[:10].split("-"))
        return (today - date(y, m, d)).days
    except Exception:
        return None


def main() -> int:
    d = json.loads(DATA.read_text(encoding="utf-8"))
    recs = d.get("formations") or d.get("records") or []
    sight = {}
    if SIGHT.exists():
        try:
            sight = json.loads(SIGHT.read_text(encoding="utf-8")).get("sightings", {})
        except Exception as exc:
            print(f"kfk_map - sightings unreadable ({exc}) - rendering without "
                  f"the recency layer (fail-open)", file=sys.stderr)
    today = datetime.now(timezone.utc).date()
    now = datetime.now(timezone.utc)

    factions = sorted({r.get("faction", "?") for r in recs})
    color = {f: FACTION_PALETTE[i % len(FACTION_PALETTE)]
             for i, f in enumerate(factions)}

    pts, labels, rings = [], [], []
    n_cmd = n_state = n_nocoord = n_spec = 0
    for r in recs:
        loc = r.get("location") or {}
        lat, lon = loc.get("lat"), loc.get("lon")
        grade = ((r.get("existence") or {}).get("grade")) or "?"
        if grade == "SPECULATIVE":
            n_spec += 1
        if lat is None or lon is None:
            n_nocoord += 1
            continue
        solid = loc.get("denotes") in COMMAND
        n_cmd += 1 if solid else 0
        n_state += 0 if solid else 1
        x, y = xy(lat, lon)
        rr = ECH_R.get(r.get("echelon", ""), 3.4)
        c = color.get(r.get("faction", "?"), "#AEB9C6")
        op = 0.28 if grade == "SPECULATIVE" else 0.95
        ds = days_since(loc.get("as_of"), today)
        if ds is not None and ds > LOC_HALFLIFE_D:
            op = max(0.15, op * (LOC_HALFLIFE_D / ds))
        title = (f"{r.get('name','')} [{r.get('designation','')}] - "
                 f"{r.get('faction','')} - {r.get('echelon','')} - existence "
                 f"{grade} - location {loc.get('denotes','?')} as_of "
                 f"{loc.get('as_of','?')}")
        style = (f'fill="{c}" fill-opacity="{op:.2f}"' if solid else
                 f'fill="none" stroke="{c}" stroke-opacity="{op:.2f}" '
                 f'stroke-width="1.3" stroke-dasharray="2.5 2"')
        pts.append(f'<circle cx="{x}" cy="{y}" r="{rr}" {style}>'
                   f'<title>{escape(title)}</title></circle>')
        sr = sight.get(r.get("id"))
        if sr and sr.get("last"):
            try:
                last = datetime.fromisoformat(str(sr["last"]).replace("Z", "+00:00"))
                if last.tzinfo is None:
                    last = last.replace(tzinfo=timezone.utc)
                if (now - last).total_seconds() / 3600 <= SIGHT_RING_H:
                    rings.append(
                        f'<circle cx="{x}" cy="{y}" r="{rr+3.5}" fill="none" '
                        f'stroke="#DCB65E" stroke-width="1.4" stroke-opacity=".9">'
                        f'<title>{escape(r.get("name",""))} - sighted in graded '
                        f'WarDesk stream, last {escape(str(sr["last"])[:16])}Z '
                        f'({sr.get("n",0)} hit(s), top grade {sr.get("top_grade")})'
                        f'</title></circle>')
            except Exception:
                pass
        if r.get("echelon") in LABEL_ECH:
            labels.append(f'<text x="{x+7}" y="{y+3}" class="lbl">'
                          f'{escape(r.get("designation") or r.get("name",""))}'
                          f'</text>')

    grat = []
    for lon in range(-180, 181, 30):
        x, _ = xy(0, lon)
        grat.append(f'<line x1="{x}" y1="{PAD}" x2="{x}" y2="{H-PAD}"/>')
    for lat in range(-60, 91, 30):
        _, y = xy(lat, 0)
        grat.append(f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}"/>')

    legend_fac = "".join(
        f'<span class="lg"><i style="background:{color[f]}"></i>{escape(f)}'
        f' <b>{sum(1 for r in recs if r.get("faction")==f)}</b></span>'
        for f in factions)

    sight_meta = ""
    if sight:
        sighted72 = len(rings)
        sight_meta = (f' - sighted &le;{SIGHT_RING_H}h: <b>{sighted72}</b>')

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Overlay - KriegForeKaster - Retro-Prescient Audit</title>
<link rel="canonical" href="https://retroprescientaudit.com/kfk_map.html">
<meta name="description" content="The KriegForeKaster board plotted with its own doctrine visible: command-located versus state-only coordinates, existence grades, location half-life, and WarDesk sighting recency.">
<meta property="og:title" content="KFK Overlay &middot; The Prescient Desk">
<meta property="og:description" content="An order-of-battle face that shows what the desk knows apart from what it merely lists. Solid points locate commands; dashed points locate states.">
<meta property="og:image" content="https://retroprescientaudit.com/og_nebelkraehe.png">
<meta property="og:url" content="https://retroprescientaudit.com/kfk_map.html">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="fonts/fonts.css">
<style>
:root{{--nacht:#080B0F;--nacht2:#0C1015;--panel:#0F131A;--hair:#1B222C;
--fg:#ECF1F7;--dim:#AEB9C6;--faint:#5c6672;--messing:#DCB65E;
--messing-dim:rgba(220,182,94,.55);--mono:'IBM Plex Mono',ui-monospace,monospace;
--sans:'IBM Plex Sans',system-ui,sans-serif}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:var(--nacht);color:var(--fg);font-family:var(--sans);
font-weight:300;line-height:1.6;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1240px;margin:0 auto;padding:2.6rem 1.2rem 4rem}}
.kicker{{font-family:var(--mono);font-size:.72rem;letter-spacing:.22em;
text-transform:uppercase;color:var(--messing-dim)}}
h1{{font-weight:200;font-size:clamp(1.7rem,4vw,2.5rem);margin:.4rem 0 .8rem}}
.stand{{font-family:var(--mono);font-size:.72rem;color:var(--faint);margin-bottom:1.6rem}}
.doctrine{{color:var(--dim);max-width:74ch;font-size:.95rem;margin-bottom:1.6rem}}
.board{{border:1px solid var(--hair);background:var(--panel);border-radius:6px;
padding:.6rem;overflow-x:auto}}
svg{{display:block;min-width:900px;width:100%;height:auto}}
.grat line{{stroke:#161B22;stroke-width:1}}
.lbl{{font-family:var(--mono);font-size:8.5px;fill:#AEB9C6}}
.strip{{display:flex;flex-wrap:wrap;gap:.5rem 1.6rem;align-items:baseline;
font-family:var(--mono);font-size:.72rem;color:var(--dim);padding:.9rem .4rem 0}}
.strip b{{color:var(--messing)}}
.lg i{{display:inline-block;width:.7em;height:.7em;border-radius:50%;
margin-right:.4em;vertical-align:baseline}}
.key{{font-family:var(--mono);font-size:.7rem;color:var(--faint);
padding:.5rem .4rem 0;max-width:100ch}}
footer{{border-top:1px solid var(--hair);margin-top:2rem;padding-top:1rem;
font-family:var(--mono);font-size:.68rem;color:var(--faint)}}
</style>
</head>
<body>
<div class="wrap">
<div class="kicker">(U//OS) - KriegForeKaster - order of battle</div>
<h1>The Overlay</h1>
<div class="stand">generated {now.strftime('%d%H%MZ %b %y').upper()} - record as_of {escape(str(d.get('as_of','?')))} - {len(recs)} formation(s)</div>
<p class="doctrine">The board renders its own doctrine instead of hiding it in a comment. <strong>Solid points locate a command</strong> (headquarters or installation centroid); <strong>dashed hollow points locate a state</strong> - a capital centroid is an honest coordinate declaring that nobody has sourced where the formation sits. SPECULATIVE existence renders near-ghost and can never fuel a forecast; claims past their location half-life fade. A brass ring is a formation named in the graded WarDesk stream inside {SIGHT_RING_H} hours.</p>
<div class="board">
<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="KriegForeKaster formations plotted on an equirectangular world grid">
<g class="grat">{''.join(grat)}</g>
{''.join(pts)}
{''.join(rings)}
{''.join(labels)}
</svg>
</div>
<div class="strip">
<span>command-located <b>{n_cmd}</b></span>
<span>state-only <b>{n_state}</b></span>
<span>no coordinate <b>{n_nocoord}</b></span>
<span>SPECULATIVE existence <b>{n_spec}</b> (never issues)</span>{sight_meta}
</div>
<div class="strip">{legend_fac}</div>
<p class="key">key: point size = echelon - solid fill = command precision - dashed hollow = state precision - dimmed = SPECULATIVE or past location half-life ({LOC_HALFLIFE_D}d) - brass ring = WarDesk sighting &le;{SIGHT_RING_H}h. Hover any point for the claim, its grade, and its as_of.</p>
<footer>RETRO-PRESCIENT AUDIT(TM) - {escape(str(d.get('disclosure',''))[:220])}</footer>
</div>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"kfk_map - {n_cmd} command-located + {n_state} state-only plotted "
          f"({n_nocoord} without coordinates) - {len(rings)} sighting ring(s) "
          f"-> {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
