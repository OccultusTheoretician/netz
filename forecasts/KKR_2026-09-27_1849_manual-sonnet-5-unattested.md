**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271849Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-27_1517.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260927-42 | 58% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog will add at least one entry for a Citrix NetScaler product, with a date-added value between 2026-09-28 and 2026-10-11. | True if the CISA KEV catalog (cisa.gov/known-exploited-vulnerabilities-catalog) lists a NetScaler-related CVE with dateAdded between 2026-09-28 and 2026-10-11 inclusive; false otherwise. |
| KKR-20260927-43 | 30% | 2026-10-20 | cyber | Microsoft will document a resumed rollout or a replacement fix for the KB5002907 Office license-deactivation issue between 2026-09-28 and 2026-10-18. | True if Microsoft's Release Health dashboard or a support.microsoft.com KB article confirms KB5002907, or its direct successor patch, is fixed and redistributed inside the window; false otherwise. |
| KKR-20260927-44 | 27% | 2026-10-12 | economics/markets | The US 10-Year Treasury yield will close at or above 5.30 percent (Reference: 5.18 percent on 2026-09-27, per the packet) on at least one day between 2026-09-28 and 2026-10-09. | True if the Treasury daily par yield curve or FRED series DGS10 shows a close at or above 5.30 percent on any date in the window; false otherwise. |
| KKR-20260927-45 | 68% | 2026-10-12 | political | A lapse in federal appropriations will force at least one US federal department to furlough staff or suspend non-excepted operations between 2026-10-01 and 2026-10-08. | True if OMB, OPM, or two of Reuters, AP, and Politico report a funding lapse causing furloughs or suspended operations at a federal department starting in the window; false otherwise. |
| KKR-20260927-46 | 53% | 2026-11-05 | political | Vivek Ramaswamy will win the 2026 Ohio gubernatorial general election held on 2026-11-03. | True if the Ohio Secretary of State certified result or an AP race call names Ramaswamy the winner by the deadline; false if Acton wins or the race is uncalled. |
| KKR-20260927-47 | 90% | 2026-10-06 | political | No candidate will win an outright majority in Brazil's first-round presidential election on 2026-10-04, forcing an October 25 runoff. | True if Brazil's Tribunal Superior Eleitoral (TSE) results portal shows no candidate above 50 percent of valid votes and schedules the runoff; false if one candidate exceeds 50 percent. |
| KKR-20260927-48 | 55% | 2026-10-14 | crime/security | South African Police Service will announce at least one arrest connected to either of the two mass shootings reported on 2026-09-27 in Johannesburg and Cape Town, between 2026-09-28 and 2026-10-12. | True if SAPS, News24, or Reuters reports a named arrest tied to either shooting, dated inside the window; false otherwise. |
| KKR-20260927-49 | 45% | 2026-10-13 | disaster | USGS will catalog at least one aftershock of magnitude 5.0 or greater within 200 km of the 2026-09-26 M6.6 New Caledonia mainshock (event id us6000txpi), occurring between 2026-09-28 and 2026-10-11. | True if USGS ComCat lists a magnitude 5.0 or greater event within 200 km of the us6000txpi epicenter with an origin time inside the window; false otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 will close below 7,600 (Reference: 7,743.41 at the 26 Sep 2026 close, per the packet) on at least one trading day between 2026-0" → REJECTED: resolution offers alternative VENUES joined by 'or' (…major index provider | or | wire…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The United States and Iran will not publicly announce a signed or explicitly agreed arrangement reopening the Strait of Hormuz to normal com" → REJECTED: statement and resolution assert opposite directions - the statement claims an absence and the resolution resolves TRUE on the event occurring. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition

## III. LEDGER STANDING

2980 issued all-time across 17 forecaster arms · 2438 open (226 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 335 issued · 271 open · 59 resolved · 31 hits / 28 misses · **Brier 0.238** against its own base rate 52.5% (climatological 0.249) · **skill +0.047**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1056 | 939 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 129 | 124 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 210 | 193 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 335 | 271 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*