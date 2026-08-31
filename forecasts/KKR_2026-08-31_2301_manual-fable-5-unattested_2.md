**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-31_1519.md · forecaster: manual/fable-5/unattested · 5 accepted / 5 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-83 | 90% | 2026-10-05 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least 8 entries with a dateAdded value between 2026-09-01 and 2026-09-30. | True if a fetch of the CISA KEV catalog on or after the deadline shows 8 or more entries whose dateAdded falls between 2026-09-01 and 2026-09-30 inclusive. |
| KKR-20260831-84 | 55% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures settle at or above 95.00 USD per barrel on at least one trading day between 2026-09-01 and 2026-10-30. | True if any official ICE Brent front-month daily settlement price between 2026-09-01 and 2026-10-30 is at or above 95.00 USD; exchange settlement records govern. |
| KKR-20260831-85 | 45% | 2026-11-03 | disaster | The Nepal government confirmed death toll from the August 2026 flood disaster reaches at least 300 at any point between 2026-08-31 and 2026-10-30. | True if Nepali government statements carried by at least two international news agencies place the confirmed dead at 300 or more on any date between 2026-08-31 and 2026-10-30. |
| KKR-20260831-86 | 70% | 2026-12-01 | political | Democratic candidates win at least 218 seats in the United States House of Representatives in the general election held 2026-11-03. | True if Associated Press race calls as of the deadline show Democratic candidates winning 218 or more House seats from the 2026-11-03 general election. |
| KKR-20260831-87 | 50% | 2026-12-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry with vendorProject Cisco and a dateAdded value between 2026-09-01 and 2026-11-30. | True if the KEV catalog contains an entry whose vendorProject value is Cisco and whose dateAdded falls between 2026-09-01 and 2026-11-30 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC decision announced 2026-09-16 raises the federal funds target range above the range in effect on 2026-09-15." → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal reserve implementation note | or | fred…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one commercial tanker in the Persian Gulf or Gulf of Oman sustains physical damage from an attack between 2026-09-01 and 2026-09-30" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A lapse in United States federal appropriations begins on 2026-10-01, with agency shutdown procedures taking effect that day." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-01 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution names a different subject than the statement — the claim is about States, United and the resolution settles on Congress, OMB. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Massachusetts murder trial of Lindsay Clancy concludes with a jury verdict or a declared mistrial between 2026-08-31 and 2026-10-30." → REJECTED: the resolution names only a venue or register (county, court, plymouth, superior) and no subject - the register is where to look, not what is claimed; name the subject inside it; the resolution names a different subject than the statement — the claim is about Clancy, Lindsay, Massachusetts and the resolution settles on County, Court, Plymouth, Superior. A row whose resolution checks a different fact can be scored correct while being wrong
- "Commercial shipping transit through the Strait of Hormuz is suspended for at least 48 consecutive hours at any point between 2026-09-01 and " → REJECTED: resolution offers alternative VENUES joined by 'or' (…al wire services, citing shipping authorities | or | maritime insurers, report a suspension of com…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1210 issued all-time across 14 forecaster arms · 1049 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 125 issued · 124 open · 1 resolved · 1 hits / 0 misses · **Brier 0.090** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 318 | 301 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 125 | 124 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 150 | 147 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 137 | 129 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*