**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270426Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-26_1538.md · forecaster: manual/fable-5/unattested · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-01 | 45% | 2026-10-02 | cyber | CISA adds CVE-2026-63520, the Microsoft SharePoint Business Connectivity Services remote code execution flaw that completes the chain with CVE-2026-55040, to the Known Exploited Vulnerabilities catalog between 2026-08-27 and 2026-09-30. | The CISA KEV JSON feed contains an entry for CVE-2026-63520 whose dateAdded value falls between 2026-08-27 and 2026-09-30 inclusive; otherwise false. |
| KKR-20260827-02 | 25% | 2026-11-03 | cyber | Boston Scientific files a Form 8-K or 8-K/A with the SEC that includes Item 1.05, Material Cybersecurity Incidents, for the August 2026 cyberattack between 2026-08-27 and 2026-10-30, following its initial Item 8.01 disclosure. | EDGAR filings for CIK 885725 show a Form 8-K or 8-K/A with filing date 2026-08-27 through 2026-10-30 whose listed items include 1.05; otherwise false. |
| KKR-20260827-03 | 90% | 2026-09-08 | political | Xi Jinping holds an in-person meeting with Egyptian President Abdel Fattah El-Sisi on Egyptian territory between 2026-08-30 and 2026-09-04, as part of the state visit announced by the Chinese Foreign Ministry. | Both Xinhua or the Chinese Foreign Ministry and the Egyptian Presidency report an in-person Xi-Sisi meeting held on Egyptian territory between 2026-08-30 and 2026-09-04; otherwise false. |
| KKR-20260827-04 | 25% | 2026-10-02 | military/conflict | United States and Iranian officials at the level of secretary of state, foreign minister, or presidential special envoy meet face to face for a negotiating session between 2026-08-27 and 2026-09-30, and both governments acknowledge the meeting. | Both the US State Department or White House and the Iranian Foreign Ministry publicly confirm a face to face US-Iran session at that level held between 2026-08-27 and 2026-09-30; mediated exchanges through third parties do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled 2026-09-16 decision, moving from 3.50-3.75 percent to a range whose upper bo" → REJECTED: the resolution names a different subject than the statement — the claim is about FOMC and the resolution settles on Federal, Reserve. A row whose resolution checks a different fact can be scored correct while being wrong
- "Brent crude spot, as recorded in the FRED series DCOILBRENTEU, is at or above 100.00 dollars per barrel on at least one day between 2026-08-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Judge Yvonne Gonzalez Rogers enters an order, consent judgment, or final judgment approving or entering the multistate settlement with Meta " → REJECTED: the resolution names only a venue or register (PACER, courtlistener, ygr) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "UKMTO publishes at least one incident advisory reporting a merchant vessel struck or damaged by a projectile, mine, or uncrewed system withi" → REJECTED: the resolution names only a venue or register (UKMTO) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The confirmed death toll in Nepal from the 26 August 2026 Bhotekoshi-Trishuli avalanche flash flood reaches at least 250 by 2026-09-16, as p" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-16 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The jury in the Maltese trial of Yorgen Fenech for complicity in the murder of Daphne Caruana Galizia returns a verdict between 2026-08-27 a" → REJECTED: the resolution names a different subject than the statement — the claim is about Caruana, Daphne, Fenech, Galizia and the resolution settles on Court, Criminal, Independent, Malta. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

927 issued all-time across 14 forecaster arms · 837 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 90 issued · 90 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 106 | 106 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 94 | 93 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*