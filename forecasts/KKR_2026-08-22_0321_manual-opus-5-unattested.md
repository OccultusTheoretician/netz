**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220321Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/opus-5/unattested · 3 accepted / 7 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-06 | 85% | 2026-11-30 | disaster | The NOAA Climate Prediction Center ENSO Diagnostic Discussion issued in November 2026 states that El Nino conditions are present. | TRUE if the CPC ENSO Diagnostic Discussion dated in November 2026 characterizes the state of the system as El Nino conditions present or continuing; FALSE if it states ENSO-neutral or La Nina. |
| KKR-20260822-07 | 22% | 2026-12-03 | economics | ICE Brent front-month futures settle at or above USD 110.00 per barrel on at least one trading day between 2026-08-24 and 2026-11-30. | TRUE if the ICE published settlement price for the Brent front-month contract is 110.00 USD per barrel or higher on any trading day in that range; otherwise FALSE. |
| KKR-20260822-08 | 50% | 2026-12-04 | economics | A document published in the Federal Register between 2026-08-24 and 2026-11-30 sets or amends a tariff-rate quota, duty rate or import allocation for beef entering the United States. | TRUE if a federalregister.gov query over that publication-date range returns at least one rule, proclamation or notice whose text sets or amends beef import duty or quota terms; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog carries an entry for CVE-2026-19478 with a dateAdded value between 2026-08-21 and 2026-10-2" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "CISA adds at least one vulnerability whose vendorProject field is Siemens to the Known Exploited Vulnerabilities catalog with a dateAdded va" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The USGS earthquake catalog records at least one magnitude 5.0 or greater event within 250 km of the 2026-08-21 M6.7 Aniso, Peru epicenter, " → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names a different subject than the statement — the claim is about Aniso, Peru, USGS and the resolution settles on FDSN, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "WHO reporting on the Democratic Republic of the Congo Ebola outbreak carries a cumulative death toll of 3,000 or more for a date between 202" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names only a venue or register (WHO, afro, disease, news) and no subject - the register is where to look, not what is claimed; name the subject inside it; the resolution names a different subject than the statement — the claim is about Congo, Democratic, Ebola, Republic and the resolution settles on AFRO, Disease, News, Outbreak. A row whose resolution checks a different fact can be scored correct while being wrong
- "At least one Hong Kong Alliance vigil organiser convicted on 2026-08-21 receives an unsuspended custodial sentence handed down between 2026-" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Swedish prosecutors file an indictment against at least one suspect over the 2026-08-21 Swedish school sword attack, with the filing occurri" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "UKMTO issues at least one incident advisory reporting an attack on a merchant vessel in the Strait of Hormuz, Gulf of Oman or Persian Gulf o" → REJECTED: the resolution names only a venue or register (UKMTO) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

839 issued all-time across 14 forecaster arms · 749 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 88 issued · 88 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 117 | 105 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 79 | 78 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*