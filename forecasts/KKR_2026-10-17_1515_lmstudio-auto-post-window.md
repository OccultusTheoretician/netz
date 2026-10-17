**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-17_1513.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261017-01 | 30% | 2026-11-02 | disaster | Between 2026-10-17 and 2026-10-24, the USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Pakistan with a depth of less than 50 km. | The USGS Significant Quakes catalog records an event with magnitude ≥6.0 and depth <50 km in Pakistan between 2026-10-17 and 2026-10-24. |
| KKR-20261017-02 | 40% | 2026-11-02 | military/conflict | Between 2026-10-17 and 2026-10-24, at least one drone strike will be reported in Kyiv by two or more independently biased sources across hostile sides. | At least one drone strike in Kyiv is reported by two or more independently biased sources across hostile sides (RU, UA, WEST) between 2026-10-17 and 2026-10-24. |
| KKR-20261017-03 | 25% | 2026-11-02 | political | Between 2026-10-17 and 2026-10-24, the Federal Register will publish a notice proposing new sanctions on Russian energy exports. | The Federal Register publishes a notice proposing new sanctions on Russian energy exports between 2026-10-17 and 2026-10-24. |
| KKR-20261017-04 | 35% | 2026-11-02 | cyber | Between 2026-10-17 and 2026-10-24, the NVD will list a new vulnerability in the Drupal content management system with a CVSS score of 9.0 or higher. | The National Vulnerability Database lists a new vulnerability in Drupal with a CVSS score ≥9.0 between 2026-10-17 and 2026-10-24. |
| KKR-20261017-05 | 30% | 2026-11-02 | disaster | Between 2026-10-17 and 2026-10-24, the USGS Significant Quakes catalog will record a magnitude 5.5 or greater earthquake in Russia with a depth of less than 100 km. | The USGS Significant Quakes catalog records an event with magnitude ≥5.5 and depth <100 km in Russia between 2026-10-17 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-17 and 2026-10-24, the CISA KEV catalog will include CVE-2026-102764 with a date-added value of 2026-10-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-102764 dateAdded 2026-10-16, before the claimed window 2026-10-17..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-17 and 2026-10-24, the S&P 500 will close below 7,600 points on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-17 and 2026-10-24, a major wildfire will be reported in California with at least 10,000 acres burned and no casualties repor" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-10-17 and 2026-10-24, the Nasdaq will experience a single-day drop exceeding 5% on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-17 and 2026-10-24, the CISA KEV catalog will include CVE-2025-61624 with a date-added value of 2026-10-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2025-61624 dateAdded 2026-10-16, before the claimed window 2026-10-17..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

4324 issued all-time across 21 forecaster arms · 3213 open (546 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 437 issued · 214 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1526 | 1230 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 437 | 214 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*