**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112207Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-11_1750.md · forecaster: manual/opus-5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260811-18 | 50% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendorProject is Fortinet or Schneider Electric, with dateAdded between 2026-08-12 and 2026-10-30. | TRUE if the CISA KEV JSON feed holds at least one entry with vendorProject Fortinet or Schneider Electric and a dateAdded value between 2026-08-12 and 2026-10-30 inclusive. |
| KKR-20260811-19 | 30% | 2026-10-20 | cyber | The CISA KEV catalog adds at least one new Microsoft SharePoint Server CVE, with dateAdded between 2026-08-12 and 2026-10-16. | TRUE if a KEV entry whose product field names SharePoint carries a dateAdded between 2026-08-12 and 2026-10-16 inclusive and was absent from the catalog on 2026-08-11. |
| KKR-20260811-20 | 32% | 2026-12-03 | military_conflict | The US Treasury designates at least one person or entity for facilitating North Korean arms or missile transfers to Russia, with the action dated between 2026-08-12 and 2026-11-30. | TRUE if an OFAC press release or SDN list update dated inside the window names DPRK-to-Russia arms, missile, or munitions transfer as a basis for the designation. |
| KKR-20260811-21 | 40% | 2026-10-05 | military_conflict | United States and Iranian officials hold a publicly acknowledged direct bilateral meeting between 2026-08-12 and 2026-09-30. | TRUE if a US executive branch statement and an Iranian foreign ministry statement both confirm a direct bilateral meeting held inside the window, and two of Reuters, AP, AFP report it. |
| KKR-20260811-22 | 28% | 2026-10-02 | economics | NYMEX front-month WTI crude futures settle at or above 95.00 US dollars per barrel on at least one trading day between 2026-08-12 and 2026-09-30. | TRUE if the CME published settlement price for the front-month WTI contract is 95.00 or higher on any trading day between 2026-08-12 and 2026-09-30 inclusive. |
| KKR-20260811-23 | 80% | 2026-11-20 | economics | The New York Fed Household Debt and Credit Report for Q3 2026 reports aggregate credit card balances above 1.26 trillion US dollars. | TRUE if the Q3 2026 report published on newyorkfed.org states an aggregate credit card balance greater than 1.26 trillion dollars, published on or before the deadline. |
| KKR-20260811-24 | 35% | 2026-12-04 | crime_security | Thailand adopts a cabinet resolution or statutory amendment permanently tightening civilian firearm permit rules, adopted between 2026-08-12 and 2026-11-30. | TRUE if a Thai government announcement plus reporting by two of Reuters, AP, AFP, Bangkok Post confirm a cabinet resolution or Firearms Act amendment adopted inside the window. |
| KKR-20260811-25 | 22% | 2026-10-05 | disaster | The USGS catalog lists at least one magnitude 6.0 or greater earthquake within 300 km of USGS event us6000tjl2, with origin time between 2026-08-12 and 2026-09-30. | TRUE if the USGS FDSN event query returns at least one M6.0 or greater event within 300 km of the us6000tjl2 epicenter with origin time inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A US federal court enters an order blocking enforcement of the administration policy limiting birthright citizenship, with the order dated b" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "CAL FIRE reports the Timber Fire near Big Sur at 100 percent containment, with a containment date between 2026-08-12 and 2026-09-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

481 issued all-time across 14 forecaster arms · 425 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 39 issued · 39 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 46 | 46 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 53 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 39 | 39 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*