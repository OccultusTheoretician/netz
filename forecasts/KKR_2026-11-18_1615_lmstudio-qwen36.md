**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-18_1613.md · forecaster: lmstudio/qwen36 · 10 accepted / 0 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261118-01 | 5% | 2026-11-30 | cyber | The CISA KEV catalog carries a date-added value for CVE-2026-114938 between 2026-11-25 and 2026-11-28 | The CISA KEV catalog carries a date-added value for CVE-2026-114938 between 2026-11-25 and 2026-11-28 |
| KKR-20261118-02 | 90% | 2026-12-07 | political | Hakeem Jeffries is sworn in as Speaker of the House between 2026-12-01 and 2026-12-04 | Hakeem Jeffries is sworn in as Speaker of the House between 2026-12-01 and 2026-12-04 |
| KKR-20261118-03 | 25% | 2026-12-07 | economics | The S&P 500 closes below 7,000 on any weekday between 2026-12-01 and 2026-12-04 | The S&P 500 closes below 7,000 on any weekday between 2026-12-01 and 2026-12-04. Reference: 7,309.67 on the packet date |
| KKR-20261118-04 | 15% | 2026-12-21 | political | The ICJ issues a ruling on the Rohingya genocide case against Myanmar between 2026-12-15 and 2026-12-18 | The ICJ issues a ruling on the Rohingya genocide case against Myanmar between 2026-12-15 and 2026-12-18 |
| KKR-20261118-05 | 45% | 2026-12-07 | economics | Anthropic files its final prospectus for its IPO between 2026-12-01 and 2026-12-04 | Anthropic files its final prospectus for its IPO between 2026-12-01 and 2026-12-04 |
| KKR-20261118-06 | 30% | 2026-12-16 | disaster | A magnitude 6.0 or greater earthquake occurs in Indonesia between 2026-12-10 and 2026-12-13 | A magnitude 6.0 or greater earthquake occurs in Indonesia between 2026-12-10 and 2026-12-13 |
| KKR-20261118-07 | 60% | 2026-12-14 | political | Jensen Huang appears before the Senate banking committee between 2026-12-08 and 2026-12-11 | Jensen Huang appears before the Senate banking committee between 2026-12-08 and 2026-12-11 |
| KKR-20261118-08 | 35% | 2026-12-07 | economics | The 10-year US Treasury yield closes above 5.25 percent on any weekday between 2026-12-01 and 2026-12-04 | The 10-year US Treasury yield closes above 5.25 percent on any weekday between 2026-12-01 and 2026-12-04. Reference: 5.07 on the packet date |
| KKR-20261118-09 | 10% | 2026-12-29 | military | Israel announces a new ceasefire agreement with Hamas between 2026-12-20 and 2026-12-23 | Israel announces a new ceasefire agreement with Hamas between 2026-12-20 and 2026-12-23 |
| KKR-20261118-10 | 50% | 2026-12-07 | political | The EU formally approves the 45 billion euro loan to Ukraine between 2026-12-01 and 2026-12-04 | The EU formally approves the 45 billion euro loan to Ukraine between 2026-12-01 and 2026-12-04 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5847 issued all-time across 23 forecaster arms · 4125 open (1972 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 241 issued · 224 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 241 | 224 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 234 | 232 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 219 | 186 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*