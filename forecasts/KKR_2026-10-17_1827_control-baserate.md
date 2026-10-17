**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171827Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-38 | 60% | 2026-12-01 | economics/markets | The EIA Cushing OK WTI spot price, published on FRED as series DCOILWTICO, is at or above 100.00 dollars per barrel for the observation dated 2026-11-20. Reference: 99.02 dollars on the packet date 2026-10-17. | FRED series DCOILWTICO shows a value of 100.00 or higher for the observation dated 2026-11-20. Reference level at seal: 99.02 on 2026-10-17. A value below 100.00 resolves false. |
| KKR-20261017-39 | 60% | 2026-11-24 | economics/markets | The 10-year Treasury constant maturity yield, published on FRED as series DGS10, is at or above 5.25 percent for the observation dated 2026-11-20. Reference: 5.10 percent on the packet date 2026-10-17. | FRED series DGS10 shows a value of 5.25 or higher for the observation dated 2026-11-20. Reference level at seal: 5.10 percent on 2026-10-17. A value below 5.25 resolves false. |
| KKR-20261017-40 | 60% | 2026-10-30 | economics/markets | The FOMC statement issued 2026-10-28 at the conclusion of the scheduled 2026-10-27 to 2026-10-28 meeting raises the federal funds target range above the 3.75 to 4.00 percent range in effect on 2026-10-17. | The FOMC statement dated 2026-10-28 on federalreserve.gov sets a target range whose upper bound exceeds 4.00 percent. Reference: 3.75 to 4.00 percent in effect at seal on 2026-10-17. Hold or cut resolves false. |
| KKR-20261017-41 | 41% | 2026-12-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry with vendorProject Drupal carrying a dateAdded between 2026-10-17 and 2026-11-30, following the critical Drupal remote code execution patches disclosed 2026-10-17. | The CISA KEV JSON feed, fetched on or after the deadline, contains at least one entry whose vendorProject is Drupal and whose dateAdded falls between 2026-10-17 and 2026-11-30 inclusive. |
| KKR-20261017-42 | 42% | 2026-10-27 | disaster | The center of Eastern Pacific Hurricane Trudy crosses the coastline of Mexico at tropical storm or hurricane intensity between 2026-10-17 and 2026-10-24, as recorded in National Hurricane Center advisories or tropical cyclone updates. | NHC public advisories or tropical cyclone updates for Trudy record the center making landfall on the Mexican coast at tropical storm or greater intensity at a time between 2026-10-17 00:00 UTC and 2026-10-24 23:59 UTC. |
| KKR-20261017-43 | 42% | 2026-11-17 | disaster | The USGS ComCat catalog records at least one earthquake of magnitude 6.0 or greater with epicenter within 150 km of the M6.9 Ozernovskiy, Russia event (USGS id us6000u2mq) and origin time between 2026-10-18 and 2026-11-14. | USGS ComCat contains an event of magnitude 6.0 or greater whose origin time is between 2026-10-18 00:00 UTC and 2026-11-14 23:59 UTC and whose epicenter lies within 150 km of USGS event us6000u2mq. |
| KKR-20261017-44 | 40% | 2026-11-17 | political | Between 2026-10-17 and 2026-11-13 the White House names a successor to Katie Zacharia as White House press secretary on a permanent basis, not as acting or interim press secretary. | A White House announcement, or reporting by two of AP, Reuters, New York Times, Washington Post, dated 2026-10-17 to 2026-11-13, identifies a named person appointed White House press secretary without an acting or interim designation. |
| KKR-20261017-45 | 40% | 2026-12-15 | political | Republicans retain a majority in the U.S. Senate in the 2026-11-03 midterm elections, with AP race calls projecting Republicans holding at least 51 of 100 seats when the 120th Congress convenes in January 2027. | AP race calls published by 2026-12-15 project Republicans holding at least 51 of 100 Senate seats in the 120th Congress, including seats not contested in 2026; uncalled races count as not Republican. |
| KKR-20261017-46 | 64% | 2026-11-04 | military/conflict | Between 2026-10-18 and 2026-10-31 UKMTO or the Joint Maritime Information Center publishes an incident advisory stating that a merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman was struck by a projectile, mine, or uncrewed system. | The UKMTO or JMIC incident list carries an advisory dated 2026-10-18 to 2026-10-31 describing a merchant vessel struck by a projectile, mine, or uncrewed system in the Persian Gulf, Strait of Hormuz, or Gulf of Oman. |
| KKR-20261017-47 | 39% | 2027-01-05 | crime/security | A federal criminal indictment or information naming Ilhan Omar as a defendant is filed or unsealed in a U.S. district court between 2026-10-17 and 2026-12-31. | A U.S. district court docket, viewable on PACER or CourtListener, shows a criminal indictment or information naming Ilhan Omar as defendant, filed or unsealed between 2026-10-17 and 2026-12-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4366 issued all-time across 21 forecaster arms · 3255 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1536 issued · 1240 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1536 | 1240 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*