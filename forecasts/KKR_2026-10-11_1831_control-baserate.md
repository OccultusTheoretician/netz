**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111831Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-33 | 69% | 2026-10-28 | military/conflict | Saudi or Saudi-led coalition aircraft carry out at least one airstrike on Houthi-held territory in Yemen between 2026-10-12 and 2026-10-25. | True if at least two of Reuters, AP, AFP, BBC or Al Jazeera report an airstrike attributed to Saudi or Saudi-led coalition forces hitting Houthi-held territory in Yemen on a date between 2026-10-12 and 2026-10-25. |
| KKR-20261011-34 | 69% | 2026-10-28 | military/conflict | At least one commercial vessel is struck, boarded or seized in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-12 and 2026-10-25. | True if UKMTO publishes at least one incident report of a vessel struck by a projectile or explosion, boarded, or seized in the Strait of Hormuz, Persian Gulf or Gulf of Oman, incident dated between 2026-10-12 and 2026-10-25. |
| KKR-20261011-35 | 58% | 2026-11-02 | economics/markets | ICE Brent crude front-month futures settle at or above 110.00 dollars per barrel on at least one trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 on the packet date. | True if the ICE Brent front-month futures settlement price is at or above 110.00 on any trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 on the packet date. |
| KKR-20261011-36 | 58% | 2026-11-18 | economics/markets | The 10-year US Treasury constant maturity yield (FRED series DGS10) is at or above 5.50 percent on at least one business day between 2026-10-13 and 2026-11-13. Reference: 5.24 percent on the packet date. | True if FRED series DGS10 shows a value of 5.50 or higher for any date between 2026-10-13 and 2026-11-13. Reference: 5.24 percent on the packet date. |
| KKR-20261011-37 | 42% | 2026-11-17 | cyber | CISA adds at least one Apple vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-12 and 2026-11-13. | True if the CISA KEV catalog lists at least one entry with vendorProject Apple and a dateAdded value between 2026-10-12 and 2026-11-13. |
| KKR-20261011-38 | 41% | 2026-12-11 | political | Democratic candidates win at least 218 seats in the US House of Representatives in the general election held on 2026-11-03. | True if the Associated Press has called at least 218 House races from the 2026-11-03 general election for Democratic candidates by the deadline. |
| KKR-20261011-39 | 41% | 2027-02-02 | political | The Verkhovna Rada adopts a resolution scheduling a Ukrainian presidential election, with the vote taken between 2026-10-12 and 2027-01-29. | True if, between 2026-10-12 and 2027-01-29, the Verkhovna Rada adopts a resolution scheduling a Ukrainian presidential election, per rada.gov.ua or reports by at least two of Reuters, AP, AFP or BBC. |
| KKR-20261011-40 | 43% | 2026-10-30 | disaster | At least one earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M 7.7 Panama earthquake (USGS event us6000u18k) between 2026-10-13 and 2026-10-27 UTC. | True if the USGS earthquake catalog lists at least one event of magnitude 6.0 or greater within 200 km of the epicenter of event us6000u18k, with origin time between 2026-10-13 and 2026-10-27 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "United States forces carry out at least one kinetic strike on Houthi targets inside Yemen between 2026-10-12 and 2026-11-08." → REJECTED: cited items name Iran, Islamic Republic of, Saudi Arabia; the claim is about United States, Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Hurricane Simon makes landfall in Mexico at major hurricane strength, with maximum sustained winds of at least 111 mph, between 2026-10-11 a" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a national hurricane center advisory, update | or | report states that simon made landfall in mex…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3896 issued all-time across 21 forecaster arms · 3082 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1380 issued · 1179 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1380 | 1179 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 320 | 287 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*