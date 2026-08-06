**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-05_1501.md · forecaster: manual/sonnet-5/unattested · 2 accepted / 6 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260806-07 | 90% | 2026-08-24 | disaster | Between 2026-08-06 and 2026-08-20, the USGS Earthquake Catalog will record at least one earthquake of magnitude 6.0 or greater anywhere in the world. | True if the USGS Earthquake Catalog lists any event of magnitude 6.0 or greater with origin time between 2026-08-06 and 2026-08-20, checked 2026-08-24; false otherwise. |
| KKR-20260806-08 | 55% | 2026-11-10 | political | Abdul El-Sayed will win the 2026 Michigan US Senate general election held on 2026-11-03. | True if official Michigan certified results or an AP race call name Abdul El-Sayed the winner of the Michigan US Senate general election, checked 2026-11-10; false otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-05 and 2026-09-19, the CISA Known Exploited Vulnerabilities catalog will change the Known Ransomware Campaign Use field for " → REJECTED: event window opens 2026-08-05, before this row is sealed (2026-08-06) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-05 and 2026-08-26, Open VSX or the Eclipse Foundation will report that the cumulative count of malicious Evil Twin-style ext" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-05, before this row is sealed (2026-08-06) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-06 and 2026-09-30, the S&P 500 index will close down 5.0% or more relative to the prior trading day close on at least one tr" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "At its September 15-16, 2026 meeting, the FOMC will raise the federal funds target range above its 2026-08-05 level of 3.50-3.75%." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-08-05, before this row is sealed (2026-08-06) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names a different subject than the statement — the claim is about FOMC and the resolution settles on Federal, Reserve, True. A row whose resolution checks a different fact can be scored correct while being wrong; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-05 and 2026-09-05, the US State Department, Omani Ministry of Foreign Affairs, or Iranian Foreign Ministry will publicly ann" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-05, before this row is sealed (2026-08-06) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-05 and 2026-10-05, the House Committee on Ethics will publicly announce a finding, report, or disciplinary recommendation re" → REJECTED: event window opens 2026-08-05, before this row is sealed (2026-08-06) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

332 issued all-time across 14 forecaster arms · 287 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 24 issued · 24 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*