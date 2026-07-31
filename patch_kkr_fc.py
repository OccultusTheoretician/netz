#!/usr/bin/env python3
"""
patch_kkr_fc.py - repair the 29 unsealed KKR-20260730 rows (RPAS 4.02f).
Run from C:\\netz. Python 3.10+.

WHAT THIS DOES
The 29 entries issued 2026-07-30 lack the failure_condition that RPAS 4.03
requires for a seal, and the keyed/keyless determination that 4.02f requires
before resolution. This script carries a PROPOSED set of all three fields per
row. Default mode prints them for review. --apply merges them into open,
still-empty entries only and saves through kkr.save_ledger - the 4.02g choke
point then seals each entry automatically. Never overwrites a non-empty field.
kkr.py stays the only writer of record: this script only hands it data.

  python patch_kkr_fc.py            # review the proposals
  python patch_kkr_fc.py --apply    # merge + save + render; seals happen at save

keyed/keyless rule applied: KEYLESS where resolution is mechanical against a
single named public instrument (exchange settlement, FOMC statement, Senate
roll call, a named .gov page). KEYED where the operator searches, reads, or
judges characterization ("tied to", "in connection with", multi-outlet
confirmation). 7 keyless, 22 keyed.
"""
import argparse
import sys
from pathlib import Path

P = {
 "KKR-20260730-01": {
  "failure_condition": "No closure or halt of commercial Strait of Hormuz transits lasting 24 or more consecutive hours, dated 2026-07-31 through 2026-09-30, is reported by at least two of Reuters, AP and Lloyds List as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator searches three archives and judges whether reported disruption meets the 24-hour closure characterization."},
 "KKR-20260730-02": {
  "failure_condition": "No Article 5 invocation tied to the 2026-07-30 Poland missile impact appears on nato.int or two major wires, dated in the window, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "The tie between an invocation and this specific incident is an operator attribution judgment."},
 "KKR-20260730-03": {
  "failure_condition": "The September 2026 FOMC statement at federalreserve.gov announces a target range equal to or higher than the prior meeting's, or no September statement exists by 2026-09-30; either reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Single named instrument; mechanical comparison of two published target ranges."},
 "KKR-20260730-04": {
  "failure_condition": "Fewer than two of Bloomberg, CNBC, FT and Reuters report an announced wind-down, closure or return of external capital for Situational Awareness LP dated in the window, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Multi-outlet search plus operator characterization of what counts as a wind-down announcement."},
 "KKR-20260730-05": {
  "failure_condition": "No Emergency Directive naming CVE-2026-20316 appears on the cisa.gov directives page with an issue date between 2026-07-30 and 2026-08-21, as read on 2026-08-21; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Single named page; presence of a named CVE string in an ED issued in-window is mechanical."},
 "KKR-20260730-06": {
  "failure_condition": "No named military operation in Khyber Pakhtunkhwa or the former tribal districts is announced by ISPR or the Pakistani government in the window, per ispr.gov.pk or two major wires, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator judges what constitutes a new named operation in the specified areas across sources."},
 "KKR-20260730-07": {
  "failure_condition": "Fewer than two of AP, Reuters, BBC and Al Jazeera report a federal sentence imposed on Hadi Matar dated 2026-07-31 through 2027-01-26, as read on 2027-01-26; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Two-wire confirmation requires operator search and reading of sentencing coverage."},
 "KKR-20260730-08": {
  "failure_condition": "No official Cameroonian government announcement of President Biya's death or resignation, carried by at least two major international wires and dated in the window, exists as read on 2027-01-26; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator reads whether an announcement is official and government-sourced across wires."},
 "KKR-20260730-09": {
  "failure_condition": "Fewer than two of BBC, Al Jazeera, Reuters and AP report Kizza Besigye released from detention (including house arrest or medical release abroad) dated in the window, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Release-status characterization across outlets is an operator reading."},
 "KKR-20260730-10": {
  "failure_condition": "Fewer than two of BBC, Guardian, DW and Reuters report a confirmed firefighter death toll of five or more attributed to the 2026 Crete wildfires, dated in the window, as read on 2026-08-31; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Numeric threshold but resolved by reading attribution in multi-outlet casualty reporting."},
 "KKR-20260730-11": {
  "failure_condition": "No official US military or DoD statement confirming a new strike inside Iranian territory occurring 2026-08-06 through 2026-09-30 is carried by two or more major outlets, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator confirms official sourcing and two-outlet carriage of a qualifying strike."},
 "KKR-20260730-12": {
  "failure_condition": "No ICE front-month Brent settlement exceeds 100.00 USD on any session 2026-08-06 through 2026-10-30, per exchange or major financial press settlement data as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Named exchange settlement series against a fixed numeric threshold; mechanical."},
 "KKR-20260730-13": {
  "failure_condition": "No formal Article 4 consultation requested by a member state and held 2026-08-06 through 2026-09-30 is publicly confirmed by NATO or a member government, as read on 2026-09-30 - routine North Atlantic Council statements not qualifying; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "The criterion's own routine-statement exclusion is an operator judgment key."},
 "KKR-20260730-14": {
  "failure_condition": "The official Nasdaq Composite close is 22,485 or higher on every session 2026-08-06 through 2026-11-30, per exchange or major financial press data as read on 2026-11-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Named index official close against a fixed numeric threshold; mechanical."},
 "KKR-20260730-15": {
  "failure_condition": "No report from Cisco Talos, CISA, or a major security vendor published 2026-08-06 through 2026-10-30 names a specific state actor or tracked group exploiting CVE-2026-20316, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator judges whether attribution names a specific tracked actor versus generic activity."},
 "KKR-20260730-16": {
  "failure_condition": "No public confirmation by Lloyds List, the IMO, or the US Navy of zero commercial Strait of Hormuz transits across 72 consecutive hours falling 2026-08-06 through 2026-11-30 exists as read on 2026-11-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator reads whether a named authority's statement amounts to confirmation of a 72-hour total halt."},
 "KKR-20260730-17": {
  "failure_condition": "No FOMC statement issued 2026-08-06 through 2026-10-30 announces a lower federal funds target range, as read at federalreserve.gov on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Single named instrument; mechanical comparison of announced target ranges."},
 "KKR-20260730-18": {
  "failure_condition": "The Senate record shows no successful confirmation vote seating Todd Blanche as Attorney General between 2026-08-06 and 2026-10-30, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Senate roll-call record is a single mechanical public instrument."},
 "KKR-20260730-19": {
  "failure_condition": "Japanese government or major wire reporting dated 2026-08-06 through 2026-08-31 states no confirmed death toll of 50 or more from the magnitude 6.8 Uto earthquake, as read on 2026-08-31; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Toll confirmation and attribution read from official and wire reporting."},
 "KKR-20260730-20": {
  "failure_condition": "No single attack in Pakistan killing 10 or more police or military personnel between 2026-08-06 and 2026-10-30 is confirmed by credible international reporting, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Single-attack scoping and credibility of reporting are operator judgments."},
 "KKR-20260730-21": {
  "failure_condition": "No new U.S. strike on Iranian soil between 2026-07-30 and 2026-08-13 is reported by U.S. Central Command, the Pentagon, or a major wire service (Reuters, AP, BBC, Al Jazeera), as read on 2026-08-13; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator reads official and wire coverage for a qualifying new strike."},
 "KKR-20260730-22": {
  "failure_condition": "No report by NATO, a NATO member government, Reuters, or AP that Article 4 consultations were formally requested or held over the reported Russian missile breach of Polish airspace, dated 2026-07-30 through 2026-08-20, exists as read on 2026-08-20; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Incident-specific linkage of consultations to this breach is an operator judgment."},
 "KKR-20260730-23": {
  "failure_condition": "No new strike on a commercial or military vessel in the Persian Gulf, Red Sea, Strait of Hormuz, or eastern Mediterranean tied to the Iran conflict is reported by Reuters, AP, or Lloyds List dated 2026-07-30 through 2026-08-27, as read on 2026-08-27; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "The connection-to-conflict qualifier is an explicit operator attribution key."},
 "KKR-20260730-24": {
  "failure_condition": "No report by Japanese government authorities, NHK, or a major wire service dated 2026-07-30 through 2026-08-14 states a confirmed death toll above 40 for the magnitude 6.8 Uto earthquake, as read on 2026-08-14; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Toll confirmation read from official and wire reporting."},
 "KKR-20260730-25": {
  "failure_condition": "No confirmation by CISA, a federal agency, or a major outlet (Reuters, The Hacker News, BleepingComputer) of a specific U.S. federal agency or critical-infrastructure victim compromised through CVE-2026-20316, dated 2026-07-30 through 2026-09-15, exists as read on 2026-09-15; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Victim-specificity and compromise attribution are operator readings of disclosure language."},
 "KKR-20260730-26": {
  "failure_condition": "Meta Platforms common stock records no daily close below its 2026-07-30 close on any trading day 2026-07-31 through 2026-08-06, per official exchange closing data as read on 2026-08-06; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Official closing-price series against a fixed reference close; mechanical."},
 "KKR-20260730-27": {
  "failure_condition": "No Senate floor vote confirming Todd Blanche as Attorney General between 2026-07-30 and 2026-09-30 is reported by a major outlet, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Resolution basis names outlet reporting rather than the Senate record; operator reads coverage."},
 "KKR-20260730-28": {
  "failure_condition": "No public claim of responsibility for the northwest Pakistan police-post attack that killed 11 officers, issued by a militant group and reported by a major outlet dated 2026-07-30 through 2026-08-13, exists as read on 2026-08-13; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Claim authenticity and incident linkage are operator readings of coverage."},
 "KKR-20260730-29": {
  "failure_condition": "No report by Greek civil protection authorities or a major wire service dated 2026-07-30 through 2026-08-20 states more than 5 confirmed deaths from the current Crete wildfire event, as read on 2026-08-20; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Event scoping and toll confirmation read from official and wire reporting."},
}


def review():
    print(f"PROPOSED repairs for {len(P)} entries (RPAS 4.02f - nothing written)")
    print("-" * 64)
    for k in sorted(P):
        v = P[k]
        print(f"\n{k}  [{v['keyed_keyless'].upper()}]")
        print(f"  FC: {v['failure_condition']}")
        print(f"  KK: {v['keyed_keyless_rationale']}")
    print("\nApply with: python patch_kkr_fc.py --apply")


def apply():
    if not Path("kkr.py").exists():
        sys.exit("run from C:\\netz - kkr.py not found here")
    sys.path.insert(0, ".")
    import kkr
    data = kkr.load_ledger()
    merged, skipped = 0, []
    for e in data["projections"]:
        pid = e.get("id")
        if pid in P:
            if str(e.get("failure_condition", "")).strip():
                skipped.append(pid)
                continue
            if e.get("status") != "open":
                skipped.append(pid + " (not open)")
                continue
            e["failure_condition"] = P[pid]["failure_condition"]
            e.setdefault("keyed_keyless", P[pid]["keyed_keyless"])
            e.setdefault("keyed_keyless_rationale",
                         P[pid]["keyed_keyless_rationale"])
            merged += 1
    print(f"merged {merged} entr(ies); skipped {len(skipped)}: {skipped}")
    kkr.save_ledger(data)          # 4.02g choke point seals here
    try:
        kkr.render_ledger()        # regenerates LEDGER.md/ledger.html + served copies
    except Exception as ex:
        print(f"render step: {ex} - run any kkr write to regenerate")
    fresh = kkr.load_ledger()
    sealed = sum(1 for e in fresh["projections"]
                 if e.get("id", "").startswith("KKR-20260730")
                 and e.get("seal_sha256"))
    print(f"sealed: {sealed}/29 KKR-20260730 entries now carry seal_sha256")
    if sealed < 29:
        print("some entries did not seal - re-run kkr verify and read stderr")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    if ap.parse_args().apply:
        apply()
    else:
        review()
