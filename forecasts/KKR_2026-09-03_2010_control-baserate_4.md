**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032010Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-03_1518.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-76 | 49% | 2026-10-08 | military_conflict | Between 2026-09-04 and 2026-10-04, at least one additional munition impact on the sovereign territory of Kuwait, Bahrain, Qatar, Saudi Arabia, or the United Arab Emirates is publicly attributed to Iran or Iran-aligned forces by the host government. | MET if two of Reuters, AP, AFP report a munition impact on one of those five states dated inside the window, and that host government publicly attributes the impact to Iran or Iran-aligned forces. |
| KKR-20260903-77 | 49% | 2026-12-09 | military_conflict | Between 2026-09-04 and 2026-12-04, commercial transit of the Strait of Hormuz halts for at least 72 consecutive hours. | MET if Reuters and either Bloomberg or Lloyds List report a continuous period of at least 72 hours inside the window in which no laden commercial tanker transited the Strait of Hormuz. |
| KKR-20260903-78 | 21% | 2026-09-18 | economics_markets | The FOMC statement issued on 2026-09-16 leaves the federal funds target range unchanged from the range in effect on the packet date. Reference: target range 3.50 to 3.75 percent on 2026-09-03. | MET if the FOMC statement published on federalreserve.gov on 2026-09-16 maintains the federal funds target range at the level in effect on 2026-09-03. |
| KKR-20260903-79 | 21% | 2026-11-10 | economics_markets | ICE Brent front-month futures settle at or below 88.00 dollars per barrel on at least one trading day between 2026-09-08 and 2026-11-06. Reference: 96.70 on the packet date. | MET if the ICE published settlement price for the Brent front-month contract is 88.00 dollars or lower on any trading day between 2026-09-08 and 2026-11-06 inclusive. |
| KKR-20260903-80 | 30% | 2027-02-02 | cyber | The CISA KEV catalog carries an entry naming CrowdStrike as the vendor with a date-added value between 2026-09-04 and 2027-01-29. | MET if the CISA KEV catalog JSON contains a record whose vendorProject field is CrowdStrike and whose dateAdded value falls between 2026-09-04 and 2027-01-29 inclusive. |
| KKR-20260903-81 | 30% | 2026-11-06 | cyber | The CISA KEV catalog gains at least 50 new entries with date-added values between 2026-09-08 and 2026-11-02 inclusive. | MET if a count of CISA KEV catalog records whose dateAdded value falls between 2026-09-08 and 2026-11-02 inclusive reaches 50 or more. |
| KKR-20260903-82 | 36% | 2026-11-09 | crime_security | Between 2026-09-04 and 2026-11-04, Ukraine issues a notice of suspicion against at least one serving SBU or HUR officer over the Kyiv inter-agency shootout. | MET if the Prosecutor General office, the SBU, or the State Bureau of Investigation publicly announces a notice of suspicion naming a serving SBU or HUR officer in connection with the Kyiv shootout. |
| KKR-20260903-83 | 35% | 2026-12-16 | political | Between 2026-09-08 and 2026-12-11, the House Committee on Oversight approves a resolution recommending that Leon Black be held in contempt of Congress. | MET if a markup record or roll call published on oversight.house.gov shows committee approval of a contempt resolution naming Leon Black, dated between 2026-09-08 and 2026-12-11. |
| KKR-20260903-84 | 36% | 2026-12-18 | disaster | The NOAA CPC Oceanic Nino Index value for the September-October-November 2026 season is at or above plus 2.0 degrees Celsius. Reference: UN and BoM record El Nino forecasts on the packet date. | MET if the CPC Oceanic Nino Index table on the CPC site lists a SON 2026 value of 2.0 or greater when read on the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-04 and 2027-02-19, Nvidia announces that its acquisition of Hugging Face has closed." → REJECTED: resolution offers alternative VENUES joined by 'or' (…nvidia press release | or | an nvidia sec…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1404 issued all-time across 15 forecaster arms · 1139 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 401 issued · 373 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
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