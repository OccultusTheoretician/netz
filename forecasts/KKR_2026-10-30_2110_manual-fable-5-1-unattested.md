**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 302110Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-30_1513.md · forecaster: manual/fable-5.1/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261030-14 | 72% | 2026-12-18 | political | Democratic candidates win a majority of US House seats in the 2026-11-03 midterm elections, with the Associated Press having called at least 218 of 435 seats for Democrats by 2026-12-15. | TRUE if Associated Press race calls as of 2026-12-15 show Democratic candidates winning at least 218 of 435 US House seats in the 2026-11-03 general election. FALSE if fewer than 218 are called for Democrats. |
| KKR-20261030-15 | 45% | 2026-12-01 | cyber | CISA adds a Drupal Commerce (Commerce Core) vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-30 and 2026-11-27. | TRUE if the CISA KEV JSON feed contains an entry whose vendorProject, product, or vulnerabilityName fields name Drupal and Commerce, with dateAdded between 2026-10-30 and 2026-11-27 inclusive. FALSE otherwise. |
| KKR-20261030-16 | 50% | 2026-12-08 | cyber | The FBI or the US Treasury Department publicly attributes the October 2026 Binance theft to North Korean state-sponsored actors in an official release dated between 2026-10-30 and 2026-12-04. | TRUE if an official release on fbi.gov, ic3.gov, or home.treasury.gov dated between 2026-10-30 and 2026-12-04 attributes the October 2026 Binance theft to North Korean (DPRK) actors such as Lazarus or TraderTraitor. FALSE otherwise. |
| KKR-20261030-17 | 20% | 2027-01-05 | political | The person serving as Minister of Transport and Sustainable Mobility of Spain on 2026-10-30 leaves that office, with a Real Decreto of cese dated between 2026-10-30 and 2026-12-31 published in the Boletin Oficial del Estado. | TRUE if the BOE (boe.es) carries a Real Decreto dated between 2026-10-30 and 2026-12-31 disposing the cese of the person who was Minister of Transport and Sustainable Mobility on 2026-10-30. FALSE otherwise. |
| KKR-20261030-18 | 10% | 2027-02-02 | crime/security | The Tennessee Supreme Court enters an order setting a new execution date for Christa Pike, with the order filed between 2026-10-30 and 2027-01-29. | TRUE if a Tennessee Supreme Court order filed between 2026-10-30 and 2027-01-29 sets an execution date for Christa Pike, as shown on tncourts.gov or reported by AP. FALSE otherwise. |
| KKR-20261030-19 | 30% | 2026-12-02 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 7.5 or greater anywhere in the world with origin time between 2026-11-01 and 2026-11-30 UTC. | TRUE if the USGS ComCat catalog (earthquake.usgs.gov), as listed on 2026-12-02, contains at least one event with magnitude 7.5 or greater and origin time between 2026-11-01 00:00 UTC and 2026-11-30 23:59 UTC. FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US Central Command or the US Department of War (Defense) officially acknowledges US military strikes on targets inside Iran conducted betwee" → REJECTED: resolution offers alternative VENUES joined by 'or' (…an official press release | or | on-record statement from us central command  …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new Israeli government wins a Knesset vote of confidence and is sworn in between 2026-10-30 and 2027-01-15." → REJECTED: resolution offers alternative VENUES joined by 'or' (…10-30 and 2027-01-15, per the knesset website | or | reuters, ap, or times of israel reporting…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The CME CF Bitcoin Reference Rate (BRR) prints below 65000 USD on at least one day between 2026-10-31 and 2026-11-30. Reference: 77510 USD p" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Nasdaq Composite closes below 24000 on at least one trading day between 2026-11-02 and 2026-12-31. Reference: 25587.46 packet quote on 2" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5170 issued all-time across 22 forecaster arms · 3448 open (590 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 473 issued · 358 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

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
| lmstudio/qwen36 | 143 | 126 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 141 | 139 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 135 | 102 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
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