**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-20 | 25% | 2026-11-24 | disaster | The USGS catalog records an earthquake of magnitude 6.0 or greater in Russia between 2026-11-15 and 2026-11-21. | The USGS Significant Quakes catalog carries a date-added value between 2026-11-15 and 2026-11-21 for an event with magnitude 6.0 or greater located in Russia. |
| KKR-20261017-21 | 45% | 2026-11-10 | cyber | CISA KEV adds a new exploited vulnerability between 2026-11-01 and 2026-11-07. | The CISA KEV catalog carries a new entry with a date-added value between 2026-11-01 and 2026-11-07. |
| KKR-20261017-22 | 35% | 2026-12-10 | economics/markets | The 10-year US Treasury yield closes above 5.25 percent on at least one trading day between 2026-12-01 and 2026-12-07. | The final 10-year US Treasury yield recorded by the exchange on any trading day between 2026-12-01 and 2026-12-07 is strictly greater than 5.25 percent. Reference: 5.10 on the packet date. |
| KKR-20261017-23 | 40% | 2026-11-19 | political | A US federal court issues a final judgment in the Elon Musk 2024 election lottery lawsuit between 2026-11-10 and 2026-11-16. | A US federal court docket records a final judgment or order resolving the core dispute in the Elon Musk 2024 election lottery lawsuit between 2026-11-10 and 2026-11-16. |
| KKR-20261017-24 | 30% | 2026-12-24 | economics/markets | The Brent crude oil price closes above 115.00 on at least one trading day between 2026-12-15 and 2026-12-21. | The final Brent crude oil closing price recorded by the exchange on any trading day between 2026-12-15 and 2026-12-21 is strictly greater than 115.00. Reference: 109.86 on the packet date. |
| KKR-20261017-25 | 35% | 2026-11-29 | political | A US federal judge signs an order granting the preliminary injunction in the Ilhan Omar federal search lawsuit between 2026-11-20 and 2026-11-26. | A US federal court docket records a signed order granting the preliminary injunction in the Ilhan Omar federal search lawsuit between 2026-11-20 and 2026-11-26. |
| KKR-20261017-26 | 20% | 2027-01-19 | disaster | The USGS catalog records an earthquake of magnitude 7.0 or greater between 2027-01-10 and 2027-01-16. | The USGS Significant Quakes catalog carries a date-added value between 2027-01-10 and 2027-01-16 for an event with magnitude 7.0 or greater. |
| KKR-20261017-27 | 25% | 2027-03-10 | cyber | A new exploited vulnerability is added to the CISA KEV catalog with a date-added value between 2027-03-01 and 2027-03-07. | The CISA KEV catalog carries a new entry with a date-added value between 2027-03-01 and 2027-03-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,500 on at least one trading day between 2026-11-02 and 2026-11-06. Reference: 7,659.44 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The Federal Reserve announces an interest rate cut between 2027-02-01 and 2027-02-07." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4346 issued all-time across 21 forecaster arms · 3235 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 72 issued · 72 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1526 | 1230 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*