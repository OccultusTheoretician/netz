**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061709Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-06_1614.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261106-16 | 88% | 2026-11-18 | disaster | The Central Pollution Control Board daily bulletin reports a 24-hour average air quality index of 401 or higher for Delhi on at least one day between 2026-11-07 and 2026-11-15. | At least one CPCB daily AQI bulletin dated between 2026-11-07 and 2026-11-15 lists a 24-hour average AQI of 401 or higher, the severe category, for Delhi. |
| KKR-20261106-17 | 42% | 2026-11-25 | political | Donald Trump, Xi Jinping and Vladimir Putin hold a dedicated in-person three-leader meeting between 2026-11-14 and 2026-11-22. | An official readout from the White House, the Kremlin or the Chinese Foreign Ministry confirms a dedicated three-leader meeting of Trump, Xi and Putin, separate from any multilateral summit session, held in person between 2026-11-14 and 2026-11-22. |
| KKR-20261106-18 | 65% | 2026-12-08 | political | The Alaska Division of Elections publishes a final-round ranked-choice tabulation or certified result between 2026-11-18 and 2026-12-04 showing Mary Peltola defeating incumbent Dan Sullivan for US Senate. | Results published by the Alaska Division of Elections between 2026-11-18 and 2026-12-04, either the final-round ranked-choice tabulation or the certified result, show Mary Peltola with more votes than incumbent Dan Sullivan for US Senate. |
| KKR-20261106-19 | 47% | 2026-12-08 | crime/security | Authorities in at least one European country announce the arrest or charging of a suspect for sending bomb threats against European flights or airports, with the announcement made between 2026-11-07 and 2026-12-05. | European police or prosecutors announce, between 2026-11-07 and 2026-12-05, the arrest or charging of a person suspected of sending bomb threats made since 2026-11-01 against European flights or airports, per two of Reuters, AP, AFP, BBC. |
| KKR-20261106-20 | 24% | 2026-12-14 | economics/markets | ICE Brent crude front-month futures settle below 90.00 dollars per barrel on 2026-12-11. Reference: 97.09 on the packet date. | The ICE Brent front-month futures settlement price for 2026-12-11 is below 90.00 dollars per barrel. Reference: 97.09 on the packet date. |
| KKR-20261106-21 | 33% | 2026-12-21 | economics/markets | The S&P 500 closes below 7,000.00 on at least one trading day between 2026-11-09 and 2026-12-18. Reference: 7,405.12 on the packet date. | At least one official S&P 500 daily close between 2026-11-09 and 2026-12-18 inclusive, per S&P Dow Jones Indices or FRED series SP500, is below 7,000.00. Reference: 7,405.12 on the packet date. |
| KKR-20261106-22 | 22% | 2026-12-23 | military/conflict | The United States and Iran both officially confirm a concluded agreement that includes reopening the Strait of Hormuz to commercial shipping, announced between 2026-11-09 and 2026-12-20. | Official statements from both the US and Iranian governments, reported by at least two of Reuters, AP and AFP, confirm a concluded agreement that includes reopening the Strait of Hormuz, announced between 2026-11-09 and 2026-12-20. |
| KKR-20261106-23 | 94% | 2027-01-19 | political | The US House of Representatives elects Hakeem Jeffries as Speaker in a roll call vote held between 2027-01-03 and 2027-01-15. | The Clerk of the House roll call for election of the Speaker of the 120th Congress, held between 2027-01-03 and 2027-01-15, records Hakeem Jeffries as elected Speaker. |
| KKR-20261106-24 | 18% | 2027-02-02 | cyber | CISA adds an OpenSSH vulnerability to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-11-07 and 2027-01-29. | The CISA KEV catalog carries at least one entry whose vendorProject or product field names OpenSSH and whose dateAdded value falls between 2026-11-07 and 2027-01-29 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Open Market Committee raises the target range for the federal funds rate at its scheduled meeting concluding on 2026-12-09." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5400 issued all-time across 22 forecaster arms · 3678 open (1268 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 494 issued · 379 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 87 | 87 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 179 | 162 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 179 | 177 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 160 | 127 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 494 | 379 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 343 | 329 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*