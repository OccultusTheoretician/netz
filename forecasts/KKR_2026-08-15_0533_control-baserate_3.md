**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 150533Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-14_1517.md · forecaster: control/baserate · 3 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260815-20 | 18% | 2026-09-29 | economic | The 10-Year Treasury Constant Maturity Rate, FRED series DGS10, closes at or above 4.75 percent on at least one trading day between 2026-08-17 and 2026-09-25. | The FRED DGS10 series shows a closing value of 4.75 or higher for at least one date between 2026-08-17 and 2026-09-25. |
| KKR-20260815-21 | 33% | 2026-10-19 | military_conflict | NATO or a Baltic national air force kinetically shoots down or intercepts a drone or unmanned aerial vehicle inside Estonian, Latvian, or Lithuanian airspace, distinct from the August 14, 2026 Balvi incident, between 2026-08-21 and 2026-10-15. | NATO, a Baltic Ministry of Defence, or two of Reuters, AP, and Bloomberg confirm a kinetic drone shoot-down in Baltic airspace within the window, distinct from the Aug 14 Balvi incident. |
| KKR-20260815-22 | 33% | 2026-12-02 | military_conflict | The government of Russia publishes a decree ordering a new mandatory, non-contract mobilization wave of reservists, distinct from routine conscription and from the September 2022 partial mobilization, between 2026-08-21 and 2026-11-30. | The official Russian legal register, pravo.gov.ru, publishes a mobilization decree, corroborated by two of Reuters, AP, ISW, and Meduza, within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

622 issued all-time across 14 forecaster arms · 566 open (34 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 116 issued · 116 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 116 | 116 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 70 | 68 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 35 | 35 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 55 | 55 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 47 | 47 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*