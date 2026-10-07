**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 072334Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-34 | 69% | 2026-11-03 | military/conflict | Russian air, missile or drone strikes kill at least 10 people in Ukraine on a single calendar day between 2026-10-09 and 2026-10-29. | At least two of Reuters, AP, AFP and BBC report Ukrainian officials attributing 10 or more deaths to Russian air, missile or drone strikes on one calendar day between 2026-10-09 and 2026-10-29. |
| KKR-20261007-35 | 58% | 2026-11-10 | economics/markets | The 10-year US Treasury constant maturity yield, FRED series DGS10, is at or above 5.50 percent on 2026-11-06. Reference: 5.30 percent on the packet date. | FRED series DGS10 shows a value of 5.50 or higher for observation date 2026-11-06. Reference: 5.30 percent on the packet date. |
| KKR-20261007-36 | 58% | 2026-11-10 | economics/markets | ICE Brent crude front-month futures settle at or above 110.00 dollars per barrel on at least one trading day between 2026-10-08 and 2026-11-06. Reference: 101.67 dollars on the packet date. | ICE Brent crude front-month futures post a daily settlement price of 110.00 dollars or higher on at least one trading day between 2026-10-08 and 2026-11-06. Reference: 101.67 dollars on the packet date. |
| KKR-20261007-37 | 42% | 2026-10-30 | cyber | CISA adds at least one Atlassian vulnerability to its Known Exploited Vulnerabilities catalog with a date added between 2026-10-07 and 2026-10-28. | The CISA KEV catalog carries at least one entry with vendorProject Atlassian and a dateAdded value between 2026-10-07 and 2026-10-28 inclusive. |
| KKR-20261007-38 | 41% | 2026-10-28 | political | Flavio Bolsonaro wins the Brazilian presidential runoff election held on 2026-10-25. | Official results of the Superior Electoral Court of Brazil (TSE) for the presidential second round held on 2026-10-25 show Flavio Bolsonaro receiving more valid votes than his opponent. |
| KKR-20261007-39 | 41% | 2026-12-15 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | Associated Press race calls or state-certified results show Democratic candidates winning 218 or more US House seats in the general election held on 2026-11-03. |
| KKR-20261007-40 | 43% | 2026-10-19 | disaster | A hurricane makes landfall in Louisiana, Mississippi, Alabama or Florida between 2026-10-08 and 2026-10-15. | National Hurricane Center advisories or tropical cyclone updates report a landfall in Louisiana, Mississippi, Alabama or Florida between 2026-10-08 and 2026-10-15 with maximum sustained winds of at least 74 mph at landfall. |
| KKR-20261007-41 | 43% | 2026-11-10 | disaster | At least one further laboratory-confirmed Ebola case, beyond the first case reported by 2026-10-07, is confirmed in Kenya between 2026-10-08 and 2026-11-06. | Kenya Ministry of Health, WHO Disease Outbreak News or Africa CDC reports show a second or later laboratory-confirmed Ebola case in Kenya with confirmation dated between 2026-10-08 and 2026-11-06. |
| KKR-20261007-42 | 33% | 2027-03-30 | crime/security | The State of Tennessee carries out the execution of Christa Pike between 2026-10-08 and 2027-03-26. | Tennessee Department of Correction records or the Death Penalty Information Center execution database list Christa Pike as executed on a date between 2026-10-08 and 2027-03-26. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The French National Assembly adopts a motion of censure against the government between 2026-10-08 and 2026-12-18." → REJECTED: the resolution requires date and the failure condition does not mention it — an outcome missing it satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements

## III. LEDGER STANDING

3576 issued all-time across 21 forecaster arms · 2762 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1274 issued · 1073 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1274 | 1073 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*