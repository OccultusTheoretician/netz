**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 252347Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: manual/sonnet-5.5/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-43 | 38% | 2026-11-10 | military/conflict | Between 2026-10-26 and 2026-11-08, United States forces strike at least one target on Iranian land, on Iranian islands or in Iranian territorial waters, and a US government statement acknowledges the strike. | A White House, Pentagon or CENTCOM statement acknowledges a US strike on a target in Iran, including islands and territorial waters, dated between 2026-10-26 and 2026-11-08, and Reuters or AP reports it by the deadline. |
| KKR-20261025-44 | 95% | 2026-11-10 | military/conflict | Between 2026-10-26 and 2026-11-08, Saudi Arabia intercepts at least one further missile or drone launched from Yemen by Houthi forces. | The Saudi Ministry of Defense, the Saudi-led coalition, or at least two of Reuters, AP, AFP and Al Jazeera report Saudi air defenses intercepted a missile or drone launched from Yemen on a date between 2026-10-26 and 2026-11-08. |
| KKR-20261025-45 | 27% | 2026-11-10 | economics/markets | On at least one trading day between 2026-10-26 and 2026-11-06, the front-month NYMEX WTI crude futures contract settles at or above 115.00 dollars per barrel. Reference: 103.27 dollars per barrel on the packet date. | CME Group settlement prices for front-month WTI crude show a settle at or above 115.00 dollars on at least one trading day between 2026-10-26 and 2026-11-06. Reference: 103.27 on the packet date. |
| KKR-20261025-46 | 9% | 2026-11-02 | economics/markets | At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range above 3.75 to 4.00 percent. Reference: 3.75 to 4.00 percent, upper bound 4.00, in effect on the packet date. | The Federal Reserve statement released on 2026-10-28 announces an increase in the federal funds target range above 3.75 to 4.00 percent, and FRED series DFEDTARU shows an upper bound above 4.00 on 2026-10-29. |
| KKR-20261025-47 | 33% | 2026-11-02 | political | Luiz Inacio Lula da Silva receives more valid votes than Flavio Bolsonaro in the Brazilian presidential runoff held on 2026-10-25. | The Superior Electoral Court (TSE) results portal shows Lula with more valid votes than Flavio Bolsonaro in the runoff held on 2026-10-25, at 100 percent of sections counted. |
| KKR-20261025-48 | 83% | 2026-12-04 | political | In the US general election held on 2026-11-03, Democratic candidates win at least 218 of the 435 seats in the US House of Representatives, as called by the Associated Press by 2026-12-04. | Associated Press race calls, cross-checked against the Clerk of the House, show Democratic candidates winning at least 218 of 435 House seats in the election held on 2026-11-03, as of 2026-12-04. |
| KKR-20261025-49 | 37% | 2026-11-10 | disaster | The USGS earthquake catalog lists at least one earthquake of magnitude 7.0 or greater anywhere in the world with an origin time between 2026-10-26 and 2026-11-08 inclusive, UTC. | A query of the USGS ComCat FDSN event API for magnitude 7.0 or greater, with origin time between 2026-10-26 and 2026-11-08 UTC inclusive, returns at least one event when queried on or after 2026-11-10. |
| KKR-20261025-50 | 35% | 2026-11-10 | disaster | Between 2026-10-26 and 2026-11-08, a country that has not previously reported a locally detected Bundibugyo Ebola case, other than the Democratic Republic of the Congo, Uganda, Kenya and Nigeria, confirms its first such case; medical evacuations do not count. | WHO, Africa CDC or a national health ministry confirms a Bundibugyo virus case detected locally, not by medical evacuation, in a country with no earlier locally detected case, with confirmation dated between 2026-10-26 and 2026-11-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-26 and 2026-11-08, SpaceX, Elon Musk, US officials or Ukrainian officials publicly state that Starlink or Starshield service" → REJECTED: resolution offers alternative VENUES joined by 'or' (… statement by spacex, elon musk, us officials | or | ukrainian officials, reported by reuters or a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "In the Israeli Knesset election held on 2026-10-27, the Likud, Shas, United Torah Judaism, Religious Zionism and Otzma Yehudit lists togethe" → REJECTED: cited items name Morocco; the claim is about Israel — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4956 issued all-time across 21 forecaster arms · 3604 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 222 issued · 219 open · 3 resolved · 3 hits / 0 misses · **Brier 0.009** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1743 | 1360 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 110 | 109 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 115 | 115 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 437 | 356 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 267 | 256 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 222 | 219 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*