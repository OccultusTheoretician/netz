**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121841Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: control/baserate · 8 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-55 | 66% | 2026-10-29 | military/conflict | Between 2026-10-13 and 2026-10-26, Saudi Arabia carries out at least one air or missile strike on Houthi-controlled territory in Yemen. | True if a Saudi official acknowledges a strike on Houthi-controlled Yemen dated 2026-10-13 to 2026-10-26, or at least two of Reuters, AP, AFP and BBC attribute such a strike to Saudi forces. |
| KKR-20261012-56 | 66% | 2026-10-29 | military/conflict | Between 2026-10-13 and 2026-10-26, the Ukrainian Air Force reports a single overnight Russian attack of at least 400 drones and missiles combined. | True if a Ukrainian Air Force report covering one night within 2026-10-13 to 2026-10-26 gives a combined drone (including decoys) and missile launch total of 400 or more, relayed by Reuters, AP or Kyiv Independent. |
| KKR-20261012-57 | 66% | 2026-10-29 | military/conflict | Between 2026-10-13 and 2026-10-26, a merchant vessel is struck by a missile, drone, mine or projectile in the Strait of Hormuz, Gulf of Oman or Persian Gulf. | True if UKMTO or US Central Command publishes a notice dated 2026-10-13 to 2026-10-26 reporting a merchant vessel struck by a missile, drone, mine or projectile in the Strait of Hormuz, Gulf of Oman or Persian Gulf. |
| KKR-20261012-58 | 42% | 2026-10-29 | political | Between 2026-10-13 and 2026-10-26, Donald Trump and Vladimir Putin hold a direct phone call or in-person meeting that the Kremlin and the White House both confirm. | True if the Kremlin (spokesperson or kremlin.ru) and the White House or Trump both confirm a Trump-Putin call or meeting dated 2026-10-13 to 2026-10-26. |
| KKR-20261012-59 | 60% | 2026-11-18 | economics/markets | ICE front-month Brent crude settles at or above 120.00 USD per barrel on at least one trading day between 2026-10-13 and 2026-11-13. Reference: 106.95 USD per barrel on the packet date 2026-10-12. | True if any ICE front-month Brent futures daily settlement from 2026-10-13 through 2026-11-13 is 120.00 USD per barrel or higher, per ICE settlement data. Reference: 106.95 USD per barrel on the packet date 2026-10-12. |
| KKR-20261012-60 | 60% | 2026-11-18 | economics/markets | The US 10-year Treasury yield closes at or above 5.50 percent on at least one business day between 2026-10-13 and 2026-11-13. Reference: 5.24 percent on the packet date 2026-10-12. | True if FRED series DGS10 shows a value of 5.50 or higher for any date from 2026-10-13 through 2026-11-13. Reference: 5.24 percent on the packet date 2026-10-12. |
| KKR-20261012-61 | 45% | 2026-10-29 | cyber | Between 2026-10-13 and 2026-10-26, CISA adds at least one SonicWall Secure Mobile Access (SMA) vulnerability to its Known Exploited Vulnerabilities catalog. | True if the CISA KEV JSON catalog carries at least one entry with vendorProject SonicWall, a product value containing SMA, and dateAdded from 2026-10-13 through 2026-10-26 inclusive. |
| KKR-20261012-62 | 44% | 2026-10-29 | disaster | Between 2026-10-13 and 2026-10-26, USGS records an earthquake of magnitude 6.5 or greater within 300 km of the epicenter of USGS event us6000u18k, the magnitude 7.7 Panama earthquake. | True if the USGS ComCat catalog lists an earthquake of magnitude 6.5 or greater with origin time from 2026-10-13 00:00 UTC through 2026-10-26 23:59 UTC, within 300 km of event us6000u18k. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-13 and 2026-11-09, a federal criminal charge naming Representative Ilhan Omar as a defendant is filed in a US court." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a us federal court docket | or | department of justice press release shows an …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3996 issued all-time across 21 forecaster arms · 2968 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1415 issued · 1141 open · 242 resolved · 152 hits / 90 misses · **Brier 0.316** against its own base rate 62.8% (climatological 0.234) · **skill -0.354**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1415 | 1141 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 328 | 272 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*