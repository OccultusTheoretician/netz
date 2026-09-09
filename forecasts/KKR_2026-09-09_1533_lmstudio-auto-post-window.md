**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091533Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-09_1530.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260909-01 | 25% | 2026-10-06 | cyber | Between 2026-09-23 and 2026-09-29, the CISA KEV catalog includes at least one new vulnerability with a CVSS score of 10.0 or higher. | The CISA KEV catalog carries a date-added value between 2026-09-23 and 2026-09-29 for a vulnerability with a CVSS score of 10.0 or higher. |
| KKR-20260909-02 | 15% | 2026-10-09 | disaster | Between 2026-09-26 and 2026-10-02, a new earthquake of magnitude 6.0 or higher is recorded by the USGS in the Pacific Northwest. | The USGS Significant Quakes feed records an earthquake of magnitude 6.0 or higher in the Pacific Northwest (e.g., Washington, Oregon, Alaska) between 2026-09-26 and 2026-10-02. |
| KKR-20260909-03 | 20% | 2026-10-10 | political | Between 2026-09-27 and 2026-10-03, a new political scandal involving a U.S. federal official is confirmed by two independent outlets (e.g., Guardian World, NPR News). | Two independent outlets (e.g., Guardian World, NPR News) confirm a political scandal involving a U.S. federal official between 2026-09-27 and 2026-10-03. |
| KKR-20260909-04 | 18% | 2026-10-12 | crime/security | Between 2026-09-29 and 2026-10-05, a new terrorist attack with at least five fatalities occurs in the Middle East, confirmed by two or more independent outlets from hostile sides. | Two or more independent outlets from hostile sides (e.g., AXIS, WEST, PS) confirm a terrorist attack in the Middle East with at least five fatalities between 2026-09-29 and 2026-10-05. |
| KKR-20260909-05 | 32% | 2026-10-13 | military/conflict | Between 2026-09-30 and 2026-10-06, a new geopolitical crisis escalates involving Iran and the U.S., resulting in a confirmed military strike on a U.S. asset in the Strait of Hormuz. | A confirmed military strike on a U.S. asset in the Strait of Hormuz is reported by two or more independent outlets from hostile sides (AXIS, WEST) between 2026-09-30 and 2026-10-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, at least one drone strike with confirmed casualties occurs in Kyiv, Ukraine, as reported by at least two " → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | a public…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-22 and 2026-09-28, the S&P 500 closes above 7,800 on at least one weekday." → REJECTED: resolution offers alternative VENUES joined by 'or' (…d by the federal reserve economic data (fred) | or | a major exchange index feed…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-24 and 2026-09-30, a cyberattack exploiting CVE-2026-81963 is confirmed in at least one public system by a third-party secur" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-25 and 2026-10-01, the Brent crude oil price exceeds $105 per barrel on at least one trading day." → REJECTED: resolution offers alternative VENUES joined by 'or' (…026-09-25 and 2026-10-01, as reported by fred | or | a major exchange feed…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-28 and 2026-10-04, a new cyberattack on a critical infrastructure system in the U.S. is confirmed by CISA or a major news wi" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

1748 issued all-time across 16 forecaster arms · 1412 open (47 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 240 issued · 111 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 537 | 499 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 240 | 111 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 188 | 185 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 206 | 200 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 192 | 160 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*