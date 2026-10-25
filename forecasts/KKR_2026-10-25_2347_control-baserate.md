**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 252347Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-25_1513.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261025-19 | 60% | 2026-12-01 | economics/markets | The EIA daily WTI Cushing spot price, FRED series DCOILWTICO, records at least one observation at or above 110.00 USD per barrel dated between 2026-10-26 and 2026-11-20 inclusive. Reference: 103.27 on the packet date. | True if FRED series DCOILWTICO, fetched on the deadline, shows any observation dated 2026-10-26 through 2026-11-20 inclusive with value 110.00 or higher; otherwise false. Reference: 103.27 on the packet date. |
| KKR-20261025-20 | 60% | 2026-11-24 | economics/markets | The S&P 500 index records at least one official daily close at or below 7200.00 dated between 2026-10-26 and 2026-11-20 inclusive. Reference: 7623.68 on the packet date. | True if FRED series SP500, the S&P Dow Jones Indices official close, shows any observation dated 2026-10-26 through 2026-11-20 inclusive at or below 7200.00; otherwise false. Reference: 7623.68 on the packet date. |
| KKR-20261025-21 | 66% | 2026-12-04 | military/conflict | Between 2026-10-25 and 2026-11-30 inclusive, United States forces strike a target inside the internationally recognized territory or territorial waters of Iran, and the White House, Department of Defense, or CENTCOM publicly acknowledges the strike as a US action. | True if a White House, Department of Defense, or CENTCOM statement acknowledges a US strike on a target inside Iranian territory or territorial waters conducted 2026-10-25 through 2026-11-30 inclusive; otherwise false. |
| KKR-20261025-22 | 66% | 2026-12-18 | military/conflict | Between 2026-10-25 and 2026-12-15 inclusive, Algerian military personnel enter Niger under the deployment approved by the Algerian parliament, as announced by the Algerian Ministry of National Defence or the state agency APS. | True if the Algerian Ministry of National Defence or APS announces Algerian troops entered Niger on a date 2026-10-25 through 2026-12-15 inclusive, and Reuters, AFP, or AP reports the announcement; otherwise false. |
| KKR-20261025-23 | 42% | 2026-12-01 | political | In the scheduled 2026-11-03 United States general election, Democratic candidates win at least 218 of the 435 seats in the House of Representatives, per Associated Press race calls. | True if Associated Press race calls, as of the deadline, show Democratic candidates winning at least 218 House seats in the 2026-11-03 election; otherwise false. |
| KKR-20261025-24 | 42% | 2026-12-02 | disaster | Between 2026-10-26 and 2026-11-30 inclusive, the UK Met Office names, or adopts from a partner meteorological service, at least one new storm other than Boelo. | True if the UK Met Office storm centre page or a Met Office news release records a storm other than Boelo named on a date 2026-10-26 through 2026-11-30 inclusive; otherwise false. |
| KKR-20261025-25 | 42% | 2027-01-05 | disaster | Between 2026-10-26 and 2026-12-31 inclusive, the WHO Director-General declares the Ebola outbreak linked to Uganda, Kenya, and Nigeria a Public Health Emergency of International Concern. | True if WHO publishes a Director-General statement declaring this Ebola outbreak a Public Health Emergency of International Concern, dated 2026-10-26 through 2026-12-31 inclusive; otherwise false. |
| KKR-20261025-26 | 36% | 2026-11-25 | crime/security | Between 2026-10-25 and 2026-11-22 inclusive, Queensland Police Service publicly announces that at least one person has been charged over the Loganholme drive-by shooting reported on 2026-10-25. | True if a Queensland Police Service media release or Queensland court listing records at least one person charged over the Loganholme shooting, with the charge announced 2026-10-25 through 2026-11-22 inclusive; otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-26 and 2026-12-20 inclusive, the French National Assembly adopts a motion of censure with at least 289 votes in favor, bring" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "In the scheduled 2026-10-25 Brazilian presidential runoff, Luiz Inacio Lula da Silva receives more valid votes than Flavio Bolsonaro in the " → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4932 issued all-time across 21 forecaster arms · 3580 open (696 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1735 issued · 1352 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

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
| manual/opus-5.5/unattested | 259 | 248 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 214 | 211 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*