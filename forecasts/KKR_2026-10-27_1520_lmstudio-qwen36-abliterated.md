**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-27_1516.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261027-14 | 30% | 2026-11-06 | cyber | CISA KEV catalog adds an exploited vulnerability with date-added between 2026-11-01 and 2026-11-04 | CISA KEV catalog carries a date-added value between 2026-11-01 and 2026-11-04 |
| KKR-20261027-15 | 25% | 2026-11-09 | economics | WTI Crude closes below 98.00 on at least one trading day between 2026-11-02 and 2026-11-06 | Reference: 100.01 on the packet date. WTI Crude settlement price is below 98.00 on at least one trading day between 2026-11-02 and 2026-11-06 |
| KKR-20261027-16 | 25% | 2026-11-10 | disaster | A magnitude 5.0 or greater earthquake occurs in the Pacific Ring of Fire between 2026-11-01 and 2026-11-08 | USGS reports an earthquake with magnitude 5.0 or greater in the Pacific Ring of Fire with event date between 2026-11-01 and 2026-11-08 |
| KKR-20261027-17 | 20% | 2026-11-11 | political | A US federal court docket records a new indictment against a former US official between 2026-11-02 and 2026-11-09 | A US federal court docket records a new indictment against a former US official with filing date between 2026-11-02 and 2026-11-09 |
| KKR-20261027-18 | 25% | 2026-11-09 | economics | The 10Y US Treasury Yield closes above 5.10 on at least one trading day between 2026-11-02 and 2026-11-06 | Reference: 4.98 on the packet date. 10Y US Treasury Yield closing value is above 5.10 on at least one trading day between 2026-11-02 and 2026-11-06 |
| KKR-20261027-19 | 30% | 2026-11-10 | cyber | A cyberattack is confirmed by CISA KEV as actively exploited between 2026-11-01 and 2026-11-08 | CISA KEV catalog carries an entry with active_exploitation true and date-added between 2026-11-01 and 2026-11-08 |
| KKR-20261027-20 | 20% | 2026-11-10 | disaster | A new Ebola case is confirmed in DR Congo between 2026-11-01 and 2026-11-08 | WHO or Ministry of Health DR Congo confirms at least one new Ebola case with report date between 2026-11-01 and 2026-11-08 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A forest fire notification is issued by GDACS for a country in Africa between 2026-11-01 and 2026-11-08" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "The S&P 500 closes above 7,800 on at least one trading day between 2026-11-02 and 2026-11-06" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A drone or missile attack occurs in the Russia-Ukraine theatre between 2026-11-01 and 2026-11-08" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5044 issued all-time across 21 forecaster arms · 3322 open (400 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 130 issued · 128 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1770 | 1261 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 125 | 108 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 130 | 128 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 126 | 93 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 447 | 332 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 276 | 262 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*