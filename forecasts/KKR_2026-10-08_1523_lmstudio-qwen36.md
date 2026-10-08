**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081523Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: lmstudio/qwen36 · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-14 | 30% | 2026-10-23 | cyber | A new critical vulnerability with a CVSS score of 10.0 is added to the CISA Known Exploited Vulnerabilities catalog between 2026-10-15 and 2026-10-20 | The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-20 for a vulnerability with a CVSS score of 10.0 |
| KKR-20261008-15 | 45% | 2026-10-23 | disaster | Hurricane Isaias makes landfall in the United States with sustained winds of at least 74 mph between 2026-10-15 and 2026-10-20 | The National Hurricane Center issues a public advisory confirming Hurricane Isaias makes landfall in the United States with sustained winds of at least 74 mph between 2026-10-15 and 2026-10-20 |
| KKR-20261008-16 | 55% | 2026-10-23 | military/conflict | Russia conducts a kinetic strike using a ballistic missile on a civilian target in Kyiv between 2026-10-15 and 2026-10-20 | Three or more independent hostile sides confirm a Russian ballistic missile strike on a civilian target in Kyiv between 2026-10-15 and 2026-10-20 |
| KKR-20261008-17 | 20% | 2026-10-23 | political | The UK House of Commons votes to approve German participation in the GCAP fighter jet programme between 2026-10-15 and 2026-10-20 | The UK House of Commons passes a motion or bill approving German participation in the GCAP fighter jet programme between 2026-10-15 and 2026-10-20 |
| KKR-20261008-18 | 15% | 2026-10-23 | crime/security | The FBI issues a public indictment against a major cybercrime market operator for ransomware activities between 2026-10-15 and 2026-10-20 | The US Department of Justice or FBI publishes a public indictment naming a major cybercrime market operator for ransomware activities between 2026-10-15 and 2026-10-20 |
| KKR-20261008-19 | 40% | 2026-10-23 | disaster | A magnitude 7.0 or greater earthquake occurs in the Pacific Ring of Fire between 2026-10-15 and 2026-10-20 | The USGS Significant Quakes catalog records an event with a magnitude of 7.0 or greater in the Pacific Ring of Fire between 2026-10-15 and 2026-10-20 |
| KKR-20261008-20 | 10% | 2026-10-23 | military/conflict | South Korea test-fires a hypersonic missile with a range exceeding 1,000 km between 2026-10-15 and 2026-10-20 | The South Korean Ministry of National Defense or a major international news agency confirms a test-fire of a hypersonic missile with a range exceeding 1,000 km between 2026-10-15 and 2026-10-20 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude oil settles above 100 USD per barrel on the New York Mercantile Exchange between 2026-10-15 and 2026-10-20" → REJECTED: cited items name Iran, Islamic Republic of, United Kingdom; the claim is about New York — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The US Congress passes legislation formally declaring a national emergency related to the Gulf of Mexico shipping attacks between 2026-10-15" → REJECTED: cited items name Iran, Islamic Republic of, Qatar, United States; the claim is about Mexico — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The S&P 500 index closes below 7,500 points on the New York Stock Exchange between 2026-10-15 and 2026-10-20" → REJECTED: the resolution names only a venue or register (NYSE) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

3632 issued all-time across 21 forecaster arms · 2818 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 17 issued · 17 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1292 | 1091 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
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