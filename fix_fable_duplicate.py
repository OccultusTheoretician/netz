#!/usr/bin/env python3
"""
fix_fable_duplicate.py — remove the duplicated second fable-5 ingest batch.

WHAT HAPPENED
fable_projections_2026-07-30.json was ingested twice. The first run wrote
KKR-20260730-01..10 and then crashed in render_ledger (the domain KeyError),
printing "ledger unchanged" — which was false, the write had already happened.
The second run, after the patch, appended the same ten forecasts again as
KKR-20260730-11..20.

WHAT THIS DOES
Removes manual/fable-5 rows whose statement duplicates an earlier manual/fable-5
row from the same date, keeping the FIRST occurrence (the lower id). Refuses to
run if the duplicates are not an exact statement match, so it cannot delete a
genuinely distinct forecast. Touches no other arm and no other date.

Backup written to ledger.json.bak_dupfix before any change.
Run from C:\netz:  python fix_fable_duplicate.py
Then:              python kkr.py --score      (rebuilds the faces)
"""
import json, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
L = HERE / "ledger.json"
if not L.exists():
    L = Path.cwd() / "ledger.json"
    if not L.exists():
        sys.exit("ledger.json not found beside this script or in cwd.")

ARM = "manual/fable-5"
DATE_PREFIX = "KKR-20260730"

data = json.loads(L.read_text(encoding="utf-8"))
projs = data["projections"]

targets = [p for p in projs
           if p.get("model") == ARM and str(p.get("id", "")).startswith(DATE_PREFIX)]
print(f"{ARM} rows dated {DATE_PREFIX}: {len(targets)}")

if len(targets) <= 10:
    sys.exit("no duplicate batch present (10 or fewer rows) — nothing to do.")

seen = {}          # statement -> id of the first row carrying it
drops = []         # (id_to_drop, id_it_duplicates)
for p in sorted(targets, key=lambda x: x["id"]):
    key = p.get("statement", "").strip()
    if key in seen:
        drops.append((p["id"], seen[key]))
    else:
        seen[key] = p["id"]

drop_ids = [d for d, _ in drops]

if not drop_ids:
    sys.exit("more than 10 rows but no exact statement duplicates — "
             "these may be distinct forecasts. Refusing to delete. Inspect by hand.")

if len(drop_ids) != len(targets) - len(seen):
    sys.exit("duplicate accounting does not reconcile — refusing to delete.")

print(f"keeping {len(seen)} unique, dropping {len(drop_ids)} duplicates:")
for dup_id, orig_id in drops:
    print(f"  drop {dup_id}  (duplicate of {orig_id})")

# any dropped row already resolved? then stop - a scored row is evidence.
resolved = [p for p in targets if p["id"] in drop_ids and p.get("status") in ("hit", "miss")]
if resolved:
    sys.exit(f"REFUSING: {len(resolved)} duplicate row(s) already carry a resolution. "
             "A scored row is evidence; resolve this by hand.")

shutil.copy2(L, L.with_name("ledger.json.bak_dupfix"))
data["projections"] = [p for p in projs if p.get("id") not in set(drop_ids)]
L.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

from collections import Counter
print()
print("backup: ledger.json.bak_dupfix")
print("per-arm counts now --")
print(Counter(p.get("model", "(none)") for p in data["projections"]))
print()
print("next:  python kkr.py --score")
