**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: lmstudio/realist · 0 accepted / 10 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

None survived validation this run.

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-07-21 and 2026-07-24, the CISA KEV catalog will carry a date-added value for a vulnerability with severity CVSS 9.0 or higher t" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, Brent crude oil futures will close above $115 per barrel on the ICE Futures Europe exchange." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, Iran will conduct a coordinated cyberattack on at least three U.S.-based financial institutions, resultin" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a Russian drone strike will result in at least one civilian fatality in Kyiv." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the U.S. 10-year Treasury yield will close above 5.2% on the Federal Reserve's FRED database." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in the Middle East." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the European Parliament will pass a resolution calling for a temporary moratorium on AI deployment in mil" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new cyberattack will be confirmed on a U.S. state-level election system, resulting in a verified data b" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the Strait of Hormuz will experience a temporary closure due to a confirmed military incident involving I" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new tropical cyclone of Category 3 or higher will be recorded in the North Atlantic basin by the Nation" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-14, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

2075 issued all-time across 16 forecaster arms · 1739 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 60 issued · 60 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 674 | 636 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*