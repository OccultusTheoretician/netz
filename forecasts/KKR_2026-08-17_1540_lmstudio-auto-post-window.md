**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171540Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-17_1537.md · forecaster: lmstudio/auto · 10 accepted / 0 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-29 | 90% | 2026-08-24 | cyber | On 2026-08-21, the CISA KEV catalog will include CVE-2025-62593 with a date-added value of 2026-08-18. | The CISA KEV catalog carries a record with the identifier CVE-2025-62593 and a date-added value of 2026-08-18. |
| KKR-20260817-30 | 65% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Kyiv with at least one corroborating report from a hostile side. | At least one report from a hostile side (RU, UA, AXIS, or WEST) confirms a drone strike in Kyiv between 2026-08-21 and 2026-08-24. |
| KKR-20260817-31 | 30% | 2026-08-26 | cyber | Between 2026-08-21 and 2026-08-24, a cyberattack exploiting CVE-2025-62593 will be confirmed by two independent sources. | Two independent sources (not from the same outlet or network) confirm a cyberattack exploiting CVE-2025-62593 between 2026-08-21 and 2026-08-24. |
| KKR-20260817-32 | 45% | 2026-08-26 | disaster | Between 2026-08-21 and 2026-08-24, a wildfire will be reported in France with at least one corroborating report from a hostile side. | At least one report from a hostile side (IL, PS, AXIS, or WEST) confirms a wildfire in France between 2026-08-21 and 2026-08-24. |
| KKR-20260817-33 | 70% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Khan Younis with at least one corroborating report from a hostile side. | At least one report from a hostile side (IL, PS, AXIS, or WEST) confirms a drone strike in Khan Younis between 2026-08-21 and 2026-08-24. |
| KKR-20260817-34 | 55% | 2026-08-26 | cyber | Between 2026-08-21 and 2026-08-24, a large-scale DDoS attack will disrupt Threema secure messaging service. | A large-scale DDoS attack will be confirmed to have disrupted Threema secure messaging service between 2026-08-21 and 2026-08-24. |
| KKR-20260817-35 | 60% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Moscow with at least one corroborating report from a hostile side. | At least one report from a hostile side (RU, UA, IL, or WEST) confirms a drone strike in Moscow between 2026-08-21 and 2026-08-24. |
| KKR-20260817-36 | 65% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Dnipro with at least one corroborating report from a hostile side. | At least one report from a hostile side (RU, UA, or AXIS) confirms a drone strike in Dnipro between 2026-08-21 and 2026-08-24. |
| KKR-20260817-37 | 70% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Nablus with at least one corroborating report from a hostile side. | At least one report from a hostile side (AXIS, PS, or IL) confirms a drone strike in Nablus between 2026-08-21 and 2026-08-24. |
| KKR-20260817-38 | 65% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Sumy with at least one corroborating report from a hostile side. | At least one report from a hostile side (RU, UA, or AXIS) confirms a drone strike in Sumy between 2026-08-21 and 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

672 issued all-time across 14 forecaster arms · 582 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 92 issued · 80 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 130 | 122 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 92 | 80 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
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