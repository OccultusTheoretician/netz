**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270427Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-26_1538.md · forecaster: manual/opus-5/unattested · 1 accepted / 1 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-22 | 30% | 2026-09-18 | economics | The FOMC raises the federal funds target range at its scheduled meeting on 2026-09-16, moving it above the 3.50 to 3.75 percent range held since 2026-07-29. | FRED series DFEDTARU shows an upper limit above 3.75 percent effective 2026-09-17, matching the FOMC policy statement released 2026-09-16. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Europe Brent spot crude prints at or below 75.00 US dollars per barrel on at least one business day between 2026-09-01 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

945 issued all-time across 14 forecaster arms · 855 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 114 issued · 114 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 114 | 114 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*