**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 252347Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-27 | 55% | 2026-12-18 | military/conflict | US forces conduct at least one strike on a target located on Iranian land territory, including Iranian islands, between 2026-11-04 and 2026-12-15. | TRUE if US Central Command, the Pentagon or the White House officially confirms a US strike on Iranian land territory or islands occurring between 2026-11-04 and 2026-12-15. Strikes only on vessels at sea do not count. |
| KKR-20261025-28 | 85% | 2026-11-18 | military/conflict | At least one Houthi-launched ballistic missile or drone is intercepted over, or strikes, Saudi Arabian territory between 2026-11-02 and 2026-11-15. | TRUE if the Saudi-led coalition spokesman, the Saudi Ministry of Defense or the Saudi Press Agency states that a Houthi missile or drone was intercepted over or struck Saudi territory between 2026-11-02 and 2026-11-15. |
| KKR-20261025-29 | 60% | 2026-12-11 | economics/markets | The FOMC raises the federal funds target range at its 2026-12-08 to 2026-12-09 meeting, with the decision announced on 2026-12-09. | TRUE if the FOMC statement issued 2026-12-09 raises the target range, as shown by FRED series DFEDTARU for 2026-12-10 exceeding its 2026-12-08 value. Unchanged or lower resolves FALSE. |
| KKR-20261025-30 | 32% | 2026-12-17 | economics/markets | The ICE Brent front-month crude futures contract settles below 100.00 USD per barrel on 2026-12-15. Reference: 111.70 on the packet date. | TRUE if the ICE Futures Europe official settlement price of the front-month Brent crude futures contract on 2026-12-15 is below 100.00 USD per barrel. Reference: 111.70 on the packet date. |
| KKR-20261025-31 | 86% | 2027-01-11 | political | Democrats win at least 218 of 435 seats in the US House of Representatives in the general election held on 2026-11-03. | TRUE if the Clerk of the House party breakdown for the 120th Congress, after members elected on 2026-11-03 are sworn in, lists at least 218 Democrats. Fewer than 218 resolves FALSE. |
| KKR-20261025-32 | 38% | 2026-11-02 | political | Luiz Inacio Lula da Silva defeats Flavio Bolsonaro in the Brazilian presidential runoff held on 2026-10-25. | TRUE if the Superior Electoral Court (TSE) official totals for the 2026-10-25 presidential runoff give Lula da Silva more than 50 percent of valid votes; FALSE if Flavio Bolsonaro wins. |
| KKR-20261025-33 | 30% | 2026-11-24 | disaster | Nigeria confirms at least one new Ebola case between 2026-10-26 and 2026-11-20, raising its cumulative confirmed count above the total held on 2026-10-25. | TRUE if an NCDC situation report or WHO Disease Outbreak News shows Nigeria with a higher cumulative confirmed Ebola case count for a date between 2026-10-26 and 2026-11-20 than on 2026-10-25. |
| KKR-20261025-34 | 47% | 2026-12-03 | disaster | The UK Met Office, Met Eireann or KNMI names at least one new storm, following Storm Boelo, between 2026-11-01 and 2026-11-30. | TRUE if the Met Office storm names page records a storm named by the UK, Ireland and Netherlands group with a naming date between 2026-11-01 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Likud wins more Knesset seats than any other list in the Israeli general election held on 2026-10-27." → REJECTED: cited items name Morocco; the claim is about Israel — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The French National Assembly adopts a motion of censure against the government between 2026-11-01 and 2026-12-31." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4940 issued all-time across 21 forecaster arms · 3588 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 267 issued · 256 open · 11 resolved · 5 hits / 6 misses · **Brier 0.362** against its own base rate 45.5% (climatological 0.248) · **skill -0.460** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1735 | 1352 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 110 | 109 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 115 | 115 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 114 | 107 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 249 | 162 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 437 | 356 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 267 | 256 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*