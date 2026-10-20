**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-18 | 25% | 2026-11-25 | disaster | A magnitude 6.0 or greater earthquake occurs in the Vanuatu Islands between 2026-11-15 and 2026-11-22. | The USGS catalog carries a date-added value for an event with magnitude >= 6.0 in the Vanuatu Islands between 2026-11-15 and 2026-11-22. |
| KKR-20261020-19 | 65% | 2026-11-11 | military | The UK government confirms the deployment of RAF Typhoon fighter jets to Saudi Arabia between 2026-11-01 and 2026-11-08. | Two distinct hostile sides (e.g., UK and Axis) confirm the deployment of RAF Typhoon jets to Saudi Arabia between 2026-11-01 and 2026-11-08. |
| KKR-20261020-20 | 55% | 2026-11-15 | political | France deploys military forces to Paris for curfews or unrest between 2026-11-05 and 2026-11-12. | Two distinct hostile sides confirm the deployment of French military forces to Paris for curfews or unrest between 2026-11-05 and 2026-11-12. |
| KKR-20261020-21 | 40% | 2026-11-23 | economics | The 10-Year US Treasury Yield closes above 5.20 on any weekday between 2026-11-16 and 2026-11-20. | The 10-Year US Treasury Yield closes above 5.20 on at least one weekday within the window. |
| KKR-20261020-22 | 60% | 2026-11-18 | military | A Houthi missile or drone strike hits a location in Saudi Arabia between 2026-11-01 and 2026-11-15. | Two distinct hostile sides confirm a Houthi missile or drone strike hits a location in Saudi Arabia between 2026-11-01 and 2026-11-15. |
| KKR-20261020-23 | 70% | 2026-11-18 | political | The US bans a major Chinese AI product (e.g., DeepSeek) across federal civilian agencies between 2026-11-01 and 2026-11-15. | The US government confirms the ban of a major Chinese AI product across federal civilian agencies between 2026-11-01 and 2026-11-15. |
| KKR-20261020-24 | 45% | 2026-11-18 | cyber | A cyberattack disrupts services for a major European bank between 2026-11-01 and 2026-11-15. | Two distinct hostile sides confirm a cyberattack disrupts services for a major European bank between 2026-11-01 and 2026-11-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,700 on any weekday between 2026-11-02 and 2026-11-06. Reference: 7,738.75 on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Brent crude oil closes above 108.00 on any weekday between 2026-11-09 and 2026-11-13." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new exploited vulnerability is added to the CISA KEV catalog between 2026-11-01 and 2026-11-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4571 issued all-time across 21 forecaster arms · 3219 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 88 issued · 88 open · nothing resolved yet — this arm earns a score at its first resolution.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1603 | 1220 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 452 | 211 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 88 | 88 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 99 | 92 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 234 | 147 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 388 | 307 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 219 | 208 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 171 | 168 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*