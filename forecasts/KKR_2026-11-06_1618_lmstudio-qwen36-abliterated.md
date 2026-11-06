**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061618Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-06_1614.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261106-10 | 30% | 2026-11-20 | cyber | A cyberattack on refrigeration systems is catalogued in the CISA KEV between 2026-11-10 and 2026-11-17. | The CISA KEV catalog carries a date-added value between 2026-11-10 and 2026-11-17 for a vulnerability related to refrigeration systems. |
| KKR-20261106-11 | 35% | 2026-11-16 | economics/markets | The Nasdaq Composite closes below 24,000 on at least one trading day between 2026-11-10 and 2026-11-13, referencing the 24,621.83 seal. | The closing value of the Nasdaq Composite index is strictly below 24,000 on any trading day between 2026-11-10 and 2026-11-13. |
| KKR-20261106-12 | 40% | 2026-11-20 | disaster | A forest fire in China is confirmed by GDACS between 2026-11-10 and 2026-11-17. | GDACS issues a forest fire alert for China with an event date between 2026-11-10 and 2026-11-17. |
| KKR-20261106-13 | 50% | 2026-11-20 | political | The UK government formally extends the Palantir NHS contract between 2026-11-10 and 2026-11-17. | A UK government announcement or official document confirms the extension of the Palantir NHS contract between 2026-11-10 and 2026-11-17. |
| KKR-20261106-14 | 40% | 2026-11-20 | economics/markets | Tesla announces the final wind-down of Cybertruck production in Texas between 2026-11-10 and 2026-11-17. | Tesla issues a public announcement or press release confirming the final wind-down of Cybertruck production in Texas between 2026-11-10 and 2026-11-17. |
| KKR-20261106-15 | 45% | 2026-11-20 | political | The EU imposes a fine on TikTok for mental health failures between 2026-11-10 and 2026-11-17. | The European Commission issues a formal decision or fine against TikTok regarding mental health failures between 2026-11-10 and 2026-11-17. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes below 7,200 on at least one trading day between 2026-11-10 and 2026-11-13, referencing the 7,405.12 seal." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Russia launches a kinetic strike on a Ukrainian energy facility between 2026-11-10 and 2026-11-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A tropical cyclone makes landfall in a populated area between 2026-11-10 and 2026-11-17." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A significant earthquake (Magnitude 6.0 or higher) occurs in the Pacific Rim between 2026-11-10 and 2026-11-17." → REJECTED: resolution offers alternative VENUES joined by 'or' (…usgs | or | gdacs reports an earthquake…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5391 issued all-time across 22 forecaster arms · 3669 open (1268 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 179 issued · 177 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 87 | 87 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 179 | 162 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 179 | 177 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 160 | 127 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 485 | 370 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 343 | 329 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*