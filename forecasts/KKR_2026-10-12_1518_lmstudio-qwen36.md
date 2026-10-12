**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-11 | 20% | 2026-10-24 | military_conflict | Houthi forces strike a commercial airport in Saudi Arabia between 2026-10-19 and 2026-10-22. | Two wire services report a Houthi strike on a Saudi commercial airport with a date of impact falling within the event window. |
| KKR-20261012-12 | 35% | 2026-10-23 | economics | WTI Crude closes above 100.00 USD per barrel on at least one trading day between 2026-10-19 and 2026-10-22. | A public market data feed shows WTI Crude closing above 100.00 USD on a day within the event window. |
| KKR-20261012-13 | 25% | 2026-10-24 | political | The European Commission imposes a final anti-dumping tariff on Chinese hybrid vehicles between 2026-10-19 and 2026-10-22. | The European Commission publishes an official regulation or press release imposing a final anti-dumping tariff on Chinese hybrid vehicles with a date within the event window. |
| KKR-20261012-14 | 40% | 2026-10-24 | disaster | A magnitude 6.0 or greater earthquake occurs in Panama between 2026-10-19 and 2026-10-22. | The USGS catalog records an earthquake with magnitude 6.0 or greater in Panama with a date within the event window. |
| KKR-20261012-15 | 30% | 2026-10-24 | cyber | A critical zero-day vulnerability is added to the CISA KEV catalog between 2026-10-19 and 2026-10-22. | A public query of the CISA KEV catalog shows a record with a date-added value falling within the event window. |
| KKR-20261012-16 | 25% | 2026-10-24 | political | The European Commission imposes a final anti-dumping tariff on Chinese hybrid vehicles between 2026-10-19 and 2026-10-22. | The European Commission publishes an official regulation or press release imposing a final anti-dumping tariff on Chinese hybrid vehicles with a date within the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-10-19 and 2026-10-22 for a vulnerability with CVSS score 10.0 exploiting a Word" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The US Department of Justice files an antitrust complaint against a major US television network between 2026-10-19 and 2026-10-22." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a public court docket | or | doj press release shows an antitrust complain…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A major US bank reports a quarterly net loss between 2026-10-19 and 2026-10-22." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major US bank reports a quarterly net loss between 2026-10-19 and 2026-10-22." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3950 issued all-time across 21 forecaster arms · 2922 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 43 issued · 43 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1399 | 1125 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 320 | 264 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*