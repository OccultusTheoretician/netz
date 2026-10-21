**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212254Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-21_1512.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261021-12 | 78% | 2026-12-18 | political | Democratic candidates win at least 218 of 435 seats in the US House elections held on 2026-11-03, as called by 2026-12-18. | Associated Press race calls or the House Clerk official results, checked on 2026-12-18, show Democratic candidates winning at least 218 House seats in the 2026-11-03 elections. |
| KKR-20261021-13 | 35% | 2027-01-05 | political | The French Prime Minister leaves office, by a decree ending the government functions or by an adopted motion de censure, between 2026-10-22 and 2026-12-31. | A decree published in the Journal Officiel (legifrance.gouv.fr) recording the end of the Prime Minister functions, or a motion de censure adopted by the National Assembly, dated between 2026-10-22 and 2026-12-31. |
| KKR-20261021-14 | 12% | 2027-02-02 | military/conflict | The governments of Russia and Ukraine both publicly announce agreement to a general ceasefire covering the entire front line between 2026-10-22 and 2027-01-29. | Official statements on kremlin.ru and president.gov.ua, corroborated by Reuters and AP, record both governments agreeing to a front-wide ceasefire between 2026-10-22 and 2027-01-29; energy-only or maritime-only pauses do not count. |
| KKR-20261021-15 | 20% | 2027-01-05 | military/conflict | The UK Ministry of Defence or the French Ministry of the Armed Forces publicly confirms that its own forces struck Houthi targets inside Yemen between 2026-10-22 and 2026-12-31. | An official gov.uk or defense.gouv.fr statement, corroborated by Reuters or AP, confirms a UK or French strike on targets inside Yemen dated between 2026-10-22 and 2026-12-31; interceptions do not count. |
| KKR-20261021-16 | 30% | 2026-12-30 | economics/markets | The daily Europe Brent spot price (EIA, FRED DCOILBRENTEU) is at or above 120.00 USD per barrel on at least one date between 2026-10-22 and 2026-12-18. Reference: 109.25 on 2026-10-21. | The EIA Europe Brent spot series (FRED DCOILBRENTEU) shows a daily value at or above 120.00 for at least one date between 2026-10-22 and 2026-12-18. Reference: 109.25 on 2026-10-21. |
| KKR-20261021-17 | 58% | 2027-01-06 | economics/markets | The 10-year US Treasury constant maturity yield (FRED DGS10) dated 2026-12-31 is at or above 5.00 percent. Reference: 5.11 percent on 2026-10-21. | The FRED DGS10 observation dated 2026-12-31 is at or above 5.00. If no observation exists for 2026-12-31, the last observation dated on or before it governs. Reference: 5.11 on 2026-10-21. |
| KKR-20261021-18 | 45% | 2026-11-20 | cyber | CISA adds at least one PHP Group (PHP) vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-21 and 2026-11-18. | The CISA KEV JSON feed contains at least one entry whose vendorProject is PHP Group (product PHP) with dateAdded between 2026-10-21 and 2026-11-18 inclusive. |
| KKR-20261021-19 | 40% | 2026-12-08 | disaster | WHO reporting published between 2026-10-22 and 2026-12-04 shows a cumulative total of at least 20 confirmed Ebola cases in Kenya for the outbreak confirmed in October 2026. Reference: 9 confirmed cases on 2026-10-21. | A WHO Disease Outbreak News post or WHO AFRO situation report published between 2026-10-22 and 2026-12-04 gives a cumulative count of at least 20 confirmed Ebola cases in Kenya. Reference: 9 on 2026-10-21. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-22 and 2027-03-31 the US Justice Department announces criminal charges against a person identified as a SafePay ransomware o" → REJECTED: resolution offers alternative VENUES joined by 'or' (…gov press release announcing charges, | or | an ofac sdn designation press release on trea…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Australian federal government announces new funding, with a stated dollar amount, for the security of federal parliamentarians between 2" → REJECTED: the resolution names a different subject than the statement — the claim is about Australian and the resolution settles on Commonwealth, MYEFO. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

4650 issued all-time across 21 forecaster arms · 3298 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 406 issued · 325 open · 73 resolved · 47 hits / 26 misses · **Brier 0.233** against its own base rate 64.4% (climatological 0.229) · **skill -0.015**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1633 | 1250 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 453 | 212 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 236 | 149 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 229 | 218 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 181 | 178 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*