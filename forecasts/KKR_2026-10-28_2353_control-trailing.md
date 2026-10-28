**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 282353Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-28_1515.md · forecaster: control/trailing · 5 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261028-19 | 69% | 2026-12-01 | economics/markets | ICE Brent crude front-month futures settle below 100.00 US dollars per barrel on at least one trading day between 2026-10-29 and 2026-11-27. Reference: 112.00 on the packet date, 2026-10-28. | True if the official ICE daily settlement price of the front-month Brent crude futures contract is below 100.00 on any trading day from 2026-10-29 through 2026-11-27 inclusive. Reference: 112.00 on 2026-10-28. |
| KKR-20261028-20 | 69% | 2027-02-02 | economics/markets | The Wendys Company (NASDAQ: WEN) files a Form 8-K with the SEC between 2026-10-29 and 2027-01-29 announcing a signed definitive agreement to be acquired in whole by Trian Fund Management or any other party. | True if SEC EDGAR shows a Wendys Form 8-K filed between 2026-10-29 and 2027-01-29 disclosing a signed definitive agreement for the acquisition of the whole company; non-binding proposals or letters of intent do not count. |
| KKR-20261028-21 | 55% | 2026-12-01 | cyber | CISA adds at least one CVE affecting Oracle E-Business Suite to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-29 and 2026-11-27. | True if the CISA KEV catalog JSON contains at least one entry with vendorProject Oracle, product naming E-Business Suite, and dateAdded between 2026-10-29 and 2026-11-27 inclusive. |
| KKR-20261028-22 | 55% | 2026-12-22 | cyber | Between 2026-10-29 and 2026-12-18 a US federal agency (FEC, CISA, FBI, ODNI, or DOJ) publicly attributes the October 2026 intrusion into the FEC campaign finance filing system to a named foreign government, threat group, or charged individual. | True if an official FEC, CISA, FBI, ODNI, or DOJ statement, advisory, or charging document published between 2026-10-29 and 2026-12-18 names a specific foreign government, threat group, or charged individual as responsible for the FEC filing-system intrusion. |
| KKR-20261028-23 | 50% | 2026-12-01 | disaster | The USGS earthquake catalog records at least one magnitude 6.0 or greater earthquake with epicenter in the Vanuatu region box 12S-21S, 164E-171E, with origin time between 2026-10-29 and 2026-11-27 UTC. | True if the USGS ComCat catalog lists at least one event with magnitude 6.0 or greater, origin time between 2026-10-29T00:00Z and 2026-11-27T23:59Z, and epicenter within latitude 12S-21S and longitude 164E-171E. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5103 issued all-time across 22 forecaster arms · 3381 open (448 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 5 issued · 5 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 5 | 5 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 132 | 115 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 133 | 131 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 129 | 96 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 460 | 345 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 286 | 272 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*