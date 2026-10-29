**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-29_1513.md · forecaster: lmstudio/qwen36-abliterated · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261029-08 | 20% | 2027-02-03 | economic | The US Federal Reserve raises the federal funds target rate by at least 25 basis points before 2027-01-31 | The Federal Reserve issues an official statement raising the federal funds target rate by 25 basis points or more on or before 2027-01-31 |
| KKR-20261029-09 | 45% | 2026-11-18 | cyber | A new CVE with a CVSS score of 9.0 or higher is added to the CISA KEV catalog between 2026-11-01 and 2026-11-15 | The CISA KEV catalog carries a date-added value between 2026-11-01 and 2026-11-15 for a vulnerability with a CVSS score of 9.0 or higher |
| KKR-20261029-10 | 35% | 2026-12-18 | economic | The S&P 500 index closes below 7,500.00 on at least one trading day between 2026-12-01 and 2026-12-15 | The S&P 500 index closing price recorded by the NYSE falls below 7,500.00 on any day from 2026-12-01 through 2026-12-15 inclusive |
| KKR-20261029-11 | 15% | 2027-04-04 | military | Russia and Ukraine sign a formal ceasefire agreement or armistice before 2027-04-01 | A joint statement or treaty document signed by representatives of Russia and Ukraine explicitly declaring a ceasefire or armistice is published on or before 2027-04-01 |
| KKR-20261029-12 | 50% | 2026-12-03 | cyber | A cyberattack causes a significant disruption to a major US cloud provider's services between 2026-11-01 and 2026-11-30 | A public outage report or service status update from a major US cloud provider (AWS, Azure, or GCP) confirms a service disruption lasting more than 4 hours caused by a cyberattack between 2026-11-01 and 2026-11-30 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The ECB appoints a successor to Christine Lagarde as President before 2027-02-01" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a european central bank press release | or | official eu publication names a new president…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Brent Crude settles above 115.00 USD per barrel on at least one trading day between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A magnitude 6.0 or greater earthquake occurs in the Pacific Ring of Fire between 2026-11-10 and 2026-11-17" → REJECTED: the resolution names only a venue or register (USGS, quakes, significant) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A major US bank fails or is seized by regulators between 2026-11-01 and 2026-12-31" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new state-level law or executive order in the US restricts abortion access before 2027-03-01" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5125 issued all-time across 22 forecaster arms · 3403 open (553 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 138 issued · 136 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 10 | 10 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 137 | 120 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 138 | 136 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 131 | 98 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 460 | 345 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 291 | 277 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*