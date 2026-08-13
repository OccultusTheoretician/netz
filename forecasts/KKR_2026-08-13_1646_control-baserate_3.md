**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131646Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-13_1519.md · forecaster: control/baserate · 4 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260813-36 | 33% | 2026-08-27 | cyber | CVE-2026-55040, the Microsoft SharePoint JWT authentication-bypass flaw under active exploitation via public proof-of-concept code as of 13 Aug 2026, will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-13 and 2026-08-25. | The CISA KEV catalog at cisa.gov lists CVE-2026-55040 with a dateAdded date between 2026-08-13 and 2026-08-25, checked as of 2026-08-27. |
| KKR-20260813-37 | 33% | 2026-09-24 | cyber | A specific victim organization of the City-Forum data-theft campaign against Salesforce Experience Cloud and ServiceNow portals will be publicly named, by the victim, by Reco, or by another named security-research firm, between 2026-08-13 and 2026-09-22. | A named security vendor, the victim itself, or a wire service publicly identifies a specific organization as a confirmed City-Forum campaign victim, in reporting dated between 2026-08-13 and 2026-09-24. |
| KKR-20260813-38 | 33% | 2026-09-01 | military/conflict | Between 2026-08-14 and 2026-08-28, Ukrainian forces will conduct a further confirmed drone or missile strike on Russian Black Sea export or naval infrastructure, at a port such as Novorossiysk, Tuapse, or another Black Sea facility. | At least two of Reuters, AP, or the Institute for the Study of War daily assessment report a Ukrainian strike on Russian Black Sea port or naval infrastructure between 2026-08-14 and 2026-08-28, checked by 2026-09-01. |
| KKR-20260813-39 | 18% | 2026-09-15 | economics/markets | WTI crude oil, the NYMEX front-month futures contract, will settle at or above 85.00 USD per barrel at the close of trading on 2026-09-15. | The NYMEX WTI front-month settlement price for 2026-09-15, as published by CME Group, the EIA, or a financial data provider, is 85.00 USD per barrel or higher. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

594 issued all-time across 14 forecaster arms · 538 open (7 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 105 issued · 105 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 105 | 105 | 0 | — | — | not computed | — | — | — |
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