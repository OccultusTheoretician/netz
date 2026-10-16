**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162053Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: manual/sonnet-5.5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-43 | 84% | 2026-11-02 | cyber | CISA adds the BeyondTrust zero-day reported as exploited since August 2026 to its Known Exploited Vulnerabilities catalog, with a BeyondTrust entry carrying a dateAdded value between 2026-10-16 and 2026-10-30. | The CISA KEV catalog carries at least one entry with vendorProject BeyondTrust and a dateAdded value from 2026-10-16 through 2026-10-30 inclusive, as retrieved on or after the deadline. |
| KKR-20261016-44 | 30% | 2026-11-17 | cyber | CISA adds the Collabora Online flaw reported as exploited to backdoor Nextcloud servers to its Known Exploited Vulnerabilities catalog, with a Collabora or Nextcloud entry carrying a dateAdded value between 2026-10-16 and 2026-11-13. | The CISA KEV catalog carries at least one entry whose vendorProject or product field names Collabora or Nextcloud, with a dateAdded value from 2026-10-16 through 2026-11-13 inclusive, as retrieved on or after the deadline. |
| KKR-20261016-45 | 30% | 2026-11-17 | economics/markets | The Nasdaq Composite records a daily close at or below 25,000.00 on at least one trading day between 2026-10-19 and 2026-11-13. Reference: 26,438.29 in the packet Market Snapshot dated 2026-10-16. | Official Nasdaq daily closes (FRED series NASDAQCOM) show at least one close at or below 25,000.00 on a trading day from 2026-10-19 through 2026-11-13. Reference: 26,438.29 on the packet date 2026-10-16. |
| KKR-20261016-46 | 27% | 2026-11-02 | disaster | At least one earthquake of magnitude 6.0 or greater strikes within 300 km of the epicenter of the magnitude 7.7 Panama mainshock (USGS event us6000u18k) between 2026-10-17 and 2026-10-30. | The USGS ComCat catalog lists at least one earthquake with magnitude 6.0 or greater, origin time between 2026-10-17 and 2026-10-30 UTC, within 300 km of the epicenter of USGS event us6000u18k. |
| KKR-20261016-47 | 24% | 2026-11-04 | disaster | A California wildfire that starts between 2026-10-17 and 2026-10-30 reaches at least 10,000 acres burned by 2026-11-04. | CAL FIRE incident records or the NIFC WFIGS interagency fire perimeters list a California wildfire with start date from 2026-10-17 through 2026-10-30 and reported size of at least 10,000 acres by the deadline. |
| KKR-20261016-48 | 94% | 2026-11-02 | military/conflict | The Houthi movement launches at least one missile or drone attack on Saudi Arabian territory between 2026-10-17 and 2026-10-30, claimed by the Houthis or reported by Saudi Arabia or its military coalition. | Reuters or AP reports a Houthi-claimed or Saudi-reported missile or drone attack on Saudi territory with an incident date from 2026-10-17 through 2026-10-30. |
| KKR-20261016-49 | 37% | 2026-12-08 | military/conflict | The United States conducts at least one military strike on a target located on Iranian land or island territory between 2026-10-17 and 2026-12-04. | CENTCOM, the Pentagon, or the White House confirms, or Reuters and AP both report citing US officials, a US air or missile strike on Iranian land or island territory dated 2026-10-17 through 2026-12-04. |
| KKR-20261016-50 | 45% | 2026-11-10 | political | Democrat James Talarico defeats Republican Ken Paxton in the Texas US Senate election held on 2026-11-03. | Associated Press race call or Texas Secretary of State unofficial election-night totals show Talarico with the most votes in the 2026-11-03 Texas US Senate election as of the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled 2026-10-27 to 2026-10-28 meeting, with the decision released on 2026-10-28. " → REJECTED: the resolution names a different subject than the statement — the claim is about FOMC, Reference and the resolution settles on Federal, Reserve. A row whose resolution checks a different fact can be scored correct while being wrong
- "Edi Rama ceases to be Prime Minister of Albania, by resignation or removal, between 2026-10-17 and 2026-11-13." → REJECTED: resolution offers alternative VENUES joined by 'or' (…omeone other than edi rama as prime minister, | or | reuters and ap report his resignation or remo…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4293 issued all-time across 21 forecaster arms · 3182 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 146 issued · 146 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1509 | 1213 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*