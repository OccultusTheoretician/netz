**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101524Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-10 | 30% | 2026-09-19 | military/conflict | Between 2026-09-10 and 2026-09-16, at least one Grade A or B confirmed kinetic event will occur in the Russia-Ukraine Theatre involving a drone or missile strike with reported casualties. | At least one Grade A or B confirmed kinetic event involving a drone or missile strike with reported casualties occurs in the Russia-Ukraine Theatre between 2026-09-10 and 2026-09-16. |
| KKR-20260910-11 | 25% | 2026-09-19 | economics/markets | Between 2026-09-10 and 2026-09-16, the European Central Bank will announce a second interest rate hike in 2026, raising rates to 2.75%. | The European Central Bank announces a second interest rate hike in 2026, raising rates to 2.75%, between 2026-09-10 and 2026-09-16. |
| KKR-20260910-12 | 30% | 2026-09-19 | disaster | Between 2026-09-10 and 2026-09-16, a confirmed natural disaster (flood, fire, or earthquake) will result in at least 50 fatalities in a country outside the United States. | A confirmed natural disaster (flood, fire, or earthquake) results in at least 50 fatalities in a country outside the United States between 2026-09-10 and 2026-09-16. |
| KKR-20260910-13 | 15% | 2026-09-19 | political | Between 2026-09-10 and 2026-09-16, a political figure in the United States will be indicted on federal corruption charges. | A political figure in the United States is indicted on federal corruption charges between 2026-09-10 and 2026-09-16. |
| KKR-20260910-14 | 25% | 2026-09-19 | cyber | Between 2026-09-10 and 2026-09-16, a major cyberattack will exploit a zero-day vulnerability in Google Chrome, resulting in the compromise of at least 1 million user accounts. | A major cyberattack exploits a zero-day vulnerability in Google Chrome, resulting in the compromise of at least 1 million user accounts between 2026-09-10 and 2026-09-16. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-15, the CISA KEV catalog will carry CVE-2026-19490 with a date-added value of 2026-09-09." → REJECTED: event window opens 2026-09-09, before this row is sealed (2026-09-10, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-10 and 2026-09-16, the 10-year Treasury yield will exceed 4.92 percent at any point during the trading day." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-09-10 and 2026-09-16, at least one confirmed cyberattack exploiting CVE-2026-20079 will be reported by a wire service or govern" → REJECTED: resolution offers alternative VENUES joined by 'or' (…wire service | or | government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-10 and 2026-09-16, a major cyberattack will result in the exposure of over 10 million user records from a U.S.-based financi" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-10 and 2026-09-16, the S&P 500 will close below 7,500 on at least one trading day." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1822 issued all-time across 16 forecaster arms · 1486 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 37 issued · 37 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 567 | 529 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*