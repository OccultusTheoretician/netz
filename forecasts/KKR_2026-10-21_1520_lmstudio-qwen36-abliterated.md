**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 211520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-21_1512.md · forecaster: lmstudio/qwen36-abliterated · 3 accepted / 7 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261021-09 | 30% | 2026-11-10 | economics | WTI Crude closes below 95.00 on at least one trading day between 2026-11-02 and 2026-11-09. | Reference: 97.86 on 2026-10-21. The closing price of WTI Crude is below 95.00 on at least one trading day between 2026-11-02 and 2026-11-09. |
| KKR-20261021-10 | 35% | 2026-11-10 | economics | The Nasdaq index closes above 27,000 on at least one trading day between 2026-11-02 and 2026-11-09. | Reference: 26,636.66 on 2026-10-21. The Nasdaq index closes above 27,000 on at least one trading day between 2026-11-02 and 2026-11-09. |
| KKR-20261021-11 | 40% | 2026-11-10 | economics | The 10Y US Treasury yield closes above 5.25 on at least one trading day between 2026-11-02 and 2026-11-09. | Reference: 5.11 on 2026-10-21. The 10Y US Treasury yield closes above 5.25 on at least one trading day between 2026-11-02 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-106931 between 2026-10-20 and 2026-10-27." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; event window opens 2026-10-20, before this row is sealed (2026-10-21, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-106931 dateAdded 2026-10-20, already inside the claimed window 2026-10-20..2026-10-27
- "A drone or missile strike hits Moscow between 2026-11-01 and 2026-11-08." → REJECTED: cited items name Australia; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A confirmed Ebola case is reported in Kenya between 2026-11-01 and 2026-11-08." → REJECTED: cited items name Nigeria; the claim is about Kenya — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A drone or missile strike hits Kyiv between 2026-11-01 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone or missile strike hits Tehran between 2026-11-01 and 2026-11-08." → REJECTED: cited items name United Kingdom; the claim is about zone:iran — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Gold closes below 4,100 on at least one trading day between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone or missile strike hits Zaporizhzhia between 2026-11-01 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4642 issued all-time across 21 forecaster arms · 3290 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 91 issued · 91 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
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