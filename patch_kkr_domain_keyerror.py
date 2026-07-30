#!/usr/bin/env python3
"""
patch_kkr_domain_keyerror.py — stop ingest crashing when a row lacks 'domain'.

render_ledger builds the OPEN PROJECTIONS table with p['domain'] (hard key).
Rows written before the domain field existed, and any row whose source JSON
omitted it, KeyError and abort the whole ingest AFTER the ledger was already
written — so the arm lands but the run dies and every later arm is skipped.
Fix: read domain defensively, exactly like 'model' two lines up already does.

Idempotent; writes kkr.py.bak once. Run from C:\netz:  python patch_kkr_domain_keyerror.py
"""
import shutil, sys
from pathlib import Path

P = Path(__file__).resolve().parent / "kkr.py"
if not P.exists():
    P = Path.cwd() / "kkr.py"
    if not P.exists():
        sys.exit("kkr.py not found beside this script or in cwd.")

src = P.read_text(encoding="utf-8")

bad = "f\"{p['probability']}% | {p['domain']} | {p['statement']} |\")"
good = "f\"{p['probability']}% | {p.get('domain','\\u2014')} | {p['statement']} |\")"

if bad not in src:
    if "p.get('domain'" in src:
        sys.exit("already patched (domain read defensively) — nothing to do.")
    sys.exit("target line not found — kkr.py changed shape; fix render_ledger by hand.")

shutil.copy2(P, P.with_suffix(".py.bak"))
P.write_text(src.replace(bad, good), encoding="utf-8")
print("patched kkr.py (backup at kkr.py.bak)")
print("render_ledger now reads domain defensively; ingest will not crash on a")
print("row that lacks it.")
