**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061616Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-06_1614.md · forecaster: lmstudio/qwen36-realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261106-05 | 25% | 2026-11-13 | economic | The Nasdaq Composite Index closes below 24,000 on any weekday between 2026-11-09 and 2026-11-13. | The Nasdaq Composite Index closing value on 2026-11-13 is strictly less than 24,000. |
| KKR-20261106-06 | 15% | 2026-11-20 | political | The European Union imposes a formal antitrust fine on TikTok exceeding 500 million euros between 2026-11-09 and 2026-11-20. | The European Commission publishes a press release or official decision imposing a fine on TikTok exceeding 500 million euros between 2026-11-09 and 2026-11-20. |
| KKR-20261106-07 | 35% | 2026-11-13 | political | The UK government extends its Palantir NHS contract for a period exceeding one year between 2026-11-09 and 2026-11-13. | The UK Department of Health and Social Care publishes a contract award notice extending the Palantir NHS contract for a period exceeding one year between 2026-11-09 and 2026-11-13. |
| KKR-20261106-08 | 45% | 2026-11-13 | economic | Brent Crude Oil closes below 90 USD per barrel on any weekday between 2026-11-09 and 2026-11-13. | Brent Crude Oil settlement price on 2026-11-13 is strictly less than 90 USD per barrel. |
| KKR-20261106-09 | 5% | 2026-11-13 | cyber | A new zero-day vulnerability is disclosed for D-Link DGS-3130 Series switches between 2026-11-09 and 2026-11-13. | A vendor advisory or CISA alert discloses a new zero-day vulnerability for D-Link DGS-3130 Series switches between 2026-11-09 and 2026-11-13. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A new vulnerability is added to the CISA Known Exploited Vulnerabilities (KEV) catalog with a date-added value between 2026-11-09 and 2026-1" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Tesla formally announces the complete cessation of Cybertruck production in Texas between 2026-11-09 and 2026-11-13." → REJECTED: resolution offers alternative VENUES joined by 'or' (…press release | or | sec…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A magnitude 6.0 or greater earthquake occurs in Fiji between 2026-11-09 and 2026-11-13." → REJECTED: resolution offers alternative VENUES joined by 'or' (…usgs | or | gdacs…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new bomb threat disrupts at least one commercial flight in Europe between 2026-11-09 and 2026-11-13." → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-11-13) is 0 day(s) after the window closes (2026-11-13). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "The US Federal Reserve announces a rate cut of at least 25 basis points at its meeting between 2026-11-09 and 2026-11-13." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5385 issued all-time across 22 forecaster arms · 3663 open (1268 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 160 issued · 127 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 87 | 87 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 179 | 162 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 173 | 171 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 160 | 127 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 485 | 370 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 343 | 329 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*