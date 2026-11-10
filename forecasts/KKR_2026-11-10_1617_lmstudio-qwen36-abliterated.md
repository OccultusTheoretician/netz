**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101617Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-10_1613.md · forecaster: lmstudio/qwen36-abliterated · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261110-11 | 90% | 2026-11-20 | cyber | The CISA KEV catalog carries a date-added value between 2026-11-10 and 2026-11-17 for at least one CVE that explicitly names OpenSSH, GPUStack, FreeSWITCH, or IBM Aspera Faspex. | The CISA KEV catalog contains at least one record with date-added between 2026-11-10 and 2026-11-17 for a CVE naming OpenSSH, GPUStack, FreeSWITCH, or IBM Aspera Faspex. |
| KKR-20261110-12 | 30% | 2026-11-20 | economics | The S&P 500 index closes below 7,400.00 on at least one trading day between 2026-11-10 and 2026-11-17. | The S&P 500 index closes below 7,400.00 on at least one trading day between 2026-11-10 and 2026-11-17. Reference: 7,502.77 on the packet date. |
| KKR-20261110-13 | 25% | 2026-11-20 | political | The House of Representatives votes to impeach Pete Hegseth between 2026-11-10 and 2026-11-17. | The House of Representatives votes to impeach Pete Hegseth on a recorded roll call vote between 2026-11-10 and 2026-11-17. |
| KKR-20261110-14 | 60% | 2026-11-20 | disaster | The USGS records a magnitude 5.0 or greater earthquake between 2026-11-10 and 2026-11-17. | The USGS records at least one earthquake with magnitude 5.0 or greater between 2026-11-10 and 2026-11-17. |
| KKR-20261110-15 | 35% | 2026-11-20 | economics | The Brent crude oil price closes below $85.00 on at least one trading day between 2026-11-10 and 2026-11-17. | The Brent crude oil price closes below $85.00 on at least one trading day between 2026-11-10 and 2026-11-17. Reference: 90.62 on the packet date. |
| KKR-20261110-16 | 45% | 2026-11-20 | cyber | A Russian Turla group hacker is publicly attributed with a cyberattack on a French supermarket chain between 2026-11-10 and 2026-11-17. | A French government agency or court officially attributes a cyberattack on a French supermarket chain to the Russian Turla group between 2026-11-10 and 2026-11-17. |
| KKR-20261110-17 | 20% | 2026-11-20 | disaster | A significant forest fire is recorded in Australia between 2026-11-10 and 2026-11-17. | The GDACS Alerts records a significant forest fire in Australia between 2026-11-10 and 2026-11-17. |
| KKR-20261110-18 | 15% | 2026-11-20 | political | The US Senate confirms a judicial nominee between 2026-11-10 and 2026-11-17. | The US Senate confirms at least one judicial nominee on a recorded roll call vote between 2026-11-10 and 2026-11-17. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Anthropic completes its initial public offering with a final share price between $70.00 and $78.00 between 2026-11-10 and 2026-11-17." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The US Federal Reserve announces a rate decision between 2026-11-10 and 2026-11-17." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5543 issued all-time across 22 forecaster arms · 3821 open (1420 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 204 issued · 202 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 132 | 132 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 198 | 181 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 204 | 202 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 178 | 145 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 509 | 394 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 364 | 350 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*