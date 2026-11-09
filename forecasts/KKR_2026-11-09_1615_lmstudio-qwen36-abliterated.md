**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-09_1611.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261109-12 | 25% | 2026-11-18 | cyber | The CISA KEV catalog records a date-added value between 2026-11-09 and 2026-11-16 for a vulnerability with CVE identifier containing SSHOLE. | The CISA KEV catalog carries a date-added value between 2026-11-09 and 2026-11-16 for a vulnerability with CVE identifier containing SSHOLE. |
| KKR-20261109-13 | 35% | 2027-01-20 | economics | The S&P 500 closes above 7,600 on at least one US trading day between 2027-01-15 and 2027-01-18. | Reference: 7,526.55 on the packet date. The S&P 500 closes above 7,600 on at least one US trading day between 2027-01-15 and 2027-01-18. |
| KKR-20261109-14 | 25% | 2027-02-06 | military | A kinetic strike by Iran or its proxies occurs in the Strait of Hormuz between 2027-02-01 and 2027-02-04. | Two hostile sides confirm a kinetic strike by Iran or its proxies in the Strait of Hormuz between 2027-02-01 and 2027-02-04. |
| KKR-20261109-15 | 60% | 2027-02-20 | crime | Russell Brand is formally convicted of rape by a UK court between 2027-02-15 and 2027-02-18. | A UK court formally convicts Russell Brand of rape between 2027-02-15 and 2027-02-18. |
| KKR-20261109-16 | 70% | 2027-03-06 | political | The US imposes sanctions on MEXC crypto exchange between 2027-03-01 and 2027-03-04. | The US imposes sanctions on MEXC crypto exchange between 2027-03-01 and 2027-03-04. |
| KKR-20261109-17 | 25% | 2027-04-20 | military | A ceasefire or major offensive operation in Ukraine is confirmed by two hostile sides between 2027-04-15 and 2027-04-18. | Two hostile sides confirm a ceasefire or major offensive operation in Ukraine between 2027-04-15 and 2027-04-18. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes below 86.00 on at least one US trading day between 2026-12-01 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A magnitude 6.0 or greater earthquake is recorded by USGS between 2026-12-15 and 2026-12-18." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major cyberattack on US critical infrastructure is confirmed by CISA between 2027-03-15 and 2027-03-18." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Gold closes above 4,200 on at least one US trading day between 2027-04-01 and 2027-04-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5491 issued all-time across 22 forecaster arms · 3769 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 196 issued · 194 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 115 | 115 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 195 | 178 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 196 | 194 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 171 | 138 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 500 | 385 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 356 | 342 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*