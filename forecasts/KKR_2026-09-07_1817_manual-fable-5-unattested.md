**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071817Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-27 | 65% | 2026-10-13 | economics/markets | ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-09. Reference: Brent 96.28 on the packet date. | TRUE if the official ICE Brent front-month daily settlement price is at or above 100.00 USD on any trading day between 2026-09-08 and 2026-10-09. Reference: 96.28 at seal. |
| KKR-20260907-28 | 60% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one ConnectWise ScreenConnect entry with a date-added value between 2026-09-08 and 2026-10-09. | TRUE if the CISA KEV catalog contains an entry naming ConnectWise or ScreenConnect in its vendor or product fields with dateAdded between 2026-09-08 and 2026-10-09. |
| KKR-20260907-29 | 85% | 2026-11-04 | disaster | The NTSB publishes a preliminary report on the 2026-09-06 cargo aircraft accident at Miami International Airport between 2026-09-08 and 2026-10-30. | TRUE if an NTSB preliminary report for the 2026-09-06 Miami cargo aircraft accident appears in the NTSB public investigation database dated between 2026-09-08 and 2026-10-30. |
| KKR-20260907-30 | 60% | 2026-12-04 | political | Democratic candidates win a majority of seats in the United States House of Representatives in the elections held 2026-11-03. | TRUE if Associated Press race calls credit Democratic candidates with at least 218 US House seats from the 2026-11-03 elections, as of 2026-12-04. |
| KKR-20260907-31 | 85% | 2026-12-22 | crime/security | The Paris court trying the murder of Federico Aramburu delivers a verdict between 2026-09-08 and 2026-12-18. | TRUE if two international news outlets report a verdict delivered in the Paris trial over the murder of Federico Aramburu between 2026-09-08 and 2026-12-18. |
| KKR-20260907-32 | 30% | 2027-01-05 | military/conflict | The United States and Iraqi governments both publicly announce completion of the US-led coalition military mission in Iraq between 2026-09-08 and 2026-12-31. | TRUE if both the US and Iraqi governments announce the coalition military mission in Iraq has ended between 2026-09-08 and 2026-12-31, reported by two international news agencies. |
| KKR-20260907-33 | 12% | 2027-03-02 | political | The Landtag of Saxony-Anhalt elects a member of the AfD as Minister-President between 2026-09-08 and 2027-02-26. | TRUE if the Landtag of Saxony-Anhalt elects an AfD member as Minister-President between 2026-09-08 and 2027-02-26, per the Landtag official record or two international news outlets. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Jakarta Soekarno-Hatta International Airport operates scheduled commercial passenger departures on at least one day between 2026-09-08 and 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…airport operator | or | two international news outlets…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Iranian forces board, seize, or fire upon a commercial merchant vessel in or near the Strait of Hormuz between 2026-09-08 and 2026-10-09." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ukmto | or | jmic…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Russian and Ukrainian government delegations hold a direct meeting at a publicly announced venue between 2026-09-08 and 2026-11-06." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

1643 issued all-time across 16 forecaster arms · 1378 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 180 issued · 178 open · 2 resolved · 2 hits / 0 misses · **Brier 0.225** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 484 | 456 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 187 | 166 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*