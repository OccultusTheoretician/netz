**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051503Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-05_1501.md · forecaster: lmstudio/auto · 2 accepted / 8 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260805-01 | 85% | 2026-08-14 | cyber | The CISA KEV catalog includes CVE-2026-9198 (IBM Langflow Code Injection) as actively exploited between 2026-08-05 and 2026-08-12. | The CISA KEV catalog carries a date-added value between 2026-08-05 and 2026-08-12 for CVE-2026-9198. |
| KKR-20260805-02 | 30% | 2026-08-14 | disaster | A magnitude 6.0 or greater earthquake with a depth of less than 100km occurs in the Philippines between 2026-08-05 and 2026-08-12. | The USGS Significant Quakes feed reports a magnitude 6.0 or greater earthquake with a depth of less than 100km in the Philippines between 2026-08-05 and 2026-08-12. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A drone attack with explosive payload targeting a commercial aircraft at Leipzig Airport, Germany, results in at least one fatality between " → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The S&P 500 index closes above 7,800 on a weekday between 2026-08-12 and 2026-08-19." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Iran and the United States reach a formal agreement on maritime security in the Strait of Hormuz between 2026-08-05 and 2026-08-12." → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A cyberattack exploiting CVE-2026-34486 (Apache Tomcat Missing Encryption) causes a public data breach at a U.S. federal agency between 2026" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The House Ethics Committee issues a formal report recommending disciplinary action against Ohio Republican Max Miller between 2026-08-05 and" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A tropical cyclone named KUJIRA-26 causes a flood alert in Sri Lanka with a population affected exceeding 50,000 between 2026-08-05 and 2026" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "The U.S. Federal Reserve announces a 0.25 percentage point increase in the federal funds rate between 2026-08-12 and 2026-08-19." → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A drone attack on a Ukrainian military target in the Belgorod region results in at least one confirmed casualty between 2026-08-05 and 2026-" → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

324 issued all-time across 14 forecaster arms · 286 open (1 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 17 issued · 17 open · nothing resolved yet — this arm earns a score at its first resolution.

*11 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 26 | 26 | 7 | 19 | 0.228 | 26.9% | 0.197 | -0.160 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 22 | 22 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*