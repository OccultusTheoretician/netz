**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: lmstudio/qwen36 · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-09 | 25% | 2026-11-20 | economics | WTI Crude oil closes above 100.00 USD per barrel on at least one trading day between 2026-11-16 and 2026-11-19. | The closing price of WTI Crude recorded by a major financial data provider is strictly greater than 100.00 USD. |
| KKR-20261009-10 | 15% | 2026-12-06 | military_conflict | Ethiopia and Eritrea sign a formal ceasefire agreement between 2026-12-01 and 2026-12-04. | A formal ceasefire agreement is signed by the governments of Ethiopia and Eritrea, verified by the UN or AU. |
| KKR-20261009-11 | 40% | 2026-12-21 | political | The US Senate confirms a new Treasury Secretary between 2026-12-15 and 2026-12-18. | The US Senate confirms a nominee to the position of US Secretary of the Treasury. |
| KKR-20261009-12 | 45% | 2027-04-06 | economics | The US Federal Reserve cuts the federal funds rate by at least 25 basis points between 2027-04-01 and 2027-04-04. | The Federal Reserve announces a reduction in the federal funds target rate of 25 basis points or more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a new critical zero-day vulnerability between 2026-11-01 and 2026-11-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A Category 4 or stronger hurricane makes landfall in the US between 2027-01-15 and 2027-01-18." → REJECTED: the resolution names a different subject than the statement — the claim is about Category and the resolution settles on Center, Hurricane, National. A row whose resolution checks a different fact can be scored correct while being wrong
- "The S&P 500 index closes below 7,500.00 on at least one trading day between 2027-02-01 and 2027-02-04." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major ransomware attack disrupts operations at a US hospital system between 2027-02-15 and 2027-02-18." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The European Union imposes new sanctions on Russian oil exports between 2027-03-01 and 2027-03-04." → REJECTED: cited items name China; the claim is about Russian Federation — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A new major cyber vulnerability affecting critical infrastructure is added to the CISA KEV catalog between 2027-03-15 and 2027-03-18." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3712 issued all-time across 21 forecaster arms · 2898 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 21 issued · 21 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
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