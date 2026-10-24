**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241835Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-24_1512.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261024-45 | 42% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 US House of Representatives seats in the general election held on 2026-11-03. | TRUE if Associated Press race calls published by 2026-12-18 award at least 218 House seats to Democratic candidates in the general election held on 2026-11-03; otherwise FALSE. |
| KKR-20261024-46 | 42% | 2027-01-04 | political | The functions of the person serving as French Prime Minister on 2026-10-24 are formally ended by presidential decree, following resignation or a successful censure motion, between 2026-10-26 and 2026-12-31. | TRUE if the Journal Officiel publishes a decree dated between 2026-10-26 and 2026-12-31 ending the functions of the person who was French Prime Minister on 2026-10-24. |
| KKR-20261024-47 | 66% | 2026-12-03 | military/conflict | US or Israeli forces strike at least one target on Iranian land territory between 2026-10-26 and 2026-11-30. | TRUE if a US or Israeli strike on a target on Iranian land territory, occurring between 2026-10-26 and 2026-11-30, is acknowledged by the striking government or reported as fact by both Reuters and AP. |
| KKR-20261024-48 | 66% | 2027-02-03 | military/conflict | A general Russia-Ukraine ceasefire covering the entire front line, with a stated duration of at least 30 days or no end date, takes effect between 2026-10-26 and 2027-01-31. | TRUE if both the Kremlin and the Ukrainian presidential office announce a full-front ceasefire lasting at least 30 days or open-ended that takes effect between 2026-10-26 and 2027-01-31; holiday, energy-only or maritime truces excluded. |
| KKR-20261024-49 | 60% | 2026-11-16 | economics/markets | The Federal Register publishes a presidential executive order addressing mortgage insurance or mortgage refinancing costs between 2026-10-26 and 2026-11-13. | TRUE if the Federal Register lists an executive order whose text addresses mortgage insurance or mortgage refinancing costs, with a publication date between 2026-10-26 and 2026-11-13. |
| KKR-20261024-50 | 46% | 2026-12-14 | cyber | CISA adds at least one PHP vulnerability, with vendorProject PHP or PHP Group, to its Known Exploited Vulnerabilities catalog between 2026-10-24 and 2026-12-11. | TRUE if the CISA KEV catalog JSON contains an entry with vendorProject PHP or PHP Group whose dateAdded value falls between 2026-10-24 and 2026-12-11 inclusive. |
| KKR-20261024-51 | 42% | 2026-11-10 | disaster | An earthquake of USGS preferred magnitude 6.0 or greater occurs within 100 km of the epicenter of USGS event us6000u4j2 (M6.9 Vanuatu, 2026-10-24) between 2026-10-25 and 2026-11-07 UTC. | TRUE if a USGS ComCat search returns an event of preferred magnitude 6.0 or greater within 100 km of the us6000u4j2 epicenter with origin time between 2026-10-25 and 2026-11-07 UTC inclusive. |
| KKR-20261024-52 | 42% | 2026-11-02 | disaster | The UK Met Office issues a red weather warning for wind or rain associated with Storm Boelo, for any part of the UK, between 2026-10-24 and 2026-10-31. | TRUE if the Met Office issues any red National Severe Weather Warning for wind or rain linked to Storm Boelo between 2026-10-24 and 2026-10-31, per its warnings archive or official statements. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The ICE Brent front-month (February 2027) futures contract settles below 100.00 USD per barrel on 2026-12-18. Reference: 111.70 USD on the p" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Islamic State claims responsibility for the gun attack on a church funeral in Jordan reported on 2026-10-23 and 2026-10-24, with the cla" → REJECTED: resolution offers alternative VENUES joined by 'or' (…rt that the islamic state, via amaq, al-naba, | or | another official is outlet, claimed the jorda…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4888 issued all-time across 21 forecaster arms · 3536 open (681 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1718 issued · 1335 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1718 | 1335 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 108 | 107 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 109 | 109 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 247 | 160 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 429 | 348 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 205 | 202 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*