**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-06 | 20% | 2026-10-28 | disaster | Between 2026-10-18 and 2026-10-24, a new earthquake of magnitude 6.0 or higher will be recorded by USGS in a region with a population density over 100 people per km². | The USGS Significant Quakes feed records at least one earthquake with magnitude ≥6.0 and depth ≤100 km in a region with population density >100 people per km² between 2026-10-18 and 2026-10-24. |
| KKR-20261017-07 | 35% | 2026-10-28 | political | Between 2026-10-18 and 2026-10-24, a new political statement by Trump regarding Russia sanctions will be confirmed by at least two independently biased sources (RU, UA, WEST). | At least one public statement by Trump regarding Russia sanctions between 2026-10-18 and 2026-10-24 is confirmed by at least two independently biased sources (RU, UA, WEST) in the record. |
| KKR-20261017-08 | 25% | 2026-10-28 | disaster | Between 2026-10-18 and 2026-10-24, a new wildfire in California will be confirmed by at least two independent sources (NPR, GDACS) with a burn area exceeding 10,000 acres. | At least one new wildfire in California between 2026-10-18 and 2026-10-24 is confirmed by at least two independent sources (NPR, GDACS) with a burn area exceeding 10,000 acres. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-18 and 2026-10-24, the CISA KEV catalog will include at least one new vulnerability with a date-added value between 2026-10-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-18 and 2026-10-24, at least one drone strike with reported casualties will be confirmed by at least two independently biased" → REJECTED: cites 20 of 116 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim
- "Between 2026-10-18 and 2026-10-24, the S&P 500 will close below 7,500 on at least one weekday." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-18 and 2026-10-24, a new cyberattack exploiting CVE-2026-102764 will be publicly reported by at least two independent source" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-18 and 2026-10-24, a new airstrike in Gaza City will be confirmed by at least two independently biased sources (IL, PS)." → REJECTED: cited items name Alaska, Australia, France, Malaysia, Mexico, Oregon; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-18 and 2026-10-24, the 10Y Yield will exceed 5.20 percent on at least one weekday." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-18 and 2026-10-24, a new cyberattack exploiting CVE-2025-61624 will be publicly reported by at least two independent sources" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4327 issued all-time across 21 forecaster arms · 3216 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 227 issued · 168 open · 58 resolved · 31 hits / 27 misses · **Brier 0.296** against its own base rate 53.4% (climatological 0.249) · **skill -0.191**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1526 | 1230 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*