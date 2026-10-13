**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131625Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: manual/opus-5.5/unattested · 10 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-62 | 6% | 2027-01-05 | military/conflict | A general ceasefire covering the entire Russia-Ukraine front line, agreed by both governments, takes effect between 2026-10-14 and 2026-12-31. | Per Reuters or AP, both the Kremlin and the Ukrainian presidential office confirm a general ceasefire across the full front line taking effect between 2026-10-14 and 2026-12-31; partial, energy-only, maritime, or holiday truces do not count. |
| KKR-20261013-63 | 30% | 2027-01-05 | military/conflict | Iranian forces board a foreign-flagged merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman and divert it toward Iran between 2026-10-14 and 2026-12-31. | Between 2026-10-14 and 2026-12-31, Iranian forces board a foreign-flagged merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman and divert it toward Iran, confirmed by UKMTO, flag state, or operator, per Reuters or AP. |
| KKR-20261013-64 | 32% | 2026-12-22 | economics/markets | The 10-year US Treasury constant maturity yield is below 5.00 percent for observation date 2026-12-18. Reference: 5.21 percent on the packet date. | FRED series DGS10 shows a value below 5.00 for observation date 2026-12-18. Reference: 5.21 percent on the packet date. |
| KKR-20261013-65 | 25% | 2027-01-05 | economics/markets | The Nasdaq Composite closes at or below 24,471.31, ten percent under the packet reference, on at least one trading day between 2026-10-14 and 2026-12-31. Reference: 27,190.34 on the packet date. | FRED series NASDAQCOM records at least one daily close at or below 24,471.31 between 2026-10-14 and 2026-12-31. Reference: 27,190.34 on the packet date. |
| KKR-20261013-66 | 18% | 2027-01-05 | cyber | CISA adds at least one GitLab vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-14 and 2026-12-31, following the GitLab patch for a CVSS 10.0 flaw. | The CISA KEV catalog carries at least one entry with vendorProject GitLab and a dateAdded value between 2026-10-14 and 2026-12-31. |
| KKR-20261013-67 | 85% | 2026-11-17 | political | Kimberly Guilfoyle resigns, is recalled, or is removed as US Ambassador to Greece between 2026-10-13 and 2026-11-13. | The White House, State Department, or Guilfoyle announces or confirms her resignation, recall, or removal as US Ambassador to Greece between 2026-10-13 and 2026-11-13, per AP or Reuters. |
| KKR-20261013-68 | 75% | 2026-12-08 | political | In the US general election held on 2026-11-03, Democratic candidates win at least 218 of 435 House seats, as called by AP between 2026-11-03 and 2026-12-04. | AP race calls made between 2026-11-03 and 2026-12-04 award at least 218 of 435 US House seats from the 2026-11-03 general election to Democratic candidates. |
| KKR-20261013-69 | 10% | 2026-12-03 | political | Bulgaria declares at least one Russian diplomat persona non grata or orders a Russian diplomat expelled between 2026-10-14 and 2026-11-30. | The Bulgarian government declares at least one Russian diplomat persona non grata or orders their expulsion between 2026-10-14 and 2026-11-30, per Reuters, AP, or the Bulgarian state news agency BTA. |
| KKR-20261013-70 | 70% | 2027-02-02 | crime/security | In the federal hate crimes trial over the 2022 Buffalo supermarket shooting, Payton Gendron is convicted on at least one count, by jury verdict or guilty plea, between 2026-10-13 and 2027-01-29. | The docket in United States v. Gendron, US District Court for the Western District of New York, records a guilty jury verdict or guilty plea on at least one count between 2026-10-13 and 2027-01-29. |
| KKR-20261013-71 | 55% | 2026-11-17 | disaster | At least one earthquake of magnitude 6.0 or greater strikes within 250 km of the epicenter of the M7.7 Panama earthquake (USGS event us6000u18k) between 2026-10-14 and 2026-11-13 UTC. | The USGS ComCat catalog lists at least one event of magnitude 6.0 or greater within 250 km of the us6000u18k epicenter with origin time between 2026-10-14 and 2026-11-13 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4085 issued all-time across 21 forecaster arms · 2974 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 168 issued · 163 open · 5 resolved · 3 hits / 2 misses · **Brier 0.440** against its own base rate 60.0% (climatological 0.240) · **skill -0.835** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1442 | 1146 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*