#!/usr/bin/env python3
"""patch_footer_uniform_kk16.py — footer uniformity + sigil off the radar.
Report-only by default; --apply writes. Idempotent; byte-level UTF-8.

A. The 14 pages carrying the bare `© 2026 NebelKrähe` get the full legal-page
   format: © 2026 NebelKrähe · LICENSE · Terms · Privacy.
B. The netz-generated pages (kkr, ledger, report) already link Terms · Privacy
   in their legalline (single-quoted hrefs — which is why a double-quote grep
   missed them); the © and LICENSE are added to netz.py's footer string so
   regeneration carries them, AND stamped identically into the three shipped
   pages plus both forecasts/ mirror twins so the mirrors stay byte-equal.
C. The big centered sigil comes off the radar: sigil img removed, rings and hub
   stacking restored. The orbiting crow and the 150px masthead lockup stay.

Never touches forecasts/ dated packets, ledger.json, hashlogs, or sealed rows.
Pages with no footer block at all (fogsim, spion, konsole) are named in the
report and left untouched — their writers are separate tools.
"""
import argparse
from pathlib import Path

ROOT = Path(".").resolve()

# ---- A: bare line -> full format (double-quoted hrefs, legal-page style) ----
A_OLD = "<br>\u00a9 2026 NebelKr\u00e4he</".encode("utf-8")
A_NEW = ("<br>\u00a9 2026 NebelKr\u00e4he \u00b7 "
         '<a href="https://github.com/OccultusTheoretician/netz/blob/main/LICENSE">LICENSE</a> \u00b7 '
         '<a href="terms.html">Terms</a> \u00b7 <a href="privacy.html">Privacy</a></').encode("utf-8")
A_MARK = "NebelKr\u00e4he \u00b7 <a href=\"https".encode("utf-8")

# ---- B: netz legalline (single-quoted hrefs, matches the generator string) ----
B_OLD = "margin:.2rem 0 .5rem'><a href='terms.html'>".encode("utf-8")
B_NEW = ("margin:.2rem 0 .5rem'>\u00a9 2026 NebelKr\u00e4he \u00b7 "
         "<a href='https://github.com/OccultusTheoretician/netz/blob/main/LICENSE'>LICENSE</a> \u00b7 "
         "<a href='terms.html'>").encode("utf-8")
B_MARK = "'>\u00a9 2026 NebelKr\u00e4he \u00b7 <a href='https".encode("utf-8")
B_PAGES = ["docs/kkr.html", "docs/ledger.html", "docs/report.html",
           "forecasts/KKR_latest.html", "forecasts/ledger.html"]
BP_OLD = "THE PRESCIENT DESK</div><div class='colophon'>".encode("utf-8")
BP_NEW = ("THE PRESCIENT DESK</div>"
          "<div class='legalline' style='font-size:.72rem;opacity:.7;margin:.2rem 0 .5rem'>"
          "\u00a9 2026 NebelKr\u00e4he \u00b7 "
          "<a href='https://github.com/OccultusTheoretician/netz/blob/main/LICENSE'>LICENSE</a> \u00b7 "
          "<a href='terms.html'>Terms</a> \u00b7 <a href='privacy.html'>Privacy</a></div>"
          "<div class='colophon'>").encode("utf-8")

# ---- C: sigil revert (exact bytes the kk16 polish patch applied) ----
C1_OLD = (b".sigil{position:absolute;left:50%;top:50%;width:54%;transform:translate(-50%,-50%);z-index:1;\n"
          b"  filter:drop-shadow(0 0 26px rgba(220,182,94,.26)) drop-shadow(0 4px 14px rgba(0,0,0,.6))}\n"
          b".rings{position:absolute;inset:0;z-index:2}")
C1_NEW = b".rings{position:absolute;inset:0}"
C2_OLD = b".hub{position:absolute;z-index:3;left:50%"
C2_NEW = b".hub{position:absolute;left:50%"
C3_OLD = (b'<div class="beam" aria-hidden="true"></div>\n'
          b'    <img class="sigil" src="crow_mark.svg" alt="" aria-hidden="true">')
C3_NEW = b'<div class="beam" aria-hidden="true"></div>'


def swap(path, old, new, mark, note, apply, log, all_hits=False):
    p = ROOT / path
    if not p.exists():
        log.append(("MISS", path, f"file absent \u2014 {note}")); return
    b = p.read_bytes()
    if mark and mark in b:
        log.append(("OK", path, f"already applied \u2014 {note}")); return
    if old in b:
        if apply:
            p.write_bytes(b.replace(old, new) if all_hits else b.replace(old, new, 1))
        log.append(("FIX" if apply else "WOULD", path, note)); return
    log.append(("MISS", path, f"target not found \u2014 {note}"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a, log = ap.parse_args(), []

    # A — upgrade every bare line under docs/
    for p in sorted((ROOT / "docs").glob("*.html")):
        b = p.read_bytes()
        if A_MARK in b:
            continue                       # legal pages and any already-upgraded
        if A_OLD in b:
            if a.apply:
                p.write_bytes(b.replace(A_OLD, A_NEW, 1))
            log.append(("FIX" if a.apply else "WOULD", f"docs/{p.name}",
                        "\u00a9 line \u2192 full LICENSE \u00b7 Terms \u00b7 Privacy format"))

    # B — generator, then the shipped pages + mirror twins (which predate the
    # legalline wiring: byline meets colophon directly, so the full div lands there)
    swap("netz.py", B_OLD, B_NEW, B_MARK, "legalline: \u00a9 + LICENSE added", a.apply, log)
    for f in B_PAGES:
        swap(f, BP_OLD, BP_NEW, B_MARK, "legalline stamped (\u00a9 + LICENSE + Terms/Privacy)", a.apply, log)

    # C — sigil off the radar; orbiter and masthead untouched
    swap("docs/index.html", C1_OLD, C1_NEW, C1_NEW + b"\n", "revert: sigil css, rings restored", a.apply, log)
    swap("docs/index.html", C2_OLD, C2_NEW, C2_NEW, "revert: hub stacking restored", a.apply, log)
    p = ROOT / "docs/index.html"; b = p.read_bytes()
    if b'<img class="sigil"' not in b:
        log.append(("OK", "docs/index.html", "already applied \u2014 sigil img absent"))
    elif C3_OLD in b:
        if a.apply:
            p.write_bytes(b.replace(C3_OLD, C3_NEW, 1))
        log.append(("FIX" if a.apply else "WOULD", "docs/index.html", "revert: sigil img removed"))
    else:
        log.append(("MISS", "docs/index.html", "sigil img present but anchor not found"))

    for s, f, note in log:
        print(f"{s:5s} {f} \u2014 {note}")
    nofoot = [f.name for f in sorted((ROOT / "docs").glob("*.html"))
              if b"<footer" not in (f.read_bytes()) and b"legalline" not in f.read_bytes()]
    print("\npages with no footer block at all (writers are separate tools; untouched): "
          + (", ".join(nofoot) if nofoot else "none"))
    if not a.apply:
        print("report only \u2014 rerun with --apply to write")


if __name__ == "__main__":
    main()
