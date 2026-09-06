**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-55 | 25% | 2026-10-06 | cyber | Between 2026-09-22 and 2026-09-29, a cyberattack exploiting an unpatched vulnerability in a critical infrastructure system is confirmed by CISA KEV catalog with a date-added value in that window. | The CISA KEV catalog carries a date-added value between 2026-09-22 and 2026-09-29 for a vulnerability exploited in a critical infrastructure system. |
| KKR-20260906-56 | 35% | 2026-10-07 | disaster | Between 2026-09-23 and 2026-09-30, a volcanic eruption in Indonesia causes flight cancellations at Jakarta International Airport, confirmed by at least two independent sources (one from BBC, one from Guardian). | The GDACS Alerts system carries a report with eventtype=ER between 2026-09-23 and 2026-09-30 for a volcanic eruption in Indonesia causing flight cancellations at Jakarta International Airport, confirmed by at least two independent sources (one from BBC, one from Guardian). |
| KKR-20260906-57 | 40% | 2026-10-09 | political | Between 2026-09-25 and 2026-10-02, a new political development in the U.S. involves a public statement by Jared Kushner or Steve Witkoff on Ukraine peace talks, confirmed by at least two independent sources (one from Guardian, one from BBC). | A public statement by Jared Kushner or Steve Witkoff on Ukraine peace talks is confirmed by at least two independent sources (one from Guardian, one from BBC) between 2026-09-25 and 2026-10-02. |
| KKR-20260906-58 | 30% | 2026-10-10 | disaster | Between 2026-09-26 and 2026-10-03, a new earthquake of magnitude 5.5 or higher is recorded in the Solomon Islands, confirmed by USGS Significant Quakes. | The USGS Significant Quakes system carries a report with magnitude ≥5.5 and location in the Solomon Islands between 2026-09-26 and 2026-10-03. |
| KKR-20260906-59 | 28% | 2026-10-11 | cyber | Between 2026-09-27 and 2026-10-04, a new phishing campaign using invisible Unicode characters is reported by BleepingComputer and confirmed by The Hacker News. | BleepingComputer reports a new phishing campaign using invisible Unicode characters between 2026-09-27 and 2026-10-04, and The Hacker News confirms it within 48 hours. |
| KKR-20260906-60 | 32% | 2026-10-12 | political | Between 2026-09-28 and 2026-10-05, a new political scandal involving a U.S. government official is reported by Politico and confirmed by Guardian World. | A new political scandal involving a U.S. government official is reported by Politico and confirmed by Guardian World between 2026-09-28 and 2026-10-05. |
| KKR-20260906-61 | 35% | 2026-10-13 | disaster | Between 2026-09-29 and 2026-10-06, a new wildfire in Brazil is reported by GDACS Alerts with eventtype=WF and confirmed by at least two independent sources (one from BBC, one from Guardian). | The GDACS Alerts system carries a report with eventtype=WF for a new wildfire in Brazil between 2026-09-29 and 2026-10-06, confirmed by at least two independent sources (one from BBC, one from Guardian). |
| KKR-20260906-62 | 20% | 2026-10-14 | cyber | Between 2026-09-30 and 2026-10-07, a new cyberattack on a government system is confirmed by CISA KEV catalog with a date-added value in that window. | The CISA KEV catalog carries a date-added value between 2026-09-30 and 2026-10-07 for a vulnerability exploited in a government system. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-28, a drone strike with confirmed casualties occurs in Kyiv, Ukraine, reported by at least two independently " → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "Between 2026-09-24 and 2026-10-01, the S&P 500 closes above 7,800 on at least one trading day, as reported by a major financial wire service" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

1553 issued all-time across 16 forecaster arms · 1288 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 224 issued · 136 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

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
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
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