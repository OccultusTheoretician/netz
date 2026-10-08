**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082338Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: manual/sonnet-5.5/unattested · 10 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-52 | 80% | 2026-10-20 | disaster | Between 2026-10-08 and 2026-10-16, Hurricane Isaias will make landfall along the US Gulf Coast from Louisiana through Apalachee Bay, Florida, with sustained winds of 74 mph or more. | Between 2026-10-08 and 2026-10-16, National Hurricane Center advisories state the center of Isaias made landfall along the US Gulf Coast from Louisiana through Apalachee Bay, Florida, with sustained winds of 74 mph or more. |
| KKR-20261008-53 | 18% | 2026-10-27 | disaster | USGS will list at least one earthquake of magnitude 6.0 or greater with a place name containing Vanuatu and a UTC origin time between 2026-10-09 and 2026-10-23. | USGS ComCat lists at least one earthquake of magnitude 6.0 or greater with place name containing Vanuatu and UTC origin time between 2026-10-09 and 2026-10-23. |
| KKR-20261008-54 | 8% | 2026-11-17 | military/conflict | Between 2026-10-12 and 2026-11-13, the governments of the United States and Iran will both publicly announce a ceasefire or a signed agreement with each other. | Between 2026-10-12 and 2026-11-13, official statements from both the US government and the Iranian government, reported by at least two of Reuters, AP and BBC, confirm a ceasefire or signed agreement between them. |
| KKR-20261008-55 | 85% | 2026-10-28 | military/conflict | Between 2026-10-12 and 2026-10-25, at least one commercial vessel will be struck by a missile, drone or other projectile in the Persian Gulf, Strait of Hormuz or Gulf of Oman. | UKMTO or at least two of Reuters, AP and BBC report a commercial vessel struck by a projectile in the Persian Gulf, Strait of Hormuz or Gulf of Oman, with the incident dated between 2026-10-12 and 2026-10-25. |
| KKR-20261008-56 | 27% | 2026-10-28 | military/conflict | Between 2026-10-12 and 2026-10-25, a single Russian attack on one locality in Ukraine will kill at least 20 people by official Ukrainian toll. | At least two of Reuters, AP and BBC report an official Ukrainian death toll of 20 or more from one Russian attack on one locality in Ukraine, with the attack dated between 2026-10-12 and 2026-10-25. |
| KKR-20261008-57 | 28% | 2026-11-13 | economics/markets | Between 2026-10-09 and 2026-10-30, the WTI crude spot price at Cushing will reach 105.00 USD per barrel or more on at least one trading day. Reference: 93.02 USD on the packet date 2026-10-08. | FRED series DCOILWTICO shows at least one daily value of 105.00 or higher with an observation date between 2026-10-09 and 2026-10-30. Reference: 93.02 on the packet date. |
| KKR-20261008-58 | 22% | 2026-11-10 | economics/markets | Between 2026-10-09 and 2026-11-06, the US 10-year Treasury constant-maturity yield will close at or above 5.60 percent on at least one trading day. Reference: 5.30 percent on the packet date 2026-10-08. | FRED series DGS10 shows at least one daily value of 5.60 or higher with an observation date between 2026-10-09 and 2026-11-06. Reference: 5.30 percent on the packet date. |
| KKR-20261008-59 | 45% | 2026-11-04 | cyber | CISA will add at least one Fortinet vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-12 and 2026-11-01. | The CISA KEV catalog JSON carries at least one entry with vendorProject Fortinet and dateAdded between 2026-10-12 and 2026-11-01 inclusive. |
| KKR-20261008-60 | 15% | 2026-11-17 | cyber | CISA will add at least one SonicWall SMA1000 vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-12 and 2026-11-13. | The CISA KEV catalog JSON carries at least one entry with vendorProject SonicWall, product or vulnerabilityName naming SMA1000, and dateAdded between 2026-10-12 and 2026-11-13 inclusive. |
| KKR-20261008-61 | 74% | 2027-01-06 | political | Democratic candidates will win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03. | As of 2027-01-06, the Clerk of the House member list for the 120th Congress shows at least 218 voting Members of the Democratic Party elected in the general election of 2026-11-03. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3673 issued all-time across 21 forecaster arms · 2859 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 80 issued · 80 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1302 | 1101 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 293 | 260 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 80 | 80 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*