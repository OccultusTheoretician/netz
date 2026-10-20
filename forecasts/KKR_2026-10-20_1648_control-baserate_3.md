**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201648Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-75 | 60% | 2026-11-10 | economics/markets | The US 10-year Treasury constant maturity yield will print above 5.25 percent on at least one day between 2026-10-21 and 2026-11-06. Reference: 5.10 percent on the packet date 2026-10-20. | FRED series DGS10 shows a daily value above 5.25 for at least one date between 2026-10-21 and 2026-11-06 inclusive. |
| KKR-20261020-76 | 60% | 2026-11-10 | economics/markets | ICE front-month Brent crude will settle above 115.00 dollars per barrel on at least one trading day between 2026-10-21 and 2026-11-06. Reference: 106.63 on the packet date. | ICE Brent front-month daily settlement exceeds 115.00 on at least one trading day between 2026-10-21 and 2026-11-06 inclusive, per ICE or EIA published Brent spot and futures data. |
| KKR-20261020-77 | 66% | 2026-11-06 | military/conflict | The UK government will confirm that RAF Typhoon fighter jets have arrived in Saudi Arabia between 2026-10-21 and 2026-11-03. | GOV.UK or a UK Ministry of Defence statement, corroborated by Reuters or BBC, states that RAF Typhoon aircraft have arrived or are operating from Saudi territory, with the statement dated between 2026-10-21 and 2026-11-03. |
| KKR-20261020-78 | 66% | 2026-11-06 | military/conflict | The United States military will carry out a publicly acknowledged strike on targets inside Iranian territory between 2026-10-21 and 2026-11-03. | The US Department of Defense or White House acknowledges a US strike on Iranian territory occurring between 2026-10-21 and 2026-11-03, and both Reuters and AP report it. |
| KKR-20261020-79 | 66% | 2026-11-06 | military/conflict | The Houthis will carry out a missile or drone attack on Saudi territory between 2026-10-21 and 2026-11-03 that Saudi authorities or two major wire services confirm. | The Saudi Ministry of Defense, or both Reuters and AP, report a Houthi missile or drone attack on Saudi territory occurring between 2026-10-21 and 2026-11-03. |
| KKR-20261020-80 | 42% | 2026-11-06 | political | France will declare a nationwide or metropolitan state of emergency by official decree between 2026-10-21 and 2026-11-03. | The Journal Officiel, searchable on Legifrance, publishes a decree declaring a state of emergency covering metropolitan France or its major cities, dated between 2026-10-21 and 2026-11-03. |
| KKR-20261020-81 | 46% | 2026-11-06 | cyber | The CISA KEV catalog will add a Siemens product vulnerability between 2026-10-21 and 2026-11-03. | The CISA KEV catalog carries at least one entry with vendorProject Siemens and a dateAdded value between 2026-10-21 and 2026-11-03 inclusive. |
| KKR-20261020-82 | 66% | 2026-11-20 | military/conflict | Russia and Ukraine will both publicly announce a general ceasefire between 2026-10-21 and 2026-11-17. | Official statements from both the Russian and Ukrainian governments, reported by Reuters and AP, announce a general ceasefire covering all front lines, dated between 2026-10-21 and 2026-11-17. |
| KKR-20261020-83 | 42% | 2026-11-06 | disaster | A magnitude 7.0 or greater earthquake will strike anywhere in the world between 2026-10-21 and 2026-11-03. | The USGS earthquake catalog lists at least one event of magnitude 7.0 or greater with an origin time between 2026-10-21 and 2026-11-03 UTC. |
| KKR-20261020-84 | 36% | 2026-11-20 | crime/security | Australian authorities will upgrade the charges against Brendan Nugent to include murder or manslaughter between 2026-10-21 and 2026-11-17. | Court records or police statements, reported by ABC, BBC or the Guardian, show Brendan Nugent charged with murder or manslaughter in connection with the attack on Helen Haines, with the charge dated between 2026-10-21 and 2026-11-17. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4631 issued all-time across 21 forecaster arms · 3279 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1633 issued · 1250 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1633 | 1250 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
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
| manual/sonnet-5.5/unattested | 181 | 178 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*