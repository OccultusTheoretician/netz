**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021617Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-02_1612.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261102-12 | 25% | 2026-11-11 | cyber | The CISA KEV catalog carries a date-added value between 2026-11-02 and 2026-11-09 for a vulnerability exploited in the supermarket refrigeration systems. | True if the CISA KEV catalog lists a vulnerability with a date-added value between 2026-11-02 and 2026-11-09 that is linked to the supermarket refrigeration systems. |
| KKR-20261102-13 | 30% | 2026-11-11 | economics/markets | WTI Crude oil closes below 90.00 USD per barrel on at least one trading day between 2026-11-02 and 2026-11-09. | True if the WTI Crude oil settlement price is below 90.00 USD per barrel on at least one trading day between 2026-11-02 and 2026-11-09. Reference: 97.31 USD on the packet date. |
| KKR-20261102-14 | 45% | 2026-11-11 | military/conflict | A confirmed kinetic event (drone, missile, or airstrike) occurs in the Kherson region between 2026-11-02 and 2026-11-09. | True if at least two distinct channels across two hostile sides report a kinetic event in Kherson between 2026-11-02 and 2026-11-09. |
| KKR-20261102-15 | 35% | 2026-11-11 | economics/markets | The Nasdaq Composite index closes below 25,000 points on at least one trading day between 2026-11-02 and 2026-11-09. | True if the Nasdaq Composite settlement price is below 25,000 points on at least one trading day between 2026-11-02 and 2026-11-09. Reference: 25,652.59 points on the packet date. |
| KKR-20261102-16 | 60% | 2026-11-11 | disaster | A forest fire notification is issued by GDACS for a location in Africa between 2026-11-02 and 2026-11-09. | True if the GDACS Alerts feed issues a forest fire notification for a location in Africa between 2026-11-02 and 2026-11-09. |
| KKR-20261102-17 | 40% | 2026-11-11 | economics/markets | The 10-year US Treasury yield closes above 5.00 percent on at least one trading day between 2026-11-02 and 2026-11-09. | True if the 10-year US Treasury yield settlement price is above 5.00 percent on at least one trading day between 2026-11-02 and 2026-11-09. Reference: 4.91 percent on the packet date. |
| KKR-20261102-18 | 35% | 2026-11-11 | economics/markets | The S&P 500 index closes below 7,600 points on at least one trading day between 2026-11-02 and 2026-11-09. | True if the S&P 500 settlement price is below 7,600 points on at least one trading day between 2026-11-02 and 2026-11-09. Reference: 7,631.17 points on the packet date. |
| KKR-20261102-19 | 45% | 2026-11-11 | military/conflict | A confirmed kinetic event (drone, missile, or airstrike) occurs in the Khan Younis region between 2026-11-02 and 2026-11-09. | True if at least two distinct channels across two hostile sides report a kinetic event in Khan Younis between 2026-11-02 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A confirmed kinetic event (drone, missile, or airstrike) occurs in the Tehran region between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A confirmed kinetic event (drone, missile, or airstrike) occurs in the Hodeidah region between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5261 issued all-time across 22 forecaster arms · 3539 open (721 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 157 issued · 155 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 53 | 53 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 155 | 138 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 157 | 155 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 144 | 111 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 321 | 307 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*