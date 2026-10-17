**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171827Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-68 | 45% | 2026-10-27 | disaster | Hurricane Trudy makes landfall in Mexico at hurricane intensity, with maximum sustained winds of at least 64 knots, between 2026-10-17 and 2026-10-24. | TRUE if a National Hurricane Center advisory or tropical cyclone update issued between 2026-10-17 and 2026-10-24 reports the center of Trudy making landfall in Mexico with maximum sustained winds of 64 knots or more; FALSE otherwise. |
| KKR-20261017-69 | 85% | 2026-10-30 | economics/markets | At least one FOMC voting member dissents from the federal funds rate decision announced on 2026-10-28 at the close of the scheduled 2026-10-27 to 2026-10-28 meeting. | TRUE if the FOMC statement published on federalreserve.gov on 2026-10-28 names at least one member voting against the policy action; FALSE if the recorded vote is unanimous. |
| KKR-20261017-70 | 78% | 2026-11-12 | military/conflict | At least one merchant vessel is hit by a projectile, drone, mine, or explosive, or is seized, in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-10-19 and 2026-11-08. | TRUE if UKMTO or JMIC reports a merchant vessel hit by a projectile, drone, mine, or explosive, or seized, in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-10-19 and 2026-11-08; FALSE otherwise. |
| KKR-20261017-71 | 55% | 2026-11-18 | military/conflict | Russia launches at least 700 drones and missiles combined at Ukraine in a single overnight attack between 2026-10-19 and 2026-11-15. | TRUE if a Ukrainian Air Force daily summary, as carried by Reuters, AP, or Kyiv Independent, counts at least 700 drones and missiles launched in one overnight attack dated between 2026-10-19 and 2026-11-15; FALSE otherwise. |
| KKR-20261017-72 | 28% | 2026-12-03 | economics/markets | The Nasdaq Composite closes at or below 23,526.03, ten percent under the reference level, on at least one trading day between 2026-10-19 and 2026-11-30. Reference: 26,140.03 on the packet date. | TRUE if FRED series NASDAQCOM shows a daily close at or below 23,526.03 for any date between 2026-10-19 and 2026-11-30 inclusive; FALSE otherwise. Reference: 26,140.03 on the packet date. |
| KKR-20261017-73 | 38% | 2026-12-11 | economics/markets | The WTI crude oil price at Cushing is at or above 110.00 dollars per barrel on at least one trading day between 2026-10-19 and 2026-11-30. Reference: 99.02 dollars per barrel on the packet date. | TRUE if FRED series DCOILWTICO shows a daily value at or above 110.00 for any date between 2026-10-19 and 2026-11-30 inclusive; FALSE otherwise. Reference: 99.02 dollars per barrel on the packet date. |
| KKR-20261017-74 | 18% | 2026-12-18 | political | Republican Senator Roger Marshall loses the 2026-11-03 Kansas US Senate general election. | TRUE if certified 2026-11-03 Kansas US Senate general election results published by the Kansas Secretary of State show a candidate other than Roger Marshall receiving the most votes; FALSE otherwise. |
| KKR-20261017-75 | 38% | 2027-01-04 | cyber | CISA adds at least one Drupal vulnerability to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-19 and 2026-12-31. | TRUE if the CISA KEV JSON feed contains at least one entry with vendorProject Drupal and dateAdded between 2026-10-19 and 2026-12-31 inclusive; FALSE otherwise. |
| KKR-20261017-76 | 18% | 2027-01-04 | crime/security | Federal criminal charges naming US Representative Ilhan Omar as a defendant become public between 2026-10-19 and 2026-12-31. | TRUE if a federal indictment, information, or criminal complaint naming Ilhan Omar as a defendant appears unsealed on a federal court docket in PACER or CourtListener between 2026-10-19 and 2026-12-31; FALSE otherwise. |
| KKR-20261017-77 | 77% | 2027-01-19 | political | A Democrat is elected Speaker of the US House at the opening of the 120th Congress, in a floor vote held between 2027-01-03 and 2027-01-15, following the 2026-11-03 midterm elections. | TRUE if the House Clerk roll call electing the 120th Congress Speaker, held between 2027-01-03 and 2027-01-15, elects a Democrat; FALSE if a non-Democrat or nobody is elected in that window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4396 issued all-time across 21 forecaster arms · 3285 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 203 issued · 198 open · 5 resolved · 3 hits / 2 misses · **Brier 0.440** against its own base rate 60.0% (climatological 0.240) · **skill -0.835** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1546 | 1250 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*