# The forgetting curve - resolution lag (LAG-1016)

As of 2026-10-17. Ledger rows: 4406. Scored with a deadline and a resolved date: 1025. Open past deadline: 546.

Lag = resolved_date minus deadline, in days. A row the desk forgets sits in the right-hand buckets. No pooled score is printed (RPAS 5.04: a Brier belongs to one forecaster); the lag table carries counts and hit share only, and Brier appears per arm below.

## Lag of scored rows

| bucket | rows | hit share |
|---|---|---|
| on-or-before deadline | 13 | 0.15 |
| 1-3 d | 297 | 0.53 |
| 4-7 d | 462 | 0.47 |
| 8-14 d | 152 | 0.60 |
| 15-30 d | 93 | 0.46 |
| over 30 d | 8 | 0.62 |

Median lag 5 d; 90th percentile 14 d; max 39 d; share resolved on or before deadline 0.01.

## Lag by arm (scored rows)

| arm | rows | median lag d | over 14 d | Brier |
|---|---|---|---|---|
| lmstudio/auto | 271 | 5 | 6 | 0.208 |
| control/baserate | 264 | 5 | 23 | 0.313 |
| manual/sonnet-5/unattested | 131 | 6 | 19 | 0.249 |
| manual/fable-5/unattested | 70 | 6 | 10 | 0.190 |
| lmstudio/realist | 58 | 8 | 17 | 0.296 |
| manual/opus-5/unattested | 51 | 5 | 4 | 0.182 |
| manual/fable-5.1/unattested | 50 | 5 | 3 | 0.248 |
| manual/sonnet-5 | 39 | 6 | 3 | 0.262 |
| manual/opus-5 | 30 | 5 | 5 | 0.210 |
| manual/fable | 27 | 3 | 1 | 0.180 |
| manual/fable-5 | 18 | 6 | 2 | 0.164 |

## Open rows past deadline (the queue the desk is forgetting)

| overdue age | rows | arms |
|---|---|---|
| 1-3 d | 108 | control/baserate 36, manual/sonnet-5/unattested 14, lmstudio/realist 14 |
| 4-7 d | 186 | control/baserate 66, manual/sonnet-5/unattested 28, lmstudio/auto 25 |
| 8-14 d | 134 | lmstudio/auto 55, control/baserate 28, lmstudio/realist 20 |
| 15-30 d | 95 | control/baserate 23, lmstudio/realist 22, lmstudio/auto 16 |
| over 30 d | 23 | lmstudio/auto 12, manual/sonnet-5/unattested 4, control/baserate 4 |

Ten oldest open rows:

- KKR-20260817-36 deadline 2026-08-26 (52 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Dnipro with at least
- KKR-20260819-01 deadline 2026-08-28 (50 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, at least one report from a hostile side in the Israel-G
- KKR-20260809-02 deadline 2026-09-02 (45 d) lmstudio/auto - Between 2026-08-27 and 2026-08-30, a new cyberattack targeting a U.S. government system is
- KKR-20260815-25 deadline 2026-09-02 (45 d) lmstudio/auto - At least one major wildfire in Europe causes over 100 evacuations between 2026-08-21 and 2
- KKR-20260820-04 deadline 2026-09-02 (45 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a new military offensive will be reported in the Zapori
- KKR-20260824-06 deadline 2026-09-04 (43 d) lmstudio/auto - A new cyberattack campaign targeting critical infrastructure in the U.S. will be attribute
- KKR-20260808-04 deadline 2026-09-07 (40 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a new wildfire will be reported in the United States by
- KKR-20260827-63 deadline 2026-09-07 (40 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed cyberattack exploiting CVE-2021-23758 will 
- KKR-20260827-64 deadline 2026-09-07 (40 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed forest fire will be reported in Canada with
- KKR-20260827-65 deadline 2026-09-07 (40 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed political statement by Trump regarding Iran

Reading rule: compare each arm's over-14-day count with its row count; an arm whose late rows cluster is an arm whose claims the desk cannot look up, and that is a property of the claims, not of the lateness. Either way the queue table is the to-do list; the keys pass runs before each sitting and the overdue rows are the sitting.
