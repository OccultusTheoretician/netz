**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121717Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-12_1518.md · forecaster: manual/opus-5/unattested · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260812-11 | 65% | 2026-09-23 | military/conflict | North Korea conducts at least one further ballistic missile launch between 2026-08-13 and 2026-09-20. | True if South Korea's Joint Chiefs of Staff confirm a North Korean ballistic missile launch dated between 2026-08-13 and 2026-09-20, carried by at least two of Yonhap, Reuters, and Associated Press. |
| KKR-20260812-12 | 22% | 2026-10-19 | military/conflict | Russian forces seize or detain at least one commercial vessel flagged in or operated from an EU member state between 2026-08-13 and 2026-10-15. | True if at least two of Reuters, Associated Press, and the flag state government confirm Russian seizure or detention of a named EU-flagged or EU-operated commercial vessel between 2026-08-13 and 2026-10-15. |
| KKR-20260812-13 | 45% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog gains an entry naming Microsoft SharePoint Server or VMware vCenter Server with a date-added value between 2026-08-13 and 2026-10-30. | True if the CISA KEV JSON feed contains an entry whose product field names SharePoint Server or vCenter Server with a dateAdded between 2026-08-13 and 2026-10-30 inclusive. |
| KKR-20260812-14 | 70% | 2026-08-24 | political | The Electoral Commission of Zambia declares Hakainde Hichilema elected president in the first round, announced between 2026-08-13 and 2026-08-20. | True if the ECZ formally declares Hichilema president-elect between 2026-08-13 and 2026-08-20 with more than 50 percent of valid votes, avoiding a runoff. |
| KKR-20260812-15 | 28% | 2026-10-19 | disaster | The USGS earthquake catalog records at least one magnitude 6.0 or greater earthquake located in Colombia with origin time between 2026-08-13 and 2026-10-15. | True if USGS ANSS ComCat lists an event of magnitude 6.0 or above whose place field names Colombia with origin time between 2026-08-13 and 2026-10-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The US headline CPI-U 12-month change for August 2026, published by BLS on 2026-09-11, is higher than the 12-month change published for July" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-11 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The FOMC leaves the federal funds target range unchanged at 3.50 to 3.75 percent at the meeting concluding 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Front-month ICE Brent crude futures settle at or above 100.00 US dollars per barrel on at least one trading day between 2026-08-13 and 2026-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A named commercial vessel is attacked, seized, or forcibly boarded in the Strait of Hormuz or Gulf of Oman between 2026-08-13 and 2026-09-30" → REJECTED: the resolution names a different subject than the statement — the claim is about Gulf, Hormuz, Oman, Strait and the resolution settles on Associated, BBC, Jazeera, Press. A row whose resolution checks a different fact can be scored correct while being wrong
- "CISA publishes an advisory naming Iranian state-sponsored or Iran-aligned cyber actors targeting US water or wastewater systems, dated betwe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…aa | or | icsa…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

532 issued all-time across 14 forecaster arms · 476 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 44 issued · 44 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 72 | 72 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 57 | 55 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 26 | 26 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*