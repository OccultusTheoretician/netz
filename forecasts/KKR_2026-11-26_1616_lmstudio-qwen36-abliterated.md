**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 261616Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-26_1612.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261126-14 | 30% | 2026-12-07 | economics | The S&P 500 index closes below 7,000 on at least one trading day between 2026-11-27 and 2026-12-04. | The S&P 500 index closes below 7,000 on at least one trading day between 2026-11-27 and 2026-12-04. Reference: 7,182.78 on the packet date. |
| KKR-20261126-15 | 40% | 2026-12-04 | disaster | A magnitude 5.0 or greater earthquake occurs in the Revilla Gigedo Islands Region between 2026-11-26 and 2026-12-03. | The USGS Significant Quakes catalog records a magnitude 5.0 or greater earthquake in the Revilla Gigedo Islands Region between 2026-11-26 and 2026-12-03. |
| KKR-20261126-16 | 85% | 2026-12-04 | political | Pablo Hernandez de Cos is confirmed as the new European Central Bank President between 2026-11-26 and 2026-12-03. | The European Central Bank confirms Pablo Hernandez de Cos as the new President between 2026-11-26 and 2026-12-03. |
| KKR-20261126-17 | 25% | 2026-12-04 | military | The Houthis impose a blockade on the Strait of Hormuz between 2026-11-26 and 2026-12-03. | The Houthis impose a blockade on the Strait of Hormuz between 2026-11-26 and 2026-12-03. |
| KKR-20261126-18 | 75% | 2026-12-04 | disaster | The Congo Ebola outbreak reaches 12,000 cases between 2026-11-26 and 2026-12-03. | The Congo Ebola outbreak reaches 12,000 cases between 2026-11-26 and 2026-12-03. |
| KKR-20261126-19 | 60% | 2026-12-04 | political | The UK sanctions Yemen's Houthis between 2026-11-26 and 2026-12-03. | The UK sanctions Yemen's Houthis between 2026-11-26 and 2026-12-03. |
| KKR-20261126-20 | 90% | 2026-12-04 | economics | Norse Atlantic Airways suspends all flights between 2026-11-26 and 2026-12-03. | Norse Atlantic Airways suspends all flights between 2026-11-26 and 2026-12-03. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-26 and 2026-12-03 for CVE-2026-103406." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-103406 dateAdded 2026-11-25, before the claimed window 2026-11-26..2026-12-03; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The 10-year US Treasury yield closes above 5.00 percent on at least one trading day between 2026-11-27 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "FIFA confirms a cyberattack between 2026-11-26 and 2026-12-03." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5987 issued all-time across 23 forecaster arms · 4265 open (2349 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 287 issued · 285 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 282 | 265 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 287 | 285 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 265 | 232 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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