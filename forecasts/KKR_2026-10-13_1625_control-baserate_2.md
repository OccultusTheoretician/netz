**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131625Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-53 | 40% | 2026-10-30 | political | Kimberly Guilfoyle resigns or is removed as US Ambassador to Greece, with the departure announced by her, the White House or the State Department between 2026-10-13 and 2026-10-27. | A White House, State Department or Guilfoyle statement, or reports from at least two of AP, Reuters and BBC, confirm her resignation or removal as US Ambassador to Greece announced between 2026-10-13 and 2026-10-27. |
| KKR-20261013-54 | 40% | 2026-11-02 | political | Pope Leo XIV is discharged from hospital after the operation to remove a growth, with the discharge occurring between 2026-10-13 and 2026-10-27. | The Holy See Press Office, or at least two of AP, Reuters and BBC, confirm Pope Leo XIV was discharged from hospital on a date between 2026-10-13 and 2026-10-27. |
| KKR-20261013-55 | 42% | 2026-10-30 | disaster | USGS records an earthquake of magnitude 6.5 or greater with an epicenter within 250 km of the M7.7 Panama mainshock (USGS event us6000u18k) and origin time between 2026-10-14 and 2026-10-27 UTC. | The USGS earthquake catalog (ComCat) lists at least one event of magnitude 6.5 or greater, origin time between 2026-10-14 and 2026-10-27 UTC, epicenter within 250 km of event us6000u18k. |
| KKR-20261013-56 | 41% | 2026-10-30 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one SAP product vulnerability with a dateAdded value between 2026-10-14 and 2026-10-27. | The CISA KEV catalog JSON carries at least one entry with vendorProject SAP and a dateAdded value between 2026-10-14 and 2026-10-27 inclusive. |
| KKR-20261013-57 | 60% | 2026-11-04 | economics/markets | ICE Brent front-month futures settle below 100.00 USD per barrel on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 105.86 on the packet date, 2026-10-13. | ICE Brent front-month daily settlement price, as published by ICE or reported by Reuters, is below 100.00 USD per barrel on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 105.86 on 2026-10-13. |
| KKR-20261013-58 | 60% | 2026-11-04 | economics/markets | The S&P 500 closes at least 2.0 percent below its prior close on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 7,796.70 on the packet date, 2026-10-13. | FRED series SP500 or S&P Dow Jones Indices shows a daily close at least 2.0 percent below the prior trading day close on at least one date between 2026-10-14 and 2026-10-30. Reference: 7,796.70 on 2026-10-13. |
| KKR-20261013-59 | 64% | 2026-10-30 | military/conflict | The Ukrainian Air Force reports that Russia launched at least 500 drones and missiles combined in a single overnight attack occurring between 2026-10-14 and 2026-10-27. | The Ukrainian Air Force, as relayed by Reuters or AP, reports at least 500 drones and missiles combined launched by Russia in one overnight attack dated between 2026-10-14 and 2026-10-27. |
| KKR-20261013-60 | 40% | 2026-11-17 | political | Bulgaria expels at least one Russian diplomat or declares one persona non grata between 2026-10-14 and 2026-11-13. | The Bulgarian Foreign Ministry, or at least two of Reuters, AP and BBC, confirm Bulgaria declared a Russian diplomat persona non grata or ordered one to leave, between 2026-10-14 and 2026-11-13. |
| KKR-20261013-61 | 64% | 2026-11-17 | military/conflict | Russia and Ukraine both publicly confirm a mutual ceasefire along the entire front line that takes effect between 2026-10-14 and 2026-11-13. | The Russian and Ukrainian governments both publicly confirm a mutual ceasefire along the entire front line taking effect between 2026-10-14 and 2026-11-13, as reported by at least two of Reuters, AP and BBC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A criminal indictment, information, or complaint naming Ilhan Omar as a defendant is filed in a US court between 2026-10-14 and 2026-11-13." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a us court docket  pacer   courtlistener | or | justice department press release shows a crim…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4075 issued all-time across 21 forecaster arms · 2964 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1442 issued · 1146 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1442 | 1146 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*