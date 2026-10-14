**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: lmstudio/qwen36-realist · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-15 | 25% | 2026-10-29 | cyber | The CISA KEV catalog carries a date-added value for a critical zero-day vulnerability between 2026-10-20 and 2026-10-27 | A new CVE is added to the CISA KEV catalog with a date_added value falling within the window |
| KKR-20261014-16 | 20% | 2026-10-29 | disaster | The USGS Significant Quakes catalog records a magnitude 6.5 or greater earthquake between 2026-10-20 and 2026-10-27 | The USGS catalog carries a date-added value for an event with magnitude 6.5 or higher within the window |
| KKR-20261014-17 | 5% | 2026-10-29 | political | Colombia inaugurates an embassy in Jerusalem between 2026-10-20 and 2026-10-27 | A diplomatic ceremony inaugurating a Colombian embassy in Jerusalem is reported by two independent wire services |
| KKR-20261014-18 | 35% | 2026-10-29 | military | A Houthi missile or drone strikes a target in Saudi Arabia between 2026-10-20 and 2026-10-27 | Two independent wire services report a Houthi missile or drone strike hitting a target in Saudi Arabia |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes above 100.00 on a weekday between 2026-10-20 and 2026-10-27" → REJECTED: cited items name Iran, Islamic Republic of, Saudi Arabia; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A major US bank reports a quarterly profit miss between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major US tech company announces layoffs exceeding 500 employees between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major US bank reports a quarterly profit miss between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major US tech company announces layoffs exceeding 500 employees between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major US bank reports a quarterly profit miss between 2026-10-20 and 2026-10-27" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

4113 issued all-time across 21 forecaster arms · 3002 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 58 issued · 58 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1452 | 1156 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 337 | 279 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*