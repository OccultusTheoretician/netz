**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 170209Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: control/baserate · 5 accepted / 0 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-06 | 50% | 2026-09-03 | military/conflict | At least one Russian air attack using missiles or drones causes an impact, explosion, or fire within Kyiv city between 2026-08-17 and 2026-08-31. | True if strikes on Kyiv city between 2026-08-17 and 2026-08-31 are reported by Ukrainian officials and by at least one Russian or non-Ukrainian international outlet. |
| KKR-20260817-07 | 50% | 2026-09-18 | military/conflict | Ukrainian drones or missiles strike a target at least 100 km from the Ukraine-Russia border inside Russia, causing fire, damage, or casualties, between 2026-08-17 and 2026-09-15. | True if Russian regional or federal officials acknowledge a Ukrainian drone or missile strike at least 100 km from the Ukraine border causing damage, fire, or casualties between 2026-08-17 and 2026-09-15. |
| KKR-20260817-08 | 50% | 2027-01-05 | military/conflict | Houthi (Ansar Allah) forces take control of central Marib city, Yemen, between 2026-08-17 and 2026-12-31. | True if at least two major international news organizations report Houthi forces control central Marib city by 2026-12-31, with Yemeni government or coalition sources conceding withdrawal or loss. |
| KKR-20260817-09 | 25% | 2026-11-02 | economics/markets | ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-17 and 2026-10-30. | True if the official ICE Brent front-month settlement price is at or above 100.00 USD on any trading day from 2026-08-17 through 2026-10-30, per ICE settlement data. |
| KKR-20260817-10 | 31% | 2026-10-02 | crime/security | Authorities announce the arrest or charging of at least one suspect in the 2026-08-15 Virginia State shooting in which five people were shot, between 2026-08-17 and 2026-09-30. | True if a law enforcement agency publicly announces an arrest or charges in the 2026-08-15 Virginia State five-victim shooting, reported by at least one national outlet, by 2026-09-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

644 issued all-time across 14 forecaster arms · 554 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 121 issued · 113 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 121 | 113 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 82 | 70 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 55 | 55 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 47 | 46 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*