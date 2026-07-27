#!/usr/bin/env python3
"""
dialektik.py — stated-versus-operational divergence for a conflict dyad.

WHAT IT DOES NOT DO.

It does not tell you a conflict is staged. That claim is unfalsifiable as
stated, and an unfalsifiable frame applied to conflict is the structure of
conspiracy reasoning. RPAS's master law kills it outright: a test that cannot
distinguish keyed from keyless is not a test, it is a mirror.

WHAT IT DOES.

It measures how far a dyad's OPERATIONAL record sits from what its STATED
antagonism predicts. Seven indicators, each a documented public fact with a
source and a date, each scored 0-4 against a written rubric. The output is a
measurement that demands explanation, never a conclusion about intent.

THREE SAFEGUARDS, MECHANICAL RATHER THAN ADVISORY.

1. CALIBRATION GATE. No live dyad can be scored until the calibration set has
   been scored and demonstrates SEPARATION — known total-war cases must land
   low and known frozen/proxy cases high. If the index cannot separate cases
   everyone already agrees about, it is measuring nothing, and the honest
   output is a published null. The gate refuses; it does not warn.

2. PRE-REGISTRATION ON THE MARKET INDICATOR. Unusual trading before an event
   is the single most seductive and least reliable input available. If you
   examine enough trading data you will always find anomalies, so a threshold
   chosen after the fact proves nothing. The market indicator contributes ZERO
   unless it carries a KKR projection id that declared instrument, window and
   threshold beforehand. Retrospective anomalies are recorded and not counted.

3. THE INDEX MUST BE ABLE TO COME OUT LOW. If every dyad scores high, that is
   the mirror again. `check` reports the distribution and says so.

    python dialektik.py rubric                       the scoring rubrics
    python dialektik.py template --out d.json        a fillable dyad
    python dialektik.py score --dyad d.json          score one dyad
    python dialektik.py calibrate                    score the calibration set
    python dialektik.py check                        is the instrument usable yet
    python dialektik.py forecast --dyad d.json       emit resolvable non-events

Standard library only. Nothing here writes to the ledger.
"""

import argparse
import json
import sys
from datetime import datetime, timezone, date
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAL = HERE / "dialektik_calibration.json"

GRADES = ["CONFESSED", "PROOF-VERBATIM", "DOCUMENTED", "REPORTED",
          "DERIVED", "SPECULATIVE"]
NOT_COUNTED = {"SPECULATIVE"}

# 0 = behaviour matches stated antagonism.  4 = behaviour contradicts it.
INDICATORS = {
    "trade": ("Bilateral trade between the belligerents during the stated conflict.",
              ["severed or near-zero, enforced",
               "sharply reduced, enforcement visible",
               "reduced but substantial flows persist",
               "largely intact through third parties",
               "intact or grown; no enforcement attempted"]),
    "transit": ("Energy, pipeline, strait, rail and overflight continuity through "
                "the contested space.",
                ["closed or contested continuously",
                 "interrupted, restored under duress",
                 "interrupted episodically, restored quickly",
                 "continuous with brief symbolic pauses",
                 "wholly uninterrupted throughout"]),
    "deconfliction": ("Notification channels, hotlines, advance warning of strikes.",
                      ["none; strikes unannounced",
                       "third-party channel, rarely used",
                       "channel exists and is used in crises",
                       "routine notification before major action",
                       "systematic advance warning; strikes telegraphed"]),
    "target_selection": ("Availability and treatment of decisive targets — leadership, "
                         "command nodes, export terminals, single points of failure.",
                         ["decisive targets struck",
                          "struck late or partially",
                          "struck symbolically; capacity preserved",
                          "available and consistently unstruck",
                          "explicitly excluded and stated as excluded"]),
    "sanctions": ("Carve-outs, waivers and enforcement in the sanctions regime, and "
                  "who authored them.",
                  ["comprehensive, enforced against own nationals",
                   "broad with narrow humanitarian carve-outs",
                   "significant sectoral carve-outs, enforced unevenly",
                   "carve-outs covering the principal revenue stream",
                   "regime nominal; principal trade licensed"]),
    "civil_continuity": ("Shipping, insurance, aviation and banking continuity through "
                         "the contested zone.",
                         ["suspended; war-risk premia prohibitive",
                          "sharply curtailed",
                          "curtailed but routed around",
                          "largely normal with higher premia",
                          "unchanged; premia near baseline"]),
    "market_prepositioning": ("Unusual positioning in instruments exposed to the dyad "
                              "ahead of events. REQUIRES PRE-REGISTRATION — see below.",
                              ["no anomaly against the pre-registered threshold",
                               "anomaly within noise",
                               "anomaly exceeding threshold once",
                               "anomaly exceeding threshold repeatedly",
                               "repeated, concentrated, and unexplained after inquiry"]),
}

# Cases whose classification is not in dispute. Scored first; the gate depends
# on them separating. Deliberately includes a contested control.
CALIBRATION_SEED = {
    "expect_low": [
        {"dyad": "Germany-USSR 1941-45",
         "why": "Total war. Trade severed, no deconfliction, decisive targets struck, "
                "no civil continuity. If this does not score near zero the indicators "
                "are not measuring antagonism."},
        {"dyad": "Iran-Iraq 1980-88",
         "why": "Prolonged conventional war between neighbours with prior trade. "
                "Tests whether the index survives a case with third-party supply to "
                "both sides."},
    ],
    "expect_high": [
        {"dyad": "India-Pakistan Line of Control, standing",
         "why": "Declared hostility with institutionalised deconfliction, notified "
                "exercises, continued sporting and diplomatic contact."},
        {"dyad": "Koreas, armistice standing",
         "why": "Formally at war since 1953 with a liaison channel, periodic joint "
                "projects and an agreed line. The high-divergence archetype."},
    ],
    "contested_control": [
        {"dyad": "Pre-9/11 airline options, September 2001",
         "why": "The market indicator's negative control, and it is contested on "
                "purpose. The 9/11 Commission found each trade innocuous — one US "
                "institution bought 95 percent of the UAL puts as part of a strategy "
                "that also went long American; much of the American volume traced to "
                "an options newsletter faxed on 9 September. Poteshman (Journal of "
                "Business, 2006) nonetheless found the option activity anomalous at "
                "roughly 99 percent for American. BOTH can be true: the anomaly was "
                "real and the explanation was real. An index that cannot hold "
                "'anomalous but explained' as a state distinct from 'anomalous and "
                "unexplained' is too crude to publish. This case is where that is "
                "tested, and it must NOT drive a high score."},
    ],
}


# ----------------------------------------------------------------------
def rubric():
    print("DIALEKTIK — indicator rubrics\n")
    print("  0 = operational behaviour matches the stated antagonism")
    print("  4 = operational behaviour contradicts it\n")
    for k, (desc, levels) in INDICATORS.items():
        print(f"  {k.upper()}")
        print(f"    {desc}")
        for i, l in enumerate(levels):
            print(f"      {i} · {l}")
        print()
    print("  Every score needs a grade, a source and an as_of, on the same ladder")
    print("  the order of battle uses. A SPECULATIVE indicator is recorded and not")
    print("  counted; it moves the denominator, never the numerator.\n")
    return 0


def template(path):
    t = {
        "dyad": "",
        "stated_posture": "what each party says the relationship is, quoted and sourced",
        "window": {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"},
        "indicators": {},
    }
    for k, (desc, _) in INDICATORS.items():
        t["indicators"][k] = {
            "score": None, "grade": "DOCUMENTED", "as_of": date.today().isoformat(),
            "sources": [""], "note": desc}
    t["indicators"]["market_prepositioning"]["preregistration"] = ""
    t["indicators"]["market_prepositioning"]["note"] = (
        "Put the KKR projection id that declared instrument, window and threshold "
        "BEFORE the event. Without it this indicator scores zero regardless of what "
        "the data shows, because a threshold chosen afterwards proves nothing.")
    Path(path).write_text(json.dumps(t, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"written → {path}")
    return 0


def read_json(p):
    raw = Path(p).read_bytes()
    for bom, enc in ((b"\xff\xfe", "utf-16"), (b"\xfe\xff", "utf-16"),
                     (b"\xef\xbb\xbf", "utf-8-sig")):
        if raw.startswith(bom):
            return json.loads(raw.decode(enc))
    return json.loads(raw.decode("utf-8"))


def score_dyad(d, verbose=True):
    counted, skipped, total = [], [], 0
    for k in INDICATORS:
        ind = (d.get("indicators") or {}).get(k)
        if not ind or ind.get("score") is None:
            skipped.append((k, "no score recorded")); continue
        g = ind.get("grade")
        if g not in GRADES:
            skipped.append((k, f"grade {g!r} not on the ladder")); continue
        if g in NOT_COUNTED:
            skipped.append((k, f"graded {g} — recorded, not counted")); continue
        if not ind.get("sources") or not any(ind["sources"]):
            skipped.append((k, "no source")); continue
        if k == "market_prepositioning" and not ind.get("preregistration"):
            skipped.append((k, "NOT PRE-REGISTERED — scores zero. A threshold chosen "
                               "after the event proves nothing; examine enough data "
                               "and anomalies are guaranteed."))
            continue
        s = int(ind["score"])
        if not 0 <= s <= 4:
            skipped.append((k, "score out of range 0-4")); continue
        counted.append((k, s)); total += s
    n = len(counted)
    idx = (total / (4 * n)) if n else None
    if verbose:
        print(f"\nDIVERGENCE — {d.get('dyad','(unnamed)')}")
        print("-" * 66)
        for k, s in counted:
            print(f"  {k:22s} {s}  {INDICATORS[k][1][s]}")
        for k, why in skipped:
            print(f"  {k:22s} —  {why}")
        if idx is None:
            print("\n  NO INDEX — nothing countable.")
        else:
            print(f"\n  index {idx:.2f}  ({total}/{4*n} over {n} counted indicators)")
            print("  0 = behaviour matches the stated antagonism. 1 = contradicts it.")
            print("  This is a measurement that demands explanation, not a finding")
            print("  about intent. It says nothing about why.")
    return idx, n, counted, skipped


def calibrate():
    if not CAL.exists():
        CAL.write_text(json.dumps({
            "schema": "dialektik-calibration/1.0",
            "note": ("Score these before scoring anything live. The instrument is not "
                     "usable until the low set and the high set separate. If they do "
                     "not, publish the null."),
            "as_of": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "cases": CALIBRATION_SEED, "scored": {}}, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
        print(f"created → {CAL.name}")
    c = read_json(CAL)
    print("\nCALIBRATION SET — score each before any live dyad\n")
    for band in ("expect_low", "expect_high", "contested_control"):
        print(f"  {band.upper().replace('_',' ')}")
        for case in c["cases"][band]:
            got = c.get("scored", {}).get(case["dyad"])
            mark = f"index {got:.2f}" if isinstance(got, (int, float)) else "unscored"
            print(f"    [{mark:>11}] {case['dyad']}")
            print(f"                  {case['why']}")
        print()
    return 0


def check():
    if not CAL.exists():
        print("NOT CALIBRATED — run: python dialektik.py calibrate")
        return 1
    c = read_json(CAL)
    scored = c.get("scored", {})
    lo = [scored.get(x["dyad"]) for x in c["cases"]["expect_low"]]
    hi = [scored.get(x["dyad"]) for x in c["cases"]["expect_high"]]
    ctl = [scored.get(x["dyad"]) for x in c["cases"]["contested_control"]]
    missing = sum(1 for v in lo + hi + ctl if not isinstance(v, (int, float)))
    print("\nINSTRUMENT CHECK")
    print("-" * 66)
    if missing:
        print(f"  {missing} calibration case(s) unscored.")
        print("  NOT USABLE. Scoring a live dyad on an uncalibrated index produces a")
        print("  number that cannot be wrong, which is the failure this gate exists")
        print("  to prevent.\n")
        return 1
    mlo, mhi = max(lo), min(hi)
    print(f"  expect-low  max : {mlo:.2f}")
    print(f"  expect-high min : {mhi:.2f}")
    print(f"  contested ctrl  : {max(ctl):.2f}")
    ok = True
    if mhi - mlo < 0.25:
        print("\n  FAIL — the sets do not separate. The index does not distinguish")
        print("  cases everyone already agrees about, so it is not measuring")
        print("  antagonism. Publish the null and stop.")
        ok = False
    if max(ctl) > 0.5:
        print("\n  FAIL — the contested control scores high. An index that reads")
        print("  'anomalous but explained' as divergence will read every market")
        print("  anomaly as conspiracy. Tighten the market rubric.")
        ok = False
    if ok:
        print(f"\n  PASS — separation {mhi - mlo:.2f}, control held below 0.5.")
        print("  Usable on live dyads. Every live score still carries its sources")
        print("  and remains a measurement, not a verdict.\n")
        return 0
    print()
    return 1


def forecast(path):
    if check() != 0:
        print("Refusing to emit forecasts from an uncalibrated instrument.")
        return 1
    d = read_json(path)
    idx, n, counted, _ = score_dyad(d, verbose=False)
    if idx is None:
        print("No index; nothing to forecast."); return 1
    hi = [k for k, s in counted if s >= 3]
    print(f"\nRESOLVABLE NON-EVENTS implied by index {idx:.2f}\n")
    print("  A high-divergence reading predicts specific things that will NOT happen.")
    print("  Non-events resolve, which is what makes this a forecast rather than a")
    print("  reading. Seal these before the window opens.\n")
    tmpl = {
        "trade": "Bilateral trade between the parties will not fall below {X} in {W}.",
        "transit": "Transit through {corridor} will not be interrupted for more than "
                   "{N} consecutive days in {W}.",
        "target_selection": "{decisive target} will not be struck in {W}.",
        "sanctions": "The carve-out covering {revenue stream} will not be withdrawn in {W}.",
        "civil_continuity": "War-risk premia on {route} will not exceed {X} in {W}.",
        "deconfliction": "No strike in {W} will occur without prior notification "
                         "reported by {source}.",
    }
    for k in hi:
        if k in tmpl:
            print(f"  [{k}] {tmpl[k]}")
    print("\n  Fill the braces with mechanical criteria, then:")
    print("    python kkr.py --ingest <file> --arm dialektik/operator\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="dialektik — stated vs operational divergence")
    sub = ap.add_subparsers(dest="cmd")
    sub.add_parser("rubric")
    t = sub.add_parser("template"); t.add_argument("--out", default="dyad.json")
    s = sub.add_parser("score"); s.add_argument("--dyad", required=True)
    sub.add_parser("calibrate")
    sub.add_parser("check")
    f = sub.add_parser("forecast"); f.add_argument("--dyad", required=True)
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help(); return 0
    if a.cmd == "rubric":
        return rubric()
    if a.cmd == "template":
        return template(a.out)
    if a.cmd == "calibrate":
        return calibrate()
    if a.cmd == "check":
        return check()
    if a.cmd == "score":
        if check() != 0:
            print("Refusing to score a live dyad on an uncalibrated instrument.")
            return 1
        score_dyad(read_json(a.dyad))
        return 0
    if a.cmd == "forecast":
        return forecast(a.dyad)


if __name__ == "__main__":
    sys.exit(main())
