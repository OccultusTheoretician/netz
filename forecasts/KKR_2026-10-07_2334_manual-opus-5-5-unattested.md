**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 072334Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-61 | 17% | 2027-01-05 | military/conflict | Between 2026-10-08 and 2026-12-31, the US and Iranian governments both publicly announce or confirm a ceasefire or agreement ending hostilities between the United States and Iran. | TRUE if, between 2026-10-08 and 2026-12-31, the US government and the Iranian government each publicly announce or confirm a ceasefire or agreement ending US-Iran hostilities, as reported by Reuters or AP. |
| KKR-20261007-62 | 18% | 2027-01-05 | economics/markets | The S&P 500 closes at or below 7000.00 on at least one trading day between 2026-10-08 and 2026-12-31 (reference: 7,777.51 on the packet date). | TRUE if FRED series SP500 shows a daily close at or below 7000.00 on any trading day between 2026-10-08 and 2026-12-31. Reference: 7,777.51 on the packet date. |
| KKR-20261007-63 | 58% | 2027-01-05 | economics/markets | The 10-year US Treasury constant-maturity yield prints at or above 5.50 percent on at least one day between 2026-10-08 and 2026-12-31 (reference: 5.30 percent on the packet date). | TRUE if FRED series DGS10 shows a value at or above 5.50 on any date between 2026-10-08 and 2026-12-31. Reference: 5.30 percent on the packet date. |
| KKR-20261007-64 | 15% | 2027-01-05 | economics/markets | Between 2026-10-08 and 2026-12-31, the US government publishes in the Federal Register a binding prohibition, quota, or export-license requirement on diesel fuel exports. | TRUE if a proclamation, executive order, or rule published in the Federal Register between 2026-10-08 and 2026-12-31 prohibits, caps by quota, or imposes a license requirement on US diesel fuel exports. |
| KKR-20261007-65 | 70% | 2026-11-09 | cyber | CISA adds at least one Atlassian vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-07 and 2026-11-06. | TRUE if the CISA KEV catalog carries an entry with vendorProject Atlassian and a dateAdded value between 2026-10-07 and 2026-11-06 inclusive. |
| KKR-20261007-66 | 30% | 2027-01-05 | cyber | CISA adds a SonicWall SMA1000 vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-07 and 2026-12-31. | TRUE if the CISA KEV catalog carries a SonicWall entry whose product field names SMA1000 or SMA 1000, with a dateAdded value between 2026-10-07 and 2026-12-31 inclusive. |
| KKR-20261007-67 | 33% | 2026-12-04 | political | The Democratic nominee wins the Texas US Senate election held on 2026-11-03 against Republican nominee Ken Paxton. | TRUE if Texas Secretary of State returns for the general election held 2026-11-03 show the Democratic nominee receiving the most votes for US Senate. |
| KKR-20261007-68 | 45% | 2026-10-28 | political | Flavio Bolsonaro wins the Brazilian presidential runoff held on 2026-10-25. | TRUE if official TSE results for the Brazilian presidential runoff held on 2026-10-25 show Flavio Bolsonaro receiving the most valid votes. |
| KKR-20261007-69 | 27% | 2026-11-09 | disaster | Between 2026-10-07 and 2026-11-06, the cumulative count of laboratory-confirmed Ebola disease cases in Kenya reaches at least 2. | TRUE if WHO Disease Outbreak News or the Kenya Ministry of Health reports at least 2 cumulative laboratory-confirmed Ebola disease cases in Kenya, with the count reached between 2026-10-07 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-08 and 2026-11-07, a single Russian air attack (missile, drone, or glide bomb) on one Ukrainian city or town kills at least " → REJECTED: cited items name Russian Federation; the claim is about Ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3603 issued all-time across 21 forecaster arms · 2789 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 112 issued · 112 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1283 | 1082 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*