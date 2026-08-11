**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111752Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-11_1750.md · forecaster: lmstudio/auto · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260811-01 | 25% | 2026-08-28 | cyber | Between 2026-08-22 and 2026-08-25, the CISA KEV catalog will add a new entry for a vulnerability in Microsoft SharePoint exploited in ransomware attacks, with a date-added value between 2026-08-22 and 2026-08-25. | The CISA KEV catalog carries a date-added value between 2026-08-22 and 2026-08-25 for a vulnerability in Microsoft SharePoint exploited in ransomware attacks. |
| KKR-20260811-02 | 45% | 2026-08-28 | economics/markets | Between 2026-08-23 and 2026-08-26, the S&P 500 will close above 7,800 points on at least one weekday within the window, based on the official market close data from the NYSE. | The S&P 500 closes above 7,800 points on at least one weekday between 2026-08-23 and 2026-08-26, as reported by the NYSE. |
| KKR-20260811-03 | 35% | 2026-08-30 | disaster | Between 2026-08-24 and 2026-08-27, a wildfire in California's Big Sur region will result in at least one confirmed fatality, as reported by two independent outlets (Guardian World and BBC World). | Two independent outlets (Guardian World and BBC World) report at least one confirmed fatality from a wildfire in California's Big Sur region between 2026-08-24 and 2026-08-27. |
| KKR-20260811-04 | 40% | 2026-08-30 | economics/markets | Between 2026-08-25 and 2026-08-28, the U.S. Federal Reserve will announce a 0.25 percentage point increase in the federal funds rate, as confirmed by a press release from the Federal Reserve Board. | A press release from the Federal Reserve Board confirms a 0.25 percentage point increase in the federal funds rate between 2026-08-25 and 2026-08-28. |
| KKR-20260811-05 | 20% | 2026-08-31 | cyber | Between 2026-08-26 and 2026-08-29, a cyberattack exploiting a zero-day vulnerability in OpenAI's GPT-5.6-Cyber model will be reported by at least two independent outlets (The Hacker News and BleepingComputer), with no public patch released by OpenAI. | Two independent outlets (The Hacker News and BleepingComputer) report a cyberattack exploiting a zero-day vulnerability in OpenAI's GPT-5.6-Cyber model between 2026-08-26 and 2026-08-29, with no public patch released by OpenAI. |
| KKR-20260811-06 | 15% | 2026-09-01 | political | Between 2026-08-27 and 2026-08-30, the European Parliament will vote to abolish the death penalty for all crimes, as confirmed by a press release from the European Parliament. | A press release from the European Parliament confirms the abolition of the death penalty for all crimes between 2026-08-27 and 2026-08-30. |
| KKR-20260811-07 | 30% | 2026-09-02 | disaster | Between 2026-08-28 and 2026-08-31, a magnitude 6.0 or higher earthquake will be recorded by the USGS in the Philippines, with a depth of less than 70 km and a location within 100 km of the island of Mindanao. | The USGS Significant Quakes database records a magnitude 6.0 or higher earthquake with a depth of less than 70 km and a location within 100 km of the island of Mindanao between 2026-08-28 and 2026-08-31. |
| KKR-20260811-08 | 25% | 2026-09-03 | crime/security | Between 2026-08-29 and 2026-09-01, the U.S. Department of Justice will announce the indictment of a former senior official from the Trump administration for obstruction of justice, as confirmed by a press release from the DOJ. | A press release from the U.S. Department of Justice confirms the indictment of a former senior official from the Trump administration for obstruction of justice between 2026-08-29 and 2026-09-01. |
| KKR-20260811-09 | 35% | 2026-09-04 | cyber | Between 2026-08-30 and 2026-09-02, a new ransomware group called 'Gunra' will be confirmed by CISA to have exploited a vulnerability in Fortinet firewalls, with a public exploit available by 2026-09-02. | CISA issues a public advisory confirming that the Gunra ransomware group exploited a vulnerability in Fortinet firewalls between 2026-08-30 and 2026-09-02, with a public exploit available by 2026-09-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-21 and 2026-08-24, a drone strike using a Russian-made Shahed-136 variant will be confirmed by at least two independent outl" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world; statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition

## III. LEDGER STANDING

465 issued all-time across 14 forecaster arms · 413 open (4 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 53 issued · 51 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 46 | 46 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 53 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*