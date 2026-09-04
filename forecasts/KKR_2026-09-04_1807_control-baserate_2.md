**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041807Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-52 | 30% | 2026-09-29 | cyber | CISA adds CVE-2026-85046, the Chrome V8 type confusion zero-day patched by Google on 2026-09-03, to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-04 and 2026-09-25. | The CISA KEV JSON feed at the deadline contains an entry with cveID CVE-2026-85046 and a dateAdded value from 2026-09-04 through 2026-09-25 inclusive. |
| KKR-20260904-53 | 30% | 2026-12-02 | cyber | CISA adds CVE-2026-20212, the Cisco Nexus 9000 Silicon One unauthenticated root RCE disclosed 2026-09-02 with no known exploitation at seal, to the KEV catalog with a dateAdded between 2026-09-04 and 2026-11-30. | The CISA KEV JSON feed at the deadline contains an entry with cveID CVE-2026-20212 and a dateAdded value from 2026-09-04 through 2026-11-30 inclusive. |
| KKR-20260904-54 | 35% | 2026-09-14 | political | In the Saxony-Anhalt Landtag election held 2026-09-06, the AfD wins an absolute majority of all seats (strictly more than half, counting overhang and leveling seats) in the official preliminary result. | The Landeswahlleiter Sachsen-Anhalt official preliminary result (vorlaeufiges amtliches Endergebnis) for 2026-09-06 shows AfD seats strictly greater than half of all Landtag seats allocated. |
| KKR-20260904-55 | 21% | 2026-09-18 | economics/markets | At its scheduled 2026-09-15 to 2026-09-16 meeting the FOMC raises the federal funds target range above the range held at seal (reference: 3.50 to 3.75 percent on the packet date). | The FOMC statement dated 2026-09-16 on federalreserve.gov, or FRED series DFEDTARL observed for 2026-09-17, shows a target range lower bound above 3.50 percent. |
| KKR-20260904-56 | 21% | 2026-10-13 | economics/markets | CME NYMEX WTI crude (CL) front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-09 (reference: 90.35 on the packet date). | CME Group published daily settlement for the front-month CL contract is at or above 100.00 on at least one trading day from 2026-09-08 through 2026-10-09 inclusive. |
| KKR-20260904-57 | 49% | 2026-09-16 | military/conflict | US envoys Steve Witkoff and/or Jared Kushner are physically present in Kyiv and meet President Zelensky in person between 2026-09-05 and 2026-09-13. | The Office of the President of Ukraine (president.gov.ua) publishes a readout or photographs of the Kyiv meeting, and at least one of Reuters, AP or AFP independently reports the envoys in Kyiv within the window. |
| KKR-20260904-58 | 49% | 2026-10-06 | military/conflict | Houthi forces take control of the Yemeni port city of Mokha (al-Mukha), Taiz governorate, between 2026-09-04 and 2026-10-02. | Either the internationally recognized Yemeni government acknowledges loss of Mokha, or at least two of Reuters, AP and AFP report Houthi forces control the city center and port, for an event dated within the window. |
| KKR-20260904-59 | 35% | 2026-11-03 | political | The Philippine Court of Appeals or Supreme Court issues a temporary restraining order, status quo ante order, or injunction halting the Quezon City RTC Branch 98 grave threats proceedings against Vice President Sara Duterte between 2026-09-04 and 2026-10-30. | An order of the Court of Appeals or Supreme Court dated within the window suspends or enjoins the Branch 98 grave threats proceedings against Duterte, confirmed by the issuing court or by two of Rappler, Inquirer, Philstar, Reuters. |
| KKR-20260904-60 | 36% | 2026-09-29 | crime/security | Between 2026-09-11 and 2026-09-25 the NSW Supreme Court sentences Daniel Billings for the murder of Molly Ticehurst to life imprisonment or to a non-parole period of 30 years or more. | The sentencing judgment (NSW Caselaw, R v Billings) or reporting by ABC and AAP shows a sentence handed down within the window that is life imprisonment or carries a non-parole period of at least 30 years. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "An earthquake of magnitude 6.0 or greater occurs within 200 km of the 2026-09-03 M6.3 Nikolski, Alaska epicenter (52.258N, 169.409W) with or" → REJECTED: the resolution names a different subject than the statement — the claim is about Alaska, Nikolski and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1464 issued all-time across 16 forecaster arms · 1199 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 419 issued · 391 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 419 | 391 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*