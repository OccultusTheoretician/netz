**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: lmstudio/realist · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-01 | 28% | 2026-10-20 | military/conflict | On 2026-10-12, a missile strike confirmed by at least two hostile sides (RU, UA) occurred in Kyiv, resulting in at least one casualty and damage to a civilian infrastructure site. | The CISA KEV catalog carries a date-added value between 2026-10-12 and 2026-10-18, and the event is corroborated by at least two independent sources from hostile sides (RU, UA) reporting a missile strike in Kyiv with at least one casualty and confirmed infrastructure damage. |
| KKR-20261011-02 | 45% | 2026-10-22 | cyber | Between 2026-10-14 and 2026-10-20, a cyberattack exploiting a vulnerability in the Nippon Columbia karaoke database results in the exfiltration of at least 8 million user records, as confirmed by a third-party security audit. | The CISA KEV catalog carries a date-added value between 2026-10-14 and 2026-10-20, and a third-party security audit confirms that at least 8 million user records were exfiltrated from the Nippon Columbia database due to a known vulnerability. |
| KKR-20261011-03 | 25% | 2026-10-24 | military/conflict | Between 2026-10-16 and 2026-10-22, Saudi Arabia launches a retaliatory airstrike on a Houthi-controlled airfield in Yemen, confirmed by at least two independent sources from hostile sides (IL, AXIS). | At least two independent sources from hostile sides (IL, AXIS) report a Saudi airstrike on a Houthi-controlled airfield in Yemen between 2026-10-16 and 2026-10-22, with no conflicting reports denying the event. |
| KKR-20261011-04 | 30% | 2026-10-19 | economics/markets | On 2026-10-17, the S&P 500 closes below 7,750 points for the first time since 2026-09-20, as confirmed by the Dow Jones Market Data feed. | The Dow Jones Market Data feed confirms that the S&P 500 closed below 7,750 points on 2026-10-17, with the closing value recorded at or below 7,749.99. |
| KKR-20261011-05 | 40% | 2026-10-26 | cyber | Between 2026-10-18 and 2026-10-24, a new exploit kit named 'P7 DarkSword' is observed in the wild, targeting iOS devices and stealing cryptocurrency wallet data, as confirmed by at least two independent cybersecurity sources. | The CISA KEV catalog carries a date-added value between 2026-10-18 and 2026-10-24, and at least two independent cybersecurity sources (e.g., BleepingComputer, The Hacker News) confirm the existence and use of the P7 DarkSword exploit kit targeting iOS devices and stealing cryptocurrency wallet data. |
| KKR-20261011-06 | 22% | 2026-10-28 | political | Between 2026-10-20 and 2026-10-26, a political crisis in Poland leads to the resignation of Prime Minister Donald Tusk, confirmed by a parliamentary vote recorded in the official government docket. | The official Polish government docket records a parliamentary vote on or before 2026-10-26 that results in the resignation of Prime Minister Donald Tusk, with at least two independent news outlets (e.g., Al Jazeera, Guardian World) confirming the outcome. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-13 and 2026-10-19, the US Federal Reserve announces a 0.5 percentage point increase in the federal funds rate, with the new " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-15, a magnitude 7.0 or greater earthquake occurs in the Panama region, with a depth of less than 60 km and a confirmed epicenter " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-15 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-19, a major forest fire in Mozambique is confirmed by GDACS Alerts and at least one independent news outlet to have destroyed at " → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "On 2026-10-21, the Brent crude oil price exceeds 110 USD per barrel for the first time since 2026-09-25, as confirmed by the CME Group's off" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3862 issued all-time across 21 forecaster arms · 3048 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 211 issued · 176 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1372 | 1171 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 30 | 30 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 27 | 27 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 312 | 279 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*