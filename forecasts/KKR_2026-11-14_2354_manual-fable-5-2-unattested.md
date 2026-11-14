**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 142354Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-14_1613.md · forecaster: manual/fable-5.2/unattested · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261114-34 | 42% | 2027-03-03 | economics/markets | The Bank of England raises Bank Rate at a Monetary Policy Committee decision announced between 2026-11-16 and 2027-02-26. | The Bank of England official Bank Rate history shows at least one increase in Bank Rate with a change date between 2026-11-16 and 2027-02-26. |
| KKR-20261114-35 | 32% | 2026-12-21 | economics/markets | ICE Brent front-month futures settle above 105.00 dollars per barrel on at least one trading day between 2026-11-16 and 2026-12-18. Reference: 95.84 on the packet date. | ICE Brent front-month daily settlement is above 105.00 on at least one trading day between 2026-11-16 and 2026-12-18. Reference: 95.84 on the packet date. |
| KKR-20261114-36 | 30% | 2026-12-21 | economics/markets | The S&P 500 index closes below 7200.00 on at least one trading day between 2026-11-16 and 2026-12-18. Reference: 7561.67 on the packet date. | The official S&P 500 daily close is below 7200.00 on at least one trading day between 2026-11-16 and 2026-12-18. Reference: 7561.67 on the packet date. |
| KKR-20261114-37 | 8% | 2027-02-03 | military/conflict | Representatives of the governments of Russia and Ukraine sign a written ceasefire, armistice or peace agreement between 2026-11-15 and 2027-01-31. | Reuters and AP both report that Russian and Ukrainian government representatives signed a written ceasefire, armistice or peace agreement on a date between 2026-11-15 and 2027-01-31. |
| KKR-20261114-38 | 9% | 2027-01-19 | cyber | The CISA Known Exploited Vulnerabilities catalog adds a PostgreSQL vulnerability with a date-added value between 2026-11-15 and 2027-01-15. | The CISA KEV catalog carries at least one entry whose vendor or product field names PostgreSQL and whose date-added value falls between 2026-11-15 and 2027-01-15. |
| KKR-20261114-39 | 82% | 2027-01-20 | political | Hakeem Jeffries is elected Speaker of the US House of Representatives in a roll call vote held between 2027-01-03 and 2027-01-15. | The Clerk of the House roll call record for the election of the Speaker, held between 2027-01-03 and 2027-01-15, shows Hakeem Jeffries elected. |
| KKR-20261114-40 | 12% | 2027-03-05 | political | South Sudan holds nationwide voting in its national elections between 2027-02-01 and 2027-02-28. | At least two of Reuters, AP and AFP report that polling stations opened for national presidential or parliamentary voting in South Sudan on a date between 2027-02-01 and 2027-02-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Donald Trump, Xi Jinping and Vladimir Putin hold an in-person joint three-way meeting on Chinese territory between 2026-11-15 and 2026-11-30" → REJECTED: the resolution names a different subject than the statement — the claim is about Chinese, Donald, Jinping, Putin and the resolution settles on AP, BBC, China, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "An earthquake of magnitude 6.0 or greater occurs within 250 km of Lata, Solomon Islands (10.72S 165.80E) between 2026-11-15 and 2026-12-14 U" → REJECTED: the resolution names only a venue or register (ComCat, USGS, usgs) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A named person is criminally charged in connection with the explosive device found at an ethanol plant in the Peoria, Illinois area, with ch" → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal | or | illinois state…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5760 issued all-time across 23 forecaster arms · 4038 open (1721 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.2/unattested`:** 23 issued · 23 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 207 | 207 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 215 | 198 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 220 | 218 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 205 | 172 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 397 | 383 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*