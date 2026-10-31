**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 311522Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-31_1513.md · forecaster: control/trailing · 8 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261031-15 | 57% | 2027-01-04 | cyber | CISA adds at least one Ivanti Connect Secure CVE, other than CVE-2026-118527 and CVE-2026-111357, to the KEV catalog between 2026-10-31 and 2026-12-31, consistent with the reported three-flaw exploit chain. | CISA KEV catalog carries an Ivanti Connect Secure entry, excluding CVE-2026-118527 and CVE-2026-111357, with dateAdded between 2026-10-31 and 2026-12-31 inclusive. |
| KKR-20261031-16 | 57% | 2026-12-15 | political | Democratic candidates win at least 218 US House seats in the general election held on 2026-11-03. | AP race calls, as published by the deadline, credit Democratic candidates with 218 or more House seats from the 2026-11-03 general election. |
| KKR-20261031-17 | 57% | 2026-12-15 | political | Democrats and Democratic-caucusing independents win at least 51 US Senate seats as a result of the general election held on 2026-11-03. | AP race calls by the deadline produce a Senate composition for the next Congress with 51 or more Democrats plus Democratic-caucusing independents. |
| KKR-20261031-18 | 57% | 2027-01-05 | economics/markets | WTI crude spot price on 2026-12-31 is below 100.00 USD per barrel. Reference: 104.12 USD on the packet date 2026-10-31. | FRED series DCOILWTICO value for 2026-12-31 is below 100.00. Reference: 104.12 on 2026-10-31. |
| KKR-20261031-19 | 57% | 2027-01-05 | economics/markets | The US 10-year Treasury constant maturity yield on 2026-12-31 is above 5.00 percent. Reference: 4.93 percent on the packet date 2026-10-31. | FRED series DGS10 value for 2026-12-31 exceeds 5.00. Reference: 4.93 percent on 2026-10-31. |
| KKR-20261031-20 | 57% | 2027-04-05 | political | Iran formally submits notice of withdrawal from the NPT under Article X between 2026-11-01 and 2027-03-31. | The UN Security Council or depositary governments receive a formal Iranian Article X withdrawal notice dated between 2026-11-01 and 2027-03-31, per UN records or Reuters/AP. |
| KKR-20261031-21 | 57% | 2027-01-05 | military/conflict | Iranian forces seize or detain a commercial tanker in the Strait of Hormuz or Gulf of Oman between 2026-11-01 and 2026-12-31. | Reuters and AP each report Iranian forces (IRGC or navy) seized or detained a commercial tanker in the Strait of Hormuz or Gulf of Oman between 2026-11-01 and 2026-12-31. |
| KKR-20261031-22 | 57% | 2027-04-20 | disaster | WHO declares the Ebola outbreak in the Democratic Republic of the Congo over between 2026-11-01 and 2027-04-15. | WHO Disease Outbreak News or an official WHO statement declares the end of the current DRC Ebola outbreak, with the declaration dated between 2026-11-01 and 2027-04-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5212 issued all-time across 22 forecaster arms · 3490 open (712 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 44 issued · 44 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 44 | 44 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 145 | 128 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 144 | 142 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 136 | 103 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 312 | 298 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*