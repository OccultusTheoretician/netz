**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161518Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260816-01 | 30% | 2026-08-26 | cyber | Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in the wild with a public exploit and a date-added value between 2026-08-17 and 2026-08-20. | The CISA KEV catalog carries a date-added value between 2026-08-17 and 2026-08-20 for a vulnerability with a public exploit and confirmed active use in the wild. |
| KKR-20260816-02 | 45% | 2026-08-28 | disaster | Between 2026-08-21 and 2026-08-24, the USGS Significant Quakes catalog will record at least one earthquake with magnitude 6.0 or higher and a depth of 10 km or less in Indonesia. | The USGS Significant Quakes catalog carries an event with magnitude ≥6.0 and depth ≤10 km in Indonesia between 2026-08-21 and 2026-08-24. |
| KKR-20260816-03 | 25% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, at least one drone strike will be reported in Kyiv by two or more independently biased outlets across hostile sides (RU, UA, WEST, AXIS) with corroborating reports. | At least one drone strike in Kyiv is reported by two or more independently biased outlets across hostile sides (RU, UA, WEST, AXIS) with corroborating reports between 2026-08-21 and 2026-08-24. |
| KKR-20260816-04 | 20% | 2026-08-28 | political | Between 2026-08-21 and 2026-08-24, the European Union will formally announce a new sanctions package targeting Iran's energy sector. | The European Union issues a public statement confirming a new sanctions package targeting Iran's energy sector between 2026-08-21 and 2026-08-24. |
| KKR-20260816-05 | 40% | 2026-08-28 | disaster | Between 2026-08-21 and 2026-08-24, a wildfire in Belgium will grow to exceed 1,000 hectares and be reported by at least two independent sources. | A wildfire in Belgium exceeds 1,000 hectares in size and is reported by at least two independent sources between 2026-08-21 and 2026-08-24. |
| KKR-20260816-06 | 15% | 2026-08-28 | economics/markets | Between 2026-08-21 and 2026-08-24, the U.S. Federal Reserve will announce a rate hike of at least 25 basis points. | The U.S. Federal Reserve announces a rate hike of at least 25 basis points between 2026-08-21 and 2026-08-24. |
| KKR-20260816-07 | 30% | 2026-08-28 | cyber | Between 2026-08-21 and 2026-08-24, a new cyberattack using AI-generated phishing content will be confirmed by at least two independent sources in the United States. | A cyberattack using AI-generated phishing content is confirmed by at least two independent sources in the United States between 2026-08-21 and 2026-08-24. |
| KKR-20260816-08 | 35% | 2026-08-28 | political | Between 2026-08-21 and 2026-08-24, a major political scandal involving a U.S. federal official will be reported by two or more major U.S. news outlets with conflicting narratives. | A major political scandal involving a U.S. federal official is reported by two or more major U.S. news outlets with conflicting narratives between 2026-08-21 and 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-21 and 2026-08-24, the S&P 500 will close above 7,800 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-08-21 and 2026-08-24, at least one new report will confirm a cyberattack on a critical infrastructure provider in the United St" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

634 issued all-time across 14 forecaster arms · 544 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 82 issued · 70 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 116 | 108 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 82 | 70 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 35 | 35 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 55 | 55 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 47 | 46 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*