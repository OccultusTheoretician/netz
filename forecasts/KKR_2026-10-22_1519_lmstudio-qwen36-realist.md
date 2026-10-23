**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: lmstudio/qwen36-realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261022-10 | 65% | 2026-11-02 | cyber | The CISA KEV catalog carries a date-added value for a critical PHP web vulnerability between 2026-10-22 and 2026-10-29. | The CISA KEV catalog lists the vulnerability with a date-added value within the window. |
| KKR-20261022-11 | 40% | 2026-11-06 | economics | WTI Crude closes below 95.00 USD per barrel on 2026-11-05. | WTI Crude settlement price on 2026-11-05 is less than 95.00 USD. |
| KKR-20261022-12 | 30% | 2026-11-02 | military_conflict | A Houthi attack on a commercial shipping vessel in the Red Sea or Gulf of Aden results in at least one fatality between 2026-10-22 and 2026-10-29. | Two independent wire services report a Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden with at least one fatality. |
| KKR-20261022-13 | 25% | 2026-11-02 | disaster | The USGS records a magnitude 6.0 or greater earthquake in China between 2026-10-22 and 2026-10-29. | The USGS earthquake catalog lists an event with magnitude 6.0 or greater in China within the window. |
| KKR-20261022-14 | 15% | 2026-11-02 | disaster | The USGS records a magnitude 7.0 or greater earthquake anywhere in the world between 2026-10-22 and 2026-10-29. | The USGS earthquake catalog lists an event with magnitude 7.0 or greater within the window. |
| KKR-20261022-15 | 30% | 2026-11-09 | military_conflict | A Houthi attack on a commercial shipping vessel in the Red Sea or Gulf of Aden results in at least one fatality between 2026-10-29 and 2026-11-05. | Two independent wire services report a Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden with at least one fatality. |
| KKR-20261022-16 | 25% | 2026-11-09 | disaster | The USGS records a magnitude 6.0 or greater earthquake in China between 2026-10-29 and 2026-11-05. | The USGS earthquake catalog lists an event with magnitude 6.0 or greater in China within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes above 7,800.00 on 2026-11-12." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A Russian missile strike hits a populated area in Kyiv between 2026-10-22 and 2026-10-29." → REJECTED: cited items name France; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The 10-Year US Treasury Yield closes above 5.20 percent on 2026-11-12." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4706 issued all-time across 21 forecaster arms · 3354 open (585 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 107 issued · 100 open · 7 resolved · 3 hits / 4 misses · **Brier 0.297** against its own base rate 42.9% (climatological 0.245) · **skill -0.215** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1657 | 1274 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 457 | 216 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*