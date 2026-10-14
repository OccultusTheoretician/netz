**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: lmstudio/qwen36 · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-07 | 45% | 2026-11-02 | cyber | The CISA KEV catalog carries a date-added value for a new critical zero-day vulnerability between 2026-10-27 and 2026-10-30. | A new entry appears in the CISA KEV catalog with a date-added value falling within the event window. |
| KKR-20261014-08 | 25% | 2026-11-05 | military_conflict | A Houthi missile or drone successfully strikes a target inside Saudi Arabia between 2026-10-27 and 2026-11-03. | A public report confirms a Houthi projectile struck a target inside Saudi Arabia within the event window. |
| KKR-20261014-09 | 20% | 2026-11-05 | disaster | The USGS reports a magnitude 7.0 or greater earthquake between 2026-10-27 and 2026-11-03. | The USGS Significant Quakes catalog records an event with magnitude 7.0 or higher within the event window. |
| KKR-20261014-10 | 35% | 2026-11-03 | economics | The 10-year US Treasury yield closes above 5.50 percent at least once between 2026-10-27 and 2026-11-02. | The 10-year US Treasury yield closes above 5.50 percent on at least one trading day within the event window. |
| KKR-20261014-11 | 10% | 2026-11-05 | political | Turkey halts live broadcasts of a major opposition TV station between 2026-10-27 and 2026-11-03. | A public report confirms Turkish authorities halted live broadcasts of a major opposition TV station within the event window. |
| KKR-20261014-12 | 25% | 2026-11-03 | economics | Brent crude oil closes above 115.00 dollars per barrel at least once between 2026-10-27 and 2026-11-02. | Brent crude oil closes above 115.00 dollars per barrel on at least one trading day within the event window. |
| KKR-20261014-13 | 40% | 2026-11-05 | disaster | The USGS reports a magnitude 6.5 or greater earthquake between 2026-10-27 and 2026-11-03. | The USGS Significant Quakes catalog records an event with magnitude 6.5 or higher within the event window. |
| KKR-20261014-14 | 20% | 2026-11-02 | cyber | A new critical zero-day vulnerability affecting major infrastructure is added to the CISA KEV catalog between 2026-10-27 and 2026-10-30. | A new entry appears in the CISA KEV catalog with a date-added value falling within the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,600 at least once between 2026-10-27 and 2026-11-02." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The Pope dies between 2026-10-27 and 2026-11-03." → REJECTED: resolution offers alternative VENUES joined by 'or' (…vatican | or | major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4109 issued all-time across 21 forecaster arms · 2998 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 57 issued · 57 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
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