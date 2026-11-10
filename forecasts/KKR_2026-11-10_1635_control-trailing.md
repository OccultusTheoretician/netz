**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101635Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-10_1613.md · forecaster: control/trailing · 8 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261110-61 | 70% | 2026-12-01 | economics/markets | The 10-year Treasury constant maturity yield (FRED DGS10) prints at or above 5.00 percent on at least one trading day between 2026-11-12 and 2026-11-27. Reference: 4.99 percent on the packet date. | TRUE if FRED series DGS10 shows a value of 5.00 or higher for any observation dated between 2026-11-12 and 2026-11-27 inclusive. Reference level at seal: 4.99. |
| KKR-20261110-62 | 70% | 2026-12-11 | economics/markets | The Federal Open Market Committee raises the federal funds target range by at least 50 basis points at its meeting concluding 2026-12-09. | TRUE if FRED series DFEDTARU for 2026-12-10 is at least 0.50 percentage points above its value for 2026-11-10. |
| KKR-20261110-63 | 36% | 2026-11-24 | political | The US House of Representatives adopts at least one article of impeachment against Defense Secretary Pete Hegseth in a floor vote held between 2026-11-10 and 2026-11-20. | TRUE if the Clerk of the House roll call record on Congress.gov shows adoption of a resolution containing an article of impeachment against Hegseth with a vote date between 2026-11-10 and 2026-11-20. |
| KKR-20261110-64 | 56% | 2026-12-01 | cyber | CISA adds at least one Google Chromium or Chrome vulnerability to the Known Exploited Vulnerabilities catalog between 2026-11-10 and 2026-11-27. | TRUE if the CISA KEV catalog carries an entry with vendor Google and product containing Chromium or Chrome with a date-added value between 2026-11-10 and 2026-11-27 inclusive. |
| KKR-20261110-65 | 56% | 2026-12-03 | cyber | CISA adds at least one Barracuda Email Security Gateway vulnerability to the Known Exploited Vulnerabilities catalog between 2026-11-10 and 2026-12-01. | TRUE if the CISA KEV catalog carries an entry with vendor Barracuda Networks and product Email Security Gateway with a date-added value between 2026-11-10 and 2026-12-01 inclusive. |
| KKR-20261110-66 | 68% | 2026-12-15 | military/conflict | Russia and Ukraine sign a ceasefire or peace agreement between 2026-11-12 and 2026-12-11. | TRUE if Reuters and AP both report that representatives of the Russian and Ukrainian governments signed a ceasefire or peace agreement on a date between 2026-11-12 and 2026-12-11. |
| KKR-20261110-67 | 68% | 2026-12-08 | military/conflict | The United States and Iran both publicly confirm a ceasefire or cessation of hostilities that takes effect between 2026-11-12 and 2026-12-04. | TRUE if Reuters and AP both report that the US and Iranian governments each confirmed a ceasefire or cessation of hostilities with an effective date between 2026-11-12 and 2026-12-04. |
| KKR-20261110-68 | 57% | 2026-11-27 | disaster | An earthquake of magnitude 6.0 or greater occurs within 300 km of the epicenter of USGS event us7000tx16 near Lata, Solomon Islands, between 2026-11-11 and 2026-11-25. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater, origin time between 2026-11-11 and 2026-11-25 UTC, with epicenter within 300 km of event us7000tx16. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5593 issued all-time across 23 forecaster arms · 3871 open (1420 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 157 issued · 157 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 157 | 157 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 198 | 181 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 204 | 202 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 178 | 145 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 518 | 403 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 8 | 8 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 372 | 358 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*