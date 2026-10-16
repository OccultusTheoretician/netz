**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: lmstudio/realist · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-04 | 30% | 2026-10-23 | military/conflict | On 2026-10-17, a drone strike targeting a military installation in Kyiv, Ukraine, results in at least one confirmed casualty, as reported by two independent sources from hostile sides (UA and WEST) with no conflicting reports. | At least one confirmed casualty from a drone strike in Kyiv, Ukraine, between 2026-10-17 and 2026-10-20, verified by two independent sources from hostile sides (UA and WEST) with no conflicting reports in corroborating outlets by 2026-10-23. |
| KKR-20261016-05 | 15% | 2026-10-26 | disaster | On 2026-10-21, a major earthquake of magnitude 7.0 or higher will be recorded by the USGS in the Pacific Ring of Fire, with at least one confirmed casualty. | The USGS Significant Quakes database records an earthquake of magnitude 7.0 or higher in the Pacific Ring of Fire between 2026-10-21 and 2026-10-24, with at least one confirmed casualty reported by a major news outlet by 2026-10-26. |
| KKR-20261016-06 | 45% | 2026-10-27 | economics/markets | Between 2026-10-18 and 2026-10-25, the 10-year U.S. Treasury yield will exceed 5.25 percent on at least one trading day, based on the prior-session close of 5.10 percent on 2026-10-16. | The 10-year U.S. Treasury yield exceeds 5.25 percent on at least one trading day between 2026-10-18 and 2026-10-25, as reported by the U.S. Department of the Treasury or FRED. |
| KKR-20261016-07 | 30% | 2026-10-26 | disaster | Between 2026-10-17 and 2026-10-24, a major wildfire in California will result in at least 10,000 evacuations, as confirmed by a state emergency management agency. | A major wildfire in California results in at least 10,000 evacuations, as confirmed by a state emergency management agency, between 2026-10-17 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-18 and 2026-10-25, the CISA KEV catalog will include at least one new vulnerability with a severity rating of 9.0 or higher," → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-20, the S&P 500 index will close below 7,600.00, based on the prior-session close of 7,724.92 on 2026-10-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-19 and 2026-10-26, a verified cyberattack exploiting CVE-2026-21589 will result in unauthorized access to a government or cr" → REJECTED: resolution offers alternative VENUES joined by 'or' (…government | or | critical infrastructure…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-10-22, a coordinated cyberattack targeting multiple European financial institutions will be confirmed by at least two independent so" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-23, the UN Security Council will adopt a resolution calling for an immediate ceasefire in Gaza, with at least 12 votes in favor a" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-19 and 2026-10-26, a drone strike in Rafah, Gaza, will result in at least one confirmed casualty, as reported by two indepen" → REJECTED: cited items name New York; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4250 issued all-time across 21 forecaster arms · 3139 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 224 issued · 165 open · 58 resolved · 31 hits / 27 misses · **Brier 0.296** against its own base rate 53.4% (climatological 0.249) · **skill -0.191**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1501 | 1205 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 60 | 60 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 63 | 63 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*