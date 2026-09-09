**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091806Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-09_1530.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260909-52 | 60% | 2026-09-18 | economic | The FOMC leaves the federal funds target range unchanged at 3.50 to 3.75 percent at its scheduled September 15-16, 2026 meeting. Reference: target range 3.50 to 3.75 percent at seal. | TRUE if the FOMC policy statement published 2026-09-16 on federalreserve.gov keeps the target range at 3.50 to 3.75 percent. |
| KKR-20260909-53 | 45% | 2026-10-13 | economic | ICE Brent front-month futures post a settlement at or above 110.00 USD per barrel on at least one trading day between 2026-09-10 and 2026-10-09. Reference: Brent 101.13 on the packet date. | TRUE if the ICE published settlement price for the front-month Brent contract reaches 110.00 or higher on any trading day inside the window. |
| KKR-20260909-54 | 70% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium CVE with a date-added value between 2026-09-09 and 2026-10-09. | TRUE if the KEV JSON feed on cisa.gov carries an entry with vendorProject Google and a dateAdded value inside that range. |
| KKR-20260909-55 | 25% | 2027-01-05 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one SAP CVE with a date-added value between 2026-09-09 and 2026-12-31. | TRUE if the KEV JSON feed on cisa.gov carries an entry with vendorProject SAP and a dateAdded value inside that range. |
| KKR-20260909-56 | 55% | 2027-02-04 | political | A Federal Register document from the Census Bureau or the Department of Commerce proposing 2030 Census content on citizenship or on race and ethnicity categories publishes between 2026-09-10 and 2027-01-31. | TRUE if federalregister.gov returns at least one document from that agency, on that subject, with a publication date inside the window. |
| KKR-20260909-57 | 20% | 2026-12-04 | military_conflict | Between 2026-09-10 and 2026-11-30, the Nigerian federal government or its armed forces publicly confirm a ceasefire arrangement with Boko Haram. | TRUE if a named Nigerian government or military spokesperson confirms such an arrangement on the record, reported by two of Reuters, AP, AFP, BBC, Al Jazeera. |
| KKR-20260909-58 | 55% | 2026-11-03 | economic | The 10-year Treasury constant maturity rate closes at or above 5.00 percent on at least one business day between 2026-09-10 and 2026-10-30. Reference: 4.85 percent on the packet date. | TRUE if FRED series DGS10 records a value of 5.00 or higher on any business day inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-10 and 2026-09-24, US Central Command or the Iranian IRGC publicly announces at least one new attack on a vessel in the Stra" → REJECTED: resolution offers alternative VENUES joined by 'or' (…centcom release | or | irgc…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-09 and 2026-10-16, the UK government announces the closure or suspension of operations at its Consulate General in Jerusalem" → REJECTED: the resolution names a different subject than the statement — the claim is about Consulate, General, Jerusalem, UK and the resolution settles on FCDO, Hansard. A row whose resolution checks a different fact can be scored correct while being wrong
- "USGS records at least one earthquake of magnitude 7.0 or greater anywhere on Earth with an origin time between 2026-09-10 and 2026-10-09." → REJECTED: the resolution names a different subject than the statement — the claim is about Earth, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1801 issued all-time across 16 forecaster arms · 1465 open (47 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 213 issued · 207 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 560 | 522 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 240 | 111 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*