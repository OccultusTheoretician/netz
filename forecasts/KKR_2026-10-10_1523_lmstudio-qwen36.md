**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101523Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: lmstudio/qwen36 · 9 accepted / 1 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-08 | 15% | 2026-10-30 | cyber | The CISA KEV catalog adds a date-added value for a critical infrastructure vulnerability between 2026-10-20 and 2026-10-27 | The CISA KEV catalog carries a date-added value between 2026-10-20 and 2026-10-27 |
| KKR-20261010-09 | 25% | 2026-11-09 | economics | WTI Crude closes above 100.00 on at least one trading day between 2026-11-02 and 2026-11-06 | The closing price of WTI Crude is above 100.00 on at least one trading day between 2026-11-02 and 2026-11-06. Reference: 91.85 on the packet date |
| KKR-20261010-10 | 20% | 2026-11-20 | military | A confirmed kinetic strike hits Saudi Arabia between 2026-11-10 and 2026-11-17 | Two or more independent wire services report a confirmed kinetic strike hitting Saudi Arabia between 2026-11-10 and 2026-11-17 |
| KKR-20261010-11 | 85% | 2026-12-07 | economics | The S&P 500 index closes above 8,000 on at least one trading day between 2026-12-01 and 2026-12-04 | The closing value of the S&P 500 index is above 8,000 on at least one trading day between 2026-12-01 and 2026-12-04. Reference: 7811.54 on the packet date |
| KKR-20261010-12 | 10% | 2026-12-20 | disaster | The USGS records a magnitude 7.0 or greater earthquake between 2026-12-10 and 2026-12-17 | The USGS Significant Quakes catalog records an event with magnitude 7.0 or greater between 2026-12-10 and 2026-12-17 |
| KKR-20261010-13 | 30% | 2027-01-15 | political | The US Treasury issues an executive order imposing sanctions on the ICC between 2027-01-05 and 2027-01-12 | The Federal Register carries an executive order imposing sanctions on the ICC with a date between 2027-01-05 and 2027-01-12 |
| KKR-20261010-14 | 90% | 2027-03-11 | military | A confirmed kinetic strike hits Ukraine between 2027-03-01 and 2027-03-08 | Two or more independent wire services report a confirmed kinetic strike hitting Ukraine between 2027-03-01 and 2027-03-08 |
| KKR-20261010-15 | 10% | 2027-03-25 | disaster | The USGS records a magnitude 7.0 or greater earthquake between 2027-03-15 and 2027-03-22 | The USGS Significant Quakes catalog records an event with magnitude 7.0 or greater between 2027-03-15 and 2027-03-22 |
| KKR-20261010-16 | 30% | 2027-04-05 | political | The US Treasury issues an executive order imposing sanctions on the ICC between 2027-03-25 and 2027-04-01 | The Federal Register carries an executive order imposing sanctions on the ICC with a date between 2027-03-25 and 2027-04-01 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A major cyberattack disrupts US banking operations between 2027-02-01 and 2027-02-08" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3795 issued all-time across 21 forecaster arms · 2981 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 30 issued · 30 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1347 | 1146 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 30 | 30 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 205 | 170 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 302 | 269 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*