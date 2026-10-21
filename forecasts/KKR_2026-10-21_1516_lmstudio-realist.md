**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 211516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-21_1512.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261021-02 | 30% | 2026-11-05 | military/conflict | Between 2026-10-21 and 2026-10-24, at least one report from a hostile side will confirm a drone strike on Kyiv with casualties claimed by Ukrainian sources. | At least one report from a hostile side (UA, IL, WEST, AXIS) confirms a drone strike on Kyiv between 2026-10-21 and 2026-10-24, with casualties claimed in at least one corroborating report. |
| KKR-20261021-03 | 25% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-24, the SafePay ransomware will be reported to have compromised at least one additional critical infrastructure organization beyond the 600 already reported. | CISA or FBI public advisories confirm that SafePay ransomware has compromised at least one additional critical infrastructure organization beyond the 600 reported on 2026-10-21. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-22, the CISA KEV catalog will include CVE-2026-106931 with a date-added value of 2026-10-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-10-20, before this row is sealed (2026-10-21, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "On 2026-10-23, the French 10-year bond yield will exceed 5.0% for the first time since 2026-10-21." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-23 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-21 and 2026-10-24, at least one report from a hostile side will confirm a missile strike on Kharkiv with casualties claimed " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-96656 with a date-added value of 2026-10-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-96656 dateAdded 2026-10-20, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-24, at least one report from a hostile side will confirm a ballistic missile strike on Zaporizhzhia with casu" → REJECTED: cited items name United Kingdom; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-24, the S&P 500 will close below 7,700 points." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-24 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-21 and 2026-10-24, at least one report from a hostile side will confirm a drone strike on Donetsk with casualties claimed by" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-110936 with a date-added value of 2026-10-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-110936 dateAdded 2026-10-20, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

4634 issued all-time across 21 forecaster arms · 3282 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 236 issued · 149 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1633 | 1250 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 453 | 212 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 88 | 88 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 99 | 92 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 236 | 149 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 398 | 317 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 229 | 218 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 181 | 178 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*