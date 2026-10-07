**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071526Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: lmstudio/qwen36-abliterated · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-20 | 30% | 2026-11-24 | disaster | A forest fire notification is catalogued in the GDACS Alerts database with an event type of WF between 2026-11-15 and 2026-11-21. | The GDACS Alerts database contains a record with eventtype WF and a date-added value falling between 2026-11-15 and 2026-11-21. |
| KKR-20261007-21 | 20% | 2026-12-14 | economics | The 10-year US Treasury yield closes above 5.50 percent on any trading day between 2026-12-07 and 2026-12-11. Reference: 5.30 on the packet date. | The closing yield of the 10-year US Treasury note is strictly greater than 5.50 on at least one trading day within the event window. |
| KKR-20261007-22 | 25% | 2026-11-29 | military | An attack jet is photographed at a Chinese military facility in Laos between 2026-11-20 and 2026-11-26. | A public report confirms the presence of an attack jet at a Chinese military facility in Laos on at least one day between 2026-11-20 and 2026-11-26. |
| KKR-20261007-23 | 30% | 2027-01-06 | disaster | A forest fire notification is catalogued in the GDACS Alerts database with an event type of WF between 2026-12-28 and 2027-01-03. | The GDACS Alerts database contains a record with eventtype WF and a date-added value falling between 2026-12-28 and 2027-01-03. |
| KKR-20261007-24 | 25% | 2027-01-13 | military | An attack jet is photographed at a Chinese military facility in Laos between 2027-01-04 and 2027-01-10. | A public report confirms the presence of an attack jet at a Chinese military facility in Laos on at least one day between 2027-01-04 and 2027-01-10. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,650.00 on any trading day between 2026-11-02 and 2026-11-06. Reference: 7,777.51 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new vulnerability is added to the CISA KEV catalog with a date-added value between 2026-11-09 and 2026-11-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Bitcoin closes below $78,000 on any trading day between 2026-12-14 and 2026-12-18. Reference: $82,948 on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new vulnerability is added to the CISA KEV catalog with a date-added value between 2026-12-21 and 2026-12-27." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 index closes below 7,650.00 on any trading day between 2026-12-28 and 2027-01-01. Reference: 7,777.51 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3558 issued all-time across 21 forecaster arms · 2744 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 13 issued · 13 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1265 | 1064 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*