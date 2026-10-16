**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-23 | 10% | 2026-11-12 | disaster | A magnitude 6.0 or greater earthquake occurs in Panama between 2026-11-02 and 2026-11-09. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2026-11-02 and 2026-11-09. |
| KKR-20261016-24 | 15% | 2026-11-12 | political | The US Senate confirms a Supreme Court justice between 2026-11-02 and 2026-11-09. | The US Senate confirms a Supreme Court justice between 2026-11-02 and 2026-11-09. |
| KKR-20261016-25 | 12% | 2026-11-12 | cyber | A major cyberattack disrupts Burger King Japan operations between 2026-11-02 and 2026-11-09. | A major cyberattack disrupts Burger King Japan operations between 2026-11-02 and 2026-11-09. |
| KKR-20261016-26 | 18% | 2026-11-12 | military | A Houthi attack hits a strategic Saudi asset between 2026-11-02 and 2026-11-09. | At least two hostile sides report a Houthi attack hitting a strategic Saudi asset between 2026-11-02 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog records a new date-added entry for CVE-2026-21589 between 2026-10-23 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-21589 dateAdded 2026-10-15, before the claimed window 2026-10-23..2026-10-30; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "WTI Crude closes above 98.00 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone or missile strike hits Moscow between 2026-11-02 and 2026-11-09." → REJECTED: cited items name New York, South Africa, United States; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The Nasdaq closes below 26,000 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The 10Y Yield closes above 5.20 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Gold closes above 4,250 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4269 issued all-time across 21 forecaster arms · 3158 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 64 issued · 64 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1501 | 1205 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 354 | 296 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*