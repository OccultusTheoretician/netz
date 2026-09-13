**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131713Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: lmstudio/auto · 0 accepted / 10 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

None survived validation this run.

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-07-21 and 2026-07-24, a drone strike from Russia hits a civilian train near the Polish border in Kyiv, resulting in at least on" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively; event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a cyberattack exploiting a vulnerability in a Tencent mobile app leads to the deployment of GrayRabbit ma" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the S&P 500 index closes above 7,800 points on at least one trading day." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a major earthquake of magnitude 6.5 or higher occurs in Indonesia, with a USGS Significant Quakes catalog" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new political party in Sweden wins at least 10% of the vote in the general election, as reported by two" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a vessel is struck in the Strait of Hormuz, resulting in a confirmed oil spill of at least 1,000 barrels," → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new cyberattack on a U.S. federal agency results in the public disclosure of at least 100,000 sensitive" → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new BRICS summit is announced by China or India, with a formal invitation issued by a member state, as " → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a major forest fire in Australia spreads beyond 10,000 hectares, as confirmed by the GDACS Alerts system " → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a U.S. congressional hearing on AI regulation is held, with a transcript published by Congress.gov within" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict; event window opens 2026-07-21, before this row is sealed (2026-09-13, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

2012 issued all-time across 16 forecaster arms · 1676 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 259 issued · 130 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 649 | 611 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*