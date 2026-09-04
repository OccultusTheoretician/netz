**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-01 | 25% | 2026-10-05 | military/conflict | A drone strike on Kyiv's security services headquarters occurs between 2026-09-21 and 2026-09-24, resulting in at least one confirmed casualty. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least one report from a hostile side (RU, UA, AXIS) confirms a drone strike on Kyiv's security services HQ with at least one confirmed casualty in corroborating reports. |
| KKR-20260904-02 | 30% | 2026-10-05 | cyber | A cyberattack exploiting the Chrome V8 zero-day vulnerability is confirmed by at least two independent sources between 2026-09-21 and 2026-09-24. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least two independent sources (e.g., BleepingComputer, The Hacker News) confirm exploitation of the Chrome V8 zero-day vulnerability during that window. |
| KKR-20260904-03 | 20% | 2026-10-05 | disaster | A major earthquake of magnitude 6.0 or higher occurs in the United States between 2026-09-21 and 2026-09-24, with at least one fatality reported. | The USGS Significant Quakes catalog carries a magnitude 6.0 or higher event with a depth of 70km or less, and at least one fatality is reported in corroborating sources (e.g., BBC World, Al Jazeera) between 2026-09-21 and 2026-09-24. |
| KKR-20260904-04 | 35% | 2026-10-05 | economics/markets | The S&P 500 index closes below 7,600 on at least one trading day between 2026-09-21 and 2026-09-24. | The S&P 500 index closes below 7,600 on at least one trading day between 2026-09-21 and 2026-09-24, as recorded in the Market Snapshot data. |
| KKR-20260904-05 | 22% | 2026-10-05 | cyber | A new vulnerability in Microsoft Teams is exploited in a coordinated attack on at least 100 organizations between 2026-09-21 and 2026-09-24. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least 100 organizations are confirmed to have been compromised via the Microsoft Teams vulnerability in corroborating reports. |
| KKR-20260904-06 | 18% | 2026-10-05 | political | A political scandal involving a U.S. presidential candidate leads to a formal indictment by a federal grand jury between 2026-09-21 and 2026-09-24. | A federal grand jury issues a formal indictment against a U.S. presidential candidate, confirmed by at least two independent sources (e.g., Guardian World, NPR News) between 2026-09-21 and 2026-09-24. |
| KKR-20260904-07 | 15% | 2026-10-05 | military/conflict | Iran announces a new military offensive in the Strait of Hormuz between 2026-09-21 and 2026-09-24, confirmed by at least two hostile sides (AXIS, WEST). | At least two hostile sides (AXIS, WEST) confirm Iran announces a new military offensive in the Strait of Hormuz between 2026-09-21 and 2026-09-24, as reported in corroborating sources. |
| KKR-20260904-08 | 32% | 2026-10-05 | economics/markets | The 10-year U.S. Treasury yield exceeds 5.0% on at least one trading day between 2026-09-21 and 2026-09-24. | The 10-year U.S. Treasury yield exceeds 5.0% on at least one trading day between 2026-09-21 and 2026-09-24, as recorded in the Market Snapshot data. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A wildfire in Mozambique spreads beyond 500 hectares and is reported by GDACS Alerts between 2026-09-21 and 2026-09-24." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "A coordinated cyberattack on a U.S. federal agency results in data exfiltration, confirmed by a public disclosure from the agency or a major" → REJECTED: resolution offers alternative VENUES joined by 'or' (…u.s. federal agency | or | a major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1412 issued all-time across 15 forecaster arms · 1147 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 208 issued · 120 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 15 | 15 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 153 | 151 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 174 | 168 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 158 | 137 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*