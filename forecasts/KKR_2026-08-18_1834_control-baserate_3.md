**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181834Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-18_1516.md · forecaster: control/baserate · 4 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260818-37 | 50% | 2026-08-28 | military/conflict | The United States will carry out a military strike on a target inside Oman between 2026-08-19 and 2026-08-26. | TRUE if the US government, the Omani government, or two independent wire services confirm a US military strike inside Oman during the window; adjudicated 2026-08-28. |
| KKR-20260818-38 | 23% | 2026-09-18 | cyber | CVE-2026-19478, the critical GitLab GraphQL flaw patched 2026-08-17, will be added to the CISA KEV catalog between 2026-08-19 and 2026-09-16. | TRUE if CISA's Known Exploited Vulnerabilities catalog lists CVE-2026-19478 with a date-added value inside the window; adjudicated 2026-09-18. |
| KKR-20260818-39 | 31% | 2026-09-28 | crime/security | A jury will return a verdict, guilty or not guilty, in the Duane Keffe D Davis murder trial in Clark County, Nevada, between 2026-09-07 and 2026-09-25. | TRUE if Clark County District Court or at least two independent wire services report a jury verdict in the Davis trial inside the window; a hung jury counts as FALSE; adjudicated 2026-09-28. |
| KKR-20260818-40 | 33% | 2026-08-28 | disaster | USGS will record a magnitude 6.0 or greater earthquake within 150 km of the M7.7 Ende, Indonesia mainshock (2026-08-17, 22:29 UTC), between 2026-08-19 and 2026-08-26. | TRUE if the USGS Earthquake Catalog lists any magnitude 6.0 or greater event within 150 km of the Ende mainshock epicenter, origin time inside the window; adjudicated 2026-08-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

748 issued all-time across 14 forecaster arms · 658 open (6 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 165 issued · 157 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 165 | 157 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 100 | 88 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 69 | 69 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 62 | 61 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*