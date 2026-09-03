**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022306Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-02_1520.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-57 | 35% | 2026-10-02 | economic | WTI crude oil, NYMEX front-month contract, settles at or above 100.00 USD per barrel on any trading day between 2026-09-03 and 2026-09-30. Reference: 90.59 USD per barrel on the packet date, 2026-09-02. | TRUE if CME/NYMEX settlement data or EIA daily spot price shows WTI at or above 100.00 USD per barrel on any date in the window; FALSE if no such settlement occurs. |
| KKR-20260902-58 | 28% | 2026-09-28 | economic | The 10-year US Treasury note yield closes at or above 5.00 percent on any trading day between 2026-09-03 and 2026-09-25. Reference: 4.80 percent on the packet date, 2026-09-02. | TRUE if the Treasury.gov daily par yield curve or FRED series DGS10 records a 10-year close at or above 5.00 percent on any date in the window; FALSE otherwise. |
| KKR-20260902-59 | 60% | 2026-09-28 | cyber | CISA adds a SonicWall SMA1000 vulnerability tied to the zero-days reported as actively exploited on 2026-09-02 to the Known Exploited Vulnerabilities catalog, with dateAdded between 2026-09-03 and 2026-09-23. | TRUE if the CISA KEV catalog lists a SonicWall SMA1000 CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline. |
| KKR-20260902-60 | 20% | 2026-09-28 | cyber | CISA adds a GeoNetwork remote-code-execution vulnerability, the unauthenticated RCE chain reported affecting government geoportal backends on 2026-09-02, to the KEV catalog, with dateAdded between 2026-09-03 and 2026-09-23. | TRUE if the CISA KEV catalog lists a GeoNetwork-related CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline. |
| KKR-20260902-61 | 65% | 2026-10-26 | crime_security | [withheld] Fourth District Court sets a specific trial start date for Tyler Robinson, the man charged with murdering Charlie Kirk, at the scheduled October 23, 2026 hearing. | TRUE if [withheld] Fourth District Court records or a wire service confirm a trial start date was set at the October 23, 2026 hearing; FALSE if the hearing is postponed or no date is set. |
| KKR-20260902-62 | 55% | 2026-09-28 | disaster_infrastructure | Nepal's National Disaster Risk Reduction and Management Authority reports a confirmed death toll of at least 1,500 from the August-September 2026 Nepal-Tibet floods, reported between 2026-09-03 and 2026-09-23. | TRUE if NDRRMA, Nepal's Home Ministry, or two independent wire services report a confirmed death toll of 1,500 or more within the window; FALSE if the reported toll stays below 1,500 throughout. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Commercial oil tanker transits through the Strait of Hormuz fall to a publicly reported near-total halt for at least 72 continuous hours at " → REJECTED: cited items name Bahrain, Iran, Islamic Republic of, Jordan; the claim is about Senegal — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The United States and Iran publicly announce a ceasefire, truce, or formal cessation of hostilities covering the ongoing conflict, announced" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ry issues a statement using ceasefire, truce, | or | cessation-of-hostilities language, confirmed …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The International Criminal Court Office of the Prosecutor publicly confirms opening a preliminary examination or investigation connected to " → REJECTED: resolution offers alternative VENUES joined by 'or' (…tatement confirming a preliminary examination | or | investigation naming the sirik strike, report…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1301 issued all-time across 14 forecaster arms · 1036 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 152 issued · 131 open · 21 resolved · 10 hits / 11 misses · **Brier 0.214** against its own base rate 47.6% (climatological 0.249) · **skill +0.141** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 344 | 316 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 192 | 104 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 152 | 131 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*