**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131646Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-13_1519.md · forecaster: manual/sonnet-5/unattested · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260813-32 | 55% | 2026-08-27 | cyber | CVE-2026-55040, the Microsoft SharePoint JWT authentication-bypass flaw under active exploitation via public proof-of-concept code as of 13 Aug 2026, will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-13 and 2026-08-25. | The CISA KEV catalog at cisa.gov lists CVE-2026-55040 with a dateAdded date between 2026-08-13 and 2026-08-25, checked as of 2026-08-27. |
| KKR-20260813-33 | 30% | 2026-09-24 | cyber | A specific victim organization of the City-Forum data-theft campaign against Salesforce Experience Cloud and ServiceNow portals will be publicly named, by the victim, by Reco, or by another named security-research firm, between 2026-08-13 and 2026-09-22. | A named security vendor, the victim itself, or a wire service publicly identifies a specific organization as a confirmed City-Forum campaign victim, in reporting dated between 2026-08-13 and 2026-09-24. |
| KKR-20260813-34 | 85% | 2026-09-01 | military/conflict | Between 2026-08-14 and 2026-08-28, Ukrainian forces will conduct a further confirmed drone or missile strike on Russian Black Sea export or naval infrastructure, at a port such as Novorossiysk, Tuapse, or another Black Sea facility. | At least two of Reuters, AP, or the Institute for the Study of War daily assessment report a Ukrainian strike on Russian Black Sea port or naval infrastructure between 2026-08-14 and 2026-08-28, checked by 2026-09-01. |
| KKR-20260813-35 | 32% | 2026-09-15 | economics/markets | WTI crude oil, the NYMEX front-month futures contract, will settle at or above 85.00 USD per barrel at the close of trading on 2026-09-15. | The NYMEX WTI front-month settlement price for 2026-09-15, as published by CME Group, the EIA, or a financial data provider, is 85.00 USD per barrel or higher. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-14 and 2026-08-28, a commercial or naval vessel in or near the Strait of Hormuz or Gulf of Oman will be attacked, fired upon" → REJECTED: resolution offers alternative VENUES joined by 'or' (…us navy fifth fleet | or | centcom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Nasdaq Composite index will close below 26000.00 on 2026-09-15, a decline of at least 3 percent from its 13 Aug 2026 close of 26805.65." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-15 exactly. Price a day, not a window: widen the window or state why the date is fixed; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Nigel Farage of Reform UK will be declared the winner of the 2026 Clacton parliamentary by-election held on 2026-08-13." → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-08-20) is 0 day(s) after the window closes (2026-08-20). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "Hakainde Hichilema will be declared the outright winner of Zambia's 13 August 2026 presidential election in the first round, with more than " → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-08-27) is 0 day(s) after the window closes (2026-08-27). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "The confirmed death toll from the 10 August 2026 magnitude-7.4 Colombia earthquake, epicenter San Jose del Palmar, will be reported at 300 o" → REJECTED: the named venue is introduced by 'such as', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-27 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Gomes Clesio Tavares, the Cameroonian national wanted under a Rome arrest warrant as an intermediary in the October 2025 bomb attack on jour" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ian outlet such as ansa, corriere della sera, | or | la repubblica, or an international wire servi…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

590 issued all-time across 14 forecaster arms · 534 open (7 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 44 issued · 44 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 101 | 101 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 64 | 62 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 49 | 49 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*