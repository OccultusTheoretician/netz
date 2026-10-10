**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102253Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-62 | 45% | 2026-11-27 | military/conflict | A single Russian attack on one Ukrainian settlement kills at least 20 people between 2026-10-12 and 2026-11-22. | Ukrainian national or regional officials report 20 or more deaths from one Russian attack on one settlement occurring between 2026-10-12 and 2026-11-22, and at least two of Reuters, AP and BBC carry that toll. |
| KKR-20261010-63 | 15% | 2027-01-05 | political | Donald Trump and Vladimir Putin meet in person at least once between 2026-10-12 and 2026-12-31. | A White House readout or a kremlin.ru event record documents a face-to-face meeting between Trump and Putin held between 2026-10-12 and 2026-12-31. Phone and video calls do not count. |
| KKR-20261010-64 | 72% | 2026-12-11 | political | Democratic candidates win at least 218 of the 435 US House seats in elections held between 2026-11-03 and 2026-12-01, covering the general election and any runoffs. | AP race calls, supplemented by state-certified results for any uncalled race, show Democrats winning 218 or more House seats in elections held between 2026-11-03 and 2026-12-01. |
| KKR-20261010-65 | 45% | 2026-12-18 | political | Marcy Kaptur receives the most votes in the Ohio congressional district 9 general election held on 2026-11-03. | Ohio Secretary of State official results for the 2026-11-03 general election show Marcy Kaptur with the highest vote total in Ohio congressional district 9. |
| KKR-20261010-66 | 25% | 2026-12-15 | economics/markets | The S&P 500 index closes at or below 7,200.00 on at least one trading day between 2026-10-12 and 2026-12-11. Reference: 7,811.54 on the packet date. | The official S&P 500 daily close, FRED series SP500, is 7,200.00 or lower on any trading day from 2026-10-12 through 2026-12-11. Reference: 7,811.54 on the packet date. |
| KKR-20261010-67 | 35% | 2027-01-12 | cyber | CISA adds at least one vulnerability in Ahsay Systems products, including AhsayCBS, to the Known Exploited Vulnerabilities catalog between 2026-10-12 and 2027-01-08. | The CISA KEV JSON feed contains an entry whose vendorProject or product names Ahsay or AhsayCBS with a dateAdded value between 2026-10-12 and 2027-01-08 inclusive. |
| KKR-20261010-68 | 55% | 2026-11-13 | disaster | At least one earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M7.7 Panama mainshock, USGS event us6000u18k, between 2026-10-12 and 2026-11-08 UTC. | A USGS ComCat query for magnitude 6.0 or greater events within 200 km of the us6000u18k epicenter, origin times from 2026-10-12 00:00 through 2026-11-08 23:59 UTC, returns at least one event. |
| KKR-20261010-69 | 65% | 2026-12-04 | disaster | A presidential major disaster declaration, FEMA type DR, for Hurricane Isaias is approved for at least one US state or territory between 2026-10-10 and 2026-11-30. | OpenFEMA DisasterDeclarationsSummaries contains a record with declarationType DR, a declarationTitle naming Isaias, and a declarationDate between 2026-10-10 and 2026-11-30 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent front-month crude futures settle at or above 115.00 dollars per barrel on at least one trading day between 2026-10-12 and 2026-11-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The United States imports Russian-origin distillate fuel oil between 2026-11-01 and 2026-12-31, recorded as a nonzero monthly value in EIA c" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

3848 issued all-time across 21 forecaster arms · 3034 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 139 issued · 139 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*