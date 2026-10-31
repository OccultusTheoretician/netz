**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 311517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-31_1513.md · forecaster: lmstudio/qwen36-abliterated · 3 accepted / 7 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261031-04 | 40% | 2026-11-09 | economics/markets | WTI Crude closes above 110.00 on any weekday between 2026-11-02 and 2026-11-06. Reference: 104.12 on the packet date. | The WTI Crude settlement price is strictly greater than 110.00 on at least one day within the event window. |
| KKR-20261031-05 | 20% | 2026-11-12 | disaster | A forest fire notification is issued by GDACS for Brazil between 2026-11-02 and 2026-11-09. | GDACS Alerts issues a forest fire notification for Brazil with a date between 2026-11-02 and 2026-11-09. |
| KKR-20261031-06 | 35% | 2026-11-12 | military/conflict | The US Senate passes a resolution to confirm the sale of 500 Patriot missiles to Ukraine between 2026-11-02 and 2026-11-09. | The US Senate passes a resolution confirming the sale of 500 Patriot missiles to Ukraine with a date between 2026-11-02 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,500.00 on any weekday between 2026-11-02 and 2026-11-06. Reference: 7,580.07 on the packet date." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new CVE is added to the CISA KEV catalog between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A major cyberattack on a US financial institution is reported by BleepingComputer or The Hacker News between 2026-11-02 and 2026-11-09." → REJECTED: resolution offers alternative VENUES joined by 'or' (…bleepingcomputer | or | the hacker news reports a major cyberattack o…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new CVE is added to the CISA KEV catalog between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI Crude closes above 110.00 on any weekday between 2026-11-02 and 2026-11-06. Reference: 104.12 on the packet date." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice
- "A forest fire notification is issued by GDACS for Brazil between 2026-11-02 and 2026-11-09." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice
- "The US Senate passes a resolution to confirm the sale of 500 Patriot missiles to Ukraine between 2026-11-02 and 2026-11-09." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice

## III. LEDGER STANDING

5196 issued all-time across 22 forecaster arms · 3474 open (712 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 144 issued · 142 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 36 | 36 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 145 | 128 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 144 | 142 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 136 | 103 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 304 | 290 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*