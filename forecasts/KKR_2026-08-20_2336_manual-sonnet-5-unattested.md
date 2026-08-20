**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 202336Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-20_1537.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260820-15 | 50% | 2026-08-31 | military_conflict | Between 2026-08-20 and 2026-08-29, Russia will conduct another missile or drone strike on Kyiv, distinct from the strike already reported on 2026-08-20, confirmed by at least two of Reuters, AP, BBC, or Guardian. | TRUE if at least two of Reuters, AP, BBC, or Guardian report a new Russian missile or drone strike hitting Kyiv city limits between 2026-08-20 and 2026-08-29, distinct from the strike reported on 2026-08-20. |
| KKR-20260820-16 | 22% | 2026-09-01 | disaster_infrastructure | Between 2026-08-20 and 2026-08-28, GDACS will upgrade its overall alert level for Central Pacific tropical cyclone TWO-C-26, GDACS event 1001306, from Green to Orange or Red. | TRUE if the GDACS event page for eventid 1001306, eventtype TC, shows an Orange or Red overall alert level at any point between 2026-08-20 and 2026-08-28. |
| KKR-20260820-17 | 18% | 2026-09-02 | military_conflict | Between 2026-08-20 and 2026-08-30, a commercial vessel transiting the Strait of Hormuz will be attacked, mined, or seized, confirmed by two or more of UKMTO, US Fifth Fleet, Reuters, or AP. | TRUE if two or more of UKMTO, US Fifth Fleet/CENTCOM, Reuters, or AP report an attack, mining, or seizure of a commercial vessel in the Strait of Hormuz between 2026-08-20 and 2026-08-30. |
| KKR-20260820-18 | 40% | 2026-09-03 | cyber | Between 2026-08-20 and 2026-08-31, CISA will add CVE-2026-73570, the actively exploited Zimbra Collaboration Suite SNMP command-injection flaw, to the Known Exploited Vulnerabilities catalog. | TRUE if the CISA KEV catalog carries a dateAdded value for CVE-2026-73570 between 2026-08-20 and 2026-08-31. |
| KKR-20260820-19 | 58% | 2026-09-14 | economic | Between 2026-08-20 and 2026-09-10, the US Treasury OFAC Specially Designated Nationals list will add one or more new Iran-program designations under the economic isolation campaign Trump announced on 2026-08-19. | TRUE if OFAC SDN List data shows one or more new Iran-program designations with a listing date between 2026-08-20 and 2026-09-10. |
| KKR-20260820-20 | 28% | 2026-09-16 | economic | On 2026-09-15, NYMEX WTI crude oil front-month futures will settle at or above 92.00 USD per barrel, up from the 86.42 USD close reported on 2026-08-20. | TRUE if the NYMEX WTI front-month futures settlement price on 2026-09-15 is at or above 92.00 USD per barrel per CME Group settlement data. |
| KKR-20260820-21 | 8% | 2026-09-23 | political | Between 2026-08-20 and 2026-09-20, Zelenskyy or the Ukrainian government will officially announce a specific date for a wartime presidential election, confirmed by two or more major wire services. | TRUE if the Ukrainian presidency or Central Election Commission announces a specific wartime presidential election date between 2026-08-20 and 2026-09-20, confirmed by two or more of Reuters, AP, or AFP. |
| KKR-20260820-22 | 50% | 2026-09-28 | crime_security | Between 2026-08-20 and 2026-09-24, Jewel Howard-Taylor, former Vice President of Liberia charged 2026-08-19 with drug trafficking and money laundering, will make a first court appearance in Liberia, reported by Reuters, AP, or BBC. | TRUE if Reuters, AP, or BBC report a first court appearance, arraignment, or bail hearing for Jewel Howard-Taylor in a Liberian court between 2026-08-20 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-08, the CME CF Bitcoin Reference Rate will fix at or above 80,000.00 USD, up from the roughly 72,571 USD level reported on 2026-0" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-08 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

817 issued all-time across 14 forecaster arms · 727 open (14 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 77 issued · 76 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 113 | 101 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 67 | 67 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 77 | 76 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*