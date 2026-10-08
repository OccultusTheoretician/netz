**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-01 | 25% | 2026-10-23 | cyber | On 2026-10-15, the CISA KEV catalog will include at least one new entry for a vulnerability with CVSS score 10.0 or higher. | The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-21, and the vulnerability has a CVSS score of 10.0 or higher. |
| KKR-20261008-02 | 40% | 2026-10-29 | disaster | Between 2026-10-20 and 2026-10-27, a tropical storm will make landfall in the U.S. Gulf Coast with a storm surge exceeding 6 feet. | The National Hurricane Center (NHC) issues a storm surge warning of 6 feet or higher for a U.S. Gulf Coast location during the event window of 2026-10-20 to 2026-10-27. |
| KKR-20261008-03 | 35% | 2026-11-02 | cyber | Between 2026-10-22 and 2026-10-29, a cyberattack exploiting a known vulnerability in Microsoft Teams will be confirmed by CISA. | CISA issues a public advisory between 2026-10-22 and 2026-10-29 stating that a cyberattack exploited a vulnerability in Microsoft Teams, with the vulnerability listed in the KEV catalog. |
| KKR-20261008-04 | 55% | 2026-10-30 | economics/markets | Between 2026-10-21 and 2026-10-28, the 10-year Treasury yield will exceed 5.5% on at least one trading day. | The 10-year Treasury yield exceeds 5.5% on at least one weekday between 2026-10-21 and 2026-10-28, as reported by the U.S. Department of the Treasury or FRED. |
| KKR-20261008-05 | 20% | 2026-11-03 | disaster | Between 2026-10-23 and 2026-10-30, a new earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific Ring of Fire. | The USGS Significant Quakes database records at least one earthquake with magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-23 and 2026-10-30. |
| KKR-20261008-06 | 28% | 2026-11-04 | cyber | Between 2026-10-24 and 2026-10-31, a major cyberattack on a U.S. financial institution will be confirmed by the FBI. | The FBI issues a public statement between 2026-10-24 and 2026-10-31 confirming a cyberattack on a U.S. financial institution that resulted in data compromise or service disruption. |
| KKR-20261008-07 | 45% | 2026-11-05 | political | Between 2026-10-25 and 2026-11-01, a new political scandal involving a U.S. government official will be reported by at least two independent outlets with differing political affiliations. | At least two independent news outlets with differing political affiliations (e.g., BBC, Guardian, CNBC, NPR) publish a report between 2026-10-25 and 2026-11-01 confirming a political scandal involving a U.S. government official. |
| KKR-20261008-08 | 32% | 2026-11-06 | cyber | Between 2026-10-26 and 2026-11-02, a new ransomware attack will be linked to a known cybercrime group via public attribution by a cybersecurity firm. | A cybersecurity firm (e.g., BleepingComputer, The Hacker News) publishes a report between 2026-10-26 and 2026-11-02 attributing a ransomware attack to a known cybercrime group (e.g., LockBit, Conti, DarkSide). |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-18 and 2026-10-25, a Russian drone strike will result in at least one confirmed casualty in Kyiv." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-19 and 2026-10-26, the S&P 500 will close above 7,850 on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…nyse | or | nasdaq official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3620 issued all-time across 21 forecaster arms · 2806 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 400 issued · 221 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1292 | 1091 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*