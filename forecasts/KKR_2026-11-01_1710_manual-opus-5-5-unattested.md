**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011710Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-01_1612.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261101-13 | 50% | 2026-12-03 | crime/security | Between 2026-11-02 and 2026-11-30, Birmingham, Alabama police announce an arrest or criminal charge in the 2026-11-01 fatal shooting outside the Magic City Classic football game. | TRUE if Birmingham police or Jefferson County prosecutors announce, or two established news outlets report, an arrest or charge in this shooting dated between 2026-11-02 and 2026-11-30. |
| KKR-20261101-14 | 55% | 2026-12-17 | economics/markets | The NYMEX WTI front-month crude settlement on 2026-12-15 is above 100.00 USD per barrel. Reference: 104.12 USD on the packet date. | TRUE if the FRED series DCOILWTICO value for 2026-12-15 is greater than 100.00. Reference: 104.12 on the packet date. |
| KKR-20261101-15 | 50% | 2027-01-05 | economics/markets | The US 10-year Treasury constant-maturity yield closes at or above 5.00 percent on at least one trading day between 2026-11-02 and 2026-12-31. Reference: 4.93 percent on the packet date. | TRUE if the FRED series DGS10 shows a value of 5.00 or higher on any date from 2026-11-02 through 2026-12-31. Reference: 4.93 percent on the packet date. |
| KKR-20261101-16 | 12% | 2027-02-03 | cyber | CISA adds a CVE affecting Canonical LXD or MicroCloud to the Known Exploited Vulnerabilities catalog between 2026-11-02 and 2027-01-31. | TRUE if the CISA KEV catalog has an entry with vendor Canonical and product LXD or MicroCloud whose dateAdded value is between 2026-11-02 and 2027-01-31. |
| KKR-20261101-17 | 30% | 2027-04-05 | cyber | Between 2026-11-02 and 2027-03-31, the US Department of Justice files an indictment, criminal complaint, or civil forfeiture complaint tied to the Binance theft the FBI attributed to North Korea. | TRUE if a justice.gov press release or a federal court docket shows such a filing tied to the Binance theft, dated 2026-11-02 through 2027-03-31. |
| KKR-20261101-18 | 72% | 2026-12-15 | political | In the scheduled 2026-11-03 US midterm elections, Democratic candidates win at least 218 of 435 House seats. | TRUE if Associated Press race calls published by 2026-12-15 give Democratic candidates 218 or more House seats. |
| KKR-20261101-19 | 55% | 2026-12-17 | political | Dan Sullivan is certified the winner of the 2026-11-03 Alaska US Senate election, with certification on or before 2026-12-15. | TRUE if the Alaska Division of Elections certified results, issued on or before 2026-12-15, show Dan Sullivan winning the 2026 US Senate race after ranked-choice tabulation. |
| KKR-20261101-20 | 15% | 2027-01-05 | military/conflict | The US military conducts a strike on Iranian territory between 2026-11-02 and 2026-12-31. | TRUE if the US Department of Defense or White House confirms a US kinetic strike on targets inside Iran's internationally recognized territory occurring between 2026-11-02 and 2026-12-31. |
| KKR-20261101-21 | 50% | 2027-01-05 | disaster | A magnitude 6.0 or greater earthquake occurs in the Vanuatu region between 2026-11-02 and 2026-12-31. | TRUE if the USGS earthquake catalog lists an event of magnitude 6.0 or greater with a place name containing Vanuatu and an origin time between 2026-11-02 and 2026-12-31 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Bitcoin closes below 70,000 USD on at least one day between 2026-11-02 and 2026-12-31. Reference: 77,934 USD on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5233 issued all-time across 22 forecaster arms · 3511 open (720 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 321 issued · 307 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

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
| lmstudio/qwen36 | 149 | 132 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 149 | 147 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 139 | 106 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 321 | 307 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*