**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: lmstudio/qwen36 · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-03 | 15% | 2026-11-16 | disaster | A magnitude 7.0 or greater earthquake occurs between 2026-11-01 and 2026-11-15 | The USGS catalog records an event with a magnitude of 7.0 or greater |
| KKR-20261025-04 | 25% | 2026-11-09 | economics | The US 10-year Treasury yield closes above 5.10 percent on any day between 2026-11-02 and 2026-11-06 | The closing yield for the US 10-year Treasury note exceeds 5.10 percent |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Brazilian President-elect Lula da Silva is inaugurated between 2026-11-01 and 2026-11-05" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The S&P 500 index closes below 7,500 at any point between 2026-11-02 and 2026-11-06" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A vulnerability with a CVSS score of 9.0 or higher is added to the CISA KEV catalog between 2026-11-01 and 2026-11-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Saudi Arabia intercepts a ballistic missile or drone attack between 2026-11-01 and 2026-11-15" → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-11-16) is 1 day(s) after the window closes (2026-11-15). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "France passes a budget law to resolve the parliamentary deadlock between 2026-11-01 and 2026-11-30" → REJECTED: the resolution names a different subject than the statement — the claim is about France and the resolution settles on French, Journal, Officiel. A row whose resolution checks a different fact can be scored correct while being wrong
- "A major US airline cancels flights due to a labor strike between 2026-11-01 and 2026-11-15" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new critical vulnerability affecting cloud infrastructure is added to the CISA KEV catalog between 2026-11-01 and 2026-11-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A significant cyberattack disrupts critical infrastructure in the US between 2026-11-01 and 2026-11-15" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

4910 issued all-time across 21 forecaster arms · 3558 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 110 issued · 109 open · 1 resolved · 1 hits / 0 misses · **Brier 0.722** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1727 | 1344 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 110 | 109 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 109 | 109 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 429 | 348 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*