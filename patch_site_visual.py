#!/usr/bin/env python3
"""
patch_site_visual.py — three confirmed visual changes, one script.

1. BACKGROUND HARMONIZATION. Every screen background to #080B0F (index's
   value). Changes the dark-theme --field in netz.py (kkr/ledger/report) and
   --ink in ohrwurm.py. Touches ONLY the screen root; the @media print white
   is left alone. Generated pages inherit on next render; this also rewrites
   the already-emitted docs/*.html so the change is visible without waiting
   for a regeneration.

2. MASTHEAD CROW. A crow lockup at the top of the hero on index.html (which is
   hand-authored — no generator writes it). Distinct from the radar-hub crow;
   uses the existing crow_mark.svg and the page's own tokens.

3. GROUPED INSTRUMENT INDEX. A five-section instrument breakout below the stat
   band on index.html, mirroring the nav groups, built from the page's own
   --messing/--line/--dim tokens so it reads native.

Idempotent throughout. Backups: netz.py.bak_visual, ohrwurm.py.bak_visual,
docs/index.html.bak_visual (once each). Run from C:\netz:
    python patch_site_visual.py
Then: python navgen.py   (keeps nav correct on the rewritten pages)
      python desk.py verify
"""
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DOCS = HERE / "docs"
TARGET_BG = "#080B0F"

changed = []


def backup_once(p, tag):
    b = p.with_name(p.name + f".bak_{tag}")
    if not b.exists():
        shutil.copy2(p, b)


# ---- 1a. netz.py dark --field (screen), NOT the print one ------------------
def fix_netz():
    p = HERE / "netz.py"
    if not p.exists():
        print("  netz.py absent — skipping generated-page background")
        return
    s = p.read_text(encoding="utf-8")
    # screen root is the one with --panel:#10141A beside it; print root has --panel:#fff
    old = "--field:#0B0D10; --panel:#10141A;"
    if old not in s:
        if f"--field:{TARGET_BG}; --panel:#10141A;" in s:
            print("  netz.py --field already harmonized")
        else:
            print("  netz.py screen --field anchor not found — SKIPPED (inspect by hand)")
        return
    backup_once(p, "visual")
    s = s.replace(old, f"--field:{TARGET_BG}; --panel:#10141A;")
    p.write_text(s, encoding="utf-8")
    changed.append("netz.py (--field -> %s)" % TARGET_BG)


# ---- 1b. ohrwurm.py --ink --------------------------------------------------
def fix_ohrwurm():
    p = HERE / "ohrwurm.py"
    if not p.exists():
        print("  ohrwurm.py absent — skipping")
        return
    s = p.read_text(encoding="utf-8")
    old = "--ink:#10131a;"
    if old not in s:
        if f"--ink:{TARGET_BG.lower()};" in s or f"--ink:{TARGET_BG};" in s:
            print("  ohrwurm.py --ink already harmonized")
        else:
            print("  ohrwurm.py --ink anchor not found — SKIPPED")
        return
    backup_once(p, "visual")
    s = s.replace(old, f"--ink:{TARGET_BG};")
    p.write_text(s, encoding="utf-8")
    changed.append("ohrwurm.py (--ink -> %s)" % TARGET_BG)


# ---- 1c. rewrite already-emitted docs pages so it shows now -----------------
def fix_emitted_pages():
    subs = [("--field:#0B0D10;", f"--field:{TARGET_BG};"),
            ("--ink:#10131a;", f"--ink:{TARGET_BG};")]
    n = 0
    for f in sorted(DOCS.glob("*.html")):
        t = f.read_text(encoding="utf-8")
        orig = t
        for a, b in subs:
            t = t.replace(a, b)
        if t != orig:
            f.write_text(t, encoding="utf-8")
            n += 1
    # mirror twins in forecasts so desk verify holds
    for tw in ("KKR_latest.html", "ledger.html"):
        tp = HERE / "forecasts" / tw
        if tp.exists():
            t = tp.read_text(encoding="utf-8")
            orig = t
            for a, b in subs:
                t = t.replace(a, b)
            if t != orig:
                tp.write_text(t, encoding="utf-8")
    if n:
        changed.append(f"{n} emitted docs page(s) + mirror twins")


# ---- 2 + 3. index.html: crow lockup + instrument index ---------------------
CROW_CSS = """<style id="masthead-crow-style">
.masthead-crow{display:flex;align-items:center;gap:.7rem;margin:0 0 1.15rem}
.masthead-crow img{width:38px;height:38px;opacity:.94}
.masthead-crow .mc-word{font:600 .95rem 'IBM Plex Mono',ui-monospace,monospace;
  letter-spacing:.26em;text-transform:uppercase;color:#ECF1F7}
.masthead-crow .mc-sub{font:600 .56rem 'IBM Plex Mono',ui-monospace,monospace;
  letter-spacing:.2em;text-transform:uppercase;color:#5A6675;margin-top:.15rem}
</style>"""

CROW_HTML = """<div class="masthead-crow" aria-label="NebelKr&auml;he">
  <img src="crow_mark.svg" alt="">
  <div><div class="mc-word">Nebelkr&auml;he</div><div class="mc-sub">The Prescient Desk</div></div>
</div>"""

INDEX_CSS = """<style id="instrument-index-style">
.instr-index{position:relative;z-index:3;border-bottom:1px solid #1B222C;
  background:rgba(8,11,15,.55);padding:1.4rem 2rem}
.instr-index-in{max-width:1180px;margin:0 auto;display:grid;
  grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1.15rem 2rem}
.ii-group .ii-label{font:600 .58rem 'IBM Plex Mono',ui-monospace,monospace;
  letter-spacing:.2em;text-transform:uppercase;color:#8A6E30;
  padding-bottom:.5rem;margin-bottom:.5rem;border-bottom:1px solid #1E2630}
.ii-group a{display:block;text-decoration:none;padding:.16rem 0;
  font:600 .74rem 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;
  color:#9BA7B5}
.ii-group a:hover{color:#DCB65E}
.ii-group a .ii-desc{color:#5A6675;font-weight:400;letter-spacing:0;
  text-transform:none;font-size:.66rem;margin-left:.5rem}
</style>"""

# groups mirror the nav; short descriptors, hand-set
INDEX_GROUPS = [
    ("DESK", [("index.html", "Desk", "the face"),
              ("report.html", "Report", "daily brief"),
              ("spion.html", "Spion", "quiet channel")]),
    ("FORECASTING", [("kkr.html", "Forecasts", "scored calls"),
                     ("ledger.html", "Ledger", "the record"),
                     ("KriegForeKaster.html", "ForeKaster", "order of battle"),
                     ("globalkaster.html", "GlobalKaster", "world board"),
                     ("fogsim.html", "FogSim", "scenarios"),
                     ("okk.html", "OberKommando", "command")]),
    ("FEDERATION", [("kraehes_kalls.html", "Kalls", "abduction log"),
                    ("nest.html", "Nest", "forecasters")]),
    ("STANDARDS", [("standards.html", "Standards", "the method"),
                   ("conformance.html", "Conformance", "RPAS-26"),
                   ("register.html", "Register", "conformance"),
                   ("verify.html", "Verify", "run the check")]),
    ("CABINET", [("ohrwurm.html", "Ohrwurm", "phrase spread"),
                 ("konsole.html", "Konsole", "cipher"),
                 ("marks.html", "Marks", "heraldry")]),
]


def build_index_block():
    parts = [INDEX_CSS,
             '<div class="instr-index" id="instrument-index" '
             'aria-label="instruments"><div class="instr-index-in">']
    for label, links in INDEX_GROUPS:
        parts.append(f'<div class="ii-group"><div class="ii-label">{label}</div>')
        for href, name, desc in links:
            parts.append(f'<a href="{href}">{name}'
                         f'<span class="ii-desc">{desc}</span></a>')
        parts.append("</div>")
    parts.append("</div></div>")
    return "".join(parts)


def fix_index():
    p = DOCS / "index.html"
    if not p.exists():
        print("  docs/index.html absent — skipping crow + index")
        return
    s = p.read_text(encoding="utf-8")
    did = []

    # crow lockup — after the hero's opening rv block, before the kicker
    if 'id="masthead-crow-style"' not in s:
        anchor = ('<header class="hero-wrap"><div class="wrap"><div class="hero">\n'
                  '  <div class="rv in">\n')
        if anchor in s:
            backup_once(p, "visual")
            s = s.replace(anchor, CROW_CSS + anchor + "    " + CROW_HTML + "\n")
            did.append("masthead crow")
        else:
            print("  index hero anchor not found — crow SKIPPED")
    else:
        print("  masthead crow already present")

    # instrument index — after the band close
    if 'id="instrument-index-style"' not in s:
        band_close = ('<a class="go" href="ledger.html">Full record \u2192</a>\n'
                      '</div></div>')
        if band_close in s:
            if 'id="masthead-crow-style"' not in s:
                backup_once(p, "visual")
            s = s.replace(band_close, band_close + "\n\n" + build_index_block())
            did.append("instrument index")
        else:
            print("  band-close anchor not found — instrument index SKIPPED")
    else:
        print("  instrument index already present")

    if did:
        p.write_text(s, encoding="utf-8")
        changed.append("index.html (" + ", ".join(did) + ")")


def main():
    fix_netz()
    fix_ohrwurm()
    fix_emitted_pages()
    fix_index()
    print()
    if changed:
        print("changed:")
        for c in changed:
            print("  -", c)
    else:
        print("nothing changed (already patched).")
    print()
    print("next:  python navgen.py       (re-stamp nav on rewritten pages)")
    print("       python desk.py verify")
    return 0


if __name__ == "__main__":
    sys.exit(main())
