**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181815Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-18_1516.md · forecaster: manual/fable-5/unattested · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260818-09 | 90% | 2026-09-22 | military/conflict | Russian forces strike Kyiv with missiles or drones at least once between 2026-08-19 and 2026-09-18, confirmed by Ukrainian officials and carried by a major international wire service. | Reuters, AP, or AFP and at least one Ukrainian government source report a Russian missile or drone strike on Kyiv occurring between 2026-08-19 and 2026-09-18. |
| KKR-20260818-10 | 30% | 2026-10-02 | military/conflict | United States forces conduct military strikes on targets inside Iranian territory between 2026-08-19 and 2026-09-30. | The US Department of Defense or the President announces US strikes on targets inside Iran conducted between 2026-08-19 and 2026-09-30, and Iranian state media acknowledge strikes occurred. |
| KKR-20260818-11 | 15% | 2026-11-03 | cyber | A vulnerability in a GitLab product is added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-19 and 2026-10-31. | The CISA KEV catalog contains at least one entry listing GitLab as vendor or product with dateAdded between 2026-08-19 and 2026-10-31. |
| KKR-20260818-12 | 40% | 2026-09-08 | political | A petition challenging the 2026 Zambian presidential election result is filed with the Constitutional Court of Zambia between 2026-08-18 and 2026-09-04. | Constitutional Court of Zambia records or at least two international wire services report a petition challenging the presidential result was filed between 2026-08-18 and 2026-09-04. |
| KKR-20260818-13 | 80% | 2026-12-02 | crime/security | A jury verdict is returned or a mistrial is declared between 2026-08-18 and 2026-11-30 in the Nevada trial over the 1996 killing of Tupac Shakur. | Nevada court records or at least two major wire services report a jury verdict returned or a mistrial declared in the Tupac Shakur murder trial between 2026-08-18 and 2026-11-30. |
| KKR-20260818-14 | 60% | 2026-11-03 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 6.5 or greater with an epicenter in Indonesia occurring between 2026-08-19 and 2026-10-31 UTC. | The USGS ComCat catalog lists at least one event of magnitude 6.5 or greater located within Indonesia with origin time between 2026-08-19 and 2026-10-31 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent crude front-month futures settle above 100.00 US dollars on at least one trading day between 2026-08-19 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Federal Open Market Committee announces no change to the federal funds target range at its scheduled meeting concluding 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about Committee, Federal, Market, Open and the resolution settles on FOMC. A row whose resolution checks a different fact can be scored correct while being wrong
- "The CISA Known Exploited Vulnerabilities catalog gains at least 12 entries with dateAdded values between 2026-08-19 and 2026-09-30 inclusive" → REJECTED: the resolution names only a venue or register (CISA, KEV, json) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The GDACS alert level for tropical cyclone SEVENTEEN-26 reaches Orange or Red between 2026-08-19 and 2026-09-01." → REJECTED: resolution offers alternative VENUES joined by 'or' (…orange | or | red…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

722 issued all-time across 14 forecaster arms · 632 open (6 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 53 issued · 53 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 149 | 141 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 100 | 88 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 63 | 63 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 58 | 57 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*