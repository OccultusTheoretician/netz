**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-19_1513.md · forecaster: lmstudio/qwen36 · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261019-03 | 30% | 2026-11-04 | cyber | The CISA KEV catalog carries a date-added value for a critical NGINX vulnerability between 2026-10-26 and 2026-11-02. | The CISA KEV catalog entry for the NGINX vulnerability has a date_added value falling within the event window. |
| KKR-20261019-04 | 15% | 2026-11-10 | disaster | A magnitude 6.0 or greater earthquake occurs in Vanuatu between 2026-11-01 and 2026-11-08. | The USGS catalog records an earthquake with magnitude 6.0 or greater in Vanuatu with an origin time between 2026-11-01 and 2026-11-08. |
| KKR-20261019-05 | 20% | 2026-11-10 | political | The Australian government announces a formal inquiry into the death of the critically injured MP Helen Haines between 2026-11-01 and 2026-11-08. | The Australian Federal Parliament or a state legislative body publishes a notice or motion formally establishing an inquiry into the death of MP Helen Haines between 2026-11-01 and 2026-11-08. |
| KKR-20261019-06 | 40% | 2026-11-10 | cyber | A new CVE is assigned to a critical vulnerability in Microsoft Windows Server between 2026-11-01 and 2026-11-08. | The NVD database records a new CVE entry for a critical vulnerability in Microsoft Windows Server with a date_added value between 2026-11-01 and 2026-11-08. |
| KKR-20261019-07 | 35% | 2026-11-10 | military/conflict | A Houthi strike kills at least 10 people in a populated area of Yemen between 2026-11-01 and 2026-11-08. | Two independent wire services report a Houthi strike in a populated area of Yemen between 2026-11-01 and 2026-11-08 resulting in at least 10 fatalities. |
| KKR-20261019-08 | 45% | 2026-11-10 | cyber | A new CVE is assigned to a critical vulnerability in Broadcom Wi-Fi products between 2026-11-01 and 2026-11-08. | The NVD database records a new CVE entry for a critical vulnerability in Broadcom Wi-Fi products with a date_added value between 2026-11-01 and 2026-11-08. |
| KKR-20261019-09 | 10% | 2026-11-10 | disaster | A magnitude 7.0 or greater earthquake occurs in Indonesia between 2026-11-01 and 2026-11-08. | The USGS catalog records an earthquake with magnitude 7.0 or greater in Indonesia with an origin time between 2026-11-01 and 2026-11-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes above 100.00 USD per barrel on at least one session between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The European Central Bank cuts its main refinancing rate by at least 25 basis points between 2026-11-01 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The US Federal Reserve raises the target federal funds rate by at least 25 basis points between 2026-11-01 and 2026-11-08." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4490 issued all-time across 21 forecaster arms · 3138 open (313 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 88 issued · 87 open · 1 resolved · 1 hits / 0 misses · **Brier 0.722** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1580 | 1197 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 445 | 204 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 79 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 231 | 144 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 378 | 297 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 212 | 201 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 165 | 162 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*