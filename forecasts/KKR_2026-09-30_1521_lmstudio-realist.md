**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 301521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-30_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260930-06 | 30% | 2026-10-14 | military/conflict | Between 2026-10-05 and 2026-10-12, at least one report from a hostile side confirms a drone strike on Kyiv with casualties claimed by Ukraine. | At least one report from a hostile side (RU, UA, AXIS) confirms a drone strike on Kyiv during the window, with casualties claimed by Ukraine. |
| KKR-20260930-07 | 40% | 2026-10-12 | cyber | Between 2026-10-03 and 2026-10-10, the CISA KEV catalog will include at least one new vulnerability with a severity rating of 'Critical' and a date-added value of 2026-10-01 or later. | The CISA KEV catalog includes at least one new vulnerability with a severity rating of 'Critical' and a date-added value of 2026-10-01 or later between 2026-10-03 and 2026-10-10. |
| KKR-20260930-08 | 35% | 2026-10-13 | economics/markets | Between 2026-10-04 and 2026-10-11, the Brent crude oil price will close above 105.00 per barrel on at least one weekday. | The Brent crude oil price closes above 105.00 per barrel on at least one weekday between 2026-10-04 and 2026-10-11. |
| KKR-20260930-09 | 32% | 2026-10-11 | military/conflict | Between 2026-10-02 and 2026-10-09, at least one report from a hostile side confirms a missile strike on Gaza City with casualties claimed by Palestinian sources. | At least one report from a hostile side (IL, PS, AXIS) confirms a missile strike on Gaza City during the window, with casualties claimed by Palestinian sources. |
| KKR-20260930-10 | 28% | 2026-10-14 | cyber | Between 2026-10-05 and 2026-10-12, the NVD will list at least one new vulnerability with a CVSS score of 9.0 or higher and a date-added value of 2026-10-01 or later. | The NVD lists at least one new vulnerability with a CVSS score of 9.0 or higher and a date-added value of 2026-10-01 or later between 2026-10-05 and 2026-10-12. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-05, the CISA KEV catalog will include CVE-2026-86950 with a date-added value of 2026-09-29." → REJECTED: event window opens 2026-09-29, before this row is sealed (2026-09-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-10-01 and 2026-10-07, the S&P 500 will close above 7,750 on at least one weekday." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-10, the USGS will record a magnitude 5.0 or higher earthquake in the Pacific Northwest with a depth less than 30 km." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-10 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-08, the Federal Register will publish a notice of a new U.S. tariff on Iranian crude oil imports." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-08 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-11, the European Central Bank will announce a 0.25 percentage point increase in its main refinancing rate." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-11 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

3107 issued all-time across 18 forecaster arms · 2565 open (298 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 148 issued · 143 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1106 | 989 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 345 | 195 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 148 | 143 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 224 | 207 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 48 | 48 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*