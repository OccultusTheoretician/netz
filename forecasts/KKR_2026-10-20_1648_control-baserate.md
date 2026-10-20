**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201648Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-35 | 60% | 2026-12-01 | economics/markets | The EIA Cushing WTI crude spot price for 2026-11-20, as carried in FRED series DCOILWTICO, is at or above 100.00 dollars per barrel. Reference: 95.81 on the packet date 2026-10-20. | FRED series DCOILWTICO observation dated 2026-11-20 is at or above 100.00 (reference 95.81 on 2026-10-20). If no observation is posted for that date, the nearest prior observation governs. |
| KKR-20261020-36 | 60% | 2027-04-02 | economics/markets | Salesforce completes its announced acquisition of Braze Inc between 2026-10-20 and 2027-03-31, with closing of the merger reported in an 8-K on SEC EDGAR. | An 8-K filed on SEC EDGAR by Braze Inc or Salesforce Inc with a filing date between 2026-10-20 and 2027-03-31 inclusive reports completion of the acquisition of Braze by Salesforce. |
| KKR-20261020-37 | 42% | 2026-11-24 | political | France declares a state of emergency under the law of 3 April 1955 for all or part of its territory in response to the current unrest, with the decree published in the Journal officiel between 2026-10-20 and 2026-11-20. | A decree declaring a state of emergency under the law of 3 April 1955 for any part of French territory appears on Legifrance (Journal officiel) with publication date between 2026-10-20 and 2026-11-20 inclusive. |
| KKR-20261020-38 | 42% | 2026-12-04 | political | Democratic candidates win a majority (at least 218 of 435 seats) of the US House of Representatives in the general election held on 2026-11-03. | AP race calls as of the deadline show Democratic candidates winning at least 218 US House seats in the 2026-11-03 general election; uncalled races and pending runoffs count as not won. |
| KKR-20261020-39 | 66% | 2027-02-02 | military/conflict | Russia and Ukraine sign a ceasefire, armistice or peace agreement covering the entire line of contact between 2026-10-20 and 2027-01-29, with the signing confirmed by both governments. | Both the Russian and Ukrainian governments publicly confirm that authorized representatives signed a ceasefire, armistice or peace agreement covering all front lines between 2026-10-20 and 2027-01-29, as reported by both Reuters and AP. |
| KKR-20261020-40 | 66% | 2027-01-05 | military/conflict | The United States and Iran announce or sign a ceasefire, cessation-of-hostilities or framework agreement between 2026-10-20 and 2026-12-31 that both governments publicly confirm. | The US and Iranian governments each publicly confirm the same ceasefire, cessation-of-hostilities or framework agreement between the two countries, announced or signed between 2026-10-20 and 2026-12-31, as reported by both Reuters and AP. |
| KKR-20261020-41 | 46% | 2026-11-24 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Siemens entry with a date-added value between 2026-10-21 and 2026-11-20, following the reported in-the-wild exploitation of a Siemens Software Center flaw. | The CISA KEV catalog JSON contains at least one entry whose vendorProject field contains the string Siemens and whose dateAdded value falls between 2026-10-21 and 2026-11-20 inclusive. |
| KKR-20261020-42 | 46% | 2026-12-03 | cyber | A ransomware or data-extortion group claims the Ahold Delhaize cyberattack by publishing a leak-site listing naming Ahold Delhaize or one of its retail banners between 2026-10-20 and 2026-11-30. | Between 2026-10-20 and 2026-11-30 a leak-site listing by a ransomware or extortion group names Ahold Delhaize or one of its retail banners, as reported by at least two of BleepingComputer, The Record, SecurityWeek, Reuters. |
| KKR-20261020-43 | 36% | 2026-12-01 | crime/security | Tommy Robinson (Stephen Yaxley-Lennon) is convicted, by jury verdict or guilty plea, on at least one count in the London Crown Court trial in progress on 2026-10-20 concerning alleged harassment of journalists, with the conviction recorded between 2026-10-20 and 2026-11-27. | A guilty verdict or guilty plea against Tommy Robinson on at least one count in the London journalist-harassment trial is recorded between 2026-10-20 and 2026-11-27 inclusive, as reported by at least two of BBC, Guardian, PA Media, Reuters. |
| KKR-20261020-44 | 42% | 2026-11-24 | disaster | USGS catalogs at least one earthquake of magnitude 6.0 or greater with epicenter within 250 km of the 2026-10-20 M6.3 Vanuatu event (USGS id us6000u3jl) and origin time between 2026-10-21 and 2026-11-20. | The USGS ComCat earthquake catalog contains at least one event with magnitude 6.0 or greater, epicenter within 250 km of event us6000u3jl, and origin time between 2026-10-21 00:00 UTC and 2026-11-20 23:59 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4591 issued all-time across 21 forecaster arms · 3239 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1613 issued · 1230 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1613 | 1230 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 452 | 211 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 88 | 88 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 99 | 92 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 234 | 147 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 398 | 317 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 219 | 208 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 171 | 168 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*