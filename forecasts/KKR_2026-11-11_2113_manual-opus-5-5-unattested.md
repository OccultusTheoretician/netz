**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112113Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-11_1613.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261111-30 | 75% | 2026-12-11 | cyber | The CISA KEV catalog adds at least one Microsoft CVE with a dateAdded value of 2026-12-08, the scheduled December 2026 Patch Tuesday. | The CISA KEV JSON feed contains at least one entry whose vendorProject is Microsoft and whose dateAdded equals 2026-12-08. |
| KKR-20261111-31 | 45% | 2026-12-08 | cyber | The CISA KEV catalog adds an N-able entry with a dateAdded value between 2026-11-11 and 2026-12-04, following the N-able zero-day hotfixes. | The CISA KEV JSON feed contains an entry whose vendorProject is N-able and whose dateAdded falls between 2026-11-11 and 2026-12-04 inclusive. |
| KKR-20261111-32 | 45% | 2027-01-05 | economics/markets | The US Treasury 10-year par yield for 2026-12-31 is at or above 5.00 percent. Reference: 5.00 percent per the packet snapshot on 2026-11-11. | The Treasury Daily Par Yield Curve Rates table shows a 10 Yr value of 5.00 or higher for the row dated 2026-12-31. Reference level 5.00 on 2026-11-11. |
| KKR-20261111-33 | 65% | 2026-12-11 | economics/markets | The FOMC statement from the December 2026 meeting, scheduled for 2026-12-09, announces a federal funds target range identical to the range in effect immediately before that meeting. | The Federal Reserve press release for the December 2026 FOMC meeting states a target range equal to the range in force on 2026-12-08. |
| KKR-20261111-34 | 30% | 2026-12-22 | economics/markets | ICE Brent front-month crude settles above 100.00 dollars per barrel on at least one trading day between 2026-11-12 and 2026-12-18. Reference: 93.87 on the packet date 2026-11-11. | ICE Futures Europe daily settlement data show a Brent front-month settlement above 100.00 on any trading day from 2026-11-12 to 2026-12-18 inclusive. Reference 93.87 on 2026-11-11. |
| KKR-20261111-35 | 60% | 2026-12-18 | military/conflict | Russia and Ukraine carry out a prisoner exchange of at least 300 persons per side between 2026-11-12 and 2026-12-15, confirmed by both the Russian Ministry of Defence and the Ukrainian Coordination Headquarters. | Official statements from both the Russian Ministry of Defence and the Ukrainian Coordination Headquarters confirm a single exchange of 300 or more persons per side completed between 2026-11-12 and 2026-12-15. |
| KKR-20261111-36 | 35% | 2026-12-15 | military/conflict | Iranian forces board or seize a commercial tanker in the Persian Gulf, Strait of Hormuz, or Gulf of Oman between 2026-11-12 and 2026-12-11, confirmed by a UKMTO advisory and the vessel operator or flag state. | A UKMTO advisory plus a statement from the tanker operator or flag state both attribute a boarding or seizure of a named commercial tanker to Iranian forces, event dated 2026-11-12 to 2026-12-11. |
| KKR-20261111-37 | 30% | 2026-12-15 | crime/security | Italian authorities announce the arrest of at least one named or identified suspect for the November 2026 email bomb threats against Italian schools between 2026-11-12 and 2026-12-11. | An Italian police, Carabinieri, or prosecutor statement announces an arrest tied to the school email bomb threats, dated 2026-11-12 to 2026-12-11, reported by ANSA and one non-Italian wire service. |
| KKR-20261111-38 | 30% | 2027-01-05 | disaster | GDACS issues an Orange or Red flood alert for Kenya with an event start date between 2026-11-12 and 2026-12-31. | The GDACS event list contains a flood event with country Kenya, alert level Orange or Red, and a start date between 2026-11-12 and 2026-12-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Mississippi Secretary of State publishes certified 2026 general election results on or before 2026-12-18 showing Scott Colom with more v" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5631 issued all-time across 23 forecaster arms · 3909 open (1598 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 381 issued · 367 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 165 | 165 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 201 | 184 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 209 | 207 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 183 | 150 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 526 | 411 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 8 | 8 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 381 | 367 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*