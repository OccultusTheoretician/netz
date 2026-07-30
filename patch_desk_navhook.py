#!/usr/bin/env python3
"""
patch_desk_navhook.py — re-stamp nav on every ship, before verify.

WHY THE HOOK EXISTS
kkr.py regenerates kkr.html and ledger.html from its own templates on every
ingest and score — templates that carry no nav. Without a post-render step,
those two pages lose their nav every render and the drift returns forever.
The ship gate is the single choke point every publication passes through, so
nav gets normalized there: cmd_ship runs navgen FIRST, then verify sees the
post-nav state (mirrors already twinned by navgen), then stages.

FAILURE POSTURE: navgen problems WARN and the ship continues. Navigation is
cosmetic; a ship gate that blocks publication over a nav bar would get
disabled within a week, and a disabled gate protects nothing. The warning
prints so a persistent failure is visible, not silent.

Idempotent; backup written to desk.py.bak_navhook once.
Run from C:\netz:  python patch_desk_navhook.py
"""
import shutil, sys
from pathlib import Path

P = Path(__file__).resolve().parent / "desk.py"
if not P.exists():
    P = Path.cwd() / "desk.py"
    if not P.exists():
        sys.exit("desk.py not found beside this script or in cwd.")

src = P.read_text(encoding="utf-8")
if "navgen" in src:
    sys.exit("already patched (navgen referenced in desk.py) — nothing to do.")

anchor = ('    globals()["PREFLIGHT"] = True\n'
          "    failed = run_verify()\n")
if anchor not in src:
    sys.exit("cmd_ship anchor not found — desk.py changed shape; patch by hand.")

hook = (
    "    # nav normalization before verify: generators rewrite pages without\n"
    "    # nav; stamping here means verify checks the post-nav mirrors. WARN,\n"
    "    # never block - a gate that fails on cosmetics gets disabled.\n"
    "    _ng = ROOT / \"navgen.py\"\n"
    "    if _ng.exists():\n"
    "        _r = subprocess.run([sys.executable, str(_ng)], cwd=str(ROOT),\n"
    "                            capture_output=True, text=True, timeout=60)\n"
    "        if _r.returncode != 0:\n"
    "            print(warn(\"  [WARN] navgen failed - shipping without nav \"\n"
    "                       \"normalization\"))\n"
    "            print(dim((_r.stdout + _r.stderr).strip()[-300:]))\n"
    "        else:\n"
    "            _stamped = [l for l in _r.stdout.splitlines()\n"
    "                        if l.strip().startswith((\"replaced\", \"inserted\"))]\n"
    "            if _stamped:\n"
    "                print(dim(f\"  nav: {len(_stamped)} page(s) re-stamped\"))\n"
)

src = src.replace(anchor, hook + anchor)

shutil.copy2(P, P.with_name("desk.py.bak_navhook"))
P.write_text(src, encoding="utf-8")
print("patched desk.py (backup at desk.py.bak_navhook)")
print("cmd_ship now runs navgen before verify; WARN-only on failure.")
