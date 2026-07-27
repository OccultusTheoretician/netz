#!/usr/bin/env python3
"""
KriegForeKaster.py — a scored order of battle.

The map is not the product. Anyone can draw a map. The product is that every
claim on it carries a grade, a source, and a date, that claims EXPIRE on a
published schedule, and that the interesting ones are issued into the predictive
ledger as dated forecasts and later resolved hit or miss in public.

Janes sells confidence. ACLED sells events. Neither publishes a miss record on
its own dispositions. That is the only unoccupied ground here, and it is the one
piece the desk already owns the machinery for.

THE UNIT OF RECORD IS THE CLAIM, NOT THE FORMATION.
A formation is not one assertion. It is four independent ones, each with its own
grade, source set, and date, because they decay at wildly different rates:

    existence    — that the formation exists at all      half-life 365d
    composition  — what it is made of                    half-life 180d
    posture      — committed / reserve / reconstituting  half-life  21d
    location     — where it is                           half-life  14d
    commander    — who has it                            half-life  60d

Commander is the field every amateur ORBAT gets wrong, because it is the most
satisfying to publish and the fastest to rot. Here it expires on its own clock
and goes visibly grey when it does.

GRADES (the desk's existing ladder, highest first):
    CONFESSED         the party itself said so, on the record
    PROOF-VERBATIM    primary document reproduced
    DOCUMENTED        named institutional source, checkable
    REPORTED          press or OSINT attribution, single-sourced
    DERIVED           inferred from other claims here — rationale required
    SPECULATIVE       held open, not asserted — rationale required, never issued

Usage
    python KriegForeKaster.py validate                  structural + provenance audit
    python KriegForeKaster.py lint                      decay report: what has expired
    python KriegForeKaster.py stats                     coverage by faction, grade, decay
    python KriegForeKaster.py issue F-0007 location --p 60 --deadline 2026-08-20 \\
           --resolution "..."                 emit a KKR projection stub
    python KriegForeKaster.py link F-0007 KKR-20260801-03

The issue path writes KriegForeKaster_projections.json, which goes into the ledger through
the existing gate and the existing arm attribution:

    python kkr.py --ingest KriegForeKaster_projections.json --arm kfk/operator

It is deliberately not coupled to kkr.py. The gate that rejects a thin statement
should be the same gate, not a second one that drifts.
"""

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone, date
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "KriegForeKaster.json"
DOCS = HERE / "docs"
PROJ_OUT = HERE / "KriegForeKaster_projections.json"

GRADES = ["CONFESSED", "PROOF-VERBATIM", "DOCUMENTED", "REPORTED",
          "DERIVED", "SPECULATIVE"]
NEEDS_RATIONALE = {"DERIVED", "SPECULATIVE"}
NEVER_ISSUE = {"SPECULATIVE"}

ECHELONS = ["theater", "front", "army group", "army", "corps", "division",
            "brigade", "regiment", "battalion", "company", "detachment"]

# days after which a claim is stale enough that displaying it as current is a lie
HALF_LIFE = {"existence": 365, "composition": 180, "commander": 60,
             "posture": 21, "location": 14}

CLAIM_BLOCKS = list(HALF_LIFE.keys())
POSTURES = ["committed", "reserve", "reconstituting", "transiting",
            "withdrawn", "unknown"]


# ----------------------------------------------------------------------
def load() -> dict:
    if not DATA_FILE.exists():
        print(f"FAIL — {DATA_FILE} not found", file=sys.stderr)
        sys.exit(1)
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save(d: dict):
    d["as_of"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    DATA_FILE.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    publish()


def publish():
    """Copy the canonical file, byte for byte, to the directory Pages serves.

    Two rules, both learned expensively. First: the served copy is a build
    product, never a manual copy anyone has to remember. Second: it is a COPY,
    not a re-serialization. Re-dumping produces a file with identical content and
    a different hash, which means the published artifact can never be checked
    against the canonical one by hash — and 'recompute the hashes' is the whole
    claim. A derived artifact that re-encodes is where damage enters unseen; the
    Kalls export proved that at cost.
    """
    if not DOCS.exists():
        return False
    shutil.copyfile(DATA_FILE, DOCS / "KriegForeKaster.json")
    print(f"published -> {DOCS / 'KriegForeKaster.json'} (byte copy)")
    return True


def parse_day(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def age_days(s):
    d = parse_day(s)
    return None if d is None else (date.today() - d).days


def decay_state(block_name, block):
    """fresh | decayed | expired-hard, plus age. Nothing here is a judgement of
    truth — only of how long ago anyone last checked."""
    if not block:
        return None, None
    a = age_days(block.get("as_of"))
    if a is None:
        return "undated", None
    hl = HALF_LIFE[block_name]
    if a <= hl:
        return "fresh", a
    if a <= hl * 3:
        return "decayed", a
    return "stale", a


# ----------------------------------------------------------------------
def validate(d: dict) -> list:
    errs = []
    for k in ("schema", "theater", "factions", "formations"):
        if k not in d:
            errs.append(f"top level: missing '{k}'")
    if errs:
        return errs

    fac_ids = {f["id"] for f in d["factions"]}
    seen = set()
    ids = {f["id"] for f in d["formations"]}

    for f in d["formations"]:
        fid = f.get("id", "?")
        p = f"{fid}"
        if fid in seen:
            errs.append(f"{p}: duplicate id")
        seen.add(fid)

        if f.get("faction") not in fac_ids:
            errs.append(f"{p}: faction '{f.get('faction')}' is not declared")
        if f.get("echelon") not in ECHELONS:
            errs.append(f"{p}: echelon '{f.get('echelon')}' not in the ladder")
        if not f.get("name"):
            errs.append(f"{p}: no name")

        par = f.get("parent")
        if par:
            if par not in ids:
                errs.append(f"{p}: parent '{par}' does not exist")
            else:
                pf = next(x for x in d["formations"] if x["id"] == par)
                if (pf.get("echelon") in ECHELONS and f.get("echelon") in ECHELONS
                        and ECHELONS.index(pf["echelon"]) >= ECHELONS.index(f["echelon"])):
                    errs.append(f"{p}: parent '{par}' is not a higher echelon")

        if not f.get("existence"):
            errs.append(f"{p}: no existence claim — a formation with no evidence "
                        f"that it exists is not a record, it is a guess")

        for b in CLAIM_BLOCKS:
            blk = f.get(b)
            if not blk:
                continue
            q = f"{p}.{b}"
            g = blk.get("grade")
            if g not in GRADES:
                errs.append(f"{q}: grade '{g}' is not on the ladder")
            if not blk.get("as_of"):
                errs.append(f"{q}: no as_of — an undated claim cannot expire, "
                            f"which means it can never be wrong")
            elif parse_day(blk["as_of"]) is None:
                errs.append(f"{q}: as_of '{blk['as_of']}' unparseable")
            elif parse_day(blk["as_of"]) > date.today():
                errs.append(f"{q}: as_of is in the future")
            srcs = blk.get("sources") or []
            if not srcs and g not in NEEDS_RATIONALE:
                errs.append(f"{q}: grade {g} with no source. Only DERIVED and "
                            f"SPECULATIVE may stand without one, and both need "
                            f"a rationale.")
            if g in NEEDS_RATIONALE and not blk.get("rationale"):
                errs.append(f"{q}: grade {g} requires a rationale")

        loc = f.get("location")
        if loc:
            try:
                lat, lon = float(loc["lat"]), float(loc["lon"])
                if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                    errs.append(f"{p}.location: coordinates out of range")
            except (KeyError, TypeError, ValueError):
                errs.append(f"{p}.location: lat/lon missing or non-numeric")

        po = f.get("posture")
        if po and po.get("value") not in POSTURES:
            errs.append(f"{p}.posture: '{po.get('value')}' not in {POSTURES}")

    return errs


# ----------------------------------------------------------------------
def lint(d: dict) -> list:
    rows = []
    for f in d["formations"]:
        for b in CLAIM_BLOCKS:
            state, a = decay_state(b, f.get(b))
            if state in ("decayed", "stale", "undated"):
                rows.append((f["id"], f["name"], b, state, a, HALF_LIFE[b]))
    return rows


def stats(d: dict):
    from collections import Counter
    fx = Counter(f["faction"] for f in d["formations"])
    gx = Counter()
    dx = Counter()
    unloc = 0
    for f in d["formations"]:
        for b in CLAIM_BLOCKS:
            if f.get(b):
                gx[f[b].get("grade")] += 1
                dx[decay_state(b, f[b])[0]] += 1
        if not f.get("location"):
            unloc += 1
    return fx, gx, dx, unloc, len(d["formations"])


# ----------------------------------------------------------------------
def issue(d, fid, claim, prob, deadline, resolution, statement=None):
    f = next((x for x in d["formations"] if x["id"] == fid), None)
    if f is None:
        print(f"FAIL — no formation {fid}", file=sys.stderr)
        return 1
    if f.get("faction") == "EXAMPLE":
        print("FAIL — EXAMPLE records are placeholders and may not be issued "
              "into the ledger.", file=sys.stderr)
        return 1
    blk = f.get(claim)
    if blk and blk.get("grade") in NEVER_ISSUE:
        print(f"FAIL — {fid}.{claim} is graded {blk['grade']}. Held open is not "
              f"a forecast. Raise the grade or state a different claim.",
              file=sys.stderr)
        return 1

    if not statement:
        print("FAIL — --statement is required. The statement must carry the "
              "claim itself; the ledger gate rejects anything a stranger "
              "cannot read on its own.", file=sys.stderr)
        return 1

    proj = [{"statement": statement,
             "domain": "military/conflict",
             "probability": int(prob),
             "resolution": resolution,
             "deadline": deadline,
             "citations": [0]}]
    PROJ_OUT.write_text(json.dumps(proj, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"written → {PROJ_OUT}")
    print(f"\nThe ledger gate has not run yet. Next:\n"
          f"  python kkr.py --ingest {PROJ_OUT.name} --arm kfk/operator\n"
          f"then link the id back:\n"
          f"  python KriegForeKaster.py link {fid} <KKR-id>")
    return 0


def link(d, fid, kkr_id):
    f = next((x for x in d["formations"] if x["id"] == fid), None)
    if f is None:
        print(f"FAIL — no formation {fid}", file=sys.stderr)
        return 1
    f.setdefault("projections", [])
    if kkr_id not in f["projections"]:
        f["projections"].append(kkr_id)
    save(d)
    print(f"{fid} ← {kkr_id}")
    return 0


# ----------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="KriegForeKaster — a scored order of battle")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("validate")
    sub.add_parser("lint")
    sub.add_parser("stats")
    sub.add_parser("publish")
    i = sub.add_parser("issue")
    i.add_argument("formation")
    i.add_argument("claim", choices=CLAIM_BLOCKS)
    i.add_argument("--p", type=int, required=True)
    i.add_argument("--deadline", required=True)
    i.add_argument("--resolution", required=True)
    i.add_argument("--statement", required=True)
    l = sub.add_parser("link")
    l.add_argument("formation")
    l.add_argument("kkr_id")
    a = ap.parse_args()

    d = load()

    if a.cmd == "validate":
        errs = validate(d)
        if errs:
            print(f"INVALID — {len(errs)} finding(s):")
            for e in errs:
                print(f"  · {e}")
            return 1
        print(f"VALID — {len(d['formations'])} formations, "
              f"{len(d['factions'])} factions, theater '{d['theater']}'")
        return 0

    if a.cmd == "lint":
        rows = lint(d)
        if not rows:
            print("No expired claims.")
            return 0
        print(f"{len(rows)} claim(s) past their published half-life:\n")
        for fid, name, b, state, age, hl in sorted(rows, key=lambda r: -(r[4] or 0)):
            agestr = "undated" if age is None else f"{age}d old, half-life {hl}d"
            print(f"  [{state.upper():8s}] {fid} {name} · {b} · {agestr}")
        print("\nDecayed is not wrong. It means nobody has checked recently, and "
              "the viewer greys it accordingly.")
        return 0

    if a.cmd == "stats":
        fx, gx, dx, unloc, total = stats(d)
        print(f"theater: {d['theater']} · {total} formations")
        print("\nby faction:")
        for k, v in fx.most_common():
            print(f"  {k:16s} {v}")
        print("\nclaims by grade:")
        for g in GRADES:
            if gx.get(g):
                print(f"  {g:16s} {gx[g]}")
        print("\nclaims by freshness:")
        for k, v in dx.most_common():
            print(f"  {str(k):16s} {v}")
        print(f"\nunlocated formations: {unloc} of {total} — these are real "
              f"records that do not appear on the map, and the viewer says so.")
        return 0

    if a.cmd == "publish":
        if not publish():
            print(f"no docs/ directory at {DOCS} — nothing published")
            return 1
        return 0

    if a.cmd == "issue":
        return issue(d, a.formation, a.claim, a.p, a.deadline, a.resolution,
                     a.statement)
    if a.cmd == "link":
        return link(d, a.formation, a.kkr_id)

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
