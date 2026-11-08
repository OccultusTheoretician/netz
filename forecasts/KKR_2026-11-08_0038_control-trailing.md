**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 080038Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-07_1612.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261108-14 | 65% | 2026-11-24 | military/conflict | Between 2026-11-08 and 2026-11-21 inclusive, US or Israeli forces conduct at least one new airstrike or missile strike on Iranian territory, corroborated by at least two of Reuters, AP, and AFP. | True if at least two of Reuters, AP, AFP report a US or Israeli strike on Iranian soil occurring between 2026-11-08 and 2026-11-21. Strikes before 2026-11-08 do not count. |
| KKR-20261108-15 | 42% | 2027-01-11 | political | Hakeem Jeffries is elected Speaker of the US House on the first ballot of the 120th Congress, with the vote held between 2027-01-03 and 2027-01-07 inclusive. | True if the House Clerk roll call record shows Jeffries winning a majority of votes cast for a person on the first Speaker ballot held between 2027-01-03 and 2027-01-07. |
| KKR-20261108-16 | 69% | 2026-12-07 | economics/markets | Front-month WTI crude settles above 100.00 USD per barrel on at least one NYMEX trading day between 2026-11-09 and 2026-12-04 inclusive. Reference: 90.83 on the packet date. | True if CME NYMEX publishes a front-month WTI daily settlement price strictly above 100.00 for any trading day from 2026-11-09 through 2026-12-04. |
| KKR-20261108-17 | 69% | 2027-04-02 | economics/markets | Anthropic common shares begin trading on the NYSE or Nasdaq between 2026-11-09 and 2027-03-31 inclusive. | True if NYSE or Nasdaq exchange records show a first trading day for Anthropic shares between 2026-11-09 and 2027-03-31, confirmed by an SEC EDGAR filing. |
| KKR-20261108-18 | 55% | 2026-12-01 | cyber | The CISA KEV catalog adds at least one CVE affecting a QNAP product with a date-added value between 2026-11-08 and 2026-11-28 inclusive. | True if the CISA KEV JSON feed contains an entry with vendorProject QNAP and dateAdded between 2026-11-08 and 2026-11-28 inclusive. |
| KKR-20261108-19 | 50% | 2026-12-09 | disaster | USGS records at least one earthquake of magnitude 6.5 or greater with an epicenter in Japan or within 200 km of its coast between 2026-11-08 and 2026-12-07 inclusive. | True if the USGS earthquake catalog lists an M6.5 or greater event between 2026-11-08 and 2026-12-07 whose location string names Japan or whose epicenter lies within 200 km of Japan. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5452 issued all-time across 22 forecaster arms · 3730 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 108 issued · 108 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 108 | 108 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 183 | 166 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 184 | 182 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 163 | 130 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 500 | 385 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 356 | 342 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*