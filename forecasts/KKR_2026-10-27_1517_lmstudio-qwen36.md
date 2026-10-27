**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-27_1516.md · forecaster: lmstudio/qwen36 · 9 accepted / 1 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261027-01 | 90% | 2026-11-06 | cyber | The CISA KEV catalog carries a date-added value for a newly exploited vulnerability between 2026-10-28 and 2026-11-04. | A new CVE entry appears in the CISA KEV catalog with a date-added value within the window. |
| KKR-20261027-02 | 25% | 2026-11-06 | disaster | A forest fire notification is issued by GDACS for a location in Australia between 2026-10-28 and 2026-11-04. | A GDACS alert with eventtype WF is published for a location in Australia within the window. |
| KKR-20261027-03 | 5% | 2026-11-06 | political | The Netherlands withdraws its participation from the Eurovision Song Contest 2027 between 2026-10-28 and 2026-11-04. | The European Broadcasting Union or the Dutch broadcaster confirms the withdrawal of the Netherlands from Eurovision 2027. |
| KKR-20261027-04 | 85% | 2026-11-13 | cyber | A new CVE is added to the CISA KEV catalog with a date-added value between 2026-11-05 and 2026-11-11. | A new CVE entry appears in the CISA KEV catalog with a date-added value within the window. |
| KKR-20261027-05 | 20% | 2026-11-09 | economics/markets | The 10-year US Treasury yield closes above 5.10 percent on any trading day between 2026-11-02 and 2026-11-06. | The 10-year US Treasury yield closing value is strictly greater than 5.10 on any trading day in the window. |
| KKR-20261027-06 | 10% | 2026-11-06 | disaster | A forest fire notification is issued by GDACS for a location in Papua New Guinea between 2026-10-28 and 2026-11-04. | A GDACS alert with eventtype WF is published for a location in Papua New Guinea within the window. |
| KKR-20261027-07 | 15% | 2026-11-06 | disaster | A forest fire notification is issued by GDACS for a location in Malawi between 2026-10-28 and 2026-11-04. | A GDACS alert with eventtype WF is published for a location in Malawi within the window. |
| KKR-20261027-08 | 30% | 2026-11-06 | disaster | A forest fire notification is issued by GDACS for a location in China between 2026-10-28 and 2026-11-04. | A GDACS alert with eventtype WF is published for a location in China within the window. |
| KKR-20261027-09 | 20% | 2026-11-06 | disaster | A forest fire notification is issued by GDACS for a location in Sudan between 2026-10-28 and 2026-11-04. | A GDACS alert with eventtype WF is published for a location in Sudan within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,600.00 on any trading day between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

5033 issued all-time across 21 forecaster arms · 3311 open (400 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 125 issued · 108 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1770 | 1261 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 125 | 108 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 123 | 121 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 122 | 89 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 447 | 332 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 276 | 262 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*