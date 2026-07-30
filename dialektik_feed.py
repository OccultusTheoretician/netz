#!/usr/bin/env python3
"""
dialektik_feed.py — War Desk pull -> proposed live dyad for dialektik.

WHAT IT DOES
Reads the newest graded events pull, filters to one theatre and one pair of
hostile sides, and writes a dyad file in dialektik's schema with:
  - stated_posture drafted from the cross-side STATEMENT track (circulation,
    not truth — the desk's own doctrine, restated in the draft),
  - per-indicator PROPOSALS from the KINETIC track, each carrying the events
    it derived from, the mechanical rule used (if any), and an honest grade.

WHAT IT REFUSES TO DO
It does not score what the corpus cannot see. Trade flows, hotlines, sanctions
architecture and insurance premia are invisible to a watched-channel pull;
those indicators are emitted unscored with the external source class named.
A proposed score appears ONLY where a stateable mechanical rule produced it,
and the rule is printed inside the file next to the score. Corpus absence is
never treated as world absence — every derived proposal says so.

REVIEW IS THE GATE. This file is a proposal. Scores recorded without your
review would be the instrument scoring itself, which is the failure dialektik
exists to prevent. After review and correction:

    python dialektik.py score --dyad <outfile>

    python dialektik_feed.py --zone iran
    python dialektik_feed.py --zone russia_ukraine
    python dialektik_feed.py --zone iran --sides AXIS,WEST --prereg-id KKR-20260730-01
"""
import argparse
import glob
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

DEFAULT_SIDES = {
    "iran": ("AXIS", "WEST"),
    "russia_ukraine": ("RU", "UA"),
    "israel_gaza": ("IL", "PS"),
}

# anchors whose striking bears directly on transit continuity, per zone
CHOKEPOINTS = {
    "iran": {"strait of hormuz", "hormuz", "bandar abbas", "qeshm", "qeshm island"},
    "russia_ukraine": {"odesa", "odessa", "sevastopol", "kerch"},
    "israel_gaza": {"suez", "eilat", "ashdod", "haifa"},
}

INDICATOR_KEYS = ["trade", "transit", "deconfliction", "target_selection",
                  "sanctions", "civil_continuity", "market_prepositioning"]


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def newest_events(explicit=None):
    if explicit:
        p = Path(explicit)
        return p if p.exists() else None
    cands = []
    for base in (HERE / "forecasts", HERE, Path.cwd()):
        cands += glob.glob(str(base / "tg_events_*.json"))
    return Path(sorted(set(cands))[-1]) if cands else None


def graded(e):
    return str(e.get("grade", "")).startswith(("A", "B"))


def anchors_of(e):
    out = []
    for k in ("anchor", "anchor_aliases"):
        v = e.get(k) or []
        out += [str(x).lower() for x in v]
    return out


def evline(e):
    return {
        "anchor": ", ".join(e.get("anchor") or ["?"]),
        "grade": str(e.get("grade", "?"))[:1],
        "sides": e.get("sides") or [],
        "n_reports": e.get("n_reports"),
        "weapons": e.get("weapons") or [],
        "first_seen": e.get("first_seen"),
        "track": e.get("track"),
    }


def ind(score, grade, sources, rationale, evidence, rule=None):
    d = {"score": score, "grade": grade,
         "as_of": datetime.now(timezone.utc).date().isoformat(),
         "sources": sources, "rationale": rationale,
         "evidence": evidence, "requires_review": True}
    if rule:
        d["rule"] = rule
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zone", default="iran")
    ap.add_argument("--sides", default=None,
                    help="two side codes, comma-separated, e.g. AXIS,WEST")
    ap.add_argument("--file", default=None)
    ap.add_argument("--dyad-name", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--prereg-id", default=None,
                    help="KKR id pre-registering the market threshold for this dyad")
    a = ap.parse_args()

    src = newest_events(a.file)
    if src is None:
        print("no tg_events_*.json found and no --file given.", file=sys.stderr)
        return 1

    if a.sides:
        parts = [s.strip().upper() for s in a.sides.split(",") if s.strip()]
        if len(parts) != 2:
            print("--sides needs exactly two codes, e.g. AXIS,WEST", file=sys.stderr)
            return 1
        s1, s2 = parts
    elif a.zone in DEFAULT_SIDES:
        s1, s2 = DEFAULT_SIDES[a.zone]
    else:
        print(f"no default sides for zone '{a.zone}' — pass --sides A,B",
              file=sys.stderr)
        return 1

    doc = read_json(src)
    events = doc.get("events", [])
    zone_ev = [e for e in events if e.get("zone") == a.zone]
    if not zone_ev:
        print(f"{src.name}: no events in zone '{a.zone}'.", file=sys.stderr)
        return 1

    def touches_both(e):
        s = set(e.get("sides") or [])
        return s1 in s and s2 in s

    dyad_ev = [e for e in zone_ev if touches_both(e) and graded(e)]
    kinetic = [e for e in dyad_ev if e.get("track") == "kinetic"]
    statements = [e for e in dyad_ev if e.get("track") == "statement"]
    # one-side context: echo inside either party, listed but never scored on
    context = [e for e in zone_ev if graded(e) and not touches_both(e)]

    seen = [e.get("first_seen") for e in dyad_ev if e.get("first_seen")]
    last = [e.get("last_seen") for e in dyad_ev if e.get("last_seen")]
    window = {"from": min(seen)[:10] if seen else "",
              "to": max(last or seen)[:10] if (last or seen) else ""}

    # ---------------- stated posture: circulation, not truth ---------------
    claim_bits = []
    for e in statements:
        anchor = ", ".join(e.get("anchor") or ["?"])
        claim_bits.append(f"{anchor} ({'/'.join(e.get('sides') or [])})")
    stated = ("Cross-side circulating claims in the pull window between "
              f"{s1} and {s2}: " + ("; ".join(claim_bits) if claim_bits
              else "none crossed the divide") + ". "
              "Statement cross-bias confirms an utterance exists, not that it "
              "is true — the desk grades circulation, the analyst judges "
              "content. FILL: the parties' official stated posture from "
              "primary statements before scoring.")

    # ---------------- indicator proposals ----------------------------------
    struck = sorted({an for e in kinetic for an in anchors_of(e)})
    choke = CHOKEPOINTS.get(a.zone, set())
    choke_hit = sorted(set(struck) & choke)
    closure_claims = [e for e in statements
                     if any(x in {"closure", "blockade"}
                            for x in anchors_of(e))]
    transit_claims = [e for e in statements
                      if any(x in {"strait of hormuz", "hormuz", "tanker",
                                   "shipping", "strait"}
                             for x in anchors_of(e))]

    inds = {}

    inds["trade"] = ind(None, "SPECULATIVE",
        ["UN Comtrade; national customs releases; sanctioned-trade tracking"],
        "A watched-channel pull cannot observe trade flows. Unscorable from "
        "this corpus; score only from external trade data.", [])

    if choke_hit:
        t_score, rung = 2, "interrupted episodically, restored quickly"
        t_rule = ("RULE: graded kinetic strike on a transit-bearing anchor "
                  f"({', '.join(choke_hit)}) with no graded closure event in "
                  "the window -> propose 2. Corpus absence of a closure event "
                  "is NOT world absence; verify against Lloyd's List / AIS "
                  "traffic before recording.")
    elif closure_claims or transit_claims:
        t_score, rung = 3, "continuous with brief symbolic pauses"
        t_rule = ("RULE: closure/transit claims circulate cross-side while no "
                  "graded kinetic event touches a transit anchor -> propose 3 "
                  "(threats circulate, passage unstruck in corpus). Verify "
                  "against Lloyd's List / AIS before recording.")
    else:
        t_score, rung, t_rule = None, "", None
    inds["transit"] = ind(t_score, "DERIVED" if t_score is not None else "SPECULATIVE",
        ["Lloyd's List; war-risk premia; AIS transit data (verify externally)"],
        (f"Proposed {t_score} — {rung}. " if t_score is not None else
         "No transit-bearing signal in this pull. ") +
        "Derived from corpus signals only.",
        [evline(e) for e in (closure_claims + transit_claims)] +
        [evline(e) for e in kinetic if set(anchors_of(e)) & choke],
        rule=t_rule)

    inds["deconfliction"] = ind(None, "SPECULATIVE",
        ["Official notification records; third-party mediation reporting"],
        "Hotlines, notification channels and advance warning are invisible to "
        "this corpus. Unscorable from the pull.", [])

    inds["target_selection"] = ind(None, "SPECULATIVE",
        ["Order-of-battle references; official target statements"],
        "The corpus supplies the STRUCK set only: "
        + (", ".join(struck) if struck else "no graded kinetic anchors")
        + ". Scoring requires the decisive-target reference list — what was "
        "available and NOT struck — which is a judgment against external "
        "knowledge, not a corpus fact. Evidence attached; score is yours.",
        [evline(e) for e in kinetic])

    sanc_claims = [e for e in statements
                   if "sanctions" in anchors_of(e)]
    inds["sanctions"] = ind(None, "SPECULATIVE",
        ["OFAC/EU/UN designations, licences and carve-out texts"],
        ("Sanctions claims circulate cross-side in this pull. " if sanc_claims
         else "No cross-side sanctions circulation in this pull. ") +
        "Carve-out and enforcement structure is only scorable from the "
        "regime documents themselves.",
        [evline(e) for e in sanc_claims])

    tanker_claims = [e for e in statements if "tanker" in anchors_of(e)]
    inds["civil_continuity"] = ind(None, "SPECULATIVE",
        ["Lloyd's war-risk premia; IATA/NOTAM records; correspondent-banking reporting"],
        "Insurance premia, aviation and banking continuity are invisible to "
        "this corpus. Tanker-related circulation attached as context only.",
        [evline(e) for e in tanker_claims])

    prereg_note = ""
    if a.prereg_id:
        ok = False
        lp = HERE / "ledger.json"
        if lp.exists():
            try:
                rows = read_json(lp).get("projections", [])
                row = next((r for r in rows if r.get("id") == a.prereg_id), None)
                if row is None:
                    prereg_note = (f"REJECTED: {a.prereg_id} not found in "
                                   "ledger.json — no pre-registration attaches.")
                elif window["from"] and str(row.get("date_issued", "9999")) > window["from"]:
                    prereg_note = (f"REJECTED: {a.prereg_id} issued "
                                   f"{row.get('date_issued')} — AFTER the window "
                                   f"opened {window['from']}. A threshold chosen "
                                   "after the events is not pre-registration.")
                else:
                    ok = True
                    prereg_note = (f"{a.prereg_id} · issued "
                                   f"{row.get('date_issued')} · "
                                   f"\"{str(row.get('statement',''))[:120]}\"")
            except Exception as ex:
                prereg_note = f"could not verify against ledger.json ({ex})"
        else:
            prereg_note = "ledger.json not found beside the script — unverified."
        preg = prereg_note if ok else ""
    else:
        preg = ""
        prereg_note = ("none supplied. Excluded by rule until a KKR projection "
                       "declares instrument, window and threshold BEFORE the "
                       "events. Pass --prereg-id to attach one.")
    inds["market_prepositioning"] = ind(None, "SPECULATIVE",
        ["Pre-registered KKR projection; options/futures data for the declared instrument"],
        "Pre-registration status: " + prereg_note, [])
    inds["market_prepositioning"]["preregistration"] = preg

    dyad_name = a.dyad_name or (f"{a.zone} {s1}-{s2} live, "
                                f"{datetime.now(timezone.utc).date().isoformat()}")
    outdoc = {
        "dyad": dyad_name,
        "_proposed_by": f"dialektik_feed.py from {src.name}",
        "_review_required": ("PROPOSAL ONLY. Recording without operator review "
                             "would be the instrument scoring itself. Correct "
                             "scores, replace SPECULATIVE grades where you "
                             "bring external sources, then: "
                             "python dialektik.py score --dyad <this file>"),
        "stated_posture": stated,
        "window": window,
        "indicators": inds,
        "_context_one_side_events": [evline(e) for e in context],
    }

    out = Path(a.out) if a.out else (
        HERE / f"dialektik_live_{a.zone}_{datetime.now(timezone.utc).date().isoformat()}.json")
    out.write_text(json.dumps(outdoc, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")

    proposed = [k for k, v in inds.items() if v["score"] is not None]
    print(f"FEED · {src.name} -> {out.name}")
    print(f"FEED · dyad {s1}-{s2} in {a.zone}: {len(kinetic)} kinetic + "
          f"{len(statements)} statement cross-side graded events "
          f"({len(context)} one-side context)")
    print(f"FEED · proposed scores: "
          + (", ".join(f"{k}={inds[k]['score']}" for k in proposed)
             if proposed else "none — evidence only"))
    print(f"FEED · unscored (corpus-blind): "
          + ", ".join(k for k in INDICATOR_KEYS if inds[k]["score"] is None))
    print("FEED · REVIEW REQUIRED before any score is used. Then:")
    print(f"         python dialektik.py score --dyad {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
