**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-27_1612.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261127-07 | 35% | 2026-12-17 | economics | SAP announces a further reduction in its workforce of at least 5,000 employees between 2026-12-01 and 2026-12-15. | True if SAP announces a further reduction in its workforce of at least 5,000 employees between 2026-12-01 and 2026-12-15; False otherwise. |
| KKR-20261127-08 | 20% | 2026-12-21 | economics | The European Central Bank announces a rate cut of at least 25 basis points between 2026-12-12 and 2026-12-19. | True if the ECB announces a rate cut of at least 25 basis points between 2026-12-12 and 2026-12-19; False otherwise. |
| KKR-20261127-09 | 45% | 2026-12-16 | disaster | A forest fire in the Amazon basin reaches an area of at least 100 square kilometers between 2026-12-01 and 2026-12-14. | True if a forest fire in the Amazon basin reaches an area of at least 100 square kilometers between 2026-12-01 and 2026-12-14; False otherwise. |
| KKR-20261127-10 | 30% | 2026-12-17 | cyber | The UK Department for Work and Pensions confirms a second major cyber incident between 2026-12-01 and 2026-12-15. | True if the UK DWP confirms a second major cyber incident between 2026-12-01 and 2026-12-15; False otherwise. |
| KKR-20261127-11 | 55% | 2026-12-12 | political | Spain's election results confirm a victory for Pedro Sánchez's party between 2026-12-01 and 2026-12-10. | True if Spain's election results confirm a victory for Pedro Sánchez's party between 2026-12-01 and 2026-12-10; False otherwise. |
| KKR-20261127-12 | 35% | 2026-12-16 | military_conflict | A Houthi attack on a commercial shipping vessel in the Red Sea results in at least one fatality between 2026-12-01 and 2026-12-14. | True if a Houthi attack on a commercial shipping vessel in the Red Sea results in at least one fatality between 2026-12-01 and 2026-12-14; False otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-27 and 2026-12-03 for a vulnerability with CVSS score 9.0 or higher." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "WTI Crude closes below 80.00 USD per barrel on any trading day between 2026-12-01 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A drone strike hits a populated area in Kyiv or Moscow between 2026-12-01 and 2026-12-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major earthquake (magnitude 6.0 or higher) occurs in Japan between 2026-12-01 and 2026-12-14." → REJECTED: no grounding citations to the report record

## III. LEDGER STANDING

5999 issued all-time across 23 forecaster arms · 4277 open (2360 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 271 issued · 238 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 288 | 271 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 287 | 285 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 271 | 238 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*