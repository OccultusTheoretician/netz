**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-03_1614.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261103-01 | 45% | 2026-11-17 | political | The US Senate holds a confirmed majority of 51 seats or more after the 2026 midterm elections. | The official Senate composition after the 2026 midterms shows the Republican party holding 51 or more seats. |
| KKR-20261103-02 | 25% | 2026-11-16 | economics | The S&P 500 index closes below 7,400 on any trading day between 2026-11-10 and 2026-11-13. | The S&P 500 index closes below 7,400 on any trading day between 2026-11-10 and 2026-11-13. Reference: 7,586.77 on the packet date. |
| KKR-20261103-03 | 85% | 2026-11-20 | disaster | A confirmed forest fire event is logged by GDACS with an event type of WF between 2026-11-10 and 2026-11-17. | A confirmed forest fire event is logged by GDACS with an event type of WF between 2026-11-10 and 2026-11-17. |
| KKR-20261103-04 | 30% | 2027-01-15 | political | The US stops paying aid to Israel after the end of 2026. | The US stops paying aid to Israel after the end of 2026. |
| KKR-20261103-05 | 10% | 2026-11-20 | cyber | A confirmed cyberattack on supermarket refrigeration systems is reported across Europe between 2026-11-10 and 2026-11-17. | A confirmed cyberattack on supermarket refrigeration systems is reported across Europe between 2026-11-10 and 2026-11-17. |
| KKR-20261103-06 | 40% | 2026-11-16 | economics | The Brent crude oil price falls below 95 per barrel on any trading day between 2026-11-10 and 2026-11-13. | The Brent crude oil price falls below 95 per barrel on any trading day between 2026-11-10 and 2026-11-13. Reference: 103.31 on the packet date. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A new CVE is added to the CISA KEV catalog with a date-added value between 2026-11-10 and 2026-11-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A confirmed forest fire event is logged by GDACS with an event type of WF in India between 2026-11-10 and 2026-11-17." → REJECTED: cited items name Botswana, South Sudan, Sudan; the claim is about India — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A confirmed cyberattack on supermarket refrigeration systems is reported across Europe between 2026-11-10 and 2026-11-17." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice
- "The Brent crude oil price falls below 95 per barrel on any trading day between 2026-11-10 and 2026-11-13." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice

## III. LEDGER STANDING

5279 issued all-time across 22 forecaster arms · 3557 open (843 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 161 issued · 144 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 59 | 59 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 161 | 144 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 157 | 155 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 144 | 111 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 327 | 313 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*