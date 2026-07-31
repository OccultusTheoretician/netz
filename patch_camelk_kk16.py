#!/usr/bin/env python3
"""patch_camelk_kk16.py — RULING 2026-07-31: the mark is NebelKrähe, camelCase K.
Reverses the lowercase-k sweep. Report-only by default; --apply writes.

Sweeps every tracked file `Nebelk` -> `NebelK` (all encodings — the k precedes
the umlaut, so literal, &auml; and &#228; forms all flip on the one needle).
All-caps NEBELKRÄHE and lowercase-ascii filenames (nebelkraehe*) are untouched
by construction.

HELD, printed with counts, never auto-flipped — the printed-record rule:
  - forecasts/KKR_2026-*.html          dated packets
  - reports/battle_report_*.html       dated battle reports
  - SITE_AUDIT_2026-07-30.md           dated audit record
  (the living faces — KKR_latest, forecasts/ledger, reports/latest — DO flip,
   and both mirror pairs receive identical bytes so desk verify holds)

RETIRED, skipped with a warning: the four legacy casing/marks patchers whose
needles encode the superseded ruling. Do not rerun them.

This session's two kk16 patch scripts ARE swept: patch_site_polish's casing
section becomes a no-op (both halves of its pair read NebelK), and
patch_footer_uniform's emission literals and markers flip to the ruled form.
"""
import argparse, fnmatch, subprocess
from pathlib import Path

ROOT = Path(".").resolve()
SELF = "patch_camelk_kk16.py"

HELD = [("forecasts/KKR_2026-*.html", "dated packet — printed record"),
        ("reports/battle_report_*.html", "dated battle report — printed record"),
        ("SITE_AUDIT_2026-07-30.md", "dated audit record — printed record")]
RETIRED = {"patch_generators_seo.py", "patch_marks_tm.py",
           "patch_site_audit_fix.py", "patch_site_marks_fix.py"}
NEVER = {"ledger.json", "docs/ledger.json", "docs/kalls_hashlog.json", "docs/plate.json"}

def held_reason(f):
    for pat, why in HELD:
        if fnmatch.fnmatch(f, pat):
            return why
    return None

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    files = [l for l in subprocess.run(["git", "ls-files"], capture_output=True,
             text=True).stdout.splitlines() if l.strip()]
    flipped = held_n = 0
    for f in sorted(files) + [SELF and None][1:]:
        if f is None or Path(f).name == SELF or f in NEVER:
            continue
        p = ROOT / f
        try:
            b = p.read_bytes()
        except OSError:
            continue
        n = b.count(b"Nebelk")
        if not n:
            continue
        why = held_reason(f)
        if why:
            print(f"HELD  {f} — x{n} — {why}"); held_n += n; continue
        if Path(f).name in RETIRED:
            print(f"RETIRE {f} — x{n} — needles encode the superseded ruling; do not rerun"); continue
        if a.apply:
            p.write_bytes(b.replace(b"Nebelk", b"NebelK"))
        print(f"{'FIX  ' if a.apply else 'WOULD'} {f} — x{n}")
        flipped += n
    # the untracked copy of this session's uniform patch, if present, flips too
    for extra in ("patch_footer_uniform_kk16.py",):
        if extra not in files and (ROOT / extra).exists():
            b = (ROOT / extra).read_bytes(); n = b.count(b"Nebelk")
            if n:
                if a.apply: (ROOT / extra).write_bytes(b.replace(b"Nebelk", b"NebelK"))
                print(f"{'FIX  ' if a.apply else 'WOULD'} {extra} — x{n} (untracked tool)"); flipped += n
    print(f"\nflipped: {flipped} · held in printed records: {held_n}")
    if not a.apply:
        print("report only — rerun with --apply to write")

if __name__ == "__main__":
    main()
