**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271614Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-27_1612.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261127-01 | 25% | 2026-12-07 | cyber | The CISA KEV catalog records a date-added value between 2026-11-27 and 2026-12-04 for a vulnerability exploited in attacks on SAP systems. | The CISA KEV catalog carries a date-added value between 2026-11-27 and 2026-12-04 for a vulnerability exploited in attacks on SAP systems. |
| KKR-20261127-02 | 20% | 2026-12-11 | disaster | A forest fire notification is issued by GDACS for an event in South Sudan between 2026-12-01 and 2026-12-08. | GDACS issues a forest fire notification for an event in South Sudan between 2026-12-01 and 2026-12-08. |
| KKR-20261127-03 | 45% | 2026-12-11 | political | The UK Department for Work and Pensions confirms a cyber incident caused a complete outage of pension payment systems between 2026-12-01 and 2026-12-08. | The UK Department for Work and Pensions confirms a cyber incident caused a complete outage of pension payment systems between 2026-12-01 and 2026-12-08. |
| KKR-20261127-04 | 35% | 2026-12-18 | economics | The European Central Bank announces a rate cut of at least 25 basis points between 2026-12-01 and 2026-12-15. | The European Central Bank announces a rate cut of at least 25 basis points between 2026-12-01 and 2026-12-15. |
| KKR-20261127-05 | 15% | 2026-12-11 | disaster | A wildfire is confirmed by GDACS in the Central African Republic between 2026-12-01 and 2026-12-08. | GDACS confirms a wildfire in the Central African Republic between 2026-12-01 and 2026-12-08. |
| KKR-20261127-06 | 50% | 2026-12-11 | cyber | The US Air Force confirms a breach of its cloud computing platform between 2026-12-01 and 2026-12-08. | The US Air Force confirms a breach of its cloud computing platform between 2026-12-01 and 2026-12-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes below 80.00 USD on a weekday between 2026-12-01 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone strike is reported in the Kyiv region of Ukraine between 2026-12-01 and 2026-12-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A ceasefire is implemented in the Gaza Strip between 2026-12-01 and 2026-12-15." → REJECTED: cited items name Brazil, United Kingdom; the claim is about Palestine, State of — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The S&P 500 closes above 7,500 on a weekday between 2026-12-01 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5993 issued all-time across 23 forecaster arms · 4271 open (2360 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 288 issued · 271 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 288 | 271 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 287 | 285 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 265 | 232 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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