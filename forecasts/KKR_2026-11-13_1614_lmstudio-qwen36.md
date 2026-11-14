**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131614Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-13_1612.md · forecaster: lmstudio/qwen36 · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261113-01 | 35% | 2026-12-07 | economic | The S&P 500 index closes below 7,200 on any weekday between 2026-11-27 and 2026-12-04. | True if the S&P 500 closing price is below 7,200 on any trading day in the window. False if it stays above. |
| KKR-20261113-02 | 40% | 2026-12-07 | economic | The US Treasury yields above 5.30 percent on any weekday between 2026-11-27 and 2026-12-04. | True if the 10Y yield exceeds 5.30 percent on any trading day. False if it stays below. |
| KKR-20261113-03 | 30% | 2026-12-07 | cyber | A cyberattack on a US critical infrastructure provider is confirmed by CISA or a major wire service between 2026-11-27 and 2026-12-04. | True if a confirmed report of a cyberattack on critical infrastructure appears. False if no such report appears. |
| KKR-20261113-04 | 25% | 2026-12-07 | military_conflict | Netanyahu launches a military strike on Iran between 2026-11-27 and 2026-12-04. | True if two hostile sides confirm a strike. False if no strike occurs. |
| KKR-20261113-05 | 20% | 2026-12-07 | disaster | A major earthquake (Magnitude 6.0 or higher) occurs in a populated area between 2026-11-27 and 2026-12-04. | True if USGS reports a magnitude 6.0+ earthquake in a populated area. False if no such event occurs. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a zero-day vulnerability exploited in the wild between 2026-11-27 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Jensen Huang resigns as CEO of Nvidia between 2026-11-27 and 2026-12-04." → REJECTED: resolution offers alternative VENUES joined by 'or' (…press release | or | sec…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A major power grid failure causes an outage lasting more than 24 hours in a US metropolitan area between 2026-11-27 and 2026-12-04." → REJECTED: cited items name India, Nigeria, South Sudan, Sudan; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…utility | or | government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Russia launches a missile or drone attack on a Ukrainian city with more than 10 reported casualties between 2026-11-27 and 2026-12-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new US tariff on Chinese goods is announced by the Commerce Department between 2026-11-27 and 2026-12-04." → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal register notice | or | official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names only a venue or register (federal, register) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

5708 issued all-time across 23 forecaster arms · 3986 open (1674 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 212 issued · 195 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 198 | 198 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 212 | 195 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 212 | 210 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 189 | 156 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 388 | 374 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*