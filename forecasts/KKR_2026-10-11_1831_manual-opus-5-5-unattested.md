**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111831Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-59 | 65% | 2026-10-28 | military/conflict | Saudi Arabia or the Saudi-led coalition carries out at least one air or missile strike on Houthi-controlled Yemen between 2026-10-12 and 2026-10-25. | TRUE if at least two of Reuters, AP and AFP report a Saudi or Saudi-led coalition air or missile strike on Houthi-controlled Yemen occurring between 2026-10-12 and 2026-10-25. |
| KKR-20261011-60 | 82% | 2026-10-28 | military/conflict | At least one merchant vessel is attacked, struck by a projectile, boarded or seized in the Strait of Hormuz, the Gulf of Oman or the Persian Gulf between 2026-10-12 and 2026-10-25. | TRUE if UKMTO reports a merchant vessel attacked, struck, boarded or seized in the Strait of Hormuz, Gulf of Oman or Persian Gulf with an incident date between 2026-10-12 and 2026-10-25. |
| KKR-20261011-61 | 62% | 2026-11-04 | military/conflict | A Russian missile or drone strike damages a Ukrainian thermal or hydroelectric power plant or gas-production facility between 2026-10-19 and 2026-11-01. | TRUE if Reuters or AP reports, citing Ukrainian officials or the operator, Russian strike damage to a Ukrainian thermal or hydroelectric power plant or gas-production facility occurring between 2026-10-19 and 2026-11-01. |
| KKR-20261011-62 | 54% | 2027-01-06 | economics/markets | The 10-year US Treasury constant-maturity yield is at or above 5.50 percent on at least one trading day between 2026-10-13 and 2026-12-31. Reference: 5.24 percent on the packet date, 2026-10-11. | TRUE if FRED series DGS10 shows a daily value of 5.50 or higher for any date between 2026-10-13 and 2026-12-31. |
| KKR-20261011-63 | 26% | 2026-12-02 | economics/markets | ICE Brent front-month crude futures settle at or above 125.00 US dollars per barrel on at least one trading day between 2026-10-12 and 2026-11-30. Reference: 104.72 dollars per barrel on the packet date, 2026-10-11. | TRUE if any ICE Futures Europe Brent front-month daily settlement price dated between 2026-10-12 and 2026-11-30 is 125.00 US dollars per barrel or higher. |
| KKR-20261011-64 | 55% | 2026-12-02 | cyber | CISA adds at least one Apple vulnerability affecting iOS or iPadOS to its Known Exploited Vulnerabilities catalog between 2026-10-12 and 2026-11-30. | TRUE if the CISA KEV catalog contains an entry with vendorProject Apple, a dateAdded value between 2026-10-12 and 2026-11-30, and iOS or iPadOS named in its product or shortDescription field. |
| KKR-20261011-65 | 42% | 2026-11-11 | disaster | An earthquake of magnitude 6.5 or greater occurs within 250 km of the epicenter of the M7.7 Panama mainshock, USGS event us6000u18k, between 2026-10-12 and 2026-11-08 UTC. | TRUE if USGS ComCat lists an event of magnitude 6.5 or greater with origin time between 2026-10-12 and 2026-11-08 UTC located within 250 km of the us6000u18k epicenter. |
| KKR-20261011-66 | 20% | 2026-12-02 | disaster | A presidential major disaster declaration naming Isaias is approved for Florida or Alabama between 2026-10-12 and 2026-11-30. | TRUE if the OpenFEMA Disaster Declarations Summaries dataset lists a DR declaration for Florida or Alabama whose title names Isaias, with a declarationDate between 2026-10-12 and 2026-11-30. |
| KKR-20261011-67 | 7% | 2027-04-05 | political | US Senator John Fetterman changes his party affiliation away from the Democratic Party between 2026-10-12 and 2027-03-31. | TRUE if the Congress.gov member record or the Senate.gov senator list shows Fetterman with a party other than Democratic, with the change effective between 2026-10-12 and 2027-03-31. |
| KKR-20261011-68 | 45% | 2026-11-17 | crime/security | Polish prosecutors charge at least one person over the alleged plot against Prime Minister Donald Tusk and the defence minister between 2026-10-12 and 2026-11-13. | TRUE if Polish prosecutors announce charges against at least one person over the alleged plot against Tusk or the defence minister between 2026-10-12 and 2026-11-13, as reported by PAP or Reuters. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3924 issued all-time across 21 forecaster arms · 3110 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 149 issued · 149 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1389 | 1188 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 320 | 287 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 149 | 149 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*