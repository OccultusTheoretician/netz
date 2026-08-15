**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151727Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-15_1726.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260815-23 | 30% | 2026-08-30 | disaster | A magnitude 7.0 or greater earthquake occurs in Indonesia between 2026-08-21 and 2026-08-28, with a depth between 10km and 150km and a confirmed death toll of at least 10. | The USGS Significant Quakes catalog records an event with magnitude >= 7.0, depth between 10km and 150km, location within Indonesia, and a confirmed death toll of at least 10 as reported by two independent wire services (BBC World, Al Jazeera) by 2026-08-30. |
| KKR-20260815-24 | 45% | 2026-09-02 | military/conflict | At least 12 people are killed in Israeli airstrikes on southern Lebanon between 2026-08-21 and 2026-08-28, confirmed by two independent sources (BBC World, Al Jazeera). | Two independent sources (BBC World, Al Jazeera) report a confirmed death toll of at least 12 in Israeli airstrikes on southern Lebanon between 2026-08-21 and 2026-08-28, with the event window ending no later than 2026-08-28. |
| KKR-20260815-25 | 20% | 2026-09-02 | disaster | At least one major wildfire in Europe causes over 100 evacuations between 2026-08-21 and 2026-08-28, confirmed by two independent sources (BBC World, Al Jazeera). | Two independent sources (BBC World, Al Jazeera) report that a wildfire in Europe caused over 100 evacuations between 2026-08-21 and 2026-08-28. |
| KKR-20260815-26 | 25% | 2026-09-02 | political | A new political alliance is formally announced between Turkey, Saudi Arabia, and Pakistan between 2026-08-21 and 2026-08-28, confirmed by two independent sources (Al Jazeera, BBC World). | Two independent sources (Al Jazeera, BBC World) report the formal announcement of a new defense or political alliance between Turkey, Saudi Arabia, and Pakistan between 2026-08-21 and 2026-08-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A cyberattack exploiting a vulnerability listed in the CISA KEV catalog between 2026-08-21 and 2026-08-28 results in a confirmed breach of a" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The S&P 500 closes above 7,850 on any trading day between 2026-08-21 and 2026-08-28." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution offers alternative VENUES joined by 'or' (…d by the federal reserve economic data (fred) | or | a major exchange (e…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new political statement by Donald Trump regarding the Strait of Hormuz is published in a major U.S. news outlet between 2026-08-21 and 202" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A new Linux-based botnet, identified as Evooo1Bot, is confirmed to have infected at least 50,000 devices globally between 2026-08-21 and 202" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The U.S. Strategic Petroleum Reserve (SPR) reaches a level below 350 million barrels by 2026-08-28." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-28 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "A new vulnerability in a major AI model's codebase is publicly disclosed and exploited between 2026-08-21 and 2026-08-28, confirmed by a cyb" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

626 issued all-time across 14 forecaster arms · 570 open (34 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 74 issued · 72 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 116 | 116 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 74 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 35 | 35 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 55 | 55 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 47 | 47 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*