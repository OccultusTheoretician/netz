**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082051Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-52 | 80% | 2026-10-13 | economic | ICE Brent front-month crude settles above 100.00 USD per barrel on at least one trading day between 2026-09-09 and 2026-10-09. Reference: 97.68 on the packet date, 2026-09-08. | TRUE if any ICE Brent front-month official settlement between 2026-09-09 and 2026-10-09 exceeds 100.00 USD per barrel. Reference level 97.68 on 2026-09-08. |
| KKR-20260908-53 | 22% | 2026-11-17 | economic | The United States and Canada announce removal or suspension of at least one tranche of the reciprocal tariffs now in force, announced between 2026-09-09 and 2026-11-13. | TRUE if a US or Canadian government announcement dated between 2026-09-09 and 2026-11-13 removes or suspends any tariff tranche applied to the other country. |
| KKR-20260908-54 | 72% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one Adobe Commerce or Magento CVE with a dateAdded value between 2026-09-09 and 2026-10-09. | TRUE if the CISA KEV JSON feed contains an Adobe Commerce or Magento entry whose dateAdded field falls between 2026-09-09 and 2026-10-09 inclusive. |
| KKR-20260908-55 | 25% | 2026-11-10 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one SAP vendor CVE with a dateAdded value between 2026-09-09 and 2026-11-06. | TRUE if the CISA KEV JSON feed contains an entry with vendorProject SAP whose dateAdded field falls between 2026-09-09 and 2026-11-06 inclusive. |
| KKR-20260908-56 | 55% | 2026-10-05 | military_conflict | Saudi Arabia conducts acknowledged military strikes on Houthi-controlled territory in Yemen between 2026-09-09 and 2026-09-30. | TRUE if two of Reuters, AP, AFP, BBC and Al Jazeera report Saudi strikes inside Houthi-held Yemen occurring in the window, with Saudi or Houthi attribution. |
| KKR-20260908-57 | 30% | 2026-11-17 | military_conflict | A ceasefire or cessation of hostilities involving Iran and the United States or Israel is publicly announced between 2026-09-09 and 2026-11-13. | TRUE if a government or the United Nations announces a ceasefire, truce or cessation of hostilities covering Iranian and US or Israeli forces, dated inside the window. |
| KKR-20260908-58 | 45% | 2026-10-13 | political | Russia expels or declares persona non grata at least one Hungarian diplomat between 2026-09-09 and 2026-10-09. | TRUE if the Russian Foreign Ministry announces expulsion or persona non grata designation of one or more Hungarian diplomats, with the announcement dated inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "In the Swedish Riksdag election held 2026-09-13, the combined seat total of V, S, MP and C exceeds the combined seat total of M, KD, L and S" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The AfD receives the largest share of Zweitstimmen in the Mecklenburg-Vorpommern Landtag election held 2026-09-20." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "At least one painting taken in the Renoir museum theft in southern France is physically recovered by authorities between 2026-09-09 and 2026" → REJECTED: the resolution names a different subject than the statement — the claim is about France, Renoir and the resolution settles on French. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1736 issued all-time across 16 forecaster arms · 1471 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 206 issued · 200 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 530 | 502 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 235 | 147 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 188 | 186 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 206 | 200 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 192 | 171 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*