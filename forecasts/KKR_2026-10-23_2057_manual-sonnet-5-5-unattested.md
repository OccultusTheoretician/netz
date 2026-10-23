**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232057Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: manual/sonnet-5.5/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-107 | 60% | 2026-10-30 | political | Flavio Bolsonaro receives more valid votes than Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25. | The Superior Electoral Court (TSE) tally for the 2026-10-25 runoff, read on 2026-10-30, shows Flavio Bolsonaro with more valid votes than Lula; a Lula lead or tie resolves false. |
| KKR-20261023-108 | 40% | 2026-12-04 | military/conflict | Official delegations of both Russia and Ukraine attend a meeting held in the United Arab Emirates on a date between 2026-11-01 and 2026-11-30, whether direct or US-mediated. | At least two of Reuters, AP, and AFP report that Russian and Ukrainian official delegations met in the UAE on a date between 2026-11-01 and 2026-11-30; announced or postponed meetings do not count. |
| KKR-20261023-109 | 46% | 2026-11-25 | military/conflict | US forces strike a target inside Iran, on land or in territorial waters, on a date between 2026-10-26 and 2026-11-22, as confirmed by US Central Command or the White House. | A US Central Command release or White House statement confirms US strikes on targets inside Iran dated between 2026-10-26 and 2026-11-22, and Reuters or AP carries the confirmation. |
| KKR-20261023-110 | 24% | 2026-11-24 | economics/markets | The ICE Brent front-month futures settlement price on 2026-11-20 is below 100.00 USD per barrel. Reference: 111.27 USD per barrel on the packet date, per the packet market snapshot. | The ICE Brent front-month settlement price for 2026-11-20 is below 100.00 USD per barrel; 100.00 or higher resolves false. Reference level 111.27 on the packet date. |
| KKR-20261023-111 | 66% | 2026-11-10 | cyber | The CISA KEV catalog adds CVE-2026-114625, the Arista VeloCloud Orchestrator SQL injection flaw, with a date-added value between 2026-10-23 and 2026-11-06. | The CISA KEV catalog JSON lists CVE-2026-114625 with a dateAdded value between 2026-10-23 and 2026-11-06 inclusive, as read on the deadline. |
| KKR-20261023-112 | 58% | 2026-11-17 | cyber | The CISA KEV catalog adds CVE-2026-109618 or CVE-2026-109619, the PHP2Shell flaws in PHP core, with a date-added value between 2026-10-23 and 2026-11-13. | The CISA KEV catalog JSON lists CVE-2026-109618 or CVE-2026-109619 with a dateAdded value between 2026-10-23 and 2026-11-13 inclusive, as read on the deadline. |
| KKR-20261023-113 | 22% | 2026-11-13 | disaster | USGS lists an earthquake of magnitude 5.5 or greater, with origin time between 2026-10-26 and 2026-11-08, located within 250 km of the epicenter of USGS event us6000u43g. | The USGS ComCat catalog, queried on the deadline, contains an event of magnitude 5.5 or greater with origin time between 2026-10-26 and 2026-11-08 within 250 km of the us6000u43g epicenter. |
| KKR-20261023-114 | 50% | 2026-11-18 | disaster | At least one additional person in Nigeria is laboratory-confirmed with Ebola, beyond any case confirmed on or before 2026-10-23, with confirmation dated between 2026-10-24 and 2026-11-13. | WHO or the Nigeria Centre for Disease Control and Prevention reports a laboratory-confirmed Ebola case in Nigeria, other than cases confirmed by 2026-10-23, with confirmation dated between 2026-10-24 and 2026-11-13. |
| KKR-20261023-115 | 5% | 2026-12-04 | crime/security | France declares a state of emergency covering all or part of metropolitan France, by decree dated between 2026-10-26 and 2026-11-30. | Legifrance or the Journal Officiel publishes a decree declaring a state of emergency applicable to all or part of metropolitan France, dated between 2026-10-26 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Student List receives more national votes than the SNS-led list headed by Aleksandar Vucic in the Serbian parliamentary election held on" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4827 issued all-time across 21 forecaster arms · 3475 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 205 issued · 202 open · 3 resolved · 3 hits / 0 misses · **Brier 0.009** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1692 | 1309 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 104 | 103 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 105 | 105 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 113 | 106 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 242 | 155 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 420 | 339 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 251 | 240 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 205 | 202 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*