**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082051Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-44 | 30% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry whose vendor or product field identifies Adobe Commerce or Magento, with a dateAdded value between 2026-09-08 and 2026-10-09. | True if the CISA KEV JSON feed, fetched on the deadline, contains at least one entry with vendorProject or product matching Adobe Commerce or Magento and dateAdded between 2026-09-08 and 2026-10-09 inclusive; else false. |
| KKR-20260908-45 | 30% | 2026-12-11 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for the SAP kernel vulnerability publicly designated OVERPASS, with a dateAdded value between 2026-09-08 and 2026-12-08. | True if the CISA KEV feed on the deadline lists an SAP entry whose CVE is identified in SAP or CISA advisories under the OVERPASS designation, with dateAdded between 2026-09-08 and 2026-12-08 inclusive; else false. |
| KKR-20260908-46 | 21% | 2026-10-13 | economics/markets | ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-09 and 2026-10-09. Reference: Brent 97.68 at packet seal on 2026-09-08. | True if any official ICE Brent front-month daily settlement price between 2026-09-09 and 2026-10-09 inclusive is 100.00 USD or higher; else false. Reference level at seal: 97.68. |
| KKR-20260908-47 | 49% | 2026-10-13 | military/conflict | Between 2026-09-09 and 2026-10-09, Saudi authorities publicly acknowledge at least one Houthi missile or drone attack impacting or intercepted over Riyadh province. | True if, for an attack occurring 2026-09-09 to 2026-10-09, Saudi official statements or state media acknowledge a Houthi projectile impacting or intercepted in Riyadh province, or two of Reuters, AP, AFP, BBC so report; else false. |
| KKR-20260908-48 | 49% | 2026-12-11 | military/conflict | A ceasefire or cessation of hostilities covering the current United States and Iran conflict is publicly announced between 2026-09-09 and 2026-12-08 and confirmed by named officials of both governments. | True if, between 2026-09-09 and 2026-12-08, named US and Iranian officials each publicly confirm a ceasefire or halt to hostilities between the two states, reported by two of Reuters, AP, AFP, BBC; else false. |
| KKR-20260908-49 | 35% | 2027-01-12 | political | A presidential document directing federal recognition or renaming of the state of New Mexico as New America is published in the Federal Register between 2026-09-09 and 2027-01-08. | True if the Federal Register publishes an executive order, proclamation, or memorandum directing federal use or recognition of the name New America for New Mexico, with publication date between 2026-09-09 and 2027-01-08; else false. |
| KKR-20260908-50 | 36% | 2027-03-01 | crime/security | French police or prosecutors publicly announce an arrest, or the recovery of at least one stolen painting, in the Renoir Museum theft of early September 2026, between 2026-09-09 and 2027-02-26. | True if, between 2026-09-09 and 2027-02-26, French authorities announce at least one arrest or one recovered painting in the Renoir Museum case, reported by two of Reuters, AP, AFP, BBC, Le Monde; else false. |
| KKR-20260908-51 | 36% | 2026-10-13 | disaster | The USGS earthquake catalog records at least one magnitude 5.0 or greater event within 150 km of USGS event us7000tdvt (the 2026-09-08 M6.3 near Nikolski, Alaska) with origin time between 2026-09-09 and 2026-10-09. | True if a USGS ComCat query on the deadline returns one or more events of magnitude 5.0 or greater within 150 km of event us7000tdvt with origin times between 2026-09-09 and 2026-10-09 inclusive; else false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "NYMEX WTI front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-09-09 and 2026-12-31. Refere" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Council of the European Union adopts a legal act suspending or prohibiting import into the EU of goods produced in Israeli settlements, " → REJECTED: resolution offers alternative VENUES joined by 'or' (…eu council regulation | or | decision suspending or banning…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1729 issued all-time across 16 forecaster arms · 1464 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 530 issued · 502 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 530 | 502 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 235 | 147 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 188 | 186 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 192 | 171 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*