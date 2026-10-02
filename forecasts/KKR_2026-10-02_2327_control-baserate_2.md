**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022327Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-02_1519.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261002-30 | 32% | 2026-12-01 | cyber | CISA adds at least one of the Dell Container Storage Modules vulnerabilities disclosed on 2026-10-01, including CVE-2026-63688 and CVE-2026-63692, to its Known Exploited Vulnerabilities catalog between 2026-10-03 and 2026-11-27. | TRUE if the CISA KEV catalog shows a dateAdded value between 2026-10-03 and 2026-11-27 inclusive for any Dell Container Storage Modules CVE disclosed 2026-10-01, including CVE-2026-63688 and CVE-2026-63692; otherwise FALSE. |
| KKR-20261002-31 | 48% | 2026-12-11 | economics/markets | After the scheduled FOMC decisions of 2026-10-28 and 2026-12-09, the upper bound of the federal funds target range stands at or above 4.25 percent (Reference: 4.00 percent upper bound at packet seal). | TRUE if FRED series DFEDTARU shows a value of 4.25 or higher for 2026-12-10, reflecting the FOMC decisions of 2026-10-28 and 2026-12-09. Reference: 4.00 percent on the packet date. |
| KKR-20261002-32 | 48% | 2026-11-09 | economics/markets | The BLS Employment Situation release scheduled for 2026-11-06 reports an October 2026 unemployment rate of 4.3 percent or higher (Reference: 4.2 percent for September 2026, 4.175 unrounded, at packet seal). | TRUE if the BLS Employment Situation for October 2026, published 2026-11-06, shows a seasonally adjusted unemployment rate of 4.3 percent or higher (FRED UNRATE first release). Reference: 4.2 percent for September 2026. |
| KKR-20261002-33 | 64% | 2026-12-03 | military/conflict | Russia launches 500 or more drones and missiles combined against Ukraine within a single attack period, as counted by the Ukrainian Air Force, between 2026-10-03 and 2026-11-30. | TRUE if one Ukrainian Air Force summary covering a single attack period between 2026-10-03 and 2026-11-30 reports 500 or more drones and missiles launched combined, as relayed by Reuters or AP. |
| KKR-20261002-34 | 64% | 2027-01-05 | military/conflict | Ethiopian and Eritrean state armed forces clash directly, or the military of one state strikes targets inside the territory of the other, between 2026-10-03 and 2026-12-31. | TRUE if at least two of Reuters, AP and AFP report as fact, not as an allegation, a direct clash between Ethiopian and Eritrean state forces or a cross-border strike by either military between 2026-10-03 and 2026-12-31. |
| KKR-20261002-35 | 31% | 2026-11-17 | disaster | Cumulative deaths in the DRC Ebola outbreak declared on 2026-05-15 reach 5,000 or more in an official count published between 2026-10-03 and 2026-11-13 (Reference: 4,018 deaths at packet seal). | TRUE if a DRC Ministry of Health or WHO situation update published between 2026-10-03 and 2026-11-13 gives cumulative outbreak deaths of 5,000 or more. Reference: 4,018 deaths at packet seal. |
| KKR-20261002-36 | 29% | 2027-03-30 | crime/security | Former NSW police officer Beau Lamarre-Condon is convicted of murder on at least one count, by jury verdict or plea, in the NSW Supreme Court between 2026-10-03 and 2027-03-26. | TRUE if, between 2026-10-03 and 2027-03-26, Beau Lamarre-Condon is convicted in the NSW Supreme Court, by verdict or plea, of murdering Jesse Baird or Luke Davies, as reported by ABC News Australia or Reuters. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds at least one Fortinet vulnerability other than CVE-2026-104286 to its Known Exploited Vulnerabilities catalog between 2026-10-03 a" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104286 dateAdded 2026-10-01, before the claimed window 2026-10-03..2026-11-13; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The EIA weekly US average retail on-highway diesel price for the survey date 2026-11-16 is below 6.00 USD per gallon (Reference: 6.382 for t" → REJECTED: event window opens 2026-09-28, before this row is sealed (2026-10-02, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The French National Assembly adopts a motion of censure against the government of Prime Minister Sebastien Lecornu between 2026-10-03 and 20" → REJECTED: the resolution requires absolute, date, majority and the failure condition does not mention them — an outcome missing them satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements

## III. LEDGER STANDING

3254 issued all-time across 18 forecaster arms · 2712 open (391 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1165 issued · 1048 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1165 | 1048 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 361 | 211 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 161 | 156 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 243 | 226 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 71 | 71 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*