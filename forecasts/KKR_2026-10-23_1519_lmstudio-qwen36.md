**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231519Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: lmstudio/qwen36 · 9 accepted / 1 rejected by validation gate · 9 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-58 | 25% | 2026-11-10 | disaster | The USGS catalog records an earthquake with magnitude 6.0 or greater in the Tibet region between 2026-11-01 and 2026-11-07. | The USGS earthquake catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a magnitude 6.0+ event in the Tibet region. |
| KKR-20261023-59 | 30% | 2026-11-10 | cyber | The CISA KEV catalog adds a new entry for an actively exploited zero-day vulnerability affecting Arista Networks VeloCloud software between 2026-11-01 and 2026-11-07. | The CISA KEV catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a vulnerability affecting Arista VeloCloud. |
| KKR-20261023-60 | 15% | 2026-11-10 | disaster | The USGS catalog records a magnitude 7.0 or greater earthquake anywhere in the world between 2026-11-01 and 2026-11-07. | The USGS earthquake catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a magnitude 7.0+ event. |
| KKR-20261023-61 | 20% | 2026-11-10 | disaster | The USGS catalog records a magnitude 6.0 or greater earthquake in the Indonesia region between 2026-11-01 and 2026-11-07. | The USGS earthquake catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a magnitude 6.0+ event in the Indonesia region. |
| KKR-20261023-62 | 25% | 2026-11-10 | cyber | The CISA KEV catalog adds a new entry for an actively exploited zero-day vulnerability affecting HPE software between 2026-11-01 and 2026-11-07. | The CISA KEV catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a vulnerability affecting HPE software. |
| KKR-20261023-63 | 20% | 2026-11-10 | disaster | The USGS catalog records a magnitude 6.0 or greater earthquake in the Italy region between 2026-11-01 and 2026-11-07. | The USGS earthquake catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a magnitude 6.0+ event in the Italy region. |
| KKR-20261023-64 | 10% | 2026-11-10 | political | The Federal Register publishes a final rule or executive order formally ending the Denmark ban on mink farming in Denmark between 2026-11-01 and 2026-11-07. | The Federal Register carries a publication date between 2026-11-01 and 2026-11-07 for a final rule or executive order ending the Denmark mink farming ban. |
| KKR-20261023-65 | 20% | 2026-11-10 | disaster | The USGS catalog records a magnitude 6.0 or greater earthquake in the China region between 2026-11-01 and 2026-11-07. | The USGS earthquake catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a magnitude 6.0+ event in the China region. |
| KKR-20261023-66 | 25% | 2026-11-10 | cyber | The CISA KEV catalog adds a new entry for an actively exploited zero-day vulnerability affecting PHP between 2026-11-01 and 2026-11-07. | The CISA KEV catalog carries a date-added value between 2026-11-01 and 2026-11-07 for a vulnerability affecting PHP. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Register publishes a final rule or executive order formally ending the US ban on mink farming in the United States between 2026-" → REJECTED: cited items name Denmark; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4778 issued all-time across 21 forecaster arms · 3426 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 104 issued · 103 open · 1 resolved · 1 hits / 0 misses · **Brier 0.722** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1679 | 1296 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 104 | 103 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 242 | 155 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*