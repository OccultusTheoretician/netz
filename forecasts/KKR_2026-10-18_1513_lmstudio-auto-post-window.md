**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181513Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-01 | 30% | 2026-11-02 | military/conflict | A Ukrainian drone attack on a Russian energy facility in St Petersburg results in at least one fatality and damage to infrastructure between 2026-10-18 and 2026-10-24. | At least one fatality is confirmed by two independent wire services (e.g., Reuters, AP) or a government agency report, and physical damage to a Russian energy facility in St Petersburg is documented by satellite imagery or official source during the event window. |
| KKR-20261018-02 | 40% | 2026-11-02 | political | France experiences a major civil unrest event resulting in over 1,500 arrests and at least 100 injuries between 2026-10-18 and 2026-10-24. | Two independent wire services (e.g., AFP, Reuters) report that over 1,500 people were arrested and at least 100 were injured in France during the event window, with injuries confirmed by medical or official sources. |
| KKR-20261018-03 | 35% | 2026-11-02 | disaster | A wildfire in Alberta, Canada, spreads beyond 500 hectares and causes at least one fatality between 2026-10-18 and 2026-10-24. | The Canadian Interagency Forest Fire Centre (CIFFC) or a provincial fire agency confirms a wildfire in Alberta exceeding 500 hectares and causing at least one fatality during the event window. |
| KKR-20261018-04 | 55% | 2026-11-02 | economics/markets | The S&P 500 index closes above 7,800 points on the final trading day of the event window, between 2026-10-18 and 2026-10-24. | The S&P 500 closes at or above 7,800.00 on the last trading day of the event window, as reported by the S&P Global Market Intelligence database. |
| KKR-20261018-05 | 20% | 2026-11-02 | military/conflict | Iran announces a new military operational plan targeting shipping in the Strait of Hormuz between 2026-10-18 and 2026-10-24. | An official statement from Iran's Ministry of Defense or IRGC confirms a new operational plan targeting shipping in the Strait of Hormuz during the event window. |
| KKR-20261018-06 | 60% | 2026-11-02 | economics/markets | The 10-year U.S. Treasury yield exceeds 5.3% on any trading day between 2026-10-18 and 2026-10-24. | The FRED database shows the 10-year U.S. Treasury yield surpassing 5.3% on at least one trading day during the event window. |
| KKR-20261018-07 | 18% | 2026-11-02 | disaster | A new outbreak of a respiratory illness with confirmed human-to-human transmission is reported in South Africa between 2026-10-18 and 2026-10-24. | The World Health Organization (WHO) or South Africa's National Institute for Communicable Diseases (NICD) confirms a new respiratory illness with human-to-human transmission in South Africa during the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A cyberattack exploiting the SiteGuard WAF vulnerability (CVE-2026-XXXX) leads to unauthorized access to at least one government system in t" → REJECTED: resolution offers alternative VENUES joined by 'or' (…u.s. | or | eu government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A major earthquake of magnitude 6.0 or higher occurs in the Pacific Northwest region of the United States between 2026-10-18 and 2026-10-24." → REJECTED: cited items name Pakistan; the claim is about Idaho, Oregon, United States, Washington — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "A coordinated cyberattack on a U.S. state-level election system disrupts voter registration or ballot processing between 2026-10-18 and 2026" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

4413 issued all-time across 21 forecaster arms · 3302 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 444 issued · 221 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1556 | 1260 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 75 | 75 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 227 | 168 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*