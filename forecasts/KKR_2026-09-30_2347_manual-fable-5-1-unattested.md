**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 302347Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-30_1517.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260930-11 | 22% | 2027-01-05 | military/conflict | United States forces carry out at least one kinetic strike on a target on Iranian land territory between 2026-10-01 and 2026-12-31. | True if the Pentagon, CENTCOM or the White House confirms, or both Reuters and AP report citing US officials, a US strike on Iranian land territory occurring between 2026-10-01 and 2026-12-31; otherwise false. |
| KKR-20260930-12 | 85% | 2026-11-03 | military/conflict | Ukrenergo imposes scheduled or emergency power outages on Kyiv city on at least one day between 2026-10-08 and 2026-10-31. | True if Ukrenergo announces scheduled or emergency outages applying to Kyiv city on any day between 2026-10-08 and 2026-10-31, as carried by at least two of Reuters, Kyiv Independent and Ukrinform; otherwise false. |
| KKR-20260930-13 | 33% | 2026-10-30 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting concluding 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date. | True if FRED series DFEDTARU reads 4.25 or higher for 2026-10-29; false if it reads 4.00 or lower. Reference: upper limit 4.00 percent on the packet date. |
| KKR-20260930-14 | 40% | 2026-11-03 | economics/markets | The 10-year Treasury constant maturity yield closes at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date. | True if FRED series DGS10 prints 5.50 or higher for any date between 2026-10-01 and 2026-10-30 inclusive; otherwise false. Reference: 5.27 percent on the packet date. |
| KKR-20260930-15 | 30% | 2026-11-03 | economics/markets | The ICE Brent December 2026 futures contract settles below 90.00 dollars a barrel on at least one trading day between 2026-10-01 and 2026-10-30. Reference: 99.12 on the packet date. | True if the ICE Brent December 2026 contract daily settlement is below 90.00 on any trading day between 2026-10-01 and 2026-10-30 inclusive; otherwise false. Reference: 99.12 on the packet date. |
| KKR-20260930-16 | 55% | 2026-12-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Cisco vulnerability whose product field contains SD-WAN with a date-added value between 2026-10-01 and 2026-11-30. | True if the CISA KEV catalog lists any Cisco entry with SD-WAN in the product field and a dateAdded value between 2026-10-01 and 2026-11-30 inclusive; otherwise false. |
| KKR-20260930-17 | 15% | 2026-12-15 | cyber | Between 2026-10-01 and 2026-12-11 CISA changes the known ransomware campaign use field to Known on the KEV catalog entry for Citrix NetScaler CVE-2026-88771 or CVE-2026-88772. | True if on 2026-12-15 the CISA KEV catalog entry for CVE-2026-88771 or CVE-2026-88772 shows knownRansomwareCampaignUse equal to Known, reflecting a change made between 2026-10-01 and 2026-12-11; false if both read Unknown. |
| KKR-20260930-18 | 15% | 2027-03-18 | crime/security | The Crown Prosecution Service authorises criminal charges against at least one individual or organisation over the Grenfell Tower fire between 2026-10-01 and 2027-03-15. | True if a CPS or Metropolitan Police statement dated between 2026-10-01 and 2027-03-15 announces authorised charges against any Grenfell suspect, as published on cps.gov.uk or carried by both BBC and Guardian; otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Branko Blanusa of the SDS finishes first in the election for President of Republika Srpska held on 2026-10-04, ahead of SNSD candidate Savo " → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Tropical cyclone 26W (Choi-wan), GDACS event 1001332, reaches typhoon strength of 65 knots or more between 2026-10-01 and 2026-10-10." → REJECTED: the resolution names a different subject than the statement — the claim is about Choi, GDACS, Tropical and the resolution settles on Center, Joint, Typhoon, Warning. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3115 issued all-time across 18 forecaster arms · 2573 open (298 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 232 issued · 215 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1106 | 989 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 345 | 195 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 148 | 143 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 232 | 215 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 48 | 48 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*