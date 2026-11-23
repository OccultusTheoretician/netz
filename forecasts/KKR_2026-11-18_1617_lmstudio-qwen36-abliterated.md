**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181617Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-18_1613.md · forecaster: lmstudio/qwen36-abliterated · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261118-17 | 90% | 2026-11-27 | political | Hakeem Jeffries is formally nominated as the House Speaker by the Senate between 2026-11-18 and 2026-11-25. | The Senate passes a resolution or the official record confirms the nomination of Hakeem Jeffries as Speaker within the window. |
| KKR-20261118-18 | 25% | 2026-11-27 | disaster | A magnitude 5.0 or greater earthquake occurs in Romania between 2026-11-18 and 2026-11-25. | The USGS catalog records an earthquake with magnitude 5.0 or higher in Romania between 2026-11-18 and 2026-11-25. |
| KKR-20261118-19 | 50% | 2026-11-27 | economics | Anthropic files its S-1 registration statement for its IPO between 2026-11-18 and 2026-11-25. | The SEC EDGAR database records an S-1 filing for Anthropic between 2026-11-18 and 2026-11-25. |
| KKR-20261118-20 | 40% | 2026-11-27 | military | Israel begins a ground operation in central Gaza between 2026-11-18 and 2026-11-25. | Two or more independent wire services report that Israeli forces have begun a ground operation in central Gaza within the window. |
| KKR-20261118-21 | 15% | 2026-11-27 | political | The ICJ issues a ruling on the Rohingya genocide case against Myanmar between 2026-11-18 and 2026-11-25. | The ICJ issues a ruling on the Rohingya genocide case against Myanmar within the window. |
| KKR-20261118-22 | 35% | 2026-11-27 | political | Jensen Huang appears before the Senate banking committee between 2026-11-18 and 2026-11-25. | The Senate banking committee records that Jensen Huang has appeared before the committee within the window. |
| KKR-20261118-23 | 20% | 2026-11-27 | disaster | A forest fire notification is recorded in Chad by GDACS between 2026-11-18 and 2026-11-25. | GDACS records a forest fire notification for Chad within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-18 and 2026-11-25 for CVE-2026-115731." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-115731 dateAdded 2026-11-17, before the claimed window 2026-11-18..2026-11-25; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The S&P 500 closes below 7,000 at least once between 2026-11-18 and 2026-11-25." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "The 10-year US Treasury yield closes above 5.25 percent at least once between 2026-11-18 and 2026-11-25." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5860 issued all-time across 23 forecaster arms · 4138 open (1972 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 241 issued · 239 open · 2 resolved · 2 hits / 0 misses · **Brier 0.381** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 241 | 224 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 241 | 239 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 225 | 192 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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