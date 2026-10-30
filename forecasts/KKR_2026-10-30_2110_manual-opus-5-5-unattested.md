**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 302110Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-30_1513.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261030-26 | 40% | 2026-12-01 | cyber | CISA adds the actively exploited Drupal Commerce Core authorization bypass CVE-2026-118539 to its Known Exploited Vulnerabilities catalog between 2026-10-30 and 2026-11-27. | The CISA KEV catalog carries an entry for CVE-2026-118539 with a dateAdded value between 2026-10-30 and 2026-11-27 inclusive. |
| KKR-20261030-27 | 10% | 2027-02-02 | cyber | CISA adds the Linux kernel TCP use-after-free CVE-2026-98432, scored 9.8 by the kernel CNA, to its Known Exploited Vulnerabilities catalog between 2026-10-30 and 2027-01-29. | The CISA KEV catalog carries an entry for CVE-2026-98432 with a dateAdded value between 2026-10-30 and 2027-01-29 inclusive. |
| KKR-20261030-28 | 75% | 2026-12-14 | economics/markets | The FOMC raises the federal funds target range at its scheduled 2026-12-08 to 2026-12-09 meeting. Reference: 4.00 percent upper limit on the packet date. | FRED series DFEDTARU shows a value above 4.00 for 2026-12-10, reflecting a hike decided at the 2026-12-08 to 2026-12-09 FOMC meeting. Reference: 4.00 percent on the packet date. |
| KKR-20261030-29 | 62% | 2026-12-08 | political | Mary Peltola wins the Alaska US Senate election held on 2026-11-03, per official results published between 2026-11-03 and 2026-12-04. | Alaska Division of Elections results for the 2026-11-03 US Senate race, published between 2026-11-03 and 2026-12-04 after any ranked-choice tabulation, show Mary Peltola as the winner. |
| KKR-20261030-30 | 35% | 2027-02-03 | political | A new Israeli government wins a Knesset confidence vote between 2026-11-05 and 2027-01-31, following the 2026-10-27 election. | The Knesset approves a new government in a confidence vote held between 2026-11-05 and 2027-01-31, as recorded on the official Knesset website. |
| KKR-20261030-31 | 8% | 2026-12-02 | political | Oscar Puente leaves office as Spanish Minister of Transport and Sustainable Mobility, by resignation or dismissal, between 2026-10-31 and 2026-11-28, before the 2026-11-29 general election. | The Boletin Oficial del Estado publishes a royal decree, dated between 2026-10-31 and 2026-11-28, ending the appointment of Oscar Puente as Minister of Transport and Sustainable Mobility. |
| KKR-20261030-32 | 10% | 2027-01-05 | disaster | An earthquake of magnitude 6.0 or greater occurs within 300 km of the epicenter of the M6.4 event southeast of Easter Island, USGS id us7000ttxz, between 2026-10-31 and 2026-12-31. | The USGS ComCat catalog lists at least one event of magnitude 6.0 or greater, epicenter within 300 km of us7000ttxz, with origin time between 2026-10-31 and 2026-12-31 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FBI publicly attributes the 2026-10-29 theft of roughly 6.3 billion dollars from Binance to North Korea between 2026-10-30 and 2026-12-3" → REJECTED: resolution offers alternative VENUES joined by 'or' (…an fbi press release, public statement | or | ic3 public service announcement dated…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "US forces strike targets on Iranian land territory between 2026-11-04 and 2026-12-15, after the 2026-11-03 US midterm elections." → REJECTED: resolution offers alternative VENUES joined by 'or' (… a white house, pentagon or centcom statement | or | by at least two of reuters, ap   bbc…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Brent crude spot price is below 100.00 dollars per barrel on 2026-12-14. Reference: 113.39 dollars on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5183 issued all-time across 22 forecaster arms · 3461 open (590 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 304 issued · 290 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 29 | 29 | 0 | — | — | not computed | — | — | — |
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
| manual/opus-5.5/unattested | 304 | 290 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*