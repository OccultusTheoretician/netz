**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060323Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-34 | 49% | 2026-09-29 | military/conflict | Between 2026-09-06 and 2026-09-26, US forces strike, disable, or destroy at least one additional Iranian oil tanker or crude carrier, as announced by US Central Command. | TRUE if a US Central Command statement dated 2026-09-06 to 2026-09-26, carried by Reuters, AP, or AFP, reports a US strike on at least one Iranian oil tanker or crude carrier in that window, excluding the three struck 2026-09-05. |
| KKR-20260906-35 | 49% | 2026-10-07 | military/conflict | Between 2026-09-05 and 2026-10-03, the governments of Russia and Ukraine both publicly confirm a general ceasefire or cessation-of-hostilities agreement covering the entire front line. | TRUE if, between 2026-09-05 and 2026-10-03, official statements from both the Kremlin and the Ukrainian presidency confirm a front-wide ceasefire agreement, reported by Reuters or AP. Partial truces (energy, Black Sea, humanitarian pauses) do not count. |
| KKR-20260906-36 | 35% | 2027-03-03 | political | Between 2026-09-05 and 2027-03-01, the US Fish and Wildlife Service publishes in the Federal Register a proposed rule to delist or downlist the gray wolf or Mexican wolf under the Endangered Species Act. | TRUE if federalregister.gov shows a document of type Proposed Rule from the Fish and Wildlife Service, publication date 2026-09-05 through 2027-03-01, proposing removal or reclassification of the gray wolf or Mexican wolf under the ESA. |
| KKR-20260906-37 | 21% | 2026-09-29 | economics/markets | Between 2026-09-08 and 2026-09-25, the US Treasury Office of Foreign Assets Control publishes at least one Iran-related designation action. | TRUE if the OFAC Recent Actions page (ofac.treasury.gov/recent-actions) lists at least one action dated 2026-09-08 through 2026-09-25 whose title contains Iran-related Designations or Iran-related Designation Updates. |
| KKR-20260906-38 | 30% | 2026-09-29 | cyber | The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-19490 (Citrix NetScaler ADC and Gateway authentication bypass) with a dateAdded value between 2026-09-05 and 2026-09-25. | TRUE if the CISA KEV JSON feed contains an entry for CVE-2026-19490 whose dateAdded field is between 2026-09-05 and 2026-09-25 inclusive. |
| KKR-20260906-39 | 36% | 2026-11-02 | crime/security | Between 2026-09-05 and 2026-10-30, the Plymouth County District Attorney announces that the Commonwealth will retry Lindsay Clancy on the murder charges, or the Plymouth Superior Court schedules a retrial date. | TRUE if, between 2026-09-05 and 2026-10-30, the Plymouth County DA states that Clancy will be retried on the murder charges, or the court docket sets a retrial date, per AP or the Boston Globe. |
| KKR-20260906-40 | 36% | 2026-09-29 | disaster | Between 2026-09-06 and 2026-09-26, the USGS catalog records at least one earthquake of magnitude 6.0 or greater with epicenter within 300 km of USGS event us7000tdvt (M6.3, 84 km SSW of Nikolski, Alaska). | TRUE if the USGS earthquake catalog (earthquake.usgs.gov) lists at least one event of magnitude 6.0 or greater, origin time 2026-09-06 through 2026-09-26 UTC, with epicenter within 300 km of event us7000tdvt. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The AfD wins an absolute majority of seats in the Saxony-Anhalt Landtag election held on 2026-09-06, per the official preliminary result." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The ICE Brent crude front-month futures contract settles at or above 100.00 USD per barrel on 2026-09-25. Reference: Brent 96.28 on the pack" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "By 2026-10-30, the CISA Known Exploited Vulnerabilities catalog marks CVE-2026-81578 or CVE-2026-82078 (PaperCut NG/MF) as knownRansomwareCa" → REJECTED: event window opens 2026-08-31, before this row is sealed (2026-09-05, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

1531 issued all-time across 16 forecaster arms · 1266 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 444 issued · 416 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 444 | 416 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 168 | 166 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 185 | 179 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 173 | 152 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*