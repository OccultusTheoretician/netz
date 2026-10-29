**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292156Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-29_1513.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261029-33 | 57% | 2026-11-16 | cyber | CISA adds a Cisco ASA or FTD vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-29 and 2026-11-12. | The CISA KEV catalog contains an entry with vendorProject Cisco, a product field naming ASA or FTD, and a dateAdded value between 2026-10-29 and 2026-11-12 inclusive. |
| KKR-20261029-34 | 57% | 2026-12-02 | cyber | CISA adds a GitLab vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-29 and 2026-11-30. | The CISA KEV catalog contains an entry with vendorProject GitLab and a dateAdded value between 2026-10-29 and 2026-11-30 inclusive. |
| KKR-20261029-35 | 57% | 2026-12-11 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting concluding on 2026-12-09. | The FOMC statement of 2026-12-09 announces a higher target range, so FRED series DFEDTARU for 2026-12-10 exceeds its value for 2026-12-08. |
| KKR-20261029-36 | 57% | 2026-12-04 | political | The Democratic nominee wins the Texas US Senate general election held on 2026-11-03. | The Texas Secretary of State canvass, or the AP race call if the canvass is incomplete, shows the Democratic nominee receiving the most votes in the 2026-11-03 Texas US Senate election. |
| KKR-20261029-37 | 57% | 2027-01-04 | crime/security | The Victorian Court of Appeal quashes at least one murder conviction of Erin Patterson in a ruling delivered between 2026-10-29 and 2026-12-31. | A Court of Appeal judgment delivered between 2026-10-29 and 2026-12-31, published by the Supreme Court of Victoria or AustLII, quashes at least one murder conviction of Erin Patterson, whether or not a retrial is ordered. |
| KKR-20261029-38 | 57% | 2026-12-02 | disaster | An earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M6.5 Bonin Islands earthquake (USGS us6000u4r9) between 2026-10-30 and 2026-11-28. | The USGS ComCat catalog lists an event of magnitude 6.0 or greater with origin time between 2026-10-30 and 2026-11-28 UTC within 200 km of the epicenter of USGS event us6000u4r9. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5151 issued all-time across 22 forecaster arms · 3429 open (553 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 23 issued · 23 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 23 | 23 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 137 | 120 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 138 | 136 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 131 | 98 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 467 | 352 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 297 | 283 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*