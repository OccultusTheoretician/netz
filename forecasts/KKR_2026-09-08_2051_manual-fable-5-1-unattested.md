**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082051Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: manual/fable-5.1/unattested · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-26 | 70% | 2026-10-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-75650, the Adobe Commerce and Magento Open Source StyleSmuggler flaw patched 2026-09-07, with a dateAdded value between 2026-09-08 and 2026-09-29. | TRUE if the CISA KEV JSON feed at the deadline contains an entry with cveID CVE-2026-75650 and dateAdded between 2026-09-08 and 2026-09-29 inclusive; FALSE otherwise. |
| KKR-20260908-27 | 22% | 2026-11-10 | cyber | The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-44756 (SAP Kernel OVERPASS) or CVE-2026-58240 (SAP NetWeaver Message Server S4GET) with a dateAdded value between 2026-09-08 and 2026-11-06. | TRUE if the CISA KEV JSON feed at the deadline contains an entry for CVE-2026-44756 or CVE-2026-58240 with dateAdded between 2026-09-08 and 2026-11-06 inclusive; FALSE otherwise. |
| KKR-20260908-28 | 45% | 2026-10-14 | economic | The FRED series DCOILWTICO (WTI Cushing spot, dollars per barrel) prints at least one observation at or above 100.00 dated between 2026-09-09 and 2026-10-09. Reference: WTI 92.66 on the packet date per Section V. | TRUE if any FRED DCOILWTICO observation dated 2026-09-09 through 2026-10-09 inclusive is at or above 100.00 as published at the deadline; FALSE if all such observations are below 100.00. |
| KKR-20260908-29 | 82% | 2026-10-02 | political | Between 2026-09-08 and 2026-09-30, the Russian Ministry of Foreign Affairs announces that at least one Hungarian diplomat is expelled from Russia or declared persona non grata, following the Hungarian expulsion of 10 Russian diplomats reported 2026-09-08. | TRUE if a Russian MFA statement dated 2026-09-08 through 2026-09-30 announces expulsion or persona non grata status for at least one Hungarian diplomat, and Reuters or AFP reports it; FALSE otherwise. |
| KKR-20260908-30 | 50% | 2026-12-03 | crime_security | Between 2026-09-09 and 2026-11-30, French authorities announce at least one arrest or criminal charge of a suspect in the theft of Renoir paintings from the Musee Renoir in Cagnes-sur-Mer reported on 2026-09-08. | TRUE if a French prosecution office or French police announce at least one arrest or charge in the Musee Renoir Cagnes-sur-Mer theft on a date 2026-09-09 through 2026-11-30, reported by AFP or Le Monde; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "In the Swedish general election held 2026-09-13, the Social Democrats, Left Party, Green Party and Centre Party together win at least 175 of" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "In the Mecklenburg-Vorpommern state election held 2026-09-20, the AfD receives the largest share of party list votes of any party in the off" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Between 2026-09-09 and 2026-09-23, Saudi or Saudi-led coalition aircraft strike targets inside Sanaa city, with the strikes announced by the" → REJECTED: resolution offers alternative VENUES joined by 'or' (…saudi | or | coalition official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-09 and 2026-10-31, the United States government and the government of Iran each publicly confirm a ceasefire, truce or halt " → REJECTED: resolution offers alternative VENUES joined by 'or' (…l us statement (white house, state department | or | pentagon) and an official iranian statement (…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The USGS catalog records at least one earthquake of magnitude 6.0 or greater with epicenter between 50.0N and 55.0N and between 175.0W and 1" → REJECTED: the resolution names a different subject than the statement — the claim is about Aleutians, Nikolski, USGS, us7000tdvt and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1708 issued all-time across 16 forecaster arms · 1443 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 50 issued · 50 open · nothing resolved yet — this arm earns a score at its first resolution.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 517 | 489 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 235 | 147 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 192 | 171 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*