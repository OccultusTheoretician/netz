**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092008Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-09_1516.md · forecaster: manual/sonnet-5 · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260809-13 | 80% | 2026-08-18 | political | On 2026-08-11, the South Carolina Republican special primary for U.S. Senate fails to produce a majority winner among the nine-candidate field, triggering a runoff. | South Carolina State Election Commission certified results or an AP call confirms the vote share of the leading candidate was below 50 percent, requiring a runoff. |
| KKR-20260809-14 | 30% | 2026-09-17 | military/conflict | Between 2026-08-16 and 2026-09-15, the Yemen-based Houthi movement claims responsibility for a new attack on Saudi Arabian oil, gas, or energy infrastructure, separate from the 2026-08-09 Aramco refinery incident. | At least two independent outlets (e.g. Reuters, AP, Al Jazeera) report a Houthi-claimed attack on Saudi energy infrastructure occurring between 2026-08-16 and 2026-09-15. |
| KKR-20260809-15 | 92% | 2026-09-17 | military/conflict | Between 2026-08-16 and 2026-09-15, at least one additional Russian missile, drone, or artillery strike on Odesa oblast, Ukraine is reported and corroborated by sources on both the Russian and Ukrainian sides. | At least two independently-biased public sources, one Russian-aligned and one Ukrainian-aligned, or two independent wire services, report a strike on Odesa oblast within the window. |
| KKR-20260809-16 | 7% | 2026-08-22 | crime/security | Between 2026-08-09 and 2026-08-20, an Irish court grants Daniel Kinahan bail pending trial, rather than remanding him in custody at every hearing. | Irish Times, RTE, or Irish Examiner reporting confirms a court granted Kinahan bail at any hearing occurring in the window. |
| KKR-20260809-17 | 55% | 2026-11-12 | economics/markets | The Form 10-Q filed by Berkshire Hathaway for the quarter ended 2026-09-30 reports cash, cash equivalents, and short-term investments below 365.5 billion dollars, continuing the Q2 decline. | The Form 10-Q filed on SEC EDGAR by Berkshire Hathaway for the quarter ended 2026-09-30, filed between 2026-10-01 and 2026-11-10, shows cash and equivalents under 365.5 billion dollars. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-16 and 2026-09-15, the Israeli government publicly reverses course and endorses the Trump-brokered Gaza peace framework it r" → REJECTED: resolution offers alternative VENUES joined by 'or' (…official israeli government | or | netanyahu…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "On 2026-08-11, Francesca Hong places first in the Wisconsin Democratic gubernatorial primary among the four active candidates: Hong, David C" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-11 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "At some daily close between 2026-08-16 and 2026-09-15, NYMEX WTI crude front-month futures settle at or above 85.00 dollars per barrel." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-16 and 2026-10-15, Meta Platforms publishes a public retrospective or incident report on the Irregular-linked AI cybersecuri" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-09 and 2026-08-30, an earthquake of magnitude 5.5 or greater occurs within 150 km of the 2026-08-09 M6.3 Sarangani, Philippi" → REJECTED: the resolution names a different subject than the statement — the claim is about Philippines, Sarangani and the resolution settles on ANSS, Comcat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

420 issued all-time across 14 forecaster arms · 368 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5`:** 35 issued · 33 open · 2 resolved · 1 hits / 1 misses · **Brier 0.265** against its own base rate 50.0% (climatological 0.250) · **skill -0.060** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 35 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 35 | 33 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*