**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041807Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-37 | 78% | 2026-09-18 | economics/markets | The FOMC raises the federal funds target range at its scheduled 2026-09-16 decision. Reference: target range 3.50 to 3.75 percent on the packet date 2026-09-04. | TRUE if the FOMC policy statement on federalreserve.gov for the 2026-09-15 to 2026-09-16 meeting sets a target range with upper bound above 3.75 percent. Adjudicated 2026-09-18. |
| KKR-20260904-38 | 40% | 2026-12-18 | military/conflict | The South Korean government announces a naval or military deployment to Strait of Hormuz escort or security operations between 2026-09-07 and 2026-12-15. | TRUE if the defence ministry or presidential office of South Korea announces such a deployment in that window and both Yonhap and Reuters report it. Adjudicated 2026-12-18. |
| KKR-20260904-39 | 72% | 2026-10-13 | cyber | The CISA KEV catalog gains an entry for a Google Chromium V8 vulnerability with a dateAdded value between 2026-09-04 and 2026-10-09. | TRUE if the CISA Known Exploited Vulnerabilities JSON contains a Google Chromium V8 record whose dateAdded falls between 2026-09-04 and 2026-10-09. Adjudicated 2026-10-13. |
| KKR-20260904-40 | 28% | 2027-02-18 | cyber | A CVE for the Cisco Nexus 9000 unauthenticated remote code execution flaw enters the CISA KEV catalog with dateAdded between 2026-09-04 and 2027-02-15. | TRUE if the CISA KEV JSON lists a Cisco NX-OS or Nexus 9000 record matching that flaw with dateAdded between 2026-09-04 and 2027-02-15. Adjudicated 2027-02-18. |
| KKR-20260904-41 | 50% | 2026-11-03 | political | Philippine Vice President Sara Duterte is taken into physical custody or surrenders to a Philippine court between 2026-09-04 and 2026-10-30. | TRUE if Philippine authorities book or process her in custody, or she surrenders in court, in that window, per Reuters and the Philippine Daily Inquirer. Adjudicated 2026-11-03. |
| KKR-20260904-42 | 18% | 2026-10-19 | disaster | USGS catalogs an earthquake of magnitude 6.0 or greater within 300 km of event us7000tdvt with origin time between 2026-09-05 and 2026-10-15. | TRUE if a USGS ComCat query returns an M6.0 or greater event within 300 km of the us7000tdvt epicenter with origin time in that window. Adjudicated 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "FRED series DGS10 prints at or above 5.00 percent on at least one business day between 2026-09-08 and 2026-11-30. Reference: 4.78 percent on" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Front-month NYMEX WTI settles at or above 100.00 dollars on at least one trading day between 2026-09-08 and 2026-11-30. Reference: 90.35 on " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Russia and Ukraine sign a written ceasefire or cessation-of-hostilities agreement covering the main front line between 2026-09-05 and 2026-1" → REJECTED: the resolution names a different subject than the statement — the claim is about Russia, Ukraine and the resolution settles on Adjudicated, Reuters, TASS. A row whose resolution checks a different fact can be scored correct while being wrong
- "The AfD is allocated more than half of all Landtag seats in the Saxony-Anhalt state election held 2026-09-06." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

1446 issued all-time across 16 forecaster arms · 1181 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 180 issued · 174 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*