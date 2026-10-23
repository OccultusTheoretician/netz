**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 230001Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-08 | 66% | 2026-12-03 | military/conflict | Official Russian and Ukrainian delegations meet in person for a negotiating round between 2026-10-23 and 2026-11-30, confirmed by both governments. | Russian (Kremlin or Foreign Ministry) and Ukrainian (Presidential Office or Foreign Ministry) officials each confirm their delegations met in person at a negotiating round held between 2026-10-23 and 2026-11-30. Remote or intermediary-only exchanges do not count. |
| KKR-20261023-09 | 66% | 2026-11-25 | military/conflict | A Houthi missile or drone attack on Saudi territory kills at least one person between 2026-10-23 and 2026-11-22, confirmed by Saudi authorities. | The Saudi Press Agency or Saudi Ministry of Defense confirms at least one person killed on Saudi territory by a Houthi-launched missile or drone in an attack occurring between 2026-10-23 and 2026-11-22. |
| KKR-20261023-10 | 60% | 2026-11-24 | economics/markets | ICE Brent crude front-month futures settle above 120.00 USD per barrel on at least one trading day between 2026-10-23 and 2026-11-20. Reference: 111.58 on the packet date. | ICE Brent Crude futures front-month contract settles strictly above 120.00 USD per barrel on at least one trading day between 2026-10-23 and 2026-11-20 inclusive, per ICE published settlement prices. Reference at seal: 111.58. |
| KKR-20261023-11 | 46% | 2026-11-09 | cyber | CISA adds at least one PHP vulnerability from the October 2026 PHP2Shell disclosure to its Known Exploited Vulnerabilities catalog with dateAdded between 2026-10-22 and 2026-11-05. | The CISA KEV catalog JSON contains at least one entry whose vendorProject or product field names PHP and whose dateAdded is between 2026-10-22 and 2026-11-05 inclusive. |
| KKR-20261023-12 | 46% | 2026-11-24 | cyber | CISA adds a GitLab vulnerability to its Known Exploited Vulnerabilities catalog with dateAdded between 2026-10-22 and 2026-11-20. | The CISA KEV catalog JSON contains at least one entry with vendorProject GitLab and dateAdded between 2026-10-22 and 2026-11-20 inclusive. |
| KKR-20261023-13 | 42% | 2026-11-25 | political | The French government declares a state of emergency under the law of 3 April 1955 covering any part of metropolitan France by decree dated between 2026-10-23 and 2026-11-22. | A decree declaring a state of emergency under the law of 3 April 1955 covering any part of metropolitan France is published in the Journal officiel de la Republique francaise dated between 2026-10-23 and 2026-11-22. |
| KKR-20261023-14 | 60% | 2027-01-05 | economics/markets | Moderna announces between 2026-10-22 and 2026-12-31 that a Phase 3 trial of intismeran autogene (mRNA-4157), its individualized neoantigen cancer therapy, met its primary endpoint. | A Moderna press release dated between 2026-10-22 and 2026-12-31 reports top-line results from a Phase 3 trial of intismeran autogene (mRNA-4157) and states the trial met its primary endpoint. A miss, delay, or no release resolves false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Israel Defense Forces or US Central Command acknowledges conducting a strike on a target inside Iranian territory between 2026-10-23 and" → REJECTED: resolution offers alternative VENUES joined by 'or' (…official idf | or | centcom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Democratic candidates win at least 218 of the 435 US House seats in the 2026-11-03 general election, as reflected in Associated Press race c" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 2026-10-22 M7.0 earthquake near Nagqu, China (USGS us6000u43g) is followed by at least one M5.5 or greater aftershock within 100 km of i" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-06 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

4726 issued all-time across 21 forecaster arms · 3374 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1664 issued · 1281 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1664 | 1281 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
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
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*