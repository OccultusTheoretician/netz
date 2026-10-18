**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: lmstudio/qwen36-abliterated · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-24 | 25% | 2026-11-06 | economics | The S&P 500 closes below 7,500 on at least one trading day between 2026-11-02 and 2026-11-06 | Reference: 7,659.44 on 2026-10-18. The S&P 500 index settles below 7,500 on any trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261018-25 | 20% | 2026-11-06 | disaster | A forest fire is reported in South Africa between 2026-11-02 and 2026-11-06 | GDACS Alerts records a forest fire event in South Africa with a date between 2026-11-02 and 2026-11-06. |
| KKR-20261018-26 | 30% | 2026-11-06 | economics | The 10Y US Treasury Yield closes above 5.20 on at least one trading day between 2026-11-02 and 2026-11-06 | Reference: 5.10 on 2026-10-18. The 10Y US Treasury Yield settles above 5.20 on any trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261018-27 | 20% | 2026-11-06 | disaster | A significant earthquake (M5.0+) occurs in Pakistan between 2026-11-02 and 2026-11-06 | USGS Significant Quakes records an earthquake of magnitude 5.0 or higher in Pakistan between 2026-11-02 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A new vulnerability is added to the CISA KEV catalog between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "WTI Crude closes above 105.00 on at least one trading day between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "France arrests over 2,000 people in total during the ongoing protests between 2026-11-02 and 2026-11-06" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; the resolution names a different subject than the statement — the claim is about France and the resolution settles on French. A row whose resolution checks a different fact can be scored correct while being wrong
- "A drone strike hits a target in Sudan between 2026-11-02 and 2026-11-06" → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-11-06) is 0 day(s) after the window closes (2026-11-06). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "Microsoft announces a new AI datacentre project in the UK between 2026-11-02 and 2026-11-06" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new vulnerability is added to the CISA KEV catalog between 2026-11-09 and 2026-11-13" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4433 issued all-time across 21 forecaster arms · 3322 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 76 issued · 76 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1556 | 1260 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 86 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*