**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071616Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-07_1612.md · forecaster: lmstudio/qwen36-abliterated · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261107-08 | 20% | 2026-11-25 | disaster | A forest fire notification is catalogued by GDACS for Mozambique between 2026-11-16 and 2026-11-23. | The GDACS Alerts feed records a new event with eventtype WF and location Mozambique with a date-added value between 2026-11-16 and 2026-11-23. |
| KKR-20261107-09 | 25% | 2026-11-23 | economics/markets | The Brent crude oil price closes above 105 USD per barrel on any weekday between 2026-11-16 and 2026-11-20. Reference: 98.32 on the packet date. | The Brent crude oil price closing value on the ICE exchange is strictly greater than 105 USD per barrel on at least one trading day within the window. |
| KKR-20261107-10 | 15% | 2026-11-25 | political | A US federal judge issues a ruling in the Home Office asylum seeker kidnapping case between 2026-11-16 and 2026-11-23. | A US federal court docket records a new entry with the case title containing 'Home Office' and 'asylum seeker' and an event date between 2026-11-16 and 2026-11-23. |
| KKR-20261107-11 | 30% | 2026-11-25 | disaster | A magnitude 5.0 or greater earthquake is recorded by USGS in Japan between 2026-11-16 and 2026-11-23. | The USGS Significant Quakes feed records an event with magnitude 5.0 or greater and location Japan with an event date between 2026-11-16 and 2026-11-23. |
| KKR-20261107-12 | 25% | 2026-11-25 | cyber | A cyberattack causes a service disruption to a major French bank between 2026-11-16 and 2026-11-23. | A wire service reports a service disruption to a major French bank caused by a cyberattack with a report date between 2026-11-16 and 2026-11-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,300 on any weekday between 2026-11-16 and 2026-11-20. Reference: 7,376.86 on the packet date." → REJECTED: cited items name Iran, Islamic Republic of; the claim is about New York — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names only a venue or register (exchange, new, stock, york) and no subject - the register is where to look, not what is claimed; name the subject inside it; the resolution names a different subject than the statement — the claim is about Reference and the resolution settles on Exchange, New, Stock, York. A row whose resolution checks a different fact can be scored correct while being wrong
- "A new exploited vulnerability is added to the CISA KEV catalog between 2026-11-16 and 2026-11-23." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Nasdaq index closes below 24,000 on any weekday between 2026-11-16 and 2026-11-20. Reference: 24,579.42 on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10-year US Treasury yield closes above 5.00 percent on any weekday between 2026-11-16 and 2026-11-20. Reference: 4.86 on the packet date" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new case of the SonicWall SonicOS SSLVPN vulnerability is added to the CISA KEV catalog between 2026-11-16 and 2026-11-23." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5433 issued all-time across 22 forecaster arms · 3711 open (1331 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 184 issued · 182 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 102 | 102 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 183 | 166 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 184 | 182 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 163 | 130 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 494 | 379 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 349 | 335 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*