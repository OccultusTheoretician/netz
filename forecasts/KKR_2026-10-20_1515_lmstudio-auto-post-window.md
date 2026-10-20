**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-20_1513.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261020-01 | 35% | 2027-04-18 | cyber | Between 2026-10-21 and 2026-10-24, a cyberattack exploiting the ClickFix platform will be confirmed by at least two independent sources, resulting in a disruption to a major financial institution. | At least two independent sources, one from a Western outlet and one from a non-Western outlet, confirm a cyberattack exploiting the ClickFix platform between 2026-10-21 and 2026-10-24, resulting in a disruption to a major financial institution. |
| KKR-20261020-02 | 20% | 2027-04-18 | military/conflict | Between 2026-10-21 and 2026-10-24, a Houthi missile strike on a Yemeni military camp will result in at least 50 casualties, confirmed by both BBC World and Al Jazeera. | At least one report from BBC World and one from Al Jazeera, both published between 2026-10-21 and 2026-10-24, confirms a Houthi missile strike on a Yemeni military camp with at least 50 casualties. |
| KKR-20261020-03 | 15% | 2027-04-18 | disaster | Between 2026-10-21 and 2026-10-24, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in the Vanuatu region. | The USGS Significant Quakes database records an earthquake with magnitude 6.5 or higher and depth less than 50 km in the Vanuatu region between 2026-10-21 and 2026-10-24. |
| KKR-20261020-04 | 30% | 2027-04-18 | military/conflict | Between 2026-10-21 and 2026-10-24, the UK will deploy Typhoon fighter jets to Saudi Arabia, confirmed by both the UK Ministry of Defence and Al Jazeera. | At least one official statement from the UK Ministry of Defence and one report from Al Jazeera, both published between 2026-10-21 and 2026-10-24, confirm the deployment of Typhoon fighter jets to Saudi Arabia. |
| KKR-20261020-05 | 28% | 2027-04-18 | cyber | Between 2026-10-21 and 2026-10-24, a data breach affecting more than 1 million users will be confirmed by a major financial institution, with the breach linked to a compromised third-party vendor. | At least one report from a Western outlet and one from a non-Western outlet, both published between 2026-10-21 and 2026-10-24, confirm a data breach affecting more than 1 million users at a major financial institution, with the breach traced to a compromised third-party vendor. |
| KKR-20261020-06 | 22% | 2027-04-18 | political | Between 2026-10-21 and 2026-10-24, a political protest in France will result in the deployment of military forces, confirmed by both the French government and BBC World. | At least one official statement from the French government and one report from BBC World, both published between 2026-10-21 and 2026-10-24, confirm the deployment of military forces in France due to a political protest. |
| KKR-20261020-07 | 18% | 2027-04-18 | cyber | Between 2026-10-21 and 2026-10-24, a cyberattack on a US federal civilian agency will be confirmed by the DHS, resulting in a system outage lasting more than 24 hours. | The DHS issues a public statement between 2026-10-21 and 2026-10-24 confirming a cyberattack on a US federal civilian agency that resulted in a system outage lasting more than 24 hours. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in a critical infr" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-21 and 2026-10-24, a drone strike will be reported in Kyiv involving a F-35 aircraft, with at least one casualty confirmed b" → REJECTED: cited items name Botswana, France, United States; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, the S&P 500 will close below 7,650 points on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; market-price resolution with weekend deadline — no settlement exists that day

## III. LEDGER STANDING

4554 issued all-time across 21 forecaster arms · 3202 open (422 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 452 issued · 211 open · 231 resolved · 70 hits / 161 misses · **Brier 0.211** against its own base rate 30.3% (climatological 0.211) · **skill -0.001**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1603 | 1220 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 452 | 211 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 92 | 85 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 231 | 144 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 388 | 307 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 219 | 208 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 171 | 168 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*