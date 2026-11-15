**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-15_1612.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261115-11 | 45% | 2026-11-25 | military_conflict | Iran launches a drone or missile attack on a US military base in Bahrain between 2026-11-16 and 2026-11-23 | The event is confirmed if two or more wire services (e.g., Reuters, AP, AFP) report a kinetic attack on a US base in Bahrain within the window. |
| KKR-20261115-12 | 30% | 2026-11-25 | disaster | A magnitude 5.0 or greater earthquake occurs in the Philippines between 2026-11-16 and 2026-11-23 | The USGS reports an earthquake with magnitude 5.0 or greater in the Philippines with an origin time between 2026-11-16 and 2026-11-23. |
| KKR-20261115-13 | 35% | 2026-11-25 | economics | A major US airline announces a pilot strike between 2026-11-16 and 2026-11-23 | A major US airline (e.g., Delta, United, American) announces a pilot strike that will begin within 30 days, reported by two wire services. |
| KKR-20261115-14 | 40% | 2026-11-24 | economics | The S&P 500 index closes below 7,400 on at least one trading day between 2026-11-16 and 2026-11-23 | Reference: 7,561.67 on the packet date. The S&P 500 close is below 7,400 on any day between 2026-11-16 and 2026-11-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Brent crude oil price closes above 96.00 USD per barrel on at least one trading day between 2026-11-16 and 2026-11-23" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new vulnerability is added to the CISA KEV catalog with a date-added value between 2026-11-16 and 2026-11-23" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The US Senate confirms a Supreme Court justice nominee between 2026-11-16 and 2026-11-23" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A cyberattack causes a service disruption for a major US cloud provider between 2026-11-16 and 2026-11-23" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A wildfire burns more than 10,000 acres in California between 2026-11-16 and 2026-11-23" → REJECTED: cited items name Australia, Central African Republic; the claim is about California — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The Federal Reserve announces an interest rate cut between 2026-11-16 and 2026-11-23" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5781 issued all-time across 23 forecaster arms · 4059 open (1723 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 224 issued · 222 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 214 | 214 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 221 | 204 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 224 | 222 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 209 | 176 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 397 | 383 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*