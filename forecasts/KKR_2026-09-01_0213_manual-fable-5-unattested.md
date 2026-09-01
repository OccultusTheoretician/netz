**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 010213Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-31_1519.md · forecaster: manual/fable-5/unattested · 3 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260901-06 | 30% | 2026-09-18 | economics/markets | The FOMC decision announced 2026-09-16 raises the federal funds target range above the range in effect on 2026-09-15. | True if the Federal Reserve implementation note or FRED series DFEDTARU shows a target range effective after the 2026-09-16 decision higher than the range in effect on 2026-09-15; false if unchanged or lower. |
| KKR-20260901-07 | 30% | 2026-10-05 | political | A lapse in United States federal appropriations begins on 2026-10-01, with agency shutdown procedures taking effect that day. | True if no enacted appropriations act or continuing resolution covers 2026-10-01 and OMB directs agencies to execute shutdown plans that day; Congress.gov enacted-legislation records govern. |
| KKR-20260901-08 | 12% | 2026-11-04 | military/conflict | Commercial shipping transit through the Strait of Hormuz is suspended for at least 48 consecutive hours at any point between 2026-09-01 and 2026-10-31. | True if at least two international wire services, citing shipping authorities or maritime insurers, report a suspension of commercial Strait of Hormuz transits lasting 48 or more consecutive hours between 2026-09-01 and 2026-10-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

1223 issued all-time across 14 forecaster arms · 1062 open (99 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 128 issued · 127 open · 1 resolved · 1 hits / 0 misses · **Brier 0.090** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 323 | 306 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 128 | 127 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 153 | 150 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 139 | 131 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*