**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-24_1611.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261124-04 | 25% | 2026-12-21 | disaster | A magnitude 6.0 or greater earthquake occurs in the Vanuatu region between 2026-12-15 and 2026-12-18 | The USGS catalog records a seismic event with magnitude >= 6.0 in the Vanuatu region with a date-added value between 2026-12-15 and 2026-12-18. |
| KKR-20261124-05 | 40% | 2026-12-26 | cyber | CISA adds a new exploited vulnerability to the KEV catalog between 2026-12-20 and 2026-12-23 | The CISA KEV catalog carries a date-added value between 2026-12-20 and 2026-12-23 for a vulnerability marked as exploited. |
| KKR-20261124-06 | 20% | 2026-12-16 | political | Iran imposes a new export restriction on a critical medicine or medical supply between 2026-12-10 and 2026-12-13 | Two wire services (e.g., Reuters, AP) report an Iranian government decree or order restricting the export of a specific medicine or medical supply between 2026-12-10 and 2026-12-13. |
| KKR-20261124-07 | 35% | 2026-12-14 | economics/markets | Anthropic stock closes below $80 on any weekday between 2026-12-07 and 2026-12-10 | The closing price of Anthropic stock is strictly less than $80 on the final trading day of the window. |
| KKR-20261124-08 | 45% | 2026-12-31 | military/conflict | A Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden between 2026-12-25 and 2026-12-28 | Two wire services report a Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden between 2026-12-25 and 2026-12-28. |
| KKR-20261124-09 | 50% | 2026-12-24 | military/conflict | Russia conducts a missile or drone strike on a Ukrainian energy facility between 2026-12-18 and 2026-12-21 | Two wire services report a Russian missile or drone strike on a Ukrainian energy facility between 2026-12-18 and 2026-12-21. |
| KKR-20261124-10 | 15% | 2027-01-05 | disaster | A Category 3 or higher hurricane makes landfall in the United States between 2026-12-28 and 2027-01-02 | The NHC or NWS records a hurricane of Category 3 or higher making landfall in the United States between 2026-12-28 and 2027-01-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,100 on any weekday between 2026-12-01 and 2026-12-04" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The 10-Year US Treasury Yield closes above 5.00% on any weekday between 2026-12-14 and 2026-12-17" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major data breach is confirmed by a US company with over 1 million affected users between 2026-12-05 and 2026-12-08" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5953 issued all-time across 23 forecaster arms · 4231 open (2196 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 274 issued · 272 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 270 | 253 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 274 | 272 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 256 | 223 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*