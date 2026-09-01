**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-01_1518.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260901-11 | 30% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-09-24, at least one report from a hostile side confirms a drone strike on Kyiv with casualties claimed by Ukrainian sources. | At least one report from a hostile side (RU or UA) confirms a drone strike on Kyiv during the window, with casualties claimed in at least one corroborating report. |
| KKR-20260901-12 | 40% | 2026-10-06 | disaster | Between 2026-09-21 and 2026-09-24, a tropical storm makes landfall in Texas with a storm surge warning issued by the National Weather Service. | The National Weather Service issues a storm surge warning for a tropical storm making landfall in Texas between 2026-09-21 and 2026-09-24. |
| KKR-20260901-13 | 20% | 2026-10-07 | cyber | Between 2026-09-21 and 2026-09-24, a cyberattack exploiting CVE-2026-81578 results in unauthorized access to a critical infrastructure system. | A confirmed cyberattack exploiting CVE-2026-81578 results in unauthorized access to a critical infrastructure system, as reported by a public source. |
| KKR-20260901-14 | 35% | 2026-10-08 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield exceeds 4.85 percent on a weekday. | The 10-year U.S. Treasury yield exceeds 4.85 percent on a weekday between 2026-09-21 and 2026-09-24. |
| KKR-20260901-15 | 30% | 2026-10-07 | disaster | Between 2026-09-21 and 2026-09-24, a major wildfire in France causes damage to a wine-producing region as confirmed by Al Jazeera. | Al Jazeera publishes a report confirming a major wildfire in France that causes damage to a wine-producing region between 2026-09-21 and 2026-09-24. |
| KKR-20260901-16 | 25% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a cyberattack attributed to Russia-aligned actors targets a U.S. government agency using a previously unreported exploit. | A cyberattack attributed to Russia-aligned actors targets a U.S. government agency using a previously unreported exploit, confirmed by at least two independent sources. |
| KKR-20260901-17 | 10% | 2026-10-08 | political | Between 2026-09-21 and 2026-09-24, a new political summit involving Russia, Iran, and the U.S. is confirmed by at least two hostile sides. | At least two hostile sides (e.g., RU, WEST, AXIS) confirm the existence of a new political summit involving Russia, Iran, and the U.S. between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2026-82078 with a date-added value of 2026-08-31." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-82078 dateAdded 2026-08-31, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, the S&P 500 closes above 7,700 points on a weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-21 and 2026-09-24, Iran announces a new nuclear enrichment program at a site not previously reported." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1232 issued all-time across 14 forecaster arms · 1071 open (99 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 184 issued · 153 open · 29 resolved · 10 hits / 19 misses · **Brier 0.250** against its own base rate 34.5% (climatological 0.226) · **skill -0.109** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 323 | 306 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 184 | 153 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 130 | 129 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 153 | 150 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 139 | 131 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*