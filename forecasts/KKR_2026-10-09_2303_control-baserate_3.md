**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092303Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-70 | 69% | 2026-11-11 | military/conflict | A Houthi missile or drone attack kills at least one person inside Saudi Arabia between 2026-10-10 and 2026-11-08. | TRUE if Saudi authorities (GACA, civil defence, Saudi Press Agency or the coalition spokesman) confirm at least one death in Saudi territory from a Houthi attack occurring in the window, as carried by Reuters or AP. |
| KKR-20261009-71 | 69% | 2026-11-25 | military/conflict | Ethiopian forces carry out an air, drone, artillery or ground attack on targets inside the internationally recognized territory of Eritrea between 2026-10-10 and 2026-11-22. | TRUE if the Ethiopian government acknowledges such an attack, or at least two of Reuters, AP and AFP report it as established fact rather than solely as an Eritrean claim, for an attack in the window. |
| KKR-20261009-72 | 58% | 2026-12-09 | economics/markets | The front-month ICE Brent crude futures contract settles at or above 100.00 USD per barrel on 2026-12-07. Reference: 104.81 USD per barrel on the packet date. | TRUE if the ICE Futures Europe settlement price of the front-month Brent crude futures contract on 2026-12-07 is at or above 100.00 USD per barrel; FALSE if below. |
| KKR-20261009-73 | 58% | 2027-01-05 | economics/markets | The 10-year US Treasury constant-maturity yield is at or below 5.00 percent on 2026-12-31. Reference: 5.27 percent on the packet date. | TRUE if FRED series DGS10 shows a value at or below 5.00 for 2026-12-31; FALSE if above. If no value is published for that date, the last prior published value is used. |
| KKR-20261009-74 | 42% | 2026-11-09 | cyber | CISA adds a Citrix NetScaler ADC or Gateway vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-09 and 2026-11-06, following the new NetScaler RCE flaw reported on 2026-10-09. | TRUE if the CISA KEV catalog contains an entry with vendorProject Citrix, a product naming NetScaler ADC or NetScaler Gateway, and a dateAdded value between 2026-10-09 and 2026-11-06; otherwise FALSE. |
| KKR-20261009-75 | 41% | 2026-12-14 | political | Democrats win control of the US Senate in the 2026-11-03 election, with Democrats plus independents caucusing with them holding at least 51 seats in the Senate that convenes in January 2027. | TRUE if AP race calls or certified results available by 2026-12-11, including any Georgia runoff, show Democrats plus independents caucusing with them holding at least 51 seats for January 2027; otherwise FALSE. |
| KKR-20261009-76 | 41% | 2026-11-20 | political | Florida Amendment 3 (HJR 1F, raising the homestead exemption from non-school property taxes) receives at least 60 percent Yes votes in the 2026-11-03 general election. | TRUE if official results published by the Florida Division of Elections show Amendment 3 receiving Yes votes at or above 60.0 percent of votes cast on the measure; FALSE otherwise. |
| KKR-20261009-77 | 33% | 2026-12-07 | crime/security | Nidal Hasan is executed by Army firing squad at Fort Hood between 2026-12-03 and 2026-12-04; the published execution date is 2026-12-03. | TRUE if the Army or the Pentagon confirms Hasan was executed on 2026-12-03 or 2026-12-04, as reported by AP or Reuters; FALSE if the execution is stayed, postponed past 2026-12-04, or commuted. |
| KKR-20261009-78 | 43% | 2026-11-09 | disaster | The President approves a major disaster declaration (FEMA type DR) for Florida for Hurricane Isaias between 2026-10-09 and 2026-11-06. | TRUE if the OpenFEMA Disaster Declarations Summaries dataset lists a DR declaration for state FL whose title names Hurricane Isaias, with a declarationDate between 2026-10-09 and 2026-11-06; otherwise FALSE. |
| KKR-20261009-79 | 43% | 2026-11-10 | disaster | An earthquake of magnitude 6.0 or greater occurs within 250 km of the epicenter of USGS event us6000u0xi (M6.3, 102 km NE of Norsup, Vanuatu) between 2026-10-12 and 2026-11-08 UTC. | TRUE if the USGS ComCat catalog at the deadline lists an event of magnitude 6.0 or greater with origin time between 2026-10-12 and 2026-11-08 UTC and epicenter within 250 km of the us6000u0xi epicenter. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3779 issued all-time across 21 forecaster arms · 2965 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1347 issued · 1146 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1347 | 1146 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 405 | 226 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 21 | 21 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 200 | 165 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 302 | 269 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*