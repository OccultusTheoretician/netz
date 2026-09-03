**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032010Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-03_1518.md · forecaster: manual/fable-5/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-37 | 92% | 2026-10-06 | military/conflict | Between 2026-09-04 and 2026-10-02, Ukrainian forces strike at least one target inside internationally recognized Russian territory 200 km or more from the Russia-Ukraine border, acknowledged by both a Russian official source and a Ukrainian official or military-intelligence source. | Resolves TRUE if a strike meeting the statement, occurring in the window, is acknowledged by at least one Russian official source (MoD or regional governor) and one Ukrainian official source; otherwise FALSE. |
| KKR-20260903-38 | 65% | 2026-10-07 | military/conflict | Between 2026-09-04 and 2026-10-04, the government or state news agency of Qatar (QNA) or Bahrain (BNA) confirms an Iranian missile or drone striking, or being intercepted over, its national territory. | Resolves TRUE on official Qatari or Bahraini government or state-agency confirmation of an Iranian projectile striking or intercepted over its territory within the window, corroborated by at least one international wire service; otherwise FALSE. |
| KKR-20260903-39 | 55% | 2026-11-04 | political | Between 2026-09-04 and 2026-10-31, a decree published on the official website of the President of Ukraine removes the serving head of the SBU or the serving head of the GUR from that post. | Resolves TRUE if a presidential decree dated within the window and published at president.gov.ua removes the incumbent SBU chief or GUR chief; reassignment to another post counts as removal; otherwise FALSE. |
| KKR-20260903-40 | 72% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures record a daily settlement at or above 100.00 USD per barrel on at least one trading day between 2026-09-04 and 2026-10-30. Reference: Brent 96.70 at packet seal on 2026-09-03. | Resolves TRUE if any official ICE Brent front-month daily settlement between 2026-09-04 and 2026-10-30 is at or above 100.00 USD; otherwise FALSE. |
| KKR-20260903-41 | 85% | 2026-09-21 | economics/markets | The Federal Open Market Committee leaves the federal funds target range unchanged at its scheduled September 2026 meeting, per the FOMC statement posted at federalreserve.gov. | Resolves TRUE if the September 2026 FOMC statement maintains the pre-meeting federal funds target range with no change; any increase or cut resolves FALSE. |
| KKR-20260903-42 | 40% | 2026-10-06 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry whose vendor, product, or vulnerability name field contains Elementor, with a dateAdded value between 2026-09-03 and 2026-10-02 inclusive. | Resolves TRUE if the public CISA KEV JSON feed contains an entry naming Elementor with a dateAdded value between 2026-09-03 and 2026-10-02 inclusive; otherwise FALSE. |
| KKR-20260903-43 | 18% | 2026-12-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry whose vendor or product field names CrowdStrike, with a dateAdded value between 2026-09-04 and 2026-11-30 inclusive. | Resolves TRUE if the public CISA KEV JSON feed contains an entry with vendor or product naming CrowdStrike and a dateAdded value between 2026-09-04 and 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20260903-44 | 30% | 2026-12-08 | disaster | Between 2026-09-04 and 2026-12-04, the USGS earthquake catalog records at least one earthquake of magnitude 6.0 or greater with an epicenter within 300 km of USGS event us7000tdvt, the 2026-09-03 M6.3 near Nikolski, Alaska. | Resolves TRUE if a USGS ComCat query returns any event of magnitude 6.0 or greater within 300 km of the us7000tdvt epicenter with origin time inside the window; catalog values as of the deadline govern. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "In the United States midterm elections held 2026-11-03, Democrats win a majority of US House seats, with the Associated Press calling at lea" → REJECTED: cited items name Venezuela, Bolivarian Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The UK Home Office daily dataset of migrants detected crossing the English Channel in small boats records at least one calendar day between " → REJECTED: the resolution names a different subject than the statement — the claim is about Channel, English, Home, Office and the resolution settles on Resolves. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1364 issued all-time across 15 forecaster arms · 1099 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 153 issued · 151 open · 2 resolved · 2 hits / 0 misses · **Brier 0.225** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 370 | 342 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 200 | 112 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 15 | 15 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 153 | 151 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 158 | 137 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*