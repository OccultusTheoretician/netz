**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-23 | 35% | 2026-12-14 | economics/markets | The 10-Year US Treasury yield closes above 5.50 percent on at least one trading day between 2026-12-07 and 2026-12-11. Reference: 5.24 on the packet date. | The closing yield of the US 10-Year Treasury note is recorded above 5.50 on any trading day within the window. |
| KKR-20261012-24 | 20% | 2026-12-03 | cyber | A new exploited vulnerability is added to the CISA KEV catalog with a date-added value between 2026-11-01 and 2026-11-30. | A new entry appears in the CISA KEV catalog with a date-added value falling between 2026-11-01 and 2026-11-30. |
| KKR-20261012-25 | 30% | 2026-11-19 | disaster | A magnitude 6.0 or greater earthquake occurs in Panama between 2026-11-10 and 2026-11-16. | The USGS Significant Quakes catalog records an earthquake of magnitude 6.0 or higher in Panama within the window. |
| KKR-20261012-26 | 25% | 2026-12-10 | political | The European Union imposes a new tariff or quota on Chinese electric vehicles between 2026-12-01 and 2026-12-07. | The European Commission publishes an official regulation or decision limiting Chinese EV imports within the window. |
| KKR-20261012-27 | 35% | 2026-11-30 | economics/markets | WTI Crude oil closes above 100.00 on at least one trading day between 2026-11-23 and 2026-11-27. Reference: 93.80 on the packet date. | The closing price of WTI Crude oil is recorded above 100.00 on any trading day within the window. |
| KKR-20261012-28 | 25% | 2026-11-05 | economics/markets | A major US bank reports a quarterly net loss between 2026-10-26 and 2026-11-02. | A US bank with assets over 100 billion reports a net loss for the quarter ending in October 2026. |
| KKR-20261012-29 | 20% | 2026-11-10 | disaster | A new case of measles is confirmed in the US between 2026-11-01 and 2026-11-07. | The CDC or a state health department confirms a new measles case within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,700.00 on at least one trading day between 2026-11-02 and 2026-11-06. Reference: 7,810.08 on the packet dat" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A Houthi attack on a Saudi commercial airport is confirmed by two hostile sides between 2026-11-15 and 2026-11-21." → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | two…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A US federal judge issues a final order blocking taxpayer-funded TV ads by 2026-11-20." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3963 issued all-time across 21 forecaster arms · 2935 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 40 issued · 40 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1399 | 1125 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 320 | 264 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*