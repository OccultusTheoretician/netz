**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-23_1518.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260923-08 | 30% | 2026-10-07 | military/conflict | Between 2026-09-23 and 2026-09-29, at least one drone strike will be confirmed in Kyiv by two or more independently biased sources. | At least one drone strike in Kyiv is confirmed by two or more independently biased sources between 2026-09-23 and 2026-09-29. |
| KKR-20260923-09 | 45% | 2026-10-07 | cyber | Between 2026-09-23 and 2026-09-29, at least one cyberattack exploiting CVE-2026-94127 will be reported by a third-party security firm. | A third-party security firm reports a cyberattack exploiting CVE-2026-94127 between 2026-09-23 and 2026-09-29. |
| KKR-20260923-10 | 25% | 2026-10-07 | disaster | Between 2026-09-23 and 2026-09-29, a major flood warning will be issued by the USGS for a location in Iowa. | The USGS issues a major flood warning for a location in Iowa between 2026-09-23 and 2026-09-29. |
| KKR-20260923-11 | 30% | 2026-10-07 | cyber | Between 2026-09-23 and 2026-09-29, at least one major cyberattack will be attributed to Chinese state-linked actors by a U.S. government agency. | A U.S. government agency attributes a major cyberattack to Chinese state-linked actors between 2026-09-23 and 2026-09-29. |
| KKR-20260923-12 | 20% | 2026-10-07 | political | Between 2026-09-23 and 2026-09-29, Iran will issue a public statement claiming a blockade of the Strait of Hormuz is underway. | Iran issues a public statement claiming a blockade of the Strait of Hormuz is underway between 2026-09-23 and 2026-09-29. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-24, the CISA KEV catalog will include CVE-2026-93952 with a date-added value of 2026-09-22." → REJECTED: event window opens 2026-09-22, before this row is sealed (2026-09-23, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-23 and 2026-09-29, the S&P 500 will close above 7,800 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-09-25, the 10-year Treasury yield will exceed 5.15 percent at market close." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-25 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-26, the Federal Register will publish a notice of a new export control regulation targeting AI-related technologies." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-27, the Dow Jones Industrial Average will close below 51,500." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-27 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2723 issued all-time across 16 forecaster arms · 2181 open (153 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 108 issued · 103 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 942 | 825 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 108 | 103 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 164 | 147 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 320 | 295 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 299 | 235 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*