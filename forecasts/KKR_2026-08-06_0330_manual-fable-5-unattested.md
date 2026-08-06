**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-05_1501.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260806-09 | 35% | 2026-10-05 | military/conflict | The United States and Iran both publicly confirm a concluded agreement governing commercial transit of the Strait of Hormuz between 2026-08-06 and 2026-09-30. | TRUE if official US and Iranian government statements confirming a concluded Hormuz transit agreement are issued in the window and reported by at least two of Reuters, AP, AFP; FALSE otherwise. |
| KKR-20260806-10 | 60% | 2026-11-04 | military/conflict | A Russian missile or drone strike on Kyiv city kills at least 5 people in a single attack between 2026-08-06 and 2026-10-31, per Ukrainian official casualty statements. | TRUE if Ukrainian authorities state at least 5 killed in one strike on Kyiv city within the window, reported by at least two international news outlets; FALSE otherwise. |
| KKR-20260806-11 | 25% | 2026-11-03 | cyber | The CISA KEV catalog adds at least one entry for Gitea, n8n, or TP-Link Omada with a date-added value between 2026-08-06 and 2026-10-30. | TRUE if the public CISA KEV catalog contains an entry whose vendor or product names Gitea, n8n, or TP-Link Omada with dateAdded between 2026-08-06 and 2026-10-30; FALSE otherwise. |
| KKR-20260806-12 | 85% | 2026-10-05 | cyber | The CISA KEV catalog adds at least 12 new entries with date-added values between 2026-08-06 and 2026-09-30. | TRUE if the public CISA KEV catalog contains 12 or more entries with dateAdded between 2026-08-06 and 2026-09-30 inclusive; FALSE otherwise. |
| KKR-20260806-13 | 55% | 2026-12-01 | political | Abdul El-Sayed wins the Michigan US Senate general election held 2026-11-03. | TRUE if AP declares El-Sayed the winner or Michigan certified results show him with the most votes for US Senate; FALSE otherwise. |
| KKR-20260806-14 | 25% | 2027-02-01 | political | Pete Hegseth departs the office of US Secretary of War, via announced resignation or removal, between 2026-08-06 and 2027-01-30. | TRUE if the White House or the department officially announces the resignation, removal, or departure of Hegseth with the announcement dated in the window, reported by two major outlets; FALSE otherwise. |
| KKR-20260806-15 | 50% | 2026-09-08 | disaster | The USGS catalog records at least one magnitude 5.0 or greater earthquake within 100 km of the 2026-08-05 Sarangani M6.3 epicenter, with origin time between 2026-08-06 and 2026-09-04. | TRUE if USGS ComCat lists at least one M5.0 or greater event within 100 km of USGS event us6000ti6x with origin time between 2026-08-06 and 2026-09-04 UTC; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled meeting of 2026-09-15 to 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about FOMC and the resolution settles on DFEDTARU, FRED. A row whose resolution checks a different fact can be scored correct while being wrong; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The WTI crude spot price falls below 70.00 USD on at least one trading day between 2026-08-06 and 2026-09-30." → REJECTED: the resolution names a different subject than the statement — the claim is about WTI and the resolution settles on DCOILWTICO, FRED. A row whose resolution checks a different fact can be scored correct while being wrong
- "German authorities publicly announce an arrest or a named suspect in the Leipzig airport explosive drone case between 2026-08-06 and 2026-11" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

339 issued all-time across 14 forecaster arms · 294 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 12 issued · 12 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 17 | 15 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 21 | 31 | 9 | 22 | 0.222 | 29.0% | 0.206 | -0.075 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*