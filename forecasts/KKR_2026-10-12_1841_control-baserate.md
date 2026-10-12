**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121841Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-38 | 60% | 2026-10-19 | economics/markets | The BLS release scheduled for 2026-10-14 shows the September 2026 CPI-U all-items 12-month change at or above 3.7 percent. Reference: 3.4 percent for August 2026, the latest reading on the packet date. | TRUE if the BLS Consumer Price Index release of 2026-10-14 (FRED CPIAUCNS) shows September 2026 all-items CPI-U up 3.7 percent or more over 12 months, not seasonally adjusted. Reference: 3.4 percent for August 2026. |
| KKR-20261012-39 | 60% | 2026-11-16 | economics/markets | ICE Brent front-month crude futures (January 2027 contract) settle above 100.00 USD per barrel on 2026-11-13. Reference: front-month Brent at 106.95 on the packet date. | TRUE if the ICE Brent front-month futures settlement price for 2026-11-13 is above 100.00 USD per barrel. Reference: 106.95 on 2026-10-12. |
| KKR-20261012-40 | 45% | 2026-11-16 | cyber | CISA adds the critical SonicWall SMA 1000 vulnerability CVE-2026-102255 to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-13 and 2026-11-13. | TRUE if the CISA KEV catalog JSON lists CVE-2026-102255 with a dateAdded value between 2026-10-13 and 2026-11-13 inclusive. |
| KKR-20261012-41 | 45% | 2026-11-16 | cyber | CISA adds the maximum-severity GitLab code execution vulnerability CVE-2026-97229 to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-13 and 2026-11-13. | TRUE if the CISA KEV catalog JSON lists CVE-2026-97229 with a dateAdded value between 2026-10-13 and 2026-11-13 inclusive. |
| KKR-20261012-42 | 66% | 2026-10-29 | military/conflict | Ukrainian forces strike at least one oil refinery inside internationally recognized Russian territory between 2026-10-13 and 2026-10-26, with the strike publicly confirmed by the General Staff of the Armed Forces of Ukraine. | TRUE if the General Staff of the Armed Forces of Ukraine publicly confirms a Ukrainian strike on an oil refinery inside Russia carried out between 2026-10-13 and 2026-10-26, as reported by Reuters, AP or the Kyiv Independent. |
| KKR-20261012-43 | 42% | 2026-12-15 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | TRUE if Associated Press race calls as of 2026-12-15 show Democratic candidates winning 218 or more US House seats in the 2026-11-03 general election. |
| KKR-20261012-44 | 32% | 2027-01-19 | crime/security | A federal indictment, criminal information or criminal complaint naming Representative Ilhan Omar as a defendant is filed or unsealed in a US district court between 2026-10-13 and 2027-01-15. | TRUE if a federal court docket (PACER or CourtListener) or a Justice Department release shows a charging document naming Ilhan Omar as defendant filed or unsealed between 2026-10-13 and 2027-01-15. |
| KKR-20261012-45 | 44% | 2026-11-16 | disaster | At least one earthquake of magnitude 6.0 or greater occurs within 150 km of the epicenter of the M 7.7 Panama earthquake (USGS event us6000u18k) with origin time between 2026-10-13 and 2026-11-12 UTC. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater within 150 km of the us6000u18k epicenter with origin time between 2026-10-13 and 2026-11-12 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled meeting ending 2026-10-28. Reference: target range 3.75 to 4.00 percent on t" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The United States military carries out at least one strike on Houthi targets in Yemen between 2026-10-13 and 2026-11-02, publicly confirmed " → REJECTED: cited items name Saudi Arabia; the claim is about Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3979 issued all-time across 21 forecaster arms · 2951 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1407 issued · 1133 open · 242 resolved · 152 hits / 90 misses · **Brier 0.316** against its own base rate 62.8% (climatological 0.234) · **skill -0.354**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1407 | 1133 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 328 | 272 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*