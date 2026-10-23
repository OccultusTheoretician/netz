**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: lmstudio/qwen36-abliterated · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261022-17 | 30% | 2026-11-23 | economics | WTI Crude closes below 95.00 on at least one trading day between 2026-11-16 and 2026-11-20. | Reference: 98.51 on 2026-10-26. WTI Crude closes below 95.00 on at least one trading day between 2026-11-16 and 2026-11-20. |
| KKR-20261022-18 | 65% | 2026-12-01 | disaster | A magnitude 6.0 or greater earthquake occurs in the Pacific Ring of Fire between 2026-11-22 and 2026-11-29. | The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in the Pacific Ring of Fire between 2026-11-22 and 2026-11-29. |
| KKR-20261022-19 | 45% | 2026-12-16 | economics | The S&P 500 closes above 7,800 on at least one trading day between 2026-12-07 and 2026-12-14. | Reference: 7,654.93 on 2026-10-26. The S&P 500 closes above 7,800 on at least one trading day between 2026-12-07 and 2026-12-14. |
| KKR-20261022-20 | 55% | 2026-12-24 | military | Russia launches a ballistic or cruise missile attack on Kyiv between 2026-12-15 and 2026-12-22. | Two hostile sides (RU, UA) report a Russian ballistic or cruise missile attack on Kyiv between 2026-12-15 and 2026-12-22. |
| KKR-20261022-21 | 10% | 2027-02-24 | disaster | A Category 3 or higher hurricane makes landfall in the United States between 2027-02-15 and 2027-02-22. | The National Hurricane Center records a Category 3 or higher hurricane making landfall in the United States between 2027-02-15 and 2027-02-22. |
| KKR-20261022-22 | 35% | 2027-03-10 | economics | The European Central Bank raises its main refinancing rate by at least 25 basis points between 2027-03-01 and 2027-03-08. | The European Central Bank raises its main refinancing rate by at least 25 basis points between 2027-03-01 and 2027-03-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog records a date-added value for the PHP2Shell vulnerability between 2026-11-01 and 2026-11-08." → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The US Senate confirms a Supreme Court nominee between 2027-01-05 and 2027-01-12." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major cyberattack disrupts US power grid operations between 2027-01-20 and 2027-01-27." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Gold closes above 4,200 on at least one trading day between 2027-02-01 and 2027-02-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4712 issued all-time across 21 forecaster arms · 3360 open (585 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-abliterated`:** 97 issued · 97 open · nothing resolved yet — this arm earns a score at its first resolution.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1657 | 1274 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 457 | 216 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*