#!/usr/bin/env python3
"""patch_site_polish_kk16.py — four fixes in one pass. Report-only by default; --apply writes.

A. LEGAL-PAGE LEGIBILITY — privacy.html/terms.html declare no text or link color,
   so body text falls back to browser-default BLACK on the site's #080B0F field and
   links to default blue/purple. Adds body/h1/strong/a colors from the site palette
   to both pages AND to patch_legal_pages.py (the generator of record).
B. CASING — every remaining `NebelK` (capital K, all encodings: ä / &auml; / &#228;)
   becomes `NebelK`. Skips, by name and with reason: the dated site-audit record and
   the four patcher scripts whose NebelK strings are search patterns for this defect.
C. COPYRIGHT — footer line `© 2026 NebelKrähe` on every docs/*.html that has a
   <footer> and lacks one. Legal pages already carry it; pages with no footer element
   are left alone.
D. HERO — the masthead crow was 38x38 on a 729x300 SVG (letterboxed to a ~15px-tall
   bird); enlarged to a proper lockup. The leuchte's aria-label promises "the
   NebelKrähe sigil within sighting rings" but the center held only a 5px hub — the
   sigil now sits centered under the rings, with the ticker and orbit above it.

Idempotent: run twice, second run reports nothing to do. All edits are byte-level
UTF-8 with no newline normalization. Never touches forecasts/ dated packets,
ledger.json, hashlogs, or any sealed record.
"""
import argparse, subprocess, sys
from pathlib import Path

ROOT = Path(".").resolve()

CASING_SKIP = {
    "SITE_AUDIT_2026-07-30.md": "dated audit record — it names this defect; printed, not repaired",
    "patch_generators_seo.py":  "its NebelK strings are search patterns for this defect",
    "patch_marks_tm.py":        "search pattern",
    "patch_site_audit_fix.py":  "search pattern",
    "patch_site_marks_fix.py":  "search pattern",
}
NEVER_TOUCH_PREFIX = ("forecasts/", ".git/")
NEVER_TOUCH_NAMES  = {"ledger.json", "kalls_hashlog.json"}

FOOT_RULE = b"footer{margin-top:2.5rem;padding-top:1rem;border-top:1px solid #26292f;font-size:.8rem;opacity:.8}"
LEGIBILITY_ADD = FOOT_RULE + b"\nbody{color:#c9c9c2}h1{color:#e8eaed}strong{color:#e8eaed}a{color:#dcb65e}"
LEGIBILITY_MARK = b"body{color:#c9c9c2}"

COPY_LINE = "<br>\u00a9 2026 NebelKr\u00e4he".encode("utf-8")
COPY_MARK = "\u00a9 2026".encode("utf-8")

HERO = [
    # E1: masthead lockup — 38x38 letterboxed a 729x300 bird to ~15px tall
    (b".masthead-crow{display:flex;align-items:center;gap:.7rem;margin:0 0 1.15rem}\n"
     b".masthead-crow img{width:38px;height:38px;opacity:.94}\n"
     b".masthead-crow .mc-word{font:600 .95rem 'IBM Plex Mono',ui-monospace,monospace;\n"
     b"  letter-spacing:.26em;text-transform:uppercase;color:#ECF1F7}\n"
     b".masthead-crow .mc-sub{font:600 .56rem 'IBM Plex Mono',ui-monospace,monospace;\n"
     b"  letter-spacing:.2em;text-transform:uppercase;color:#5A6675;margin-top:.15rem}",
     b".masthead-crow{display:flex;align-items:center;gap:1rem;margin:0 0 1.4rem}\n"
     b".masthead-crow img{width:150px;height:auto;opacity:.96;filter:drop-shadow(0 0 14px rgba(220,182,94,.22))}\n"
     b".masthead-crow .mc-word{font:600 1.3rem 'IBM Plex Mono',ui-monospace,monospace;\n"
     b"  letter-spacing:.3em;text-transform:uppercase;color:#ECF1F7}\n"
     b".masthead-crow .mc-sub{font:600 .66rem 'IBM Plex Mono',ui-monospace,monospace;\n"
     b"  letter-spacing:.22em;text-transform:uppercase;color:#5A6675;margin-top:.2rem}",
     b"width:150px;height:auto",
     "masthead lockup enlarged (150px, aspect kept)"),
    # E2: sigil CSS + explicit stacking so the alert ticker stays above the bird
    (b".rings{position:absolute;inset:0}",
     b".sigil{position:absolute;left:50%;top:50%;width:54%;transform:translate(-50%,-50%);z-index:1;\n"
     b"  filter:drop-shadow(0 0 26px rgba(220,182,94,.26)) drop-shadow(0 4px 14px rgba(0,0,0,.6))}\n"
     b".rings{position:absolute;inset:0;z-index:2}",
     b".sigil{position:absolute",
     "sigil style added; rings/ticker stacked above it"),
    # E2b: hub dot above the sigil
    (b".hub{position:absolute;left:50%;top:50%;width:5px;",
     b".hub{position:absolute;z-index:3;left:50%;top:50%;width:5px;",
     b".hub{position:absolute;z-index:3",
     "hub above sigil"),
    # E3: sigil markup — beam, then sigil, then rings, so rings paint over the bird
    (b'<div class="beam" aria-hidden="true"></div>',
     b'<div class="beam" aria-hidden="true"></div>\n'
     b'    <img class="sigil" src="crow_mark.svg" alt="" aria-hidden="true">',
     b'<img class="sigil"',
     "sigil placed in the leuchte"),
    # E4: mobile — leuchte slightly larger, masthead scaled for narrow screens
    (b".leuchte{order:-1;width:min(260px,70vw)}",
     b".leuchte{order:-1;width:min(300px,76vw)}\n"
     b"  .masthead-crow img{width:112px}\n"
     b"  .masthead-crow .mc-word{font-size:1.05rem}",
     b"width:min(300px,76vw)",
     "mobile sizes"),
]

def tracked():
    out = subprocess.run(["git", "ls-files"], capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if l.strip()]

def edit(path, old, new, mark, note, apply, log):
    p = ROOT / path
    if not p.exists():
        log.append(("MISS", path, f"file absent — {note}")); return 0
    b = p.read_bytes()
    if mark and mark in b:
        log.append(("OK", path, f"already applied — {note}")); return 0
    for o, n in ((old, new), (old.replace(b"\n", b"\r\n"), new.replace(b"\n", b"\r\n"))):
        if o in b:
            if apply:
                p.write_bytes(b.replace(o, n, 1))
            log.append(("FIX" if apply else "WOULD", path, note)); return 1
    log.append(("MISS", path, f"target string not found — {note}")); return 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    log, files = [], tracked()

    # A — legibility (pages + their generator, whose f-string doubles the braces)
    dbl = lambda x: x.replace(b"{", b"{{").replace(b"}", b"}}")
    for f in ("docs/privacy.html", "docs/terms.html"):
        edit(f, FOOT_RULE, LEGIBILITY_ADD, LEGIBILITY_MARK,
             "legibility: body/h1/strong/a colors", a.apply, log)
    edit("patch_legal_pages.py", dbl(FOOT_RULE), dbl(LEGIBILITY_ADD), dbl(LEGIBILITY_MARK),
         "legibility: generator template", a.apply, log)

    # B — casing
    hits = 0
    for f in files:
        if f.startswith(NEVER_TOUCH_PREFIX) or Path(f).name in NEVER_TOUCH_NAMES:
            continue
        if Path(f).name in CASING_SKIP:
            p = ROOT / f
            if p.exists() and b"NebelK" in p.read_bytes():
                log.append(("SKIP", f, CASING_SKIP[Path(f).name]))
            continue
        p = ROOT / f
        try:
            b = p.read_bytes()
        except OSError:
            continue
        n = b.count(b"NebelK")
        if n:
            if a.apply:
                p.write_bytes(b.replace(b"NebelK", b"NebelK"))
            log.append(("FIX" if a.apply else "WOULD", f, f"casing x{n}")); hits += n

    # C — footer copyright on docs pages that have a footer and lack the mark
    for f in sorted(files):
        if not (f.startswith("docs/") and f.endswith(".html")):
            continue
        p = ROOT / f
        b = p.read_bytes()
        i = b.rfind(b"<footer")
        if i < 0:
            continue
        if COPY_MARK in b[i:]:
            continue
        for anchor in (b"</div></footer>", b"</footer>"):
            j = b.rfind(anchor)
            if j > i:
                if a.apply:
                    p.write_bytes(b[:j] + COPY_LINE + b[j:])
                log.append(("FIX" if a.apply else "WOULD", f, "footer \u00a9 2026 NebelKr\u00e4he"))
                break

    # D — hero
    for old, new, mark, note in HERO:
        edit("docs/index.html", old, new, mark, f"hero: {note}", a.apply, log)

    # awareness: where generator-side footer wiring lives (regen re-check point)
    gen = [f for f in files if f.endswith(".py") and
           b"privacy.html" in (ROOT / f).read_bytes()]
    for s, f, note in log:
        print(f"{s:5s} {f} — {note}")
    print(f"\ncasing occurrences handled: {hits}")
    if gen:
        print("note: generator files referencing privacy.html (footer wiring lives here; "
              "if a page regenerates without its \u00a9 line, re-run this patch): "
              + ", ".join(gen))
    if not a.apply:
        print("\nreport only — rerun with --apply to write")

if __name__ == "__main__":
    main()
