**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041504Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-04_1502.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260804-49 | 25% | 2026-08-18 | cyber | Between 2026-08-06 and 2026-08-13, a cyberattack exploiting CVE-2026-18577 in N-able N-central systems results in unauthorized access to at least one critical infrastructure network. | The CISA KEV catalog carries a date-added value between 2026-08-06 and 2026-08-13 for CVE-2026-18577. |
| KKR-20260804-50 | 35% | 2026-08-25 | disaster | Between 2026-08-10 and 2026-08-17, a wildfire in the Russian Federation, as reported by GDACS Alerts, burns more than 10,000 hectares. | The GDACS Alerts system records a green forest fire notification for the Russian Federation with a burned area exceeding 10,000 hectares between 2026-08-10 and 2026-08-17. |
| KKR-20260804-51 | 40% | 2026-08-26 | political | Between 2026-08-11 and 2026-08-18, a new political scandal involving a U.S. federal official is reported by at least two independent outlets, including Al Jazeera and BBC World. | At least two independent news outlets, including Al Jazeera and BBC World, publish a report on a new political scandal involving a U.S. federal official between 2026-08-11 and 2026-08-18. |
| KKR-20260804-52 | 30% | 2026-08-28 | cyber | Between 2026-08-13 and 2026-08-20, a major cyberattack on a U.S. government agency is confirmed by at least two independent sources, including BleepingComputer and The Hacker News. | At least two independent sources, including BleepingComputer and The Hacker News, publish a report confirming a major cyberattack on a U.S. government agency between 2026-08-13 and 2026-08-20. |
| KKR-20260804-53 | 45% | 2026-08-30 | political | Between 2026-08-15 and 2026-08-22, a new political development involving Iran's foreign ministry and the U.S. government is reported by at least two independent sources, including Al Jazeera and BBC World. | At least two independent sources, including Al Jazeera and BBC World, publish a report on a new political development involving Iran's foreign ministry and the U.S. government between 2026-08-15 and 2026-08-22. |
| KKR-20260804-54 | 35% | 2026-08-31 | economics/markets | Between 2026-08-16 and 2026-08-23, a new economic policy shift by the U.S. Federal Reserve is announced by at least two independent financial news outlets, including CNBC and MarketWatch. | At least two independent financial news outlets, including CNBC and MarketWatch, publish a report announcing a new economic policy shift by the U.S. Federal Reserve between 2026-08-16 and 2026-08-23. |
| KKR-20260804-55 | 25% | 2026-09-01 | cyber | Between 2026-08-17 and 2026-08-24, a new cyberattack on a major financial institution in Europe is confirmed by at least two independent sources, including BleepingComputer and The Hacker News. | At least two independent sources, including BleepingComputer and The Hacker News, publish a report confirming a new cyberattack on a major financial institution in Europe between 2026-08-17 and 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-08-05, a drone strike targeting a military installation in Odesa, Ukraine, is confirmed by at least two independent sources from hos" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-12 and 2026-08-19, the S&P 500 index closes above 7,700 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-08-14 and 2026-08-21, a new missile strike in Crimea, Ukraine, is confirmed by at least two independent sources from hostile si" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world

## III. LEDGER STANDING

310 issued all-time across 14 forecaster arms · 272 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 15 issued · 15 open · nothing resolved yet — this arm earns a score at its first resolution.

*11 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 15 | 15 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 26 | 26 | 7 | 19 | 0.228 | 26.9% | 0.197 | -0.160 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 19 | 19 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*