**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 262315Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-26_1513.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261026-33 | 63% | 2026-12-02 | military/conflict | Between 2026-10-27 and 2026-11-30, the United States and Iran conclude an agreement covering the Strait of Hormuz that both the White House and the Iranian foreign ministry publicly confirm as concluded. | True if, between 2026-10-27 and 2026-11-30, both the White House and the Iranian foreign ministry confirm a concluded US-Iran agreement covering the Strait of Hormuz; statements that a deal is close or under negotiation do not count. |
| KKR-20261026-34 | 63% | 2026-11-18 | military/conflict | Between 2026-10-27 and 2026-11-16, Saudi authorities (Ministry of Defense or the Saudi-led coalition) publicly confirm at least one new Houthi missile or drone launched toward Saudi territory, whether intercepted or impacting. | True if a Saudi Ministry of Defense or coalition statement, carried by Reuters or AP, confirms at least one Houthi missile or drone launched toward Saudi territory with launch date between 2026-10-27 and 2026-11-16. |
| KKR-20261026-35 | 59% | 2026-12-17 | economics/markets | The front-month NYMEX WTI crude futures contract settles below 85.00 USD per barrel on 2026-12-15. Reference: 100.93 on the packet date 2026-10-26. | True if the CME Group official settlement price for the nearest-expiry NYMEX WTI crude oil futures contract on 2026-12-15 is below 85.00 USD per barrel; reference level 100.93 on 2026-10-26. |
| KKR-20261026-36 | 59% | 2026-12-22 | economics/markets | Anthropic common stock has its first day of trading on Nasdaq or the NYSE on a date between 2026-10-27 and 2026-12-18. | True if the exchange listing record and an SEC EDGAR 424B4 prospectus (or equivalent direct-listing filing) show Anthropic shares first traded on Nasdaq or NYSE on a date between 2026-10-27 and 2026-12-18. |
| KKR-20261026-37 | 45% | 2026-11-24 | cyber | CISA adds at least one of the PHP2Shell vulnerabilities, CVE-2026-109618 or CVE-2026-109619, to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-26 and 2026-11-20. | True if the CISA KEV catalog JSON feed contains an entry for CVE-2026-109618 or CVE-2026-109619 whose dateAdded field is between 2026-10-26 and 2026-11-20 inclusive. |
| KKR-20261026-38 | 42% | 2026-12-04 | political | In the 2026-11-03 US House elections, Democratic candidates win at least 218 of 435 seats, as called by the Associated Press by 2026-12-04. | True if, by 2026-12-04, Associated Press race calls show Democratic candidates winning at least 218 US House seats in the 2026-11-03 general election; uncalled races count as not won. |
| KKR-20261026-39 | 42% | 2026-11-30 | political | BMA consultant doctors in England are on strike on 2026-11-25, the first day of the two-day action announced for 2026-11-25 to 2026-11-27. | True if BMA consultant doctors in England are on strike on 2026-11-25, confirmed by both a BMA statement and NHS England; action suspended, cancelled or postponed before that date resolves false. |
| KKR-20261026-40 | 42% | 2026-12-22 | political | The Superior Electoral Court (TSE) of Brazil holds the diplomacao ceremony formally conferring the presidential diploma on Luiz Inacio Lula da Silva on a date between 2026-12-01 and 2026-12-19. | True if the TSE official website or Diario da Justica Eletronico records the diplomacao of Luiz Inacio Lula da Silva as president-elect on a date between 2026-12-01 and 2026-12-19 inclusive. |
| KKR-20261026-41 | 38% | 2026-12-02 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 6.0 or greater with a USGS place name containing Bonin Islands and origin time between 2026-10-27 00:00 UTC and 2026-11-30 23:59 UTC. | True if the USGS ComCat catalog lists an event with magnitude 6.0 or greater, place field containing Bonin Islands, and origin time between 2026-10-27 00:00 UTC and 2026-11-30 23:59 UTC. |
| KKR-20261026-42 | 44% | 2026-12-22 | crime/security | A jury at Southwark Crown Court returns a verdict on at least one count in the trial of Russell Brand on a date between 2026-10-27 and 2026-12-18. | True if a jury verdict, guilty or not guilty, on at least one count against Russell Brand is delivered at Southwark Crown Court between 2026-10-27 and 2026-12-18, as reported by Reuters and the BBC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5006 issued all-time across 21 forecaster arms · 3292 open (347 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1761 issued · 1252 open · 477 resolved · 273 hits / 204 misses · **Brier 0.300** against its own base rate 57.2% (climatological 0.245) · **skill -0.226**.

*88 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1761 | 1252 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 116 | 105 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 123 | 121 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 122 | 91 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 447 | 332 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 267 | 253 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*