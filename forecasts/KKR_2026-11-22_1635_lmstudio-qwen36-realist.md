**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221635Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-22_1632.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261122-05 | 30% | 2026-11-30 | economics | The Nasdaq Composite Index closes below 20,000.00 on any trading day between 2026-11-23 and 2026-11-27. | True if the Nasdaq Composite Index closes below 20,000.00 on any trading day in the window; False if it closes above that level every day. Reference: 22,617.73 on the packet date. |
| KKR-20261122-06 | 15% | 2026-12-10 | economics | The Bank of England cuts its base interest rate by at least 25 basis points between 2026-11-23 and 2026-12-07. | True if the Bank of England announces a base rate cut of 25 basis points or more during the window; False if the rate remains unchanged or is raised. |
| KKR-20261122-07 | 45% | 2026-12-12 | disaster | The USGS records a magnitude 6.0 or greater earthquake between 2026-11-23 and 2026-12-07. | True if the USGS Significant Quakes catalog records an event with magnitude >= 6.0 in the window; False if no such event is recorded. |
| KKR-20261122-08 | 40% | 2026-12-02 | military_conflict | Saudi Arabia intercepts a drone or missile launched by the Houthis between 2026-11-23 and 2026-11-30. | True if at least one wire service reports Saudi interception of a Houthi-launched drone or missile in the window; False if no such interception is reported. |
| KKR-20261122-09 | 20% | 2026-12-12 | political | The European Union imposes new sanctions on Russian oil entities between 2026-11-23 and 2026-12-07. | True if the EU Official Journal publishes a new sanctions regulation targeting Russian oil entities in the window; False if no such regulation is published. |
| KKR-20261122-10 | 30% | 2026-12-02 | cyber | A major US cloud provider (AWS, Azure, or GCP) experiences a service outage lasting more than 4 hours between 2026-11-23 and 2026-11-30. | True if Downdetector or a major wire service reports a cloud outage lasting >4 hours for AWS, Azure, or GCP in the window; False if no such outage is reported. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-22 and 2026-11-29 for a vulnerability with a CVSS base score of 9.0 or highe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone or missile strike hits a civilian target in Khartoum, Sudan, resulting in at least one confirmed death." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

5918 issued all-time across 23 forecaster arms · 4196 open (2129 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 247 issued · 214 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

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
| lmstudio/qwen36 | 261 | 244 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 257 | 255 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 247 | 214 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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