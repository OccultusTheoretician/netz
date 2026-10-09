**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091525Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-20 | 25% | 2026-11-10 | disaster | The USGS catalog records an earthquake with magnitude 6.0 or greater between 2026-11-01 and 2026-11-07. | The USGS Significant Quakes feed carries a date-added value between 2026-11-01 and 2026-11-07 for an event with magnitude 6.0 or greater. |
| KKR-20261009-21 | 35% | 2026-12-10 | economics | The S&P 500 index closes below 7,600.00 on at least one trading day between 2026-12-01 and 2026-12-07. | Reference: 7,796.60 on the packet date. The S&P 500 index closes below 7,600.00 on at least one trading day between 2026-12-01 and 2026-12-07. |
| KKR-20261009-22 | 20% | 2026-11-10 | military | Ethiopia and Eritrea sign a ceasefire agreement between 2026-11-01 and 2026-11-07. | A ceasefire agreement between Ethiopia and Eritrea is signed and reported by two independent wire services between 2026-11-01 and 2026-11-07. |
| KKR-20261009-23 | 25% | 2026-11-24 | political | The US Supreme Court grants certiorari in a case involving the ICC between 2026-11-15 and 2026-11-21. | The US Supreme Court grants certiorari in a case involving the ICC and the order is filed in the public docket between 2026-11-15 and 2026-11-21. |
| KKR-20261009-24 | 30% | 2026-10-29 | disaster | A hurricane makes landfall in the United States between 2026-10-20 and 2026-10-26. | A hurricane makes landfall in the United States as confirmed by the NWS between 2026-10-20 and 2026-10-26. |
| KKR-20261009-25 | 45% | 2026-11-10 | cyber | The FBI announces the indictment of a Chinese national for critical infrastructure hacking between 2026-11-01 and 2026-11-07. | The FBI announces the indictment of a Chinese national for critical infrastructure hacking and the indictment is filed in the public docket between 2026-11-01 and 2026-11-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog records a new exploited vulnerability between 2026-11-15 and 2026-11-21." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10-year US Treasury yield closes above 5.50 percent on at least one trading day between 2026-12-15 and 2026-12-21." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Brent crude oil closes above 110.00 on at least one trading day between 2026-12-01 and 2026-12-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major cyberattack disrupts at least one US hospital between 2026-12-15 and 2026-12-21." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3725 issued all-time across 21 forecaster arms · 2911 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 23 issued · 23 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
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