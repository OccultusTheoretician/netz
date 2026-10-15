**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151616Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-15_1512.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261015-71 | 64% | 2026-11-03 | military/conflict | Between 2026-10-16 and 2026-10-31, a Ukrainian drone or missile attack causes a fire or physical damage at one or more oil refineries in Russia. | TRUE if Reuters or AP reports a Ukrainian drone or missile attack causing fire or damage at a named oil refinery in Russia between 2026-10-16 and 2026-10-31 inclusive, confirmed by a Russian official or the Ukrainian military. |
| KKR-20261015-72 | 64% | 2026-11-18 | military/conflict | Between 2026-10-16 and 2026-11-15, a drone or missile hits at least one tanker vessel in the Black Sea or Sea of Azov, other than vessels already struck on or before 2026-10-15. | TRUE if Reuters or AP reports a new drone or missile hit on a named tanker in the Black Sea or Sea of Azov, at sea or in port, occurring between 2026-10-16 and 2026-11-15 inclusive. |
| KKR-20261015-73 | 64% | 2027-01-05 | military/conflict | Between 2026-10-16 and 2026-12-31, US forces drop a GBU-43/B Massive Ordnance Air Blast bomb on a target in Iran or Iranian territorial waters. | TRUE if the Pentagon or CENTCOM confirms, or Reuters and AP both report citing US officials, that a GBU-43/B was used against a target in Iran or its territorial waters between 2026-10-16 and 2026-12-31 inclusive. |
| KKR-20261015-74 | 60% | 2027-01-05 | economics/markets | The 10-year US Treasury constant-maturity yield for 2026-12-31 is above 5.00 percent. Reference: 5.05 percent on the packet date 2026-10-15. | TRUE if FRED series DGS10 shows a value strictly above 5.00 for 2026-12-31. Reference: 5.05 percent on 2026-10-15 per the packet market snapshot. |
| KKR-20261015-75 | 60% | 2026-12-04 | economics/markets | The BLS final-demand Producer Price Index 12-month change for October 2026, in its first release published between 2026-11-09 and 2026-11-30, is 6.0 percent or higher. Reference: 6.3 percent for September 2026. | TRUE if the first BLS release of October 2026 PPI data, published between 2026-11-09 and 2026-11-30, shows series WPUFD4 up 6.0 percent or more from October 2025. Reference: 6.3 percent for September 2026. |
| KKR-20261015-76 | 41% | 2026-12-03 | cyber | Between 2026-10-15 and 2026-11-30, CISA adds at least one vulnerability with Nextcloud or Collabora as vendor to its Known Exploited Vulnerabilities catalog. | TRUE if the CISA KEV catalog contains an entry whose vendorProject names Nextcloud or Collabora with a dateAdded value between 2026-10-15 and 2026-11-30 inclusive. |
| KKR-20261015-77 | 40% | 2026-12-15 | political | In the US general election held on 2026-11-03, Democratic candidates win at least 218 of the 435 seats in the House of Representatives. | TRUE if, by 2026-12-15, AP race calls, or certified state results for races AP has not called, give Democrats 218 or more House seats from the 2026-11-03 general election. |
| KKR-20261015-78 | 40% | 2027-01-05 | political | Between 2026-10-16 and 2026-12-31, Edi Rama formally resigns as Prime Minister of Albania or is removed from that office by parliament. | TRUE if Reuters or AP reports that Edi Rama formally resigned as Prime Minister of Albania, or was removed by parliament, between 2026-10-16 and 2026-12-31 inclusive. A stated intention to resign does not count. |
| KKR-20261015-79 | 39% | 2027-04-05 | crime/security | Between 2026-10-16 and 2027-03-31, the United States carries out the death sentence of Nidal Hasan, the 2009 Fort Hood shooter. | TRUE if the US Army, the Pentagon, or the Bureau of Prisons confirms, or Reuters and AP report, that Nidal Hasan was executed between 2026-10-16 and 2027-03-31 inclusive. |
| KKR-20261015-80 | 42% | 2026-11-18 | disaster | Between 2026-10-16 and 2026-11-15, at least one earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M7.7 Pitaloza Arriba, Panama mainshock, USGS event us6000u18k. | TRUE if a USGS ComCat search for magnitude 6.0 or greater within 200 km of the us6000u18k epicenter returns at least one event with a UTC origin date between 2026-10-16 and 2026-11-15 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4243 issued all-time across 21 forecaster arms · 3132 open (481 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1501 issued · 1205 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1501 | 1205 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 429 | 206 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 60 | 60 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 63 | 63 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*