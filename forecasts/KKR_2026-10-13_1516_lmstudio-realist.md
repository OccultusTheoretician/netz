**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-07 | 20% | 2026-10-25 | disaster | On 2026-10-17, a major earthquake of magnitude 6.5 or higher occurs in the Mid-Atlantic Ridge, with a depth of less than 20 km, as confirmed by the USGS Significant Quakes database. | The USGS Significant Quakes database carries an event with magnitude ≥6.5 and depth <20 km in the Mid-Atlantic Ridge between 2026-10-13 and 2026-10-17. |
| KKR-20261013-08 | 45% | 2026-10-23 | political | Between 2026-10-13 and 2026-10-20, a new political scandal involving a U.S. ambassador leads to their resignation, confirmed by at least two independent outlets from hostile political camps. | The CISA KEV catalog carries a date-added value between 2026-10-13 and 2026-10-20. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-14, a drone strike targeting a Russian military installation in Kharkiv is confirmed by at least two independent sources from hos" → REJECTED: cited items name China, Mongolia, Panama, United States; the claim is about Russian Federation, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-10-13 and 2026-10-20, a cyberattack exploiting CVE-2026-104935 in Ivanti Connect Secure results in unauthorized access to at le" → REJECTED: cited items name Panama; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, already inside the claimed window 2026-10-13..2026-10-20
- "On 2026-10-15, a French supermarket chain experiences a cyberattack that causes refrigeration systems to fail, resulting in food spoilage an" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "On 2026-10-16, the S&P 500 closes below 7,700 for the first time since 2026-09-20, based on the prior-session close reference of 7,796.70." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-16 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-13 and 2026-10-20, a new Houthi-led attack on a commercial vessel in the Red Sea results in a confirmed maritime incident wi" → REJECTED: cited items name Israel, Palestine, State of; the claim is about Djibouti, Egypt, Eritrea, Saudi Arabia, Sudan, Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-10-13 and 2026-10-20, a new vulnerability in SAP systems is exploited in a real-world attack, resulting in unauthorized access " → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "On 2026-10-18, the U.S. Treasury yield on the 10-year bond falls below 5.00 percent, based on the prior-session close of 5.21 percent." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-18 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution names a different subject than the statement — the claim is about Treasury and the resolution settles on Yield. A row whose resolution checks a different fact can be scored correct while being wrong
- "On 2026-10-19, a major wildfire in Indonesia, fueled by El Niño, results in the destruction of more than 200 homes, as confirmed by the GDAC" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

4022 issued all-time across 21 forecaster arms · 2911 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 217 issued · 158 open · 58 resolved · 30 hits / 28 misses · **Brier 0.293** against its own base rate 51.7% (climatological 0.250) · **skill -0.173**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1128 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 328 | 270 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*