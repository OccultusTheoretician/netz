#!/usr/bin/env python3
"""
WAR DESK wiring — one-shot, idempotent.

Patches the two surfaces that consume Module 3's output:
  netz.py         -> injects the WAR DESK section into the daily battle report
                     (fresh only; staleness is printed, never silently omitted)
                     and gives it its own tab in the HTML report
  docs/index.html -> adds the live tile (a card + a band stat, fed by war_desk.json)

Run once:  python wardesk_wire.py
Re-run safe: every edit is sentinel-guarded and reports SKIP if already applied.
Rollback:  python wardesk_wire.py --revert   (restores the .bak written on first run)
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ------------------------------------------------------------------ netz.py

HELPER = '''

WARDESK_FILE = HERE / "forecasts" / "WARDESK_latest.md"


def war_desk_body(hours: int) -> str:
    """Body of the WAR DESK section, produced by tg_grade.py (Module 3).

    Freshness is a publication gate: a desk older than the report window is
    withheld and SAID to be withheld. An absent pull prints as an absent pull.
    """
    if not WARDESK_FILE.exists():
        return ("*No WAR DESK run on record. The Telegram cross-bias pipeline has not "
                "produced a graded file — section reports empty rather than omitted.*\\n")
    age = (datetime.now(timezone.utc).timestamp() - WARDESK_FILE.stat().st_mtime) / 3600
    if age > hours:
        return (f"*Last cross-bias pull ran {age:.1f}h ago, outside this {hours}h report "
                f"window. The stale desk is withheld rather than passed off as current.*\\n")
    body = WARDESK_FILE.read_text(encoding="utf-8")
    lines = body.split("\\n")
    if lines and lines[0].startswith("## "):   # heading re-issued below with the numeral
        lines = lines[1:]
    return "\\n".join(lines).strip() + "\\n"
'''

ANCHOR_HELPER = '''def render_report(config, clusters, conv, health, synth, model_used, hours, counts,'''

CALL = '''    out.append(f"## {next(sec)}. WAR DESK — CROSS-BIAS CONFIRMED EVENTS\\n")
    out.append(war_desk_body(hours))
    out.append("")

'''

ANCHOR_CALL = '''    out.append(f"## {next(sec)}. PIR STATUS\\n")'''

TAB_OLD = '''    ("Command", ["KEY JUDGMENTS", "INDICATIONS", "PIR STATUS"]),'''
TAB_NEW = '''    ("Command", ["KEY JUDGMENTS", "INDICATIONS", "PIR STATUS"]),
    ("War Desk", ["WAR DESK"]),'''

# ------------------------------------------------------------- docs/index.html

CARD_ANCHOR = '''    <a class="card" href="https://github.com/OccultusTheoretician/voidsection">'''

CARD = '''    <a class="card" href="report.html#tab_wardesk">
      <span class="card-k">Verification instrument</span>
      <span class="card-t">The War Desk</span>
      <span class="card-d">Armed-conflict claims graded by who disagrees. A report is single-source until an <em>independently-biased</em> channel corroborates it; when enemies agree an event happened, it happened. Single-source claims are counted and withheld.</span>
      <span class="card-go">Confirmed events &rarr;</span>
    </a>
'''

BAND_ANCHOR = '''  <span class="asof" id="b-asof">Live from the ledger</span>'''

BAND = '''  <div class="stat"><span class="lbl">War Desk A/B</span><span class="val" id="b-wd">—</span></div>
'''

JS_ANCHOR = '''})();
</script>
</body></html>'''

JS = '''})();
(function(){
  fetch('war_desk.json').then(function(r){return r.json()}).then(function(d){
    var g=d.grades||{}; var el=document.getElementById('b-wd');
    if(el) el.textContent=(g.A||0)+'A / '+(g.B||0)+'B';
  }).catch(function(){});
})();
</script>
</body></html>'''


def edit(path: Path, sentinel: str, anchor: str, insert: str, before: bool = True,
         replace: tuple[str, str] | None = None) -> str:
    if not path.exists():
        return f"MISS  {path.name} not found"
    src = path.read_text(encoding="utf-8")
    if sentinel in src:
        return f"SKIP  {path.name}: already wired"
    if replace:
        old, new = replace
        if old not in src:
            return f"FAIL  {path.name}: replace-anchor not found"
        src = src.replace(old, new, 1)
    else:
        if anchor not in src:
            return f"FAIL  {path.name}: anchor not found — patch by hand"
        src = src.replace(anchor, (insert + anchor) if before else (anchor + insert), 1)
    bak = path.with_suffix(path.suffix + ".bak")
    if not bak.exists():
        shutil.copy2(path, bak)
    path.write_text(src, encoding="utf-8")
    return f"OK    {path.name}: wired"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--revert", action="store_true", help="restore .bak files")
    args = ap.parse_args()

    netz, index = HERE / "netz.py", HERE / "docs" / "index.html"

    if args.revert:
        for p in (netz, index):
            bak = p.with_suffix(p.suffix + ".bak")
            if bak.exists():
                shutil.copy2(bak, p)
                print(f"REVERT {p.name}")
            else:
                print(f"NOBAK  {p.name}")
        return 0

    print(edit(netz, "def war_desk_body", ANCHOR_HELPER, HELPER + "\n\n", before=True))
    print(edit(netz, 'WAR DESK — CROSS-BIAS CONFIRMED EVENTS\\n")', ANCHOR_CALL, CALL, before=True))
    print(edit(netz, '("War Desk"', "", "", replace=(TAB_OLD, TAB_NEW)))
    print(edit(index, 'card-t">The War Desk', CARD_ANCHOR, CARD, before=True))
    print(edit(index, 'id="b-wd"', BAND_ANCHOR, BAND, before=True))
    print(edit(index, "war_desk.json", "", "", replace=(JS_ANCHOR, JS)))
    print("\n.bak written alongside each file on first run · `--revert` restores them")
    return 0


if __name__ == "__main__":
    sys.exit(main())
