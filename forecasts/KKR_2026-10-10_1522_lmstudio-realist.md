**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-03 | 30% | 2026-10-22 | military/conflict | Between 2026-10-12 and 2026-10-18, a Russian glide bomb attack on Zaporizhzhia will result in at least 15 confirmed fatalities. | At least 15 confirmed fatalities are reported in the aftermath of a Russian glide bomb attack on Zaporizhzhia between 2026-10-12 and 2026-10-18. |
| KKR-20261010-04 | 35% | 2026-10-23 | cyber | Between 2026-10-13 and 2026-10-19, a cyberattack exploiting unpatched AhsayCBS flaws will result in the deployment of webshells on at least one critical infrastructure system. | At least one critical infrastructure system reports the deployment of a webshell via exploitation of unpatched AhsayCBS flaws between 2026-10-13 and 2026-10-19. |
| KKR-20261010-05 | 20% | 2026-10-24 | disaster | Between 2026-10-14 and 2026-10-20, a tropical storm will cause at least one fatality in the U.S. Gulf Coast region. | At least one fatality is reported in the U.S. Gulf Coast region due to a tropical storm between 2026-10-14 and 2026-10-20. |
| KKR-20261010-06 | 25% | 2026-10-26 | cyber | Between 2026-10-16 and 2026-10-22, a cyberattack using ARTEX AI or Claude agents will target at least one South Korean financial institution. | At least one South Korean financial institution reports a cyberattack involving ARTEX AI or Claude agents between 2026-10-16 and 2026-10-22. |
| KKR-20261010-07 | 10% | 2026-10-28 | political | Between 2026-10-18 and 2026-10-24, a new diplomatic initiative involving Trump, Putin, and Zelensky will be publicly announced. | A new diplomatic initiative involving Trump, Putin, and Zelensky is publicly announced between 2026-10-18 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-15, the CISA KEV catalog will carry at least one new entry with a date-added value between 2026-10-11 and 2026-10-14." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-16, the S&P 500 will close below 7,750.00." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-16 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-15 and 2026-10-21, a new round of sanctions will be imposed by the U.S. on Iran related to nuclear activities." → REJECTED: cited items name Russian Federation, United States; the claim is about Iran, Islamic Republic of — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-17, the 10-year U.S. Treasury yield will settle at or above 5.35 percent." → REJECTED: cited items name Mozambique; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-20, the Brent crude oil price will close above 106.00 per barrel." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-20 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

3786 issued all-time across 21 forecaster arms · 2972 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 205 issued · 170 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1347 | 1146 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 21 | 21 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 205 | 170 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 302 | 269 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*