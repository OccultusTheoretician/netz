**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101526Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-24 | 25% | 2026-11-09 | economics/markets | The S&P 500 index closes at or above 10,000 on the Nasdaq exchange between 2026-11-02 and 2026-11-06. Reference: 7,811.54 on the packet date. | The S&P 500 index closing value on the Nasdaq exchange is 10,000 or higher on at least one day between 2026-11-02 and 2026-11-06. |
| KKR-20261010-25 | 30% | 2026-11-24 | disaster | A magnitude 6.0 or greater earthquake is recorded by the USGS between 2026-11-15 and 2026-11-21. | The USGS Significant Quakes catalog carries a date-added value between 2026-11-15 and 2026-11-21 for an event with magnitude 6.0 or higher. |
| KKR-20261010-26 | 20% | 2026-11-16 | economics/markets | The Brent crude oil price closes at or above 110.00 on the ICE exchange between 2026-11-09 and 2026-11-13. Reference: 104.72 on the packet date. | The Brent crude oil price closing value on the ICE exchange is 110.00 or higher on at least one day between 2026-11-09 and 2026-11-13. |
| KKR-20261010-27 | 20% | 2027-02-10 | political | A US federal judge issues a ruling in the case against the International Criminal Court between 2027-02-01 and 2027-02-07. | A US federal court docket records a ruling in the case against the International Criminal Court with a date between 2027-02-01 and 2027-02-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A new vulnerability is added to the CISA KEV catalog with a date-added value between 2026-12-01 and 2026-12-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A state-level conflict onset or major offensive operation is confirmed in the Russia-Ukraine Theatre between 2026-11-02 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The 10-year US Treasury yield closes at or below 4.50 on the Federal Reserve data between 2026-12-07 and 2026-12-11. Reference: 5.24 on the " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new CISA KEV entry is added with a date-added value between 2027-01-11 and 2027-01-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A tropical storm makes landfall in the United States between 2026-11-16 and 2026-11-22." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new CISA KEV entry is added with a date-added value between 2027-03-01 and 2027-03-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3806 issued all-time across 21 forecaster arms · 2992 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 27 issued · 27 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1347 | 1146 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 30 | 30 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 27 | 27 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 205 | 170 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 302 | 269 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 88 | 88 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*