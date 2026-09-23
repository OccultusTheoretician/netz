**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232215Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-23_1518.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260923-13 | 55% | 2026-10-27 | cyber | Between 2026-09-23 and 2026-10-23, CISA adds to its Known Exploited Vulnerabilities catalog a new Oracle PeopleSoft or PeopleTools vulnerability other than CVE-2026-35273, following the ShinyHunters claim of an FBI breach through an unpatched PeopleSoft zero-day. | The CISA KEV JSON feed contains an entry with vendorProject Oracle and a product naming PeopleSoft or PeopleTools, a CVE ID other than CVE-2026-35273, and a dateAdded value from 2026-09-23 through 2026-10-23 inclusive. |
| KKR-20260923-14 | 65% | 2026-10-30 | economics/markets | At its scheduled meeting concluding 2026-10-28, the FOMC raises the federal funds target range above the 3.75 to 4.00 percent range in effect on the packet date. Reference: upper limit 4.00 percent on 2026-09-23. | The FOMC statement released 2026-10-28 on federalreserve.gov sets a target range upper limit of 4.25 percent or higher, and FRED series DFEDTARU shows 4.25 or higher effective 2026-10-29. |
| KKR-20260923-15 | 38% | 2026-11-02 | economics/markets | On at least one business day between 2026-09-24 and 2026-10-30, the 10-year Treasury constant maturity yield (FRED series DGS10) is at or above 5.50 percent. Reference: 10Y yield 5.06 percent in the packet market snapshot on 2026-09-23. | FRED series DGS10 shows a daily value of 5.50 or higher for at least one date from 2026-09-24 through 2026-10-30 inclusive. |
| KKR-20260923-16 | 65% | 2026-10-13 | political | Between 2026-09-23 and 2026-10-09, US District Judge Timothy J. Kelly enters an order granting, in whole or in part, a temporary restraining order or preliminary injunction restoring White House access to at least one plaintiff in the suit filed 2026-09-21 by CNN, MS NOW and Politico against the Trump administration. | The D.D.C. docket for the CNN, MS NOW and Politico suit before Judge Kelly shows an order dated 2026-09-23 through 2026-10-09 granting TRO or preliminary injunction relief, in whole or in part, to at least one plaintiff. |
| KKR-20260923-17 | 30% | 2026-11-04 | military/conflict | Between 2026-09-24 and 2026-10-31, Russia and Ukraine each publicly announce acceptance of a mutual halt to strikes on energy infrastructure, the energy truce pushed by Trump and endorsed by Zelensky at the UN. | Within the window, a Kremlin statement on kremlin.ru or via TASS quoting Putin or Peskov, and a Ukrainian presidential statement on president.gov.ua or by Zelensky, each confirm agreement to a mutual energy-strike moratorium. |
| KKR-20260923-18 | 25% | 2026-11-17 | military/conflict | Between 2026-09-24 and 2026-11-13, the United States announces that its naval blockade of Iranian ports and vessels, in force since 2026-07-14, is lifted or suspended. | A White House, Pentagon or CENTCOM statement dated inside the window declares the naval blockade of Iran lifted or suspended, and both Reuters and AP report that announcement. |
| KKR-20260923-19 | 30% | 2026-11-04 | military/conflict | Between 2026-09-24 and 2026-10-31, at least one air or drone strike hits Mekelle (Mekele) city, capital of the Tigray region of Ethiopia, amid the mutual offensive accusations between Addis Ababa and the TPLF. | At least two of Reuters, AP, AFP and BBC report, citing residents, hospital staff, humanitarian or UN sources, an air or drone strike impacting inside Mekelle city on a date inside the window. |
| KKR-20260923-20 | 45% | 2026-10-27 | crime/security | Between 2026-09-24 and 2026-10-23, the South African Police Service announces the arrest of at least one suspect in the mass shooting at a house in South Africa in which eleven people were killed, reported by BBC on 2026-09-23. | A SAPS media statement on saps.gov.za, or a SAPS or NPA spokesperson quoted by two of Reuters, AP, AFP, BBC and News24, confirms at least one arrest for that shooting on a date inside the window. |
| KKR-20260923-21 | 15% | 2026-10-27 | disaster | Between 2026-09-24 and 2026-10-23, USGS records an earthquake of magnitude 6.0 or greater within 250 km of the epicenter of the 2026 M6.5 event 169 km west of Nikolski, Alaska (USGS event id us7000ti1p). | The USGS ComCat catalog lists an event of magnitude 6.0 or greater with origin time inside the window and epicenter within 250 km of the us7000ti1p epicenter. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "In the 2026-11-03 US midterm elections, Democrats plus independents who caucus with them win at least 51 seats in the Senate that convenes i" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

2732 issued all-time across 16 forecaster arms · 2190 open (153 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 173 issued · 156 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 942 | 825 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 108 | 103 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 173 | 156 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 320 | 295 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 299 | 235 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*