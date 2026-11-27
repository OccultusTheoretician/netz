**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 261614Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-26_1612.md · forecaster: lmstudio/qwen36-realist · 9 accepted / 1 rejected by validation gate · 8 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261126-05 | 20% | 2026-12-05 | cyber | The CISA KEV catalog carries a date-added value for a new critical vulnerability between 2026-11-27 and 2026-12-03. | The CISA KEV catalog carries a date-added value for a new critical vulnerability between 2026-11-27 and 2026-12-03. |
| KKR-20261126-06 | 90% | 2026-12-05 | economic | Norse Atlantic Airways suspends all flights between 2026-11-27 and 2026-12-03. | Norse Atlantic Airways suspends all flights between 2026-11-27 and 2026-12-03. |
| KKR-20261126-07 | 25% | 2026-12-12 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-04 and 2026-12-10. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-04 and 2026-12-10. |
| KKR-20261126-08 | 20% | 2026-12-19 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-11 and 2026-12-17. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-11 and 2026-12-17. |
| KKR-20261126-09 | 20% | 2026-12-26 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-18 and 2026-12-24. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-18 and 2026-12-24. |
| KKR-20261126-10 | 20% | 2027-01-02 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-25 and 2026-12-31. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2026-12-25 and 2026-12-31. |
| KKR-20261126-11 | 20% | 2027-01-09 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-01 and 2027-01-07. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-01 and 2027-01-07. |
| KKR-20261126-12 | 20% | 2027-01-16 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-08 and 2027-01-14. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-08 and 2027-01-14. |
| KKR-20261126-13 | 20% | 2027-01-23 | cyber | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-15 and 2027-01-21. | A new critical vulnerability is cataloged in the CISA KEV catalog between 2027-01-15 and 2027-01-21. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,000 on any trading day between 2026-11-27 and 2026-12-03." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5980 issued all-time across 23 forecaster arms · 4258 open (2349 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 265 issued · 232 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

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
| lmstudio/qwen36 | 282 | 265 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 280 | 278 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 265 | 232 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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