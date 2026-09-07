**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: lmstudio/realist · 9 accepted / 1 rejected by validation gate · 8 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-04 | 25% | 2027-03-06 | cyber | On 2026-09-21, the CISA KEV catalog will carry a date-added value for a vulnerability with a CVSS score of 9.0 or higher, exploited in at least one confirmed incident between 2026-09-15 and 2026-09-21. | The CISA KEV catalog will list at least one vulnerability with a CVSS score of 9.0 or higher and a date-added value between 2026-09-15 and 2026-09-21, and at least one independent source (e.g., BleepingComputer, The Hacker News) will report a confirmed exploitation event during that window. |
| KKR-20260907-05 | 30% | 2027-03-06 | military/conflict | Between 2026-09-18 and 2026-09-25, a drone strike originating from Russian-controlled territory will result in at least one confirmed casualty in Kyiv, as verified by at least two independent sources from hostile sides (UA, WEST). | At least one casualty (defined as death or serious injury requiring hospitalization) will be reported in Kyiv during the window, with at least two independent sources from hostile sides (UA, WEST) confirming the event and attributing it to a drone strike from Russian-controlled territory. |
| KKR-20260907-06 | 20% | 2027-03-06 | disaster | Between 2026-09-16 and 2026-09-22, a major earthquake of magnitude 6.0 or higher will be recorded in the Pacific Ring of Fire, as confirmed by the USGS Significant Quakes database. | The USGS Significant Quakes database will list a seismic event with magnitude 6.0 or higher and depth less than 100 km, occurring between 2026-09-16 and 2026-09-22, with a confirmed location in the Pacific Ring of Fire. |
| KKR-20260907-07 | 10% | 2027-03-06 | political | On 2026-09-20, the German far-right AfD will win a majority in a federal parliamentary election, as confirmed by the official Federal Returning Officer report. | The official Federal Returning Officer report will list the AfD as the largest party in the German federal election held on 2026-09-20, with more than 30% of the vote. |
| KKR-20260907-08 | 35% | 2027-03-06 | military/conflict | Between 2026-09-17 and 2026-09-24, Iran will issue a public statement declaring a restricted zone in the Strait of Hormuz, as confirmed by at least two independent sources from hostile sides (AXIS, WEST). | At least two independent sources from hostile sides (AXIS, WEST) will report a public statement from Iran declaring a restricted zone in the Strait of Hormuz during the window. |
| KKR-20260907-09 | 25% | 2027-03-06 | economics/markets | On 2026-09-22, the 10-year U.S. Treasury yield will exceed 4.8% for the first time since 2023, as reported by the U.S. Department of the Treasury. | The U.S. Department of the Treasury will report a 10-year yield above 4.8% on 2026-09-22, based on the daily auction results. |
| KKR-20260907-10 | 18% | 2027-03-06 | disaster | Between 2026-09-19 and 2026-09-26, a wildfire will break out in the Amazon rainforest, resulting in at least 500,000 hectares burned, as confirmed by the GDACS Alerts system. | The GDACS Alerts system will list a wildfire event in the Amazon rainforest with a burned area of at least 500,000 hectares, confirmed by at least two independent sources. |
| KKR-20260907-11 | 5% | 2027-03-06 | economics/markets | On 2026-09-21, the U.S. Federal Reserve will announce a 50 basis point interest rate hike, as confirmed by the official FOMC press release. | The Federal Reserve will issue a press release on 2026-09-21 stating that the FOMC has raised the federal funds rate by 50 basis points. |
| KKR-20260907-12 | 22% | 2027-03-06 | cyber | Between 2026-09-15 and 2026-09-22, a cyberattack exploiting the N-able N-central flaw will result in a confirmed breach of a government agency's network, as verified by the CISA KEV catalog and a government press release. | The CISA KEV catalog will list the N-able N-central flaw (CVE-2026-XXXX) with a date-added value between 2026-09-15 and 2026-09-22, and a government agency will issue a public statement confirming a breach due to this vulnerability. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-23, the S&P 500 will close above 7,800 for the first time, based on the prior day's closing price of 7,718.60." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-23 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1622 issued all-time across 16 forecaster arms · 1357 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 25 issued · 25 open · nothing resolved yet — this arm earns a score at its first resolution.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 484 | 456 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*