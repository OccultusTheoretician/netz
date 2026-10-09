**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092303Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: manual/sonnet-5.5/unattested · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-44 | 55% | 2026-10-27 | cyber | CISA adds the maximum-severity SonicWall SMA1000 flaw CVE-2026-102255 to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-09 and 2026-10-23. | The CISA KEV JSON catalog carries an entry with cveID CVE-2026-102255 and a dateAdded value between 2026-10-09 and 2026-10-23 inclusive. |
| KKR-20261009-45 | 45% | 2026-11-10 | cyber | CISA adds the NetScaler ADC and NetScaler Gateway memory overflow flaw CVE-2026-107406 to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-09 and 2026-11-06. | The CISA KEV JSON catalog carries an entry with cveID CVE-2026-107406 and a dateAdded value between 2026-10-09 and 2026-11-06 inclusive. |
| KKR-20261009-46 | 25% | 2026-11-13 | economics/markets | The FRED series DCOILWTICO WTI spot price is at or above 100.00 USD per barrel on at least one date between 2026-10-12 and 2026-11-06. Reference: 91.98 USD per barrel in the packet market snapshot dated 2026-10-09. | FRED series DCOILWTICO shows at least one daily value of 100.00 USD per barrel or higher dated 2026-10-12 through 2026-11-06 inclusive. Reference: 91.98 on the packet date. |
| KKR-20261009-47 | 22% | 2026-11-10 | economics/markets | The US 10-year Treasury constant maturity yield in FRED series DGS10 is at or above 5.50 percent on at least one date between 2026-10-12 and 2026-11-06. Reference: 5.27 percent in the packet market snapshot dated 2026-10-09. | FRED series DGS10 shows at least one daily value of 5.50 percent or higher dated 2026-10-12 through 2026-11-06 inclusive. Reference: 5.27 percent on the packet date. |
| KKR-20261009-48 | 9% | 2026-10-27 | disaster | USGS lists at least one earthquake of magnitude 6.5 or greater with Vanuatu in its place text and an origin time between 2026-10-10 and 2026-10-24 UTC. | A USGS ComCat query returns at least one event of magnitude 6.5 or greater whose place field contains Vanuatu, with origin time from 2026-10-10 00:00 UTC through 2026-10-24 23:59 UTC. |
| KKR-20261009-49 | 25% | 2026-10-30 | military/conflict | At least one person is killed inside Saudi Arabia by a Houthi missile or drone strike that occurs between 2026-10-12 and 2026-10-26. | Reuters and AP both report that at least one person was killed inside Saudi Arabia by a Houthi missile or drone strike occurring between 2026-10-12 and 2026-10-26 inclusive. |
| KKR-20261009-50 | 8% | 2026-11-10 | military/conflict | The US and Iranian governments each publicly confirm a ceasefire or cessation of hostilities between them, in statements dated between 2026-10-12 and 2026-11-06. | Reuters and AP both report official statements from Washington and Tehran, dated 2026-10-12 through 2026-11-06 inclusive, confirming a mutual ceasefire or end of hostilities between the two countries. |
| KKR-20261009-51 | 62% | 2026-12-11 | political | After the general election held on 2026-11-03, AP race calls as of 2026-12-11 show Democrats and independents who caucus with them holding at least 51 of the 100 US Senate seats. | AP results as of 2026-12-11 show the Democratic caucus winning or holding at least 51 of 100 Senate seats after the 2026-11-03 election, counting any runoffs completed by that date. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "FEMA records a presidentially declared major disaster (type DR) for Hurricane Isaias in at least one US state, with a declaration date betwe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…openfema disasterdeclarationssummaries | or | the fema…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Army executes Nidal Hasan by firing squad at Fort Hood, Texas, on 2026-12-03, the date set in the Army execution order signed 2026-10-06" → REJECTED: event window opens 2026-10-06, before this row is sealed (2026-10-09, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

3751 issued all-time across 21 forecaster arms · 2937 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 88 issued · 88 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1329 | 1128 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
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
| manual/opus-5.5/unattested | 121 | 121 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*