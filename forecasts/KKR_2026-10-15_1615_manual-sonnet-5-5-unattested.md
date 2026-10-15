**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151615Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-15_1512.md · forecaster: manual/sonnet-5.5/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261015-47 | 75% | 2026-10-28 | military/conflict | At least one oil refinery inside Russia, excluding occupied Ukrainian territory, is struck by a Ukrainian drone or missile between 2026-10-19 and 2026-10-25. | Reuters, AP or BBC report, or the Russian Defense Ministry or a Russian regional governor states, that a named refinery in Russia was hit by Ukrainian drones or missiles on a date from 2026-10-19 through 2026-10-25. |
| KKR-20261015-48 | 27% | 2026-11-04 | military/conflict | A merchant vessel is struck by a drone, missile or naval mine inside Romanian territorial waters or the Romanian exclusive economic zone between 2026-10-19 and 2026-11-01, not counting the vessels reported on fire on 2026-10-15. | Romanian authorities state, or two of Reuters, AP, BBC and DW report, a new drone, missile or mine strike on a merchant ship inside Romanian waters or exclusive economic zone between 2026-10-19 and 2026-11-01. |
| KKR-20261015-49 | 28% | 2026-11-25 | economics/markets | The 10-year US Treasury constant maturity yield for 2026-11-20 is at or above 5.25 percent. Reference: 5.05 percent in the packet market snapshot of 2026-10-15. | FRED series DGS10 reports a value of 5.25 or higher for observation date 2026-11-20, as retrieved on or after 2026-11-25. |
| KKR-20261015-50 | 21% | 2026-11-25 | economics/markets | The Nasdaq Composite records a daily close below 24000 on at least one trading day between 2026-10-19 and 2026-11-20. Reference: 26611.73 in the packet market snapshot of 2026-10-15. | FRED series NASDAQCOM shows a daily closing value below 24000 for any observation date from 2026-10-19 through 2026-11-20 inclusive, as retrieved on or after 2026-11-25. |
| KKR-20261015-51 | 35% | 2026-11-09 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Langflow entry with a dateAdded value between 2026-10-15 and 2026-11-05. | The CISA KEV JSON feed carries an entry whose vendorProject or product field is Langflow and whose dateAdded value falls from 2026-10-15 through 2026-11-05 inclusive. |
| KKR-20261015-52 | 30% | 2026-11-05 | disaster | USGS records an earthquake of magnitude 6.0 or greater with Panama in its place name and an origin time between 2026-10-19 and 2026-11-01 UTC. | A USGS ComCat query for magnitude 6.0 or greater with origin time from 2026-10-19T00:00Z through 2026-11-01T23:59Z returns at least one event whose place field contains Panama. |
| KKR-20261015-53 | 45% | 2026-12-14 | crime/security | The US military executes Nidal Malik Hasan, the Fort Hood shooter, between 2026-12-03 and 2026-12-10. | The Army or Pentagon announces, and at least two of AP, Reuters and BBC report, that Hasan was executed on a date from 2026-12-03 through 2026-12-10. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US forces use a GBU-43/B Massive Ordnance Air Blast bomb, known as the MOAB, in combat anywhere between 2026-10-19 and 2026-12-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (…pentagon | or | centcom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Federal Open Market Committee raises the federal funds target range at its meeting ending 2026-10-28. Reference: upper bound of 4.00 per" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Democrats win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4216 issued all-time across 21 forecaster arms · 3105 open (481 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 138 issued · 138 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1484 | 1188 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 429 | 206 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 60 | 60 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 63 | 63 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 174 | 169 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*