**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192250Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-19_1519.md · forecaster: manual/sonnet-5/unattested · 7 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260819-20 | 18% | 2026-09-11 | political | Between 2026-08-19 and 2026-09-09, Saudi Arabia, Bahrain, Qatar, Kuwait, or Oman formally announces new trade restrictions or a trade suspension against Iran, distinct from the UAE action already reported. | TRUE if, between 2026-08-19 and 2026-09-09, the government of Saudi Arabia, Bahrain, Qatar, Kuwait, or Oman issues an official trade-restriction announcement against Iran, per two of Reuters, AP, or Bloomberg. |
| KKR-20260819-21 | 45% | 2026-09-04 | cyber | Between 2026-08-19 and 2026-09-02, the CISA Known Exploited Vulnerabilities catalog lists 10 or more entries with a dateAdded value in that range, following the 4 entries added 2026-08-18. | TRUE if the public CISA KEV JSON feed shows 10 or more entries with dateAdded between 2026-08-19 and 2026-09-02 inclusive, queried on or after 2026-09-04. |
| KKR-20260819-22 | 38% | 2026-09-21 | economic | Between 2026-08-19 and 2026-09-18, the 10-Year Treasury constant maturity yield (FRED series DGS10) closes at or above 4.85 percent on at least one trading day, up from 4.65 percent on 2026-08-19. | TRUE if FRED series DGS10 records a daily close of 4.85 or higher on any trading day between 2026-08-19 and 2026-09-18, per data available by 2026-09-21. |
| KKR-20260819-23 | 15% | 2026-11-17 | crime_security | Between 2026-08-19 and 2026-11-15, German federal prosecutors file a formal indictment against the Ukrainian national arrested in Croatia over the 2022 Nord Stream pipeline bombings. | TRUE if the Generalbundesanwalt files a formal indictment against the Croatia-arrested individual, reported by two of Reuters, AP, or DPA, before 2026-11-17. |
| KKR-20260819-24 | 50% | 2026-09-18 | disaster | Between 2026-08-19 and 2026-09-16, USGS catalogs at least one aftershock of magnitude 6.0 or greater within 150 km of the M7.7 Ende, Indonesia epicenter recorded 2026-08-19. | TRUE if the USGS earthquake catalog lists an event of magnitude 6.0 or greater within 150 km of the Ende epicenter with origin time between 2026-08-19 and 2026-09-16. |
| KKR-20260819-25 | 7% | 2026-10-19 | political | Between 2026-08-19 and 2026-10-17, Ukraine's Verkhovna Rada or Central Election Commission formally schedules a date for a presidential election, following the sacked defence minister's public call for one. | TRUE if the Verkhovna Rada or Ukraine's Central Election Commission issues an official act setting a presidential election date, reported by two of Reuters, AP, or Ukrainska Pravda, by 2026-10-19. |
| KKR-20260819-26 | 20% | 2026-10-19 | disaster | Between 2026-08-19 and 2026-10-17, the WHO Director-General declares the Democratic Republic of Congo Ebola outbreak, which reached 5,000 cases this window, a Public Health Emergency of International Concern. | TRUE if WHO's Director-General issues a formal PHEIC declaration covering the DRC Ebola outbreak between 2026-08-19 and 2026-10-17, per WHO statement and two wire services, by 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-19 and 2026-09-16, Iran announces closure of the Strait of Hormuz to commercial shipping, or the US Navy Fifth Fleet or EIA " → REJECTED: cited items name Iran, Islamic Republic of, United Arab Emirates; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "At the 2026-09-18 market close, Marvell (MRVL) cumulative return since the 2026-08-18 close exceeds Broadcom (AVGO) cumulative return since " → REJECTED: event window opens 2026-08-18, before this row is sealed (2026-08-19) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

774 issued all-time across 14 forecaster arms · 684 open (11 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 69 issued · 68 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 165 | 157 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 105 | 93 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 69 | 68 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*