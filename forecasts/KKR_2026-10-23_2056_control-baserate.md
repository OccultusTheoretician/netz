**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232056Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-88 | 66% | 2026-12-03 | military/conflict | Government-designated Russian and Ukrainian delegations take part in the same negotiating session in the United Arab Emirates on at least one day between 2026-11-01 and 2026-11-30. | TRUE if two of Reuters, AP, AFP, BBC report government-designated Russian and Ukrainian delegations took part in the same talks session in the UAE on a date between 2026-11-01 and 2026-11-30; a prisoner exchange alone does not count. |
| KKR-20261023-89 | 66% | 2026-12-03 | military/conflict | Between 2026-10-24 and 2026-11-30, the United States and Iran each publicly confirm an agreed ceasefire or truce between the two countries, of any stated duration. | TRUE if, between 2026-10-24 and 2026-11-30, the White House, State Department or Pentagon and the Iranian government or foreign ministry each publicly confirm an agreed US-Iran ceasefire or truce, as reported by at least two of Reuters, AP, AFP. |
| KKR-20261023-90 | 66% | 2026-11-24 | military/conflict | US forces conduct at least one strike on a target on Iranian land territory between 2026-10-24 and 2026-11-20 that US Central Command, the Pentagon or the White House publicly acknowledges. | TRUE if US Central Command, the Pentagon or the White House publicly acknowledges a US strike on a target on Iranian land territory that occurred between 2026-10-24 and 2026-11-20, as reported by Reuters or AP. |
| KKR-20261023-91 | 60% | 2026-11-24 | economics/markets | The ICE front-month Brent crude futures contract settles at or above 125.00 US dollars per barrel on at least one trading day between 2026-10-26 and 2026-11-20. Reference: Brent 111.27 on the packet date. | TRUE if the ICE Futures Europe daily settlement price of the front-month Brent crude futures contract is 125.00 US dollars or higher on at least one trading day between 2026-10-26 and 2026-11-20 inclusive. Reference: 111.27 on 2026-10-23. |
| KKR-20261023-92 | 42% | 2026-11-20 | political | James Talarico wins the 2026-11-03 US Senate general election in Texas, as called by the Associated Press. | TRUE if the Associated Press has called the 2026-11-03 Texas US Senate general election for James Talarico by the deadline; FALSE if AP has called it for another candidate or has not called it by the deadline. |
| KKR-20261023-93 | 36% | 2026-11-10 | crime/security | At least one suspect in the 2026-10-23 gun attack on a church funeral in Karak governorate, Jordan, is arrested or killed between 2026-10-23 and 2026-11-06, as announced by Jordanian authorities. | TRUE if the Public Security Directorate, interior ministry or government spokesperson of Jordan announces, and Reuters, AP or AFP reports, that at least one suspect in the 2026-10-23 Karak church attack was arrested or killed between 2026-10-23 and 2026-11-06. |
| KKR-20261023-94 | 42% | 2026-11-10 | disaster | The USGS catalog records at least one earthquake of magnitude 6.0 or greater with epicenter within 100 km of USGS event us6000u43g (M7.0 near Nagqu, China) and origin time between 2026-10-24 and 2026-11-06 UTC. | TRUE if a USGS ComCat search on or after the deadline returns at least one event with magnitude 6.0 or greater, origin time from 2026-10-24 00:00 to 2026-11-06 23:59 UTC, and epicenter within 100 km of event us6000u43g. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog lists CVE-2026-114625, the Arista VeloCloud Orchestrator SQL injection zero-day, with a dat" → REJECTED: event window opens 2026-10-22, before this row is sealed (2026-10-23, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The CISA Known Exploited Vulnerabilities catalog lists CVE-2026-109618 or CVE-2026-109619, the PHP2Shell flaws, with a dateAdded between 202" → REJECTED: event window opens 2026-10-21, before this row is sealed (2026-10-23, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Flavio Bolsonaro receives more valid votes than Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25, per the o" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4806 issued all-time across 21 forecaster arms · 3454 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1686 issued · 1303 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1686 | 1303 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
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
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*