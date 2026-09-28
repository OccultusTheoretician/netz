**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-28_1516.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260928-01 | 32% | 2026-10-24 | military/conflict | At least one major military strike or drone attack will be confirmed in Kyiv, Ukraine, between 2026-10-15 and 2026-10-22, with casualties reported by at least two independent sources from hostile sides (RU, UA). | At least one report from a source in RU or UA, and one from the other side, confirms a military strike or drone attack in Kyiv during the window, with at least one casualty explicitly stated in both reports. |
| KKR-20260928-02 | 45% | 2026-11-10 | economics/markets | The S&P 500 will close below 7,500.00 on at least one trading day between 2026-11-01 and 2026-11-07, based on the prior-session close of 7,682.84 on 2026-09-28. | The S&P 500 closing price on any trading day between 2026-11-01 and 2026-11-07 is less than 7,500.00, as reported by CNBC Top News, MarketWatch, or Bloomberg. |
| KKR-20260928-03 | 38% | 2026-10-29 | disaster | A tropical cyclone named Hurricane Polo will make landfall in Mexico's Baja California Peninsula between 2026-10-20 and 2026-10-27, with a minimum wind speed of 111 mph (Category 3) as reported by the National Hurricane Center or BBC World. | The National Hurricane Center or BBC World reports that Hurricane Polo made landfall in Baja California Peninsula between 2026-10-20 and 2026-10-27 with sustained winds of at least 111 mph (Category 3). |
| KKR-20260928-04 | 30% | 2026-10-14 | political | Iran will publicly announce a new military or strategic initiative related to the Strait of Hormuz between 2026-10-05 and 2026-10-12, confirmed by at least two independent sources from hostile sides (AXIS, WEST). | At least two reports from sources in AXIS and WEST, including Al Jazeera, BBC World, or The Guardian, confirm Iran's announcement of a new military or strategic initiative related to the Strait of Hormuz between 2026-10-05 and 2026-10-12. |
| KKR-20260928-05 | 40% | 2026-11-25 | political | A political scandal involving a U.S. federal official or elected representative will be confirmed by two major news outlets (e.g., Guardian World, CNBC Top News, NPR News) between 2026-11-15 and 2026-11-22, resulting in a public resignation or indictment. | Two major news outlets (Guardian World, CNBC Top News, or NPR News) report that a U.S. federal official or elected representative resigned or was indicted due to a political scandal between 2026-11-15 and 2026-11-22. |
| KKR-20260928-06 | 22% | 2026-10-14 | disaster | A major earthquake with magnitude 6.5 or higher will be recorded by the USGS in the Pacific Northwest region (Washington, Oregon, or Northern California) between 2026-10-05 and 2026-10-12, confirmed by a USGS significant quake alert. | The USGS Significant Quakes feed reports an earthquake with magnitude 6.5 or higher in the Pacific Northwest (Washington, Oregon, or Northern California) between 2026-10-05 and 2026-10-12. |
| KKR-20260928-07 | 27% | 2026-10-14 | crime/security | A terrorist attack involving explosives will be confirmed in the UK near a U.S.-run air base, with at least one casualty, between 2026-10-05 and 2026-10-12, by at least two independent sources (e.g., BBC World, Guardian World, Al Jazeera). | At least two independent sources (BBC World, Guardian World, Al Jazeera) confirm a terrorist attack involving explosives near a U.S.-run air base in the UK with at least one casualty between 2026-10-05 and 2026-10-12. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A coordinated cyberattack exploiting CVE-2026-88772 or CVE-2026-88771 will be confirmed by CISA or a major news outlet between 2026-10-05 an" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88771 dateAdded 2026-09-27, before the claimed window 2026-10-05..2026-10-12; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A major cyberattack using the Carbonato Botnet will be confirmed by CISA or a major news outlet between 2026-10-10 and 2026-10-17, targeting" → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new U.S. federal policy will be enacted to ban diesel exports, confirmed by a White House press release or CNBC Top News report, between 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…white house press release | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2995 issued all-time across 17 forecaster arms · 2453 open (232 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 336 issued · 186 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1064 | 947 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 336 | 186 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 129 | 124 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 210 | 193 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 335 | 271 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*