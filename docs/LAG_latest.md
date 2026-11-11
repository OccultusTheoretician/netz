# The forgetting curve - resolution lag (LAG-1016)

As of 2026-11-11. Ledger rows: 5593. Scored with a deadline and a resolved date: 1626. Open past deadline: 1598.

Lag = resolved_date minus deadline, in days. A row the desk forgets sits in the right-hand buckets. No pooled score is printed (RPAS 5.04: a Brier belongs to one forecaster); the lag table carries counts and hit share only, and Brier appears per arm below.

## Lag of scored rows

| bucket | rows | hit share |
|---|---|---|
| on-or-before deadline | 13 | 0.15 |
| 1-3 d | 356 | 0.53 |
| 4-7 d | 863 | 0.49 |
| 8-14 d | 194 | 0.61 |
| 15-30 d | 163 | 0.44 |
| over 30 d | 37 | 0.35 |

Median lag 6 d; 90th percentile 17 d; max 54 d; share resolved on or before deadline 0.01.

## Lag by arm (scored rows)

| arm | rows | median lag d | over 14 d | Brier |
|---|---|---|---|---|
| control/baserate | 477 | 6 | 46 | 0.300 |
| lmstudio/auto | 319 | 5 | 37 | 0.202 |
| manual/sonnet-5/unattested | 196 | 6 | 28 | 0.245 |
| lmstudio/realist | 119 | 8 | 34 | 0.317 |
| manual/fable-5.1/unattested | 107 | 6 | 7 | 0.211 |
| manual/fable-5/unattested | 102 | 6 | 14 | 0.203 |
| manual/opus-5/unattested | 95 | 6 | 10 | 0.208 |
| manual/sonnet-5 | 41 | 6 | 5 | 0.250 |
| manual/opus-5 | 35 | 6 | 7 | 0.213 |
| lmstudio/qwen36-realist | 31 | 4 | 0 | 0.242 |
| manual/fable | 27 | 3 | 1 | 0.180 |
| manual/fable-5 | 24 | 6 | 3 | 0.164 |
| manual/sonnet-5.5/unattested | 15 | 5 | 0 | 0.122 |
| manual/opus-5.5/unattested | 14 | 7 | 0 | 0.312 |
| lmstudio/qwen36 | 11 | 3 | 0 | 0.227 |

## Open rows past deadline (the queue the desk is forgetting)

| overdue age | rows | arms |
|---|---|---|
| 1-3 d | 253 | control/baserate 81, lmstudio/qwen36 44, manual/sonnet-5.5/unattested 36 |
| 4-7 d | 327 | control/baserate 113, manual/sonnet-5.5/unattested 33, manual/fable-5.1/unattested 32 |
| 8-14 d | 570 | control/baserate 208, manual/fable-5.1/unattested 65, lmstudio/auto 55 |
| 15-30 d | 299 | control/baserate 95, lmstudio/realist 36, manual/sonnet-5/unattested 35 |
| over 30 d | 149 | lmstudio/auto 57, lmstudio/realist 31, control/baserate 26 |

Ten oldest open rows:

- KKR-20260817-36 deadline 2026-08-26 (77 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Dnipro with at least
- KKR-20260815-25 deadline 2026-09-02 (70 d) lmstudio/auto - At least one major wildfire in Europe causes over 100 evacuations between 2026-08-21 and 2
- KKR-20260820-04 deadline 2026-09-02 (70 d) lmstudio/auto - Between 2026-08-21 and 2026-08-24, a new military offensive will be reported in the Zapori
- KKR-20260808-04 deadline 2026-09-07 (65 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a new wildfire will be reported in the United States by
- KKR-20260827-63 deadline 2026-09-07 (65 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed cyberattack exploiting CVE-2021-23758 will 
- KKR-20260827-64 deadline 2026-09-07 (65 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed forest fire will be reported in Canada with
- KKR-20260827-65 deadline 2026-09-07 (65 d) lmstudio/auto - Between 2026-08-27 and 2026-09-03, a confirmed political statement by Trump regarding Iran
- KKR-20260822-05 deadline 2026-09-08 (64 d) manual/sonnet-5/unattested - At the sentencing hearing scheduled for 2026-09-04 at Preston Crown Court, at least one of
- KKR-20260811-27 deadline 2026-09-10 (62 d) manual/sonnet-5/unattested - A US water or energy utility beyond those in items 33, 34, and 37 will publicly disclose a
- KKR-20260811-53 deadline 2026-09-10 (62 d) control/baserate - A US water or energy utility beyond those in items 33, 34, and 37 will publicly disclose a

Reading rule: compare each arm's over-14-day count with its row count; an arm whose late rows cluster is an arm whose claims the desk cannot look up, and that is a property of the claims, not of the lateness. Either way the queue table is the to-do list; the keys pass runs before each sitting and the overdue rows are the sitting.
