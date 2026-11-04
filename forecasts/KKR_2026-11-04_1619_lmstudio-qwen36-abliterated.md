**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041619Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-04_1615.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261104-08 | 30% | 2026-11-12 | economics | WTI Crude closes below 85.00 USD per barrel on the Nasdaq settlement on 2026-11-12. | Reference: 91.85 USD on the packet date. WTI Crude closes below 85.00 USD per barrel on the Nasdaq settlement on 2026-11-12. |
| KKR-20261104-09 | 20% | 2026-11-13 | disaster | A forest fire notification is recorded in GDACS Alerts for Nigeria between 2026-11-04 and 2026-11-11. | GDACS Alerts records a forest fire notification for Nigeria with an event date between 2026-11-04 and 2026-11-11. |
| KKR-20261104-10 | 65% | 2026-11-12 | economics | The S&P 500 closes above 7,600 on the Nasdaq settlement on 2026-11-12. | Reference: 7,683.68 on the packet date. The S&P 500 closes above 7,600 on the Nasdaq settlement on 2026-11-12. |
| KKR-20261104-11 | 35% | 2026-11-13 | cyber | Binance confirms a crypto heist exceeding 6.0 billion USD between 2026-11-04 and 2026-11-11. | Binance confirms a crypto heist exceeding 6.0 billion USD with a date of confirmation between 2026-11-04 and 2026-11-11. |
| KKR-20261104-12 | 40% | 2026-11-12 | economics | The 10Y Treasury Yield closes below 4.80 percent on the Federal Reserve settlement on 2026-11-12. | Reference: 4.91 percent on the packet date. The 10Y Treasury Yield closes below 4.80 percent on the Federal Reserve settlement on 2026-11-12. |
| KKR-20261104-13 | 20% | 2026-11-13 | disaster | A forest fire notification is recorded in GDACS Alerts for Sudan between 2026-11-04 and 2026-11-11. | GDACS Alerts records a forest fire notification for Sudan with an event date between 2026-11-04 and 2026-11-11. |
| KKR-20261104-14 | 15% | 2026-11-13 | political | The US House of Representatives passes a resolution to reverse Trump tariffs between 2026-11-04 and 2026-11-11. | The US House of Representatives passes a resolution to reverse Trump tariffs with a date of passage between 2026-11-04 and 2026-11-11. |
| KKR-20261104-15 | 20% | 2026-11-13 | disaster | A forest fire notification is recorded in GDACS Alerts for Botswana between 2026-11-04 and 2026-11-11. | GDACS Alerts records a forest fire notification for Botswana with an event date between 2026-11-04 and 2026-11-11. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-119977 between 2026-11-04 and 2026-11-11." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-119977 dateAdded 2026-11-03, before the claimed window 2026-11-04..2026-11-11; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Binance confirms a crypto heist exceeding 6.0 billion USD between 2026-11-04 and 2026-11-11." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice

## III. LEDGER STANDING

5317 issued all-time across 22 forecaster arms · 3595 open (1018 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 169 issued · 167 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 66 | 66 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 168 | 151 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 169 | 167 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 149 | 116 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 334 | 320 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*