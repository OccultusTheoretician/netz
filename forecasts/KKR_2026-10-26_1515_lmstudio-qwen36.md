**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 261515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-26_1513.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261026-01 | 85% | 2026-11-05 | economics/markets | Anthropic files a registration statement on SEC Form S-1 with the US Securities and Exchange Commission between 2026-10-27 and 2026-11-03. | The SEC EDGAR database contains a Form S-1 filed by Anthropic with a filing date between 2026-10-27 and 2026-11-03. |
| KKR-20261026-02 | 15% | 2026-11-10 | disaster | A magnitude 6.0 or greater earthquake occurs in the Bonin Islands, Japan region between 2026-11-01 and 2026-11-08. | The USGS Significant Earthquakes catalog records an event with magnitude 6.0 or greater in the Bonin Islands, Japan region with an origin time between 2026-11-01 and 2026-11-08. |
| KKR-20261026-03 | 10% | 2026-11-10 | political | The US Department of Justice files a civil lawsuit against the state of Alaska regarding election administration between 2026-11-01 and 2026-11-08. | The PACER court docket for the District of Columbia contains a civil complaint filed by the US Department of Justice against the state of Alaska with a filing date between 2026-11-01 and 2026-11-08. |
| KKR-20261026-04 | 15% | 2026-11-10 | cyber | A major cyberattack disrupts the power grid in Sudan between 2026-11-01 and 2026-11-08. | Two wire services (Al Jazeera and BBC World) report a cyberattack causing power grid disruption in Sudan with an event date between 2026-11-01 and 2026-11-08. |
| KKR-20261026-05 | 35% | 2026-11-10 | economics/markets | The Federal Reserve announces a 25 basis point interest rate cut at its meeting between 2026-11-01 and 2026-11-08. | The Federal Reserve releases a statement announcing a 25 basis point interest rate cut with a release date between 2026-11-01 and 2026-11-08. |
| KKR-20261026-06 | 20% | 2026-11-10 | disaster | A tropical cyclone makes landfall in Queensland, Australia between 2026-11-01 and 2026-11-08. | The Australian Bureau of Meteorology issues a Tropical Cyclone Warning for landfall in Queensland with an issue date between 2026-11-01 and 2026-11-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes above 7,800.00 on any trading day between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new vulnerability is added to the CISA Known Exploited Vulnerabilities (KEV) catalog with a date-added value between 2026-10-27 and 2026-1" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Saudi Arabia launches a kinetic strike on Houthi missile facilities in Yemen between 2026-11-01 and 2026-11-08." → REJECTED: cited items name Saudi Arabia; the claim is about Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The European Union imposes new sanctions on Russian entities in response to the Ukraine conflict between 2026-11-01 and 2026-11-08." → REJECTED: cited items name Iran, Islamic Republic of; the claim is about Russian Federation, Ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4970 issued all-time across 21 forecaster arms · 3618 open (709 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 116 issued · 115 open · 1 resolved · 1 hits / 0 misses · **Brier 0.722** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1751 | 1368 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 116 | 115 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
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
| manual/sonnet-5.5/unattested | 222 | 219 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*