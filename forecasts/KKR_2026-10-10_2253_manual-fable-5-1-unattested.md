**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102253Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: manual/fable-5.1/unattested · 10 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-28 | 82% | 2026-10-28 | military/conflict | Between 2026-10-12 and 2026-10-25, King Khalid International Airport in Riyadh is hit or targeted by at least one further missile or drone attack that Saudi authorities acknowledge or the attacking party claims. | TRUE if at least two of AP, Reuters, AFP and BBC report a missile or drone attack on or aimed at Riyadh airport between 2026-10-12 and 2026-10-25, acknowledged by Saudi authorities or claimed by the attacker; otherwise FALSE. |
| KKR-20261010-29 | 55% | 2026-11-03 | disaster | The USGS catalog records at least one earthquake of magnitude 6.0 or greater within 200 km of the epicenter of the M 7.7 Panama mainshock (USGS event us6000u18k) with origin time between 2026-10-11 and 2026-10-31 UTC. | TRUE if a USGS ComCat query (minimum magnitude 6.0, 200 km radius around event us6000u18k, origin times 2026-10-11 through 2026-10-31 UTC) returns at least one event; otherwise FALSE. |
| KKR-20261010-30 | 20% | 2026-11-03 | disaster | The US National Hurricane Center names at least one new Atlantic-basin tropical or subtropical storm (any name after Isaias on the 2026 list) between 2026-10-11 and 2026-10-31 UTC. | TRUE if the NHC Atlantic advisory archive shows a storm first receiving a name after Isaias on the 2026 list in an advisory issued between 2026-10-11 and 2026-10-31 UTC; otherwise FALSE. |
| KKR-20261010-31 | 30% | 2026-11-23 | economics/markets | ICE Brent front-month crude oil futures settle below 95.00 dollars per barrel on 2026-11-20. Reference: 104.72 on the packet date. | TRUE if the official ICE settlement price of the front-month Brent futures contract on 2026-11-20 is below 95.00; FALSE if it is 95.00 or higher. Reference: 104.72 on the packet date. |
| KKR-20261010-32 | 25% | 2026-12-02 | economics/markets | The 10-year US Treasury constant maturity yield (FRED series DGS10) is below 5.00 percent on 2026-11-30. Reference: 5.24 percent on the packet date. | TRUE if the FRED DGS10 observation for 2026-11-30 is below 5.00 percent; FALSE if it is 5.00 or higher. Reference: 5.24 percent on the packet date. |
| KKR-20261010-33 | 55% | 2026-12-02 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one AhsayCBS vulnerability with a date-added value between 2026-10-11 and 2026-11-30. | TRUE if the CISA KEV catalog JSON contains at least one entry whose vendor or product field names Ahsay or AhsayCBS with a dateAdded value between 2026-10-11 and 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20261010-34 | 65% | 2026-12-03 | crime/security | Between 2026-10-12 and 2026-11-30, at least one additional person, beyond those reported arrested through 2026-10-10, is arrested or criminally charged in any country in connection with the ShinyHunters hacking group. | TRUE if at least two of Reuters, AP, BleepingComputer, KrebsOnSecurity and The Record report a ShinyHunters-linked arrest or criminal charge of a previously unarrested person occurring between 2026-10-12 and 2026-11-30; otherwise FALSE. |
| KKR-20261010-35 | 88% | 2026-12-11 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | TRUE if Associated Press race calls or state-certified results available at the deadline show Democrats winning at least 218 House seats in the 2026-11-03 election; otherwise FALSE. |
| KKR-20261010-36 | 10% | 2027-01-04 | military/conflict | Between 2026-10-12 and 2026-12-31, the United States and Iran both publicly confirm a concluded agreement ending their war (a final deal, not a truce extension, framework or agreement in principle). | TRUE if at least two of Reuters, AP, AFP and BBC report that both governments confirmed a signed or finalized agreement ending the war, concluded between 2026-10-12 and 2026-12-31; otherwise FALSE. |
| KKR-20261010-37 | 75% | 2027-01-04 | political | Donald Trump and Vladimir Putin meet in person at least once between 2026-10-12 and 2026-12-31, either in a bilateral meeting or by interacting face to face at a multilateral summit. | TRUE if at least two of Reuters, AP, AFP and BBC report an in-person encounter in which Trump and Putin interact, taking place between 2026-10-12 and 2026-12-31; phone and video calls do not count; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3816 issued all-time across 21 forecaster arms · 3002 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 312 issued · 279 open · 25 resolved · 20 hits / 5 misses · **Brier 0.207** against its own base rate 80.0% (climatological 0.160) · **skill -0.296** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1347 | 1146 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
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
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*