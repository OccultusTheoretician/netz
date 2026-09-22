**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221748Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-22_1518.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260922-42 | 42% | 2026-11-17 | cyber | The Broadcom VMware VeloCloud Orchestrator vulnerability reported as CVSS 10.0 and actively exploited via certificate-based authentication bypass is added to the CISA Known Exploited Vulnerabilities catalog with a Date Added value between 2026-09-22 and 2026-11-13. | True if the CISA KEV catalog carries an entry for a VeloCloud Orchestrator certificate-based authentication bypass or closely matching actively-exploited flaw with a Date Added value in the stated window; false if no such entry exists by the deadline. |
| KKR-20260922-43 | 15% | 2026-11-24 | disaster | GDACS wildfire event 1032333 in Indonesia, at Green alert level and in its 63rd day of coverage as of 22 Sep 2026, is escalated by GDACS to Orange or Red alert level at any point between 2026-09-22 and 2026-11-20. | True if the GDACS event report for eventid 1032333 shows an Orange or Red alert level at any point in the window; false if the event remains Green or is closed and archived at Green through window close. |
| KKR-20260922-44 | 12% | 2026-12-22 | economic | Brent crude oil settles at or above 130.00 USD per barrel on any trading day between 2026-09-23 and 2026-12-18. Reference: 100.03 USD per barrel on the packet date, 22 Sep 2026. | True if Reuters, Bloomberg, or ICE exchange settlement data report a Brent front-month settlement price at or above 130.00 USD per barrel on any trading day in the window; false otherwise. |
| KKR-20260922-45 | 38% | 2026-12-03 | economic | The 10-year US Treasury note yield closes at or below 4.55 percent on any trading day between 2026-09-23 and 2026-11-30. Reference: 4.96 percent on the packet date, 22 Sep 2026. | True if the Treasury daily par yield curve or the FRED series DGS10 shows a 10-year close at or below 4.55 percent on any date in the window; false otherwise. |
| KKR-20260922-46 | 22% | 2026-10-26 | military_conflict | A mining, seizure, boarding, or attack on a commercial vessel transiting the Strait of Hormuz is reported between 2026-09-23 and 2026-10-21. | True if two or more of Reuters, AP, S&P Global Platts, or Lloyds List report a mining, seizure, boarding, or attack on a commercial vessel transiting the Strait of Hormuz within the window; false otherwise. |
| KKR-20260922-47 | 17% | 2026-11-10 | political | Russia and Ukraine both publicly confirm an active moratorium on strikes against energy infrastructure, sustained for at least 5 consecutive days, at some point between 2026-09-23 and 2026-11-06. | True if statements from both the Russian and Ukrainian governments or their authorized spokespeople, reported by Reuters or AP, confirm an energy-infrastructure strike moratorium holding for 5 or more consecutive days within the window; false otherwise. |
| KKR-20260922-48 | 55% | 2026-11-10 | crime_security | The armed group responsible for the 15 deaths in the Far North Cameroon raid conducts a further attack on a populated locality in Far North Region, Cameroon, between 2026-09-23 and 2026-11-06. | True if two or more of Reuters, AP, or Al Jazeera report a further attack by the same or an affiliated armed group on a populated locality in Far North Region within the window; false otherwise. |
| KKR-20260922-49 | 58% | 2027-02-03 | crime_security | OpenAI or Sam Altman files a responsive motion, such as dismissal or transfer, in the British Columbia lawsuit over the Tumbler Ridge school shooting, docketed between 2026-09-23 and 2027-01-29. | True if the British Columbia Supreme Court docket for this case shows a filed responsive motion from either defendant within the window; false otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Republicans hold a majority of seats in the US House of Representatives as called by the Associated Press following the 2026-11-03 general e" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

2705 issued all-time across 16 forecaster arms · 2239 open (193 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 299 issued · 251 open · 43 resolved · 21 hits / 22 misses · **Brier 0.207** against its own base rate 48.8% (climatological 0.250) · **skill +0.172**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 934 | 849 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 324 | 174 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 103 | 98 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 164 | 154 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 320 | 303 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 299 | 251 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*