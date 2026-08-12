**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121720Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-12_1518.md · forecaster: control/baserate · 5 accepted / 0 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260812-28 | 33% | 2026-09-23 | military/conflict | North Korea conducts at least one further ballistic missile launch between 2026-08-13 and 2026-09-20. | True if South Korea's Joint Chiefs of Staff confirm a North Korean ballistic missile launch dated between 2026-08-13 and 2026-09-20, carried by at least two of Yonhap, Reuters, and Associated Press. |
| KKR-20260812-29 | 33% | 2026-10-19 | military/conflict | Russian forces seize or detain at least one commercial vessel flagged in or operated from an EU member state between 2026-08-13 and 2026-10-15. | True if at least two of Reuters, Associated Press, and the flag state government confirm Russian seizure or detention of a named EU-flagged or EU-operated commercial vessel between 2026-08-13 and 2026-10-15. |
| KKR-20260812-30 | 33% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog gains an entry naming Microsoft SharePoint Server or VMware vCenter Server with a date-added value between 2026-08-13 and 2026-10-30. | True if the CISA KEV JSON feed contains an entry whose product field names SharePoint Server or vCenter Server with a dateAdded between 2026-08-13 and 2026-10-30 inclusive. |
| KKR-20260812-31 | 33% | 2026-08-24 | political | The Electoral Commission of Zambia declares Hakainde Hichilema elected president in the first round, announced between 2026-08-13 and 2026-08-20. | True if the ECZ formally declares Hichilema president-elect between 2026-08-13 and 2026-08-20 with more than 50 percent of valid votes, avoiding a runoff. |
| KKR-20260812-32 | 33% | 2026-10-19 | disaster | The USGS earthquake catalog records at least one magnitude 6.0 or greater earthquake located in Colombia with origin time between 2026-08-13 and 2026-10-15. | True if USGS ANSS ComCat lists an event of magnitude 6.0 or above whose place field names Colombia with origin time between 2026-08-13 and 2026-10-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

549 issued all-time across 14 forecaster arms · 493 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 83 issued · 83 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 83 | 83 | 0 | — | — | not computed | — | — | — |
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