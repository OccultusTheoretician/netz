#!/usr/bin/env python3
"""
fogsim_oob.py — seed a FogSim scenario from the real order of battle.

FogSim runs deterministic, sealed, re-executable scenarios but on abstract
BLUE/RED aggregates that represent no real force. This builds a scenario dict
from the Kaster's *actual* graded formations — real coordinates, real
provenance — so a force-on-force run starts from documented order of battle
rather than invented numbers. Then FogSim proper runs it, unchanged.

THE WALL (non-negotiable, and the entire reason this is a separate tool):
    - reads KriegForeKaster.json; NEVER writes it. The sourced board is
      immutable to this tool.
    - every artifact it emits is stamped SIMULATED and carries the same
      "represents a model, not a conflict picture" disclosure the board and
      the FogSim page already make.
    - real provenance rides INTO the scenario (which formations, what grades,
      what sources, as-of dates) so a reader can see the run rests on dated
      public data and can judge how stale that data is — the sim inherits the
      board's honesty, it does not launder it into false precision.

    python fogsim_oob.py build --blue united-states --red russia \\
        --name "USA vs RUS — documented OOB, illustrative only" \\
        --out fogsim_scenario_oob.json
    python fogsim_oob.py build --blue-ids F-XVIII,F-82ABN --red russia ...
    python fogsim_oob.py forecast --scenario fogsim_scenario_oob.json \\
        --outcome blue_holds --probability 40 --keyless \\
        --rationale "..." --deadline 2026-12-31

`build` writes a scenario FogSim can seal and run. `forecast` binds a sealed
ledger prediction about the run's outcome BEFORE it executes — the auditor's
move: commit the call, then let the deterministic run score it. Nothing here
resolves; kkr --resolve reads the executed FogSim reveal at the deadline.
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import re

HERE = Path(__file__).resolve().parent
BOARD = HERE / "KriegForeKaster.json"
SPINE = HERE / "docs" / "kfk_spine.json"

DISCLOSURE = ("SIMULATED. This scenario is seeded from the Kaster's graded "
              "order of battle but represents a MODEL, not a conflict "
              "picture. Aggregate strengths are derived from documented "
              "formation records under a stated rule; the run certifies the "
              "integrity of the campaign record, never that the model "
              "resembles war. First in this model is not first in the world.")

# STRENGTH MODEL — sourced personnel first, echelon fallback second, both
# disclosed. A state formation's strength is the real active-personnel figure
# from the spine's Factbook field (public domain, graded, dated). Sub-national
# formations, and states whose personnel string will not parse, fall back to
# an echelon weight — and the scenario records WHICH basis each side used, so
# a reader sees where the run rests on sourced counts and where on a proxy.
# Factbook gives personnel only: a real but crude force measure with no
# readiness, equipment quality, or doctrine. Equipment/quality data at the
# expert standard (IISS Military Balance) is licensed and is cited, never
# ingested. Effectiveness stays a fixed per-side constant so the run remains a
# pure function of (scenario, seed) — FogSim's re-execution property.
ECHELON_WEIGHT = {
    "armed forces": 1000.0, "command": 300.0, "corps": 200.0,
    "division": 100.0, "brigade": 30.0, "unit": 10.0,
}


def load_spine():
    try:
        return json.loads(SPINE.read_text(encoding="utf-8-sig"))
    except Exception:
        return {"actors": []}


def parse_personnel(text):
    """Take the first active-force figure from a Factbook personnel string.
    Returns (number, basis_note) or (None, why). Ranges take the LOW end and
    say so; 'million'/'thousand' scale words are honored. Never guesses."""
    t = str(text or "").lower()
    if not t:
        return None, "no personnel string"
    # Four defects the naive "first number wins" scan produced on the live
    # spine, each of which shipped a figure a reader would have believed:
    #   Sudan  -> 2023        a YEAR ("...fighting ... in 2023, size
    #                         estimates ... up to 200,000 SAF ...")
    #   Gaza   -> 2023        a year RANGE ("the 2023-2025 conflict")
    #   Mali   -> 35          low end of "35-40,000", whose scale lives on
    #   Guinea -> 10          the high end only
    # A first pass at the fix introduced a fifth, worse one: scanning for a
    # range ANYWHERE let China's parenthetical "950,000-1 million Ground"
    # override its own headline "approximately 2 million", yielding 9.5e11.
    # So: strip years, anchor on the FIRST digit in the string, and only then
    # ask whether that token opens a range.
    t = re.sub(r"\b(?:19|20)\d{2}\s*[-\u2013]\s*(?:19|20)\d{2}\b", " ", t)
    t = re.sub(r"\(\s*(?:19|20)\d{2}(?:\s*est\.?)?\s*\)", " ", t)
    t = re.sub(r"\b(?:in|since|as of|during)\s+(?:19|20)\d{2}\b", " ", t)

    NUM = r"\d[\d.,]*"           # must START with a digit: a bare comma is
    m = re.search(NUM, t)         # not a number (it read as one before)
    if not m:
        return None, "no number in personnel string"
    lo_s = m.group(0).rstrip(".,")
    tail = t[m.end():]
    rng = re.match(r"\s*(?:[-\u2013]|to)\s*(" + NUM + r")", tail)
    hi_s = rng.group(1).rstrip(".,") if rng else None
    after = tail[rng.end():] if rng else tail
    scale = None
    sm = re.match(r"\s*(million|thousand)\b", after)
    if sm:
        scale = sm.group(1)
    try:
        val = float(lo_s.replace(",", ""))
    except ValueError:
        return None, f"unparseable number {lo_s!r}"
    note = "point figure"
    if hi_s:
        note = "low end of a stated range"
        # "35-40,000": a bare low end inherits the high end's magnitude.
        if "," in hi_s and "," not in lo_s:
            try:
                hival = float(hi_s.replace(",", ""))
            except ValueError:
                hival = 0.0
            if hival > val:
                digits = len(hi_s.replace(",", "").split(".")[0])
                val *= 10 ** (digits - len(lo_s.split(".")[0]))
    if scale == "million":
        val *= 1_000_000
    elif scale == "thousand":
        val *= 1_000
    if val < 500:
        return None, (f"figure {val:g} below the plausibility floor for a "
                      f"national force — string not parsed confidently, so "
                      f"nothing is claimed")
    if val > 5_000_000:
        return None, (f"figure {val:g} above the plausibility ceiling for a "
                      f"national force — refused rather than published")
    return round(val, 0), note


# Bare substring matching bound the wrong actor on 17 name pairs in the live
# spine — 'india' inside 'British Indian Ocean Territory', 'niger' inside
# 'Nigeria', 'mali' inside 'Somalia', 'oman' inside 'Romania', 'sudan' inside
# 'South Sudan', 'guinea' inside three others. First match won, silently, and
# the scenario then carried another country's personnel figure with full
# provenance dressing. Matching is now tiered, and ambiguity is REFUSED
# rather than resolved by loop order.
_ALIAS = {
    "usa": "united states", "us": "united states", "u.s.": "united states",
    "america": "united states", "united states of america": "united states",
    "uk": "united kingdom", "u.k.": "united kingdom",
    "great britain": "united kingdom", "britain": "united kingdom",
    "drc": "congo, democratic republic of the",
    "dr congo": "congo, democratic republic of the",
    "north korea": "korea, north", "south korea": "korea, south",
    "prc": "china", "roc": "taiwan", "uae": "united arab emirates",
    "russian federation": "russia", "czechia": "czech republic",
    "burma": "burma", "myanmar": "burma", "turkiye": "turkey",
}


def _norm(s):
    s = str(s or "").lower()
    s = s.replace(" — national armed forces", "")
    s = re.sub(r"[^a-z0-9,\s-]", " ", s)
    s = re.sub(r"[\s-]+", " ", s).strip()
    s = re.sub(r"^the\s+", "", s)
    return _ALIAS.get(s, s)


def _invert(s):
    """'korea, north' -> 'north korea'; leaves other forms alone."""
    if "," in s:
        head, tail = s.split(",", 1)
        return f"{tail.strip()} {head.strip()}".strip()
    return s


def _candidates(key, actors):
    """Tier 1 exact, tier 2 comma-inverted exact, tier 3 whole-word prefix.

    Tier 3 requires the key to match at a word boundary AND to be the leading
    words of the actor name, which is what kills 'india' -> 'British Indian
    Ocean Territory' and 'oman' -> 'Romania' while keeping 'china' ->
    'China'. Substring-anywhere is never used.
    """
    exact = [a for a in actors if _norm(a.get("name")) == key]
    if exact:
        return exact, "exact name"
    inv = [a for a in actors
           if _invert(_norm(a.get("name"))) == key
           or _norm(a.get("name")) == _invert(key)]
    if inv:
        return inv, "name matched after comma inversion"
    pref = [a for a in actors
            if re.match(r"^" + re.escape(key) + r"\b", _norm(a.get("name")))]
    if pref:
        return pref, "leading whole-word match"
    return [], "no spine actor matched"


def spine_personnel_for(name, spine):
    key = _norm(name)
    if len(key) < 3:
        return {"strength": None,
                "why": f"key {key!r} too short to match safely"}
    actors = [a for a in spine.get("actors", [])
              if a.get("actor_type") == "state"]
    cands, how = _candidates(key, actors)
    if len(cands) > 1:
        names = ", ".join(sorted(str(c.get("name")) for c in cands)[:6])
        return {"strength": None,
                "why": (f"ambiguous: {key!r} matched {len(cands)} spine "
                        f"actors ({names}) — refused rather than guessed; "
                        f"name the formation with --blue-ids/--red-ids")}
    for a in cands:
        if True:
            fld = a.get("fields", {}).get("personnel", {})
            n, why = parse_personnel(fld.get("value"))
            if n:
                return {"strength": n, "basis": "sourced personnel",
                        "detail": f"{why}; {how}", "source": fld.get("source"),
                        "grade": fld.get("grade"), "as_of": fld.get("as_of"),
                        "raw": str(fld.get("value", ""))[:200],
                        "matched": str(a.get("name"))}
            return {"strength": None, "why": f"{why} ({how})",
                    "source": fld.get("source")}
    return {"strength": None, "why": how}


def load_board():
    return json.loads(BOARD.read_text(encoding="utf-8-sig"))


def pick(formations, faction=None, ids=None, detail=False):
    if ids:
        want = {i.strip() for i in ids.split(",")}
        return [f for f in formations if f.get("id") in want]
    if faction:
        key = faction.strip().lower()
        # The board's faction slugs are hyphenated ("united-states") and the
        # tool's own error text recommends that form, but the seed formations
        # are named with spaces ("United States of America — national armed
        # forces"). So `--blue united-states` missed the seed and silently
        # returned 13 sub-national echelon proxies (strength 1090) while
        # `--blue "united states"` returned the sourced national figure
        # (1,280,000). Same command, two incomparable scenarios, no warning.
        nkey = re.sub(r"[-_]+", " ", key).strip()
        # A country name should resolve to its single national armed-forces
        # seed formation (sourced personnel), giving a clean state-vs-state
        # matchup where both sides rest on the same sourced layer. Only when
        # --oob-detail is set do we return the sub-national formations, which
        # are echelon proxies and should be matched against another side's
        # sub-national OOB, not against a national aggregate.
        seed = [f for f in formations
                if f.get("echelon") == "armed forces"
                and (key in str(f.get("name", "")).lower()
                     or nkey in re.sub(r"[-_]+", " ",
                                       str(f.get("name", "")).lower()))]
        subnat = [f for f in formations
                  if f.get("echelon") != "armed forces"
                  and str(f.get("faction", "")).lower() == key]
        # Branch order, corrected: an explicit --oob-detail request must not
        # fall through to the national aggregate when a side has no
        # sub-national formations on the board. Silently swapping echelon
        # proxies for a sourced national figure changes what the run means
        # and hid the substitution inside a matching strength number.
        if detail:
            if not subnat:
                print(f"--oob-detail requested for {faction!r} but the board "
                      f"carries no sub-national formations for it; refusing "
                      f"to substitute the national aggregate. Drop "
                      f"--oob-detail for a state-vs-state run, or name "
                      f"formations with --blue-ids/--red-ids.",
                      file=sys.stderr)
            return subnat
        if seed:
            # One seed per country is the intent; more than one means the
            # board has drifted and the operator should see it, not have it
            # averaged away. (The former "exact" filter here re-applied the
            # same test that built `seed` and could never narrow anything.)
            if len(seed) > 1:
                print(f"warning: {faction!r} matched {len(seed)} "
                      f"armed-forces seeds on the board: "
                      f"{', '.join(str(f.get('name')) for f in seed)}",
                      file=sys.stderr)
            return seed
        return subnat
    return []


def side_block(label, forms, spine):
    strength = 0.0
    members = []
    sourced = fallback = 0
    for f in forms:
        loc = f.get("location") if isinstance(f.get("location"), dict) else {}
        ex = f.get("existence") if isinstance(f.get("existence"), dict) else {}
        rec = {"id": f.get("id"), "name": f.get("name"),
               "echelon": f.get("echelon"),
               "lat": loc.get("lat"), "lon": loc.get("lon"),
               "existence_grade": ex.get("grade")}
        sp = (spine_personnel_for(f.get("name"), spine)
              if f.get("echelon") == "armed forces" else {"strength": None})
        if sp.get("strength"):
            w = sp["strength"]
            rec.update({"basis": "sourced personnel", "weight": w,
                        "personnel_source": sp.get("source"),
                        "personnel_grade": sp.get("grade"),
                        "personnel_as_of": sp.get("as_of"),
                        "personnel_raw": sp.get("raw"),
                        "basis_detail": sp.get("detail")})
            sourced += 1
        else:
            w = ECHELON_WEIGHT.get(f.get("echelon"), 10.0)
            rec.update({"basis": "echelon proxy", "weight": w,
                        "basis_detail": sp.get("why", "no sourced personnel")})
            fallback += 1
        strength += w
        members.append(rec)
    return {
        "label": label,
        "strength": round(strength, 1),
        "effectiveness": 0.0013,   # fixed constant — see module note
        "provenance": {
            "formation_count": len(forms),
            "sourced_personnel": sourced,
            "echelon_fallback": fallback,
            "members": members,
            "strength_model": (f"strength = sum of real active-personnel "
                               f"figures where the spine sources them "
                               f"({sourced} of {len(forms)}), echelon proxy "
                               f"otherwise ({fallback}); personnel is a real "
                               f"but crude measure — no equipment quality or "
                               f"readiness. IISS-class data is licensed, "
                               f"cited not ingested."),
        },
    }


def cmd_build(a):
    board = load_board()
    spine = load_spine()
    forms = board["formations"]
    blue = pick(forms, a.blue, a.blue_ids, a.oob_detail)
    red = pick(forms, a.red, a.red_ids, a.oob_detail)
    if not blue or not red:
        print(f"empty side — blue {len(blue)}, red {len(red)}. Name a faction "
              f"present on the board (e.g. united-states, russia, china) or "
              f"--blue-ids/--red-ids with real formation ids.", file=sys.stderr)
        # print available factions to make the miss self-correcting
        fac = sorted({str(f.get("faction")) for f in forms})
        print("factions on the board:", ", ".join(fac), file=sys.stderr)
        return 1
    bb = side_block(a.blue or "BLUE", blue, spine)
    rb = side_block(a.red or "RED", red, spine)
    bp0, rp0 = bb["provenance"], rb["provenance"]
    mixed = ((bp0["sourced_personnel"] and not rp0["sourced_personnel"])
             or (rp0["sourced_personnel"] and not bp0["sourced_personnel"]))
    if mixed and not getattr(a, "allow_mixed_basis", False):
        print(f"REFUSED — mixed strength bases. BLUE rests on "
              f"{'sourced personnel' if bp0['sourced_personnel'] else 'echelon proxies'} "
              f"(strength {bb['strength']}), RED on "
              f"{'sourced personnel' if rp0['sourced_personnel'] else 'echelon proxies'} "
              f"(strength {rb['strength']}). Personnel counts and echelon "
              f"proxy weights differ by ~3 orders of magnitude; a run across "
              f"them is arithmetic, not a matchup. Put both sides on the same "
              f"layer, or pass --allow-mixed-basis to seal it anyway with the "
              f"mismatch stamped into the artifact.", file=sys.stderr)
        return 1
    scenario = {
        "name": a.name or f"{a.blue or 'BLUE'} vs {a.red or 'RED'} — "
                          f"documented OOB, illustrative only",
        "simulated": True,
        "disclosure": DISCLOSURE,
        "seeded_from": {
            "board": "KriegForeKaster.json",
            "board_as_of": board.get("as_of"),
            "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
        "blue": bb,
        "red": rb,
        "basis_comparability": ("both sides on the same strength layer"
                               if not mixed else
                               "MIXED BASIS, sealed under explicit override: "
                               "one side is sourced personnel, the other "
                               "echelon proxies; the strengths are not "
                               "commensurable and this run's outcome carries "
                               "that defect"),
        "parameters": {"dt": 1.0, "max_ticks": a.max_ticks,
                       "break_fraction": a.break_fraction, "shock": a.shock},
    }
    out = HERE / a.out
    out.write_text(json.dumps(scenario, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(f"SIMULATED scenario written → {a.out}")
    bp, rp = scenario["blue"]["provenance"], scenario["red"]["provenance"]
    print(f"  BLUE {scenario['blue']['label']}: {len(blue)} formations, "
          f"strength {scenario['blue']['strength']} "
          f"({bp['sourced_personnel']} sourced, {bp['echelon_fallback']} proxy)")
    print(f"  RED  {scenario['red']['label']}: {len(red)} formations, "
          f"strength {scenario['red']['strength']} "
          f"({rp['sourced_personnel']} sourced, {rp['echelon_fallback']} proxy)")
    print(f"  board untouched (read-only). Now seal + run with FogSim:")
    print(f"    python fogsim.py seal --scenario {a.out} --count N --question "
          f"\"...\" --hashlog fogsim_hashlog_oob.json")
    print(f"    python fogsim.py run  --scenario {a.out} ... ; "
          f"python fogsim.py reveal ...")
    return 0


def cmd_forecast(a):
    """Bind a sealed ledger forecast about the run's outcome, before it runs.
    Uses the ledger's own seal + gate, arm fogsim/scenario."""
    scen = json.loads((HERE / a.scenario).read_text(encoding="utf-8-sig"))
    if not scen.get("simulated"):
        print("refusing: scenario is not stamped simulated — this arm is for "
              "model forecasts only, never a claim about the real world.",
              file=sys.stderr)
        return 1
    import kkr
    from candidate_desk import seal
    from kkr import validate_projection

    now = datetime.now(timezone.utc)
    entry = {
        "id": None,
        "date_issued": now.strftime("%Y-%m-%d"),
        "deadline": a.deadline,
        "statement": (f"In the FogSim sealed campaign for scenario "
                      f"\"{scen['name']}\" (SIMULATED, seeded from the graded "
                      f"order of battle), the modal outcome across the "
                      f"declared run set is \"{a.outcome}\"."),
        "resolution": (f"Resolved from the executed FogSim reveal for this "
                       f"scenario (fogsim_reveal_oob.json in this repository) "
                       f"read on {a.deadline}: YES if the most frequent "
                       f"outcome across revealed runs equals \"{a.outcome}\". "
                       f"This scores a MODEL, not a war."),
        "probability": a.probability,
        "failure_condition": (f"The modal revealed outcome is not "
                              f"\"{a.outcome}\" at the deadline; the run is a "
                              f"pure function of scenario, rules version and "
                              f"seed, so a miss is a fully re-executable "
                              f"fact. A model outcome is not a world outcome."),
        "keyed_keyless": "keyed" if a.keyed else "keyless",
        "keyed_keyless_rationale": a.rationale.strip(),
        "status": "open",
        "model": "fogsim/scenario",
        "resolved_date": None,
        "audit": None,
        "notes": f"SIMULATED forecast; scenario seeded from board "
                 f"{scen.get('seeded_from', {}).get('board_as_of')}",
    }
    reasons = [r for r in validate_projection(
        {"statement": entry["statement"], "resolution": entry["resolution"],
         "deadline": entry["deadline"], "probability": entry["probability"],
         "domain": "scenario"})
        if r != "no grounding citations to the report record"]
    if reasons:
        print("NOT SEALED — gate rejects:", file=sys.stderr)
        for r in reasons:
            print(f"  ✗ {r}", file=sys.stderr)
        return 1
    data = kkr.load_ledger()
    tag = now.strftime("%Y%m%d")
    n = 1 + sum(1 for e in data["projections"]
                if str(e.get("id", "")).startswith(f"FS-{tag}-"))
    entry["id"] = f"FS-{tag}-{n:02d}"
    seal(entry)
    data["projections"].append(entry)
    kkr.save_ledger(data)
    print(f"SEALED · {entry['id']} · fogsim/scenario · p={a.probability}% · "
          f"outcome \"{a.outcome}\" · deadline {a.deadline} · "
          f"{entry['keyed_keyless']}")
    print(f"  seal {entry['seal_sha256'][:16]}… — copy ledger.json to docs\\, "
          f"commit both. Then seal+run the FogSim campaign; resolve at "
          f"deadline via kkr --resolve.")
    return 0


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--blue"); b.add_argument("--red")
    b.add_argument("--blue-ids"); b.add_argument("--red-ids")
    b.add_argument("--name")
    b.add_argument("--out", default="fogsim_scenario_oob.json")
    b.add_argument("--max-ticks", type=int, default=600)
    b.add_argument("--break-fraction", type=float, default=0.55)
    b.add_argument("--shock", type=float, default=0.35)
    b.add_argument("--allow-mixed-basis", action="store_true",
                   help="seal a run whose sides rest on different strength "
                        "layers; the mismatch is stamped into the artifact")
    b.add_argument("--oob-detail", action="store_true",
                   help="draw sub-national formations (echelon proxies) "
                        "instead of the sourced national seed; match only "
                        "against another --oob-detail side")
    f = sub.add_parser("forecast")
    f.add_argument("--scenario", default="fogsim_scenario_oob.json")
    f.add_argument("--outcome", required=True,
                   choices=["blue_holds", "red_holds", "mutual_break",
                            "no_decision"])
    f.add_argument("--probability", type=int, required=True)
    f.add_argument("--deadline", required=True)
    g = f.add_mutually_exclusive_group(required=True)
    g.add_argument("--keyed", action="store_true")
    g.add_argument("--keyless", action="store_true")
    f.add_argument("--rationale", required=True)
    a = ap.parse_args()
    return {"build": cmd_build, "forecast": cmd_forecast}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
