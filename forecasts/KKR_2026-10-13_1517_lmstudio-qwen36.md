**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-09 | 85% | 2026-10-22 | political | Kimberly Guilfoyle resigns as US Ambassador to Greece between 2026-10-13 and 2026-10-20 | Kimberly Guilfoyle submits her resignation as US Ambassador to Greece between 2026-10-13 and 2026-10-20 |
| KKR-20261013-10 | 45% | 2026-10-28 | economics | WTI Crude closes above 100 USD per barrel on at least one trading day between 2026-10-20 and 2026-10-27 | WTI Crude closes above 100 USD per barrel on at least one trading day between 2026-10-20 and 2026-10-27 |
| KKR-20261013-11 | 25% | 2026-10-22 | disaster | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2026-10-13 and 2026-10-20 | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2026-10-13 and 2026-10-20 |
| KKR-20261013-12 | 30% | 2026-10-22 | military | Yemeni government forces advance into or capture Taiz between 2026-10-13 and 2026-10-20 | Yemeni government forces advance into or capture Taiz between 2026-10-13 and 2026-10-20 |
| KKR-20261013-13 | 65% | 2026-10-28 | political | The Federal Register publishes a notice of termination for Ambassador Kimberly Guilfoyle between 2026-10-20 and 2026-10-27 | The Federal Register publishes a notice of termination for Ambassador Kimberly Guilfoyle between 2026-10-20 and 2026-10-27 |
| KKR-20261013-14 | 15% | 2026-10-28 | disaster | The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2026-10-20 and 2026-10-27 | The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2026-10-20 and 2026-10-27 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-104935 between 2026-10-13 and 2026-10-20" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, already inside the claimed window 2026-10-13..2026-10-20
- "The S&P 500 closes below 7,500 on at least one trading day between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The CISA KEV catalog carries a date-added value for a new critical vulnerability between 2026-10-20 and 2026-10-27" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Pakistan lifts emergency rule in its former prime minister's stronghold between 2026-10-13 and 2026-10-20" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

4028 issued all-time across 21 forecaster arms · 2917 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 49 issued · 49 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1128 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 328 | 270 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*