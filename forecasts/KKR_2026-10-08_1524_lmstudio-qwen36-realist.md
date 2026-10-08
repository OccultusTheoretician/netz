**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081524Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 1 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-21 | 30% | 2026-10-19 | economics/markets | The US Treasury 10-year yield closes above 5.50 percent on any US trading day between 2026-10-13 and 2026-10-16. | The closing yield of the US Treasury 10-year note exceeds 5.50 percent on the specified dates. |
| KKR-20261008-22 | 25% | 2026-10-23 | military/conflict | A maritime vessel is hit by projectiles or mines in the Strait of Hormuz or Gulf of Oman between 2026-10-13 and 2026-10-20. | A vessel is confirmed hit by projectiles or mines in the Strait of Hormuz or Gulf of Oman. |
| KKR-20261008-23 | 20% | 2026-10-25 | cyber | The CISA KEV catalog adds an entry for a critical vulnerability in the FortiGate VPN appliance between 2026-10-15 and 2026-10-22. | The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-22 for a FortiGate vulnerability. |
| KKR-20261008-24 | 15% | 2026-10-25 | disaster | A magnitude 6.0 or greater earthquake occurs in the Philippines between 2026-10-15 and 2026-10-22. | The USGS Significant Quakes catalog records an event with magnitude 6.0 or greater in the Philippines. |
| KKR-20261008-25 | 35% | 2026-10-25 | political | South Korea formally recalls its ambassador to Ukraine from duty between 2026-10-15 and 2026-10-22. | The South Korean Ministry of Foreign Affairs formally recalls its ambassador to Ukraine from duty. |
| KKR-20261008-26 | 10% | 2026-10-25 | crime/security | The owner of the Empire cybercrime market is sentenced to prison between 2026-10-15 and 2026-10-22. | A court docket records a prison sentence for the owner of the Empire cybercrime market. |
| KKR-20261008-27 | 15% | 2026-10-25 | political | The UK House of Commons passes a vote to join the GCAP fighter jet programme between 2026-10-15 and 2026-10-22. | The UK House of Commons passes a vote to join the GCAP fighter jet programme. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes above $100.00 per barrel on any US trading day between 2026-10-13 and 2026-10-16." → REJECTED: cited items name Iran, Islamic Republic of, United Kingdom; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3639 issued all-time across 21 forecaster arms · 2825 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 26 issued · 26 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1292 | 1091 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*