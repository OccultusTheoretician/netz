**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 3 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-11 | 30% | 2026-11-09 | economics | WTI Crude closes below 90.00 on the NYMEX between 2026-11-02 and 2026-11-06. | Reference: 95.81 on the packet date. WTI Crude closes below 90.00 on the NYMEX on any trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261020-12 | 20% | 2026-11-19 | political | France deploys more than 10,000 police or military personnel to Paris between 2026-11-13 and 2026-11-17. | French government reports or wire services confirm the deployment of more than 10,000 police or military personnel to Paris between 2026-11-13 and 2026-11-17. |
| KKR-20261020-13 | 15% | 2026-11-16 | disaster | A magnitude 6.0 or greater earthquake occurs in the Vanuatu Islands between 2026-11-10 and 2026-11-14. | The USGS Significant Quakes catalog records an event with a magnitude of 6.0 or greater in the Vanuatu Islands between 2026-11-10 and 2026-11-14. |
| KKR-20261020-14 | 10% | 2026-11-26 | military | The UK deploys more than 100 Typhoon fighter jets to Saudi Arabia between 2026-11-20 and 2026-11-24. | UK government reports or wire services confirm the deployment of more than 100 Typhoon fighter jets to Saudi Arabia between 2026-11-20 and 2026-11-24. |
| KKR-20261020-15 | 15% | 2026-12-07 | disaster | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in the Vanuatu Islands between 2026-12-01 and 2026-12-05. | The USGS Significant Quakes catalog records an event with a magnitude of 6.0 or greater in the Vanuatu Islands between 2026-12-01 and 2026-12-05. |
| KKR-20261020-16 | 15% | 2027-01-07 | disaster | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in the Vanuatu Islands between 2027-01-01 and 2027-01-05. | The USGS Significant Quakes catalog records an event with a magnitude of 6.0 or greater in the Vanuatu Islands between 2027-01-01 and 2027-01-05. |
| KKR-20261020-17 | 15% | 2027-02-07 | disaster | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in the Vanuatu Islands between 2027-02-01 and 2027-02-05. | The USGS Significant Quakes catalog records an event with a magnitude of 6.0 or greater in the Vanuatu Islands between 2027-02-01 and 2027-02-05. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a newly exploited vulnerability between 2026-10-27 and 2026-11-03." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes above 8,000 on the NYSE between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10Y US Treasury Yield closes above 5.50 on the NYSE between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4564 issued all-time across 21 forecaster arms · 3212 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 99 issued · 92 open · 7 resolved · 3 hits / 4 misses · **Brier 0.297** against its own base rate 42.9% (climatological 0.245) · **skill -0.215** · under 30 resolved, this is noise.

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