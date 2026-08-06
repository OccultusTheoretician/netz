**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-05_1501.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260806-01 | 48% | 2026-11-03 | economics | ICE Brent front-month crude futures settle at or below 70.00 USD per barrel on at least one settlement date between 2026-08-06 and 2026-10-30. | Any ICE-published front-month Brent settlement price with a settlement date between 2026-08-06 and 2026-10-30 is 70.00 or lower. |
| KKR-20260806-02 | 35% | 2026-12-18 | economics | A filing entered on the US Court of International Trade docket between 2026-08-06 and 2026-12-15 states that cumulative IEEPA tariff refunds issued have reached 150 billion USD or more. | A government filing on the CIT docket dated inside the window states cumulative IEEPA refunds of at least 150 billion USD. A lower stated figure resolves false. |
| KKR-20260806-03 | 35% | 2026-12-04 | military_conflict | UKMTO issues an incident advisory, or CENTCOM issues a statement, reporting an attack on or seizure of a commercial vessel in the Strait of Hormuz or Gulf of Oman between 2026-08-06 and 2026-11-30. | A UKMTO advisory or CENTCOM statement dated inside the window reports an attack on or seizure of a commercial vessel in the named waters. |
| KKR-20260806-04 | 18% | 2027-01-06 | cyber | The CISA KEV catalog carries at least one entry naming Gitea in its vendorProject or product field, with a dateAdded value between 2026-08-06 and 2026-12-31. | A CISA KEV entry naming Gitea in vendorProject or product carries a dateAdded value inside the window. No such entry resolves false. |
| KKR-20260806-05 | 38% | 2026-10-05 | disaster | The USGS earthquake catalog lists at least one event of magnitude 6.0 or greater within 300 km of the epicenter of USGS event us6000ti6x, with an origin time between 2026-08-06 and 2026-09-30. | A USGS FDSN event query for magnitude 6.0 or greater, radius 300 km around the us6000ti6x epicenter, origin time inside the window, returns one or more events. |
| KKR-20260806-06 | 55% | 2026-12-04 | political | The House Committee on Ethics publishes a statement or report on ethics.house.gov naming Representative Max Miller, dated between 2026-08-06 and 2026-11-30. | A document published on ethics.house.gov and dated inside the window names Representative Max Miller. No such document resolves false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FRED series DFEDTARU records a value on 2026-12-31 strictly higher than its value on 2026-08-05, reflecting a rate increase at the 2026-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A single Russian strike event on Kyiv city or Kyiv oblast between 2026-08-06 and 2026-09-15 kills 10 or more people according to Ukrainian a" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "German federal or Saxony state authorities announce at least one arrest in the investigation of the explosive-laden drone found at Leipzig/H" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The CISA KEV catalog carries 50 or more entries with a dateAdded value between 2026-08-06 and 2026-10-05 inclusive." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

330 issued all-time across 14 forecaster arms · 285 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 31 issued · 31 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 17 | 15 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 21 | 31 | 9 | 22 | 0.222 | 29.0% | 0.206 | -0.075 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 22 | 22 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*