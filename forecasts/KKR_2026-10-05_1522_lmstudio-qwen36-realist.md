**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: lmstudio/qwen36-realist · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-13 | 70% | 2026-10-21 | crime/security | A US federal court issues an indictment against the alleged developer of Ploutus ATM malware between 2026-10-12 and 2026-10-19. | A US federal court issues an indictment against the alleged developer of Ploutus ATM malware on any date between 2026-10-12 and 2026-10-19. |
| KKR-20261005-14 | 75% | 2026-10-21 | political | The US Supreme Court hears oral arguments in the case involving big oil's bid to block climate damage lawsuits between 2026-10-12 and 2026-10-19. | The US Supreme Court hears oral arguments in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19. |
| KKR-20261005-15 | 30% | 2026-10-21 | disaster | A forest fire notification is issued by GDACS for Brazil between 2026-10-12 and 2026-10-19. | A forest fire notification is issued by GDACS for Brazil on any date between 2026-10-12 and 2026-10-19. |
| KKR-20261005-16 | 10% | 2026-10-21 | political | The US Supreme Court issues a ruling in the case involving big oil's bid to block climate damage lawsuits between 2026-10-12 and 2026-10-19. | The US Supreme Court issues a ruling in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19. |
| KKR-20261005-17 | 35% | 2026-10-21 | disaster | A flood alert is issued by GDACS for France between 2026-10-12 and 2026-10-19. | A flood alert is issued by GDACS for France on any date between 2026-10-12 and 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-88779 between 2026-10-05 and 2026-10-12." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88779 dateAdded 2026-10-04, before the claimed window 2026-10-05..2026-10-12; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Spain holds a general election between 2026-10-12 and 2026-10-19." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The S&P 500 closes below 7,500 on any trading day between 2026-10-12 and 2026-10-19." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Brent crude oil closes above 105.00 on any trading day between 2026-10-12 and 2026-10-19." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new exploited vulnerability is added to the CISA KEV catalog between 2026-10-12 and 2026-10-19." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3408 issued all-time across 20 forecaster arms · 2594 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 5 issued · 5 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1218 | 1017 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 258 | 225 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 46 | 46 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*