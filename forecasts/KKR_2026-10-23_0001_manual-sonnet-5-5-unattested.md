**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 230001Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: manual/sonnet-5.5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-31 | 82% | 2026-11-09 | cyber | Following reported exploitation of the PHP2Shell flaws, the CISA KEV catalog adds at least one entry whose vendorProject or product field contains PHP, with a dateAdded value between 2026-10-22 and 2026-11-05. | Fetch the CISA known exploited vulnerabilities JSON catalog after the deadline; true if any entry has vendorProject or product containing PHP and dateAdded from 2026-10-22 through 2026-11-05 inclusive. |
| KKR-20261023-32 | 10% | 2026-11-16 | cyber | After disclosure of the CVSS 10.0 GitLab code execution flaw, the CISA KEV catalog adds at least one entry with vendorProject GitLab and a dateAdded value between 2026-10-22 and 2026-11-12. | Fetch the CISA known exploited vulnerabilities JSON catalog after the deadline; true if any entry has vendorProject equal to GitLab and dateAdded from 2026-10-22 through 2026-11-12 inclusive. |
| KKR-20261023-33 | 85% | 2026-11-09 | military/conflict | At least one person is killed inside Saudi Arabia by a Houthi missile or drone attack occurring between 2026-10-23 and 2026-11-05. | At least two of Reuters, AP, AFP and BBC report one or more deaths inside Saudi Arabia from a Houthi missile or drone strike dated 2026-10-23 through 2026-11-05 inclusive. |
| KKR-20261023-34 | 40% | 2026-12-03 | military/conflict | US or Israeli forces strike a target on Iranian soil between 2026-10-23 and 2026-11-30. | At least two of Reuters, AP, AFP and BBC report a US or Israeli air, missile or drone strike on a target on Iranian soil dated 2026-10-23 through 2026-11-30 inclusive; strikes on vessels at sea do not count. |
| KKR-20261023-35 | 40% | 2026-12-08 | military/conflict | Official delegations of Russia, Ukraine and the United States meet in person for trilateral negotiations between 2026-10-23 and 2026-12-04. | At least two of Reuters, AP, AFP and BBC report that Russian, Ukrainian and US delegations met in person at one venue for negotiations dated 2026-10-23 through 2026-12-04; separate shuttle meetings do not count. |
| KKR-20261023-36 | 16% | 2026-11-09 | disaster | USGS lists an earthquake of magnitude 6.0 or greater, other than event us6000u43g, within 300 km of that event epicenter with origin time between 2026-10-23 and 2026-11-05 UTC. | Query the USGS ComCat catalog after the deadline; true if any event other than us6000u43g with magnitude 6.0 or greater lies within 300 km of its epicenter with origin time 2026-10-23 through 2026-11-05 UTC. |
| KKR-20261023-37 | 6% | 2026-11-16 | political | France declares a state of emergency covering any part of metropolitan France between 2026-10-23 and 2026-11-12. | The Journal Officiel on Legifrance publishes a decree declaring a state of emergency under the 1955 law that covers any part of metropolitan France, dated 2026-10-23 through 2026-11-12 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE front-month Brent crude futures settle above 125.00 USD per barrel on at least one trading day between 2026-10-23 and 2026-11-20. Refere" → REJECTED: resolution offers alternative VENUES joined by 'or' (…onth daily settlement, as reported by reuters | or | ice, exceeds 125…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The NASDAQ Composite closes below 24,500 on at least one trading day between 2026-10-23 and 2026-11-20. Reference: 26,099.07 in the packet m" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "At its meeting on 2026-10-27 and 2026-10-28, the FOMC leaves the federal funds target range unchanged from the range in effect on 2026-10-22" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4749 issued all-time across 21 forecaster arms · 3397 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 196 issued · 193 open · 3 resolved · 3 hits / 0 misses · **Brier 0.009** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1672 | 1289 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 457 | 216 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*