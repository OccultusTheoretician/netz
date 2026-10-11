**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111526Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-19 | 25% | 2026-10-22 | military_conflict | Houthi forces launch a kinetic strike on Riyadh airport between 2026-10-12 and 2026-10-19 | Al Jazeera or BBC World reports a confirmed Houthi strike on Riyadh airport within the window |
| KKR-20261011-20 | 20% | 2026-10-22 | disaster | A magnitude 6.0 or greater earthquake occurs in Panama between 2026-10-12 and 2026-10-19 | USGS Significant Quakes reports a magnitude 6.0 or greater earthquake in Panama between 2026-10-12 and 2026-10-19 |
| KKR-20261011-21 | 65% | 2026-10-22 | political | Pope Leo XIV undergoes lung surgery between 2026-10-12 and 2026-10-19 | NPR News or BBC World reports that Pope Leo XIV has undergone lung surgery between 2026-10-12 and 2026-10-19 |
| KKR-20261011-22 | 35% | 2026-10-22 | political | Polish police confirm a plot to assassinate Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19 | Al Jazeera or Guardian World reports that Polish police have confirmed a plot to assassinate Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19 |
| KKR-20261011-23 | 40% | 2026-10-22 | political | A migrant boat capsizes off Djibouti with at least 100 dead between 2026-10-12 and 2026-10-19 | Al Jazeera or BBC World reports a migrant boat capsizing off Djibouti with at least 100 dead between 2026-10-12 and 2026-10-19 |
| KKR-20261011-24 | 55% | 2026-10-22 | cyber | Nippon Columbia malware incident exposes at least 8 million records between 2026-10-12 and 2026-10-19 | BleepingComputer reports that the Nippon Columbia malware incident has exposed at least 8 million records between 2026-10-12 and 2026-10-19 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA KEV catalog adds a new exploited vulnerability between 2026-10-12 and 2026-10-19" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "WTI Crude settles above 95.00 on at least one trading day between 2026-10-12 and 2026-10-19" → REJECTED: cited items name Australia, Panama; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A forest fire is reported in Angola between 2026-10-12 and 2026-10-19" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "The S&P 500 closes above 7,900 on at least one trading day between 2026-10-12 and 2026-10-19" → REJECTED: cited items name Panama, Russian Federation, Ukraine; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3880 issued all-time across 21 forecaster arms · 3066 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 33 issued · 33 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1372 | 1171 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 312 | 279 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*