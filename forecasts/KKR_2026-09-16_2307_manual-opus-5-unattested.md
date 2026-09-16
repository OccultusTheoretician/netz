**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162307Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: manual/opus-5/unattested · 10 accepted / 0 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-46 | 60% | 2026-10-12 | military/conflict | A missile or drone attack on Saudi Arabian territory claimed by or attributed to the Houthis, counting interceptions, occurs between 2026-09-17 and 2026-10-07. | TRUE if at least two of AP, Reuters and AFP report a missile or drone attack on Saudi territory, claimed by or attributed to the Houthis and including interceptions, occurring between 2026-09-17 and 2026-10-07. |
| KKR-20260916-47 | 20% | 2026-11-05 | military/conflict | The US President or the Government of Iran publicly announces a ceasefire, truce or cessation of hostilities between the United States and Iran between 2026-09-17 and 2026-11-02. | TRUE if AP and Reuters both report that the US President or the Government of Iran announced a ceasefire, truce or cessation of US-Iran hostilities between 2026-09-17 and 2026-11-02; otherwise FALSE. |
| KKR-20260916-48 | 55% | 2026-10-20 | military/conflict | Russia and Ukraine complete at least one exchange of prisoners of war, announced by both governments, between 2026-09-17 and 2026-10-16. | TRUE if both the Russian Defence Ministry and the Ukrainian government (the President or the POW Coordination Headquarters) announce a completed prisoner-of-war exchange that took place between 2026-09-17 and 2026-10-16. |
| KKR-20260916-49 | 45% | 2026-11-09 | economics/markets | WTI crude oil, as the EIA Cushing spot price in FRED series DCOILWTICO, closes below 90.00 dollars per barrel on at least one trading day between 2026-09-17 and 2026-10-30. Reference: 101.87 on the packet date. | TRUE if FRED series DCOILWTICO shows a daily value below 90.00 for any date between 2026-09-17 and 2026-10-30; otherwise FALSE. Reference: 101.87 WTI on the packet date, per the packet market snapshot. |
| KKR-20260916-50 | 30% | 2026-11-02 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28. | TRUE if FRED DFEDTARU for 2026-10-29 exceeds its 2026-10-27 value, i.e. a hike at the 2026-10-27 to 2026-10-28 meeting. Reference: relative to the 2026-10-27 upper bound; packet holds no funds-rate level. |
| KKR-20260916-51 | 20% | 2026-11-04 | economics/markets | The S&P 500 closes at or below 7046.19, a 7.5 percent decline from the packet reference, on at least one trading day between 2026-09-17 and 2026-10-30. Reference: 7617.50 on the packet date. | TRUE if FRED series SP500 shows a daily close at or below 7046.19 for any date between 2026-09-17 and 2026-10-30; otherwise FALSE. Reference: 7617.50 on the packet date. |
| KKR-20260916-52 | 40% | 2026-11-03 | cyber | CISA adds the exploited Acronis backup plugin for cPanel vulnerability to its Known Exploited Vulnerabilities catalog between 2026-09-17 and 2026-10-30. | TRUE if the CISA KEV catalog carries an entry with vendorProject Acronis whose product or vulnerabilityName references cPanel and whose dateAdded falls between 2026-09-17 and 2026-10-30; otherwise FALSE. |
| KKR-20260916-53 | 30% | 2026-11-03 | cyber | CISA adds a WSO2 vulnerability to its Known Exploited Vulnerabilities catalog between 2026-09-17 and 2026-10-30. | TRUE if the CISA KEV catalog carries an entry with vendorProject WSO2 whose dateAdded falls between 2026-09-17 and 2026-10-30; otherwise FALSE. |
| KKR-20260916-54 | 52% | 2027-01-08 | political | Democrats win control of the US Senate in the 2026-11-03 midterm elections, holding at least 51 seats with caucusing independents in the 120th Congress. | TRUE if the senate.gov party division for the 120th Congress, read on 2027-01-08 after the 2026-11-03 election, shows Democrats plus independents caucusing with them at 51 or more seats; otherwise FALSE. |
| KKR-20260916-55 | 6% | 2027-01-05 | political | Friedrich Merz formally resigns as German Federal Chancellor, or the Bundestag elects a different Chancellor, between 2026-09-17 and 2026-12-31. | TRUE if Bundestag or Federal Government records show Merz formally submitted his resignation as Chancellor, or the Bundestag elected another person Chancellor, between 2026-09-17 and 2026-12-31; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2281 issued all-time across 16 forecaster arms · 1879 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 263 issued · 256 open · 7 resolved · 5 hits / 2 misses · **Brier 0.137** against its own base rate 71.4% (climatological 0.204) · **skill +0.329** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 758 | 705 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 113 | 111 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 249 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 263 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 242 | 199 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*