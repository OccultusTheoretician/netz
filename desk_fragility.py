#!/usr/bin/env python3
"""
desk_fragility.py — the desk auditing its own foundation.

The grader computes single_outlet_sides on every event and nothing reads it.
That field is the corroboration-depth disclosure: a Grade A event with four
hostile sides where three sides are one outlet each is confirmed across BIAS,
not across independent reporting — the desk's own faces say so line by line,
but no instrument totals it. This one does.

Reads the newest tg_events pull (or --file), writes FRAGILITY_<stamp>.md and
FRAGILITY_latest.md into forecasts/. Touches nothing else: no ledger, no
existing face, no served tile.

    python desk_fragility.py
    python desk_fragility.py --file forecasts\\tg_events_2026-07-30_0745.json
"""
import argparse
import glob
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from runguard import write_run_artifact   # KK21h

HERE = Path(__file__).resolve().parent


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def newest_events(explicit=None):
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    cands = []
    for base in (HERE / "forecasts", HERE, Path.cwd()):
        cands += glob.glob(str(base / "tg_events_*.json"))
    if not cands:
        return None
    return Path(sorted(set(cands))[-1])  # dated names sort chronologically


def is_graded(e):
    return str(e.get("grade", "")).startswith(("A", "B"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None, help="explicit tg_events_*.json")
    a = ap.parse_args()

    src = newest_events(a.file)
    if src is None:
        print("no tg_events_*.json found in forecasts/, script dir, or cwd "
              "and no --file given.", file=sys.stderr)
        return 1

    doc = read_json(src)
    events = doc.get("events", doc if isinstance(doc, list) else [])
    graded = [e for e in events if is_graded(e)]
    if not graded:
        print(f"{src.name}: no Grade A/B events — nothing to audit.")
        return 0

    kinetic = [e for e in graded if e.get("track") == "kinetic"]
    statements = [e for e in graded if e.get("track") == "statement"]

    def fully_single(e):
        sides = e.get("sides") or []
        sos = e.get("single_outlet_sides") or []
        return bool(sides) and len(sos) == len(sides)

    full = [e for e in graded if fully_single(e)]
    partial = [e for e in graded
               if (e.get("single_outlet_sides") and not fully_single(e))]
    deep = [e for e in graded if not e.get("single_outlet_sides")]

    prio = Counter()
    for e in graded:
        for s in e.get("single_outlet_sides") or []:
            prio[(e.get("zone", "?"), s)] += 1

    stamp = src.stem.replace("tg_events_", "")
    now = datetime.now(timezone.utc).strftime("%d%H%MZ %b %y").upper()

    out = []
    out.append("## FRAGILITY — CORROBORATION DEPTH OF THE GRADED RECORD\n")
    out.append("*A side resting on one outlet is corroboration across bias, "
               "not across independent reporting. The grader discloses this "
               "per event in `single_outlet_sides`; this face totals the "
               "disclosure. Grades are not being revised — the method counts "
               "sides, and the sides are real. What is measured here is how "
               "thin the ice under each side is.*\n")
    out.append(f"Source pull: `{src.name}` · rendered {now}\n")
    out.append(f"**{len(graded)} graded events** ({len(kinetic)} kinetic, "
               f"{len(statements)} statement) · "
               f"**{len(full)} rest entirely on single outlets** · "
               f"{len(partial)} partially · {len(deep)} with multi-outlet "
               f"depth on every side\n")

    out.append("**⬛ EXPANSION PRIORITY — single-outlet dependency by zone and side**\n")
    out.append("> Adding a channel here upgrades corroboration on graded "
               "events. Adding a channel anywhere else adds volume.\n")
    for (zone, side), n in prio.most_common():
        out.append(f"- **{zone} / {side}** — carries {n} graded event(s) on one outlet")
    out.append("")

    out.append("**◼ PER-EVENT DEPTH** (single-outlet sides marked \\*)\n")
    for e in sorted(graded, key=lambda x: (str(x.get("grade", "")),
                                           x.get("zone", ""),
                                           str(x.get("anchor", "")))):
        anchor = ", ".join(e.get("anchor") or ["?"])
        sos = set(e.get("single_outlet_sides") or [])
        sides = " ".join((s + "*") if s in sos else s
                         for s in (e.get("sides") or []))
        g = str(e.get("grade", "?"))[:1]
        out.append(f"- [{g}] **{anchor}** · {e.get('zone','?')} · "
                   f"{e.get('track','?')} · sides: {sides} · "
                   f"{e.get('n_reports','?')} rpt / "
                   f"{e.get('n_channels','?')} chan")
    out.append("")
    out.append("*Depth marker: a starred side would lose its vote if that one "
               "channel went quiet or went bad. Method note stands: sides are "
               "counted, not outlets — this face changes nothing about the "
               "grades and everything about how far to trust them.*\n")

    md = "\n".join(out)
    dest_dir = HERE / "forecasts"
    dest_dir.mkdir(exist_ok=True)
    dated = dest_dir / f"FRAGILITY_{stamp}.md"
    latest = dest_dir / "FRAGILITY_latest.md"
    dated = write_run_artifact(dated, md, tag="fragility")
    latest.write_text(md, encoding="utf-8")

    print(f"FRAGILITY · {len(graded)} graded · {len(full)} fully single-outlet "
          f"({100*len(full)//max(1,len(graded))}%)")
    print("FRAGILITY · expansion priority:")
    for (zone, side), n in prio.most_common(6):
        print(f"    {zone}/{side}  {n}")
    print(f"FRAGILITY · face -> {dated}")
    print(f"FRAGILITY · face -> {latest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
