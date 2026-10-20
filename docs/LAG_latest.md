# The forgetting curve - resolution lag (LAG-1016)

As of 2026-10-20. Ledger rows: 4631. Scored with a deadline and a resolved date: 1265. Open past deadline: 422.

Lag = resolved_date minus deadline, in days. A row the desk forgets sits in the right-hand buckets. No pooled score is printed (RPAS 5.04: a Brier belongs to one forecaster); the lag table carries counts and hit share only, and Brier appears per arm below.

## Lag of scored rows

| bucket | rows | hit share |
|---|---|---|
| on-or-before deadline | 13 | 0.15 |
| 1-3 d | 314 | 0.54 |
| 4-7 d | 645 | 0.50 |
| 8-14 d | 177 | 0.60 |
| 15-30 d | 106 | 0.51 |
| over 30 d | 10 | 0.70 |

Median lag 6 d; 90th percentile 14 d; max 52 d; share resolved on or before deadline 0.01.

## Lag by arm (scored rows)

| arm | rows | median lag d | over 14 d | Brier |
|---|---|---|---|---|
| control/baserate | 351 | 6 | 25 | 0.316 |
| lmstudio/auto | 289 | 5 | 10 | 0.209 |
| manual/sonnet-5/unattested | 158 | 6 | 21 | 0.251 |
| lmstudio/realist | 86 | 8 | 21 | 0.321 |
| manual/fable-5/unattested | 84 | 6 | 10 | 0.193 |
| manual/fable-5.1/unattested | 73 | 5 | 3 | 0.233 |
| manual/opus-5/unattested | 69 | 6 | 5 | 0.195 |
| manual/sonnet-5 | 40 | 6 | 4 | 0.256 |
| manual/opus-5 | 32 | 5 | 5 | 0.204 |
| manual/fable | 27 | 3 | 1 | 0.180 |
| manual/fable-5 | 23 | 6 | 3 | 0.170 |
| manual/opus-5.5/unattested | 11 | 7 | 0 | 0.362 |

## Open rows past deadline (the queue the desk is forgetting)

| overdue age | rows | arms |
|---|---|---|
| 1-3 d | 117 | control/baserate 49, manual/sonnet-5/unattested 20, manual/opus-5/unattested 13 |
| 4-7 d | 55 | control/baserate 17, manual/sonnet-5/unattested 10, lmstudio/auto 10 |
| 8-14 d | 105 | lmstudio/auto 45, lmstudio/realist 22, control/baserate 19 |
| 15-30 d | 112 | lmstudio/auto 29, control/baserate 27, lmstudio/realist 20 |
| over 30 d | 33 | lmstudio/auto 14, control/baserate 7, manual/sonnet-5/unattested 6 |

Ten oldest open rows:

- KKR-20260817-36 deadline 2026-08-26 (55 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Dnipro with at least
- KKR-20260809-02 deadline 2026-09-02 (48 d) lmstudio/auto - Between 2026-08-27 and 2026-08-30, a new cyberattack targeting a U.S. government system is
- KKR-20260815-25 deadline 2026-09-02 (48 d) lmstudio/auto - At least one major wildfire in Europe causes over 100 evacuations between 2026-08-21 and 2
- KKR-20260820-04 deadline 2026-09-02 (48 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a new military offensive will be reported in the Zapori
- KKR-20260824-06 deadline 2026-09-04 (46 d) lmstudio/auto - A new cyberattack campaign targeting critical infrastructure in the U.S. will be attribute
- KKR-20260808-04 deadline 2026-09-07 (43 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a new wildfire will be reported in the United States by
- KKR-20260827-63 deadline 2026-09-07 (43 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed cyberattack exploiting CVE-2021-23758 will 
- KKR-20260827-64 deadline 2026-09-07 (43 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed forest fire will be reported in Canada with
- KKR-20260827-65 deadline 2026-09-07 (43 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed political statement by Trump regarding Iran
- KKR-20260822-05 deadline 2026-09-08 (42 d) manual/sonnet-5/unattested - At the sentencing hearing scheduled for 2026-09-04 at Preston Crown Court, at least one of

Reading rule: compare each arm's over-14-day count with its row count; an arm whose late rows cluster is an arm whose claims the desk cannot look up, and that is a property of the claims, not of the lateness. Either way the queue table is the to-do list; the keys pass runs before each sitting and the overdue rows are the sitting.
