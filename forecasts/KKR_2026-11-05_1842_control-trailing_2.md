**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051842Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-05_1613.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261105-36 | 57% | 2026-12-07 | cyber | The CISA KEV catalog carries a date-added value between 2026-11-05 and 2026-12-04 for CVE-2026-107441, the Zyxel GS1900 out-of-bounds write flaw. | TRUE if the CISA KEV JSON feed lists CVE-2026-107441 with a dateAdded value between 2026-11-05 and 2026-12-04. |
| KKR-20261105-37 | 57% | 2026-12-07 | political | A federal court order barring construction of the Trump arch at Memorial Circle, entered between 2026-11-05 and 2026-12-04, is in force and unstayed on 2026-12-04. | TRUE if the D.D.C. docket in the arch cases before Judge Chutkan shows an injunction or restraining order against construction, entered between 2026-11-05 and 2026-12-04, in force on 2026-12-04 and not stayed on appeal. |
| KKR-20261105-38 | 57% | 2026-12-11 | economics/markets | The FOMC raises the upper bound of the federal funds target range to at least 4.25 percent at its meeting of 2026-12-08 to 2026-12-09. Reference: 4.00 percent on the packet date. | TRUE if FRED series DFEDTARU reads 4.25 or higher on 2026-12-10, following the FOMC decision of 2026-12-09. Reference: 4.00 percent on the packet date. |
| KKR-20261105-39 | 57% | 2026-12-14 | military/conflict | US forces carry out at least one air or missile strike on Iranian territory, including Iranian islands, between 2026-11-09 and 2026-12-11. | TRUE if CENTCOM or the Pentagon acknowledges, or two of Reuters, AP and BBC report citing US officials, a US strike on Iranian land or islands dated between 2026-11-09 and 2026-12-11. |
| KKR-20261105-40 | 57% | 2026-12-21 | economics/markets | The Bank of England MPC raises Bank Rate above 4.00 percent at its decision of 2026-12-17. Reference: 4.00 percent on the packet date. | TRUE if the Bank of England official Bank Rate series shows a rate above 4.00 percent effective 2026-12-17. Reference: 4.00 percent on the packet date. |
| KKR-20261105-41 | 57% | 2027-03-01 | political | The US Senate passes a joint or concurrent resolution directing the removal of US forces from hostilities against Iran between 2027-01-03 and 2027-02-26. | TRUE if a Senate.gov roll call dated between 2027-01-03 and 2027-02-26 records majority passage of a war powers resolution directing removal of US forces from hostilities against Iran. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5376 issued all-time across 22 forecaster arms · 3654 open (1220 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 87 issued · 87 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 87 | 87 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 175 | 158 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 173 | 171 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 155 | 122 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 485 | 370 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 343 | 329 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*