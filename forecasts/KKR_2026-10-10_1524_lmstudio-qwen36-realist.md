**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101524Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-10_1517.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261010-17 | 25% | 2026-10-22 | cyber | The CISA KEV catalog carries a date-added value between 2026-10-11 and 2026-10-18 for a vulnerability exploited in the wild to deploy webshells or mine crypto. | A new entry in the CISA KEV catalog with a date-added value in the window and description matching webshell deployment or crypto mining. |
| KKR-20261010-18 | 30% | 2026-10-20 | economics/markets | WTI Crude futures settle above 95.00 USD per barrel on at least one trading day between 2026-10-13 and 2026-10-16. | A settlement price for WTI Crude futures exceeding 95.00 USD per barrel on a weekday in the window. |
| KKR-20261010-19 | 65% | 2026-10-22 | military/conflict | A Russian glide bomb or missile strike hits a populated area in Ukraine causing at least 10 fatalities between 2026-10-11 and 2026-10-18. | Two wire services report a Russian strike on a populated area in Ukraine with 10 or more fatalities in the window. |
| KKR-20261010-20 | 45% | 2026-10-22 | political | India detains at least 500 individuals in New Delhi during protests between 2026-10-11 and 2026-10-18. | Two wire services report the detention of at least 500 individuals in New Delhi during protests in the window. |
| KKR-20261010-21 | 15% | 2026-10-22 | disaster | A magnitude 7.0 or greater earthquake occurs in Panama between 2026-10-11 and 2026-10-18. | The USGS catalog carries a date-added value in the window for a magnitude 7.0 or greater earthquake in Panama. |
| KKR-20261010-22 | 35% | 2026-10-22 | disaster | A tropical storm or hurricane makes landfall in the United States between 2026-10-11 and 2026-10-18. | The NWS or NOAA issues a landfall warning or report for a tropical storm or hurricane in the United States in the window. |
| KKR-20261010-23 | 5% | 2026-10-22 | cyber | A major cyberattack disrupts the power grid of a NATO member state between 2026-10-11 and 2026-10-18. | Two wire services report a major cyberattack disrupting the power grid of a NATO member state in the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index settles above 8,000 on at least one trading day between 2026-10-13 and 2026-10-16." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new major ransomware group emerges with a public manifesto or claim of responsibility between 2026-10-11 and 2026-10-18." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The European Central Bank announces an interest rate cut between 2026-10-11 and 2026-10-18." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…ecb website | or | two…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count; the resolution names only a venue or register (ecb) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

3802 issued all-time across 21 forecaster arms · 2988 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 40 issued · 40 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
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