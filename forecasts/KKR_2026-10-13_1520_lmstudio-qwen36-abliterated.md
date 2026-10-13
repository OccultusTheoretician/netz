**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-18 | 85% | 2026-10-30 | political | Kimberly Guilfoyle resigns as ambassador between 2026-10-20 and 2026-10-27. | Public reporting confirms Kimberly Guilfoyle has resigned as ambassador by 2026-10-27. |
| KKR-20261013-19 | 60% | 2026-11-09 | economics | WTI Crude closes above 95.00 on at least one trading day between 2026-11-02 and 2026-11-06. | WTI Crude closes above 95.00 on at least one trading day between 2026-11-02 and 2026-11-06. Reference: 93.94 on the packet date. |
| KKR-20261013-20 | 70% | 2026-11-20 | disaster | A magnitude 6.0 or greater earthquake occurs between 2026-11-10 and 2026-11-17. | USGS Significant Quakes reports an earthquake with magnitude 6.0 or greater between 2026-11-10 and 2026-11-17. |
| KKR-20261013-21 | 55% | 2026-11-27 | economics | Six Flags stock closes below 10.00 on at least one trading day between 2026-11-20 and 2026-11-24. | Six Flags stock closes below 10.00 on at least one trading day between 2026-11-20 and 2026-11-24. |
| KKR-20261013-22 | 30% | 2026-12-11 | cyber | A cyberattack causes a service outage for Yandex between 2026-12-01 and 2026-12-08. | Public reporting confirms a cyberattack caused a service outage for Yandex between 2026-12-01 and 2026-12-08. |
| KKR-20261013-23 | 25% | 2026-12-25 | disaster | Pennsylvania reports a seventh death from the measles outbreak between 2026-12-15 and 2026-12-22. | Public reporting confirms a seventh death from the measles outbreak in Pennsylvania between 2026-12-15 and 2026-12-22. |
| KKR-20261013-24 | 45% | 2027-01-11 | economics | The 10Y US Treasury Yield closes below 5.00 on at least one trading day between 2027-01-04 and 2027-01-08. | The 10Y US Treasury Yield closes below 5.00 on at least one trading day between 2027-01-04 and 2027-01-08. Reference: 5.21 on the packet date. |
| KKR-20261013-25 | 65% | 2027-02-11 | military | A Houthi airstrike hits a position in Yemen between 2027-02-01 and 2027-02-08. | Public reporting confirms a Houthi airstrike hit a position in Yemen between 2027-02-01 and 2027-02-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA KEV catalog carries CVE-2026-104935 with a date-added value between 2026-10-13 and 2026-10-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, already inside the claimed window 2026-10-13..2026-10-20
- "India holds a general election or major parliamentary vote between 2027-03-01 and 2027-03-15." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

4039 issued all-time across 21 forecaster arms · 2928 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 48 issued · 48 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1128 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 49 | 49 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 48 | 48 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 54 | 54 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 217 | 158 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 328 | 270 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*