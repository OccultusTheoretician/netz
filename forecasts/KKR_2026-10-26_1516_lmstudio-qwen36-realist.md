**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 261516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-26_1513.md · forecaster: lmstudio/qwen36-realist · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261026-07 | 30% | 2026-11-09 | economics | WTI Crude closes above 115.00 on a weekday between 2026-11-02 and 2026-11-06. | WTI Crude closes above 115.00 on a weekday between 2026-11-02 and 2026-11-06. Reference: 100.93 on the packet date. |
| KKR-20261026-08 | 20% | 2026-11-16 | disaster | The USGS catalog records an earthquake of Magnitude 6.0 or greater in the Bonin Islands region between 2026-11-01 and 2026-11-14. | The USGS catalog records an earthquake of Magnitude 6.0 or greater in the Bonin Islands region between 2026-11-01 and 2026-11-14. |
| KKR-20261026-09 | 25% | 2026-11-16 | military | Saudi Arabia and Iran sign a bilateral security agreement to reduce tensions in the Red Sea between 2026-11-01 and 2026-11-14. | Saudi Arabia and Iran sign a bilateral security agreement to reduce tensions in the Red Sea between 2026-11-01 and 2026-11-14. |
| KKR-20261026-10 | 35% | 2026-11-09 | economics | The S&P 500 closes below 7,500 on a weekday between 2026-11-02 and 2026-11-06. | The S&P 500 closes below 7,500 on a weekday between 2026-11-02 and 2026-11-06. Reference: 7695.16 on the packet date. |
| KKR-20261026-11 | 20% | 2026-11-16 | military | A major cyberattack disrupts power generation in Sudan between 2026-11-01 and 2026-11-14. | A major cyberattack disrupts power generation in Sudan between 2026-11-01 and 2026-11-14. |
| KKR-20261026-12 | 25% | 2026-11-16 | economics | The European Central Bank cuts its main refinancing rate by at least 25 basis points between 2026-11-01 and 2026-11-14. | The European Central Bank cuts its main refinancing rate by at least 25 basis points between 2026-11-01 and 2026-11-14. |
| KKR-20261026-13 | 30% | 2026-11-16 | disaster | A forest fire notification is issued by GDACS for a major population center in Indonesia between 2026-11-01 and 2026-11-14. | A forest fire notification is issued by GDACS for a major population center in Indonesia between 2026-11-01 and 2026-11-14. |
| KKR-20261026-14 | 35% | 2026-11-16 | political | The UK government announces a new policy to incentivize carmakers to turn EVs into grid storage between 2026-11-01 and 2026-11-14. | The UK government announces a new policy to incentivize carmakers to turn EVs into grid storage between 2026-11-01 and 2026-11-14. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a critical infrastructure vulnerability between 2026-11-01 and 2026-11-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Federal Register publishes a final rule implementing new export controls on AI chips between 2026-11-02 and 2026-11-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4978 issued all-time across 21 forecaster arms · 3626 open (709 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 122 issued · 115 open · 7 resolved · 3 hits / 4 misses · **Brier 0.297** against its own base rate 42.9% (climatological 0.245) · **skill -0.215** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1751 | 1368 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 116 | 115 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 115 | 115 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 122 | 115 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 437 | 356 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 267 | 256 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 222 | 219 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*