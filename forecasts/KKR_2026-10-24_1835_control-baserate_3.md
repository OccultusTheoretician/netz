**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241835Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-24_1512.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261024-62 | 66% | 2026-11-18 | military/conflict | The United States military conducts at least one strike on a target located on Iranian land territory, including Iranian islands, between 2026-10-26 and 2026-11-15 inclusive. | Between 2026-10-26 and 2026-11-15 inclusive, US Central Command, the Pentagon or the White House confirms, or two of Reuters, AP, AFP and BBC independently report, a US strike on a target on Iranian land. |
| KKR-20261024-63 | 66% | 2026-11-18 | military/conflict | A single Russian missile or drone attack on one Ukrainian city kills at least 20 people between 2026-10-26 and 2026-11-15 inclusive. | By the deadline, Ukrainian officials and two of Reuters, AP, AFP and BBC report a confirmed death toll of at least 20 from one Russian strike on one Ukrainian city occurring between 2026-10-26 and 2026-11-15 inclusive. |
| KKR-20261024-64 | 60% | 2026-12-14 | economics/markets | At least one of S&P Global Ratings, Fitch Ratings or Moodys Ratings lowers the long-term sovereign credit rating of France by one or more notches between 2026-10-26 and 2026-12-11 inclusive. | S&P Global Ratings, Fitch Ratings or Moodys Ratings publishes a rating action between 2026-10-26 and 2026-12-11 inclusive lowering the long-term sovereign rating of France by at least one notch; outlook changes alone do not count. |
| KKR-20261024-65 | 46% | 2026-11-12 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one vulnerability in the PHP language runtime, with a date-added value between 2026-10-26 and 2026-11-08 inclusive. | The CISA KEV catalog JSON carries at least one entry with a dateAdded value between 2026-10-26 and 2026-11-08 inclusive whose vendorProject is PHP Group or whose product is PHP. |
| KKR-20261024-66 | 36% | 2026-11-10 | crime/security | Jordanian security forces arrest or kill at least one suspect in the church funeral shooting in Jordan that was reported on 2026-10-24, between 2026-10-24 and 2026-11-07 inclusive. | Between 2026-10-24 and 2026-11-07 inclusive, Jordanian officials confirm the arrest or killing of at least one suspect in the church shooting, and two of Reuters, AP, AFP and BBC report it. |
| KKR-20261024-67 | 42% | 2026-11-05 | disaster | At least one earthquake of magnitude 7.0 or greater occurs anywhere on Earth between 2026-10-25 and 2026-11-02 inclusive, by UTC origin time. | The USGS earthquake catalog lists at least one event of magnitude 7.0 or greater with origin time between 2026-10-25 and 2026-11-02 inclusive (UTC), using the magnitude shown at the deadline. |
| KKR-20261024-68 | 42% | 2026-11-18 | disaster | A laboratory-confirmed Ebola case is identified in a country that had reported no confirmed Ebola case in 2026 before 2026-10-24, between 2026-10-26 and 2026-11-15 inclusive, excluding patients medically evacuated from abroad. | Between 2026-10-26 and 2026-11-15 inclusive, WHO or a national health ministry reports a laboratory-confirmed Ebola case in a country with no confirmed Ebola case in 2026 before 2026-10-24, excluding medically evacuated patients. |
| KKR-20261024-69 | 42% | 2026-11-25 | political | The Democratic Party wins at least 218 of the 435 seats in the United States House of Representatives in the general election held on 2026-11-03. | By the deadline, the Associated Press has projected, or Clerk of the House results show, Democrats winning at least 218 House seats in the 2026-11-03 general election. |
| KKR-20261024-70 | 42% | 2026-12-14 | political | The French government falls, meaning the Prime Minister in office on 2026-10-24 submits a resignation of the government accepted by the President, or the National Assembly adopts a censure motion against it, between 2026-10-26 and 2026-12-11 inclusive. | Between 2026-10-26 and 2026-12-11 inclusive, the Elysee announces acceptance of the government resignation, or the National Assembly adopts a censure motion against it, per the Journal Officiel or Assemblee nationale records. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE front-month Brent crude futures settle at or above 125.00 dollars per barrel on at least one trading day between 2026-10-26 and 2026-11-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4906 issued all-time across 21 forecaster arms · 3554 open (681 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1727 issued · 1344 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1727 | 1344 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
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
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*