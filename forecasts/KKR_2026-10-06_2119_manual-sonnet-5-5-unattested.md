**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062119Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: manual/sonnet-5.5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-44 | 72% | 2026-10-23 | military/conflict | Between 2026-10-07 and 2026-10-21, at least one commercial vessel is struck by a drone, missile or other projectile in the Strait of Hormuz or the Gulf of Oman. | UKMTO, US Central Command, or two of Reuters, AP and AFP report a commercial vessel struck by a drone, missile or projectile in the Strait of Hormuz or Gulf of Oman between 2026-10-07 and 2026-10-21. |
| KKR-20261006-45 | 38% | 2026-10-26 | political | Between 2026-10-07 and 2026-10-22, the British Consulate-General in East Jerusalem closes or suspends operations in response to the Israeli order to close it by 2026-10-08. | The UK Foreign Office, or two of Reuters, AP, AFP and BBC, state that the British Consulate-General in East Jerusalem closed or suspended operations between 2026-10-07 and 2026-10-22 because of the Israeli closure order. |
| KKR-20261006-46 | 18% | 2026-10-30 | cyber | Between 2026-10-07 and 2026-10-28, the CISA Known Exploited Vulnerabilities catalog gains at least one entry whose vendorProject is Rejetto. | The CISA KEV catalog JSON carries at least one entry with vendorProject Rejetto and a dateAdded value between 2026-10-07 and 2026-10-28 inclusive. |
| KKR-20261006-47 | 35% | 2026-10-30 | disaster | Between 2026-10-07 and 2026-10-28, the Kenyan Ministry of Health or the WHO announces at least one further laboratory-confirmed Ebola case in Kenya beyond those announced on or before 2026-10-06. | The Kenyan Ministry of Health or the WHO announces between 2026-10-07 and 2026-10-28 at least one new laboratory-confirmed Ebola case in Kenya beyond those already announced on or before 2026-10-06. |
| KKR-20261006-48 | 36% | 2026-11-06 | economics/markets | The US goods and services trade deficit for September 2026, first published in the BEA and Census release scheduled for 2026-11-04, is larger than 105.6 billion dollars. Reference: August 2026 deficit of 105.6 billion dollars, released 2026-10-06. | The BEA and Census release of 2026-11-04 reports a September 2026 goods and services deficit above 105.6 billion dollars, as first published. Reference: 105.6 billion dollars for August 2026, released 2026-10-06. |
| KKR-20261006-49 | 22% | 2026-11-25 | economics/markets | The US 10-year constant maturity Treasury yield for 2026-11-20 is at or above 5.50 percent. Reference: 5.26 percent in the packet market snapshot of 2026-10-06. | FRED series DGS10 reports a value of 5.50 or higher for 2026-11-20. Reference: 5.26 percent on the packet date 2026-10-06. |
| KKR-20261006-50 | 30% | 2026-12-11 | economics/markets | The WTI crude oil spot price for 2026-12-04 is below 80.00 dollars per barrel. Reference: 87.77 dollars per barrel in the packet market snapshot of 2026-10-06. | FRED series DCOILWTICO reports a value below 80.00 for 2026-12-04. Reference: 87.77 dollars per barrel on the packet date 2026-10-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-07 and 2026-11-04, Houthi forces launch at least one missile or drone that is aimed at, or lands in, Saudi territory." → REJECTED: resolution offers alternative VENUES joined by 'or' (…audi ministry of defense, saudi press agency, | or | two of reuters, ap   afp report a houthi-laun…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "In the US general election of 2026-11-03, candidates of the Democratic Party win at least 218 of the 435 seats in the US House of Representa" → REJECTED: cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-07 and 2026-12-11, the Pentagon or the US Army publicly announces a specific calendar date for the execution of Nidal Hasan " → REJECTED: resolution offers alternative VENUES joined by 'or' (…pentagon | or | army…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3511 issued all-time across 21 forecaster arms · 2697 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 61 issued · 61 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1250 | 1049 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*