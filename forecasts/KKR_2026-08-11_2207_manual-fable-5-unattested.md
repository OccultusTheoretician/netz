**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112207Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-11_1750.md · forecaster: manual/fable-5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260811-10 | 92% | 2026-09-15 | military/conflict | At least one Russian missile or drone strike on Kyiv city between 2026-08-12 and 2026-09-11 is acknowledged by Ukrainian officials and reported by at least two international wire services. | TRUE if Ukrainian officials acknowledge and two of Reuters, AP, AFP report at least one Russian air attack impacting Kyiv city with strike date between 2026-08-12 and 2026-09-11. |
| KKR-20260811-11 | 25% | 2026-12-03 | political | The United States and Iran jointly announce a signed ceasefire or framework agreement between 2026-08-12 and 2026-11-30. | TRUE if the US government and the government of Iran each officially confirm a signed ceasefire or framework agreement announced between 2026-08-12 and 2026-11-30, per two international wire services. |
| KKR-20260811-12 | 20% | 2026-10-02 | economics/markets | NYMEX WTI crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-12 and 2026-09-30. | TRUE if CME official settlement data show the WTI front-month contract settling at or above 100.00 USD on any trading day between 2026-08-12 and 2026-09-30. |
| KKR-20260811-13 | 85% | 2026-12-18 | economics/markets | The New York Fed Quarterly Report on Household Debt and Credit covering Q3 2026, published between 2026-11-01 and 2026-12-15, states aggregate credit card balances at or above 1.26 trillion USD. | TRUE if the NY Fed Q3 2026 Household Debt and Credit report, released between 2026-11-01 and 2026-12-15, states aggregate credit card balances at or above 1.26 trillion USD. |
| KKR-20260811-14 | 35% | 2026-11-04 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Microsoft SharePoint vulnerability with a dateAdded value between 2026-08-12 and 2026-10-31. | TRUE if the CISA KEV catalog contains at least one entry whose product field references SharePoint and whose dateAdded falls between 2026-08-12 and 2026-10-31. |
| KKR-20260811-15 | 30% | 2026-12-08 | cyber | CISA publishes a new cybersecurity advisory, distinct from any existing on 2026-08-11, that names Gunra ransomware, with publication date between 2026-08-12 and 2026-12-04. | TRUE if the cisa.gov advisories index lists an advisory first published between 2026-08-12 and 2026-12-04 whose text names Gunra. |
| KKR-20260811-16 | 65% | 2026-09-14 | disaster | The UK Met Office announces between 2026-09-01 and 2026-09-10 that summer 2026 was the warmest summer on record for the UK in its national temperature series. | TRUE if a Met Office publication dated between 2026-09-01 and 2026-09-10 states summer 2026 set the UK record for warmest summer in its series. |
| KKR-20260811-17 | 5% | 2027-02-03 | crime/security | Russian authorities transfer Bashar al-Assad to Syrian government custody between 2026-08-12 and 2027-01-31. | TRUE if two of Reuters, AP, AFP report that Assad was transferred from Russia into Syrian government custody with transfer date between 2026-08-12 and 2027-01-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A merchant vessel is struck by a Houthi-launched weapon in the Red Sea, Gulf of Aden, or Arabian Sea between 2026-08-12 and 2026-09-30." → REJECTED: cited items name Philippines; the claim is about Djibouti, Egypt, Eritrea, Saudi Arabia, Sudan, Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Philippines; the claim is about Djibouti, Egypt, Eritrea, Saudi Arabia, Sudan, Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The USGS catalog records an earthquake of magnitude 6.0 or greater within 250 km of Colombia mainshock us6000tjl2 with origin time between 2" → REJECTED: the resolution names only a venue or register (USGS) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

473 issued all-time across 14 forecaster arms · 417 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 20 issued · 20 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*