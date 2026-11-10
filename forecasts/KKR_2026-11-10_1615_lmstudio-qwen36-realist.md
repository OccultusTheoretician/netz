**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-10_1613.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 3 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261110-04 | 25% | 2026-11-18 | cyber | The CISA KEV catalog carries a date-added value between 2026-11-11 and 2026-11-15 for a vulnerability with CVSS score 10.0 affecting a major cloud provider. | The CISA KEV catalog carries a date-added value between 2026-11-11 and 2026-11-15 for a vulnerability with CVSS score 10.0 affecting a major cloud provider. |
| KKR-20261110-05 | 20% | 2026-11-27 | political | Pete Hegseth resigns as Pentagon chief or is removed from office between 2026-11-17 and 2026-11-24. | Pete Hegseth resigns as Pentagon chief or is removed from office between 2026-11-17 and 2026-11-24. |
| KKR-20261110-06 | 15% | 2026-11-27 | disaster | A magnitude 6.0 or greater earthquake is recorded by the USGS in the Solomon Islands region between 2026-11-17 and 2026-11-24. | A magnitude 6.0 or greater earthquake is recorded by the USGS in the Solomon Islands region between 2026-11-17 and 2026-11-24. |
| KKR-20261110-07 | 35% | 2026-11-23 | economics | The US 10-year Treasury yield closes above 5.20 on any weekday between 2026-11-17 and 2026-11-20. | The US 10-year Treasury yield closes above 5.20 on any weekday between 2026-11-17 and 2026-11-20. |
| KKR-20261110-08 | 30% | 2026-11-27 | political | The US House of Representatives passes an impeachment resolution against Pete Hegseth between 2026-11-17 and 2026-11-24. | The US House of Representatives passes an impeachment resolution against Pete Hegseth between 2026-11-17 and 2026-11-24. |
| KKR-20261110-09 | 20% | 2026-11-27 | cyber | A major cyberattack disrupts the power grid in France between 2026-11-17 and 2026-11-24. | A major cyberattack disrupts the power grid in France between 2026-11-17 and 2026-11-24. |
| KKR-20261110-10 | 25% | 2026-11-23 | economics | Gold closes above 4,200.00 on the London Bullion Market on any weekday between 2026-11-17 and 2026-11-20. | Gold closes above 4,200.00 on the London Bullion Market on any weekday between 2026-11-17 and 2026-11-20. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes below 80.00 on the New York Mercantile Exchange on any weekday between 2026-11-17 and 2026-11-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A Grade A or B kinetic event involving drones or missiles occurs in Kyiv between 2026-11-17 and 2026-11-24." → REJECTED: cited items name France, Iran, Islamic Republic of, Israel, Palestine, State of; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Iran conducts a ballistic missile test exceeding 2,000km range between 2026-11-17 and 2026-11-24." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5535 issued all-time across 22 forecaster arms · 3813 open (1420 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 178 issued · 145 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 132 | 132 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 198 | 181 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 196 | 194 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 178 | 145 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 509 | 394 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 364 | 350 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*