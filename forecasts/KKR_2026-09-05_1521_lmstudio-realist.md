**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260905-09 | 25% | 2026-09-14 | military/conflict | Between 2026-09-05 and 2026-09-12, at least one drone strike will be reported in the Kyiv region with confirmed casualties from a cross-bias source. | At least one drone strike in the Kyiv region between 2026-09-05 and 2026-09-12 is confirmed by at least two independently biased sources reporting casualties. |
| KKR-20260905-10 | 20% | 2026-09-14 | cyber | Between 2026-09-05 and 2026-09-12, a major cyberattack exploiting CVE-2026-85046 will be confirmed by at least two independent sources. | At least two independent sources confirm a cyberattack exploiting CVE-2026-85046 between 2026-09-05 and 2026-09-12. |
| KKR-20260905-11 | 35% | 2026-09-14 | military/conflict | Between 2026-09-05 and 2026-09-12, the US will conduct a military strike on an Iranian oil tanker in the Persian Gulf. | A US military strike on an Iranian oil tanker in the Persian Gulf is confirmed by at least two independently biased sources between 2026-09-05 and 2026-09-12. |
| KKR-20260905-12 | 15% | 2026-09-14 | disaster | Between 2026-09-05 and 2026-09-12, a new earthquake of magnitude 6.0 or higher will be recorded in the USGS Significant Quakes database. | A new earthquake of magnitude 6.0 or higher is recorded in the USGS Significant Quakes database between 2026-09-05 and 2026-09-12. |
| KKR-20260905-13 | 40% | 2026-09-14 | disaster | Between 2026-09-05 and 2026-09-12, at least one forest fire in Africa will be reported by GDACS Alerts with a green alert level. | At least one forest fire in Africa is reported by GDACS Alerts with a green alert level between 2026-09-05 and 2026-09-12. |
| KKR-20260905-14 | 30% | 2026-09-14 | political | Between 2026-09-05 and 2026-09-12, the US will announce new sanctions on Iran related to regional proxy activities. | The US announces new sanctions on Iran related to regional proxy activities between 2026-09-05 and 2026-09-12, confirmed by at least two independently biased sources. |
| KKR-20260905-15 | 45% | 2026-09-14 | political | Between 2026-09-05 and 2026-09-12, a new political scandal involving a US government official will be reported by at least two independent sources. | A new political scandal involving a US government official is reported by at least two independent sources between 2026-09-05 and 2026-09-12. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-06, the CISA KEV catalog will carry a date-added value of CVE-2026-85046 between 2026-09-04 and 2026-09-05." → REJECTED: event window opens 2026-09-04, before this row is sealed (2026-09-05, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-85046 dateAdded 2026-09-04, already inside the claimed window 2026-09-04..2026-09-05
- "Between 2026-09-05 and 2026-09-12, the S&P 500 will close above 7,750 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-05 and 2026-09-12, a major cyberattack on a US federal agency will be confirmed by at least two independent sources." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1491 issued all-time across 16 forecaster arms · 1226 open (87 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 11 issued · 11 open · nothing resolved yet — this arm earns a score at its first resolution.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 431 | 403 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*