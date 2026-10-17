**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: lmstudio/qwen36 · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-09 | 15% | 2026-11-11 | disaster | The USGS records a magnitude 6.5 or greater earthquake between 2026-11-01 and 2026-11-08. | The USGS Significant Quakes catalog logs an event with magnitude 6.5 or higher during the event window. |
| KKR-20261017-10 | 20% | 2026-11-18 | political | France enacts a law or decree restricting protests between 2026-11-01 and 2026-11-15. | A French law or decree restricting protests is published in the Journal Officiel during the event window. |
| KKR-20261017-11 | 35% | 2026-11-18 | military/conflict | The UAE formally re-enters the Yemen conflict with military forces between 2026-11-01 and 2026-11-15. | UAE military forces are confirmed present in Yemen by at least two independent hostile sources during the event window. |
| KKR-20261017-12 | 20% | 2026-12-03 | disaster | A new major hurricane forms in the Atlantic between 2026-11-01 and 2026-11-30. | The National Hurricane Center designates a new tropical cyclone as a hurricane in the Atlantic basin during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a new critical zero-day vulnerability between 2026-10-27 and 2026-11-03." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "WTI Crude closes above 105.00 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major US bank files for bankruptcy between 2026-11-01 and 2026-11-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new critical zero-day vulnerability is exploited in the wild between 2026-11-01 and 2026-11-15." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The US Congress passes a bipartisan infrastructure bill between 2026-11-01 and 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new major cyberattack targets US critical infrastructure between 2026-11-01 and 2026-11-15." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

4331 issued all-time across 21 forecaster arms · 3220 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 75 issued · 75 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1526 | 1230 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*