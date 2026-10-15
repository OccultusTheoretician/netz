**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151615Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-15_1512.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261015-29 | 65% | 2026-11-04 | military/conflict | Between 2026-10-16 and 2026-10-31 the Ukrainian General Staff publicly claims a strike on at least one oil refinery inside the Russian Federation, and a Russian regional governor or the Russian Ministry of Defence acknowledges a drone attack on, or fire at, that refinery or its locality on the same date. | True if, for a date between 2026-10-16 and 2026-10-31, the Ukrainian General Staff claims a strike on a refinery inside Russia and a Russian governor or MoD acknowledges a drone attack or fire at that refinery or its locality. |
| KKR-20261015-30 | 30% | 2026-11-18 | military/conflict | US Central Command or the US Department of Defense publicly confirms a US military strike on a target located inside the territory of Iran that occurred between 2026-10-16 and 2026-11-15. | True if a CENTCOM or Department of Defense statement, press release, or official social media post confirms a US strike on Iranian territory dated between 2026-10-16 and 2026-11-15. Targets at sea do not count. |
| KKR-20261015-31 | 22% | 2027-01-05 | economics/markets | The 10-year US Treasury constant maturity yield, FRED series DGS10, prints 5.50 percent or higher on at least one observation date between 2026-10-16 and 2026-12-31. Reference: 5.05 percent on the packet date, 2026-10-15. | True if the FRED DGS10 series shows any daily value at or above 5.50 for an observation date from 2026-10-16 through 2026-12-31 inclusive. Reference level at seal: 5.05 percent. |
| KKR-20261015-32 | 50% | 2026-12-02 | economics/markets | The Nasdaq Composite index closes at or below 25,281.14, which is 5 percent below the 2026-10-15 packet reference level of 26,611.73, on at least one trading day between 2026-10-16 and 2026-11-30. | True if the official Nasdaq Composite closing value, per Nasdaq or FRED series NASDAQCOM, is 25,281.14 or lower on any trading day from 2026-10-16 through 2026-11-30. Reference at seal: 26,611.73. |
| KKR-20261015-33 | 40% | 2026-12-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry with a dateAdded between 2026-10-16 and 2026-11-30 whose vendorProject or product field names Drupal, Next.js, or NGINX. | True if the CISA KEV JSON feed contains at least one entry with dateAdded from 2026-10-16 through 2026-11-30 whose vendorProject or product value contains Drupal, Next.js, or NGINX (case-insensitive). |
| KKR-20261015-34 | 50% | 2026-11-18 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 6.0 or greater with an epicenter within 200 km of the epicenter of USGS event us6000u18k (the M7.7 Pitaloza Arriba, Panama event) and an origin time between 2026-10-16 and 2026-11-15 UTC. | True if the USGS ComCat search returns at least one event, magnitude 6.0 or higher, origin time 2026-10-16 00:00 UTC to 2026-11-15 23:59 UTC, within 200 km of the us6000u18k epicenter. |
| KKR-20261015-35 | 70% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03. | True if, as of the deadline, Associated Press race calls or state-certified results show Democratic candidates winning at least 218 US House seats in the 2026-11-03 general election. |
| KKR-20261015-36 | 10% | 2026-12-03 | political | Edi Rama submits his resignation as Prime Minister of Albania, is dismissed, or loses a parliamentary no-confidence vote on a date between 2026-10-16 and 2026-11-30. | True if Rama submits his resignation, is dismissed, or loses a parliamentary no-confidence vote on a date between 2026-10-16 and 2026-11-30, as reported by two of Reuters, AP, AFP. |
| KKR-20261015-37 | 40% | 2027-01-05 | crime/security | The death sentence of Nidal Hasan, the 2009 Fort Hood shooter, is carried out on a date between 2026-10-16 and 2026-12-31, as confirmed by the US Army or the US Department of Defense. | True if the US Army or Department of Defense publicly confirms that Nidal Hasan was executed on a date between 2026-10-16 and 2026-12-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA issues at least one new Emergency Directive, published on the CISA directives page with an issue date between 2026-10-16 and 2026-11-30" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4200 issued all-time across 21 forecaster arms · 3089 open (481 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 354 issued · 296 open · 50 resolved · 34 hits / 16 misses · **Brier 0.248** against its own base rate 68.0% (climatological 0.218) · **skill -0.140**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1475 | 1179 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 429 | 206 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 65 | 65 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 60 | 60 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 63 | 63 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 174 | 169 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*