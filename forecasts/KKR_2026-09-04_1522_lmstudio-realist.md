**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: lmstudio/realist · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-09 | 30% | 2026-09-14 | economics/markets | Between 2026-09-06 and 2026-09-12, the US dollar strengthens to a 10-year high against the euro, with EUR/USD falling below 1.1450 at the close of the final trading day. | The EUR/USD exchange rate closes below 1.1450 on 2026-09-12. |
| KKR-20260904-10 | 25% | 2026-09-16 | cyber | Between 2026-09-07 and 2026-09-13, a cyberattack exploiting the Chrome V8 zero-day vulnerability is confirmed by at least two independent sources, including CISA or BleepingComputer, with evidence of active exploitation in the wild. | The CISA KEV catalog carries a date-added value between 2026-09-07 and 2026-09-13, and at least two independent sources (e.g., BleepingComputer, The Hacker News) confirm active exploitation of the Chrome V8 zero-day vulnerability. |
| KKR-20260904-11 | 30% | 2026-09-18 | military/conflict | Between 2026-09-09 and 2026-09-15, Iran launches a coordinated missile and drone attack on Israeli military installations in the Golan Heights, confirmed by at least two hostile sides (IL, PS) with casualty reports. | At least two hostile sides (IL, PS) report a coordinated missile and drone attack on Israeli military installations in the Golan Heights between 2026-09-09 and 2026-09-15, with confirmed casualties. |
| KKR-20260904-12 | 32% | 2026-09-21 | cyber | Between 2026-09-13 and 2026-09-19, a cyberattack targeting the Ukrainian power grid is confirmed by at least two hostile sides (RU, UA), with sustained outages reported in Kyiv. | At least two hostile sides (RU, UA) report a cyberattack on the Ukrainian power grid between 2026-09-13 and 2026-09-19, with sustained outages confirmed in Kyiv. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-05, a drone strike targeting the Ukrainian Security Service headquarters in Kyiv is confirmed by at least three independent sourc" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-05 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-08, a major earthquake of magnitude 6.0 or higher occurs in the Himalayan region, with USGS reporting a depth of less than 50 km " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-08 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-10, a new vulnerability in Microsoft Teams desktop client is exploited in a targeted cyberattack, confirmed by BleepingComputer a" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-10 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-11 and 2026-09-17, the S&P 500 index closes below 7,600 for three consecutive trading days, with the final close on 2026-09-" → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-09-12, the French hospital fined €500,000 for a data breach exposes the personal data of 727,000 patients, confirmed by BleepingComp" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-12 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-14, a new vulnerability in HPE ArubaOS-CX is exploited in a widespread attack, confirmed by BleepingComputer and the CISA KEV cat" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-14 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1416 issued all-time across 16 forecaster arms · 1151 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 4 issued · 4 open · nothing resolved yet — this arm earns a score at its first resolution.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 15 | 15 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 153 | 151 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 174 | 168 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 158 | 137 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*