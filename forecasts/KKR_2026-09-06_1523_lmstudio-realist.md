**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061523Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-63 | 30% | 2026-09-24 | cyber | On 2026-09-22, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in the wild, with a date-added value between 2026-09-17 and 2026-09-21. | The CISA KEV catalog carries a date-added value between 2026-09-17 and 2026-09-21 for at least one new entry. |
| KKR-20260906-64 | 25% | 2026-09-26 | military/conflict | Between 2026-09-21 and 2026-09-24, a drone strike will be confirmed by at least two hostile sides in the Kyiv theater, with weapons reported as drone and casualties stated in at least one corroborating report. | At least two hostile sides (RU, UA, AXIS, WEST) report a drone strike in Kyiv between 2026-09-21 and 2026-09-24, with weapons reported as drone and casualties stated in at least one corroborating report. |
| KKR-20260906-65 | 35% | 2026-09-27 | disaster | Between 2026-09-22 and 2026-09-25, a volcanic eruption will cause flight cancellations at Jakarta International Airport, with at least 100,000 passengers stranded, as confirmed by two independent sources. | Between 2026-09-22 and 2026-09-25, a volcanic eruption causes flight cancellations at Jakarta International Airport, with at least 100,000 passengers stranded, as confirmed by two independent sources. |
| KKR-20260906-66 | 30% | 2026-09-27 | political | Between 2026-09-21 and 2026-09-25, Iran will issue a public statement via a hostile side (AXIS or WEST) claiming a 'more painful' response to U.S. attacks, with the statement confirmed by two independent sources. | Between 2026-09-21 and 2026-09-25, Iran issues a public statement via a hostile side (AXIS or WEST) claiming a 'more painful' response to U.S. attacks, confirmed by two independent sources. |
| KKR-20260906-67 | 35% | 2026-09-27 | cyber | Between 2026-09-21 and 2026-09-25, a cyberattack exploiting a zero-day vulnerability in Magento or Adobe Commerce will be confirmed by two independent sources, with the attack resulting in data exfiltration. | Between 2026-09-21 and 2026-09-25, a cyberattack exploiting a zero-day vulnerability in Magento or Adobe Commerce is confirmed by two independent sources, with the attack resulting in data exfiltration. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-23, the S&P 500 will close above 7,750 points, based on the prior-session close of 7,718.60." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-24, the 10-year U.S. Treasury yield will close above 4.85 percent, based on the prior-session close of 4.78 percent." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-24 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-23, the EUR/USD exchange rate will close below 1.15, based on the prior-session close of 1.16." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-22 and 2026-09-25, a U.S. government agency will release a public report confirming that AI data centers are transforming ru" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-09-24, the M 6.3 earthquake in Nikolski, Alaska, will be confirmed by a second independent source as having caused structural damage" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-24 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1558 issued all-time across 16 forecaster arms · 1293 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 16 issued · 16 open · nothing resolved yet — this arm earns a score at its first resolution.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 458 | 430 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 224 | 136 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 168 | 166 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 185 | 179 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 173 | 152 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*