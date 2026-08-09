**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091518Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-09_1516.md · forecaster: lmstudio/auto · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260809-01 | 25% | 2026-08-28 | cyber | Between 2026-08-22 and 2026-08-25, a cyberattack exploiting a vulnerability in a critical infrastructure system is reported by at least two wire services with independent verification, and the CISA KEV catalog includes the vulnerability with a date-added value in that window. | The CISA KEV catalog carries a date-added value between 2026-08-22 and 2026-08-25, and the attack is reported by at least two wire services with independent verification. |
| KKR-20260809-02 | 32% | 2026-09-02 | cyber | Between 2026-08-27 and 2026-08-30, a new cyberattack targeting a U.S. government system is reported by two wire services with independent verification, and the CISA KEV catalog includes the vulnerability with a date-added value in that window. | The CISA KEV catalog carries a date-added value between 2026-08-27 and 2026-08-30, and the attack is reported by two wire services with independent verification. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-21 and 2026-08-24, a drone strike targeting a military installation in Kyiv, Ukraine, is confirmed by at least three indepen" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-23 and 2026-08-26, a magnitude 6.0 or higher earthquake occurs in the Pacific Northwest, confirmed by the USGS Significant Q" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-24 and 2026-08-27, a wildfire in Australia expands to exceed 10,000 hectares, confirmed by the GDACS Alerts feed with a gree" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-25 and 2026-08-28, the S&P 500 index closes above 7,850 on a weekday, based on the prior-session close as reference." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-08-26 and 2026-08-29, a political statement by Iran's Foreign Ministry regarding the Strait of Hormuz is confirmed by at least " → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-28 and 2026-08-31, a new oil refinery fire in Saudi Arabia is confirmed by at least two independently biased sources (AXIS a" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-29 and 2026-09-01, a new political statement by Netanyahu rejecting a U.S.-proposed peace plan for Gaza is confirmed by at l" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-30 and 2026-09-02, a new earthquake of magnitude 5.5 or higher occurs in the Mediterranean region, confirmed by the USGS Sig" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world

## III. LEDGER STANDING

405 issued all-time across 14 forecaster arms · 355 open (2 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 35 issued · 33 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 35 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 20 | 32 | 9 | 23 | 0.221 | 28.1% | 0.202 | -0.093 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 62 | 62 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 30 | 28 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*