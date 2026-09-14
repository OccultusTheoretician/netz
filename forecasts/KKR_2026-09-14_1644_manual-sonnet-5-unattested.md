**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141644Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260914-07 | 25% | 2026-10-08 | military_conflict | Russia conducts another missile or drone strike hitting rail infrastructure within 50 kilometers of the Ukraine-Poland border between 2026-09-15 and 2026-10-05, following the strike near that border reported on 14 September 2026. | TRUE if at least two of Reuters, AP, Ukrzaliznytsia (Ukrainian state railways), or a Polish government statement confirm a Russian missile or drone strike hit rail infrastructure (track, station, or rolling stock) within 50 km of the Ukraine-Poland border at any point between 2026-09-15 and 2026-10-05. FALSE otherwise. |
| KKR-20260914-08 | 58% | 2026-10-08 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for the GitLab vulnerability reported as under active exploitation on 14 September 2026, with a dateAdded value between 2026-09-15 and 2026-10-06. | TRUE if the CISA KEV catalog (cisa.gov known_exploited_vulnerabilities JSON feed) contains an entry for a GitLab product vulnerability with a dateAdded value between 2026-09-15 and 2026-10-06. FALSE otherwise. |
| KKR-20260914-09 | 62% | 2026-10-12 | economic | The 10-Year US Treasury yield closes at or above 5.00 percent on at least one business day between 2026-09-15 and 2026-10-09. Reference: 4.99 percent on the packet date, 2026-09-14. | TRUE if the FRED DGS10 series or the US Treasury daily par yield curve rate for the 10-year tenor shows a value of 5.00 percent or higher for any business day between 2026-09-15 and 2026-10-09. FALSE otherwise. |
| KKR-20260914-10 | 32% | 2026-10-12 | economic | WTI crude oil (NYMEX front-month contract) settles at or above 110.00 USD per barrel on at least one trading day between 2026-09-15 and 2026-10-09. Reference: 103.36 USD per barrel on the packet date, 2026-09-14. | TRUE if the NYMEX WTI front-month futures settlement price is 110.00 USD per barrel or higher on any trading day between 2026-09-15 and 2026-10-09, as reported by CME Group settlement data or two of Reuters, Bloomberg, or CNBC. FALSE otherwise. |
| KKR-20260914-11 | 15% | 2026-10-15 | political | Gulf states and Iran hold and conclude a meeting on Strait of Hormuz safe passage or de-confliction, producing a joint statement or announced agreement, between 2026-09-15 and 2026-10-13, after three postponements reported through 14 September 2026. | TRUE if at least two of Reuters, AP, Al Jazeera, Iranian state media, or a Gulf state government statement confirm a Gulf states-Iran meeting on Hormuz concluded with a joint statement or announced agreement between 2026-09-15 and 2026-10-13. FALSE otherwise. |
| KKR-20260914-12 | 10% | 2026-10-15 | disaster_infrastructure | GDACS raises its alert level for the Angola forest fire event, GDACS event ID 1031945, green as of 14 September 2026, to Orange or Red, between 2026-09-15 and 2026-10-13. | TRUE if the GDACS report page for event ID 1031945 (eventtype WF) shows an Orange or Red alert level at any point between 2026-09-15 and 2026-10-13. FALSE if it remains Green or is closed or archived without upgrade. |
| KKR-20260914-13 | 28% | 2026-11-18 | political | The EPA publishes a proposed or final rule in the Federal Register repealing or replacing the current federal carbon dioxide emission standards for power plants, between 2026-09-21 and 2026-11-16, following the reporting on 14 September 2026 that the agency is poised to act. | TRUE if a Federal Register document from the EPA proposing or finalizing repeal or replacement of the power-plant CO2 emission standards is published at any point between 2026-09-21 and 2026-11-16. FALSE otherwise. |
| KKR-20260914-14 | 12% | 2026-11-18 | crime_security | The Criminal Cases Review Commission announces a decision on whether to refer Lucy Letby's convictions to the Court of Appeal, between 2026-09-21 and 2026-11-16. | TRUE if the CCRC or at least two of BBC, Guardian, or Reuters report that the CCRC has announced a decision, either referral or non-referral, on the Letby case between 2026-09-21 and 2026-11-16. FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The US Senate passes the Clarity Act (digital asset market structure legislation) via a floor vote held between 2026-09-15 and 2026-09-17, t" → REJECTED: resolution offers alternative VENUES joined by 'or' (…congress.gov | or | senate.gov…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A Houthi or other Iran-aligned force conducts another attack on Saudi Arabia's oil infrastructure, such as a pipeline, refinery, storage sit" → REJECTED: resolution offers alternative VENUES joined by 'or' (…saudi government | or | saudi aramco…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2083 issued all-time across 16 forecaster arms · 1747 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 234 issued · 202 open · 32 resolved · 16 hits / 16 misses · **Brier 0.224** against its own base rate 50.0% (climatological 0.250) · **skill +0.105**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 674 | 636 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*