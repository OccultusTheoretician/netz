**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051648Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-23 | 83% | 2026-10-28 | political | Flavio Bolsonaro receives more valid votes than Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25. | TSE official results for the presidential runoff held on 2026-10-25 show Flavio Bolsonaro with more valid votes than Lula da Silva. |
| KKR-20261005-24 | 88% | 2026-12-02 | political | The Partido Popular wins more seats in the Congress of Deputies than any other party in the Spanish general election held on 2026-11-29. | Spanish Interior Ministry official results for the general election held on 2026-11-29 show the Partido Popular with strictly more Congress seats than every other party. |
| KKR-20261005-25 | 15% | 2026-12-21 | political | The French National Assembly adopts a motion of censure against the sitting government between 2026-10-12 and 2026-12-18. | Assemblee nationale official vote records show a motion of censure adopted by the required absolute majority in a vote held between 2026-10-12 and 2026-12-18. |
| KKR-20261005-26 | 17% | 2026-10-30 | economics/markets | The FOMC raises the federal funds target range at its meeting ending 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date. | FRED series DFEDTARU, the target range upper limit, reads 4.25 or higher for 2026-10-29. Reference: 4.00 percent on the packet date. |
| KKR-20261005-27 | 48% | 2026-11-02 | economics/markets | Nvidia shares close at or above 248.00 dollars on Nasdaq on at least one trading day between 2026-10-06 and 2026-10-30. Reference: 233.95 dollars at the 2026-10-02 close, about 237 intraday on the packet date. | The Nasdaq official closing price of NVDA is 248.00 dollars or higher on at least one trading day between 2026-10-06 and 2026-10-30. Reference: 233.95 dollars at the 2026-10-02 close. |
| KKR-20261005-28 | 65% | 2026-10-28 | crime/security | At least one person is arrested on charges tied to the 2026-10-04 block party shooting in Vienna, Dooly County, Georgia, between 2026-10-05 and 2026-10-26. | The Georgia Bureau of Investigation or the Dooly County Sheriff confirms an arrest, made between 2026-10-05 and 2026-10-26, on charges tied to the Vienna shooting of 2026-10-04. |
| KKR-20261005-29 | 28% | 2026-12-07 | military/conflict | The United States carries out at least one military strike on a target on Iranian land territory between 2026-10-12 and 2026-12-04. | The Pentagon, CENTCOM or the White House confirms, or both Reuters and AP report, a US strike on Iranian land territory carried out between 2026-10-12 and 2026-12-04. |
| KKR-20261005-30 | 90% | 2026-10-28 | military/conflict | At least one commercial vessel is struck or attacked in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-12 and 2026-10-25. | UKMTO publishes at least one incident notice of a vessel struck or attacked in the Strait of Hormuz, Persian Gulf or Gulf of Oman, with an incident date between 2026-10-12 and 2026-10-25. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Democratic Party candidates win at least 17 of the 35 US Senate contests of the 2026-11-03 elections, counting any runoff held on or before " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds at least one further Citrix NetScaler vulnerability, beyond CVE-2026-88779, to its Known Exploited Vulnerabilities catalog between" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88779 dateAdded 2026-10-04, before the claimed window 2026-10-06..2026-11-06; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

3421 issued all-time across 21 forecaster arms · 2607 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 266 issued · 233 open · 25 resolved · 20 hits / 5 misses · **Brier 0.207** against its own base rate 80.0% (climatological 0.160) · **skill -0.296** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1218 | 1017 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 46 | 46 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*