**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192251Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-19_1519.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260819-35 | 23% | 2026-12-02 | cyber | CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value in the window 2026-08-26 to 2026-11-30. | The CISA KEV catalog contains at least one entry with vendorProject Microsoft and a dateAdded value between 2026-08-26 and 2026-11-30 inclusive. |
| KKR-20260819-36 | 33% | 2026-11-04 | disaster | At least one earthquake of magnitude 7.0 or greater occurs worldwide with origin time in the window 2026-08-26 to 2026-10-31 UTC. | The USGS ComCat catalog lists at least one event of magnitude 7.0 or greater with origin time between 2026-08-26T00:00Z and 2026-10-31T23:59Z. |
| KKR-20260819-37 | 50% | 2026-10-19 | military/conflict | The UAE government publicly attributes a missile or drone impact on UAE territory or territorial waters to Iran, for an impact in the window 2026-08-26 to 2026-10-15. | Reuters and Agence France-Presse both report a UAE government statement attributing a missile or drone impact on UAE territory or territorial waters to Iran within the window. |
| KKR-20260819-38 | 50% | 2026-12-04 | military/conflict | Iran publicly agrees to permit unrestricted commercial transit of the Strait of Hormuz under an agreement announced in the window 2026-08-26 to 2026-11-30. | Reuters and the Associated Press both report an agreement, announced within the window, under which Iran permits unrestricted commercial transit of the Strait of Hormuz. |
| KKR-20260819-39 | 31% | 2026-12-15 | crime/security | Croatia surrenders to German custody the Ukrainian diver arrested in Pula on 2026-08-19 over the Nord Stream blasts, in the window 2026-08-26 to 2026-12-11. | The German Federal Public Prosecutor confirms the suspect has been surrendered by Croatia and brought before a judge of the Federal Court of Justice within the window. |
| KKR-20260819-40 | 29% | 2026-12-04 | political | NABU or SAPO issues a formal notice of suspicion to a serving or former official of the Ukrainian Office of the President in the window 2026-08-26 to 2026-11-30. | NABU or SAPO publicly announces a notice of suspicion naming a serving or former Office of the President official, reported by Reuters and Ukrainska Pravda. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

788 issued all-time across 14 forecaster arms · 698 open (11 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 179 issued · 171 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 179 | 171 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 105 | 93 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 69 | 68 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*