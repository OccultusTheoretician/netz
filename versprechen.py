#!/usr/bin/env python3
"""versprechen.py -- VERSPRECHEN-2026-09-02: the promise book's public face.

The AI-claims book (frontier item, reopened 2026-08-27) seals frontier labs'
own stated commitments as forecast rows before their outcomes: STATED versus
OPERATIONAL, applied to the people building the measurement stack. This tool
renders docs/versprechen.html from the two files that ARE the book:

    ai_claims_register_2026-08-27.json   the frozen-source register: design
                                         rulings, sources with archive.org
                                         snapshots, promises that resolved
                                         before the book opened (OBSERVED,
                                         never sealed), the freeze note
    ledger.json                          the sealed rows themselves, found by
                                         matching the register's seed
                                         statements; controls shown beside

Read-only against both. Static output; regenerate after any book ingest.
Nav is stamped by navgen.py (the page is listed in nav_manifest.json), so this
writer emits a bare <body> and never carries its own nav.
"""
from __future__ import annotations

import hashlib
import html
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REGISTER = HERE / "ai_claims_register_2026-08-27.json"
LEDGER = HERE / "ledger.json"
SEED = HERE / "ai_claims_seed_2026-08-27.json"
OUT = HERE / "docs" / "versprechen.html"

STYLE = (
    "body{background:#0c0e11;color:#d6d3cb;font-family:'IBM Plex Sans',sans-serif;"
    "max-width:900px;margin:0 auto;padding:0 1.25rem 3rem;font-size:15px;line-height:1.6}"
    ".kicker{font:500 .8rem 'IBM Plex Mono',monospace;letter-spacing:.06em;"
    "text-transform:uppercase;color:#8b8b85;margin-top:2.4rem}"
    "h1{color:#f2f0ea}h2{color:#e9e7e2;font-size:1.05rem;margin-top:2rem}"
    "table{border-collapse:collapse;margin:10px 0;font-family:'IBM Plex Mono',monospace;font-size:12.5px;width:100%}"
    "td,th{border:1px solid #26292f;padding:4px 10px;text-align:left;vertical-align:top}"
    "th{color:#8b8b85;font-weight:600}"
    "td.num{text-align:right;white-space:nowrap}"
    ".note{color:#8b8b85;max-width:46rem}.warn{color:#c9a227}"
    ".status-open{color:#8b8b85}.status-hit{color:#7fb069}.status-miss{color:#c05b4d}.status-void{color:#565650}"
    "a{color:#9db4c9}code{font-family:'IBM Plex Mono',monospace;font-size:.92em}"
)


def esc(s) -> str:
    return html.escape(str(s), quote=True)


def sha_lf(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def main() -> int:
    for p in (REGISTER, LEDGER, SEED):
        if not p.exists():
            print(f"versprechen: {p.name} not found - run from C:\\netz", file=sys.stderr)
            return 2
    reg = json.loads(REGISTER.read_text(encoding="utf-8-sig"))
    seed = json.loads(SEED.read_text(encoding="utf-8-sig"))
    led = json.loads(LEDGER.read_text(encoding="utf-8-sig"))
    rows = led["projections"]

    # the sealed book rows: matched by the register's own seed statements,
    # operator row plus its paired control, in seed order
    sealed = []
    for s in seed:
        stem = s["statement"][:60]
        ops = [r for r in rows if r["statement"][:60] == stem and r["model"] == "operator/human"]
        ctl = [r for r in rows if r["statement"][:60] == stem and r["model"] == "control/baserate"]
        for o in ops:
            sealed.append((o, ctl[0] if ctl else None))

    gen = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%MZ")
    as_of = led.get("as_of") or led.get("generated") or ""
    rsha = sha_lf(REGISTER)

    B = []
    B.append("<!doctype html><html lang='en'><head><meta charset='utf-8'>\n")
    B.append("<title>VERSPRECHEN</title>\n")
    B.append('<link rel="canonical" href="https://retroprescientaudit.com/versprechen.html">\n')
    B.append("<meta name='description' content='The promise book: frontier AI labs' stated commitments, "
             "sealed as forecast rows before their outcomes and adjudicated in public.'>\n")
    B.append("<meta property='og:image' content='https://retroprescientaudit.com/og_nebelkraehe.png'>\n")
    B.append("<meta name='viewport' content='width=device-width,initial-scale=1'>\n")
    B.append("<link rel='stylesheet' href='fonts/fonts.css'>\n")
    B.append(f"<style>{STYLE}</style><link rel=\"stylesheet\" href=\"brand.css\">\n")
    B.append("</head><body>\n")

    B.append("<div class='kicker'>Instrument</div>\n<h1>VERSPRECHEN</h1>\n")
    B.append("<p class='note'>The promise book. Frontier AI labs publish commitments with dates on them; "
             "this book seals those commitments as forecast rows before their outcomes, under the same gate, "
             "the same controls and the same adjudication as every other row on the desk. Stated versus "
             "operational, applied to the people building the measurement stack. "
             f"{esc(reg.get('book', ''))}.</p>\n")

    B.append("<h2>Sealed rows</h2>\n")
    B.append("<p class='note'>Each row quotes the promise as the lab stated it and names the page; the "
             "operator prices it and a climatological control seals in the same run. Rows resolve on the "
             "register's frozen sources, not on press.</p>\n")
    B.append("<table><tr><th>id</th><th>statement</th><th class='num'>p</th>"
             "<th>deadline</th><th>status</th><th>control</th></tr>\n")
    for o, c in sealed:
        st = o.get("status", "open")
        B.append("<tr>"
                 f"<td><code>{esc(o['id'])}</code></td>"
                 f"<td>{esc(o['statement'])}</td>"
                 f"<td class='num'>{esc(o['probability'])}%</td>"
                 f"<td class='num'>{esc(o['deadline'])}</td>"
                 f"<td class='status-{esc(st)}'>{esc(st)}</td>"
                 f"<td><code>{esc(c['id']) if c else '&mdash;'}</code></td>"
                 "</tr>\n")
    B.append("</table>\n")
    if not sealed:
        B.append("<p class='warn'>No sealed rows matched the register's seed statements; "
                 "the register and the ledger have drifted apart. Fix before publishing.</p>\n")

    B.append("<h2>Observed, never sealed</h2>\n")
    B.append("<p class='note'>Promises that resolved before the book could seal them. Logged with outcomes, "
             "excluded from every score: a row sealed after its outcome would be retrodiction, and the book "
             "keeps the same law as the ledger.</p>\n")
    B.append("<table><tr><th>promise</th><th>outcome</th><th>why not sealed</th></tr>\n")
    for ob in reg.get("observed_not_sealed", []):
        B.append("<tr>"
                 f"<td>{esc(ob.get('promise', ''))}</td>"
                 f"<td>{esc(ob.get('outcome', ''))}</td>"
                 f"<td>{esc(ob.get('why_not_sealed', ''))}</td>"
                 "</tr>\n")
    B.append("</table>\n")

    B.append("<h2>Frozen sources</h2>\n")
    B.append("<p class='note'>Every promise resolves against the page as it stood when the book opened. "
             f"{esc(str(reg.get('freeze_note', '')))}</p>\n")
    B.append("<table><tr><th>key</th><th>page</th><th>frozen</th></tr>\n")
    for s in reg.get("sources", []):
        url = s.get("url", ""); snap = s.get("snapshot", "")
        link = (f"<a href='{esc(url)}'>{esc(url)}</a>" if str(url).startswith("http") else esc(url))
        snaplink = (f"<a href='{esc(snap)}'>snapshot</a> {esc(s.get('frozen', ''))}"
                    if str(snap).startswith("http") else esc(s.get("frozen", "") or snap))
        B.append(f"<tr><td><code>{esc(s.get('key', ''))}</code></td><td>{link}</td><td>{snaplink}</td></tr>\n")
    B.append("</table>\n")

    B.append("<h2>Design rulings</h2>\n")
    for r in reg.get("design_rulings", []):
        B.append(f"<p class='note'>&mdash; {esc(r)}</p>\n")

    B.append(f"<p class='note'>Register <code>{esc(REGISTER.name)}</code> sha256 <code>{rsha[:16]}</code>; "
             f"ledger as of {esc(as_of)}; page generated {gen}. "
             "Everything above recomputes from the register and the ledger in the repository.</p>\n")
    B.append("</body></html>\n")

    OUT.write_text("".join(B), encoding="utf-8")
    print(f"versprechen: {OUT} written | sealed rows {len(sealed)} | observed "
          f"{len(reg.get('observed_not_sealed', []))} | sources {len(reg.get('sources', []))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
