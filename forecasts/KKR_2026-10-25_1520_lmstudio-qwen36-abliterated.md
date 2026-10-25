**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-05 | 20% | 2026-11-17 | disaster | A magnitude 6.0 or greater earthquake occurs in the Bonin Islands region between 2026-11-01 and 2026-11-14. | The USGS Significant Quakes catalog records an event with magnitude >= 6.0 in the Bonin Islands region with a date-added value between 2026-11-01 and 2026-11-14. |
| KKR-20261025-06 | 45% | 2026-12-18 | economics | The US Federal Reserve cuts the federal funds rate by at least 25 basis points at its December 2026 meeting. | The Federal Reserve announces a rate cut of 25 basis points or more at the December 2026 FOMC meeting. |
| KKR-20261025-07 | 55% | 2026-11-03 | political | Lula wins the Brazilian presidential election runoff in October 2026. | Lula is declared the winner of the Brazilian presidential election runoff in October 2026. |
| KKR-20261025-08 | 35% | 2027-01-04 | economics | The 10-year US Treasury yield closes below 4.99 on the last trading day of 2026. | The 10-year US Treasury yield closing price on 2026-12-31 is less than 4.99. |
| KKR-20261025-09 | 30% | 2026-11-17 | military | Saudi Arabia intercepts a missile or drone from the Houthis between 2026-11-01 and 2026-11-14. | Saudi Arabia intercepts a missile or drone from the Houthis with corroboration from two independent sources between 2026-11-01 and 2026-11-14. |
| KKR-20261025-10 | 25% | 2026-11-17 | disaster | The USGS records a magnitude 5.0 or greater earthquake in China between 2026-11-01 and 2026-11-14. | The USGS Significant Quakes catalog records an event with magnitude >= 5.0 in China with a date-added value between 2026-11-01 and 2026-11-14. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes above 7,623.68 on the last trading day of 2026." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The Brent crude oil price closes above 111.70 on the last trading day of 2026." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new exploited vulnerability is added to the CISA KEV catalog between 2026-11-01 and 2026-11-14." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "France passes legislation to address the budget deficit caused by the October 2026 riots." → REJECTED: the resolution names a different subject than the statement — the claim is about France and the resolution settles on French. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

4916 issued all-time across 21 forecaster arms · 3564 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 115 issued · 115 open · nothing resolved yet — this arm earns a score at its first resolution.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1727 | 1344 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 110 | 109 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 115 | 115 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 429 | 348 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*