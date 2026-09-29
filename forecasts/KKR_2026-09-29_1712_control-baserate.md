**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291712Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-29_1517.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260929-20 | 32% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one entry whose vendorProject or product field names Kiteworks, with a dateAdded value between 2026-09-29 and 2026-11-13 inclusive. | TRUE if the CISA KEV JSON feed contains an entry naming Kiteworks in vendorProject or product with dateAdded from 2026-09-29 through 2026-11-13; FALSE otherwise. |
| KKR-20260929-21 | 29% | 2026-10-06 | crime/security | The State of Tennessee carries out the scheduled execution of Christa Gail Pike on 2026-09-30, the date set by the Tennessee Supreme Court. | TRUE if the Tennessee Department of Correction confirms Pike was executed on 2026-09-30 and the Death Penalty Information Center execution database records it; FALSE if stayed, delayed past that date, or commuted. |
| KKR-20260929-22 | 29% | 2027-01-05 | crime/security | Between 2026-09-30 and 2026-12-31, the UK Crown Prosecution Service or Counter Terrorism Policing publicly announces that at least one person arrested in the RAF Fairford suspected-plot investigation has been charged under the Terrorism Act 2000, the Terrorism Act 2006, or the National Security Act 2023. | TRUE if a CPS or Counter Terrorism Policing statement, or a court listing, confirms a Terrorism Act or National Security Act 2023 charge against an RAF Fairford suspect dated within the window; FALSE otherwise. |
| KKR-20260929-23 | 64% | 2026-12-02 | military/conflict | Between 2026-10-01 and 2026-11-30, the United States government and the Iranian government each publicly confirm a signed or jointly announced agreement (memorandum, ceasefire, or framework) that provides for reopening the Strait of Hormuz to commercial shipping. | TRUE if within the window the White House or State Department and the Iranian Foreign Ministry or state media (IRNA) each confirm the same agreement providing for Hormuz reopening; a unilateral proposal or talks alone do not count. |
| KKR-20260929-24 | 64% | 2026-11-06 | military/conflict | Between 2026-10-01 and 2026-10-31, the UK Maritime Trade Operations (UKMTO) centre publishes at least one incident or warning advisory reporting a merchant vessel attacked or struck by a projectile in the Red Sea, Bab el-Mandeb, or Gulf of Aden. | TRUE if the UKMTO public advisories list at least one incident dated within the window describing an attack on or projectile strike against a merchant vessel in the Red Sea, Bab el-Mandeb, or Gulf of Aden; FALSE otherwise. |
| KKR-20260929-25 | 48% | 2026-11-04 | economics/markets | The ICE Brent crude front-month futures contract settles at or below 85.00 US dollars per barrel on at least one trading day between 2026-10-01 and 2026-10-30. Reference: 97.04 on the packet date, after an 8.97 percent one-day fall (section V). | TRUE if any official ICE Brent front-month settlement price dated 2026-10-01 through 2026-10-30 is at or below 85.00; FALSE if every settlement in the window is above 85.00. |
| KKR-20260929-26 | 48% | 2026-11-04 | economics/markets | The 10-year US Treasury constant maturity yield (FRED series DGS10) prints at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.26 percent on the packet date (section V). | TRUE if any DGS10 observation dated 2026-10-01 through 2026-10-30 is greater than or equal to 5.50; FALSE if all observations in the window are below 5.50. |
| KKR-20260929-27 | 39% | 2027-01-05 | political | The French National Assembly adopts a motion de censure against the government in a vote held between 2026-10-01 and 2026-12-31, reaching the 289-vote absolute majority required under Article 49 of the Constitution. | TRUE if the Assemblee nationale official vote record (scrutin) shows a motion de censure adopted with at least 289 votes on a date within the window; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog adds at least one further CVE with vendorProject Apple (any CVE other than CVE-2026-86950) " → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-86950 dateAdded 2026-09-29, before the claimed window 2026-10-01..2026-10-31; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Oura files a final IPO prospectus (SEC form type 424B4 or 424B1) on EDGAR between 2026-09-30 and 2026-12-31, or its shares begin regular-way" → REJECTED: resolution offers alternative VENUES joined by 'or' (…424b4 | or | 424b1…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3067 issued all-time across 17 forecaster arms · 2525 open (260 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1091 issued · 974 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1091 | 974 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 340 | 190 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 143 | 138 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 224 | 207 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*