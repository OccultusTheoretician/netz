**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221634Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-22_1632.md · forecaster: lmstudio/qwen36 · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261122-01 | 30% | 2026-12-09 | military_conflict | A drone or missile attack kills at least one civilian in Gaza City between 2026-12-01 and 2026-12-07. | Two independent wire services (e.g., Reuters, AP) report a drone or missile attack in Gaza City between 2026-12-01 and 2026-12-07 resulting in at least one civilian death. |
| KKR-20261122-02 | 15% | 2026-12-24 | disaster | The USGS records an earthquake with magnitude 6.0 or greater in Peru between 2026-12-15 and 2026-12-22. | The USGS Significant Quakes catalog lists an event with magnitude 6.0 or greater in Peru with a date between 2026-12-15 and 2026-12-22. |
| KKR-20261122-03 | 10% | 2026-12-09 | political | The UN Security Council passes a resolution condemning Iran's missile attacks between 2026-12-01 and 2026-12-07. | The UN Security Council passes a resolution condemning Iran's missile attacks between 2026-12-01 and 2026-12-07. |
| KKR-20261122-04 | 10% | 2026-12-19 | disaster | A wildfire in Australia causes at least one fatality between 2026-12-10 and 2026-12-17. | A major wire service reports a wildfire in Australia between 2026-12-10 and 2026-12-17 causing at least one fatality. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-11-29 and 2026-12-02 for a vulnerability matching the description in item 22 (M" → REJECTED: the resolution names only a venue or register (CISA, KEV, cve) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI Crude futures settle above 85.00 USD per barrel on the last trading day of 2026 (2026-12-31)." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The South Korean government formally announces the resignation of the Minister of Education between 2026-12-01 and 2026-12-07." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The Nasdaq Composite Index closes below 20,000 for the first time since the market snapshot in item 5." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major US bank (e.g., JPMorgan Chase, Bank of America) reports a quarterly net loss attributable to cyber incidents between 2027-01-25 and " → REJECTED: the resolution names a different subject than the statement — the claim is about America, Bank, Chase, JPMorgan and the resolution settles on SEC. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Federal Reserve announces a 50 basis point interest rate cut between 2026-12-15 and 2026-12-22." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5912 issued all-time across 23 forecaster arms · 4190 open (2129 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 261 issued · 244 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 261 | 244 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 257 | 255 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 241 | 208 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
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