**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181834Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-18_1516.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260818-31 | 50% | 2026-09-04 | military/conflict | Between 2026-08-19 and 2026-09-01, the Ukrainian Air Force command reports on at least seven separate overnight periods that Russia launched 100 or more one-way attack drones. | Daily Ukrainian Air Force air-defence tallies covering nights from 2026-08-19 to 2026-09-01 show 100 or more drones launched on seven or more of those nights, with at least one wire service reporting the same figures. |
| KKR-20260818-32 | 50% | 2026-11-04 | military/conflict | The United States conducts at least one military strike on Omani territory between 2026-08-19 and 2026-10-31. | At least two of Reuters, AP, AFP, and BBC report a US strike on Omani soil dated between 2026-08-19 and 2026-10-31, or US Central Command confirms one. |
| KKR-20260818-33 | 29% | 2026-10-05 | political | Between 2026-08-19 and 2026-09-30, either Russia or the United Kingdom expels at least one accredited diplomat of the other state. | The Russian foreign ministry or the UK Foreign Office announces the expulsion of at least one diplomat of the other state, dated 2026-08-19 to 2026-09-30, corroborated by two wire services. |
| KKR-20260818-34 | 23% | 2027-01-20 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendorProject field is GitLab, with a dateAdded between 2026-08-19 and 2027-01-15. | A fetch of the CISA KEV JSON feed returns at least one entry with vendorProject GitLab and a dateAdded between 2026-08-19 and 2027-01-15 inclusive. |
| KKR-20260818-35 | 29% | 2026-10-20 | political | In the Disney and ABC First Amendment suit against the FCC, the FCC files a motion to dismiss or an answer between 2026-08-19 and 2026-10-15. | The federal docket for the ABC or Disney suit against the FCC records a motion to dismiss or an answer filed by the FCC between 2026-08-19 and 2026-10-15. |
| KKR-20260818-36 | 33% | 2026-10-05 | disaster | The USGS earthquake catalog lists at least one magnitude 6.5 or greater event with an epicenter in Indonesia between 2026-08-19 and 2026-09-30. | A USGS FDSN event query for 2026-08-19 to 2026-09-30 returns one or more events of magnitude 6.5 or greater within the Indonesian region bounding box. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

744 issued all-time across 14 forecaster arms · 654 open (6 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 161 issued · 153 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 161 | 153 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
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