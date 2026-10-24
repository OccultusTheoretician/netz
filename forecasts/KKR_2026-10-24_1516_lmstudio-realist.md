**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-24_1512.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261024-05 | 25% | 2026-11-03 | cyber | Between 2026-10-26 and 2026-11-01, the CISA KEV catalog will include at least one new entry for a vulnerability in a widely deployed open-source software component that is actively exploited in the wild. | The CISA KEV catalog carries a date-added value between 2026-10-26 and 2026-11-01 for a vulnerability in a widely deployed open-source software component that is actively exploited in the wild. |
| KKR-20261024-06 | 35% | 2026-11-04 | cyber | On 2026-10-27, a cyberattack exploiting CVE-2026-110447 in Collabora Online will result in a confirmed breach of at least one government or critical infrastructure system, as verified by a third-party cybersecurity firm. | A confirmed breach of at least one government or critical infrastructure system due to exploitation of CVE-2026-110447 in Collabora Online occurs between 2026-10-27 and 2026-10-28, as verified by a third-party cybersecurity firm. |
| KKR-20261024-07 | 20% | 2026-11-05 | disaster | On 2026-10-29, a wildfire in the Four Corners region of the United States will result in at least one fatality, as confirmed by two independent news outlets reporting from the area. | At least one fatality occurs due to a wildfire in the Four Corners region of the United States between 2026-10-29 and 2026-10-30, as confirmed by two independent news outlets reporting from the area. |
| KKR-20261024-08 | 30% | 2026-11-07 | cyber | Between 2026-10-30 and 2026-11-05, a cyberattack exploiting the Brotli decoder flaw (CVE-2026-110447) will lead to a confirmed remote code execution on a system used by a major financial institution, as verified by a public security advisory. | A confirmed remote code execution due to the Brotli decoder flaw (CVE-2026-110447) occurs on a system used by a major financial institution between 2026-10-30 and 2026-11-05, as verified by a public security advisory. |
| KKR-20261024-09 | 22% | 2026-11-12 | disaster | Between 2026-11-03 and 2026-11-10, a major earthquake of magnitude 6.5 or higher will be recorded in Vanuatu, as verified by the USGS Significant Quakes database. | A major earthquake of magnitude 6.5 or higher is recorded in Vanuatu between 2026-11-03 and 2026-11-10, as verified by the USGS Significant Quakes database. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-25, a drone strike targeting a military installation in Kherson, Ukraine, results in at least one confirmed casualty as reported " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-28 and 2026-11-04, the S&P 500 index will close below 7,500 on at least one weekday, based on the prior-session close of 7,6" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-31, a missile strike in Hebron, Israel, will result in at least one confirmed casualty, as reported by two independent outlets fr" → REJECTED: cited items name France, Nigeria; the claim is about Israel, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-11-01 and 2026-11-08, the 10-year U.S. Treasury yield will exceed 5.00 percent on at least one weekday, based on the prior-sess" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-11-02, a fire at the Eagle's Nest retreat in Bavaria, Germany, will be confirmed by a public investigation to have been caused by ar" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-02 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

4845 issued all-time across 21 forecaster arms · 3493 open (681 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 247 issued · 160 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1701 | 1318 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 104 | 103 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 105 | 105 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 113 | 106 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 247 | 160 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 420 | 339 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 251 | 240 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 205 | 202 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*