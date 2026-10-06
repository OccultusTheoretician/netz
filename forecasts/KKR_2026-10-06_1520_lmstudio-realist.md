**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-05 | 35% | 2026-10-20 | cyber | Between 2026-10-12 and 2026-10-18, a confirmed cyberattack will compromise the Danish population registry, resulting in the exposure of personal data for at least 8.8 million individuals. | At least one report from two or more hostile sides (DEN, WEST) confirms a cyberattack on the Danish population registry between 2026-10-12 and 2026-10-18, with exposure of personal data affecting at least 8.8 million individuals. |
| KKR-20261006-06 | 15% | 2026-10-25 | cyber | Between 2026-10-16 and 2026-10-22, a major cyberattack will be confirmed on a critical infrastructure system in the United States, resulting in a disruption to essential services lasting more than 24 hours. | At least one report from two or more hostile sides (US, WEST) confirms a cyberattack on a critical infrastructure system in the United States between 2026-10-16 and 2026-10-22, resulting in a disruption to essential services lasting more than 24 hours. |
| KKR-20261006-07 | 30% | 2026-10-26 | economics/markets | Between 2026-10-18 and 2026-10-24, the 10-year U.S. Treasury yield will close below 5.00 percent on at least one weekday. | The 10-year U.S. Treasury yield closes below 5.00 percent on at least one weekday between 2026-10-18 and 2026-10-24, as reported by a machine-readable source such as FRED. |
| KKR-20261006-08 | 10% | 2026-10-30 | disaster | Between 2026-10-22 and 2026-10-28, a confirmed earthquake of magnitude 5.0 or higher will be recorded by the USGS in the Pacific Northwest. | The USGS Significant Quakes catalog will carry a date-added value between 2026-10-22 and 2026-10-28 for an earthquake of magnitude 5.0 or higher in the Pacific Northwest. |
| KKR-20261006-09 | 35% | 2026-11-02 | political | Between 2026-10-24 and 2026-10-30, a confirmed political event will occur in France involving a national strike or protest that results in the closure of at least 500 schools. | At least one report from two or more hostile sides (FR, WEST) confirms a national strike or protest in France between 2026-10-24 and 2026-10-30, resulting in the closure of at least 500 schools. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-15, the CISA KEV catalog will carry a date-added value between 2026-10-05 and 2026-10-14 for a vulnerability in Rejetto HFS serve" → REJECTED: event window opens 2026-10-05, before this row is sealed (2026-10-06, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-10-10 and 2026-10-16, at least one drone attack will be confirmed by cross-bias reporting in the Kyiv or Zaporizhzhia region of" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-14 and 2026-10-20, the S&P 500 index will close above 7,900 points on at least one weekday." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-15 and 2026-10-21, a confirmed airstrike will occur in Gaza City, with at least one side reporting casualties." → REJECTED: cited items name India; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-20 and 2026-10-26, a confirmed drone attack will occur in Moscow, with at least one side reporting casualties." → REJECTED: cited items name Congo, Indonesia; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3470 issued all-time across 21 forecaster arms · 2656 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 185 issued · 150 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1242 | 1041 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*