#!/usr/bin/env python3
"""
patch_ingest_seal.py - two fixes, one run. From C:\\netz. Default REPORTS;
--apply writes. Never stages, never commits.

A. PARSER PASSTHROUGH (permanent). parse_projections rebuilds each entry from
   a six-field whitelist, silently stripping failure_condition, keyed_keyless
   and keyed_keyless_rationale. Result: no manual batch can EVER enter sealed,
   whatever the JSON carries - today's 29 UNSEALED lines are this one defect.
   The edit passes the three fields through when present; absent fields change
   nothing, so Qwen's six-field output is unaffected.

B. 4.02f REPAIR for today's manual/fable-5 rows. Their failure conditions and
   keyed/keyless determinations already exist in C:\\netz\\fable_projections.json
   - authored before issuance, stripped at ingest. The repair reads that file,
   matches ledger rows by exact statement text (both sides pass through the
   same .strip()), merges the trio into open unsealed fable-5 rows only, and
   saves through kkr.save_ledger - the 4.02g choke point seals them. Never
   overwrites a non-empty field. sonnet-5 / opus-5 rows are untouched: their
   batch files carry no seal fields, and drafting failure conditions without
   reading their statements would be invention, not repair.

  python patch_ingest_seal.py            # report
  python patch_ingest_seal.py --apply    # write parser fix + seal fable-5
"""
import argparse
import json
import sys
from pathlib import Path

OLD_PARSE = (
    '            out.append({"statement": str(p["statement"]).strip(),\n'
    '                        "domain": str(p.get("domain", "general")).strip().lower(),\n'
    '                        "probability": prob,\n'
    '                        "resolution": str(p["resolution"]).strip(),\n'
    '                        "deadline": p["deadline"],\n'
    '                        "citations": [int(c) for c in p.get("citations", [])]})\n'
)
NEW_PARSE = (
    '            entry = {"statement": str(p["statement"]).strip(),\n'
    '                     "domain": str(p.get("domain", "general")).strip().lower(),\n'
    '                     "probability": prob,\n'
    '                     "resolution": str(p["resolution"]).strip(),\n'
    '                     "deadline": p["deadline"],\n'
    '                     "citations": [int(c) for c in p.get("citations", [])]}\n'
    '            # RPAS 4.02g passthrough: a batch arriving with its seal\n'
    '            # fields enters sealed; absent fields change nothing.\n'
    '            for k in ("failure_condition", "keyed_keyless",\n'
    '                      "keyed_keyless_rationale"):\n'
    '                if str(p.get(k, "")).strip():\n'
    '                    entry[k] = str(p[k]).strip()\n'
    '            out.append(entry)\n'
)

BATCH = "fable_projections.json"
ARM = "manual/fable-5"
DAY = "KKR-20260731"


def parser_fix(apply: bool) -> str:
    p = Path("kkr.py")
    t = p.read_text(encoding="utf-8")
    if NEW_PARSE in t:
        return "ALREADY DONE  kkr.py: parser passthrough"
    n = t.count(OLD_PARSE)
    if n == 0:
        return "MISSING STR   kkr.py: parser whitelist not found - inspect manually"
    if n > 1:
        return f"NOT UNIQUE    kkr.py ({n}x) - skipped"
    if apply:
        p.write_text(t.replace(OLD_PARSE, NEW_PARSE, 1), encoding="utf-8")
    return f"{'EDITED' if apply else 'WILL EDIT':13s} kkr.py: parser passthrough (3 seal fields)"


def repair(apply: bool):
    src = Path(BATCH)
    if not src.exists():
        print(f"MISSING FILE  {BATCH} - repair skipped"); return
    batch = json.loads(src.read_text(encoding="utf-8"))
    trio = {}
    for b in batch:
        st = str(b.get("statement", "")).strip()
        if st and str(b.get("failure_condition", "")).strip():
            trio[st] = {k: str(b[k]).strip() for k in
                        ("failure_condition", "keyed_keyless",
                         "keyed_keyless_rationale") if str(b.get(k, "")).strip()}
    print(f"batch file: {len(batch)} entries, {len(trio)} carry seal fields")
    sys.path.insert(0, ".")
    import kkr
    data = kkr.load_ledger()
    merged, unmatched = 0, []
    for e in data["projections"]:
        if (e.get("model") == ARM and str(e.get("id", "")).startswith(DAY)
                and e.get("status") == "open"
                and not str(e.get("failure_condition", "")).strip()):
            hit = trio.get(str(e.get("statement", "")).strip())
            if hit:
                if apply:
                    e.update(hit)
                merged += 1
            else:
                unmatched.append(e["id"])
    print(f"{'MERGED' if apply else 'WILL MERGE':13s} {merged} {ARM} row(s)")
    if unmatched:
        print(f"NO MATCH      {unmatched} - statement text differs; not touched")
    if apply and merged:
        kkr.save_ledger(data)  # choke point seals here
        fresh = kkr.load_ledger()
        sealed = sum(1 for e in fresh["projections"]
                     if e.get("model") == ARM and str(e.get("id", "")).startswith(DAY)
                     and e.get("seal_sha256"))
        print(f"sealed: {sealed} {ARM} rows now carry seal_sha256")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    print(("APPLYING" if a.apply else "PROPOSED (nothing written)") + "\n" + "-" * 56)
    print(parser_fix(a.apply))
    print()
    repair(a.apply)
    if not a.apply:
        print("\nApply with: python patch_ingest_seal.py --apply")
    else:
        print("\nsonnet-5 / opus-5 rows remain unsealed by design - upload their")
        print("two JSONs and the failure conditions get drafted from their")
        print("actual statements, same pattern as the 07-30 repair.")
