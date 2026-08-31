**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 301517Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-30_1516.md · forecaster: lmstudio/auto · 0 accepted / 10 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

None survived validation this run.

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-07-21 and 2026-07-24, the CISA KEV catalog will include at least one vulnerability with a date-added value between 2026-08-25 a" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-28 and 2026-09-04, at least one report from a hostile side confirms a drone strike on a Ukrainian military installation in K" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-29 and 2026-09-05, the S&P 500 will close above 7,800 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; event window opens 2026-08-29, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-27 and 2026-09-03, at least one report from a hostile side confirms a missile strike on a civilian area in Kyiv." → REJECTED: event window opens 2026-08-27, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-25 and 2026-09-01, at least one report from a hostile side confirms a cyberattack targeting a critical infrastructure provid" → REJECTED: event window opens 2026-08-25, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-26 and 2026-09-02, at least one report from a hostile side confirms a new flood alert in Nepal." → REJECTED: resolution offers alternative VENUES joined by 'or' (…at least one report from a hostile side (ps | or | il) confirms a new flood alert in nepal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-26, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-28 and 2026-09-04, at least one report from a hostile side confirms a drone strike on a civilian area in Deir Al-Balah." → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-27 and 2026-09-03, at least one report from a hostile side confirms a new earthquake of magnitude 5.0 or higher in the Kerma" → REJECTED: event window opens 2026-08-27, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-29 and 2026-09-05, at least one report from a hostile side confirms a new forest fire in the United States." → REJECTED: event window opens 2026-08-29, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-25 and 2026-09-01, at least one report from a hostile side confirms a new cyberattack targeting a government system in Iran." → REJECTED: resolution offers alternative VENUES joined by 'or' (…at least one report from a hostile side (west | or | axis) confirms a new cyberattack targeting a …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-25, before this row is sealed (2026-08-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

1123 issued all-time across 14 forecaster arms · 962 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 169 issued · 138 open · 29 resolved · 10 hits / 19 misses · **Brier 0.250** against its own base rate 34.5% (climatological 0.226) · **skill -0.109** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 281 | 264 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 114 | 113 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 135 | 132 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 121 | 113 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*