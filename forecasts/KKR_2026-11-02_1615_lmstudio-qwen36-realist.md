**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-02_1612.md · forecaster: lmstudio/qwen36-realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261102-07 | 30% | 2026-11-09 | economics/markets | WTI Crude settles below 90.00 USD per barrel on the New York Mercantile Exchange on any weekday between 2026-11-02 and 2026-11-06. | WTI Crude settles below 90.00 USD per barrel on the New York Mercantile Exchange on any weekday between 2026-11-02 and 2026-11-06. Reference: 97.31 USD on the packet date. |
| KKR-20261102-08 | 20% | 2026-11-12 | political | The Federal Register publishes a final rule between 2026-11-02 and 2026-11-09 that imposes new sanctions on entities linked to the Iranian nuclear program. | The Federal Register publishes a final rule between 2026-11-02 and 2026-11-09 that imposes new sanctions on entities linked to the Iranian nuclear program. |
| KKR-20261102-09 | 15% | 2026-11-12 | disaster | A confirmed earthquake with magnitude 6.0 or higher occurs in Tanzania between 2026-11-02 and 2026-11-09. | A confirmed earthquake with magnitude 6.0 or higher occurs in Tanzania between 2026-11-02 and 2026-11-09. |
| KKR-20261102-10 | 40% | 2026-11-12 | cyber | A confirmed cyberattack disrupts refrigeration systems at European supermarkets between 2026-11-02 and 2026-11-09. | A confirmed cyberattack disrupts refrigeration systems at European supermarkets between 2026-11-02 and 2026-11-09. |
| KKR-20261102-11 | 15% | 2026-11-12 | disaster | A confirmed earthquake with magnitude 6.0 or higher occurs in Sudan between 2026-11-02 and 2026-11-09. | A confirmed earthquake with magnitude 6.0 or higher occurs in Sudan between 2026-11-02 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-02 and 2026-11-09 for a vulnerability with CVSS score 9.0 or higher." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The European Central Bank announces an interest rate cut between 2026-11-02 and 2026-11-09." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The US Senate confirms a nominee to the Supreme Court between 2026-11-02 and 2026-11-09." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A confirmed cyberattack disrupts refrigeration systems at European supermarkets between 2026-11-02 and 2026-11-09." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice
- "WTI Crude settles below 90.00 USD per barrel on the New York Mercantile Exchange on any weekday between 2026-11-02 and 2026-11-06." → REJECTED: DUPBATCH-1026 duplicate of an earlier row of this batch; not sealed twice

## III. LEDGER STANDING

5253 issued all-time across 22 forecaster arms · 3531 open (721 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 144 issued · 111 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

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
| lmstudio/qwen36-abliterated | 149 | 147 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
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