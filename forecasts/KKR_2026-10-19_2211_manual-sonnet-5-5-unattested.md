**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192211Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-19_1513.md · forecaster: manual/sonnet-5.5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261019-55 | 82% | 2026-11-24 | political | Democratic candidates win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03, with Associated Press race calls showing this by 2026-11-24. | Associated Press race calls as of 2026-11-24 show Democratic candidates winning at least 218 House seats in the 2026-11-03 general election. |
| KKR-20261019-56 | 80% | 2026-12-14 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its meeting concluding on 2026-12-09. Reference: the target range was 3.75 to 4.00 percent on the packet date. | The Federal Reserve press release dated 2026-12-09 announces a target range above 3.75 to 4.00 percent, and FRED series DFEDTARU for 2026-12-10 exceeds 4.00. |
| KKR-20261019-57 | 35% | 2026-11-27 | military/conflict | United States forces carry out at least one acknowledged military strike on a target on Iranian land or in Iranian territorial waters between 2026-11-04 and 2026-11-24. | US officials acknowledge, or at least two of Reuters, AP, BBC and NYT report, a US military strike on a target on Iranian soil or in Iranian territorial waters occurring between 2026-11-04 and 2026-11-24. |
| KKR-20261019-58 | 14% | 2026-11-24 | political | Donald Trump and Vladimir Putin meet in person for talks at the same venue between 2026-10-26 and 2026-11-20. | At least two of Reuters, AP and BBC report that Trump and Putin were physically together for talks between 2026-10-26 and 2026-11-20, including any three-way meeting with Xi Jinping. |
| KKR-20261019-59 | 15% | 2026-12-18 | political | Sebastien Lecornu ceases to hold the office of French prime minister, through resignation, dismissal or an adopted motion of censure, between 2026-10-20 and 2026-12-16. | Journal Officiel or Elysee records acceptance of the resignation of Sebastien Lecornu, his dismissal, or adoption by the Assemblee nationale of a motion de censure, between 2026-10-20 and 2026-12-16; caretaker continuation after acceptance still counts. |
| KKR-20261019-60 | 9% | 2026-11-12 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one vulnerability affecting F5 NGINX products with a dateAdded value between 2026-10-20 and 2026-11-09. | The CISA KEV catalog JSON feed lists at least one entry referencing NGINX in its vendorProject, product or vulnerabilityName field with a dateAdded value between 2026-10-20 and 2026-11-09. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent front-month futures settle at or above 120.00 dollars per barrel on at least one trading day between 2026-10-26 and 2026-11-20. Re" → REJECTED: resolution offers alternative VENUES joined by 'or' (…m 2026-10-26 through 2026-11-20, per ice data | or | reuters settlement reports…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one merchant vessel (tanker, container ship or bulk carrier) sinks in or near the Strait of Hormuz, Persian Gulf or Gulf of Oman af" → REJECTED: the resolution names a different subject than the statement — the claim is about Gulf, Hormuz, Oman, Persian and the resolution settles on AP, BBC, CNBC, IMO. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Singapore National Environment Agency reports a 24-hour PSI of 201 or higher (Very Unhealthy) in at least one of its five regions at som" → REJECTED: cited items name Indonesia; the claim is about Singapore — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A federal grand jury indictment or prosecutor information charging Alfozan, the suspect in the OpenAI bugging case, is filed in US federal c" → REJECTED: cited items name Saudi Arabia; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4541 issued all-time across 21 forecaster arms · 3189 open (313 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 171 issued · 168 open · 3 resolved · 3 hits / 0 misses · **Brier 0.009** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1597 | 1214 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 445 | 204 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 92 | 85 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 231 | 144 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 388 | 307 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 219 | 208 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 171 | 168 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*