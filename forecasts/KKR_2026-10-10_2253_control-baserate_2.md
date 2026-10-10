**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102253Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-55 | 69% | 2026-10-28 | military/conflict | Between 2026-10-12 and 2026-10-25, a single Russian missile, drone or glide-bomb attack on one Ukrainian city or town kills at least 20 people, per the death toll Ukrainian officials report as of 2026-10-28. | Ukrainian officials report 20 or more deaths from one Russian attack on one locality occurring between 2026-10-12 and 2026-10-25, and two of Reuters, AP, BBC carry that toll by 2026-10-28. |
| KKR-20261010-56 | 69% | 2026-11-10 | military/conflict | Between 2026-10-12 and 2026-11-06, the governments of Iran and the United States each publicly confirm a ceasefire or cessation of hostilities in the war involving Iran. | Reuters and AP both report that the Iranian and US governments each publicly confirmed a ceasefire or cessation-of-hostilities agreement announced between 2026-10-12 and 2026-11-06. |
| KKR-20261010-57 | 58% | 2026-11-02 | economics/markets | Between 2026-10-12 and 2026-10-29, the front-month ICE Brent futures contract settles at or above 110.00 dollars per barrel on at least one trading day. Reference: 104.72 in the packet market snapshot of 2026-10-10, the prior-session close. | ICE Futures Europe settlement data for the front-month Brent contract show a daily settlement of 110.00 dollars or more on at least one trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 in the packet snapshot of 2026-10-10. |
| KKR-20261010-58 | 58% | 2026-11-10 | economics/markets | Between 2026-10-12 and 2026-11-06, the S&P 500 closes below 7,400.00 on at least one trading day. Reference: 7,811.54 in the packet market snapshot of 2026-10-10, the prior-session close. | The S&P 500 daily closing level, per S&P Dow Jones Indices or FRED series SP500, is below 7,400.00 on at least one trading day between 2026-10-12 and 2026-11-06. Reference: 7,811.54 in the packet snapshot of 2026-10-10. |
| KKR-20261010-59 | 42% | 2026-11-10 | cyber | Between 2026-10-12 and 2026-11-06, CISA adds at least one vulnerability in Ahsay backup software, including AhsayCBS, to its Known Exploited Vulnerabilities catalog. | The CISA KEV catalog JSON carries at least one entry whose vendorProject or product field contains Ahsay and whose dateAdded value falls between 2026-10-12 and 2026-11-06 inclusive. |
| KKR-20261010-60 | 33% | 2026-11-10 | crime/security | Between 2026-10-12 and 2026-11-06, authorities in any country publicly announce the arrest or criminal charging of at least one alleged ShinyHunters member who had not been publicly arrested or charged before 2026-10-12. | At least two of BleepingComputer, Krebs on Security, The Record, Reuters or AP report an arrest or charge of an alleged ShinyHunters member publicly announced between 2026-10-12 and 2026-11-06, not publicly arrested or charged before 2026-10-12. |
| KKR-20261010-61 | 43% | 2026-10-27 | disaster | Between 2026-10-11 and 2026-10-24, the USGS catalog records at least one earthquake of magnitude 7.0 or greater within 300 km of the epicenter of the M7.7 Panama mainshock, USGS event us6000u18k, excluding that mainshock. | USGS ComCat query for origin times between 2026-10-11 and 2026-10-24 UTC, magnitude 7.0 or greater, within 300 km of event us6000u18k, excluding that event, returns at least one earthquake. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-12 and 2026-10-30, US Treasury OFAC or the White House issues a general license or executive order explicitly authorizing US" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ofac recent actions page | or | the federal register shows a general license,…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "In the US House general election held on 2026-11-03, Democratic candidates win at least 218 of the 435 seats, as called by the Associated Pr" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-12 and 2026-11-06, FEMA declares a major disaster of type DR for at least one US state or territory with a declaration title" → REJECTED: resolution offers alternative VENUES joined by 'or' (…openfema disasterdeclarationssummaries | or | the fema declarations page lists a declaratio…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3840 issued all-time across 21 forecaster arms · 3026 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1364 issued · 1163 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1364 | 1163 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 30 | 30 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 27 | 27 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 205 | 170 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 312 | 279 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*