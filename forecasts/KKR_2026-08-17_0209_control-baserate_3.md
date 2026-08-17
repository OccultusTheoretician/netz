**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 170209Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: control/baserate · 4 accepted / 0 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-25 | 50% | 2026-09-22 | military/conflict | Between 2026-08-17 and 2026-09-20, Qatar and Iran issue public statements that converge on a single account of the fate of the three Iranian pilots Qatar allegedly shot down in March 2026, either confirming them alive and held or confirming their deaths. | TRUE if Qatar and Iran state the same outcome for the three named pilots, reported by Reuters, AP, or AFP, between 2026-08-17 and 2026-09-20; otherwise FALSE. |
| KKR-20260817-26 | 50% | 2026-09-17 | military/conflict | Between 2026-08-17 and 2026-09-15, the United States government takes a formal, documented action asserting a sovereignty or territorial claim over any part of the Strait of Hormuz, beyond rhetorical statements by the President. | TRUE if the Federal Register, a State Department notice, or a wire service reports a formal US filing or action claiming sovereignty over Hormuz waters between 2026-08-17 and 2026-09-15; otherwise FALSE. |
| KKR-20260817-27 | 23% | 2026-09-02 | cyber | Between 2026-08-17 and 2026-08-31, a cybersecurity vendor or outlet other than BleepingComputer, such as Krebs on Security, The Hacker News, Malwarebytes, SentinelOne, or Objective-See, publishes independent research naming and attributing the AmnesiaStealer macOS malware campaign. | TRUE if a named second security vendor or outlet publishes independent attribution of AmnesiaStealer between 2026-08-17 and 2026-08-31; otherwise FALSE. |
| KKR-20260817-28 | 29% | 2026-09-22 | political | Between 2026-08-17 and 2026-09-20, the US Navy or Department of Defense publicly confirms that USS George Washington has relieved USS Abraham Lincoln on its Middle East deployment station. | TRUE if DoD or Navy public affairs, or a wire service citing an on-record defense official, confirms the Lincoln to George Washington handover between 2026-08-17 and 2026-09-20; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

662 issued all-time across 14 forecaster arms · 572 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 130 issued · 122 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 130 | 122 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 82 | 70 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 51 | 50 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*