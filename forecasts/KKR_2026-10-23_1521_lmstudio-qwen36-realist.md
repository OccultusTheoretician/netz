**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 4 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-67 | 30% | 2026-11-09 | economics | WTI Crude closes below 95.00 on at least one weekday between 2026-11-02 and 2026-11-06. | The closing price of WTI Crude is below 95.00 on at least one trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261023-68 | 20% | 2026-11-10 | disaster | A magnitude 6.0 or greater earthquake is recorded by USGS in the Indonesia archipelago between 2026-11-01 and 2026-11-08. | USGS Significant Quakes records an event with mag >= 6.0 in Indonesia between 2026-11-01 and 2026-11-08. |
| KKR-20261023-69 | 25% | 2026-11-09 | economics | The 10-year US Treasury yield closes above 5.20 on at least one weekday between 2026-11-02 and 2026-11-06. | The closing value of the 10-year US Treasury yield is above 5.20 on at least one trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261023-70 | 30% | 2026-11-10 | military | Russia conducts a kinetic strike on a Ukrainian city with over 500,000 population between 2026-11-01 and 2026-11-08. | Two independent wire services report a Russian kinetic strike on a Ukrainian city with population over 500,000 between 2026-11-01 and 2026-11-08. |
| KKR-20261023-71 | 25% | 2026-11-09 | economics | The 10-year US Treasury yield closes below 4.80 on at least one weekday between 2026-11-02 and 2026-11-06. | The closing value of the 10-year US Treasury yield is below 4.80 on at least one trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261023-72 | 30% | 2026-11-10 | military | Russia conducts a kinetic strike on a Ukrainian city with over 500,000 population between 2026-11-01 and 2026-11-08. | Two independent wire services report a Russian kinetic strike on a Ukrainian city with population over 500,000 between 2026-11-01 and 2026-11-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-10-23 and 2026-10-30 for a vulnerability with CVSS score 9.0 or higher." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The S&P 500 closes above 7,800 on at least one weekday between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A new CVE with CVSS score 9.0 or higher is added to the CISA KEV catalog between 2026-11-01 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A magnitude 6.0 or greater earthquake is recorded by USGS in the Philippines between 2026-11-01 and 2026-11-08." → REJECTED: cited items name China; the claim is about Philippines — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4784 issued all-time across 21 forecaster arms · 3432 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 113 issued · 106 open · 7 resolved · 3 hits / 4 misses · **Brier 0.297** against its own base rate 42.9% (climatological 0.245) · **skill -0.215** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1679 | 1296 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 104 | 103 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 113 | 106 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 242 | 155 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*