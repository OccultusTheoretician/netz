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
from datetime import datetime, timezone, date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA_FILE = HERE / "KriegForeKaster.json"
DOCS = HERE / "docs"
PROJ_OUT = HERE / "KriegForeKaster_projections.json"

GRADES = ["CONFESSED", "PROOF-VERBATIM", "DOCUMENTED", "REPORTED",
          "DERIVED", "SPECULATIVE"]
NEEDS_RATIONALE = {"DERIVED", "SPECULATIVE"}
NEVER_ISSUE = {"SPECULATIVE"}

ECHELONS = ["armed forces", "service", "theater", "front", "army group", "army",
            "corps", "division", "brigade", "regiment", "battalion", "company",
            "detachment"]

# days after which a claim is stale enough that displaying it as current is a lie
# Subordination joins the ladder. It was the only load-bearing field in this
# schema carrying no grade, no source and no date — a relationship determining
# the whole structure of the board, settable by anyone and checkable by no one.
# That is the undocumented-tab defect and it does not get to live here.
HALF_LIFE = {"existence": 365, "composition": 180, "subordination": 730,
             "order_of_battle": 180, "factionalization": 365,
             "commander": 60, "posture": 21, "location": 14}

CLAIM_BLOCKS = list(HALF_LIFE.keys())

# What a coordinate actually points at. Precision is DECLARED, never implied:
# 195 of these locate a capital, which locates a state and not a command.
DENOTES = ["headquarters", "installation centroid", "capital centroid", "approximate"]

# Which of those actually locate a COMMAND. This is the distinction the record
# has always carried and the counts never read. A capital centroid is not a
# defective coordinate — it is an honest one, declaring that nobody has sourced
# where the formation sits. Counting it as "located" turned a truthful field
# into a false claim on the face.
COMMAND_PRECISION = {"headquarters", "installation centroid"}
STATE_PRECISION = {"capital centroid", "approximate"}


def command_located(f: dict) -> bool:
    """True only where a coordinate points at a command. Unknown denotes -> False."""
    loc = f.get("location") or {}
    return loc.get("denotes") in COMMAND_PRECISION


def state_only(f: dict) -> bool:
    """A coordinate that locates the state and not the command."""
    loc = f.get("location") or {}
    return loc.get("denotes") in STATE_PRECISION

# ----------------------------------------------------------------------
# ORDER OF BATTLE — counts, by class, each with its own source
# ----------------------------------------------------------------------
OOB_FIELDS = ["active_personnel", "reserve_personnel", "paramilitary_personnel",
              "manoeuvre_divisions", "manoeuvre_brigades", "main_battle_tanks",
              "artillery_systems", "combat_aircraft", "rotary_wing",
              "principal_surface_combatants", "submarines", "special_operations_units"]

# ----------------------------------------------------------------------
# FACTIONALIZATION — coup-proofing structure, and ONLY structure.
#
# These are the observable, sourceable features of a force built to be
# survivable against its own officers: parallel chains, praetorian units,
# who appoints generals, how soldiers are recruited, whether commands rotate.
# All of it is published — constitutions, org charts, defence white papers,
# the standard literature on coup-proofing in authoritarian regimes.
#
# What is deliberately absent is a field for INTENT. There is nowhere in this
# schema to record that one faction secretly controls another, that a coup is
# being prepared, or who is really in charge. Structure is checkable and
# purpose is not, and a board that asserts hidden purpose about a real
# military is unfalsifiable — which is the property this entire apparatus
# exists to refuse. Record the architecture. Let a reader draw the inference,
# and let the forecast be the thing that tests it.
# ----------------------------------------------------------------------
FACTION_INDICATORS = {
    "parallel_forces": ("Armed services with independent chains of command to the "
                        "head of state, outside the regular defence ministry.",
                        ["single unified chain", "one semi-autonomous branch",
                         "two chains, overlapping missions",
                         "two chains, competing missions and separate procurement",
                         "three or more, with separate industrial bases"]),
    "praetorian_units": ("Formations whose stated mission is regime or leadership "
                         "protection, standing outside the regular order of battle.",
                         ["none", "ceremonial guard only", "brigade-scale, armed",
                          "division-scale with armour",
                          "corps-scale with independent logistics and air"]),
    "appointment_control": ("Who appoints and removes general officers.",
                            ["merit board, published criteria",
                             "defence ministry with legislative confirmation",
                             "defence ministry, executive discretion",
                             "head of state directly, no confirmation",
                             "head of state directly, with a political vetting body"]),
    "recruitment_basis": ("How the force is manned, and whether documented sources "
                          "report ethnic, sectarian or regional stacking in the "
                          "officer corps.",
                          ["volunteer, no reported stacking",
                           "conscription, no reported stacking",
                           "reported stacking in selected formations",
                           "documented stacking in the officer corps",
                           "documented stacking with a formal quota or exclusion"]),
    "command_rotation": ("Whether senior commands rotate on a published schedule, "
                         "which limits constituency-building in a formation.",
                         ["published rotation, observed", "published, observed unevenly",
                          "no published policy, rotation occurs",
                          "long tenures common", "indefinite tenure normal"]),
    "internal_security_role": ("Whether regular armed forces hold a standing domestic "
                               "security mission.",
                               ["none, constitutionally barred", "disaster response only",
                                "border and counter-terror", "standing domestic mission",
                                "primary mission is internal"]),
    "coup_record": ("Documented coups or attempted coups in the last fifty years.",
                    ["none", "one attempt, failed", "one successful",
                     "two or more attempts", "two or more successful"]),
}
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
        if isinstance(par, str) and par:
            errs.append(f"{p}: parent is a bare id with no grade, source or date. "
                        f"Subordination determines the structure of this board and "
                        f"must be recorded as a claim like any other.")
        elif isinstance(par, dict):
            pid = par.get("id")
            if not pid:
                errs.append(f"{p}.subordination: no parent id")
            elif pid not in ids:
                errs.append(f"{p}.subordination: parent '{pid}' does not exist")
            else:
                pf = next(x for x in d["formations"] if x["id"] == pid)
                if (pf.get("echelon") in ECHELONS and f.get("echelon") in ECHELONS
                        and ECHELONS.index(pf["echelon"]) >= ECHELONS.index(f["echelon"])):
                    errs.append(f"{p}.subordination: '{pid}' is not a higher echelon")

        if not f.get("existence"):
            errs.append(f"{p}: no existence claim — a formation with no evidence "
                        f"that it exists is not a record, it is a guess")

        for b in CLAIM_BLOCKS:
            blk = f.get("parent") if b == "subordination" else f.get(b)
            if not blk or not isinstance(blk, dict):
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

        oob = f.get("order_of_battle")
        if isinstance(oob, dict):
            for k in oob:
                if k in ("grade", "as_of", "sources", "note", "rationale"):
                    continue
                if k not in OOB_FIELDS:
                    errs.append(f"{p}.order_of_battle: '{k}' is not a recognised count "
                                f"field; add it to OOB_FIELDS or drop it")
        fx = f.get("factionalization")
        if isinstance(fx, dict):
            for k, v in fx.items():
                if k in ("grade", "as_of", "sources", "note", "rationale"):
                    continue
                if k not in FACTION_INDICATORS:
                    errs.append(f"{p}.factionalization: '{k}' is not a structural "
                                f"indicator. This block records ARCHITECTURE only — "
                                f"there is no field here for intent, control or "
                                f"allegiance, by design.")
                elif not (isinstance(v, int) and 0 <= v <= 4):
                    errs.append(f"{p}.factionalization.{k}: score must be 0-4")

        loc = f.get("location")
        if loc and loc.get("denotes") not in DENOTES:
            errs.append(f"{p}.location: denotes is {loc.get('denotes')!r} — a coordinate "
                        f"must state what it points at, one of {DENOTES}. A capital "
                        f"centroid locates a state, not a command.")
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
            blk = f.get("parent") if b == "subordination" else f.get(b)
            state, a = decay_state(b, blk if isinstance(blk, dict) else None)
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
            blk = f.get("parent") if b == "subordination" else f.get(b)
            if isinstance(blk, dict):
                gx[blk.get("grade")] += 1
                dx[decay_state(b, blk)[0]] += 1
        if not f.get("location"):
            unloc += 1
    return fx, gx, dx, unloc, len(d["formations"])


# ----------------------------------------------------------------------
def freshness(d: dict) -> dict:
    """The freshness layer.

    Nobody can beat Janes on where the formation is. What nobody publishes at
    all is how long it has been since anyone could say. That is computable from
    open sources alone, it is honest, and it is the one number a coverage vendor
    is structurally barred from printing, because their product is confidence.
    """
    per_class = {b: [] for b in CLAIM_BLOCKS}
    per_form, states = {}, {}
    for f in d["formations"]:
        worst = None
        for b in CLAIM_BLOCKS:
            blk = f.get("parent") if b == "subordination" else f.get(b)
            if not blk or not isinstance(blk, dict):
                continue
            st, a = decay_state(b, blk)
            states[st] = states.get(st, 0) + 1
            if a is None:
                continue
            per_class[b].append(a)
            ratio = a / HALF_LIFE[b]
            if worst is None or ratio > worst[1]:
                worst = (b, ratio, a)
        per_form[f["id"]] = {
            "name": f["name"],
            "stalest_claim": worst[0] if worst else None,
            "age_days": worst[2] if worst else None,
            "half_lives_elapsed": round(worst[1], 2) if worst else None,
            "command_located": command_located(f),
            "state_only": state_only(f),
            # unlocated now means NOT command-located, which is what every
            # downstream reader already assumed it meant.
            "unlocated": not command_located(f)}
    summary = {}
    for b, ages in per_class.items():
        rec = {"n": len(ages), "half_life_days": HALF_LIFE[b]}
        if ages:
            ages = sorted(ages)
            rec.update({"median_age_days": ages[len(ages) // 2],
                        "max_age_days": ages[-1],
                        "past_half_life": sum(1 for a in ages if a > HALF_LIFE[b])})
        summary[b] = rec
    return {"schema": "kfk-freshness/1.0",
            "generator": "KriegForeKaster.py",
            "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "theater": d["theater"],
            "formations": len(d["formations"]),
            "claim_states": states,
            "by_claim_class": summary,
            "by_formation": per_form}


def halflife_projections(d: dict, claim: str = "commander", horizon: int = None):
    """Turn the decay model into forecasts that score it.

    A half-life is an assertion, and assertions are what this whole apparatus
    exists to distrust. Issued at exactly one half-life the model says fifty
    percent, so these rows can never show SKILL — a 50% row costs 0.25 whatever
    happens. What they test is CALIBRATION: across enough of them the realised
    frequency should land near the stated one. That is why they belong on their
    own arm and must never be pooled with judgement forecasts.
    """
    h = HALF_LIFE[claim]
    t = horizon or h
    out, skipped = [], []
    for f in d["formations"]:
        blk = f.get("parent") if claim == "subordination" else f.get(claim)
        if not isinstance(blk, dict) or not blk:
            skipped.append((f["id"], f"no {claim} claim"))
            continue
        if blk.get("grade") in NEVER_ISSUE:
            skipped.append((f["id"], f"{claim} graded {blk['grade']}"))
            continue
        # A formation already carrying a projection is not re-issued. Two live rows
        # on the same claim are correlated by construction, and correlated rows are
        # not independent observations against the thirty-resolution floor.
        if f.get("projections"):
            skipped.append((f["id"], f"already carries {len(f['projections'])} "
                                     f"projection(s) — link before re-issuing"))
            continue
        as_of = parse_day(blk.get("as_of"))
        if as_of is None:
            skipped.append((f["id"], "undated claim"))
            continue
        deadline = as_of + timedelta(days=t)
        if deadline <= date.today() + timedelta(days=3):
            skipped.append((f["id"], f"deadline {deadline} inside the ledger 3-day floor"))
            continue
        p = max(5, min(95, int(round((1 - 0.5 ** (t / h)) * 100))))
        src = (blk.get("sources") or [""])[0]
        if claim == "commander":
            who = " ".join(x for x in (blk.get("rank"), blk.get("name")) if x)
            stmt = (f"{who} will no longer be named as commanding officer of the "
                    f"{f['name']} in the source of record on {deadline.isoformat()}.")
            res = (f"Resolved on {deadline.isoformat()} by inspecting {src} : hit if a "
                   f"different officer is named, miss if the same officer is named.")
        else:
            val = blk.get("value") or blk.get("place") or blk.get("summary") or "the recorded value"
            stmt = (f"The {claim} of the {f['name']} recorded as {val} will differ in "
                    f"the source of record on {deadline.isoformat()}.")
            res = (f"Resolved on {deadline.isoformat()} by inspecting {src} : hit if the "
                   f"recorded {claim} differs, miss if it is unchanged.")
        out.append({"statement": stmt, "domain": "military/conflict",
                    "probability": p, "resolution": res,
                    "deadline": deadline.isoformat(), "citations": [0],
                    "_formation": f["id"]})
    return out, skipped, t, h


# ----------------------------------------------------------------------
TEMPLATE = {
    "id": "F-XXXX",
    "faction": "faction-id-declared-in-the-file",
    "echelon": "armed forces",
    "parent": None,
    "name": "",
    "designation": "",
    "existence": {"grade": "DOCUMENTED", "as_of": "TODAY", "sources": [""],
                  "note": "what the source is, and whether as_of is a publication "
                          "date or a retrieval date"},
    "location": {"lat": 0.0, "lon": 0.0, "place": "", "denotes": "headquarters",
                 "grade": "DOCUMENTED", "as_of": "TODAY", "sources": [""],
                 "note": "centroid, approximate; headquarters not deployed position"},
    "commander": {"name": "", "rank": "", "grade": "DOCUMENTED",
                  "as_of": "TODAY", "sources": [""], "note": ""},
    "projections": [],
    "notes": "",
}


def report(d, fid):
    """A full battle report for one force, printing the GAPS as loudly as the
    facts. A report that shows only what is known reads as knowledge; this one
    shows the shape of the ignorance next to it, which is the honest form."""
    f = next((x for x in d["formations"] if x["id"] == fid), None)
    if f is None:
        print(f"FAIL — no formation {fid}", file=sys.stderr); return 1
    fac = next((x for x in d["factions"] if x["id"] == f.get("faction")), {})
    print(f"\n{'='*70}")
    print(f"  {f['name']}")
    print(f"  {f.get('designation','')} · {f.get('echelon','')} · {fac.get('name','')}")
    print(f"{'='*70}")

    for b in CLAIM_BLOCKS:
        blk = f.get("parent") if b == "subordination" else f.get(b)
        title = b.replace("_", " ").upper()
        if not isinstance(blk, dict):
            print(f"\n  {title}\n    — no claim recorded")
            continue
        st, age = decay_state(b, blk)
        print(f"\n  {title}   [{blk.get('grade')}]  as of {blk.get('as_of')}"
              f"  ({st}{'' if age is None else f', {age}d, half-life {HALF_LIFE[b]}d'})")
        if b == "order_of_battle":
            any_ = False
            for k in OOB_FIELDS:
                v = blk.get(k)
                if v is not None:
                    print(f"    {k.replace('_',' '):32s} {v:>12,}" if isinstance(v, int)
                          else f"    {k.replace('_',' '):32s} {v}")
                    any_ = True
                else:
                    print(f"    {k.replace('_',' '):32s} {'—':>12}")
            if not any_:
                print("    every field empty — the block exists and states nothing")
        elif b == "factionalization":
            for k, (desc, levels) in FACTION_INDICATORS.items():
                v = blk.get(k)
                if isinstance(v, int) and 0 <= v <= 4:
                    print(f"    {k.replace('_',' '):24s} {v}  {levels[v]}")
                else:
                    print(f"    {k.replace('_',' '):24s} —  unscored")
            idx = faction_index(blk)
            print(f"    {'─'*60}")
            if idx is None:
                print("    no index — nothing scored")
            else:
                print(f"    structural factionalization index  {idx:.2f}")
                print("    0 = one chain, merit appointment, no praetorians.")
                print("    1 = parallel armies, praetorian corps, personal appointment.")
                print("    This measures ARCHITECTURE. It says nothing about anyone's")
                print("    intent, and there is no field in this schema to record any.")
        else:
            for k in ("summary", "value", "name", "rank", "place", "id", "note",
                      "rationale", "denotes"):
                if blk.get(k):
                    print(f"    {k}: {blk[k]}")
        for u in (blk.get("sources") or []):
            print(f"    source: {u}")
        if not (blk.get("sources") or []):
            print("    source: none — permitted only for DERIVED and SPECULATIVE")
    if f.get("projections"):
        print(f"\n  UNDER FORECAST\n    " + ", ".join(f["projections"]))
    print()
    return 0


def faction_index(blk):
    vals = [blk.get(k) for k in FACTION_INDICATORS]
    vals = [v for v in vals if isinstance(v, int) and 0 <= v <= 4]
    return (sum(vals) / (4 * len(vals))) if vals else None


def cmd_template():
    t = json.loads(json.dumps(TEMPLATE).replace("TODAY", date.today().isoformat()))
    print(json.dumps(t, indent=2, ensure_ascii=False))
    print("\n# Fill it, drop the blocks you have no source for, then:", file=sys.stderr)
    print("#   python KriegForeKaster.py add --from new.json", file=sys.stderr)
    print("# A block with no source is rejected unless it is graded DERIVED or",
          file=sys.stderr)
    print("# SPECULATIVE and carries a rationale. That is the point of the gate.",
          file=sys.stderr)
    return 0


def cmd_add(d, path):
    """Insert one formation, but only if it survives the same audit as the file.

    Intake is where an order of battle rots. A record entered without a source
    is indistinguishable from one entered with a source a week later, so the
    gate runs before the write, not after.
    """
    try:
        new = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:
        print(f"FAIL — cannot read {path}: {e}", file=sys.stderr); return 1
    if isinstance(new, list):
        incoming = new
    else:
        incoming = [new]
    ids = {f["id"] for f in d["formations"]}
    for rec_ in incoming:
        if rec_.get("id") in ids:
            print(f"FAIL — {rec_.get('id')} already exists", file=sys.stderr); return 1
        if rec_.get("id", "").startswith("F-XXXX"):
            print("FAIL — the template id was not replaced", file=sys.stderr); return 1
    trial = json.loads(json.dumps(d))
    trial["formations"].extend(incoming)
    errs = validate(trial)
    if errs:
        print(f"REJECTED — {len(errs)} finding(s), nothing written:", file=sys.stderr)
        for e in errs:
            print(f"  · {e}", file=sys.stderr)
        return 1
    d["formations"].extend(incoming)
    save(d)
    for rec_ in incoming:
        print(f"added · {rec_['id']} · {rec_['name']}")
    print(f"{len(d['formations'])} formations")
    return 0


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
    sub.add_parser("template")
    rp = sub.add_parser("report")
    rp.add_argument("formation")
    ad = sub.add_parser("add")
    ad.add_argument("--from", dest="src", required=True,
                    help="JSON file holding one formation, or an array of them")
    sub.add_parser("freshness")
    hl = sub.add_parser("halflife")
    hl.add_argument("--claim", choices=CLAIM_BLOCKS, default="commander")
    hl.add_argument("--horizon", type=int, default=None,
                    help="days; defaults to one half-life, where the model says 50%%")
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

    if a.cmd == "template":
        return cmd_template()

    d = load()

    if a.cmd == "add":
        return cmd_add(d, a.src)

    if a.cmd == "report":
        return report(d, a.formation)

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
        print(f"\nnot located to a command: {unloc} of {total} — these are real "
              f"records that do not appear on the map, and the viewer says so.")
        return 0

    if a.cmd == "publish":
        if not publish():
            print(f"no docs/ directory at {DOCS} — nothing published")
            return 1
        return 0

    if a.cmd == "freshness":
        fr = freshness(d)
        print(f"FRESHNESS — {fr['theater']} · as of {fr['as_of']}\n")
        for b, r in fr["by_claim_class"].items():
            if not r["n"]:
                print(f"  {b:12s} no claims recorded")
                continue
            print(f"  {b:12s} n={r['n']:<3d} half-life {r['half_life_days']:>3d}d · "
                  f"median {r['median_age_days']:>4d}d · oldest {r['max_age_days']:>4d}d · "
                  f"{r['past_half_life']} past half-life")
        print("\n  stalest claim per formation:")
        for fid, r in sorted(fr["by_formation"].items(),
                             key=lambda kv: -(kv[1]["half_lives_elapsed"] or 0)):
            hl = r["half_lives_elapsed"]
            print(f"    {fid:10s} {r['name'][:34]:34s} {str(r['stalest_claim']):11s} "
                  f"{str(r['age_days']):>5s}d = {hl} half-lives"
                  + ("  [state-only]" if r.get("state_only") else ("  [unlocated]" if r["unlocated"] else "")))
        print(f"\n  claim states: {fr['claim_states']}")
        if DOCS.exists():
            (DOCS / "freshness.json").write_text(
                json.dumps(fr, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"\npublished -> {DOCS / 'freshness.json'}")
        else:
            print(f"\nno docs/ at {DOCS} — not published")
        return 0

    if a.cmd == "halflife":
        rows, skipped, t, h = halflife_projections(d, a.claim, a.horizon)
        print(f"HALF-LIFE CALIBRATION SET — claim '{a.claim}', half-life {h}d, "
              f"horizon {t}d, model probability "
              f"{max(5, min(95, int(round((1 - 0.5 ** (t / h)) * 100))))}%\n")
        for r in rows:
            print(f"  {r['_formation']:10s} p={r['probability']:>2d}% due {r['deadline']}")
            print(f"             {r['statement']}")
        for fid, why in skipped:
            print(f"  SKIP {fid:10s} {why}")
        if not rows:
            print("\nNothing to issue.")
            return 1
        clean = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
        PROJ_OUT.write_text(json.dumps(clean, indent=2, ensure_ascii=False),
                            encoding="utf-8")
        print(f"\nwritten -> {PROJ_OUT}")
        print("\nThese rows test CALIBRATION, not skill: at one half-life the model "
              "says 50%, and a 50% row costs 0.25 whatever happens. They must go on "
              "their own arm and never be pooled with judgement calls.\n")
        print(f"  python kkr.py --ingest {PROJ_OUT.name} --arm kfk/halflife")
        print("then link each id back with:  python KriegForeKaster.py link <F-id> <KKR-id>")
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
