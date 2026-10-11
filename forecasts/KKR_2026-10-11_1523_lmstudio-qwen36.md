**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111523Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: lmstudio/qwen36 · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-07 | 25% | 2026-11-06 | cyber | The CISA KEV catalog carries a date-added value between 2026-10-27 and 2026-11-03 for a vulnerability exploited in the P7 DarkSword iOS exploit kit. | The CISA KEV catalog entry for the P7 DarkSword exploit kit vulnerability has a date-added value falling within the event window. |
| KKR-20261011-08 | 35% | 2026-11-09 | military_conflict | A Houthi strike hits a target in Saudi Arabia between 2026-11-02 and 2026-11-06. | Two or more wire services report a Houthi strike hitting a target in Saudi Arabia between 2026-11-02 and 2026-11-06. |
| KKR-20261011-09 | 15% | 2026-11-09 | disaster | The USGS catalog records a magnitude 7.0 or greater earthquake in Panama between 2026-11-02 and 2026-11-06. | The USGS catalog records a magnitude 7.0 or greater earthquake in Panama between 2026-11-02 and 2026-11-06. |
| KKR-20261011-10 | 10% | 2026-11-09 | political | Polish authorities formally indict Prime Minister Donald Tusk for the alleged assassination plot between 2026-11-02 and 2026-11-06. | Polish authorities formally indict Prime Minister Donald Tusk for the alleged assassination plot between 2026-11-02 and 2026-11-06. |
| KKR-20261011-11 | 35% | 2026-11-09 | military_conflict | A Houthi strike hits a target in Saudi Arabia between 2026-11-02 and 2026-11-06. | Two or more wire services report a Houthi strike hitting a target in Saudi Arabia between 2026-11-02 and 2026-11-06. |
| KKR-20261011-12 | 15% | 2026-11-09 | disaster | The USGS catalog records a magnitude 7.0 or greater earthquake in Panama between 2026-11-02 and 2026-11-06. | The USGS catalog records a magnitude 7.0 or greater earthquake in Panama between 2026-11-02 and 2026-11-06. |
| KKR-20261011-13 | 10% | 2026-11-09 | political | Polish authorities formally indict Prime Minister Donald Tusk for the alleged assassination plot between 2026-11-02 and 2026-11-06. | Polish authorities formally indict Prime Minister Donald Tusk for the alleged assassination plot between 2026-11-02 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes above 95.00 USD on a weekday between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes below 7,700 on a weekday between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The S&P 500 closes below 7,700 on a weekday between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3869 issued all-time across 21 forecaster arms · 3055 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 37 issued · 37 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1372 | 1171 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 27 | 27 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 312 | 279 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*