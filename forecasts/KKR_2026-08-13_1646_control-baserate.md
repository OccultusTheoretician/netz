**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131646Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-13_1519.md · forecaster: control/baserate · 7 accepted / 0 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260813-15 | 33% | 2026-10-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose affected product is Microsoft SharePoint, with a dateAdded value between 2026-08-14 and 2026-09-30. | TRUE if a fetch of the CISA KEV JSON at the deadline shows any Microsoft SharePoint entry with dateAdded between 2026-08-14 and 2026-09-30 inclusive; otherwise FALSE. |
| KKR-20260813-16 | 33% | 2026-11-03 | political | The White House publicly names a specific individual as the next White House press secretary, acting or permanent, between 2026-08-14 and 2026-10-30. | TRUE if AP or Reuters carries a White House announcement, dated between 2026-08-14 and 2026-10-30, naming a specific successor as press secretary; otherwise FALSE. |
| KKR-20260813-17 | 33% | 2026-08-21 | political | The Reform UK candidate is declared the winner of the Clacton by-election held on 2026-08-13. | TRUE if the returning officer's declared result, as carried by BBC or PA Media, names the Reform UK candidate as the winner; otherwise FALSE. |
| KKR-20260813-18 | 33% | 2026-10-02 | disaster | At least one reactor unit at Romania's Cernavoda nuclear plant records nonzero electricity output on the ENTSO-E transparency platform on at least one day between 2026-08-14 and 2026-09-30. | TRUE if ENTSO-E actual generation per generation unit shows output above 0 MW for any Cernavoda unit on any date between 2026-08-14 and 2026-09-30; otherwise FALSE. |
| KKR-20260813-19 | 33% | 2026-11-03 | military/conflict | The United States and Iran both publicly confirm a ceasefire or framework agreement between them, with confirmations dated between 2026-08-14 and 2026-10-30. | TRUE if statements from both the US and Iranian governments confirming a ceasefire or framework agreement, each carried by AP, Reuters, or AFP, are dated between 2026-08-14 and 2026-10-30; otherwise FALSE. |
| KKR-20260813-20 | 33% | 2026-09-30 | military/conflict | The OHCHR human rights monitoring mission monthly update covering August 2026 reports a Ukraine civilian-killed total lower than the July 2026 total it states. | TRUE if the published OHCHR HRMMU update covering August 2026 states an August civilian-killed total strictly below its stated July 2026 total; FALSE if equal, higher, or no update is published by the deadline. |
| KKR-20260813-21 | 33% | 2026-10-19 | crime/security | Nick Reiner enters a plea in court to the indictment referenced in reporting dated 2026-08-13, with the plea entered between 2026-08-14 and 2026-10-15. | TRUE if Los Angeles County court records, or reporting by AP, Reuters, or the Los Angeles Times, show a plea entered by Nick Reiner between 2026-08-14 and 2026-10-15; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

576 issued all-time across 14 forecaster arms · 520 open (7 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 96 issued · 96 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 96 | 96 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 64 | 62 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*