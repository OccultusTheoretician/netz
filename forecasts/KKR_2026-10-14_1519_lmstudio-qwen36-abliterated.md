**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-19 | 60% | 2026-11-24 | disaster | A magnitude 6.0 or greater earthquake is recorded by the USGS between 2026-11-15 and 2026-11-22. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake between 2026-11-15 and 2026-11-22. |
| KKR-20261014-20 | 30% | 2026-11-29 | military | A Houthi missile or drone strike hits Saudi Arabia between 2026-11-20 and 2026-11-27. | A Houthi missile or drone strike hits Saudi Arabia between 2026-11-20 and 2026-11-27. |
| KKR-20261014-21 | 70% | 2026-12-29 | political | The Pope is hospitalized for lung cancer treatment between 2026-12-20 and 2026-12-27. | The Pope is hospitalized for lung cancer treatment between 2026-12-20 and 2026-12-27. |
| KKR-20261014-22 | 15% | 2027-01-19 | disaster | A USGS recorded magnitude 7.0 or greater earthquake occurs between 2027-01-10 and 2027-01-17. | The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2027-01-10 and 2027-01-17. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-10-14 and 2026-10-21 for CVE-2026-104935." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-14..2026-10-21; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "WTI Crude closes above 94.99 on 2026-11-06." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-06 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Netflix lays off more than 1,000 employees by 2026-11-10." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The 10-year Treasury yield closes above 5.26 on 2026-12-01." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-12-01 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The S&P 500 closes below 7,741 on 2026-12-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-12-15 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Gold closes below 4,111 on 2027-02-01." → REJECTED: statement too thin to adjudicate (38 chars) — a third party reading the statement alone must be able to say what was claimed; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2027-02-01 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

4117 issued all-time across 21 forecaster arms · 3006 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 52 issued · 52 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1452 | 1156 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 52 | 52 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*