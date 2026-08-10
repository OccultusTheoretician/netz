**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101650Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-10_1516.md · forecaster: manual/fable-5 · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260810-10 | 85% | 2026-09-04 | military/conflict | Between 2026-08-11 and 2026-08-31, Ukrainian forces strike at least one oil refinery or oil processing facility on Russian territory, corroborated by at least two international news organizations. | At least two international news organizations (e.g. Reuters, AFP, BBC) report a Ukrainian strike hitting a named Russian oil refinery or oil processing facility occurring between 2026-08-11 and 2026-08-31. |
| KKR-20260810-11 | 15% | 2026-09-15 | economics/markets | ICE Brent crude front-month futures settle above 110.00 USD per barrel on at least one trading day between 2026-08-11 and 2026-09-11. | Official ICE Brent front-month daily settlement price exceeds 110.00 USD on any trading day between 2026-08-11 and 2026-09-11, per ICE settlement records. |
| KKR-20260810-12 | 85% | 2026-11-03 | economics/markets | Intel prices or completes a common stock offering of at least 10 billion USD between 2026-08-11 and 2026-10-30, per filings on SEC EDGAR. | SEC EDGAR shows an Intel Corporation prospectus supplement, 424B, or 8-K filed between 2026-08-11 and 2026-10-30 pricing or completing a common stock offering with gross proceeds of at least 10 billion USD. |
| KKR-20260810-13 | 40% | 2026-12-22 | political | A US House committee or subcommittee holds a hearing between 2026-09-01 and 2026-12-18 at which an OpenAI or Anthropic executive testifies about the reported AI company security breach. | Congress.gov or official House committee records list a hearing held between 2026-09-01 and 2026-12-18 with a witness from OpenAI or Anthropic addressing the breach. |
| KKR-20260810-14 | 30% | 2026-09-14 | disaster | USGS catalogs at least one M6.0 or greater earthquake with epicenter within 200 km of event us6000tjl2 and origin time between 2026-08-11 and 2026-09-10 UTC. | The USGS earthquake catalog lists an event of magnitude 6.0 or higher, epicenter within 200 km of USGS event us6000tjl2, origin time between 2026-08-11 and 2026-09-10 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC leaves the federal funds target range unchanged at its scheduled meeting concluding 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The CISA KEV catalog contains at least one CVE affecting Progress LoadMaster or SonicWall SMA1000 with a dateAdded value between 2026-08-01 " → REJECTED: event window opens 2026-08-01, before this row is sealed (2026-08-10) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The Israeli government formally announces acceptance of the US-backed 15-point Gaza plan or a publicly identified revision of it between 202" → REJECTED: cited items name Palestine, State of; the claim is about Israel — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Palestine, State of; the claim is about Israel — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The official cumulative death toll for the 2026 Assam floods reaches or exceeds 150 on or before 2026-09-10." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-10 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Daniel Kinahan remains remanded in custody in Ireland, with no court ordering his release on bail, from 2026-08-10 through 2026-10-30." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-10 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

434 issued all-time across 14 forecaster arms · 382 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5`:** 38 issued · 38 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 44 | 42 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 35 | 33 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*