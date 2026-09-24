**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241643Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-24_1520.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260924-22 | 60% | 2026-10-12 | military/conflict | Houthi forces fire at least one ballistic missile, cruise missile, or armed drone that the Saudi-led coalition says it intercepted or destroyed, in an incident occurring between 2026-09-25 and 2026-10-08. | TRUE if a Saudi-led coalition statement, carried by the Saudi Press Agency or at least two of Reuters, AP, AFP, Al Jazeera, reports such an interception dated between 2026-09-25 and 2026-10-08. |
| KKR-20260924-23 | 55% | 2026-10-28 | military/conflict | Armed clashes between Ethiopian federal forces and Tigrayan armed forces of any faction take place on at least one day between 2026-10-12 and 2026-10-25. | TRUE if at least two of Reuters, AP, AFP, and BBC report fighting between Ethiopian federal forces and Tigrayan forces that occurred between 2026-10-12 and 2026-10-25; fighting dated earlier does not count. |
| KKR-20260924-24 | 45% | 2026-10-27 | economics/markets | The 10-year US Treasury constant-maturity yield closes at or above 5.35 percent on at least one trading day between 2026-09-25 and 2026-10-23. Reference: 5.14 percent on the packet date. | TRUE if FRED series DGS10 records a value of 5.35 or higher for any date between 2026-09-25 and 2026-10-23 inclusive; FALSE otherwise. |
| KKR-20260924-25 | 33% | 2026-10-27 | economics/markets | ICE Brent front-month crude futures settle at or above 110.00 dollars per barrel on at least one trading day between 2026-09-25 and 2026-10-23. Reference: 101.42 on the packet date. | TRUE if the ICE Futures Europe daily settlement for the front-month Brent contract is 110.00 or higher on any trading day between 2026-09-25 and 2026-10-23 inclusive; FALSE otherwise. |
| KKR-20260924-26 | 65% | 2026-10-12 | cyber | CISA adds the WordPress vulnerability CVE-2026-87902 to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-24 and 2026-10-08. | TRUE if the CISA KEV catalog carries an entry with cveID CVE-2026-87902 whose dateAdded falls between 2026-09-24 and 2026-10-08 inclusive; FALSE otherwise. |
| KKR-20260924-27 | 30% | 2026-10-12 | cyber | CISA adds CVE-2026-48842, the Roundcube Webmail virtuser_query SQL injection flaw, to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-24 and 2026-10-08. | TRUE if the CISA KEV catalog carries an entry with cveID CVE-2026-48842 whose dateAdded falls between 2026-09-24 and 2026-10-08 inclusive; FALSE otherwise. |
| KKR-20260924-28 | 12% | 2026-12-17 | political | Vladimir Putin attends the G20 leaders summit at Trump National Doral in Doral, Florida, in person on 2026-12-14 or 2026-12-15. | TRUE if the Kremlin or at least two of Reuters, AP, AFP confirm Putin was physically present at the summit on 2026-12-14 or 2026-12-15; video participation or a delegation without Putin resolves FALSE. |
| KKR-20260924-29 | 50% | 2026-11-24 | political | The US Supreme Court grants, in whole or in part, a federal government application to stay or vacate a lower-court order restricting deportations to third countries, by an order entered between 2026-09-25 and 2026-11-20. | TRUE if the supremecourt.gov docket shows an order granting such an application in whole or in part, entered between 2026-09-25 and 2026-11-20; an administrative stay alone, a denial, or no ruling resolves FALSE. |
| KKR-20260924-30 | 40% | 2026-10-27 | crime/security | Polish authorities charge or detain at least one person in connection with the Starlink station fire that Polish authorities have called sabotage, with the charge or detention occurring between 2026-09-25 and 2026-10-23. | TRUE if Polish prosecutors, police, or the ABW announce, or at least two of Reuters, AP, AFP, PAP report, a charge (including in absentia) or detention tied to the fire made between 2026-09-25 and 2026-10-23. |
| KKR-20260924-31 | 35% | 2026-10-02 | disaster | The National Weather Service issues a Hurricane Warning for at least one Hawaii zone between 2026-09-24 and 2026-09-30 UTC. | TRUE if the NWS alert record, via the NWS API or the Iowa Environmental Mesonet VTEC archive, shows a Hurricane Warning (HU.W) issued by WFO Honolulu between 2026-09-24 and 2026-09-30 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2798 issued all-time across 17 forecaster arms · 2256 open (170 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 10 issued · 10 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 972 | 855 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 113 | 108 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 181 | 164 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 10 | 10 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 306 | 242 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*