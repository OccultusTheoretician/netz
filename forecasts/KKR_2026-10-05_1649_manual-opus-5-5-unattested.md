**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051649Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-55 | 70% | 2026-10-28 | political | Flavio Bolsonaro wins the Brazilian presidential runoff held on 2026-10-25, defeating Luiz Inacio Lula da Silva with more than 50 percent of valid votes. | TRUE if the Superior Electoral Court (TSE) official result for the 2026-10-25 presidential runoff gives Flavio Bolsonaro more than 50 percent of valid votes; otherwise FALSE. |
| KKR-20261005-56 | 64% | 2026-12-09 | political | In the Spanish general election held on 2026-11-29, PP lists and Vox lists together win at least 176 of the 350 seats in the Congress of Deputies. | TRUE if Interior Ministry or Central Electoral Board results for the 2026-11-29 general election, including the overseas vote, give PP lists (including PP-led coalitions) and Vox at least 176 Congress seats combined; otherwise FALSE. |
| KKR-20261005-57 | 80% | 2027-01-19 | political | In a floor vote held between 2027-01-03 and 2027-01-15, the US House of Representatives elects a Democrat as Speaker of the 120th Congress following the 2026-11-03 midterm elections. | TRUE if a roll call recorded by the Clerk of the House between 2027-01-03 and 2027-01-15 elects a Democratic member as Speaker of the 120th Congress; otherwise FALSE. |
| KKR-20261005-58 | 20% | 2026-10-30 | economics/markets | At its meeting concluding on 2026-10-28, the FOMC raises the federal funds target range above the 3.75-4.00 percent range in force at seal. | TRUE if the FOMC statement released on 2026-10-28 sets a target range upper bound above 4.00 percent, shown by FRED series DFEDTARU for 2026-10-29; otherwise FALSE. Reference: 3.75-4.00 percent on the packet date. |
| KKR-20261005-59 | 30% | 2026-12-02 | cyber | CISA adds CVE-2026-61500, the Rejetto HFS session forgery flaw, to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-05 and 2026-11-30. | TRUE if the CISA KEV catalog lists CVE-2026-61500 with a dateAdded value between 2026-10-05 and 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20261005-60 | 84% | 2026-10-28 | military/conflict | Between 2026-10-12 and 2026-10-25, at least three separate weapon strikes on or seizures of merchant vessels occur in the Strait of Hormuz, Persian Gulf or Gulf of Oman. | TRUE if UKMTO incident notices record at least three distinct incidents dated 2026-10-12 to 2026-10-25 of merchant vessels struck by weapons or seized in the Strait of Hormuz, Persian Gulf or Gulf of Oman; otherwise FALSE. |
| KKR-20261005-61 | 25% | 2026-11-17 | military/conflict | The United States and Iran agree a ceasefire or truce, publicly confirmed by both the White House and the Iranian government, between 2026-10-05 and 2026-11-13. | TRUE if between 2026-10-05 and 2026-11-13 the White House and the Iranian government each publicly confirm a US-Iran ceasefire or truce, as reported by at least two of Reuters, AP and AFP; otherwise FALSE. |
| KKR-20261005-62 | 74% | 2026-11-17 | crime/security | Between 2026-10-05 and 2026-11-13, Japanese prosecutors indict the US Marine arrested on Okinawa on 2026-10-04 over the killing of a 39-year-old woman in a Naha hotel. | TRUE if Kyodo or NHK reports the Naha District Public Prosecutors Office indicted that Marine on murder, robbery-murder or any other charge tied to the death, with the indictment dated 2026-10-05 to 2026-11-13; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The ECB euro foreign exchange reference rate for the US dollar published for 2026-11-27 is below 1.1000 dollars per euro." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-27 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "GDACS raises tropical cyclone KOGUMA-26 to an Orange or Red alert level at any update issued between 2026-10-05 and 2026-10-19." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

3453 issued all-time across 21 forecaster arms · 2639 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 95 issued · 95 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1234 | 1033 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*