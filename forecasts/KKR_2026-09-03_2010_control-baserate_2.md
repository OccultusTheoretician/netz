**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032010Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-03_1518.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-60 | 21% | 2026-09-22 | economics/markets | The Bank of Japan raises its short-term policy interest rate at the Monetary Policy Meeting concluding 2026-09-18, to a level above the rate in effect on 2026-09-03. | The Statement on Monetary Policy published on boj.or.jp for the MPM concluding 2026-09-18 sets the uncollateralized overnight call rate guideline above the level in effect on 2026-09-03. |
| KKR-20260903-61 | 21% | 2026-10-09 | economics/markets | Brent crude trades above 110.00 US dollars per barrel on at least one trading day between 2026-09-04 and 2026-10-02. Reference: 96.70 on the packet date. | The FRED series DCOILBRENTEU (EIA Brent Europe spot) reports a daily value strictly above 110.00 for at least one observation dated 2026-09-04 through 2026-10-02 inclusive. Reference: 96.70 on the packet date. |
| KKR-20260903-62 | 30% | 2026-10-02 | cyber | CISA adds at least one CVE whose KEV vendorProject or product field names Elementor to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-03 and 2026-09-30. | The CISA KEV JSON feed (cisa.gov known-exploited-vulnerabilities.json) contains an entry whose vendorProject or product field includes Elementor and whose dateAdded is from 2026-09-03 through 2026-09-30 inclusive. |
| KKR-20260903-63 | 35% | 2026-12-22 | political | The US House Committee on Oversight and Government Reform votes to approve a report or resolution recommending that Leon Black be held in contempt of Congress between 2026-09-03 and 2026-12-18. | The committee website (oversight.house.gov) or Congress.gov records a committee vote approving a contempt of Congress report or resolution naming Leon Black, held on a date from 2026-09-03 through 2026-12-18 inclusive. |
| KKR-20260903-64 | 49% | 2026-10-06 | military/conflict | The US Department of Defense announces the death of at least one US service member from hostile action in the CENTCOM area of responsibility, with a date of death between 2026-09-04 and 2026-10-01. | A casualty release on defense.gov identifies at least one US service member whose death is attributed to hostile action or enemy attack in the CENTCOM area of responsibility, with date of death 2026-09-04 through 2026-10-01 inclusive. |
| KKR-20260903-65 | 36% | 2026-10-07 | disaster | The USGS catalog records an earthquake of magnitude 6.0 or greater with epicenter within 300 km of the 2026-09-03 M6.3 event 84 km SSW of Nikolski, Alaska (us7000tdvt), with origin time between 2026-09-04 and 2026-10-03. | The USGS earthquake catalog (earthquake.usgs.gov) lists an event with magnitude 6.0 or greater, epicenter within 300 km of event us7000tdvt, and origin time from 2026-09-04 00:00 UTC through 2026-10-03 23:59 UTC. |
| KKR-20260903-66 | 36% | 2027-01-06 | disaster | The NOAA CPC weekly Nino 3.4 sea surface temperature anomaly reaches at least +2.0 degrees C for at least one week dated between 2026-09-07 and 2026-12-28. | The NOAA CPC weekly SST anomaly table (cpc.ncep.noaa.gov/data/indices/wksst9120.for) shows a Nino 3.4 anomaly of 2.0 or higher for any week whose listed date falls from 2026-09-07 through 2026-12-28 inclusive. |
| KKR-20260903-67 | 36% | 2026-11-04 | crime/security | UK Home Office figures record 900 or more people arriving in the UK by small boat on at least one single day between 2026-09-04 and 2026-10-31. | The Home Office small boat arrivals dataset on gov.uk (migrants detected crossing the English Channel in small boats) shows a daily arrivals figure of 900 or more for at least one date from 2026-09-04 through 2026-10-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Open Market Committee leaves the federal funds target range unchanged at its scheduled meeting concluding 2026-09-16, keeping th" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The head of the Security Service of Ukraine (SBU), the Defence Intelligence (HUR), or the Foreign Intelligence Service (SZRU) is removed fro" → REJECTED: resolution offers alternative VENUES joined by 'or' (…decree published at president.gov.ua | or | a verkhovna rada…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1387 issued all-time across 15 forecaster arms · 1122 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 384 issued · 356 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 384 | 356 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
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
| manual/opus-5/unattested | 174 | 168 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 158 | 137 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*