**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201648Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-45 | 30% | 2026-11-23 | cyber | The CISA KEV catalog adds a Siemens Software Center vulnerability, the flaw ClickFix attackers reportedly exploited, with a date-added value between 2026-10-21 and 2026-11-20. | TRUE if the CISA KEV catalog lists a Siemens Software Center CVE with dateAdded between 2026-10-21 and 2026-11-20 inclusive; otherwise FALSE. |
| KKR-20261020-46 | 35% | 2026-12-02 | cyber | The CISA KEV catalog adds at least one Plex Media Server CVE tied to the Plex2Shell exploitation, with a date-added value between 2026-10-21 and 2026-11-30. | TRUE if the CISA KEV catalog lists a Plex product CVE with dateAdded between 2026-10-21 and 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20261020-47 | 55% | 2027-01-04 | economics/markets | The US 10-year Treasury constant maturity yield is above 5.00 percent on 2026-12-31. Reference: 5.10 percent on the packet date. | TRUE if the FRED series DGS10 observation for 2026-12-31 is greater than 5.00; FALSE if 5.00 or lower. Reference: 5.10 percent on 2026-10-20. |
| KKR-20261020-48 | 50% | 2026-12-22 | economics/markets | Brent crude spot falls below 100.00 USD per barrel on at least one trading day between 2026-10-21 and 2026-12-18. Reference: 106.63 USD on the packet date. | TRUE if FRED series DCOILBRENTEU shows any daily value below 100.00 dated 2026-10-21 through 2026-12-18; otherwise FALSE. Reference: 106.63 on 2026-10-20. |
| KKR-20261020-49 | 62% | 2026-12-14 | political | In the scheduled 2026-11-03 US midterm election, Democrats win at least 218 House seats as called by the Associated Press by 2026-12-11. | TRUE if AP race calls published by 2026-12-11 award Democratic candidates at least 218 of 435 House seats; otherwise FALSE. |
| KKR-20261020-50 | 12% | 2027-02-03 | political | Albanian Prime Minister Edi Rama resigns or is removed from office between 2026-10-21 and 2027-01-31. | TRUE if Reuters or AP report Rama resigned, was dismissed, or lost office via no-confidence vote with effect between 2026-10-21 and 2027-01-31; otherwise FALSE. |
| KKR-20261020-51 | 80% | 2026-12-03 | military/conflict | The UK Ministry of Defence or RAF officially confirms RAF Typhoon jets have arrived in Saudi Arabia between 2026-10-21 and 2026-11-30. | TRUE if an official UK MoD or RAF statement, published between 2026-10-21 and 2026-11-30, confirms Typhoons are deployed in Saudi Arabia; otherwise FALSE. |
| KKR-20261020-52 | 10% | 2027-02-03 | military/conflict | Russia and Ukraine both announce a general ceasefire that takes effect between 2026-10-21 and 2027-01-31. | TRUE if Reuters and AP both report that the Russian and Ukrainian governments each declared a front-wide ceasefire taking effect between 2026-10-21 and 2027-01-31; otherwise FALSE. |
| KKR-20261020-53 | 12% | 2027-01-05 | disaster | USGS records an earthquake of magnitude 7.0 or greater within 300 km of Port-Olry, Vanuatu between 2026-10-21 and 2026-12-31. | TRUE if the USGS ComCat catalog lists an event of magnitude 7.0+ within 300 km of Port-Olry with origin time between 2026-10-21 and 2026-12-31 UTC; otherwise FALSE. |
| KKR-20261020-54 | 55% | 2027-01-05 | crime/security | A Kenyan court sentences cult leader Paul Mackenzie following his murder conviction, with sentence pronounced between 2026-10-21 and 2026-12-31. | TRUE if at least two of Reuters, AP, or BBC report a Kenyan court pronounced sentence on Mackenzie between 2026-10-21 and 2026-12-31; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4601 issued all-time across 21 forecaster arms · 3249 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 229 issued · 218 open · 11 resolved · 5 hits / 6 misses · **Brier 0.362** against its own base rate 45.5% (climatological 0.248) · **skill -0.460** · under 30 resolved, this is noise.

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
| manual/opus-5.5/unattested | 229 | 218 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 171 | 168 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*