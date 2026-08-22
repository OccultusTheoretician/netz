**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220321Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/sonnet-5/unattested · 2 accepted / 7 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-04 | 40% | 2026-08-28 | economic | On 2026-08-27, the first full Nasdaq trading session after Nvidia Corporation (NVDA) releases its August 26, 2026 after-market earnings, NVDA closes up or down 6 percent or more from its 2026-08-26 closing price. | Resolves YES if the official Nasdaq closing price for NVDA on 2026-08-27 differs from its 2026-08-26 closing price by 6 percent or more in either direction, per Nasdaq or a standard market-data provider; resolves NO if the move is smaller than 6 percent. |
| KKR-20260822-05 | 40% | 2026-09-08 | crime_security | At the sentencing hearing scheduled for 2026-09-04 at Preston Crown Court, at least one of the five Barclays-branch Palestine Action defendants (Atiqnisar, Kelly, Malik, O'Hagan, or Yaniv) receives an immediate custodial sentence. | Resolves YES if Preston Crown Court sentencing coverage (BBC, Guardian, PA Media, or comparable outlets) confirms at least one of the five defendants receives an immediate custodial sentence rather than a suspended sentence, community order, or fine; resolves NO if all five receive non-custodial or suspended sentences. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The 50 percent United States tariff on the Canadian goods categories named in the order Trump announced (cement, hockey sticks, and related " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-08-21 and 2026-09-18, the USGS catalog records an earthquake of magnitude 6.0 or greater within 150 km of the August 21, 2026 M" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds an entry for CVE-2026-19478, the GitLab remote code" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds at least one entry for a Microsoft Entra ID product" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-09-18, United States military forces carry out a kinetic strike on a target inside Iranian sovereign territory, " → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-09-18, Swedish police or prosecutors publicly classify the August 21, 2026 sword attack at a Swedish school as a" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-12-31, a Hong Kong court sentences Lee Cheuk-yan or Chow Hang-tung in the West Kowloon incitement-to-subversion " → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

836 issued all-time across 14 forecaster arms · 746 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 79 issued · 78 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 117 | 105 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 85 | 85 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 79 | 78 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*