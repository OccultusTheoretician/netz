**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071525Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-14 | 20% | 2026-10-24 | disaster | The USGS Significant Quakes catalog records an earthquake with magnitude 6.0 or greater between 2026-10-15 and 2026-10-22. | True if a magnitude 6.0+ event is recorded in the catalog within the window; False if no such event is recorded. |
| KKR-20261007-15 | 60% | 2026-10-24 | political | The UK Conservative Party leadership election concludes with a winner announced between 2026-10-15 and 2026-10-22. | True if a winner is publicly announced by a wire service within the window; False if the contest is still ongoing or unresolved. |
| KKR-20261007-16 | 15% | 2026-10-24 | disaster | A major power outage lasting more than 24 hours occurs in France between 2026-10-15 and 2026-10-22, confirmed by RTE or a major wire service. | True if RTE or a wire service confirms a >24h outage; False if no such event is reported. |
| KKR-20261007-17 | 35% | 2026-10-24 | cyber | A new CVE is added to the NVD database with a CVSS score of 9.0 or higher for a vulnerability exploited in the wild, with a date_added between 2026-10-15 and 2026-10-22. | True if such a CVE exists in the NVD with the specified date_added; False if no such entry is found. |
| KKR-20261007-18 | 55% | 2026-10-23 | economics/markets | The S&P 500 closes above 7,900 on at least one trading day between 2026-10-15 and 2026-10-22. | True if the index closes above 7,900 on any day in the window; False if it remains at or below 7,900 for the entire window. Reference: 7,777.51 on the packet date. |
| KKR-20261007-19 | 10% | 2026-10-24 | disaster | A tropical cyclone makes landfall in the United States between 2026-10-15 and 2026-10-22, confirmed by the NHC. | True if the NHC confirms a landfall within the window; False if no landfall occurs. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-10-07 and 2026-10-14 for a vulnerability exploited in the wild that was first r" → REJECTED: the resolution names only a venue or register (KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI Crude closes below 87.00 USD per barrel on at least one trading day between 2026-10-15 and 2026-10-22." → REJECTED: the resolution names a different subject than the statement — the claim is about Crude, WTI and the resolution settles on Reference. A row whose resolution checks a different fact can be scored correct while being wrong
- "The 10-year US Treasury yield closes above 5.50% on at least one trading day between 2026-10-15 and 2026-10-22." → REJECTED: the resolution names a different subject than the statement — the claim is about Treasury and the resolution settles on Reference. A row whose resolution checks a different fact can be scored correct while being wrong
- "The European Central Bank announces an interest rate cut between 2026-10-15 and 2026-10-22." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

3553 issued all-time across 21 forecaster arms · 2739 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 19 issued · 19 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1265 | 1064 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*