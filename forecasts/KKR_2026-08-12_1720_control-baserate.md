**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121720Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-12_1518.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260812-22 | 33% | 2026-10-02 | military/conflict | At least one attack on a commercial vessel occurs in the Red Sea, Bab el-Mandeb, or Gulf of Aden between 2026-08-13 and 2026-09-30. | TRUE if UKMTO or US CENTCOM publicly reports at least one attack on a commercial vessel in the Red Sea, Bab el-Mandeb, or Gulf of Aden occurring between 2026-08-13 and 2026-09-30. |
| KKR-20260812-23 | 33% | 2026-11-02 | cyber | A vulnerability affecting VMware vCenter Server is added to the CISA KEV catalog with a date-added value between 2026-08-13 and 2026-10-30. | TRUE if the CISA Known Exploited Vulnerabilities catalog contains an entry naming VMware vCenter Server with dateAdded between 2026-08-13 and 2026-10-30 inclusive. |
| KKR-20260812-24 | 33% | 2026-10-02 | cyber | A Microsoft Defender vulnerability is added to the CISA KEV catalog with a date-added value between 2026-08-13 and 2026-09-30. | TRUE if the CISA KEV catalog contains an entry whose product field names Microsoft Defender with dateAdded between 2026-08-13 and 2026-09-30 inclusive. |
| KKR-20260812-25 | 33% | 2026-10-14 | disaster | USGS records an earthquake of magnitude 6.0 or greater within 300 km of USGS event us6000tjl2 with origin time between 2026-08-13 and 2026-10-12 UTC. | TRUE if the USGS earthquake catalog lists at least one event of magnitude 6.0 or greater within 300 km of event us6000tjl2 with origin time between 2026-08-13 and 2026-10-12 UTC. |
| KKR-20260812-26 | 33% | 2026-10-14 | military/conflict | Russian authorities seize or detain a commercial vessel flagged in or owned by an EU or UK entity between 2026-08-13 and 2026-10-12. | TRUE if at least two of Reuters, AP, and AFP report Russian seizure or detention of an EU or UK flagged or owned commercial vessel occurring between 2026-08-13 and 2026-10-12. |
| KKR-20260812-27 | 33% | 2026-12-02 | political | The government of Iraq announces a signed agreement or decree providing for disarmament or integration of Iran-aligned militia groups between 2026-08-13 and 2026-11-30. | TRUE if at least two of Reuters, AP, AFP, or Al Jazeera report an Iraqi government announcement of a signed disarmament or integration agreement or decree covering Iran-aligned militias between 2026-08-13 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

544 issued all-time across 14 forecaster arms · 488 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 78 issued · 78 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 78 | 78 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 57 | 55 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 26 | 26 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*