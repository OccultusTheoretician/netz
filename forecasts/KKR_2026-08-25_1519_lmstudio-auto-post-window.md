**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251519Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-25_1517.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260825-01 | 30% | 2026-09-03 | military/conflict | Airstrikes on Gaza City occurred between 2026-08-25 and 2026-08-31, resulting in at least one confirmed casualty as reported by Al Jazeera and BBC World. | The CISA KEV catalog carries a date-added value between 2026-08-25 and 2026-08-31, and at least one of the following outlets reports a confirmed casualty: Al Jazeera, BBC World, or The Guardian. |
| KKR-20260825-02 | 35% | 2026-09-03 | military/conflict | A drone attack on a refinery in Russia's Krasnodar region caused a fire and at least two fatalities between 2026-08-25 and 2026-08-31. | Al Jazeera reports a drone attack on a refinery in Russia's Krasnodar region between 2026-08-25 and 2026-08-31, resulting in at least two fatalities. |
| KKR-20260825-03 | 30% | 2026-09-03 | economics/markets | The S&P 500 index closed above 7,700 on a weekday between 2026-08-25 and 2026-08-31. | The S&P 500 closes above 7,700 on a weekday between 2026-08-25 and 2026-08-31, as reported by the Federal Reserve Economic Data (FRED). |
| KKR-20260825-04 | 20% | 2026-09-03 | political | A new U.S. federal law was enacted to impose sanctions on Iran, with at least 60 entities listed, between 2026-08-25 and 2026-08-31. | The Federal Register publishes a new U.S. law imposing sanctions on Iran, listing at least 60 entities, between 2026-08-25 and 2026-08-31. |
| KKR-20260825-05 | 30% | 2026-09-03 | disaster | A magnitude 5.5 or higher earthquake occurred in Japan between 2026-08-25 and 2026-08-31, with a depth of less than 100 km. | The USGS Significant Quakes catalog lists an earthquake with magnitude 5.5 or higher and depth less than 100 km in Japan between 2026-08-25 and 2026-08-31. |
| KKR-20260825-06 | 25% | 2026-09-03 | economics/markets | A new U.S. tariff on Canadian goods, valued at $20 billion, was announced by the Canadian government between 2026-08-25 and 2026-08-31. | CNBC Top News reports that the Canadian government announced a retaliatory tariff on $20 billion of U.S. goods between 2026-08-25 and 2026-08-31. |
| KKR-20260825-07 | 35% | 2026-09-03 | cyber | A major cyberattack targeting a U.S. defense contractor was confirmed by CISA between 2026-08-25 and 2026-08-31. | CISA Advisories publishes a new advisory confirming a cyberattack on a U.S. defense contractor between 2026-08-25 and 2026-08-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Oracle WebLogic vulnerability CVE-2026-21962 was exploited in a cyberattack on a U.S. government system between 2026-08-25 and 2026-08-3" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-21962 dateAdded 2026-08-24, before the claimed window 2026-08-25..2026-08-31; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A major wildfire in the United States, affecting at least two states, was reported by the NWS or GDACS between 2026-08-25 and 2026-08-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (…severe wildfire alert | or | gdacs…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution narrows the claim with a qualifier the statement never makes — green, orange. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "A cyberattack on a hospital operator in the U.S. resulted in the theft of patient data between 2026-08-25 and 2026-08-31." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

899 issued all-time across 14 forecaster arms · 809 open (55 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 144 issued · 132 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 144 | 132 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 81 | 81 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 99 | 99 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 90 | 89 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*