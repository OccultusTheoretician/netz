**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151614Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-15_1612.md · forecaster: lmstudio/qwen36-realist · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261115-07 | 35% | 2026-12-01 | military/conflict | A drone or missile attack strikes a US military base or facility in Bahrain between 2026-11-22 and 2026-11-29. | True if a third-party wire service reports a kinetic strike on a US facility in Bahrain within the window; False if no such strike is reported. |
| KKR-20261115-08 | 10% | 2026-12-01 | disaster | The Federal Aviation Administration issues a nationwide ground stop for US commercial flights between 2026-11-22 and 2026-11-29. | True if the FAA issues a nationwide ground stop within the window; False if no such stop is issued. |
| KKR-20261115-09 | 45% | 2026-11-30 | economics/markets | The S&P 500 index settles above 7,800.00 on at least one trading day between 2026-11-23 and 2026-11-27. | True if the settlement price exceeds 7,800.00 on any day in the window; False if it remains below that level throughout. Reference: 7,561.67 on the packet date. |
| KKR-20261115-10 | 25% | 2026-12-01 | disaster | A major power outage affecting over 100,000 customers occurs in the Philippines between 2026-11-22 and 2026-11-29. | True if a wire service reports a power outage of the specified scale in the window; False if no such outage is reported. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-22 and 2026-11-29 for a vulnerability exploited in the Cursor IDE or its Cla" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Brent crude oil settles below 90.00 USD per barrel on at least one trading day between 2026-11-23 and 2026-11-27." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The International Court of Justice issues a public order or judgment regarding the genocide case between The Gambia and Myanmar between 2026" → REJECTED: the resolution names a different subject than the statement — the claim is about Court, Gambia, International, Justice and the resolution settles on ICJ. A row whose resolution checks a different fact can be scored correct while being wrong
- "The USGS reports a magnitude 6.0 or greater earthquake in the Philippines between 2026-11-22 and 2026-11-29." → REJECTED: the resolution names only a venue or register (USGS) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The European Commission imposes a fine exceeding 500 million EUR on a US technology company between 2026-11-22 and 2026-12-15." → REJECTED: cited items name Italy; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names only a venue or register (ec) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A wildfire in Australia destroys more than 1,000 hectares of land between 2026-11-22 and 2026-11-29." → REJECTED: resolution offers alternative VENUES joined by 'or' (…gdacs | or | local authorities report a fire of the specif…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names only a venue or register (GDACS) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

5777 issued all-time across 23 forecaster arms · 4055 open (1723 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 209 issued · 176 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 214 | 214 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 221 | 204 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 220 | 218 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 209 | 176 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 397 | 383 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*