**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-02_1520.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-36 | 30% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include at least one entry for a zero-day vulnerability in SonicWall SMA1000 devices that was actively exploited in the wild. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24 for a vulnerability with CVE identifier or exploit description matching SonicWall SMA1000 zero-day flaws. |
| KKR-20260902-37 | 25% | 2026-10-07 | military/conflict | Between 2026-09-22 and 2026-09-28, at least one drone strike will be confirmed by two or more independently biased sources in the Kyiv region of Ukraine. | At least one drone strike event in Kyiv, Ukraine, is confirmed by two or more sources from distinct hostile sides (RU, UA) with no single side carrying more than 60% of the volume. |
| KKR-20260902-38 | 45% | 2026-10-08 | economics/markets | Between 2026-09-23 and 2026-09-29, the S&P 500 index will close above 7,700 points on at least one trading day. | The S&P 500 closes at or above 7,700.00 on at least one weekday between 2026-09-23 and 2026-09-29, based on the official market close from a public exchange. |
| KKR-20260902-39 | 15% | 2026-10-10 | disaster | Between 2026-09-25 and 2026-10-01, a new earthquake of magnitude 6.0 or greater will be recorded by the USGS in the Pacific Ring of Fire region. | The USGS Significant Quakes feed records a new earthquake event with magnitude ≥6.0 and depth ≤100km in the Pacific Ring of Fire between 2026-09-25 and 2026-10-01. |
| KKR-20260902-40 | 30% | 2026-10-12 | cyber | Between 2026-09-27 and 2026-10-03, a new ransomware attack will be confirmed by two or more independent sources targeting a U.S. healthcare provider, resulting in data exposure of over 100,000 patients. | At least two independently biased sources (e.g., BleepingComputer, The Hacker News) confirm a ransomware attack on a U.S. healthcare provider between 2026-09-27 and 2026-10-03, with data exposure affecting more than 100,000 patients. |
| KKR-20260902-41 | 28% | 2026-10-13 | military/conflict | Between 2026-09-28 and 2026-10-04, a new conflict escalation event involving Iran and Israel will be confirmed by two or more hostile sides in the Strait of Hormuz region. | At least two independently biased sources (AXIS, WEST, IL) confirm a new military event (e.g., missile, drone, naval engagement) in the Strait of Hormuz between 2026-09-28 and 2026-10-04. |
| KKR-20260902-42 | 40% | 2026-10-14 | political | Between 2026-09-29 and 2026-10-05, a new political scandal involving a U.S. federal official will be reported by two or more independent outlets, resulting in a formal investigation or resignation. | At least two independent outlets (e.g., BBC World, Guardian World, Politico) report a new political scandal involving a U.S. federal official that leads to a formal investigation or resignation by 2026-10-05. |
| KKR-20260902-43 | 18% | 2026-10-15 | disaster | Between 2026-09-30 and 2026-10-06, a new flood disaster in Nepal will be confirmed by two or more independent sources, resulting in at least 100 fatalities. | At least two independent sources (e.g., BBC World, Al Jazeera, Guardian World) confirm a new flood disaster in Nepal between 2026-09-30 and 2026-10-06, with a death toll of 100 or more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-24 and 2026-09-30, a new cyberattack exploiting a critical Langflow vulnerability will be reported by two or more independen" → REJECTED: resolution offers alternative VENUES joined by 'or' (…theft of an openai | or | aws…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-26 and 2026-10-02, the 10-year U.S. Treasury yield will exceed 5.0% on at least one trading day." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day

## III. LEDGER STANDING

1282 issued all-time across 14 forecaster arms · 1017 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 192 issued · 104 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 344 | 316 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 192 | 104 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5/unattested | 138 | 136 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 159 | 153 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 146 | 125 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*