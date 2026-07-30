#!/usr/bin/env python3
"""
kfk_promote.py — promote spine facts into graded board claims.

The spine (docs/kfk_spine.json) holds 251 state actors whose fields each
carry {value, as_of, source, grade}. The board (KriegForeKaster.json) holds
the formations whose claim classes decay on half-life clocks. This tool
translates spine fields into board claims WITH PROVENANCE CARRIED OVER —
source, date, and the original reliability code all ride into the claim.
It never invents, never overwrites: only EMPTY claim fields fill, populated
ones are skipped and counted.

    python kfk_promote.py                          dry run, full census
    python kfk_promote.py --apply --classes commander,composition

Class map (spine field → board claim class):
    chief_of_defence  → commander     (half-life 60d)
    service_branches  → composition   (180d; personnel folded into note)
    posture_note      → posture       (21d)
    hq_coordinates    → location      (14d)

THE STALE-ON-ARRIVAL FACT, printed rather than hidden: the spine's facts are
compendium-dated (mostly 2025). Against the half-lives above, most promoted
claims are past half-life the moment they land. That is the instrument
working — a Factbook-sourced board IS that stale, the freshness face should
say so, and the stale queue is the re-confirmation work queue. The dry run
prints the exact consequence per class; the operator chooses which classes
go on the public face.

Grade map, printed in every promoted note: spine reliability codes A* map to
the board's DOCUMENTED (official public-domain compendium), everything else
to REPORTED; the original code is preserved verbatim in the note.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPINE = HERE / "docs" / "kfk_spine.json"
BOARD_ROOT = HERE / "KriegForeKaster.json"
BOARD_DOCS = HERE / "docs" / "KriegForeKaster.json"

CLASS_MAP = {
    "commander":   ("chief_of_defence", 60),
    "composition": ("service_branches", 180),
    "posture":     ("posture_note", 21),
    "location":    ("hq_coordinates", 14),
}


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def grade_map(g):
    g = str(g or "").strip()
    return ("DOCUMENTED" if g[:1].upper() == "A" else "REPORTED"), g


def age_days(as_of, now):
    s = str(as_of or "").strip()
    m = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", s)
    if not m:
        return None
    y, mo, d = int(m.group(1)), int(m.group(2) or 7), int(m.group(3) or 1)
    try:
        return (now - datetime(y, mo, d, tzinfo=timezone.utc)).days
    except ValueError:
        return None


def build_claim(field, cls, now):
    board_grade, orig = grade_map(field.get("grade"))
    claim = {
        "grade": board_grade,
        "as_of": str(field.get("as_of", "")),
        "sources": [field.get("source", "")],
        "note": (f"Promoted from the spine (kfk_promote); original "
                 f"reliability {orig or 'unstated'}. Value: "
                 f"{str(field.get('value', ''))[:400]}"),
        "promoted": now.strftime("%Y-%m-%d"),
    }
    if cls == "location":
        m = re.findall(r"-?\d+\.\d+", str(field.get("value", "")))
        if len(m) >= 2:
            claim["lat"], claim["lon"] = float(m[0]), float(m[1])
    return claim


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--classes", default="commander,composition",
                    help="comma list from: " + ",".join(CLASS_MAP))
    a = ap.parse_args()
    classes = [c.strip() for c in a.classes.split(",") if c.strip()]
    bad = [c for c in classes if c not in CLASS_MAP]
    if bad:
        print(f"unknown class(es): {bad}", file=sys.stderr)
        return 1

    now = datetime.now(timezone.utc)
    spine = json.loads(SPINE.read_text(encoding="utf-8"))
    board = json.loads(BOARD_ROOT.read_text(encoding="utf-8"))

    # join: spine state actors ↔ board 'armed forces' formations, by
    # faction-slug == name-slug, then by name containment. Unmatched print.
    actors = {slug(x["name"]): x for x in spine["actors"]
              if x.get("actor_type") == "state"}
    rows = [f for f in board["formations"]
            if f.get("echelon") == "armed forces"]
    matched, unmatched = {}, []
    for f in rows:
        key = slug(f.get("faction", ""))
        act = actors.get(key)
        if not act:
            ns = slug(f.get("name", ""))
            act = next((v for k, v in actors.items()
                        if k and (k in ns or ns in k)), None)
        if act:
            matched[f["id"]] = (f, act)
        else:
            unmatched.append(f.get("name"))

    print(f"KFK PROMOTE — {len(rows)} armed-forces rows · "
          f"{len(matched)} matched to spine states · "
          f"{len(unmatched)} unmatched (printed, never guessed)")
    for n in unmatched[:8]:
        print(f"    unmatched: {n}")
    if len(unmatched) > 8:
        print(f"    … and {len(unmatched) - 8} more")

    total_written = 0
    for cls in classes:
        spine_field, half = CLASS_MAP[cls]
        fillable = skipped = nosrc = stale = 0
        for f, act in matched.values():
            fld = (act.get("fields") or {}).get(spine_field)
            if not fld or not str(fld.get("value", "")).strip():
                continue
            if f.get(cls):
                skipped += 1
                continue
            if not fld.get("source"):
                nosrc += 1
                continue
            fillable += 1
            ad = age_days(fld.get("as_of"), now)
            if ad is not None and ad > half:
                stale += 1
            if a.apply:
                f[cls] = build_claim(fld, cls, now)
                total_written += 1
        print(f"  [{cls:<12}] fillable {fillable:>3} · already-populated "
              f"skipped {skipped:>3} · unsourced refused {nosrc:>2} · "
              f"STALE ON ARRIVAL {stale:>3} of {fillable} "
              f"(half-life {half}d — the freshness face will say so)")

    if not a.apply:
        print("\nDRY RUN — nothing written. Choose classes and rerun with "
              "--apply. The stale counts above are the public consequence.")
        return 0

    board["as_of"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    board["disclosure"] = (str(board.get("disclosure", "")) +
        f" PROMOTION {now.strftime('%Y-%m-%d')}: {total_written} claims "
        f"promoted from the compendium spine with provenance carried over; "
        f"claims arriving past half-life are counted stale on the freshness "
        f"face rather than hidden — the stale queue is the re-confirmation "
        f"work queue.")
    txt = json.dumps(board, ensure_ascii=False, indent=2)
    BOARD_ROOT.write_text(txt, encoding="utf-8")
    BOARD_DOCS.write_text(txt, encoding="utf-8")
    print(f"\nAPPLIED — {total_written} claims written to board (root + "
          f"docs). Rerun your KriegForeKaster refresh so freshness.json and "
          f"the page recount, then commit all three.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
