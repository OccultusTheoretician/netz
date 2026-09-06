**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062247Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-101 | 21% | 2026-09-18 | economics/markets | At the scheduled FOMC meeting concluding 2026-09-16, the Committee raises the federal funds target range above the range in effect at packet seal. Reference: target range 3.50 to 3.75 percent on 2026-09-06 (FRED series DFEDTARU upper limit 3.75). | True if the FOMC statement dated 2026-09-16 announces a target range whose upper limit exceeds 3.75 percent, reflected in FRED DFEDTARU for 2026-09-17; false if the range is held or lowered. |
| KKR-20260906-102 | 49% | 2026-10-05 | military/conflict | Between 2026-09-07 and 2026-09-30 inclusive, UKMTO publishes at least one advisory reporting an attack on, boarding of, or seizure of a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf. | True if the UKMTO advisories archive contains at least one advisory dated 2026-09-07 through 2026-09-30 describing an attack, boarding, or seizure of a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf. |
| KKR-20260906-103 | 35% | 2026-11-04 | political | Between 2026-09-07 and 2026-10-31 inclusive, Donald Trump and Vladimir Putin hold an in-person meeting, confirmed by both the White House and the Kremlin. | True if both whitehouse.gov and kremlin.ru publish confirmation that Trump and Putin met in person on a date between 2026-09-07 and 2026-10-31 inclusive; video or telephone contact does not count. |
| KKR-20260906-104 | 36% | 2026-09-22 | crime/security | Between 2026-09-06 and 2026-09-20 inclusive, Victoria Police announce that a person has been arrested and charged over the alleged axe attack in Victoria, Australia, reported by the Guardian on 2026-09-06, that left three people with life-threatening injuries. | True if a Victoria Police media release, or two of ABC News, The Age, and Guardian Australia, report a person arrested and charged over that attack, with the charge laid between 2026-09-06 and 2026-09-20 inclusive. |
| KKR-20260906-105 | 30% | 2026-10-06 | cyber | Between 2026-09-07 and 2026-10-02 inclusive, CISA adds to its Known Exploited Vulnerabilities catalog at least one CVE whose product is Adobe Commerce or Magento Open Source, with a dateAdded value in that range. | True if the CISA KEV JSON feed contains an entry with vendorProject Adobe or Magento, product Commerce, Adobe Commerce, or Magento, and dateAdded between 2026-09-07 and 2026-10-02 inclusive. |
| KKR-20260906-106 | 30% | 2026-11-03 | cyber | Between 2026-09-07 and 2026-10-30 inclusive, CISA adds to its Known Exploited Vulnerabilities catalog at least one CVE whose product is VMware Workstation or VMware Fusion (vendor VMware or Broadcom), with a dateAdded value in that range. | True if the CISA KEV JSON feed contains an entry whose product field names Workstation or Fusion under vendorProject VMware or Broadcom, with dateAdded between 2026-09-07 and 2026-10-30 inclusive. |
| KKR-20260906-107 | 36% | 2026-10-07 | disaster | Between 2026-09-07 and 2026-10-04 inclusive, the USGS earthquake catalog records at least one earthquake of magnitude 6.5 or greater with epicenter within 300 km of the 2026 M6.3 event 84 km SSW of Nikolski, Alaska (USGS event id us7000tdvt). | True if a USGS ComCat search returns at least one event of magnitude 6.5 or greater with origin time between 2026-09-07 00:00 UTC and 2026-10-04 23:59 UTC located within 300 km of USGS event us7000tdvt. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The ICE Brent crude front-month futures contract settles at or above 100.00 dollars per barrel on 2026-10-02. Reference: 96.28 dollars per b" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10-year Treasury constant maturity yield published by the Federal Reserve (FRED series DGS10) for 2026-10-30 is at or above 5.00 percent" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-06 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "In the Saxony-Anhalt Landtag election held on 2026-09-06, the AfD receives the largest share of the statewide party-list vote of any party, " → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

1598 issued all-time across 16 forecaster arms · 1333 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 472 issued · 444 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 472 | 444 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 224 | 136 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*