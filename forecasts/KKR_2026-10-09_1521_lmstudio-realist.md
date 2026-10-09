**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-06 | 25% | 2026-10-25 | cyber | Between 2026-10-16 and 2026-10-23, at least one new cyberattack exploiting CVE-2016-3081 in Apache Struts will be reported in at least two independent public sources. | At least two independent public sources (e.g., BleepingComputer, The Hacker News, or CISA) report a confirmed cyberattack exploiting CVE-2016-3081 in Apache Struts between 2026-10-16 and 2026-10-23. |
| KKR-20261009-07 | 35% | 2026-10-25 | disaster | Between 2026-10-16 and 2026-10-23, at least one new tropical storm or hurricane will make landfall in the United States with a storm surge warning in effect. | At least one tropical storm or hurricane makes landfall in the United States between 2026-10-16 and 2026-10-23, with a storm surge warning issued by the National Hurricane Center (NHC) for the affected area. |
| KKR-20261009-08 | 30% | 2026-10-25 | cyber | Between 2026-10-16 and 2026-10-23, at least one new cyberattack exploiting a zero-day vulnerability in a widely used open-source project will be reported in at least two independent public sources. | At least two independent public sources (e.g., BleepingComputer, The Hacker News, or CISA) report a confirmed cyberattack exploiting a zero-day vulnerability in a widely used open-source project between 2026-10-16 and 2026-10-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-16 and 2026-10-23, the CISA KEV catalog will include at least one vulnerability with a date-added value between 2026-10-08 a" → REJECTED: cited items name China, Ireland, Japan; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-16 and 2026-10-23, the S&P 500 will close above 7,850 points on at least one weekday." → REJECTED: cites 13 of 137 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim; market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-10-16 and 2026-10-23, the U.S. Federal Reserve will announce a 0.5 percentage point increase in the federal funds rate." → REJECTED: cites 13 of 137 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim; resolution offers alternative VENUES joined by 'or' (…federal reserve board | or | a major financial…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-16 and 2026-10-23, at least one new military conflict event (e.g., drone strike, artillery attack, missile launch) will be c" → REJECTED: cites 131 of 137 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim
- "Between 2026-10-16 and 2026-10-23, at least one new cyberattack exploiting a vulnerability in a government or defense contractor system will" → REJECTED: resolution offers alternative VENUES joined by 'or' (…vulnerability in a government | or | defense contractor…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-16 and 2026-10-23, at least one new political event (e.g., resignation, indictment, major policy announcement) involving a U" → REJECTED: cites 25 of 137 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-16 and 2026-10-23, at least one new natural disaster (e.g., wildfire, flood, earthquake) with a green alert issued by GDACS " → REJECTED: cites 19 of 137 items in the record — a prior that excludes nothing predicts nothing, and a keyless determination against the whole record is a determination against no record; cite the items that ground THIS claim

## III. LEDGER STANDING

3708 issued all-time across 21 forecaster arms · 2894 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 200 issued · 165 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1320 | 1119 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 405 | 226 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 200 | 165 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 293 | 260 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 121 | 121 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 80 | 80 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*