**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-11 | 20% | 2026-09-21 | disaster_infrastructure | Between 2026-08-21 and 2026-09-18, the USGS catalog records an earthquake of magnitude 6.0 or greater within 150 km of the August 21, 2026 M6.7 Peru mainshock epicenter near Aniso, Peru. | Resolves YES if the USGS Earthquake Catalog lists an event of magnitude 6.0 or greater with an epicenter within 150 km of the M6.7 Peru mainshock, occurring between 2026-08-21 and 2026-09-18; resolves NO otherwise. |
| KKR-20260822-12 | 55% | 2026-09-22 | cyber | Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds an entry for CVE-2026-19478, the GitLab remote code execution flaw reported under active exploitation on 2026-08-21. | Resolves YES if the CISA KEV catalog (kev.cisa.gov or its published JSON feed) lists CVE-2026-19478 with a dateAdded value between 2026-08-21 and 2026-09-18; resolves NO if no such entry exists by the deadline. |
| KKR-20260822-13 | 30% | 2026-09-22 | cyber | Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds at least one entry for a Microsoft Entra ID product vulnerability, corresponding to the maximum-severity flaw Microsoft disclosed as under active exploitation on 2026-08-21. | Resolves YES if the CISA KEV catalog lists at least one CVE with vendorProject Microsoft and a product field containing Entra, with a dateAdded value between 2026-08-21 and 2026-09-18; resolves NO if no such entry exists by the deadline. |
| KKR-20260822-14 | 15% | 2026-09-22 | military_conflict | Between 2026-08-21 and 2026-09-18, United States military forces carry out a kinetic strike on a target inside Iranian sovereign territory, including territorial waters. | Resolves YES if the strike is corroborated under the two-independent-side standard used in this record (for example, both Iranian and Western or Gulf-state sources) reporting a U.S. strike on Iranian territory within the window; resolves NO otherwise. |
| KKR-20260822-15 | 25% | 2026-09-22 | crime_security | Between 2026-08-21 and 2026-09-18, Swedish police or prosecutors publicly classify the August 21, 2026 sword attack at a Swedish school as a terrorist offense under Swedish law. | Resolves YES if Polisen or the Swedish Prosecution Authority states, per reporting from BBC, Reuters, AP, TT, or a major Swedish outlet, that the attack is being investigated or charged as a terrorist offense under the Swedish Act on Criminal Responsibility for Terrorist Offences; resolves NO if authorities charge it solely as attempted murder, aggravated assault, or a similar non-terrorism offense, or make no such classification by the deadline. |
| KKR-20260822-16 | 45% | 2027-01-05 | political | Between 2026-08-21 and 2026-12-31, a Hong Kong court sentences Lee Cheuk-yan or Chow Hang-tung in the West Kowloon incitement-to-subversion case, and at least one of the two receives an immediate custodial term of 3 years or longer. | Resolves YES if Hong Kong court reporting (for example HKFP, RTHK, Reuters, AP, SCMP) confirms a sentencing decision for Lee Cheuk-yan or Chow Hang-tung between 2026-08-21 and 2026-12-31 in which at least one receives an immediate custodial term of 3 years or longer; resolves NO if sentencing occurs but neither meets that term, or the case has not reached sentencing by the window close. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

847 issued all-time across 14 forecaster arms · 757 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 85 issued · 84 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

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
| manual/fable-5/unattested | 72 | 72 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 85 | 84 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*