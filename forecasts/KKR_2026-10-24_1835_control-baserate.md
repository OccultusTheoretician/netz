**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241835Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-24_1512.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261024-28 | 66% | 2026-11-18 | military/conflict | US military forces conduct at least one kinetic strike on a target inside the territory of Iran between 2026-10-25 and 2026-11-15. | True if US Central Command or the White House publicly confirms, or Reuters and AP both report, a US kinetic strike on a target inside Iran occurring between 2026-10-25 and 2026-11-15. Interceptions of Iranian projectiles do not count. |
| KKR-20261024-29 | 66% | 2026-11-10 | military/conflict | Between 2026-10-25 and 2026-11-07, the Ukrainian Air Force reports at least one overnight Russian attack in which 500 or more drones and missiles combined were launched against Ukraine. | True if an official Ukrainian Air Force daily report, as carried by Reuters, AP or Ukrinform, states that Russia launched 500 or more drones and missiles combined in a single overnight attack dated between 2026-10-25 and 2026-11-07. |
| KKR-20261024-30 | 46% | 2026-12-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one PHP entry (vendorProject PHP Group or PHP) with a dateAdded value between 2026-10-24 and 2026-11-30. | True if the CISA KEV catalog JSON contains an entry whose vendorProject field is PHP Group or PHP and whose dateAdded is between 2026-10-24 and 2026-11-30 inclusive, as of the deadline. |
| KKR-20261024-31 | 46% | 2027-01-06 | cyber | The HHS Office for Civil Rights breach portal lists a Quest Diagnostics breach affecting 500 or more individuals with a breach submission date between 2026-10-24 and 2026-12-31. | True if the HHS OCR Breach Portal lists an entry whose Name of Covered Entity contains Quest Diagnostics, affecting 500 or more individuals, with Breach Submission Date between 2026-10-24 and 2026-12-31. |
| KKR-20261024-32 | 42% | 2026-12-01 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election scheduled for 2026-11-03. | True if, as of 2026-12-01, the Associated Press has called at least 218 of the 435 US House races from the 2026-11-03 general election for Democratic Party candidates. |
| KKR-20261024-33 | 42% | 2027-01-05 | political | The US Treasury Office of Foreign Assets Control designates at least one additional International Criminal Court judge, prosecutor or staff member under Executive Order 14203 between 2026-10-24 and 2026-12-31. | True if an OFAC Recent Actions notice dated between 2026-10-24 and 2026-12-31 announces a new SDN designation of an ICC judge, prosecutor or staff member under Executive Order 14203. Designations of non-ICC persons do not count. |
| KKR-20261024-34 | 42% | 2027-01-05 | political | The Malaysian government or the Malaysian Communications and Multimedia Commission formally orders a nationwide public ban or block of the Waze navigation app between 2026-10-24 and 2026-12-31. | True if Bernama, Reuters or The Star reports a formal Malaysian government or MCMC order, announced between 2026-10-24 and 2026-12-31, banning or blocking Waze nationwide for the general public. |
| KKR-20261024-35 | 42% | 2026-11-10 | disaster | USGS catalogs an earthquake of magnitude 6.0 or greater with epicenter within 250 km of USGS event us6000u4j2 (the M6.9 Vanuatu earthquake of 2026-10-24) and origin time between 2026-10-25 and 2026-11-07. | True if the USGS ComCat catalog, as of the deadline, lists an event of magnitude 6.0 or greater with origin time between 2026-10-25 00:00 UTC and 2026-11-07 23:59 UTC and epicenter within 250 km of event us6000u4j2. |
| KKR-20261024-36 | 36% | 2026-11-10 | crime/security | The Islamic State group, via its Amaq agency or an official statement, claims responsibility between 2026-10-24 and 2026-11-07 for the gun attack on a church funeral in Jordan first reported on 2026-10-23. | True if SITE Intelligence Group, Reuters or AP reports an Islamic State or Amaq claim of responsibility, issued between 2026-10-24 and 2026-11-07, for the gun attack on a church funeral in Jordan first reported on 2026-10-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent front-month crude futures settle at or above 125.00 USD per barrel on at least one trading day between 2026-10-26 and 2026-11-20. " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4872 issued all-time across 21 forecaster arms · 3520 open (681 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1710 issued · 1327 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1710 | 1327 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 108 | 107 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 109 | 109 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 247 | 160 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 429 | 348 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 251 | 240 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 205 | 202 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*