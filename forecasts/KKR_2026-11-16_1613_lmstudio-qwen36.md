**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 161613Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-16_1611.md · forecaster: lmstudio/qwen36 · 5 accepted / 5 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261116-01 | 15% | 2026-12-07 | economics | WTI Crude closes at or above 95.00 USD on any trading day between 2026-12-01 and 2026-12-04. | The closing price of WTI Crude on the NYMEX is 95.00 USD or higher on any trading day between 2026-12-01 and 2026-12-04. |
| KKR-20261116-02 | 30% | 2026-12-10 | political | The Federal Register publishes a final rule between 2026-12-01 and 2026-12-08 that explicitly restricts the export of AI chips to China. | The Federal Register publishes a final rule between 2026-12-01 and 2026-12-08 that explicitly restricts the export of AI chips to China. |
| KKR-20261116-03 | 25% | 2026-12-07 | economics | The Nasdaq Composite closes below 22,000 on any trading day between 2026-12-01 and 2026-12-04. | The Nasdaq Composite closes below 22,000 on any trading day between 2026-12-01 and 2026-12-04. |
| KKR-20261116-04 | 15% | 2027-02-10 | disaster | The USGS reports a magnitude 7.0 or higher earthquake with an epicenter located within 100 kilometers of Tokyo between 2027-02-01 and 2027-02-08. | The USGS Significant Earthquakes report lists an event with magnitude 7.0 or higher and an epicenter within 100 kilometers of Tokyo between 2027-02-01 and 2027-02-08. |
| KKR-20261116-05 | 15% | 2027-05-07 | economics | The Nasdaq Composite closes below 20,000 on any trading day between 2027-05-01 and 2027-05-04. | The Nasdaq Composite closes below 20,000 on any trading day between 2027-05-01 and 2027-05-04. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-16 and 2026-11-23 for a vulnerability with CVSS score 9.0 or higher." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The USGS reports a magnitude 6.0 or higher earthquake with an epicenter located within 50 kilometers of Tehran between 2026-12-15 and 2026-1" → REJECTED: cited items name Australia; the claim is about zone:iran — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A confirmed mass shooting in the United States between 2027-01-01 and 2027-01-08 results in five or more fatalities." → REJECTED: cited items name South Africa; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The House of Representatives passes a bill between 2027-03-01 and 2027-03-08 that explicitly repeals the CHIPS and Science Act." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A confirmed mass shooting in the United States between 2027-04-01 and 2027-04-08 results in five or more fatalities." → REJECTED: cited items name South Africa; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

5812 issued all-time across 23 forecaster arms · 4090 open (1734 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 226 issued · 209 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 226 | 209 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 224 | 222 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 209 | 176 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*