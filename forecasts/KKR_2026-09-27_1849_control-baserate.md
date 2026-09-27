**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271849Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-27_1517.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260927-18 | 64% | 2026-11-04 | military/conflict | The United States and Iran publicly confirm a ceasefire, truce, or halt-to-hostilities agreement that takes effect on a date between 2026-09-28 and 2026-10-31. | TRUE if both the White House or State Department and the Iran Foreign Ministry publicly confirm a ceasefire, truce, or halt to hostilities taking effect between 2026-09-28 and 2026-10-31, as reported by at least two of Reuters, AP, AFP. |
| KKR-20260927-19 | 64% | 2026-12-03 | military/conflict | Forces of the internationally recognized Yemeni government retake the Red Sea port city of Mocha (al-Mokha) from the Houthis on a date between 2026-09-28 and 2026-11-30. | TRUE if the Yemeni government announces control of Mocha city and at least two of Reuters, AP, AFP independently report government forces holding the city, with the recapture dated between 2026-09-28 and 2026-11-30. |
| KKR-20260927-20 | 32% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE affecting Citrix NetScaler ADC or NetScaler Gateway with a dateAdded value between 2026-09-27 and 2026-10-09. | TRUE if the CISA KEV JSON feed contains at least one entry whose product or vulnerabilityName field includes NetScaler and whose dateAdded is between 2026-09-27 and 2026-10-09 inclusive. |
| KKR-20260927-21 | 32% | 2026-10-20 | cyber | CISA issues an Emergency Directive naming Citrix NetScaler ADC or NetScaler Gateway, with an issue date between 2026-09-27 and 2026-10-16. | TRUE if the CISA directives page lists an Emergency Directive (any ED number) naming NetScaler ADC or NetScaler Gateway, dated between 2026-09-27 and 2026-10-16. Binding Operational Directives, alerts, and KEV additions do not count. |
| KKR-20260927-22 | 29% | 2026-10-05 | crime/security | The State of Tennessee carries out the execution of Christa Pike on 2026-09-30 as scheduled. | TRUE if the Tennessee Department of Correction confirms Christa Pike was executed on 2026-09-30 and the Death Penalty Information Center execution database records that date; a stay, reprieve, or commutation resolves FALSE. |
| KKR-20260927-23 | 29% | 2026-11-04 | crime/security | At least one suspect appears in a South African court charged in connection with the 2026-09-26 Wedela tavern mass shooting near Johannesburg, with the first appearance dated between 2026-09-28 and 2026-10-30. | TRUE if SAPS or the National Prosecuting Authority publicly confirms, or two of Reuters, AP, AFP report, a court appearance by at least one accused charged for the Wedela shooting, dated between 2026-09-28 and 2026-10-30. |
| KKR-20260927-24 | 39% | 2026-12-04 | political | Democratic candidates win at least 218 of 435 US House seats in the 2026-11-03 general election, per Associated Press race calls as of 2026-12-04. | TRUE if the AP election results tally, as of 2026-12-04, shows Democratic candidates called as winners in at least 218 US House races from the 2026-11-03 general election. Uncalled races count as not won. |
| KKR-20260927-25 | 31% | 2026-10-30 | disaster | The USGS earthquake catalog records an earthquake of magnitude 6.5 or greater with epicenter within 200 km of USGS event us6000txpi (the 2026-09-26 M6.6 near Tadine, New Caledonia) and origin time between 2026-09-28 and 2026-10-27 UTC. | TRUE if a USGS FDSN event query returns at least one event with USGS preferred magnitude 6.5 or greater, epicenter within 200 km of event us6000txpi, and origin time from 2026-09-28T00:00Z through 2026-10-27T23:59Z. |
| KKR-20260927-26 | 48% | 2026-11-04 | economics/markets | The S&P 500 records at least one close-to-close daily decline of 2.00 percent or more on a trading day between 2026-09-28 and 2026-10-30. Reference: 7743.41 close on the packet date. | TRUE if FRED series SP500 shows any observation dated 2026-09-28 through 2026-10-30 whose close is at least 2.00 percent below the immediately preceding trading day close. Reference level 7743.41 on the packet date. |
| KKR-20260927-27 | 48% | 2026-11-04 | economics/markets | The 10-year US Treasury constant maturity yield (FRED DGS10) prints 5.50 percent or higher on at least one observation dated between 2026-09-28 and 2026-10-30. Reference: 5.18 percent on the packet date. | TRUE if FRED series DGS10 contains any observation dated 2026-09-28 through 2026-10-30 with value 5.50 or greater. Reference level 5.18 percent on the packet date. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2958 issued all-time across 17 forecaster arms · 2416 open (226 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1049 issued · 932 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1049 | 932 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 129 | 124 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 210 | 193 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 27 | 27 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 327 | 263 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*