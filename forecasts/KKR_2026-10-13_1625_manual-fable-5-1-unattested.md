**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131625Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-26 | 82% | 2026-11-17 | military/conflict | At least one merchant vessel is damaged or sunk by a drone, missile or naval mine strike in the Black Sea or at one of its ports between 2026-10-14 and 2026-11-13. | TRUE if at least two of Reuters, AP, BBC and AFP report a merchant vessel damaged or sunk by drone, missile or mine in the Black Sea or its ports between 2026-10-14 and 2026-11-13; otherwise FALSE. |
| KKR-20261013-27 | 26% | 2026-11-17 | economics/markets | The 10-year US Treasury constant maturity yield (FRED series DGS10) for 2026-11-13 is below 5.00 percent. Reference: 5.21 percent on the packet date 2026-10-13. | TRUE if the FRED DGS10 observation for 2026-11-13 is below 5.00 percent; FALSE if it is 5.00 percent or higher. Reference: 5.21 percent on the packet date. |
| KKR-20261013-28 | 24% | 2026-10-30 | economics/markets | The ICE Brent crude futures contract for December 2026 settles below 100.00 USD per barrel on 2026-10-28. Reference: front-month Brent at 105.86 on the packet date 2026-10-13. | TRUE if the official ICE settlement price of the Brent December 2026 contract on 2026-10-28 is below 100.00 USD per barrel; otherwise FALSE. Reference: 105.86 on the packet date. |
| KKR-20261013-29 | 38% | 2026-11-17 | economics/markets | The Nasdaq Composite records at least one daily close below 26,000.00 between 2026-10-14 and 2026-11-13. Reference: 27,190.34 on the packet date 2026-10-13. | TRUE if FRED series NASDAQCOM shows a daily close below 26,000.00 on any trading day between 2026-10-14 and 2026-11-13; otherwise FALSE. Reference: 27,190.34 on the packet date. |
| KKR-20261013-30 | 20% | 2027-01-04 | cyber | CISA adds at least one GitLab vulnerability to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-14 and 2026-12-31. | TRUE if the CISA KEV catalog contains at least one entry whose vendorProject is GitLab and whose dateAdded falls between 2026-10-14 and 2026-12-31; otherwise FALSE. |
| KKR-20261013-31 | 90% | 2026-11-17 | political | Kimberly Guilfoyle resigns or is removed as US ambassador to Greece, with the departure confirmed by her, the White House or the State Department between 2026-10-13 and 2026-11-13. | TRUE if at least two of AP, Reuters, CNBC, the Guardian and BBC report confirmation by Guilfoyle, the White House or the State Department, made between 2026-10-13 and 2026-11-13, that she resigned or was removed as ambassador; otherwise FALSE. |
| KKR-20261013-32 | 78% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | TRUE if Associated Press race calls as of 2026-12-18 show Democratic candidates winning at least 218 House seats in the 2026-11-03 election; FALSE if they show 217 or fewer. |
| KKR-20261013-33 | 50% | 2027-02-02 | crime/security | A guilty verdict or guilty plea on at least one count is entered in the federal hate crimes case over the 2022 Buffalo supermarket shooting (United States v. Gendron, Western District of New York) between 2026-10-14 and 2027-01-29. | TRUE if the Western District of New York docket for United States v. Gendron shows a guilty verdict or guilty plea on at least one count entered between 2026-10-14 and 2027-01-29; otherwise FALSE. |
| KKR-20261013-34 | 40% | 2026-11-17 | disaster | The USGS catalog records at least one earthquake of magnitude 6.0 or greater within 200 km of the epicenter of the M 7.7 Panama earthquake (USGS event us6000u18k), with origin time between 2026-10-14 and 2026-11-13 UTC. | TRUE if a USGS ComCat query returns at least one event of magnitude 6.0 or greater within 200 km of the us6000u18k epicenter with origin time between 2026-10-14 and 2026-11-13 UTC; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A general ceasefire between Russia and Ukraine covering the entire front line, confirmed by both governments and declared for at least 7 day" → REJECTED: the resolution names a different subject than the statement — the claim is about Russia, Ukraine and the resolution settles on AFP, AP, BBC, Kyiv. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

4048 issued all-time across 21 forecaster arms · 2937 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 337 issued · 279 open · 50 resolved · 34 hits / 16 misses · **Brier 0.248** against its own base rate 68.0% (climatological 0.218) · **skill -0.140**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1128 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*