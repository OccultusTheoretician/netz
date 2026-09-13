**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131715Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260913-01 | 25% | 2026-09-28 | economics/markets | Between 2026-09-18 and 2026-09-25, the S&P 500 closes above 7,700 points on at least three trading days, with each close verified by the Dow Jones Market Data feed. | The Dow Jones Market Data feed shows the S&P 500 closing above 7,700 on three or more days between 2026-09-18 and 2026-09-25. |
| KKR-20260913-02 | 35% | 2026-10-01 | cyber | Between 2026-09-20 and 2026-09-27, a cyberattack exploiting a vulnerability in a major cloud provider's API is confirmed by CISA KEV and two independent security firms. | The CISA KEV catalog carries a date-added value between 2026-09-20 and 2026-09-27 for a vulnerability exploited in a cloud provider's API, with two independent security firms reporting the exploit. |
| KKR-20260913-03 | 30% | 2026-10-02 | disaster | Between 2026-09-21 and 2026-09-28, a major forest fire in California spreads beyond 5,000 acres, as confirmed by the USGS Significant Quakes feed and two independent news outlets. | The USGS Significant Quakes feed and two independent news outlets confirm a forest fire in California exceeding 5,000 acres between 2026-09-21 and 2026-09-28. |
| KKR-20260913-04 | 20% | 2026-09-26 | political | On 2026-09-23, a new political coalition in Sweden is formed following the general election, with the far-right party securing a ministerial role, as confirmed by the Swedish government's official website and two international news agencies. | The Swedish government's official website and two international news agencies (e.g., BBC, Al Jazeera) confirm the formation of a new coalition government with a far-right minister on 2026-09-23. |
| KKR-20260913-05 | 35% | 2026-09-29 | military/conflict | Between 2026-09-19 and 2026-09-26, Iran conducts a ballistic missile test near the Strait of Hormuz, resulting in a confirmed alert from the UKMTO and two independent satellite tracking services. | The UKMTO alert and two independent satellite tracking services confirm a ballistic missile test near the Strait of Hormuz between 2026-09-19 and 2026-09-26. |
| KKR-20260913-06 | 30% | 2026-10-01 | economics/markets | Between 2026-09-20 and 2026-09-27, the price of Brent crude oil exceeds $110 per barrel on at least two consecutive trading days, as verified by the FRED database. | The FRED database shows Brent crude oil exceeding $110 per barrel on two or more consecutive trading days between 2026-09-20 and 2026-09-27. |
| KKR-20260913-07 | 25% | 2026-09-28 | political | On 2026-09-25, a new BRICS summit resolution is adopted calling for a joint peace initiative in the Middle East, as confirmed by the official BRICS website and two international news agencies. | The official BRICS website and two international news agencies (e.g., Al Jazeera, BBC) confirm the adoption of a joint peace initiative resolution at the BRICS summit on 2026-09-25. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-15, a Russian drone strike hits a civilian train near the Polish border in the Kyiv-Warsaw corridor, resulting in at least three " → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "On 2026-09-22, the US Federal Reserve announces a 0.5 percentage point increase in the federal funds rate, as reported by the Federal Reserv" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-22 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-24, a cyberattack on a major U.S. financial institution results in a temporary outage of online banking services, confirmed by th" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-24 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2019 issued all-time across 16 forecaster arms · 1683 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 60 issued · 60 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 649 | 611 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*