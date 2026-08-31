**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-30_1516.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-34 | 53% | 2026-09-30 | military/conflict | A single Russian strike on Kyiv occurring between 2026-09-07 and 2026-09-27 produces an official Ukrainian death toll of 10 or more for that one attack. | TRUE if, for one attack occurring between 2026-09-07 and 2026-09-27, the State Emergency Service of Ukraine or the Kyiv City Military Administration states a death toll of 10 or more for that attack, and Reuters or AFP carries that figure by 2026-09-30. Cumulative multi-day totals do not count. |
| KKR-20260831-35 | 53% | 2026-12-09 | military/conflict | The individual serving as head of state of Niger on 2026-09-07 ceases to hold that office at some point between 2026-09-07 and 2026-12-06. | TRUE if Reuters and AFP both report, by 2026-12-09, that the person serving as head of state of Niger on 2026-09-07 no longer holds that office as of any date on or before 2026-12-06, whether by removal, resignation, death, or transfer of power. |
| KKR-20260831-36 | 33% | 2026-11-09 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry naming WordPress or a WordPress plugin or theme, with a dateAdded value between 2026-09-07 and 2026-11-06. | TRUE if the CISA KEV catalog JSON, fetched on 2026-11-09, contains at least one record whose vendorProject or product field references WordPress or a WordPress plugin or theme, and whose dateAdded falls between 2026-09-07 and 2026-11-06 inclusive. |
| KKR-20260831-37 | 33% | 2026-10-19 | cyber | Manchester Airports Group confirms unauthorized access to its systems in an attributable statement issued between 2026-08-31 and 2026-10-16. | TRUE if a named Manchester Airports Group spokesperson or an official company statement acknowledging unauthorized access to its systems or theft of its data is carried by at least two of BBC News, Reuters, and BleepingComputer, dated between 2026-08-31 and 2026-10-16, and verifiable by 2026-10-19. |
| KKR-20260831-38 | 25% | 2026-12-07 | economics/markets | The US Treasury daily par yield curve records a 10-year constant maturity yield of 5.00 percent or higher on at least one business day between 2026-09-08 and 2026-12-04. | TRUE if the Treasury daily par yield curve published at home.treasury.gov, or FRED series DGS10, shows a 10-year value of 5.00 or above on any business day from 2026-09-08 through 2026-12-04, checked on 2026-12-07. |
| KKR-20260831-39 | 52% | 2026-10-19 | disaster | The confirmed cumulative death toll for the August 2026 Nepal-Tibet flood event reaches 1,000 or more in official figures issued between 2026-09-07 and 2026-10-16. | TRUE if a cumulative confirmed toll of 1,000 or more for this event, attributed to the National Disaster Risk Reduction and Management Authority of Nepal, the Nepali Ministry of Home Affairs, or Chinese state authorities, is carried by at least two of Reuters, AFP, Al Jazeera, and the Guardian, dated on or before 2026-10-16 and verifiable by 2026-10-19. Missing-persons counts do not count toward the total. |
| KKR-20260831-40 | 43% | 2027-02-02 | crime/security | The Crown Prosecution Service announces a decision to bring criminal charges against at least one former undercover police officer in the undercover policing matter, between 2026-09-07 and 2027-01-29. | TRUE if the Crown Prosecution Service publishes a charging decision, or is reported by both the Guardian and BBC News to have made one, bringing criminal charges against at least one former undercover officer in connection with the undercover policing scandal, dated between 2026-09-07 and 2027-01-29 and verifiable by 2027-02-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Front-month NYMEX WTI crude settles at or above 95.00 US dollars per barrel on at least one trading day between 2026-09-08 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about Front, NYMEX, WTI and the resolution settles on CL, CME, Crude, Group. A row whose resolution checks a different fact can be scored correct while being wrong
- "A wildfire with an ignition date between 2026-08-31 and 2026-09-27 in Siskiyou County, California reaches a reported size of 10,000 acres or" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…an incident on inciweb | or | in the nifc incident record, located in siski…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Federal Register publishes at least one Presidential Document adjusting duties on steel or aluminum imports into the United States, with" → REJECTED: cited items name Canada; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

1163 issued all-time across 14 forecaster arms · 1002 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 297 issued · 280 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 297 | 280 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 114 | 113 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 142 | 139 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 130 | 122 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*