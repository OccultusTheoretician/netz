**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-19_1513.md · forecaster: lmstudio/realist · 1 accepted / 9 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261019-02 | 15% | 2026-11-03 | cyber | Between 2026-10-22 and 2026-10-28, a cyberattack exploiting the NGINX vulnerability CVE-2026-XXXX is confirmed in at least three distinct government or critical infrastructure systems. | The CISA KEV catalog carries a date-added value between 2026-10-22 and 2026-10-28, and at least three distinct government or critical infrastructure systems report exploitation of the NGINX vulnerability CVE-2026-XXXX. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-20, a drone strike targeting a Russian military installation in Belgorod resulted in at least 10 casualties and was confirmed by " → REJECTED: cited items name Australia; the claim is about Russian Federation, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-27, the S&P 500 index closes below 7,650 on at least three separate trading days." → REJECTED: resolution offers alternative VENUES joined by 'or' (…d by the federal reserve economic data (fred) | or | a major exchange settlement feed…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-10-23, a major earthquake of magnitude 7.0 or higher occurs in Vanuatu, confirmed by the USGS Significant Quakes feed." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-24 and 2026-10-30, the 10-year U.S. Treasury yield exceeds 5.25 percent on at least two consecutive trading days." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-25, a coordinated cyberattack on multiple European financial institutions, confirmed by at least two independent sources from hos" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-25 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-26 and 2026-11-01, a major wildfire in California spreads beyond 10,000 acres and is confirmed by the GDACS Alerts system." → REJECTED: cited items name Australia; the claim is about California — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "On 2026-10-27, a missile strike on a civilian target in Gaza City results in at least 20 fatalities, confirmed by at least two independent s" → REJECTED: cited items name Australia; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-27 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-28 and 2026-11-03, the French government announces a new defense pact with Qatar, confirmed by at least two independent sour" → REJECTED: cited items name Qatar; the claim is about France — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-29, a cyberattack on the U.S. Department of Defense network is confirmed by the CISA KEV catalog and two independent sources from" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4483 issued all-time across 21 forecaster arms · 3131 open (313 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 231 issued · 144 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1580 | 1197 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 445 | 204 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 81 | 80 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 79 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 231 | 144 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 378 | 297 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 212 | 201 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 165 | 162 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*