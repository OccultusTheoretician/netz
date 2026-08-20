**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 202336Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-20_1537.md · forecaster: manual/opus-5/unattested · 10 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260820-23 | 60% | 2026-09-29 | cyber | CISA adds at least one Zimbra Collaboration CVE to the Known Exploited Vulnerabilities catalog, with a date-added value between 2026-08-21 and 2026-09-25. | The CISA KEV catalog JSON contains an entry whose vendorProject or product field names Zimbra and whose dateAdded falls between 2026-08-21 and 2026-09-25 inclusive. |
| KKR-20260820-24 | 45% | 2026-11-24 | cyber | CISA adds at least one Citrix NetScaler ADC or NetScaler Gateway CVE to the Known Exploited Vulnerabilities catalog, with a date-added value between 2026-08-21 and 2026-11-20. | The CISA KEV catalog JSON contains an entry with vendorProject Citrix and a product field naming NetScaler, whose dateAdded falls between 2026-08-21 and 2026-11-20 inclusive. |
| KKR-20260820-25 | 55% | 2026-09-24 | military_conflict | A single Russian strike on Kyiv city occurring between 2026-08-21 and 2026-09-20 kills at least 10 people according to Ukrainian official figures. | At least two of Reuters, AP, BBC and Guardian report one strike event in Kyiv city inside the window carrying an official Ukrainian death toll of 10 or more. |
| KKR-20260820-26 | 22% | 2026-10-19 | military_conflict | United States forces conduct an officially acknowledged strike on targets inside Iranian territory between 2026-08-21 and 2026-10-15. | The Department of Defense or the White House publicly confirms US munitions struck targets inside Iran, the strike dated inside the window, carried by both Reuters and AP. |
| KKR-20260820-27 | 40% | 2026-11-03 | economic | ICE Brent front-month crude futures settle at or above 100.00 US dollars per barrel on at least one trading day between 2026-08-21 and 2026-10-30. | ICE published front-month Brent settlement data shows a settlement price of 100.00 or higher on at least one session dated inside the window. |
| KKR-20260820-28 | 38% | 2027-01-06 | economic | The 10-year Treasury constant maturity yield reaches 5.00 percent or higher on at least one business day between 2026-08-21 and 2026-12-31. | FRED series DGS10 carries a value of 5.00 or greater on at least one observation date inside the window. |
| KKR-20260820-29 | 75% | 2026-09-23 | disaster_infrastructure | USGS catalogs an earthquake of magnitude 6.0 or greater within 300 km of the 2026-08-20 Ende, Indonesia M7.7 epicenter, with origin time between 2026-08-21 and 2026-09-20. | A USGS ComCat query for magnitude 6.0 or greater, radius 300 km from the Ende mainshock epicenter, across the stated window, returns one or more events. |
| KKR-20260820-30 | 12% | 2026-12-18 | political | The Verkhovna Rada or Ukraine's Central Election Commission adopts an act naming a polling date for a nationwide presidential election, between 2026-08-21 and 2026-12-15. | At least two of Reuters, AP and BBC report adoption of an act or resolution naming a specific polling date for a Ukrainian presidential election inside the window. |
| KKR-20260820-31 | 30% | 2027-01-05 | crime_security | A Chinese court sentences a named former Evergrande Group executive other than Hui Ka Yan to ten years imprisonment or more, between 2026-08-21 and 2026-12-31. | At least two of Reuters, AP, BBC and South China Morning Post report a Chinese court imposing a term of ten years or more on a named former Evergrande executive. |
| KKR-20260820-32 | 33% | 2027-01-05 | economic | The Digital Asset Market Clarity Act becomes public law, with enactment dated between 2026-08-21 and 2026-12-31. | The Congress.gov actions list for the Digital Asset Market Clarity Act shows a Became Public Law entry dated inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

827 issued all-time across 14 forecaster arms · 737 open (14 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 85 issued · 85 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 113 | 101 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 67 | 67 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 85 | 85 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 77 | 76 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*