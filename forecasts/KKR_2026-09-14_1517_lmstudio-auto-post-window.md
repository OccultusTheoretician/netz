**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141517Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260914-01 | 25% | 2026-09-28 | economics/markets | Between 2026-09-22 and 2026-09-25, the S&P 500 closes below 7,500 points on at least one trading day, based on the official market close from the NYSE. | The S&P 500 index closes below 7,500 points on at least one trading day between 2026-09-22 and 2026-09-25, as recorded by the NYSE official close. |
| KKR-20260914-02 | 35% | 2026-09-30 | economics/markets | Between 2026-09-25 and 2026-09-28, the 10-year U.S. Treasury yield exceeds 5.1% on at least one trading day, based on the official close from the U.S. Treasury. | The 10-year U.S. Treasury yield exceeds 5.1% on at least one trading day between 2026-09-25 and 2026-09-28, as recorded by the U.S. Treasury's official daily yield data. |
| KKR-20260914-03 | 10% | 2026-10-01 | military/conflict | Between 2026-09-26 and 2026-09-29, Iran announces a formal closure of the Strait of Hormuz to foreign shipping, as confirmed by a statement from the Iranian Foreign Ministry and at least two independent news outlets. | A statement from the Iranian Foreign Ministry, published between 2026-09-26 and 2026-09-29, confirms the closure of the Strait of Hormuz to foreign shipping, and at least two independent news outlets (e.g., BBC, Al Jazeera, Guardian) report the closure. |
| KKR-20260914-04 | 25% | 2026-10-02 | cyber | Between 2026-09-27 and 2026-09-30, a cyberattack on a U.S. federal agency results in the exposure of at least 1 million user records, as confirmed by a CISA KEV entry and a federal press release. | The CISA KEV catalog carries a date-added value between 2026-09-27 and 2026-09-30, and a U.S. federal agency issues a public press release confirming the exposure of at least 1 million user records due to a cyberattack. |
| KKR-20260914-05 | 15% | 2026-10-03 | political | Between 2026-09-28 and 2026-10-01, the U.S. Congress passes the Clarity Act with a majority vote in both chambers, as confirmed by a roll call vote on Congress.gov. | A roll call vote on Congress.gov confirms that the Clarity Act passed in both the House and Senate with a majority vote, as recorded by the official legislative database. |
| KKR-20260914-06 | 30% | 2026-10-05 | cyber | Between 2026-09-30 and 2026-10-03, a major data breach at Revolut exposes financial information and passport details of at least 500,000 users, as confirmed by a CISA KEV entry and a press release from Revolut. | The CISA KEV catalog carries a date-added value between 2026-09-30 and 2026-10-03, and Revolut issues a public press release confirming the exposure of financial information and passport details of at least 500,000 users. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, a Russian drone strike on a passenger train near the Ukraine-Poland border results in at least one fatali" → REJECTED: resolution offers alternative VENUES joined by 'or' (…government | or | military…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-23 and 2026-09-26, a malicious OAuth application exploits a vulnerability in Google Workspace, leading to unauthorized acces" → REJECTED: resolution offers alternative VENUES joined by 'or' (…third-party security firm | or | official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-24 and 2026-09-27, a flash flood in the Central African Republic causes at least 50 fatalities, as confirmed by GDACS Alerts" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Between 2026-09-29 and 2026-10-02, a tropical cyclone named FIFTEEN-E-26 causes at least 100 fatalities in the Pacific region, as confirmed " → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

2075 issued all-time across 16 forecaster arms · 1739 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 265 issued · 136 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 674 | 636 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*