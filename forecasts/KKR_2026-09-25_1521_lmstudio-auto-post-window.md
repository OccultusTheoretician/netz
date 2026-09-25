**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-25_1520.md · forecaster: lmstudio/auto · 0 accepted / 10 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

None survived validation this run.

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-07-21 and 2026-07-24, the CISA KEV catalog will include CVE-2026-5430 with a date-added value of 2026-09-24." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the S&P 500 will close above 7,800 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a drone attack will be reported in Kyiv with casualties claimed by Ukrainian sources." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a cyberattack exploiting CVE-2026-71362 will be confirmed by at least two independent sources." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, Hurricane Nolo will make landfall in Hawaii with sustained winds exceeding 74 mph." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, the 10-year U.S. Treasury yield will exceed 5.30 percent on at least one trading day." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, Iran will publicly announce the reopening of the Strait of Hormuz within seven days." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a major cyberattack on a U.S. federal agency will be confirmed by the CISA KEV catalog." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new round of fighting in northern Ethiopia will displace over 50,000 people." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-07-21 and 2026-07-24, a new U.S.-China trade negotiation will be announced by the USTR." → REJECTED: event window opens 2026-07-21, before this row is sealed (2026-09-25, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

2824 issued all-time across 17 forecaster arms · 2282 open (189 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 329 issued · 179 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 990 | 873 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 113 | 108 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 181 | 164 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 10 | 10 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 314 | 250 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*