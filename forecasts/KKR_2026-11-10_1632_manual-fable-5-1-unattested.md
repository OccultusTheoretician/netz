**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101632Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-10_1613.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261110-19 | 55% | 2026-12-15 | economics/markets | FRED series DGS10 records a 10-year Treasury constant-maturity yield of 5.00 percent or higher on at least one trading day between 2026-11-11 and 2026-12-11. Reference: 4.99 percent on the packet date. | True if any DGS10 value dated 2026-11-11 through 2026-12-11 on FRED is at or above 5.00; false otherwise. |
| KKR-20261110-20 | 20% | 2026-12-22 | economics/markets | The FOMC raises the federal funds target range by at least 50 basis points at its scheduled meeting concluding in December 2026. | True if the Federal Reserve policy statement for the December 2026 meeting raises the target range by 50 basis points or more; false for any smaller change, hold, or cut. |
| KKR-20261110-21 | 65% | 2026-12-15 | economics/markets | Anthropic files a final prospectus (Form 424B4) on SEC EDGAR dated between 2026-11-11 and 2026-12-11 showing an initial public offering price of at least 70 USD per share. | True if EDGAR shows an Anthropic 424B4 dated in the window with a public offering price of 70 USD or more; false if no such filing or a lower price. |
| KKR-20261110-22 | 45% | 2026-12-15 | economics/markets | FRED series DCOILWTICO records a WTI spot price below 80.00 USD on at least one day between 2026-11-11 and 2026-12-11. Reference: 85.63 on the packet date. | True if any DCOILWTICO value dated 2026-11-11 through 2026-12-11 is below 80.00; false otherwise. |
| KKR-20261110-23 | 25% | 2026-11-30 | political | The US House adopts at least one article of impeachment against Secretary of Defense Pete Hegseth in a roll call recorded on Congress.gov between 2026-11-10 and 2026-11-24. | True if Congress.gov records a House roll call in the window adopting a resolution impeaching Hegseth; a motion to table, refer, or a failed vote resolves false. |
| KKR-20261110-24 | 35% | 2027-02-05 | political | The EU publishes in the Official Journal a sanctions listing under its cyber-attack regime naming at least one Iranian person or entity, with the listing text citing attacks on French targets, between 2026-11-10 and 2027-01-31. | True if EUR-Lex shows an implementing regulation or decision dated in the window listing an Iranian person or entity whose statement of reasons references cyberattacks in France; false otherwise. |
| KKR-20261110-25 | 75% | 2026-11-27 | cyber | The CISA KEV catalog adds an entry with vendorProject Google and product Chromium carrying a dateAdded between 2026-11-10 and 2026-11-24. | True if the CISA KEV JSON feed contains a Google Chromium entry whose dateAdded falls in the window; false otherwise. |
| KKR-20261110-26 | 55% | 2026-12-03 | cyber | The CISA KEV catalog adds an entry with vendorProject Barracuda Networks carrying a dateAdded between 2026-11-10 and 2026-11-30. | True if the CISA KEV JSON feed contains a Barracuda Networks entry whose dateAdded falls in the window; false otherwise. |
| KKR-20261110-27 | 25% | 2026-12-14 | disaster | USGS records an earthquake of magnitude 6.0 or greater with epicenter within 300 km of USGS event us7000tx16 (near Lata, Solomon Islands) between 2026-11-11 and 2026-12-10. | True if the USGS ComCat catalog lists an M6.0 or greater event in the window within 300 km of the us7000tx16 epicenter; false otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The governments of Russia and Ukraine both publicly announce acceptance of a general ceasefire with a stated effective date between 2026-11-" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — partial. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

5552 issued all-time across 22 forecaster arms · 3830 open (1420 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 518 issued · 403 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 132 | 132 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 198 | 181 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 204 | 202 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 178 | 145 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 518 | 403 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 364 | 350 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*