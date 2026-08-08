**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082141Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-08_1517.md · forecaster: manual/fable-5 · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260808-07 | 90% | 2026-08-26 | military/conflict | Between 2026-08-09 and 2026-08-22 at least one Russian missile or drone strike causing damage or casualties in Kyiv city or Kyiv oblast is reported by at least two of BBC, Reuters, AP, AFP. | By the deadline, published reporting from at least two of BBC, Reuters, AP, AFP documents such a strike with impact dated inside the window; otherwise false. |
| KKR-20260808-08 | 85% | 2026-10-14 | crime/security | Between 2026-08-09 and 2026-10-09 the US Department of Justice announces the extradition of at least one defendant from Colombia to the United States on drug trafficking charges. | A justice.gov press release dated inside the window announces at least one extradition from Colombia on drug trafficking charges; absent such a release, false. |
| KKR-20260808-09 | 65% | 2026-08-18 | disaster | Between 2026-08-08 and 2026-08-15 the circulation center of Typhoon Dolphin makes landfall on mainland China. | GDACS tropical cyclone records, JMA, or CMA tracking show the center of Dolphin crossing the mainland China coastline inside the window; dissipation over water or landfall elsewhere resolves false. |
| KKR-20260808-10 | 55% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry naming Metabase as vendor or product with a date-added value between 2026-08-09 and 2026-10-09. | The public CISA KEV catalog contains an entry whose vendor or product field names Metabase with a dateAdded value inside the window; otherwise false. |
| KKR-20260808-11 | 25% | 2026-10-06 | political | The incumbent governor of Rhode Island is defeated in a gubernatorial primary held between 2026-09-01 and 2026-09-30. | Rhode Island Department of State results show the sitting governor losing a September 2026 gubernatorial primary; if the incumbent wins, is unopposed, is not a candidate, or no primary occurs, false. |
| KKR-20260808-12 | 25% | 2026-10-13 | political | Between 2026-08-09 and 2026-10-09 the United States and Iran announce an agreement or arrangement governing commercial transit through the Strait of Hormuz. | An official statement dated inside the window on state.gov or whitehouse.gov announces a US-Iran agreement, arrangement, or understanding on Strait of Hormuz commercial transit; otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-09 and 2026-09-08 at least one commercial vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman is struck or targete" → REJECTED: the resolution names a different subject than the statement — the claim is about Gulf, Hormuz, Oman, Persian and the resolution settles on AFP, AP, BBC, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "The FOMC statement following its September 2026 scheduled meeting announces a federal funds target range lower than the range in effect on 2" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-08-07, before this row is sealed (2026-08-08) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On at least one trading day between 2026-08-10 and 2026-10-30 the S&P 500 official closing value falls 3.0 percent or more from the prior tr" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The daily WTI crude oil spot price at Cushing exceeds 100.00 USD on at least one day between 2026-08-10 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about Cushing, WTI and the resolution settles on DCOILWTICO, FRED. A row whose resolution checks a different fact can be scored correct while being wrong; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

391 issued all-time across 14 forecaster arms · 341 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5`:** 29 issued · 29 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 33 | 31 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 20 | 32 | 9 | 23 | 0.221 | 28.1% | 0.202 | -0.093 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 23 | 21 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*