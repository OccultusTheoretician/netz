**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191520Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-19_1519.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260819-01 | 30% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, at least one report from a hostile side in the Israel-Gaza-Levant Theatre will confirm a drone strike on Gaza City with casualties claimed in the corroborating reports. | At least one report from a hostile side in the Israel-Gaza-Levant Theatre confirms a drone strike on Gaza City between 2026-08-21 and 2026-08-24, with casualties claimed in the corroborating reports. |
| KKR-20260819-02 | 25% | 2026-08-28 | disaster | Between 2026-08-21 and 2026-08-24, the USGS Significant Quakes feed will record a magnitude 5.0 or higher earthquake in Indonesia with a depth of less than 10 km. | The USGS Significant Quakes feed records a magnitude 5.0 or higher earthquake in Indonesia with a depth of less than 10 km between 2026-08-21 and 2026-08-24. |
| KKR-20260819-03 | 35% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, at least one report from a hostile side in the Russia-Ukraine Theatre will confirm a missile strike on Kyiv with casualties claimed in the corroborating reports. | At least one report from a hostile side in the Russia-Ukraine Theatre confirms a missile strike on Kyiv between 2026-08-21 and 2026-08-24, with casualties claimed in the corroborating reports. |
| KKR-20260819-04 | 20% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, at least one report from a hostile side in the Iran Theatre will confirm a ballistic missile strike on Tehran with casualties claimed in the corroborating reports. | At least one report from a hostile side in the Iran Theatre confirms a ballistic missile strike on Tehran between 2026-08-21 and 2026-08-24, with casualties claimed in the corroborating reports. |
| KKR-20260819-05 | 30% | 2026-08-28 | military/conflict | Between 2026-08-21 and 2026-08-24, at least one report from a hostile side in the Russia-Ukraine Theatre will confirm a drone strike on Dnipro with casualties claimed in the corroborating reports. | At least one report from a hostile side in the Russia-Ukraine Theatre confirms a drone strike on Dnipro between 2026-08-21 and 2026-08-24, with casualties claimed in the corroborating reports. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-08-21, the CISA KEV catalog will include CVE-2026-33824 with a date-added value of 2026-08-18." → REJECTED: event window opens 2026-08-18, before this row is sealed (2026-08-19) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will list CVE-2026-55040 with a date-added value of 2026-08-18." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-55040 dateAdded 2026-08-18, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will include CVE-2026-65400 with a date-added value of 2026-08-18." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-65400 dateAdded 2026-08-18, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will list CVE-2026-59310 with a date-added value of 2026-08-18." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-59310 dateAdded 2026-08-18, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will include CVE-2026-33824 with a date-added value of 2026-08-18 and be marked as a" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-33824 dateAdded 2026-08-18, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

753 issued all-time across 14 forecaster arms · 663 open (11 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 105 issued · 93 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 165 | 157 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 105 | 93 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
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