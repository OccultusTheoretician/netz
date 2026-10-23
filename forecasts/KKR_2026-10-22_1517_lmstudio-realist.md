**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: lmstudio/realist · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261022-05 | 25% | 2026-11-05 | cyber | Between 2026-10-24 and 2026-10-31, a coordinated cyberattack exploiting the PHP2Shell vulnerability disables at least three critical government systems in the United States, as verified by CISA KEV catalog entries with date-added values in that window. | The CISA KEV catalog carries a date-added value between 2026-10-24 and 2026-10-31 for at least three vulnerabilities linked to the PHP2Shell exploit. |
| KKR-20261022-06 | 10% | 2026-11-09 | disaster | Between 2026-10-30 and 2026-11-06, a major earthquake of magnitude 7.0 or higher occurs in the Pacific Ring of Fire, as confirmed by the USGS Significant Quakes feed with a magnitude of 7.0 or greater and a location within the Ring of Fire. | The USGS Significant Quakes feed reports a magnitude 7.0 or greater earthquake with a location within the Pacific Ring of Fire between 2026-10-30 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-23, a drone strike targeting a military installation in Kyiv, Ukraine, results in at least 30 casualties, confirmed by at least t" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-25, a missile strike on a civilian infrastructure site in Zaporizhzhia, Ukraine, causes at least 30 fatalities, as confirmed by t" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-26 and 2026-11-02, a major wildfire in California spreads beyond 10,000 acres, as confirmed by the USGS Significant Quakes f" → REJECTED: cited items name Argentina, Brazil, China; the claim is about California — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "On 2026-10-27, a cyberattack on a major financial institution in the UK results in a 3% drop in the FTSE 100 index within 24 hours, as confi" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict
- "Between 2026-10-28 and 2026-11-04, a state-sponsored cyberattack on a US government agency leads to the public disclosure of classified docu" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "On 2026-10-29, a drone attack on a civilian site in Gaza City results in at least 30 casualties, as confirmed by two or more independent sou" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-31, a cyberattack on a critical infrastructure provider in Europe results in a 2% or greater drop in the Eurozone composite index" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict
- "Between 2026-11-01 and 2026-11-08, a political assassination of a high-ranking official in Iran occurs, as confirmed by two or more independ" → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict

## III. LEDGER STANDING

4696 issued all-time across 21 forecaster arms · 3344 open (585 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 238 issued · 151 open · 86 resolved · 49 hits / 37 misses · **Brier 0.321** against its own base rate 57.0% (climatological 0.245) · **skill -0.311**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1657 | 1274 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 457 | 216 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*