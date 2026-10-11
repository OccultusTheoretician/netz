**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111524Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: lmstudio/qwen36-realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-14 | 30% | 2026-10-22 | economics/markets | The S&P 500 index closes below 7,500 on at least one trading day between 2026-10-16 and 2026-10-20. | A market close recorded below 7,500. Reference: 7,811.54 on the packet date. |
| KKR-20261011-15 | 45% | 2026-10-21 | military/conflict | A Houthi missile or drone strike hits a target inside Saudi Arabia between 2026-10-12 and 2026-10-19. | Two wire services report a kinetic strike by Houthi forces on Saudi territory within the window. |
| KKR-20261011-16 | 20% | 2026-10-21 | disaster | A magnitude 7.0 or greater earthquake occurs in Panama between 2026-10-12 and 2026-10-19. | The USGS catalog carries a date-added value for an event with magnitude 7.0 or higher in Panama. |
| KKR-20261011-17 | 30% | 2026-10-29 | military/conflict | A Houthi blockade or strike disrupts commercial shipping in the Strait of Hormuz between 2026-10-20 and 2026-10-27. | Two wire services report a disruption to commercial shipping in the Strait of Hormuz caused by Houthi actions. |
| KKR-20261011-18 | 15% | 2026-10-29 | disaster | A magnitude 6.5 or greater earthquake occurs in Panama between 2026-10-20 and 2026-10-27. | The USGS catalog carries a date-added value for an event with magnitude 6.5 or higher in Panama. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a critical infrastructure vulnerability between 2026-10-12 and 2026-10-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Polish authorities file formal charges against the alleged assassins of Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19." → REJECTED: resolution offers alternative VENUES joined by 'or' (…polish court docket | or | wire…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The 10-year US Treasury yield closes above 5.50 percent on at least one trading day between 2026-10-16 and 2026-10-20." → REJECTED: the resolution names a different subject than the statement — the claim is about Treasury and the resolution settles on Reference. A row whose resolution checks a different fact can be scored correct while being wrong
- "A new critical infrastructure vulnerability is cataloged in the CISA KEV between 2026-10-20 and 2026-10-27." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Brent crude oil price closes above 115.00 on at least one trading day between 2026-10-16 and 2026-10-20." → REJECTED: the resolution names a different subject than the statement — the claim is about Brent and the resolution settles on Reference. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3874 issued all-time across 21 forecaster arms · 3060 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 45 issued · 45 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1372 | 1171 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 27 | 27 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 312 | 279 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*