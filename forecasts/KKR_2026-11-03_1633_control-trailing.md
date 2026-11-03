**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031633Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-03_1614.md · forecaster: control/trailing · 7 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261103-23 | 57% | 2027-01-20 | political | A Democratic member is elected Speaker of the 120th Congress in a House roll call held between 2027-01-03 and 2027-01-15. | True if the Clerk of the House roll call held between 2027-01-03 and 2027-01-15 records a Democratic member elected Speaker of the 120th Congress. |
| KKR-20261103-24 | 57% | 2027-01-20 | political | Democrats and independents caucusing with them hold at least 51 US Senate seats between 2027-01-03 and 2027-01-15. | True if the Senate.gov party division record shows at least 51 Democrats plus caucusing independents at any point between 2027-01-03 and 2027-01-15. |
| KKR-20261103-25 | 57% | 2026-11-24 | military_conflict | Russian and Ukrainian delegations attend US-mediated talks in Abu Dhabi between 2026-11-04 and 2026-11-20. | True if Reuters and AP both report Russian and Ukrainian delegations attended US-mediated talks in Abu Dhabi held between 2026-11-04 and 2026-11-20. |
| KKR-20261103-26 | 57% | 2026-12-22 | economics/markets | ICE Brent front-month futures settle above 100.00 dollars per barrel on 2026-12-18. Reference: 103.31 dollars on the packet date. | True if the ICE Brent front-month settlement on 2026-12-18 is above 100.00 dollars. Reference: 103.31 dollars on 2026-11-03. |
| KKR-20261103-27 | 57% | 2027-01-05 | economics/markets | The S&P 500 closes above 7,800.00 on 2026-12-31. Reference: 7,586.77 on the packet date. | True if the FRED SP500 series value for 2026-12-31 is above 7,800.00. Reference: 7,586.77 on 2026-11-03. |
| KKR-20261103-28 | 57% | 2026-12-08 | cyber | CISA adds a Siemens IoT2050 vulnerability to the Known Exploited Vulnerabilities catalog between 2026-11-04 and 2026-12-04. | True if the CISA KEV catalog carries a Siemens entry naming IoT2050 with a date-added value between 2026-11-04 and 2026-12-04. |
| KKR-20261103-29 | 57% | 2026-12-18 | disaster | PHIVOLCS raises Mayon Volcano to Alert Level 4 or higher between 2026-11-04 and 2026-12-15. | True if a PHIVOLCS Mayon bulletin issued between 2026-11-04 and 2026-12-15 raises the volcano to Alert Level 4 or 5. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5302 issued all-time across 22 forecaster arms · 3580 open (843 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 66 issued · 66 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 66 | 66 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 161 | 144 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 161 | 159 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 149 | 116 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 334 | 320 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*