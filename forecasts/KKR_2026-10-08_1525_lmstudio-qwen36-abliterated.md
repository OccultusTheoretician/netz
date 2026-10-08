**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081525Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-28 | 35% | 2026-11-29 | military/conflict | Russia launches a kinetic attack on a Ukrainian data center between 2026-11-20 and 2026-11-27 | At least two hostile sides report a kinetic strike on a Ukrainian data center between 2026-11-20 and 2026-11-27 |
| KKR-20261008-29 | 40% | 2026-12-15 | economics/markets | The Brent crude oil price closes above 110.00 on 2026-12-15 | The Brent crude oil closing price on 2026-12-15 is strictly greater than 110.00 |
| KKR-20261008-30 | 30% | 2026-12-29 | political | A US federal judge issues a ruling in the DNC vs Trump advertising case between 2026-12-20 and 2026-12-27 | A US federal court docket records a ruling in the DNC vs Trump advertising case between 2026-12-20 and 2026-12-27 |
| KKR-20261008-31 | 25% | 2027-01-24 | cyber | A major cyberattack on a US bank is confirmed by the CISA KEV catalog between 2027-01-15 and 2027-01-22 | The CISA KEV catalog carries a new entry for a major cyberattack on a US bank with a date-added value between 2027-01-15 and 2027-01-22 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,650.00 at the market close on 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A tropical cyclone makes landfall in the United States between 2026-11-10 and 2026-11-17" → REJECTED: the resolution names a different subject than the statement — the claim is about States, United and the resolution settles on NWS, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "A new CVE is added to the CISA KEV catalog with a date-added value between 2026-12-01 and 2026-12-08" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10-year US Treasury yield closes above 5.50 on 2027-01-10" → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "A new CVE is added to the CISA KEV catalog with a date-added value between 2027-02-01 and 2027-02-08" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 index closes below 7,650.00 at the market close on 2027-03-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3643 issued all-time across 21 forecaster arms · 2829 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 17 issued · 17 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
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