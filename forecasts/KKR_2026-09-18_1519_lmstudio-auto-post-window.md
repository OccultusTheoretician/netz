**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-18_1518.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260918-01 | 45% | 2026-10-01 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year Treasury yield will exceed 5.05 percent at the close of any trading day. | The 10-year Treasury yield exceeds 5.05 percent at the close of any trading day between 2026-09-21 and 2026-09-24. |
| KKR-20260918-02 | 25% | 2026-10-05 | disaster | Between 2026-09-21 and 2026-09-24, a magnitude 6.0 or higher earthquake will be recorded by the USGS in the Pacific Northwest. | The USGS Significant Quakes database records a magnitude 6.0 or higher earthquake in the Pacific Northwest between 2026-09-21 and 2026-09-24. |
| KKR-20260918-03 | 35% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-24, a cyberattack exploiting CVE-2025-39964 will be reported by at least two independent sources (e.g., BleepingComputer, The Hacker News). | At least two independent sources (e.g., BleepingComputer, The Hacker News) report a cyberattack exploiting CVE-2025-39964 between 2026-09-21 and 2026-09-24. |
| KKR-20260918-04 | 20% | 2026-10-05 | crime/security | Between 2026-09-21 and 2026-09-24, a school shooting in the Philippines resulting in at least three fatalities will be confirmed by two independent sources (e.g., Al Jazeera, BBC World). | Two independent sources (e.g., Al Jazeera, BBC World) confirm a school shooting in the Philippines between 2026-09-21 and 2026-09-24 resulting in at least three fatalities. |
| KKR-20260918-05 | 30% | 2026-10-05 | political | Between 2026-09-21 and 2026-09-24, a new statement by Iran's IRGC regarding a blockade in the Strait of Hormuz will be confirmed by at least two independently biased sources (AXIS and WEST). | At least two independently biased sources (one from AXIS, one from WEST) confirm a new statement by Iran's IRGC regarding a blockade in the Strait of Hormuz between 2026-09-21 and 2026-09-24. |
| KKR-20260918-06 | 25% | 2026-10-05 | disaster | Between 2026-09-21 and 2026-09-24, a major forest fire in South Africa will be reported by GDACS Alerts with a green alert level. | GDACS Alerts reports a green forest fire notification in South Africa between 2026-09-21 and 2026-09-24. |
| KKR-20260918-07 | 30% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-24, a new vulnerability in Microsoft 365 will be exploited in a supply-chain attack, confirmed by BleepingComputer and The Hacker News. | BleepingComputer and The Hacker News confirm a supply-chain attack exploiting a new vulnerability in Microsoft 365 between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2025-39964 and CVE-2026-53266 with a date-added value of 2026-09-18" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-53266 dateAdded 2026-09-18, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, a drone attack on Kyiv will be confirmed by at least two independently biased sources (UA and RU) with no" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-09-21 and 2026-09-24, a drone attack on Tehran will be confirmed by at least two independently biased sources (AXIS and WEST) w" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world

## III. LEDGER STANDING

2446 issued all-time across 16 forecaster arms · 1980 open (103 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 293 issued · 143 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 835 | 750 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 293 | 143 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 81 | 76 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 131 | 121 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 283 | 266 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 262 | 214 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*