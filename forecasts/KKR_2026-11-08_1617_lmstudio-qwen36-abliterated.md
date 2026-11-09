**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081617Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-08_1613.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261108-36 | 25% | 2026-12-16 | disaster | A 5.5-magnitude or larger earthquake occurs in Japan between 2026-12-10 and 2026-12-13. | The USGS catalog records an earthquake with magnitude 5.5 or higher in Japan within the event window. |
| KKR-20261108-37 | 45% | 2027-01-13 | political | Gadi Eisenkot successfully forms the next government of Israel between 2027-01-01 and 2027-01-10. | Eisenkot is sworn in as Prime Minister or his coalition is officially registered within the event window. |
| KKR-20261108-38 | 20% | 2027-02-07 | disaster | The USGS catalog records an earthquake of magnitude 6.0 or higher in Japan between 2027-02-01 and 2027-02-04. | The USGS catalog carries a date-added value for a Japan earthquake with magnitude 6.0 or higher between the start and end dates. |
| KKR-20261108-39 | 40% | 2026-12-07 | crime/security | Polish prosecutors formally indict the suspect in the Krakow shooting between 2026-12-01 and 2026-12-04. | A formal indictment document is filed in the Krakow court docket within the event window. |
| KKR-20261108-40 | 30% | 2026-12-28 | economics/markets | The Brent crude oil price closes below 95.00 dollars per barrel at least once between 2026-12-20 and 2026-12-23. Reference: 98.32 dollars on the packet date. | The Brent crude oil price settles below 95.00 dollars per barrel on any trading day within the event window. |
| KKR-20261108-41 | 10% | 2027-04-07 | disaster | A 6.5-magnitude or larger earthquake occurs in Japan between 2027-04-01 and 2027-04-04. | The USGS catalog records an earthquake with magnitude 6.5 or higher in Japan within the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,200 at least once between 2026-12-01 and 2026-12-04. Reference: 7,376.86 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The 10-year US Treasury yield closes above 5.00 percent at least once between 2026-12-15 and 2026-12-18. Reference: 4.86 percent on the pack" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new vulnerability is added to the CISA KEV catalog between 2026-12-01 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes above 7,500 at least once between 2027-03-01 and 2027-03-04. Reference: 7,376.86 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5474 issued all-time across 22 forecaster arms · 3752 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 190 issued · 188 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 188 | 171 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 190 | 188 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 167 | 134 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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