**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171827Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-58 | 64% | 2026-11-04 | military/conflict | Between 2026-10-18 and 2026-11-01, Russia launches at least 600 drones and missiles combined against Ukraine in a single overnight attack, as tallied by the Ukrainian Air Force. | A Ukrainian Air Force tally, repeated by Reuters or AP, gives at least 600 drones and missiles combined for one overnight attack with a report date between 2026-10-18 and 2026-11-01 inclusive. |
| KKR-20261017-59 | 64% | 2026-11-04 | military/conflict | Between 2026-10-18 and 2026-10-31, at least one merchant vessel is struck by a projectile, drone, missile, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman. | UKMTO or JMIC incident reports list at least one merchant vessel struck by a projectile, drone, missile, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman, dated between 2026-10-18 and 2026-10-31 inclusive. |
| KKR-20261017-60 | 40% | 2026-11-04 | political | Between 2026-10-18 and 2026-10-31, Egypt formally authorises defence assistance to Saudi Arabia, through a vote of its House of Representatives or an announcement by its presidency or cabinet. | At least two of Reuters, AP, and Al-Ahram report that the Egyptian House of Representatives voted to approve, or the presidency or cabinet announced, authorisation of defence assistance to Saudi Arabia, dated between 2026-10-18 and 2026-10-31 inclusive. |
| KKR-20261017-61 | 60% | 2026-11-04 | economics/markets | Between 2026-10-19 and 2026-10-30, the front-month ICE Brent crude futures contract settles above 120.00 USD per barrel on at least one trading day. Reference: 109.86 USD per barrel on the packet date. | ICE Futures Europe daily settlement for front-month Brent exceeds 120.00 USD per barrel on at least one trading day between 2026-10-19 and 2026-10-30 inclusive. Reference: 109.86 USD per barrel on the packet date. |
| KKR-20261017-62 | 60% | 2026-11-04 | economics/markets | Between 2026-10-19 and 2026-10-30, the 10-year US Treasury yield is above 5.25 percent on at least one trading day. Reference: 5.10 percent on the packet date. | FRED series DGS10 shows a value above 5.25 for at least one date between 2026-10-19 and 2026-10-30 inclusive. Reference: 5.10 percent on the packet date. |
| KKR-20261017-63 | 41% | 2026-11-10 | cyber | Between 2026-10-18 and 2026-11-06, CISA adds at least one Drupal vulnerability to its Known Exploited Vulnerabilities catalog. | The CISA KEV catalog JSON carries at least one entry with vendorProject Drupal and a dateAdded value between 2026-10-18 and 2026-11-06 inclusive. |
| KKR-20261017-64 | 42% | 2026-10-28 | disaster | Between 2026-10-18 and 2026-10-25, the center of Hurricane Trudy, at whatever intensity it then holds, makes landfall on the Mexican mainland or Baja California coast. | National Hurricane Center advisories or best-track data for Trudy record its center making landfall on the Mexican mainland or Baja California coast, with a UTC landfall date between 2026-10-18 and 2026-10-25 inclusive. |
| KKR-20261017-65 | 42% | 2026-11-04 | disaster | Between 2026-10-18 and 2026-11-01 UTC, at least one earthquake of magnitude 7.0 or greater occurs anywhere in the world. | The USGS ComCat earthquake catalog lists at least one event with magnitude 7.0 or greater and origin time between 2026-10-18T00:00Z and 2026-11-01T23:59Z, using magnitudes as listed at the deadline. |
| KKR-20261017-66 | 40% | 2026-11-10 | political | Roger Marshall receives more votes than any other candidate in the Kansas general election for US Senate held on 2026-11-03. | Kansas Secretary of State results, as posted by 2026-11-10, show Roger Marshall with the most votes among all candidates in the 2026-11-03 US Senate general election in Kansas. |
| KKR-20261017-67 | 40% | 2026-11-17 | political | Between 2026-10-19 and 2026-11-13, OFAC announces new Russia-related Designations on its Recent Actions page. | The OFAC Recent Actions page lists an entry dated between 2026-10-19 and 2026-11-13 inclusive whose title contains Russia-related Designations, excluding entries that only update or remove designations. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4386 issued all-time across 21 forecaster arms · 3275 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1546 issued · 1250 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1546 | 1250 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*