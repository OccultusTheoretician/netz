**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171617Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-17_1614.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261117-11 | 25% | 2026-12-03 | political | Jensen Huang resigns as Nvidia CEO by 2026-12-01 | Nvidia issues a public filing confirming the resignation of Jensen Huang as CEO on or before 2026-12-01 |
| KKR-20261117-12 | 30% | 2026-12-17 | military_conflict | The Kerch Bridge reopens fully to rail traffic by 2026-12-15 | Russian state media or the Kerch Bridge operator confirms full rail traffic restoration on the Kerch Bridge on or before 2026-12-15 |
| KKR-20261117-13 | 65% | 2026-12-12 | disaster | A magnitude 6.0 or greater earthquake occurs in Indonesia between 2026-12-01 and 2026-12-10 | The USGS catalog records an earthquake with magnitude 6.0 or greater in Indonesia between 2026-12-01 and 2026-12-10 |
| KKR-20261117-14 | 35% | 2026-12-20 | economics | Anthropic prices its IPO above $100 per share | Anthropic announces a final IPO price per share above $100 |
| KKR-20261117-15 | 55% | 2026-11-27 | political | Mary Peltola wins the Alaska Senate special election | Mary Peltola is declared the winner of the Alaska Senate special election by a major wire service by 2026-11-25 |
| KKR-20261117-16 | 45% | 2026-12-17 | economics | The 10-year US Treasury yield closes above 5.25 percent on at least one day between 2026-12-01 and 2026-12-15 | The 10-year US Treasury yield closes above 5.25 percent on at least one trading day between 2026-12-01 and 2026-12-15 |
| KKR-20261117-17 | 30% | 2026-12-17 | military_conflict | A Houthi attack disrupts shipping in the Red Sea between 2026-12-01 and 2026-12-15 | Two or more hostile sides report a Houthi attack on shipping in the Red Sea between 2026-12-01 and 2026-12-15 |
| KKR-20261117-18 | 15% | 2027-01-17 | cyber | California sues OpenAI and wins a preliminary injunction against AI agent sandbox escapes by 2027-01-15 | A California court issues a preliminary injunction against OpenAI regarding AI agent sandbox escapes on or before 2027-01-15 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes above 7,500 on at least one day between 2026-12-01 and 2026-12-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new exploited vulnerability is added to the CISA KEV catalog between 2026-12-01 and 2026-12-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5837 issued all-time across 23 forecaster arms · 4115 open (1812 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 234 issued · 232 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 231 | 214 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 234 | 232 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 219 | 186 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*