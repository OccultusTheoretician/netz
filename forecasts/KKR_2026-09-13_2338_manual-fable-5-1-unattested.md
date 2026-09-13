**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 132338Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260913-24 | 40% | 2026-10-07 | military/conflict | Between 2026-09-14 and 2026-10-04, a merchant vessel is struck by a projectile, hit by an uncrewed surface craft, boarded, or seized in the Red Sea, Bab al-Mandeb, or Gulf of Aden. | TRUE if UKMTO publishes an incident dated 2026-09-14 to 2026-10-04 reporting a merchant vessel struck by a projectile, hit by an uncrewed craft, boarded, or seized in the Red Sea, Bab al-Mandeb, or Gulf of Aden; FALSE otherwise. |
| KKR-20260913-25 | 30% | 2026-10-14 | military/conflict | Between 2026-09-14 and 2026-10-11, at least one Russian-launched military drone or missile enters Polish airspace, as confirmed by the Operational Command of the Polish Armed Forces or the Polish Ministry of National Defence. | TRUE if the Operational Command of the Polish Armed Forces or the Polish Ministry of National Defence publicly confirms a Russian-launched drone or missile entered Polish airspace on a date between 2026-09-14 and 2026-10-11; FALSE otherwise. |
| KKR-20260913-26 | 15% | 2026-10-14 | political | Between 2026-09-14 and 2026-10-11, US and Iranian officials at cabinet, foreign-minister, or presidential special-envoy level hold a direct in-person meeting confirmed by both governments. | TRUE if the US State Department or White House and the Foreign Ministry of Iran both confirm a direct in-person meeting at that level held between 2026-09-14 and 2026-10-11; indirect or mediated exchanges do not count. |
| KKR-20260913-27 | 25% | 2027-02-02 | political | Between 2026-09-14 and 2027-01-29, a member of the Sweden Democrats is appointed as a minister in the Swedish government. | TRUE if the Government Offices of Sweden (regeringen.se) list of ministers as of 2027-01-29 includes a Sweden Democrats member appointed between 2026-09-14 and 2027-01-29; FALSE otherwise. |
| KKR-20260913-28 | 25% | 2026-10-05 | economics/markets | The CME NYMEX WTI crude oil November 2026 futures contract (CLX26) settles at or above 110.00 USD per barrel on 2026-10-02. Reference: 100.05 front-month WTI on the packet date. | TRUE if the official CME Group settlement price for CLX26 on 2026-10-02 is 110.00 or higher; FALSE if below 110.00. Reference: 100.05 front-month WTI on the packet date. |
| KKR-20260913-29 | 15% | 2026-10-20 | cyber | Between 2026-09-14 and 2026-10-16, CISA adds a Tencent vulnerability (including Sogou Input Method, CVE-2026-51990) to the Known Exploited Vulnerabilities catalog. | TRUE if the CISA KEV JSON feed carries an entry whose vendorProject is Tencent or whose product includes Sogou, with dateAdded between 2026-09-14 and 2026-10-16; FALSE otherwise. |
| KKR-20260913-30 | 50% | 2026-12-01 | crime/security | Between 2026-09-14 and 2026-11-27, a Terrebonne Parish grand jury returns an indictment charging Kaegan Jude Solet with at least one count of first-degree or second-degree murder for the Houma, Louisiana stabbings. | TRUE if the 32nd Judicial District Court docket or the Terrebonne Parish District Attorney confirms a grand jury indictment on first- or second-degree murder returned between 2026-09-14 and 2026-11-27; FALSE otherwise. |
| KKR-20260913-31 | 40% | 2026-09-30 | disaster | The confirmed death toll from the Virgo Transport 8 ferry capsizing in the Java Sea reaches at least 50 by 2026-09-27, per Basarnas or the Indonesian Ministry of Transportation. | TRUE if Basarnas or the Indonesian Ministry of Transportation reports cumulative confirmed deaths of 50 or more on or before 2026-09-27; persons listed as missing do not count as confirmed deaths. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-14 and 2026-09-27, at least one merchant vessel is struck, attacked, boarded, or seized in the Strait of Hormuz, Gulf of Oma" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the ukmto website | or | official x account publishes an incident or w…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-14 and 2026-09-27, Iran and Oman (or Iran and any other GCC member state) sign an agreement or memorandum on shipping throug" → REJECTED: resolution offers alternative VENUES joined by 'or' (…meeting | or | joint…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2043 issued all-time across 16 forecaster arms · 1707 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 90 issued · 90 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 657 | 619 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*