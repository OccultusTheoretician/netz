**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-09 | 25% | 2026-10-17 | cyber | On 2026-10-15, the CISA KEV catalog will include at least one new entry for a vulnerability with CVSS score 10.0 or higher that was actively exploited in the wild between 2026-10-08 and 2026-10-14. | The CISA KEV catalog carries a date-added value between 2026-10-08 and 2026-10-14 for a vulnerability with CVSS score 10.0 or higher that was actively exploited in the wild during that window. |
| KKR-20261008-10 | 30% | 2026-10-18 | military/conflict | Between 2026-10-08 and 2026-10-14, at least one drone strike reported in the Russia-Ukraine Theatre will result in confirmed casualties, defined as at least one death or serious injury, as verified by two independent sources from different hostile sides. | At least one report from two distinct hostile sides (RU, UA, AXIS) confirms a drone strike in the Russia-Ukraine Theatre between 2026-10-08 and 2026-10-14 that resulted in at least one confirmed death or serious injury. |
| KKR-20261008-11 | 15% | 2026-10-18 | disaster | Between 2026-10-08 and 2026-10-14, at least one major earthquake of magnitude 6.0 or higher will be recorded by the USGS and confirmed by at least two independent seismic monitoring agencies. | The USGS Significant Quakes feed reports a magnitude 6.0 or higher earthquake between 2026-10-08 and 2026-10-14, and at least two independent seismic monitoring agencies (e.g., EMSC, GFZ) confirm the event. |
| KKR-20261008-12 | 25% | 2026-10-20 | political | On 2026-10-17, the UK government will announce a new sanctions regime targeting Russian energy exports, with the policy published in the UK Government's official register. | The UK Government's official register (https://www.legislation.gov.uk) contains a new sanctions order targeting Russian energy exports, published on or before 2026-10-17. |
| KKR-20261008-13 | 40% | 2026-10-19 | economics/markets | On 2026-10-15, the Brent crude oil price will exceed $110 per barrel, based on the closing price from the ICE Futures Europe exchange. | The Brent crude oil price, as reported by ICE Futures Europe on the settlement date, is greater than $110 per barrel. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On or before 2026-10-15, the 10-year U.S. Treasury yield will exceed 5.50 percent, based on the closing yield on the U.S. Department of the " → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-08 and 2026-10-14, at least one cyberattack targeting a U.S. financial institution will be publicly attributed to a state ac" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "On 2026-10-16, the S&P 500 will close below 7,700 points, based on the official closing price from the New York Stock Exchange." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-10-08 and 2026-10-14, at least one confirmed cyberattack using a zero-day exploit against a critical infrastructure system (e.g" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-08 and 2026-10-14, at least one missile strike reported in the Israel-Gaza-Levant Theatre will be confirmed by two hostile s" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3625 issued all-time across 21 forecaster arms · 2811 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 197 issued · 162 open · 34 resolved · 26 hits / 8 misses · **Brier 0.383** against its own base rate 76.5% (climatological 0.180) · **skill -1.128**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1292 | 1091 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*