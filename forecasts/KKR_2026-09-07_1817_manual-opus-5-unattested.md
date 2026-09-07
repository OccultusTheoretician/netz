**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071817Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-34 | 32% | 2026-12-02 | economics/markets | ICE Brent front-month futures settle at or above 110.00 US dollars per barrel on at least one trading day between 2026-09-14 and 2026-11-27. Reference: 96.28 on the packet date, 2026-09-07. | TRUE if ICE publishes a front-month Brent settlement price greater than or equal to 110.00 for any trading day between 2026-09-14 and 2026-11-27 inclusive. Intraday highs do not count; settlement prices only. Reference level at seal: 96.28. |
| KKR-20260907-35 | 70% | 2026-11-03 | cyber | The CISA KEV catalog adds at least one vulnerability with vendorProject N-able, carrying a dateAdded value between 2026-09-08 and 2026-10-30. | TRUE if the CISA Known Exploited Vulnerabilities JSON feed contains an entry whose vendorProject field reads N-able and whose dateAdded falls between 2026-09-08 and 2026-10-30 inclusive. Entries carrying an earlier dateAdded do not count. |
| KKR-20260907-36 | 25% | 2026-12-08 | cyber | The CISA KEV catalog adds at least one vulnerability with vendorProject MikroTik, carrying a dateAdded value between 2026-09-08 and 2026-12-04. | TRUE if the CISA Known Exploited Vulnerabilities JSON feed contains an entry whose vendorProject field reads MikroTik and whose dateAdded falls between 2026-09-08 and 2026-12-04 inclusive. Pre-existing MikroTik entries do not count. |
| KKR-20260907-37 | 55% | 2026-11-04 | military/conflict | A commercial vessel is struck by weapons fire, forcibly boarded, or seized in the Strait of Hormuz or the Gulf of Oman between 2026-09-14 and 2026-10-31. | TRUE if two or more of Reuters, AP, and Bloomberg report a commercial vessel hit by weapons fire, forcibly boarded, or seized in the Strait of Hormuz or Gulf of Oman, dated inside the window. |
| KKR-20260907-38 | 45% | 2026-10-16 | military/conflict | Israeli strikes in Lebanon kill at least 25 people within a single 24-hour period between 2026-09-14 and 2026-10-12. | TRUE if two or more of Reuters, AFP, and AP carry a Lebanese Health Ministry figure of 25 or more killed by Israeli strikes in Lebanon over one 24-hour period inside the window. |
| KKR-20260907-39 | 15% | 2026-12-23 | political | The Landtag of Saxony-Anhalt elects an AfD member as Minister-President between 2026-09-14 and 2026-12-18. | TRUE if the official plenary record of the Landtag of Sachsen-Anhalt shows a Minister-President elected inside the window who holds AfD membership at the vote. A caretaker incumbent continuing in office resolves FALSE. |
| KKR-20260907-40 | 38% | 2026-10-27 | disaster | Nepal's official confirmed flood death toll reaches 1,500 or higher between 2026-09-14 and 2026-10-23. | TRUE if Nepal's National Disaster Risk Reduction and Management Authority publishes a confirmed cumulative 2026 flood death toll of 1,500 or more, dated inside the window. Missing-persons counts are excluded. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FRED series DGS10 records a daily value at or above 5.00 percent on at least one business day between 2026-09-14 and 2026-12-18. Referen" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Russian and Ukrainian government delegations hold an in-person bilateral meeting between 2026-09-14 and 2026-12-15." → REJECTED: the resolution names only a venue or register (AFP, AP, Reuters, third) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "At least one defendant is convicted at the Paris assize trial over the killing of Federico Aramburu between 2026-09-08 and 2026-11-30." → REJECTED: the resolution names a different subject than the statement — the claim is about Aramburu, Federico, Paris and the resolution settles on AFP, Acquittal, Monde, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1650 issued all-time across 16 forecaster arms · 1385 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 199 issued · 193 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 484 | 456 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 187 | 166 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*