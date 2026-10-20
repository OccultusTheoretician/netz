**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-08 | 25% | 2026-11-05 | military/conflict | Between 2026-10-21 and 2026-10-27, at least one confirmed F-35 aircraft will be reported as involved in a military operation in the Iran Theatre. | At least one report from a cross-bias confirmed source (Grade A or B) will state that an F-35 aircraft was used in a military operation in the Iran Theatre during the event window. |
| KKR-20261020-09 | 35% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-27, a cyberattack exploiting the ClickFix platform will be confirmed by at least two independent sources across hostile sides. | At least two reports from distinct channels across two hostile sides (RU, IL, UA, WEST, AXIS) will confirm a cyberattack using the ClickFix platform during the event window. |
| KKR-20261020-10 | 30% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-27, a cyberattack on a critical infrastructure provider will result in a service disruption affecting at least 100,000 users in the US or Europe. | At least two independent sources (e.g., BleepingComputer, The Hacker News) will confirm a cyberattack on a critical infrastructure provider causing service disruption to 100,000 or more users in the US or Europe during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-21, the CISA KEV catalog will include at least one new exploited vulnerability with a date-added value between 2026-10-20 and 202" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-22, the S&P 500 will close below 7,700 points at the end of the trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-21 and 2026-10-27, at least one major offensive operation will be confirmed in the Donbas region by cross-bias reporting." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-23, the 10-year US Treasury yield will close above 5.20 percent." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-21 and 2026-10-27, a military strike in Gaza City will result in at least 15 civilian casualties, confirmed by cross-bias re" → REJECTED: cited items name Australia, United States; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-27, a natural disaster (earthquake, flood, or wildfire) will be confirmed by GDACS Alerts with a severity lev" → REJECTED: cited items name Botswana, Cameroon, China, Mali, Nigeria, Thailand; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-27, a political leader in a NATO country will be formally charged with a criminal offense related to foreign " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4557 issued all-time across 21 forecaster arms · 3205 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 234 issued · 147 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

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
| lmstudio/qwen36-abliterated | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 92 | 85 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
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