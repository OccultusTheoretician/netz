**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091524Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-13 | 15% | 2026-10-26 | economics | The S&P 500 index closes below 7,500.00 on any trading day between 2026-10-16 and 2026-10-23. | The S&P 500 index closes below 7,500.00 on any trading day between 2026-10-16 and 2026-10-23. Reference: 7,796.60 on the packet date. |
| KKR-20261009-14 | 65% | 2026-10-26 | disaster | The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-16 and 2026-10-23. | The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-16 and 2026-10-23. |
| KKR-20261009-15 | 30% | 2026-11-16 | political | The US Senate confirms the nomination of a new Federal Reserve Board member between 2026-10-16 and 2026-11-13. | The US Senate confirms the nomination of a new Federal Reserve Board member between 2026-10-16 and 2026-11-13. |
| KKR-20261009-16 | 40% | 2026-11-02 | crime_security | The FBI announces the disruption of a major ransomware gang operating out of Eastern Europe between 2026-10-16 and 2026-10-30. | The FBI announces the disruption of a major ransomware gang operating out of Eastern Europe between 2026-10-16 and 2026-10-30. |
| KKR-20261009-17 | 55% | 2026-10-26 | economics | WTI Crude oil futures settle above $100.00 on any trading day between 2026-10-16 and 2026-10-23. | WTI Crude oil futures settle above $100.00 on any trading day between 2026-10-16 and 2026-10-23. Reference: 91.98 on the packet date. |
| KKR-20261009-18 | 20% | 2026-11-16 | military_conflict | Ethiopia and Eritrea agree to a ceasefire or de-escalation of hostilities between 2026-10-16 and 2026-11-13. | Ethiopia and Eritrea agree to a ceasefire or de-escalation of hostilities between 2026-10-16 and 2026-11-13. |
| KKR-20261009-19 | 65% | 2026-10-26 | disaster | The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-16 and 2026-10-23. | The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-16 and 2026-10-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA KEV carries a date-added value between 2026-10-10 and 2026-10-17 for a vulnerability with CVSS score 9.0 or higher." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Saudi Arabia reopens Riyadh International Airport to commercial traffic after the Houthi attack on 2026-10-09." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-09 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "A new critical vulnerability (CVSS 9.0+) is added to the CISA KEV catalog between 2026-10-10 and 2026-10-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3719 issued all-time across 21 forecaster arms · 2905 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 33 issued · 33 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1320 | 1119 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 405 | 226 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 21 | 21 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 200 | 165 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 293 | 260 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 121 | 121 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 80 | 80 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*