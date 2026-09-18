**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182321Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-18_1518.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260918-46 | 20% | 2026-10-20 | military/conflict | The United States military conducts a direct kinetic strike (missile, air, or naval gunfire) against Houthi forces or positions at or near the Bab el-Mandeb strait between 2026-09-25 and 2026-10-16. | TRUE if Reuters, AP, or BBC report a confirmed US strike on Houthi targets at or near Bab el-Mandeb in the stated window; checked 2026-10-20 using wire-service and CENTCOM reporting. |
| KKR-20260918-47 | 25% | 2026-10-20 | economics/markets | WTI crude oil (NYMEX front-month futures) settles at or above 100.00 USD per barrel on any trading day between 2026-09-21 and 2026-10-16. Reference: 96.92 on the packet date, 2026-09-18. | TRUE if CME/NYMEX front-month WTI settlement data show a close at or above 100.00 USD/bbl on any session between 2026-09-21 and 2026-10-16; checked 2026-10-20 against exchange records. |
| KKR-20260918-48 | 22% | 2026-10-20 | economics/markets | The Nasdaq index closes at or above 27717.70, five percent above the packet reference, on any trading day between 2026-09-21 and 2026-10-16. Reference: 26397.81 on the packet date, 2026-09-18. | TRUE if Nasdaq closing data show a close at or above 27717.70 on any session between 2026-09-21 and 2026-10-16; checked 2026-10-20 against exchange or major financial-data-provider records. |
| KKR-20260918-49 | 12% | 2026-11-10 | cyber | CISA adds a CVE for the Microsoft Azure AI Foundry flaw described in the September 18, 2026 report, CVSS 10.0 and already patched by Microsoft, to its Known Exploited Vulnerabilities catalog between 2026-09-25 and 2026-11-06. | TRUE if the CISA KEV catalog lists an Azure AI Foundry CVE with a dateAdded value between 2026-09-25 and 2026-11-06; checked 2026-11-10 against cisa.gov/known-exploited-vulnerabilities-catalog. |
| KKR-20260918-50 | 45% | 2026-10-06 | disaster | USGS records at least one aftershock of magnitude 5.0 or greater within 300 km of the M6.5 earthquake 169 km west of Nikolski, Alaska, event us7000ti1p, between 2026-09-18 and 2026-10-02. | TRUE if the USGS earthquake catalog lists a magnitude 5.0-plus event within 300 km of event us7000ti1p between 2026-09-18 and 2026-10-02; checked 2026-10-06 via earthquake.usgs.gov. |
| KKR-20260918-51 | 8% | 2026-10-06 | disaster | GDACS raises its alert level above Green, to Orange or Red, for the Italy forest fire logged as event 1032034, already in its 59th day of coverage as of 2026-09-18, between 2026-09-18 and 2026-10-02. | TRUE if the GDACS report page for event 1032034 shows an Orange or Red alert level at any point between 2026-09-18 and 2026-10-02; checked 2026-10-06 via gdacs.org. |
| KKR-20260918-52 | 55% | 2026-10-06 | crime/security | Pakistani government, police, or military (ISPR) officials publicly name a specific militant organization as responsible for the September 18, 2026 blast at a police-complex mosque in Pakistan, between 2026-09-18 and 2026-10-02. | TRUE if Reuters, AP, Al Jazeera, or Dawn quote a Pakistani official naming a specific militant group for the blast between 2026-09-18 and 2026-10-02; checked 2026-10-06. |
| KKR-20260918-53 | 55% | 2026-11-10 | political | Republicans retain majority control of the U.S. Senate after the November 3, 2026 election. | TRUE if Republicans hold 51 or more Senate seats, or 50 seats with the Vice President breaking ties, per AP or major-network calls after the November 3, 2026 election; checked 2026-11-10. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Democrats win a majority of seats in the U.S. House of Representatives in the November 3, 2026 election, ending Republican control of the ch" → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

2492 issued all-time across 16 forecaster arms · 2026 open (103 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 270 issued · 222 open · 43 resolved · 21 hits / 22 misses · **Brier 0.207** against its own base rate 48.8% (climatological 0.250) · **skill +0.172**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 850 | 765 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 293 | 143 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 89 | 84 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 136 | 126 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 293 | 276 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 270 | 222 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*