**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-01 | 90% | 2026-10-01 | cyber | On 2026-09-17, the CISA KEV catalog will include CVE-2026-58704 with a date-added value of 2026-09-16. | The CISA KEV catalog carries a date-added value of 2026-09-16 for CVE-2026-58704. |
| KKR-20260916-02 | 25% | 2026-10-05 | disaster | Between 2026-09-16 and 2026-09-23, a green forest fire notification will be issued for Spain via GDACS Alerts. | GDACS Alerts issues a green forest fire notification for Spain between 2026-09-16 and 2026-09-23. |
| KKR-20260916-03 | 35% | 2026-10-05 | political | Between 2026-09-16 and 2026-09-23, the US House of Representatives will vote to end the Iran war for a third time. | The US House of Representatives votes to end the Iran war for a third time between 2026-09-16 and 2026-09-23. |
| KKR-20260916-04 | 40% | 2026-10-05 | economics/markets | Between 2026-09-16 and 2026-09-23, the EUR/USD exchange rate will close above 1.1600 on at least one trading day. | The EUR/USD exchange rate closes above 1.1600 on at least one trading day between 2026-09-16 and 2026-09-23. |
| KKR-20260916-05 | 32% | 2026-10-05 | cyber | Between 2026-09-16 and 2026-09-23, a critical ScreenConnect vulnerability (CVE-2026-XXXXX) will be actively exploited in attacks, as confirmed by at least two independent sources. | At least two independent sources confirm that a critical ScreenConnect vulnerability (CVE-2026-XXXXX) is actively exploited in attacks between 2026-09-16 and 2026-09-23. |
| KKR-20260916-06 | 15% | 2026-10-05 | political | Between 2026-09-16 and 2026-09-23, the US Senate will pass a resolution to ban social media use for users under 13 in the European Union. | The US Senate passes a resolution to ban social media use for users under 13 in the European Union between 2026-09-16 and 2026-09-23. |
| KKR-20260916-07 | 38% | 2026-10-05 | disaster | Between 2026-09-16 and 2026-09-23, a building collapse in Gaza City will result in at least 15 fatalities, as confirmed by at least two corroborating reports. | At least two corroborating reports confirm that a building collapse in Gaza City results in at least 15 fatalities between 2026-09-16 and 2026-09-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-16 and 2026-09-23, at least one report from a hostile side confirms a drone strike on Kharkiv, Ukraine, with no casualties s" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-09-16 and 2026-09-23, the S&P 500 will close below 7,600.00 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-16 and 2026-09-23, at least one report from a hostile side confirms a missile attack on Zaporizhzhia, Ukraine, with no casua" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world

## III. LEDGER STANDING

2233 issued all-time across 16 forecaster arms · 1831 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 280 issued · 130 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 741 | 688 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 69 | 64 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 105 | 103 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 240 | 233 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 253 | 246 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 242 | 199 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*