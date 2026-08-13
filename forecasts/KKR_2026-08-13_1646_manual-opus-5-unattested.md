**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131646Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-13_1519.md · forecaster: manual/opus-5/unattested · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260813-22 | 80% | 2026-09-22 | cyber | Between 2026-08-14 and 2026-09-18, CISA adds at least one Microsoft SharePoint Server CVE to the Known Exploited Vulnerabilities catalog. | The CISA KEV catalog JSON contains an entry with vendorProject Microsoft and a product string naming SharePoint, carrying a dateAdded value between 2026-08-14 and 2026-09-18 inclusive. |
| KKR-20260813-23 | 85% | 2026-10-01 | military_conflict | Between 2026-08-17 and 2026-09-27, Ukrainian forces strike a Russian Black Sea port, oil terminal, or grain terminal, and both sides acknowledge the strike. | A Russian regional governor or the Russian Defence Ministry and a Ukrainian military or intelligence source each describe a strike on a Russian Black Sea port facility occurring inside the window, carried by Reuters or AFP. |
| KKR-20260813-24 | 38% | 2026-09-24 | military_conflict | Between 2026-08-17 and 2026-09-20, Iranian forces seize, board, or detain at least one commercial vessel in the Strait of Hormuz or the Gulf of Oman. | UKMTO issues an incident advisory and Reuters or Lloyds List reports an Iranian seizure, boarding, or detention of a commercial vessel in those waters occurring inside the window. |
| KKR-20260813-25 | 74% | 2026-10-05 | political | A named successor to Karoline Leavitt as White House press secretary is publicly announced between 2026-08-14 and 2026-09-30. | The White House or the President names a specific individual as press secretary or acting press secretary inside the window, reported by both the Associated Press and Reuters. |
| KKR-20260813-26 | 22% | 2026-09-18 | disaster | USGS records at least one magnitude 6.0 or greater earthquake within 250 km of the epicenter of event us6000tjl2, with origin time between 2026-08-17 and 2026-09-14. | A USGS ComCat query returns one or more events of magnitude 6.0 or above within 250 km of the us6000tjl2 epicenter with origin time inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-14 and 2026-11-13, a putative class action arising from the Trezor customer data breach is filed in a United States federal " → REJECTED: resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "WTI front-month crude settles at or above 95.00 dollars per barrel on at least one trading day between 2026-08-17 and 2026-09-30." → REJECTED: the resolution names a different subject than the statement — the claim is about WTI and the resolution settles on CME, Crude, Light, NYMEX. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Treasury 10-year constant maturity par yield closes at or below 4.25 percent on at least one business day between 2026-08-17 and 2026-11" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Electoral Commission of Zambia declares the incumbent president the winner of the 2026 general election, with the declaration made betwe" → REJECTED: the resolution names a different subject than the statement — the claim is about Commission, Electoral, Zambia and the resolution settles on BBC, ECZ, News, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "Tropical cyclone ONE-C of the 2026 Central Pacific season is carried at hurricane strength, 64 knots or greater, in an advisory issued betwe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…tral pacific hurricane center public advisory | or | the nhc advisory archive lists maximum sustai…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

581 issued all-time across 14 forecaster arms · 525 open (7 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 49 issued · 49 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 96 | 96 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 64 | 62 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 49 | 49 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*