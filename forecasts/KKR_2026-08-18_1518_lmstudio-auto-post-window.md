**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181518Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-18_1516.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260818-01 | 25% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone strike will be reported in Kyiv with casualties claimed by Ukrainian sources. | At least one report from a Ukrainian source confirms casualties from a drone strike in Kyiv between 2026-08-21 and 2026-08-24. |
| KKR-20260818-02 | 35% | 2026-08-27 | economics/markets | Between 2026-08-21 and 2026-08-24, the 10-year U.S. Treasury yield will exceed 5.33% at the close of any trading day. | The 10-year U.S. Treasury yield, as reported by FRED, exceeds 5.33% on at least one trading day between 2026-08-21 and 2026-08-24. |
| KKR-20260818-03 | 20% | 2026-08-28 | disaster | Between 2026-08-21 and 2026-08-24, a wildfire in Belgium will be classified as 'red' by GDACS. | GDACS issues a red alert for a wildfire in Belgium between 2026-08-21 and 2026-08-24. |
| KKR-20260818-04 | 30% | 2026-08-28 | cyber | Between 2026-08-21 and 2026-08-24, a cyberattack exploiting CVE-2025-62593 will be reported by at least two independent sources. | At least two independent, non-identical sources report a cyberattack exploiting CVE-2025-62593 between 2026-08-21 and 2026-08-24. |
| KKR-20260818-05 | 15% | 2026-08-28 | political | Between 2026-08-21 and 2026-08-24, a U.S. federal court will issue a ruling on the Disney ABC First Amendment lawsuit against the FCC. | A U.S. federal court issues a ruling on the Disney ABC First Amendment lawsuit against the FCC between 2026-08-21 and 2026-08-24. |
| KKR-20260818-06 | 25% | 2026-08-28 | disaster | Between 2026-08-21 and 2026-08-24, a magnitude 6.0 or higher earthquake will be recorded in Indonesia by the USGS. | The USGS reports a magnitude 6.0 or higher earthquake in Indonesia between 2026-08-21 and 2026-08-24. |
| KKR-20260818-07 | 10% | 2026-08-28 | political | Between 2026-08-21 and 2026-08-24, a political scandal involving a U.S. state governor will be reported by at least three major wire services. | At least three major wire services (e.g., AP, Reuters, Bloomberg) report a political scandal involving a U.S. state governor between 2026-08-21 and 2026-08-24. |
| KKR-20260818-08 | 18% | 2026-08-28 | cyber | Between 2026-08-21 and 2026-08-24, a major cyberattack on a financial institution will be confirmed by the CISA KEV catalog and reported by two major financial news outlets. | The CISA KEV catalog lists a vulnerability exploited in a major cyberattack on a financial institution, and two major financial news outlets report the incident between 2026-08-21 and 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will include CVE-2025-62593 with a date-added value of 2026-08-17." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2025-62593 dateAdded 2026-08-17, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-21 and 2026-08-24, a cyberattack on a U.S. government agency will be confirmed by CISA and two independent news outlets." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

716 issued all-time across 14 forecaster arms · 626 open (6 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 100 issued · 88 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 149 | 141 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 100 | 88 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 47 | 47 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 63 | 63 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 58 | 57 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*