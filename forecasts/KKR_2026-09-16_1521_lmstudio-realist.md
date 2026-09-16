**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: lmstudio/realist · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-08 | 40% | 2026-10-07 | cyber | Between 2026-09-19 and 2026-09-25, a new ransomware variant exploiting the Acronis cPanel Backup Plugin vulnerability (CVE-2026-58704) is observed in at least 15 distinct organizations across Europe and North America, as confirmed by BleepingComputer and The Hacker News. | BleepingComputer and The Hacker News publish reports between 2026-09-19 and 2026-09-25 confirming that a new ransomware variant exploiting the Acronis cPanel Backup Plugin vulnerability (CVE-2026-58704) has affected at least 15 distinct organizations in Europe and North America. |
| KKR-20260916-09 | 32% | 2026-10-08 | economics/markets | Between 2026-09-18 and 2026-09-25, the 10-year U.S. Treasury yield exceeds 5.0% on at least three consecutive trading days, as confirmed by the prior-session close data from MarketWatch. | MarketWatch reports that the 10-year U.S. Treasury yield exceeded 5.0% on at least three consecutive trading days between 2026-09-18 and 2026-09-25. |
| KKR-20260916-10 | 45% | 2026-10-10 | political | On 2026-09-23, the European Union formally invites Canada to become its first associate member, as confirmed by two independent outlets (BBC World and Al Jazeera) reporting the same announcement. | Two independent outlets (BBC World and Al Jazeera) report on 2026-09-23 that the European Union formally invited Canada to become its first associate member. |
| KKR-20260916-11 | 18% | 2026-10-09 | cyber | Between 2026-09-17 and 2026-09-24, a cyberattack targeting the U.S. power grid using a previously unknown exploit is confirmed by CISA to have disrupted at least one regional grid operator, as reported by BleepingComputer and The Hacker News. | CISA confirms via the KEV catalog that a previously unknown exploit was used in a cyberattack between 2026-09-17 and 2026-09-24 to disrupt at least one regional U.S. power grid operator, as confirmed by BleepingComputer and The Hacker News. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-17, a drone strike targeting a military installation in Kharkiv, Ukraine, results in at least one confirmed casualty, as verified" → REJECTED: the named venue is introduced by 'such as', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-18 and 2026-09-24, a cyberattack exploiting CVE-2026-58704 on Google Pixel devices is confirmed by CISA to have compromised " → REJECTED: resolution offers alternative VENUES joined by 'or' (…u.s. federal agency | or | major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-58704 dateAdded 2026-09-16, before the claimed window 2026-09-18..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "On 2026-09-20, the U.S. Senate passes a resolution to end military support for Saudi Arabia in Yemen, as confirmed by two independent wire s" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-20 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-09-22, a major wildfire in Papua New Guinea, as reported by GDACS Alerts, results in the evacuation of at least 5,000 people, confir" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-22 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Between 2026-09-17 and 2026-09-23, the S&P 500 index closes below 7,500 for at least three consecutive trading days, as confirmed by the pri" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-09-21, a drone attack on a power station in Zaporizhzhia, Ukraine, causes a regional blackout affecting at least 100,000 people, con" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-21 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2237 issued all-time across 16 forecaster arms · 1835 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 73 issued · 68 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 741 | 688 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 105 | 103 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 240 | 233 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 253 | 246 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 242 | 199 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*