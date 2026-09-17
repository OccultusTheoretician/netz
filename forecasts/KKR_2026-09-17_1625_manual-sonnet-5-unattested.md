**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171625Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-17_1518.md · forecaster: manual/sonnet-5/unattested · 10 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260917-55 | 25% | 2026-10-19 | military/conflict | Between 2026-09-17 and 2026-10-15, the United States and Iran announce a ceasefire, truce, or formal end to hostilities, confirmed by a government statement or by at least two of Reuters, AP, or AFP. | TRUE if Reuters, AP, or AFP report a US-Iran ceasefire, truce, or hostilities-end announcement dated between 2026-09-17 and 2026-10-15; adjudicated 2026-10-19. FALSE otherwise. |
| KKR-20260917-56 | 30% | 2026-10-12 | military/conflict | Between 2026-09-17 and 2026-10-08, India or Pakistan's government issues a formal diplomatic protest or demarche over this week's India-Pakistan naval ship collision, confirmed by a government statement or by Reuters, AP, or AFP. | TRUE if India's MEA or Pakistan's Foreign Office issues a demarche or formal protest over the collision, reported by Reuters, AP, or AFP, dated 2026-09-17 to 2026-10-08; adjudicated 2026-10-12. FALSE otherwise. |
| KKR-20260917-57 | 30% | 2026-11-02 | economics/markets | WTI crude oil settles below 95.00 dollars per barrel on any NYMEX trading day between 2026-10-01 and 2026-10-30. Reference: 101.09 dollars per barrel on the packet date, 2026-09-17. | TRUE if the CME/NYMEX WTI front-month settlement price closes below 95.00 dollars on any trading day from 2026-10-01 to 2026-10-30, per CME Group data; adjudicated 2026-11-02. FALSE otherwise. |
| KKR-20260917-58 | 45% | 2026-11-16 | economics/markets | Bitcoin trades above 90,000 dollars on any day between 2026-09-17 and 2026-11-14, per Coinbase or Kraken spot price data. Reference: 76,270 dollars on the packet date, 2026-09-17. | TRUE if Coinbase or Kraken spot BTC-USD trades above 90,000 dollars on any day from 2026-09-17 to 2026-11-14; adjudicated 2026-11-16. FALSE otherwise. |
| KKR-20260917-59 | 20% | 2026-10-12 | cyber | Between 2026-09-17 and 2026-10-08, CISA publishes a cybersecurity advisory naming the China-aligned group FamousSparrow or the SparroWocky backdoor, confirmed on cisa.gov. | TRUE if a CISA advisory on cisa.gov names FamousSparrow or SparroWocky, published between 2026-09-17 and 2026-10-08; adjudicated 2026-10-12. FALSE otherwise. |
| KKR-20260917-60 | 60% | 2026-10-12 | cyber | Between 2026-09-17 and 2026-10-08, Microsoft confirms a fix or re-release for the Windows 11 KB5124008 domain-trust break, via its Release Health dashboard or a Support advisory. | TRUE if Microsoft's Release Health dashboard or Support site confirms a fix or re-release for the KB5124008 domain-trust issue between 2026-09-17 and 2026-10-08; adjudicated 2026-10-12. FALSE otherwise. |
| KKR-20260917-61 | 65% | 2026-10-19 | political | Between 2026-09-17 and 2026-10-15, the Riksdag holds a formal vote confirming a new Swedish prime minister following Ulf Kristersson's resignation, recorded in the Riksdag's own vote record. | TRUE if the Riksdag's vote record shows a confirmation vote for a new prime minister dated 2026-09-17 to 2026-10-15; adjudicated 2026-10-19. FALSE otherwise. |
| KKR-20260917-62 | 25% | 2026-10-12 | political | Between 2026-09-17 and 2026-10-08, Meta publicly confirms compliance with the Oversight Board ruling on deepfake removal, via a Meta Newsroom post or the Oversight Board's implementation tracker. | TRUE if Meta Newsroom or the Oversight Board implementation tracker shows a confirmed compliance update on the deepfake ruling, dated 2026-09-17 to 2026-10-08; adjudicated 2026-10-12. FALSE otherwise. |
| KKR-20260917-63 | 20% | 2026-10-26 | crime/security | Between 2026-09-17 and 2026-10-22, the US House refers the Leon Black contempt matter to the Department of Justice, or holds a follow-up roll-call vote on enforcement, recorded on congress.gov. | TRUE if congress.gov records a DOJ referral or a follow-up House roll-call vote on the Leon Black matter, dated 2026-09-17 to 2026-10-22; adjudicated 2026-10-26. FALSE otherwise. |
| KKR-20260917-64 | 35% | 2026-10-05 | disaster | Between 2026-09-17 and 2026-10-01, an aftershock of magnitude 5.0 or greater occurs within 200 km of the M6.5 earthquake 165 km west of Nikolski, Alaska (USGS event us7000ti1p), per the USGS Earthquake Catalog. | TRUE if the USGS Earthquake Catalog records an M5.0-or-greater event within 200 km of the Nikolski mainshock, dated 2026-09-17 to 2026-10-01; adjudicated 2026-10-05. FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2429 issued all-time across 16 forecaster arms · 1963 open (82 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 262 issued · 214 open · 43 resolved · 21 hits / 22 misses · **Brier 0.207** against its own base rate 48.8% (climatological 0.250) · **skill +0.172**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 825 | 740 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 286 | 136 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 81 | 76 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 131 | 121 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 283 | 266 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 262 | 214 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*