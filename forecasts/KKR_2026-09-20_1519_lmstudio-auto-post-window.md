**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-20_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260920-01 | 30% | 2026-10-01 | military/conflict | Moscow was struck by a drone attack between 2026-09-21 and 2026-09-24, resulting in at least one confirmed casualty. | At least one confirmed casualty from a drone attack on Moscow is reported by at least two independent, non-aligned news outlets (e.g., BBC, Al Jazeera, Reuters, AP) between 2026-09-21 and 2026-09-24. |
| KKR-20260920-02 | 45% | 2026-10-07 | economics/markets | The S&P 500 closes above 7,800.00 on or before 2026-10-05. | The closing price of the S&P 500 index on or before 2026-10-05 is greater than 7,800.00, as reported by the CBOE or a major financial data provider such as Bloomberg or Reuters. |
| KKR-20260920-03 | 40% | 2026-10-01 | political | Iran announces a new condition for ending its war with the U.S. between 2026-09-21 and 2026-09-24, confirmed by at least two independent news outlets. | At least two independent, non-aligned news outlets (e.g., Al Jazeera, BBC, Reuters) report that Iran has announced a new condition for ending its war with the U.S. between 2026-09-21 and 2026-09-24. |
| KKR-20260920-04 | 20% | 2026-10-01 | cyber | A cyberattack targeting a U.S. federal agency is confirmed by CISA KEV between 2026-09-21 and 2026-09-24, with a public advisory issued. | The CISA KEV catalog contains a new entry with a date-added value between 2026-09-21 and 2026-09-24, explicitly linking a vulnerability to a confirmed cyberattack on a U.S. federal agency. |
| KKR-20260920-05 | 30% | 2026-10-01 | disaster | A tropical cyclone with Category 3 or higher intensity makes landfall in the U.S. between 2026-09-21 and 2026-09-24, confirmed by the National Hurricane Center. | The National Hurricane Center (NHC) issues a landfall advisory for a tropical cyclone with sustained winds of at least 111 mph (Category 3 or higher) in the United States between 2026-09-21 and 2026-09-24. |
| KKR-20260920-06 | 35% | 2026-10-01 | military/conflict | A major offensive operation begins in the Gaza Strip between 2026-09-21 and 2026-09-24, confirmed by at least two independent news outlets. | At least two independent, non-aligned news outlets (e.g., Al Jazeera, BBC, Reuters) report that a major offensive operation has begun in the Gaza Strip between 2026-09-21 and 2026-09-24. |
| KKR-20260920-07 | 50% | 2026-10-07 | economics/markets | The 10-year U.S. Treasury yield exceeds 5.25% on or before 2026-10-05, based on the FRED database. | The 10-year U.S. Treasury yield, as reported by FRED (Federal Reserve Economic Data), exceeds 5.25% on or before 2026-10-05. |
| KKR-20260920-08 | 25% | 2026-10-01 | cyber | A new cyberattack on a critical infrastructure system in Europe is confirmed by the EU Agency for Cybersecurity (ENISA) between 2026-09-21 and 2026-09-24. | ENISA issues a public advisory confirming a cyberattack on a critical infrastructure system in Europe between 2026-09-21 and 2026-09-24, with the event date within that window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A vulnerability in the OpenAI Codex sandbox is exploited in a real-world system between 2026-09-21 and 2026-10-05, leading to unauthorized a" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A magnitude 6.5 or greater earthquake occurs in Papua New Guinea between 2026-09-21 and 2026-09-24, with a confirmed death toll of at least " → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

2554 issued all-time across 16 forecaster arms · 2088 open (164 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 309 issued · 159 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 876 | 791 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 309 | 159 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 91 | 86 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 141 | 131 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 299 | 282 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 277 | 229 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*