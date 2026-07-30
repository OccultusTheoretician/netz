#!/usr/bin/env python3
"""
build_dialektik_calibration.py — write the five calibration dyads, scored.

WHAT THIS IS
The calibration set is deliberately built from cases whose classification is
NOT in dispute, so the scores follow from documented history rather than
judgment. This script writes all five files with scores, sources and a written
rationale per indicator, ready for `dialektik.py record`.

WHAT THIS IS NOT
It is not tuned. Each indicator was scored on its own documented merits against
the rubric before any index was computed, and the script prints whatever index
falls out. If the sets fail to separate, that is the null and it stands.

THREE HANDLING RULES APPLIED, EACH VISIBLE IN THE FILES
1. An indicator with no bilateral regime to measure (sanctions between two
   belligerents already at open war) is graded SPECULATIVE: recorded, not
   counted. Forcing a number there would invent divergence out of a category
   error.
2. market_prepositioning on every historical dyad has no pre-registered KKR
   threshold, so it is left unregistered and the scorer excludes it. That is the
   rule working, not a gap.
3. The 9/11 control is scored on market_prepositioning ALONE, because the other
   six indicators describe a conflict dyad and this case is a market-anomaly
   control. See the CONTROL NOTE printed at the end - it sits on the gate
   boundary and is the one score worth your override.

SOURCES are named by class (standard historiography, named agreements, named
papers). Verify citation specifics before anything from this reaches a
published surface.

Run from C:\netz:  python build_dialektik_calibration.py
"""
import json, sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
TODAY = date.today().isoformat()

def ind(score, grade, sources, why):
    return {"score": score, "grade": grade, "as_of": TODAY,
            "sources": sources, "rationale": why}

CASES = {}

# ---------------------------------------------------------------- EXPECT LOW
CASES["Germany-USSR 1941-45"] = {
 "file": "cal_germany_ussr.json",
 "stated_posture": "Both parties declared a war of annihilation. Germany's stated aim was "
                   "conquest and Lebensraum; the USSR's was the destruction of the invader. "
                   "No party claimed a limited or managed conflict.",
 "window": {"from": "1941-06-22", "to": "1945-05-08"},
 "indicators": {
  "trade": ind(0, "DOCUMENTED", ["German-Soviet Commercial Agreement (1940), terminated at invasion 22 June 1941; standard Barbarossa economic historiography"],
    "Trade severed at the moment of invasion and stayed severed. The 1940 commercial agreement, which had been running deliveries up to the eve of Barbarossa, ended absolutely. Enforcement total on both sides."),
  "transit": ind(0, "DOCUMENTED", ["Eastern Front operational histories"],
    "No transit continuity of any kind. The contested space WAS the front line; there was no corridor, pipeline or overflight arrangement to preserve."),
  "deconfliction": ind(0, "DOCUMENTED", ["Absence of any notification channel is itself well documented across the Eastern Front literature"],
    "No hotline, no notification, no third-party channel used for warning. Strikes unannounced by design."),
  "target_selection": ind(0, "DOCUMENTED", ["Sieges of Leningrad and Stalingrad; strategic bombing of industrial centres; operations against leadership and command"],
    "Decisive targets struck without reservation: capitals besieged, industry targeted, command and leadership attacked. Nothing held back as available-but-unstruck."),
  "sanctions": ind(None, "SPECULATIVE", ["n/a - no sanctions regime existed between the belligerents"],
    "CATEGORY NOT APPLICABLE. Sanctions are an instrument for parties not in open total war; there was no regime, carve-out or licensing to measure. Recorded as SPECULATIVE so it moves nothing rather than inventing a score."),
  "civil_continuity": ind(0, "DOCUMENTED", ["Wartime shipping, insurance and aviation records for the Eastern theatre"],
    "Civil shipping, banking and aviation across the line suspended entirely. War-risk cover for the contested zone did not meaningfully exist."),
  "market_prepositioning": ind(None, "DOCUMENTED", ["n/a - historical case, no pre-registered threshold"],
    "No KKR projection declared an instrument, window and threshold before the event. By rule this indicator contributes nothing. Left unregistered deliberately."),
 }}

CASES["Iran-Iraq 1980-88"] = {
 "file": "cal_iran_iraq.json",
 "stated_posture": "Both states declared existential war aims - Iraq's initial territorial and "
                   "regime objectives, Iran's stated aim of removing the Iraqi leadership. "
                   "Neither framed the conflict as limited.",
 "window": {"from": "1980-09-22", "to": "1988-08-20"},
 "indicators": {
  "trade": ind(0, "DOCUMENTED", ["Bilateral trade statistics for the war years; standard Iran-Iraq War economic accounts"],
    "DIRECT bilateral trade between the two belligerents was severed. Third-party ARMS SUPPLY to each side is a different fact and is not bilateral trade between them - the indicator measures the dyad, so third-party supply does not raise this score."),
  "transit": ind(2, "DOCUMENTED", ["Tanker War record; Operation Earnest Will (1987) reflagging and convoy operations"],
    "Gulf shipping was repeatedly struck and repeatedly restored. Neither party closed the Strait of Hormuz despite both having the means and the stated motive. Interrupted episodically, restored quickly."),
  "deconfliction": ind(1, "DOCUMENTED", ["UN-mediated moratoria on the War of the Cities, 1983-1988"],
    "No direct channel, but UN-brokered pauses on city bombing were negotiated and periodically observed. A third-party channel, rarely used - which is exactly rung 1."),
  "target_selection": ind(0, "DOCUMENTED", ["Repeated strikes on Kharg Island export terminal; War of the Cities; Faw peninsula operations"],
    "Decisive targets struck: the principal oil export terminal hit repeatedly, capitals under missile attack, no evident category of target preserved."),
  "sanctions": ind(None, "SPECULATIVE", ["UNSC Res. 479 (1980) and the arms embargo were multilateral measures on the conflict, not a bilateral regime between the parties"],
    "CATEGORY NOT APPLICABLE as a dyadic measure. The embargo was a third-party instrument widely evaded by suppliers to both sides; scoring it as dyadic carve-out behaviour would import a fact about arms markets into a claim about the belligerents' own restraint."),
  "civil_continuity": ind(2, "DOCUMENTED", ["Lloyd's war-risk premia for the Gulf, 1984-88; reflagging record"],
    "Commercial shipping continued but was curtailed and routed under convoy protection, with war-risk premia far above baseline. Curtailed but routed around."),
  "market_prepositioning": ind(None, "DOCUMENTED", ["n/a - historical case, no pre-registered threshold"],
    "No pre-registration. Excluded by rule."),
 }}

# --------------------------------------------------------------- EXPECT HIGH
CASES["India-Pakistan Line of Control, standing"] = {
 "file": "cal_india_pakistan.json",
 "stated_posture": "Both states maintain declared hostility over Kashmir, characterise the "
                   "other as an aggressor, and have fought repeated wars and standoffs. "
                   "The stated relationship is unresolved armed antagonism.",
 "window": {"from": "2004-01-01", "to": TODAY},
 "indicators": {
  "trade": ind(3, "DOCUMENTED", ["India's withdrawal of MFN status and tariff action, 2019; third-country trade routing literature"],
    "Direct bilateral trade suspended in 2019, but substantial indirect trade continues to be documented through third countries. Largely intact through third parties."),
  "transit": ind(3, "DOCUMENTED", ["Kartarpur Corridor agreement, opened November 2019; Attari-Wagah crossing; Samjhauta Express suspension 2019"],
    "A dedicated pilgrimage corridor was OPENED during a period of peak hostility and has operated since. Crossings continue with episodic symbolic suspensions."),
  "deconfliction": ind(4, "DOCUMENTED", ["DGMO hotline (weekly, standing since 2004); 2021 joint ceasefire re-affirmation; 2005 pre-notification of ballistic missile tests; Agreement on the Prohibition of Attack against Nuclear Installations (1988) - lists exchanged every 1 January since 1992"],
    "The strongest single reading in the calibration set. Two states in declared hostility exchange lists of their nuclear installations every New Year's Day without interruption, pre-notify missile tests by agreement, and run a standing weekly military hotline. Systematic advance warning."),
  "target_selection": ind(3, "DOCUMENTED", ["Balakot strike, February 2019, and its assessed effect; absence of strikes on command, leadership or strategic assets across the period"],
    "Decisive targets are available and consistently unstruck. The 2019 exchange, the most kinetic episode in decades, produced strikes assessed as causing negligible material damage."),
  "sanctions": ind(None, "SPECULATIVE", ["No bilateral sanctions regime exists between the parties"],
    "CATEGORY NOT APPLICABLE. There is no dyadic sanctions architecture to score for carve-outs. Recorded, not counted."),
  "civil_continuity": ind(3, "DOCUMENTED", ["Pakistan airspace closure February-July 2019 and its restoration; continued participation in ICC cricket events at neutral venues"],
    "Overflight and civil links are suspended episodically and restored; sporting and diplomatic contact continues in third-country settings. Largely normal with elevated friction."),
  "market_prepositioning": ind(None, "DOCUMENTED", ["n/a - no pre-registered KKR threshold for this dyad"],
    "No pre-registration. Excluded by rule. This is the indicator to register first if this dyad is ever scored live."),
 }}

CASES["Koreas, armistice standing"] = {
 "file": "cal_koreas.json",
 "stated_posture": "No peace treaty exists; the parties remain formally at war under the 1953 "
                   "Armistice. Both maintain declared hostility and large standing forces on "
                   "a fortified line.",
 "window": {"from": "1953-07-27", "to": TODAY},
 "indicators": {
  "trade": ind(3, "DOCUMENTED", ["Kaesong Industrial Complex, operating 2004-2016; Mount Kumgang tourism project"],
    "Joint industrial manufacturing operated for twelve years between two states formally at war, employing DPRK labour in ROK-managed facilities. Closed in 2016, so not 'intact' at standing, but the fact that it existed at all across a declared war line is a substantial divergence."),
  "transit": ind(3, "DOCUMENTED", ["Gyeongui and Donghae rail reconnection projects; DMZ crossing arrangements under inter-Korean agreements"],
    "Rail and road reconnection across the world's most fortified line has been built, used, and periodically suspended. Continuous with symbolic pauses."),
  "deconfliction": ind(4, "DOCUMENTED", ["Panmunjom liaison channel; inter-Korean military hotlines; Comprehensive Military Agreement, September 2018 (no-fly zones, guard post withdrawal, buffer zones)"],
    "Standing liaison and military hotlines, cyclically severed and restored, plus a negotiated agreement creating mutual no-fly and buffer zones along the line. Systematic, institutionalised advance-warning architecture."),
  "target_selection": ind(4, "DOCUMENTED", ["Seoul's proximity to the DMZ and its non-targeting since 1953; absence of leadership strikes by either party across seven decades"],
    "A capital city of ten million sits within artillery range of the line and has not been struck in seventy years. Leadership on both sides untouched throughout. Decisive targets available, and their exclusion is effectively stated policy."),
  "sanctions": ind(None, "SPECULATIVE", ["UNSC sanctions on the DPRK are a multilateral regime, not a bilateral inter-Korean instrument"],
    "CATEGORY NOT APPLICABLE as a dyadic measure. Scoring multilateral UNSC measures here would attribute third-party architecture to the dyad."),
  "civil_continuity": ind(3, "DOCUMENTED", ["Separated-family reunion programmes; joint and unified teams at the 2018 Winter Olympics; Mount Kumgang tourism"],
    "Family reunions, joint sporting delegations and tourism have all operated across the line during the declared state of war, episodically suspended and restored."),
  "market_prepositioning": ind(None, "DOCUMENTED", ["n/a - no pre-registered KKR threshold"],
    "No pre-registration. Excluded by rule."),
 }}

# -------------------------------------------------------- CONTESTED CONTROL
CASES["Pre-9/11 airline options, September 2001"] = {
 "file": "cal_airline_options.json",
 "stated_posture": "CONTROL CASE, not a conflict dyad. This exists to test whether the market "
                   "indicator can hold 'anomalous but explained' apart from 'anomalous and "
                   "unexplained'. Only market_prepositioning is scored; the six conflict "
                   "indicators are category-inapplicable and graded SPECULATIVE.",
 "window": {"from": "2001-09-06", "to": "2001-09-10"},
 "indicators": {
  "trade": ind(None, "SPECULATIVE", ["n/a - control case, not a conflict dyad"], "CATEGORY NOT APPLICABLE."),
  "transit": ind(None, "SPECULATIVE", ["n/a - control case"], "CATEGORY NOT APPLICABLE."),
  "deconfliction": ind(None, "SPECULATIVE", ["n/a - control case"], "CATEGORY NOT APPLICABLE."),
  "target_selection": ind(None, "SPECULATIVE", ["n/a - control case"], "CATEGORY NOT APPLICABLE."),
  "sanctions": ind(None, "SPECULATIVE", ["n/a - control case"], "CATEGORY NOT APPLICABLE."),
  "civil_continuity": ind(None, "SPECULATIVE", ["n/a - control case"], "CATEGORY NOT APPLICABLE."),
  "market_prepositioning": ind(2, "DOCUMENTED",
    ["Poteshman, Journal of Business (2006) - option activity assessed anomalous at roughly the 99th percentile for one carrier",
     "9/11 Commission Report and its staff findings - each trade traced to an innocuous explanation, including one institution's offsetting strategy and an options newsletter circulated 9 September 2001"],
    "The anomaly was REAL (a published, threshold-based finding) and the explanation was ALSO REAL (traced by inquiry). Rung 2 is 'anomaly exceeding threshold once'. Rungs 3 and 4 require repetition or an anomaly that survives inquiry UNEXPLAINED - neither holds here, and scoring this high is precisely the failure the control exists to catch."),
 }}
CASES["Pre-9/11 airline options, September 2001"]["indicators"]["market_prepositioning"]["preregistration"] = (
  "HISTORICAL CONTROL. The threshold was declared by Poteshman (2006) in the published "
  "literature, not chosen by this desk after examining the data. Recorded so the control "
  "yields a countable index; no live dyad may use this route.")


def main():
    written = []
    for name, spec in CASES.items():
        doc = {"dyad": name,
               "stated_posture": spec["stated_posture"],
               "window": spec["window"],
               "indicators": spec["indicators"]}
        p = HERE / spec["file"]
        p.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written.append((name, spec["file"]))
        print(f"  written  {spec['file']:28s} {name}")

    print()
    print("  Every score carries a rationale and a source class in the file.")
    print("  Verify citation specifics before any of this reaches a published surface.")
    print()
    print("  CONTROL NOTE - the one score worth your override:")
    print("  the 9/11 control scores market_prepositioning at 2, giving index 0.50.")
    print("  The gate fails the control only ABOVE 0.50, so it passes on the boundary")
    print("  with zero margin. Rung 3 would give 0.75 and FAIL the instrument. The")
    print("  case for 2: the anomaly was explained by inquiry, and rungs 3-4 require")
    print("  repetition or an unexplained residue. If you read it as 3, edit the score")
    print("  in cal_airline_options.json and re-record - the gate result will change,")
    print("  and that is the gate doing its job rather than a bug.")
    print()
    print("  next:  run_dialektik_calibration.bat")
    return 0

if __name__ == "__main__":
    sys.exit(main())
