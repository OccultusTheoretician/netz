**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: lmstudio/auto · 2 accepted / 8 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-01 | 30% | 2026-10-18 | disaster | Between 2026-10-10 and 2026-10-16, a magnitude 6.0 or higher earthquake occurs in Panama, confirmed by USGS Significant Quakes and GDACS Alerts. | A magnitude 6.0 or higher earthquake occurs in Panama between 2026-10-10 and 2026-10-16, as confirmed by USGS Significant Quakes and GDACS Alerts. |
| KKR-20261010-02 | 35% | 2026-10-18 | political | Between 2026-10-10 and 2026-10-16, the US Department of Treasury releases a new sanctions list targeting Russian energy firms, confirmed by Al Jazeera and BBC World. | The US Department of Treasury releases a new sanctions list targeting Russian energy firms between 2026-10-10 and 2026-10-16, as confirmed by Al Jazeera and BBC World. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A Russian drone strike on Zaporizhzhia on 2026-10-12 kills at least 15 people, with confirmed casualties reported by BBC World and Al Jazeer" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-12 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-11, a missile attack in Gaza City results in at least 10 fatalities, confirmed by Al Jazeera and BBC World." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-11 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-10 and 2026-10-14, the S&P 500 closes above 7,850 on at least two separate trading days." → REJECTED: cites 75 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim; market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-10-10 and 2026-10-16, the CISA KEV catalog adds at least three new exploited vulnerabilities with a severity rating of 9.0 or h" → REJECTED: cites 106 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim
- "On 2026-10-13, the US Senate confirms a nominee to the Supreme Court, as reported by CNBC Top News and Politico." → REJECTED: cites 20 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-13 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-10 and 2026-10-16, a cyberattack using the P7 DarkSword iOS exploit kit results in the theft of at least 50,000 cryptocurren" → REJECTED: cites 102 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim
- "Between 2026-10-10 and 2026-10-16, a tropical storm causes at least 15 deaths in the Gulf Coast region of the United States, confirmed by th" → REJECTED: cites 51 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim
- "Between 2026-10-10 and 2026-10-16, a cyberattack on a South Korean financial institution using ARTEX AI and Claude agents results in a data " → REJECTED: cites 112 of 132 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim

## III. LEDGER STANDING

3781 issued all-time across 21 forecaster arms · 2967 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 407 issued · 228 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

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
| lmstudio/realist | 200 | 165 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
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