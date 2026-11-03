**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031616Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-03_1614.md · forecaster: lmstudio/qwen36-realist · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261103-07 | 30% | 2026-11-16 | political | The US imposes new sanctions on Iran's Qeshm Island. | The US Treasury OFAC publishes a notice of sanctions targeting entities or assets on Qeshm Island. |
| KKR-20261103-08 | 25% | 2026-11-16 | military/conflict | A new Russian offensive operation begins in the Kherson region. | Two hostile sides report a new Russian offensive operation in the Kherson region between 2026-11-06 and 2026-11-13. |
| KKR-20261103-09 | 25% | 2026-11-16 | economics/markets | The Brent crude oil price rises above 110 USD per barrel. | Brent crude oil price exceeds 110 USD per barrel. |
| KKR-20261103-10 | 30% | 2026-11-16 | cyber | A new cyberattack disrupts supermarket freezers across Europe. | Two independent sources report a new cyberattack disrupting supermarket freezers across Europe between 2026-11-06 and 2026-11-13. |
| KKR-20261103-11 | 30% | 2026-11-16 | disaster | A new forest fire is confirmed by GDACS in South Sudan. | GDACS Alerts carries an eventid for a new forest fire in South Sudan. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,450 on 2026-11-06, a decline of more than 1.8% from the 7,586.77 reference level on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The US Congress passes a continuing resolution to fund the federal government through at least 2027-01-30." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new vulnerability is added to the CISA KEV catalog with a date-added value between 2026-11-06 and 2026-11-13." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A forest fire in Botswana is confirmed by GDACS with an eventid between 1033431 and 1034000." → REJECTED: the resolution names a different subject than the statement — the claim is about Botswana, GDACS and the resolution settles on Alerts, GDACS. A row whose resolution checks a different fact can be scored correct while being wrong
- "The US stops paying aid to Israel." → REJECTED: statement too thin to adjudicate (34 chars) — a third party reading the statement alone must be able to say what was claimed

## III. LEDGER STANDING

5284 issued all-time across 22 forecaster arms · 3562 open (843 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 149 issued · 116 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 59 | 59 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 161 | 144 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 157 | 155 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 149 | 116 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 327 | 313 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*