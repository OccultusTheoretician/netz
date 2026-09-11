**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: lmstudio/realist · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-06 | 30% | 2026-09-20 | military/conflict | Between 2026-09-11 and 2026-09-17, at least one reported drone strike in the Kyiv theater will be confirmed by cross-bias agreement across three hostile sides. | At least one drone strike in the Kyiv theater, reported between 2026-09-11 and 2026-09-17, is confirmed by cross-bias agreement across three hostile sides (RU, UA, WEST). |
| KKR-20260911-07 | 40% | 2026-09-20 | cyber | Between 2026-09-11 and 2026-09-17, at least one new vulnerability in the CISA KEV catalog will be linked to an active exploit in a critical infrastructure system. | Between 2026-09-11 and 2026-09-17, at least one vulnerability listed in the CISA KEV catalog is actively exploited in a critical infrastructure system. |
| KKR-20260911-08 | 35% | 2026-09-22 | cyber | Between 2026-09-13 and 2026-09-19, at least one major cyberattack on a U.S. financial institution will be reported by two or more independent outlets with hostile bias. | Between 2026-09-13 and 2026-09-19, at least one major cyberattack on a U.S. financial institution is reported by two or more independent outlets with hostile bias (e.g., RU, WEST, AXIS). |
| KKR-20260911-09 | 60% | 2026-09-23 | economics/markets | Between 2026-09-14 and 2026-09-20, the 10-year U.S. Treasury yield will exceed 5.0% on at least one weekday. | The 10-year U.S. Treasury yield exceeds 5.0% on at least one weekday between 2026-09-14 and 2026-09-20. |
| KKR-20260911-10 | 30% | 2026-09-24 | military/conflict | Between 2026-09-15 and 2026-09-21, at least one confirmed airstrike in the Khan Younis area will be reported by three or more independent outlets with hostile bias. | Between 2026-09-15 and 2026-09-21, at least one confirmed airstrike in the Khan Younis area is reported by three or more independent outlets with hostile bias (AXIS, IL, PS). |
| KKR-20260911-11 | 20% | 2026-09-25 | economics/markets | Between 2026-09-16 and 2026-09-22, the U.S. dollar will trade above 1.17 against the euro on at least one weekday. | The EUR/USD exchange rate is below 1.17 on at least one weekday between 2026-09-16 and 2026-09-22. |
| KKR-20260911-12 | 45% | 2026-09-26 | cyber | Between 2026-09-17 and 2026-09-23, at least one new cyberattack exploiting CVE-2026-67277 will be reported by two or more independent outlets. | Between 2026-09-17 and 2026-09-23, at least one cyberattack exploiting CVE-2026-67277 is reported by two or more independent outlets. |
| KKR-20260911-13 | 25% | 2026-09-27 | political | Between 2026-09-18 and 2026-09-24, at least one major political statement about Iran's nuclear program will be made by a U.S. or EU official and confirmed by cross-bias agreement across two hostile sides. | Between 2026-09-18 and 2026-09-24, at least one major political statement about Iran's nuclear program is made by a U.S. or EU official and confirmed by cross-bias agreement across two hostile sides (AXIS, WEST). |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-15, the CISA KEV catalog will include CVE-2026-86060 with a date-added value of 2026-09-10." → REJECTED: event window opens 2026-09-10, before this row is sealed (2026-09-11, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-12 and 2026-09-18, the S&P 500 will close above 7,700 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1893 issued all-time across 16 forecaster arms · 1557 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 45 issued · 45 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 596 | 558 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*