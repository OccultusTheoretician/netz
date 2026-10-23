**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 230001Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-15 | 55% | 2026-12-03 | military/conflict | Official Russian and Ukrainian government delegations hold at least one in-person negotiating session on ending or pausing the war, bilaterally or with mediators present, between 2026-10-23 and 2026-11-30. | TRUE if official sources on both the Russian and Ukrainian sides confirm an in-person negotiating session attended by delegations of both governments, held between 2026-10-23 and 2026-11-30. Prisoner-exchange technical contacts alone do not count. |
| KKR-20261023-16 | 30% | 2027-01-04 | military/conflict | Israel or the United States carries out an air, missile, or drone strike on targets inside Iranian territory between 2026-10-23 and 2026-12-31, and the government that carried it out publicly acknowledges it. | TRUE if the Israeli government or IDF, or the US government, publicly acknowledges conducting an air, missile, or drone strike on Iranian territory that occurred between 2026-10-23 and 2026-12-31; otherwise FALSE. |
| KKR-20261023-17 | 25% | 2027-01-15 | economics/markets | The WTI crude spot price (FRED series DCOILWTICO) records a daily value at or above 110.00 USD per barrel on at least one date between 2026-10-23 and 2026-12-31. Reference: WTI 98.51 on the packet date. | TRUE if FRED series DCOILWTICO shows any daily value dated between 2026-10-23 and 2026-12-31 at or above 110.00; otherwise FALSE. Reference: 98.51 on the packet date. |
| KKR-20261023-18 | 85% | 2026-11-23 | cyber | CISA adds at least one PHP vulnerability (KEV vendorProject PHP, such as the PHP2Shell flaws) to its Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-22 and 2026-11-20. | TRUE if the CISA KEV catalog lists an entry with vendorProject PHP whose dateAdded falls between 2026-10-22 and 2026-11-20 inclusive; otherwise FALSE. |
| KKR-20261023-19 | 30% | 2027-01-04 | cyber | CISA adds at least one GitLab vulnerability (KEV vendorProject GitLab), such as the CVSS 10.0 flaw reported on 2026-10-21, to its Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-22 and 2026-12-31. | TRUE if the CISA KEV catalog lists an entry with vendorProject GitLab whose dateAdded falls between 2026-10-22 and 2026-12-31 inclusive; otherwise FALSE. |
| KKR-20261023-20 | 33% | 2026-12-18 | political | California Proposition 40, the billionaire wealth tax measure, is approved by voters in the general election held on 2026-11-03. | TRUE if the certified Statement of Vote from the California Secretary of State shows more Yes than No votes on Proposition 40 in the 2026-11-03 general election; otherwise FALSE. |
| KKR-20261023-21 | 12% | 2027-04-16 | crime/security | A court dismisses every criminal charge against Virginia state Senator L. Louise Lucas, in the case reported on 2026-10-22, by an order entered between 2026-10-23 and 2027-04-13. | TRUE if the court docket in the criminal case against L. Louise Lucas records an order dismissing every charge against her, entered between 2026-10-23 and 2027-04-13; otherwise FALSE. |
| KKR-20261023-22 | 15% | 2026-11-24 | disaster | An earthquake of USGS magnitude 6.0 or greater occurs within 100 km of the epicenter of USGS event us6000u43g, the M7.0 east-northeast of Nagqu, China, between 2026-10-23 and 2026-11-21 UTC. | TRUE if USGS ComCat lists an event with preferred magnitude 6.0 or greater, origin time between 2026-10-23 and 2026-11-21 UTC, and epicenter within 100 km of event us6000u43g; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A Houthi missile or drone attack on Saudi Arabian territory kills at least one person between 2026-10-23 and 2026-11-22." → REJECTED: resolution offers alternative VENUES joined by 'or' (…the saudi press agency, | or | at least two of reuters, ap   afp, report one…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Democratic candidates win at least 218 of the 435 US House of Representatives seats in the general election held on 2026-11-03." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4734 issued all-time across 21 forecaster arms · 3382 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 245 issued · 234 open · 11 resolved · 5 hits / 6 misses · **Brier 0.362** against its own base rate 45.5% (climatological 0.248) · **skill -0.460** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1664 | 1281 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 457 | 216 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*