**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082141Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-08_1517.md · forecaster: manual/sonnet-5 · 7 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260808-18 | 62% | 2026-08-26 | military/conflict | Russia strikes Kyiv with a single wave using four or more distinct weapon types (missile, drone, glide bomb, cruise, ballistic, etc), corroborated by both Ukrainian and Russian-aligned sources, between 2026-08-11 and 2026-08-24. | TRUE if Kyiv is struck by four or more distinct weapon types in one wave between 2026-08-11 and 2026-08-24, reported by both Ukrainian and Russian-aligned sources, adjudicated by 2026-08-26. |
| KKR-20260808-19 | 36% | 2026-08-26 | military/conflict | A NATO member state reports intercepting or shooting down a Russian-attributed drone inside its own territory, between 2026-08-11 and 2026-08-24. | TRUE if a NATO government or NATO itself publicly confirms intercepting or downing a Russian-attributed drone within a member state territory between 2026-08-11 and 2026-08-24, confirmed by 2026-08-26. |
| KKR-20260808-20 | 12% | 2026-09-10 | military/conflict | Iran imposes a closure or blockade on commercial shipping transit through the Strait of Hormuz at any point between 2026-08-11 and 2026-09-08. | TRUE if Iran announces or enforces a closure, blockade, or de facto halt of transit through the Strait of Hormuz between 2026-08-11 and 2026-09-08, confirmed by two or more wire services by 2026-09-10. |
| KKR-20260808-21 | 74% | 2026-08-25 | cyber | A CVE for the Metabase authentication-bypass or SQL-injection vulnerability reported as actively exploited on 2026-08-07 and 2026-08-08 is added to the CISA Known Exploited Vulnerabilities catalog, with dateAdded between 2026-08-09 and 2026-08-23. | TRUE if the CISA KEV catalog lists a Metabase-related CVE with dateAdded between 2026-08-09 and 2026-08-23, checked by 2026-08-25. |
| KKR-20260808-22 | 14% | 2026-09-08 | cyber | CISA updates the Known Exploited Vulnerabilities catalog entry for CVE-2026-8037, the Progress LoadMaster command-injection vulnerability, so that knownRansomwareCampaignUse equals Known, at any point between 2026-08-09 and 2026-09-06. | TRUE if the CISA KEV entry for CVE-2026-8037 shows knownRansomwareCampaignUse equal to Known at any check between 2026-08-09 and 2026-09-06, verified by 2026-09-08. |
| KKR-20260808-23 | 18% | 2026-09-10 | political | The sitting Governor of Rhode Island leaves office, through resignation, recall, impeachment conviction, or removal, at any point between 2026-08-11 and 2026-09-08. | TRUE if the individual holding the Rhode Island governorship on 2026-08-08 is no longer Governor of Rhode Island at any point between 2026-08-11 and 2026-09-08, confirmed by 2026-09-10. |
| KKR-20260808-24 | 52% | 2026-08-18 | disaster | Typhoon Dolphin makes landfall on the coast of mainland China at any point between 2026-08-09 and 2026-08-16. | TRUE if the China Meteorological Administration or the Joint Typhoon Warning Center records a mainland China landfall for Typhoon Dolphin between 2026-08-09 and 2026-08-16, confirmed by 2026-08-18. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7650.00 on at least one trading day between 2026-08-10 and 2026-08-21, giving back roughly half of the 2026-0" → REJECTED: cited items overlap the claim only on vocabulary common across the whole report — shared words are not shared content, and a prior that fits every item grounds none of them; cite an item carrying something specific to THIS claim; cited items overlap the claim only on vocabulary common across the whole report — shared words are not shared content, and a prior that fits every item grounds none of them; cite an item carrying something specific to THIS claim
- "COMEX front-month gold futures settle at a fresh nominal all-time high above 4399.70 on at least one trading day between 2026-08-10 and 2026" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

403 issued all-time across 14 forecaster arms · 353 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5`:** 30 issued · 28 open · 2 resolved · 1 hits / 1 misses · **Brier 0.265** against its own base rate 50.0% (climatological 0.250) · **skill -0.060** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 33 | 31 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 20 | 32 | 9 | 23 | 0.221 | 28.1% | 0.202 | -0.093 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 62 | 62 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 30 | 28 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*