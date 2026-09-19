**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-19_1516.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260919-09 | 30% | 2026-10-05 | cyber | Between 2026-09-20 and 2026-09-26, at least one new exploit for CVE-2026-53266 will be publicly disclosed. | At least one public exploit for CVE-2026-53266 is disclosed in a credible source by 2026-09-26. |
| KKR-20260919-10 | 20% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-27, a new vulnerability in the Linux kernel will be publicly disclosed and listed in the CISA KEV catalog. | A new Linux kernel vulnerability is publicly disclosed and listed in the CISA KEV catalog between 2026-09-21 and 2026-09-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-21, the CISA KEV catalog will include CVE-2025-39964 with a date-added value of 2026-09-18." → REJECTED: event window opens 2026-09-18, before this row is sealed (2026-09-19, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "On 2026-09-22, the S&P 500 will close below 7,600.00." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-20 and 2026-09-25, a drone strike will be confirmed in Kyiv involving a Geran or Shahed UAV." → REJECTED: resolution offers alternative VENUES joined by 'or' (…grade a | or | b cross-bias…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-09-23, the US dollar will trade at 1.17 or higher against the euro." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-21 and 2026-09-27, a new cyberattack will be confirmed targeting a critical infrastructure provider in the United States." → REJECTED: resolution offers alternative VENUES joined by 'or' (…grade a | or | b cross-bias…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-09-24, the 10-year U.S. Treasury yield will exceed 5.10 percent." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-24 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-20 and 2026-09-26, a missile strike will be confirmed in Gaza City involving an airstrike or drone." → REJECTED: resolution offers alternative VENUES joined by 'or' (…grade a | or | b cross-bias…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-09-25, the Brent crude oil price will close above 102.00 per barrel." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-25 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2510 issued all-time across 16 forecaster arms · 2044 open (157 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 91 issued · 86 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 858 | 773 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 301 | 151 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 91 | 86 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 136 | 126 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 293 | 276 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 270 | 222 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*