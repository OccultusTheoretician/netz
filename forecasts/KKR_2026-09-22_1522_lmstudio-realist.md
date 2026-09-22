**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-22_1518.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260922-08 | 25% | 2026-10-06 | military/conflict | Between 2026-09-22 and 2026-09-29, at least one report from a hostile side in the Iran Theatre will confirm a drone or missile strike on Tehran with casualties exceeding 5. | At least one corroborated report from a hostile side (AXIS, IL, WEST) confirms a drone or missile strike on Tehran during the event window with casualties exceeding 5. |
| KKR-20260922-09 | 20% | 2026-10-06 | cyber | Between 2026-09-22 and 2026-09-29, at least one report from a hostile side in the Iran Theatre will confirm a cyberattack on a critical infrastructure system in the United States. | At least one corroborated report from a hostile side (AXIS, WEST) confirms a cyberattack on a critical infrastructure system in the United States during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-23, the CISA KEV catalog will include CVE-2026-7273 with a date-added value of 2026-09-21." → REJECTED: event window opens 2026-09-21, before this row is sealed (2026-09-22, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-22 and 2026-09-28, no report from a hostile side in the Russia-Ukraine Theatre will confirm a kinetic attack on Kyiv with ca" → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "On 2026-09-25, the 10-year Treasury yield will close below 4.96 percent, the reference level on the packet date." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-25 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-24, the S&P 500 will close above 7,764.88, the reference level on the packet date." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-24 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-22 and 2026-09-28, no report from a hostile side in the Israel-Gaza-Levant Theatre will confirm an airstrike on Gaza City wi" → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "On 2026-09-26, the USGS Significant Quakes catalog will record a magnitude 6.5 or higher earthquake in Alaska with a depth greater than 50 k" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-27, the Nasdaq will close above 27,207.76, the reference level on the packet date." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-27 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-22 and 2026-09-28, no report from a hostile side in the Russia-Ukraine Theatre will confirm a kinetic attack on Dnipro with " → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition

## III. LEDGER STANDING

2665 issued all-time across 16 forecaster arms · 2199 open (193 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 103 issued · 98 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 918 | 833 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 324 | 174 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 103 | 98 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 156 | 146 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*