#!/usr/bin/env python3
"""
patch_kkr_fc_0731.py - RPAS 4.02f repair for the 19 unsealed 2026-07-31 rows
(manual/sonnet-5 and manual/opus-5). From C:\\netz. Default REPORTS; --apply
merges + saves through kkr.save_ledger, where the 4.02g choke point seals.
Never overwrites a non-empty field; merges only open rows whose arm matches.

  python patch_kkr_fc_0731.py            # review
  python patch_kkr_fc_0731.py --apply    # merge + seal

keyed/keyless rule as established: KEYLESS = single named mechanical
instrument (exchange close, FOMC statement, the CISA KEV page). KEYED =
multi-outlet search or operator characterization. 5 keyless, 14 keyed.
"""
import argparse
import sys
from pathlib import Path

P = {
 # ---- manual/sonnet-5 · KKR-20260731-11 .. -19 ----
 "KKR-20260731-11": {"arm": "manual/sonnet-5",
  "failure_condition": "Neither the Gaza Board of Peace nor Reuters, AP, Al Jazeera or BBC reports a verified Hamas weapons handover or destruction event under the agreement dated 2026-07-31 through 2026-08-31, as read on 2026-08-31; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator reads Board and wire coverage and judges what constitutes a verified handover or destruction event."},
 "KKR-20260731-12": {"arm": "manual/sonnet-5",
  "failure_condition": "No new Iran-linked strike on a vessel or a US-linked asset in the Gulf states or the Strait of Hormuz dated 2026-07-31 through 2026-08-14 is reported by U.S. Central Command, Reuters, AP or CNBC, as read on 2026-08-14; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Iran-linkage attribution and asset-class characterization are operator readings of official and wire coverage."},
 "KKR-20260731-13": {"arm": "manual/sonnet-5",
  "failure_condition": "Anthropic publishes no blog post, security advisory or report specifically addressing the reported Claude-related breach of three organizations and the PyPI malware upload, as reported by a major outlet dated 2026-07-31 through 2026-08-21, as read on 2026-08-21; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Whether a publication specifically addresses the named incident is an operator characterization judgment."},
 "KKR-20260731-14": {"arm": "manual/sonnet-5",
  "failure_condition": "No report by Spanish authorities, Reuters or AP dated 2026-07-31 through 2026-08-19 states a confirmed migrant death toll above 60 from the Ceuta border-crossing surge, as read on 2026-08-19; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Toll confirmation and surge attribution are read from official and wire reporting."},
 "KKR-20260731-15": {"arm": "manual/sonnet-5",
  "failure_condition": "Apple common stock records no daily close below its 2026-07-31 close on any trading day 2026-08-03 through 2026-08-07, per official exchange closing data as read on 2026-08-07; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Official closing-price series against a fixed reference close; mechanical."},
 "KKR-20260731-16": {"arm": "manual/sonnet-5",
  "failure_condition": "No Federal Reserve announcement of an increase in the federal funds rate dated 2026-07-31 through 2026-10-30 is reported by a major financial outlet, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Resolution basis names outlet reporting rather than the FOMC statement alone; operator reads coverage."},
 "KKR-20260731-17": {"arm": "manual/sonnet-5",
  "failure_condition": "No major-outlet report dated 2026-07-31 through 2026-08-28 names a new accuser alleging misconduct against the St Paul mayor, and none reports a resignation or a formal ethics or criminal proceeding involving the mayor, as read on 2026-08-28; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Compound criterion; operator judges accuser novelty and what constitutes a formal proceeding."},
 "KKR-20260731-18": {"arm": "manual/sonnet-5",
  "failure_condition": "No report by Greek or Spanish civil protection authorities or a major wire service dated 2026-07-31 through 2026-08-24 states a combined confirmed death toll above 5 from the current Greece and Spain wildfire events, as read on 2026-08-24; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Combining tolls across two national events and attributing them to the named fires is an operator reading."},
 "KKR-20260731-19": {"arm": "manual/sonnet-5",
  "failure_condition": "No report by Reuters, AP, Al Jazeera or Deutsche Welle dated 2026-07-31 through 2026-08-18 describes a new Houthi-Saudi strike or attack in Yemen beyond the current flare-up, as read on 2026-08-18; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator judges what counts as a new exchange beyond the flare-up already reported."},
 # ---- manual/opus-5 · KKR-20260731-20 .. -29 ----
 "KKR-20260731-20": {"arm": "manual/opus-5",
  "failure_condition": "No official US Navy, CENTCOM or DoD statement carried by two or more major outlets confirms a direct armed engagement between US forces and Iranian forces or Iranian-operated vessels or aircraft in or near the Strait of Hormuz occurring 2026-08-07 through 2026-09-30, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Official confirmation plus two-outlet carriage plus engagement characterization are operator readings."},
 "KKR-20260731-21": {"arm": "manual/opus-5",
  "failure_condition": "No official statement from the Gaza Board of Peace, a named international monitoring body, or the US government dated 2026-08-07 through 2026-10-30 confirms a completed physical handover of heavy weapons by Hamas; announcements of agreement alone do not resolve true; that reading on 2026-10-30 scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Completedness and the heavy-weapons class are operator judgments; the criterion itself excludes announcement-only reporting."},
 "KKR-20260731-22": {"arm": "manual/opus-5",
  "failure_condition": "No FOMC statement issued 2026-08-07 through 2026-12-31 announces a higher federal funds target range, as read at federalreserve.gov on 2026-12-31; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Single named instrument; mechanical comparison of announced target ranges."},
 "KKR-20260731-23": {"arm": "manual/opus-5",
  "failure_condition": "No NYMEX front-month WTI settlement exceeds 95.00 USD on any session 2026-08-07 through 2026-09-30, per exchange or major financial press settlement data as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Named exchange settlement series against a fixed numeric threshold; mechanical."},
 "KKR-20260731-24": {"arm": "manual/opus-5",
  "failure_condition": "Neither Frontex nor the European Commission issues a public statement dated 2026-08-07 through 2026-09-30 announcing personnel deployment or emergency border funding to Spain for the Ceuta crossings, as read on 2026-09-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator judges whether a statement announces qualifying deployment or funding for the named border."},
 "KKR-20260731-25": {"arm": "manual/opus-5",
  "failure_condition": "No publicly reported letter, formal inquiry or hearing notice from a US congressional committee, member of Congress, or federal agency naming Anthropic and referencing the reported autonomous breach is dated 2026-08-07 through 2026-11-30, as read on 2026-11-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator reads whether a communication names the company and references the incident."},
 "KKR-20260731-26": {"arm": "manual/opus-5",
  "failure_condition": "The CISA KEV catalog shows no entry for the late July 2026 JetBrains TeamCity remote code execution vulnerability with a date added between 2026-08-07 and 2026-10-30, as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Named government catalog page; presence of a dated entry is mechanical."},
 "KKR-20260731-27": {"arm": "manual/opus-5",
  "failure_condition": "The official CBOE VIX close does not exceed 35.00 on any session 2026-08-07 through 2026-10-30, per CBOE or major financial press data as read on 2026-10-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyless",
  "keyed_keyless_rationale": "Named index official close against a fixed numeric threshold; mechanical."},
 "KKR-20260731-28": {"arm": "manual/opus-5",
  "failure_condition": "No statement by Pakistani authorities, the Alpine Club of Pakistan, or major wire reporting dated 2026-08-07 through 2026-08-31 confirms a death toll of at least eight from the Broad Peak avalanche, as read on 2026-08-31; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Toll confirmation and event attribution are read from official and wire reporting."},
 "KKR-20260731-29": {"arm": "manual/opus-5",
  "failure_condition": "No credible reporting dated 2026-08-07 through 2026-11-30 confirms the St Paul mayor resigning, being removed from office, or publicly announcing she will not seek re-election, as read on 2026-11-30; that reading scores this entry a MISS.",
  "keyed_keyless": "keyed",
  "keyed_keyless_rationale": "Operator judges credibility of reporting and which of the three outcomes occurred."},
}


def run(apply: bool):
    print(("APPLYING" if apply else "PROPOSED (nothing written)") + "\n" + "-" * 56)
    sys.path.insert(0, ".")
    import kkr
    data = kkr.load_ledger()
    byid = {e.get("id"): e for e in data["projections"]}
    merged, skipped = 0, []
    for pid in sorted(P):
        want = P[pid]
        e = byid.get(pid)
        if e is None:
            skipped.append(f"{pid} (absent)"); continue
        if e.get("model") != want["arm"]:
            skipped.append(f"{pid} (arm {e.get('model')} != {want['arm']})"); continue
        if e.get("status") != "open":
            skipped.append(f"{pid} (not open)"); continue
        if str(e.get("failure_condition", "")).strip():
            skipped.append(f"{pid} (FC present)"); continue
        if apply:
            e["failure_condition"] = want["failure_condition"]
            e.setdefault("keyed_keyless", want["keyed_keyless"])
            e.setdefault("keyed_keyless_rationale", want["keyed_keyless_rationale"])
        merged += 1
        print(f"{'MERGED' if apply else 'WILL MERGE':13s} {pid}  [{want['keyed_keyless'].upper()}]")
    if skipped:
        print(f"skipped: {skipped}")
    if apply and merged:
        kkr.save_ledger(data)  # 4.02g choke point seals here
        fresh = kkr.load_ledger()
        day = [e for e in fresh["projections"]
               if str(e.get("id", "")).startswith("KKR-20260731")]
        sealed = sum(1 for e in day if e.get("seal_sha256"))
        print(f"\nsealed: {sealed}/{len(day)} KKR-20260731 rows carry seal_sha256")
    elif not apply:
        print(f"\n{merged} row(s) will merge. Apply with: "
              "python patch_kkr_fc_0731.py --apply")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    run(ap.parse_args().apply)
