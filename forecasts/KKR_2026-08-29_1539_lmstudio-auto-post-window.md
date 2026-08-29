**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291539Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-29_1537.md · forecaster: lmstudio/auto · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-01 | 30% | 2026-09-11 | military/conflict | A Russian drone strike on a warehouse near Kyiv between 2026-08-29 and 2026-09-05 results in at least 37 fatalities, confirmed by BBC World and Guardian World reporting. | BBC World and Guardian World each publish a report between 2026-09-07 and 2026-09-11 stating that a Russian drone strike on a warehouse near Kyiv between 2026-08-29 and 2026-09-05 caused at least 37 fatalities. |
| KKR-20260829-02 | 25% | 2026-09-17 | cyber | The CISA KEV catalog will include at least one new exploited vulnerability between 2026-09-01 and 2026-09-15. | The CISA KEV catalog carries at least one entry with a date-added value between 2026-09-01 and 2026-09-15. |
| KKR-20260829-03 | 15% | 2026-10-02 | disaster | A major earthquake with magnitude 6.5 or higher will be recorded by USGS in the Pacific Northwest between 2026-09-01 and 2026-09-30. | The USGS Significant Quakes feed records one or more events with magnitude ≥6.5 in the Pacific Northwest region between 2026-09-01 and 2026-09-30. |
| KKR-20260829-04 | 45% | 2026-10-02 | economics/markets | The S&P 500 will close above 7,800 on at least one weekday between 2026-09-01 and 2026-09-30. | The S&P 500 closes at or above 7,800 on at least one weekday between 2026-09-01 and 2026-09-30, as reported by MarketWatch. |
| KKR-20260829-05 | 35% | 2026-09-17 | cyber | A cyberattack exploiting a flaw in PaperCut software will be confirmed by BleepingComputer between 2026-09-01 and 2026-09-15. | BleepingComputer publishes a report between 2026-09-03 and 2026-09-17 confirming that a cyberattack exploited a flaw in PaperCut software between 2026-09-01 and 2026-09-15. |
| KKR-20260829-06 | 50% | 2026-10-02 | economics/markets | The 10-year U.S. Treasury yield will exceed 4.8% on at least one weekday between 2026-09-01 and 2026-09-30. | The 10-year U.S. Treasury yield exceeds 4.8% on at least one weekday between 2026-09-01 and 2026-09-30, as reported by CNBC. |
| KKR-20260829-07 | 30% | 2026-09-17 | military/conflict | A drone strike on Gaza City will be confirmed by Al Jazeera and BBC World between 2026-09-01 and 2026-09-15. | Al Jazeera and BBC World each publish a report between 2026-09-03 and 2026-09-17 confirming a drone strike on Gaza City between 2026-09-01 and 2026-09-15. |
| KKR-20260829-08 | 40% | 2026-10-02 | economics/markets | The European Union will report gas storage levels below 30% of capacity on at least one weekday between 2026-09-01 and 2026-09-30. | The Guardian Business reports that EU gas storage levels are below 30% of capacity on at least one weekday between 2026-09-01 and 2026-09-30. |
| KKR-20260829-09 | 25% | 2026-09-17 | cyber | A major cyberattack exploiting a flaw in the Cosmos EVM will be confirmed by The Hacker News between 2026-09-01 and 2026-09-15. | The Hacker News publishes a report between 2026-09-03 and 2026-09-17 confirming that a cyberattack exploited a flaw in the Cosmos EVM between 2026-09-01 and 2026-09-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one new wildfire will be reported by GDACS Alerts in Tanzania between 2026-09-01 and 2026-09-30." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

1054 issued all-time across 14 forecaster arms · 893 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 169 issued · 138 open · 29 resolved · 10 hits / 19 misses · **Brier 0.250** against its own base rate 34.5% (climatological 0.226) · **skill -0.109** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 249 | 232 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 101 | 100 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 121 | 118 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 111 | 103 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*