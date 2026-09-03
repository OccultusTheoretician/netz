**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-03_1518.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-15 | 25% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, at least one confirmed cyberattack exploiting CVE-2026-83548 will be reported by two or more independent sources. | At least one confirmed cyberattack exploiting CVE-2026-83548 is reported by two or more independent sources between 2026-09-21 and 2026-09-24. |
| KKR-20260903-16 | 35% | 2026-10-06 | economics/markets | Between 2026-09-21 and 2026-09-24, the Netherlands will publicly confirm the transfer of at least $5 billion in gold from the United States to Canada or the United Kingdom. | The Netherlands publicly confirms the transfer of at least $5 billion in gold from the United States to Canada or the United Kingdom between 2026-09-21 and 2026-09-24. |
| KKR-20260903-17 | 20% | 2026-10-07 | disaster | Between 2026-09-21 and 2026-09-24, a magnitude 6.0 or higher earthquake will be recorded by the USGS in the South Sandwich Islands region. | The USGS records a magnitude 6.0 or higher earthquake in the South Sandwich Islands region between 2026-09-21 and 2026-09-24. |
| KKR-20260903-18 | 15% | 2026-10-09 | military/conflict | Between 2026-09-21 and 2026-09-24, Iran will launch a missile strike against a target in Kuwait City, confirmed by at least two independent sources. | Iran launches a missile strike against a target in Kuwait City, confirmed by at least two independent sources between 2026-09-21 and 2026-09-24. |
| KKR-20260903-19 | 40% | 2026-10-05 | economics/markets | Between 2026-09-21 and 2026-09-24, the Brent crude oil price will exceed $100 per barrel on at least one trading day. | The Brent crude oil price exceeds $100 per barrel on at least one trading day between 2026-09-21 and 2026-09-24. |
| KKR-20260903-20 | 28% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-48710 will be reported by two or more independent sources. | A confirmed cyberattack exploiting CVE-2026-48710 is reported by two or more independent sources between 2026-09-21 and 2026-09-24. |
| KKR-20260903-21 | 18% | 2026-10-07 | disaster | Between 2026-09-21 and 2026-09-24, a magnitude 5.5 or higher earthquake will be recorded by the USGS in China. | The USGS records a magnitude 5.5 or higher earthquake in China between 2026-09-21 and 2026-09-24. |
| KKR-20260903-22 | 22% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-9586 will be reported by two or more independent sources. | A confirmed cyberattack exploiting CVE-2026-9586 is reported by two or more independent sources between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2026-59822 with a date-added value of 2026-09-02." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-59822 dateAdded 2026-09-02, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, the S&P 500 will close above 7,800 points on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1342 issued all-time across 15 forecaster arms · 1077 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 200 issued · 112 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 370 | 342 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 200 | 112 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 152 | 131 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*