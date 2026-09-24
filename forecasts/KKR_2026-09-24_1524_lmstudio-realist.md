**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241524Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-24_1520.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260924-01 | 25% | 2026-10-07 | cyber | On 2026-10-05, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in a critical infrastructure attack between 2026-09-24 and 2026-10-04. | The CISA KEV catalog carries a date-added value between 2026-09-24 and 2026-10-04 for a vulnerability that was actively exploited in a confirmed attack on a critical infrastructure system. |
| KKR-20260924-02 | 30% | 2026-10-10 | military/conflict | Between 2026-10-01 and 2026-10-07, a drone strike will be confirmed by at least two hostile sides in the Gaza City area. | At least two hostile sides (IL, PS, AXIS) will independently report a drone strike in Gaza City between 2026-10-01 and 2026-10-07, with corroborating reports from distinct channels. |
| KKR-20260924-03 | 35% | 2026-10-14 | cyber | Between 2026-10-05 and 2026-10-12, a cyberattack exploiting a critical WordPress vulnerability will be confirmed by CISA. | CISA issues a public advisory confirming a cyberattack exploiting a vulnerability in WordPress (CVE-2026-87902) between 2026-10-05 and 2026-10-12. |
| KKR-20260924-04 | 20% | 2026-10-10 | military/conflict | Between 2026-10-01 and 2026-10-07, a missile attack will be confirmed by at least two hostile sides in Kyiv. | At least two hostile sides (RU, UA) will independently report a missile attack in Kyiv between 2026-10-01 and 2026-10-07, with corroborating reports from distinct channels. |
| KKR-20260924-05 | 15% | 2026-10-10 | political | Between 2026-10-01 and 2026-10-07, a new round of sanctions will be announced by the U.S. and EU targeting Iran's energy sector. | On or before 2026-10-07, the U.S. and EU jointly announce new sanctions targeting Iran's energy sector, confirmed by at least two independent news outlets from different geopolitical blocs. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-01 and 2026-10-07, the S&P 500 will close above 7,750 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-12, the 10-year U.S. Treasury yield will exceed 5.25 percent at market close." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-12 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-15, the Dow Jones Industrial Average will close below 50,500." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-15 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-01 and 2026-10-07, a state-level cyberattack on a government health system will be confirmed by two independent outlets from" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "On 2026-10-20, the 30-year Treasury yield will reach its highest level since 2004, exceeding 5.30 percent." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-20 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2772 issued all-time across 16 forecaster arms · 2230 open (170 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 113 issued · 108 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 964 | 847 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 113 | 108 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 173 | 156 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 306 | 242 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*