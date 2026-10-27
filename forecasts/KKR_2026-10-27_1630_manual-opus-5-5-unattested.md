**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271630Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-27_1516.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261027-37 | 72% | 2026-11-18 | crime/security | The man serving a life sentence for murder whose escape from a Tennessee prison was reported on 2026-10-27 is apprehended, surrenders, or is confirmed dead between 2026-10-27 and 2026-11-16. | TRUE if Tennessee Department of Correction, TBI, or US Marshals officials announce that the life-sentenced inmate reported escaped from a Tennessee prison on 2026-10-27 was apprehended, surrendered, or found dead between 2026-10-27 and 2026-11-16; FALSE otherwise. |
| KKR-20261027-38 | 33% | 2026-12-02 | disaster | An earthquake of magnitude 6.0 or greater occurs on the Vanuatu arc, within latitude -21 to -13 and longitude 166 to 171, between 2026-10-28 and 2026-11-30 UTC. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater with epicenter in latitude -21 to -13 and longitude 166 to 171, origin time between 2026-10-28 and 2026-11-30 UTC; FALSE otherwise. |
| KKR-20261027-39 | 35% | 2026-12-14 | economics/markets | The FOMC lowers the federal funds target range at its scheduled meeting concluding on 2026-12-09. | TRUE if the FOMC statement issued on 2026-12-09 lowers the federal funds target range, confirmed by FRED series DFEDTARU for 2026-12-10 being below its 2026-12-08 value; FALSE otherwise. |
| KKR-20261027-40 | 75% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | TRUE if Associated Press race calls made between 2026-11-03 and 2026-12-16 credit Democratic candidates with at least 218 House seats from the 2026-11-03 election; FALSE otherwise. |
| KKR-20261027-41 | 42% | 2026-12-21 | economics/markets | ICE Brent front-month crude futures settle below 100.00 USD per barrel on 2026-12-18. Reference: 109.18 USD on the packet date. | TRUE if the ICE Brent front-month futures settlement price on 2026-12-18 is below 100.00 USD per barrel; FALSE if at or above 100.00. Reference: 109.18 USD on the packet date. |
| KKR-20261027-42 | 38% | 2027-01-04 | political | Following the 2026-10-27 Knesset election, a new Israeli government wins a Knesset confidence vote and is sworn in between 2026-10-28 and 2026-12-31. | TRUE if the Knesset approves a new government in a confidence vote held between 2026-10-28 and 2026-12-31, per the Knesset plenum record or two of Reuters, AP, Times of Israel; FALSE otherwise. |
| KKR-20261027-43 | 37% | 2027-01-04 | cyber | CISA adds the Brotli decompression flaw publicized as HTTP2Shell to the KEV catalog with a dateAdded value between 2026-10-27 and 2026-12-31. | TRUE if the CISA KEV catalog lists an entry naming Brotli in its vulnerabilityName or shortDescription with a dateAdded value between 2026-10-27 and 2026-12-31; FALSE otherwise. |
| KKR-20261027-44 | 70% | 2027-01-11 | disaster | The DRC Ebola outbreak reaches at least 15,000 cumulative cases, all classifications combined, in official data dated between 2026-10-28 and 2026-12-31. Reference: above 10,000 on the packet date. | TRUE if a WHO publication or official DRC health ministry update, with data dated between 2026-10-28 and 2026-12-31, reports at least 15,000 cumulative cases, all classifications combined, for the DRC Ebola outbreak; FALSE otherwise. |
| KKR-20261027-45 | 7% | 2027-02-03 | military/conflict | A front-wide Russia-Ukraine ceasefire, open-ended or at least 30 days long and announced by both governments, takes effect between 2026-10-28 and 2027-01-31. | TRUE if Kyiv and Moscow both officially announce a front-wide ceasefire, open-ended or at least 30 days long, taking effect between 2026-10-28 and 2027-01-31, per Reuters and AP; localized, energy-only or holiday truces excluded. |
| KKR-20261027-46 | 25% | 2027-02-03 | military/conflict | Israel or the United States carries out an officially acknowledged air, missile, or drone strike on targets inside Iran between 2026-10-28 and 2027-01-31. | TRUE if the Israeli or US government officially acknowledges an air, missile, or drone strike on targets inside Iran conducted between 2026-10-28 and 2027-01-31, as reported by two of Reuters, AP, AFP; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5070 issued all-time across 21 forecaster arms · 3348 open (400 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 286 issued · 272 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1778 | 1269 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 125 | 108 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 130 | 128 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 126 | 93 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 455 | 340 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
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