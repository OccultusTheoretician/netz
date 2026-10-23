**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: lmstudio/realist · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-54 | 35% | 2026-12-14 | economics/markets | On or before 2026-12-10, the 10-year U.S. Treasury yield will fall below 4.85 percent and remain below that level for at least three consecutive trading days. | The 10-year U.S. Treasury yield, as reported by FRED, is below 4.85 percent on 2026-12-10, 2026-12-11, and 2026-12-12. |
| KKR-20261023-55 | 20% | 2026-11-29 | cyber | Between 2026-11-20 and 2026-11-27, a cyberattack exploiting the Arista VeloCloud SQL injection flaw will be confirmed by at least two independent sources to have compromised a U.S. federal agency's network. | Two or more independent sources (not affiliated with the same outlet group) report that a U.S. federal agency's network was compromised via the Arista VeloCloud SQL injection flaw during the event window. |
| KKR-20261023-56 | 22% | 2026-11-20 | military/conflict | Between 2026-11-10 and 2026-11-17, a major offensive operation by Russian forces will be confirmed by two hostile sides (RU, UA) to have begun in the Luhansk region of Ukraine. | At least two reports from hostile sides (RU, UA) confirm the start of a major offensive operation in Luhansk during the event window, with at least one report citing a significant troop or equipment movement. |
| KKR-20261023-57 | 32% | 2026-11-14 | cyber | Between 2026-11-05 and 2026-11-12, a cyberattack on a U.S. state government system will be confirmed by CISA to have exploited a known vulnerability in a widely used open-source library. | CISA's KEV catalog lists a new entry with a date-added value between 2026-11-05 and 2026-11-12, and the vulnerability is linked to a confirmed cyberattack on a U.S. state government system. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-11-15, the CISA KEV catalog will include at least one new entry for a critical SQL injection vulnerability in a widely used enterpri" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-15 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution names a different subject than the statement — the claim is about CISA, KEV, SQL and the resolution settles on CISA, CVSS, KEV. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-11-01 and 2026-11-07, a Russian military drone strike will result in at least one confirmed casualty in Kyiv, Ukraine." → REJECTED: cited items name United States; the claim is about Ukraine, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-12-03, a magnitude 6.5 or higher earthquake will be recorded in the Himalayan region, with at least 10 fatalities confirmed by two i" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-12-03 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-12-15, the S&P 500 index will close above 7,800 points for the first time since the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-12-15 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-11-28, a confirmed outbreak of Ebola in Nigeria will result in at least 15 new cases reported by the WHO or a national health author" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-28 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-11-18 and 2026-11-25, a political scandal involving a U.S. federal official will be confirmed by two major wire services to hav" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4769 issued all-time across 21 forecaster arms · 3417 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 242 issued · 155 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1679 | 1296 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 242 | 155 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*