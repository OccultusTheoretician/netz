**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 282353Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-28_1515.md · forecaster: control/trailing · 5 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261028-29 | 57% | 2026-12-11 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting concluding on 2026-12-09. | TRUE if the FOMC statement released on 2026-12-09 announces a higher target range, equivalently FRED series DFEDTARU for 2026-12-10 exceeds its 2026-12-08 value; FALSE if the range is held or cut. |
| KKR-20261028-30 | 57% | 2027-01-13 | economics/markets | WTI crude (FRED series DCOILWTICO) records a daily value below 90.00 dollars per barrel on at least one day between 2026-11-02 and 2026-12-31. Reference: WTI 102.60 on the packet date. | TRUE if any DCOILWTICO daily observation dated 2026-11-02 through 2026-12-31, as published on FRED at the deadline, is below 90.00; FALSE otherwise. Reference: 102.60 dollars per barrel at seal. |
| KKR-20261028-31 | 57% | 2026-12-15 | cyber | CISA adds at least one Oracle E-Business Suite vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-28 and 2026-12-11. | TRUE if the CISA KEV JSON feed, fetched on the deadline, holds an entry with vendorProject Oracle, product E-Business Suite, and dateAdded from 2026-10-28 through 2026-12-11 inclusive; FALSE otherwise. |
| KKR-20261028-32 | 57% | 2027-01-15 | cyber | A University of New Mexico health entity submits a HIPAA breach report to the HHS Office for Civil Rights with a breach submission date between 2026-10-28 and 2027-01-08. | TRUE if the HHS OCR breach portal, checked on the deadline, lists a covered entity whose name contains UNM or University of New Mexico with a breach submission date between 2026-10-28 and 2027-01-08; FALSE otherwise. |
| KKR-20261028-33 | 57% | 2026-11-24 | political | No candidate wins more than 50 percent in the 2026-11-03 Georgia US Senate general election, sending the race to a runoff. | TRUE if Georgia Secretary of State results (certified, or final unofficial if certification is pending) for the 2026-11-03 US Senate general election show no candidate above 50 percent; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5113 issued all-time across 22 forecaster arms · 3391 open (448 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 10 issued · 10 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 10 | 10 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 132 | 115 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 133 | 131 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 129 | 96 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 460 | 345 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 291 | 277 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*