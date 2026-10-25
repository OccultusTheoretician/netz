**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-01 | 40% | 2026-11-12 | economics/markets | On 2026-10-29, the 10-year U.S. Treasury yield exceeds 5.00 percent for the first time since 2023, as confirmed by the Federal Reserve's FRED database. | The 10-year U.S. Treasury yield exceeds 5.00 percent on 2026-10-29, as confirmed by the FRED database (https://fred.stlouisfed.org/series/IRLTLT01USM156N). |
| KKR-20261025-02 | 32% | 2026-11-07 | disaster | Between 2026-10-26 and 2026-11-03, a major earthquake of magnitude 6.5 or higher occurs in the Bonin Islands, Japan region, with a depth of less than 100 km, as confirmed by USGS Significant Quakes and GDACS Alerts. | Between 2026-10-26 and 2026-11-03, a magnitude 6.5 or higher earthquake occurs in the Bonin Islands, Japan region with a depth of less than 100 km, as confirmed by USGS Significant Quakes and GDACS Alerts. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-26, a drone strike targeting a military installation in Hebron, Israel, results in at least one confirmed casualty, as reported b" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-25 and 2026-10-31, the CISA KEV catalog adds at least one new vulnerability with a 'high' or 'critical' severity rating that" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-27, a tropical cyclone named IN-FA-26 causes a Category 3 or higher storm surge in coastal regions of Australia, resulting in at " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-27 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-26 and 2026-11-02, the S&P 500 index closes below 7,500 on at least three separate trading days, as recorded by the NYSE clo" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; market-price resolution with weekend deadline — no settlement exists that day
- "On 2026-10-28, a major cyberattack on a U.S. federal agency results in the public exposure of classified documents, confirmed by at least tw" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-28 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-25 and 2026-11-01, Iran conducts a missile or drone strike on a military target in Tel Aviv, Israel, resulting in at least o" → REJECTED: cited items name Iran, Islamic Republic of, zone:iran; the claim is about Israel, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-30, Saudi Arabia intercepts a missile or drone launched from Iran-backed Houthi forces near Mecca, with at least one confirmed ca" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-30 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-25 and 2026-11-02, the price of Brent crude oil exceeds $115 per barrel on at least two consecutive trading days, as confirm" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; market-price resolution with weekend deadline — no settlement exists that day

## III. LEDGER STANDING

4908 issued all-time across 21 forecaster arms · 3556 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 249 issued · 162 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1727 | 1344 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 108 | 107 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 109 | 109 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 429 | 348 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*