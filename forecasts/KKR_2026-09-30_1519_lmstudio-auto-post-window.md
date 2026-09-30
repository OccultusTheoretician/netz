**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 301519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-30_1517.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260930-01 | 25% | 2026-10-22 | military/conflict | Between 2026-10-10 and 2026-10-17, at least one report from a hostile side in the Iran Theatre will corroborate a missile launch from Tehran toward the Strait of Hormuz. | At least one report from a hostile side in the Iran Theatre corroborates a missile launch from Tehran toward the Strait of Hormuz between 2026-10-10 and 2026-10-17. |
| KKR-20260930-02 | 35% | 2026-11-10 | disaster | Between 2026-11-01 and 2026-11-07, the USGS will record a magnitude 5.0 or greater earthquake in the United States with a depth of less than 50 km. | The USGS records a magnitude 5.0 or greater earthquake in the United States with a depth of less than 50 km between 2026-11-01 and 2026-11-07. |
| KKR-20260930-03 | 60% | 2026-10-30 | cyber | Between 2026-10-20 and 2026-10-27, the CISA KEV catalog will list at least one new exploited vulnerability with a severity rating of 'Critical' and a date-added value between 2026-10-20 and 2026-10-27. | The CISA KEV catalog lists at least one new exploited vulnerability with a severity rating of 'Critical' and a date-added value between 2026-10-20 and 2026-10-27. |
| KKR-20260930-04 | 20% | 2026-11-24 | political | Between 2026-11-15 and 2026-11-22, the Federal Register will publish a notice of a new U.S. government rule related to AI safety with a docket number starting with 'FR-2026-XXXX'. | The Federal Register publishes a notice of a new U.S. government rule related to AI safety with a docket number starting with 'FR-2026-XXXX' between 2026-11-15 and 2026-11-22. |
| KKR-20260930-05 | 40% | 2026-12-10 | disaster | Between 2026-12-01 and 2026-12-08, the GDACS Alerts system will issue a Green flood alert for a region in the United States with a population affected of at least 100,000. | The GDACS Alerts system issues a Green flood alert for a region in the United States with a population affected of at least 100,000 between 2026-12-01 and 2026-12-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-15, the CISA KEV catalog will include CVE-2026-86950 with a date-added value of 2026-09-29." → REJECTED: event window opens 2026-09-29, before this row is sealed (2026-09-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-10-01 and 2026-10-07, no report from a hostile side in the Russia-Ukraine Theatre will corroborate a drone strike on Kyiv with " → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "On 2026-10-18, the S&P 500 will close at a level below 7,650." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-18 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-11-05, the 10-year U.S. Treasury yield will close above 5.35 percent." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-05 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-05 and 2026-10-12, no report from a hostile side in the Israel-Gaza-Levant Theatre will corroborate a drone strike on Gaza C" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

3102 issued all-time across 18 forecaster arms · 2560 open (298 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 345 issued · 195 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

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
| lmstudio/realist | 143 | 138 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
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