**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061524Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: lmstudio/qwen36-abliterated · 3 accepted / 7 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-25 | 45% | 2026-12-19 | disaster | A major commercial airline flight is grounded due to a technical failure between 2026-12-10 and 2026-12-16. | A major commercial airline flight is grounded due to a technical failure between 2026-12-10 and 2026-12-16, as reported by two independent wire services. |
| KKR-20261006-26 | 35% | 2027-03-10 | disaster | A major US city declares a state of emergency due to severe flooding between 2027-03-01 and 2027-03-07. | A major US city declares a state of emergency due to severe flooding between 2027-03-01 and 2027-03-07, as recorded in the Federal Register. |
| KKR-20261006-27 | 40% | 2027-03-18 | economics/markets | The European Central Bank raises interest rates by at least 25 basis points by 2027-03-15. | The European Central Bank raises interest rates by at least 25 basis points by 2027-03-15, as recorded in the ECB press release. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,600 at least once between 2026-11-02 and 2026-11-06. Reference: 7,836.33 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A confirmed case of pneumonic plague is reported in Russia between 2026-11-01 and 2026-11-07. Reference: 5.26 percent on the packet date." → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | a who…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The 10-year US Treasury yield closes above 5.50 percent at least once between 2026-12-01 and 2026-12-07. Reference: 5.26 percent on the pack" → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal reserve | or | a major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A critical zero-day vulnerability is added to the CISA KEV catalog between 2026-11-15 and 2026-11-21." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The US Congress passes a continuing resolution to fund the government by 2027-01-15." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A significant cyberattack disrupts a major US hospital system between 2027-02-01 and 2027-02-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major US tech company announces a significant layoff of at least 5,000 employees by 2027-03-31." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3488 issued all-time across 21 forecaster arms · 2674 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 8 issued · 8 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1242 | 1041 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*