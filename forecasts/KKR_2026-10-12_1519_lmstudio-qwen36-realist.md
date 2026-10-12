**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 4 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-17 | 25% | 2026-10-23 | cyber | Between 2026-10-14 and 2026-10-21, the CISA KEV catalog carries a date-added value for a critical remote code execution vulnerability in the SonicWall SMA 1000, confirming the exploitation trend noted in item 18. | The CISA KEV catalog lists the specific SonicWall SMA 1000 flaw as an exploited vulnerability. |
| KKR-20261012-18 | 30% | 2026-10-23 | disaster | Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama, following the M7.7 event in item 22. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama. |
| KKR-20261012-19 | 20% | 2026-10-23 | political | Between 2026-10-14 and 2026-10-21, the Federal Register publishes a notice of a new US sanctions regime targeting Iranian entities related to the Strait of Hormuz, as discussed in item 70. | The Federal Register publishes a notice of a new US sanctions regime targeting Iranian entities related to the Strait of Hormuz. |
| KKR-20261012-20 | 25% | 2026-10-23 | disaster | Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Tonga, following the M5.5 event in item 36. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Tonga. |
| KKR-20261012-21 | 15% | 2026-10-23 | political | Between 2026-10-14 and 2026-10-21, the Federal Register publishes a notice of a new US sanctions regime targeting Russian entities related to the energy ceasefire, as discussed in item 34. | The Federal Register publishes a notice of a new US sanctions regime targeting Russian entities related to the energy ceasefire. |
| KKR-20261012-22 | 20% | 2026-10-23 | disaster | Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Alaska, following the M5.5 event in item 41. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Alaska. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-14 and 2026-10-21, the S&P 500 closes below 7,700.00, referencing the 7,810.08 close on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-14 and 2026-10-21, the Nasdaq closes below 26,500.00, referencing the 27,295.19 close on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-14 and 2026-10-21, the S&P 500 closes above 7,900.00, referencing the 7,810.08 close on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-14 and 2026-10-21, the Nasdaq closes above 28,000.00, referencing the 27,295.19 close on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3956 issued all-time across 21 forecaster arms · 2928 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 51 issued · 51 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1399 | 1125 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 320 | 264 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*