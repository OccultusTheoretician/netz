**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 042115Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-04_1502.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260804-62 | 30% | 2026-08-20 | military/conflict | Between 2026-08-04 and 2026-08-18, a single Russian or Ukrainian long-range strike will be independently confirmed by two or more wire services, such as Reuters, AP, or AFP, to have killed 20 or more people in one incident. | TRUE if two or more independent wire services report one strike in the window with a confirmed death toll of 20 or more; FALSE if no single incident reaches that two-source-confirmed toll by 2026-08-20. |
| KKR-20260804-63 | 25% | 2026-08-27 | military/conflict | Between 2026-08-04 and 2026-08-25, the Israeli and Lebanese governments will each publicly confirm one specific written security arrangement, such as a troop withdrawal timeline, border demarcation, or disarmament mechanism, reached through the talks round described in item 90. | TRUE if both governments confirm the same specific written arrangement by 2026-08-27; FALSE if talks continue, stall, or collapse without a jointly confirmed written arrangement. |
| KKR-20260804-64 | 15% | 2026-09-10 | cyber | Between 2026-08-04 and 2026-09-08, the CISA Known Exploited Vulnerabilities catalog will add a second CVE, distinct from CVE-2026-18577, affecting N-able N-central. | TRUE if the CISA KEV catalog lists any additional N-able N-central CVE with a date-added value in the window; FALSE if no such second entry appears by 2026-09-10. |
| KKR-20260804-65 | 20% | 2026-08-13 | disaster | Between 2026-08-04 and 2026-08-11, the Japan Meteorological Agency will issue a Special Warning, its highest alert level, for Typhoon Dolphin covering at least one prefecture. | TRUE if JMA public advisories show a Special Warning issued for Typhoon Dolphin in the window; FALSE if JMA issues no Special Warning by 2026-08-13. |
| KKR-20260804-66 | 55% | 2026-11-06 | crime/security | Between 2026-08-04 and 2026-11-04, the person charged with arson over the Old Trails wildfire in item 9 will be indicted or have an information filed advancing the case to Washington Superior Court. | TRUE if the county Superior Court docket shows the case advanced via indictment or filed information in the window; FALSE if it remains at initial charge, or is dismissed, by 2026-11-06. |
| KKR-20260804-67 | 25% | 2026-11-06 | political | Between 2026-08-04 and 2026-11-04, the Second Circuit Court of Appeals will enter an order or ruling, on the merits or on a stay motion, in New York's case over the ICE-officer mask ban blocked in item 113. | TRUE if the Second Circuit public docket shows an order or ruling on this matter within the window; FALSE if none appears by 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude oil will settle at or below 70.00 USD per barrel, NYMEX front-month contract per CME Group or EIA, on at least one trading day bet" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-04 and 2026-08-18, The Hacker News or BleepingComputer will report that the Keyv-linked npm supply-chain campaign in item 14" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Between 2026-08-04 and 2026-10-04, the World Health Organization or DRC Ministry of Health will report a cumulative Ebola death toll of 2,00" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

322 issued all-time across 14 forecaster arms · 284 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 22 issued · 22 open · nothing resolved yet — this arm earns a score at its first resolution.

*11 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 15 | 15 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 26 | 26 | 7 | 19 | 0.228 | 26.9% | 0.197 | -0.160 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 22 | 22 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*