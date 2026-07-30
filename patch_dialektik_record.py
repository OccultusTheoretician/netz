#!/usr/bin/env python3
"""
patch_dialektik_record.py — the missing command that closes the calibration loop.

THE GAP
dialektik.py's calibrate/check read a `scored` map keyed by dyad name, but no
command WRITES to it. `score --dyad` scores a standalone file, prints an index,
and (correctly) refuses if the instrument is uncalibrated — so you can never
score the calibration cases themselves, because scoring them is what lifts the
gate. The workflow was incomplete; that is why the instrument sat unrun.

THE FIX
Adds `dialektik.py record --dyad <file> --case "<exact dyad name>"`. It scores
the filled file WITHOUT the gate (calibration scoring is pre-gate by
definition), verifies the case name exists in the calibration set, and writes
the resulting index into dialektik_calibration.json under `scored`. After the
five cases are recorded, `check` opens or publishes a null on the honest
numbers.

Refuses to record a case name not in the set, and refuses if the file yields no
countable index (an all-unscored file cannot silently register as 0.00).

Idempotent. Backup written to dialektik.py.bak once.
Run from C:\netz:  python patch_dialektik_record.py
"""
import shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
P = HERE / "dialektik.py"
if not P.exists():
    P = Path.cwd() / "dialektik.py"
    if not P.exists():
        sys.exit("dialektik.py not found beside this script or in cwd.")

src = P.read_text(encoding="utf-8")
if "def record(" in src or 'sub.add_parser("record")' in src:
    sys.exit("already patched (record present) — nothing to do.")

# --- 1. insert the record() function just before def main() -----------------
anchor = "def main():\n"
if anchor not in src:
    sys.exit("anchor (def main) not found — dialektik.py changed shape; patch by hand.")

record_fn = '''def record(path, case):
    """Score a calibration case and write its index into the calibration file.

    Pre-gate by design: scoring the calibration set is the act that lets the
    gate pass, so this MUST NOT call check(). It verifies the case name is real
    and that the file yields a countable index before writing.
    """
    if not CAL.exists():
        # create the seeded file so the case names exist to match against
        calibrate()
    c = read_json(CAL)
    known = {x["dyad"] for band in ("expect_low", "expect_high", "contested_control")
             for x in c["cases"][band]}
    if case not in known:
        print(f"  no calibration case named exactly:\\n    {case}")
        print("  known cases:")
        for k in sorted(known):
            print(f"    {k}")
        return 1
    d = read_json(path)
    idx, n, counted, skipped = score_dyad(d, verbose=True)
    if idx is None:
        print("\\n  REFUSING to record: the file yields no countable index. An "
              "all-unscored\\n  file must not register as 0.00. Fill scores, grades "
              "and sources first.")
        return 1
    c.setdefault("scored", {})[case] = round(idx, 4)
    CAL.write_text(json.dumps(c, indent=2, ensure_ascii=False) + "\\n", encoding="utf-8")
    print(f"\\n  recorded {case} -> index {idx:.2f} ({n} indicator(s) counted)")
    print("  run: python dialektik.py check")
    return 0


'''
src = src.replace(anchor, record_fn + anchor)

# --- 2. register the subparser ----------------------------------------------
sub_anchor = '    f = sub.add_parser("forecast"); f.add_argument("--dyad", required=True)\n'
if sub_anchor not in src:
    sys.exit("subparser anchor not found.")
src = src.replace(
    sub_anchor,
    sub_anchor +
    '    r = sub.add_parser("record")\n'
    '    r.add_argument("--dyad", required=True)\n'
    '    r.add_argument("--case", required=True,\n'
    '                   help="exact calibration dyad name to record this index under")\n'
)

# --- 3. dispatch ------------------------------------------------------------
disp_anchor = '    if a.cmd == "forecast":\n        return forecast(a.dyad)\n'
if disp_anchor not in src:
    sys.exit("dispatch anchor not found.")
src = src.replace(
    disp_anchor,
    disp_anchor +
    '    if a.cmd == "record":\n'
    '        return record(a.dyad, a.case)\n'
)

shutil.copy2(P, P.with_suffix(".py.bak"))
P.write_text(src, encoding="utf-8")
print("patched dialektik.py (backup at dialektik.py.bak)")
print("added: record --dyad <file> --case \"<exact dyad name>\"")
print()
print("workflow now:")
print("  1. fill each dyad in the workpaper")
print("  2. python dialektik.py record --dyad <case>.json --case \"<name>\"")
print("  3. repeat for all five")
print("  4. python dialektik.py check   (opens the gate or prints the null)")
