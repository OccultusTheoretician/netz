**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082051Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: manual/sonnet-5/unattested · 5 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-16 | 47% | 2026-10-01 | cyber | CVE-2026-75650, the Adobe Commerce and Magento Open Source remote code execution flaw Adobe confirmed as actively exploited on 2026-09-08, is added to the CISA Known Exploited Vulnerabilities catalog between 2026-09-08 and 2026-09-29. | The CISA KEV catalog lists CVE-2026-75650 with a dateAdded value between 2026-09-08 and 2026-09-29 inclusive. |
| KKR-20260908-17 | 16% | 2026-10-12 | cyber | The SAP kernel vulnerability SAP disclosed on 2026-09-08 under the codename OVERPASS, rated maximum severity, is added to the CISA Known Exploited Vulnerabilities catalog between 2026-09-08 and 2026-10-08. | The CISA KEV catalog lists an SAP kernel CVE matching the OVERPASS advisory with a dateAdded value between 2026-09-08 and 2026-10-08 inclusive. |
| KKR-20260908-18 | 37% | 2026-10-12 | crime_security | French police publicly announce at least one arrest of a suspect linked to the 2026-09-08 theft of paintings from the Musee Renoir in Cagnes-sur-Mer, between 2026-09-08 and 2026-10-08. | A mainstream outlet reports French authorities have arrested and identified a suspect connected to the Cagnes-sur-Mer Renoir Museum theft, on or before 2026-10-08. |
| KKR-20260908-19 | 58% | 2026-10-01 | disaster_infrastructure | A named humanitarian body publicly reports the closure or suspension of services at one or more specific Sudanese hospitals due to healthcare system collapse, between 2026-09-08 and 2026-09-29. | MSF, WHO, or another named humanitarian or UN body states in public reporting that a specific named Sudanese hospital or facility suspended or ceased operating due to collapse, within the window. |
| KKR-20260908-20 | 63% | 2026-10-12 | political | OFAC adds at least one additional Iran-program entity or individual to the SDN list, beyond the airlines sanctioned per 2026-09-08 reporting, between 2026-09-09 and 2026-10-08. | The US Treasury OFAC Specially Designated Nationals list shows a new Iran-program listing dated after 2026-09-08 and on or before 2026-10-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent crude front-month futures close at or above 105.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-09. R" → REJECTED: cited items name Iran, Islamic Republic of; the claim is about Saudi Arabia — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Saudi Arabia or the Saudi-led coalition conducts publicly reported airstrikes on Houthi military targets in Yemen between 2026-09-08 and 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…at least two independent wire services | or | outlets (reuters, ap, afp, bbc, al jazeera) r…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The government of Israel publicly reverses or suspends its 2026-09-08 order to close the United Kingdom consulate in Jerusalem, between 2026" → REJECTED: resolution offers alternative VENUES joined by 'or' (…israeli government statement | or | mainstream…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The government of Russia orders or carries out the expulsion of Hungarian diplomats as a reciprocal measure for the 2026-09-08 expulsion of " → REJECTED: resolution offers alternative VENUES joined by 'or' (…russian foreign ministry | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1698 issued all-time across 16 forecaster arms · 1433 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 192 issued · 171 open · 21 resolved · 10 hits / 11 misses · **Brier 0.214** against its own base rate 47.6% (climatological 0.249) · **skill +0.141** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 512 | 484 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 235 | 147 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 192 | 171 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*