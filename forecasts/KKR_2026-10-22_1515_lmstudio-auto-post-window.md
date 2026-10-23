**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-22_1513.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261022-01 | 30% | 2027-04-18 | cyber | Between 2026-10-23 and 2026-10-29, the CISA KEV catalog will include at least one new entry for a vulnerability with CVSS score 10.0 that enables unauthenticated remote code execution. | The CISA KEV catalog carries a date-added value between 2026-10-23 and 2026-10-29 for a vulnerability with CVSS score 10.0 and unauthenticated remote code execution capability. |
| KKR-20261022-02 | 32% | 2027-04-18 | disaster | Between 2026-10-29 and 2026-11-05, a tropical cyclone named JOSEPHINE-26 will cause a Category 3 or higher storm surge in a coastal region of the Indian Ocean, as confirmed by GDACS. | The GDACS Alerts system carries a Category 3 or higher storm surge event for tropical cyclone JOSEPHINE-26 in the Indian Ocean between 2026-10-29 and 2026-11-05. |
| KKR-20261022-03 | 20% | 2027-04-18 | disaster | Between 2026-10-30 and 2026-11-06, a magnitude 7.0 or greater earthquake will occur in the China-Tibet region, as confirmed by USGS. | The USGS Significant Quakes database records a magnitude 7.0 or greater earthquake in the China-Tibet region between 2026-10-30 and 2026-11-06. |
| KKR-20261022-04 | 18% | 2027-04-18 | crime/security | Between 2026-11-01 and 2026-11-08, a political assassination attempt will be confirmed against a sitting U.S. federal official, with at least two independent sources reporting the event. | At least two independent sources (e.g., BBC World, Al Jazeera, Guardian World) confirm a political assassination attempt against a sitting U.S. federal official between 2026-11-01 and 2026-11-08. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-24 and 2026-10-31, at least one major financial institution in the United States will report a data breach involving custome" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…wire service | or | regulatory…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-25 and 2026-11-01, the S&P 500 index will close below 7,500 on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-26 and 2026-11-02, the 10-year U.S. Treasury yield will exceed 5.25 percent on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-27 and 2026-11-03, a drone strike will be confirmed in Kyiv by at least two independently biased sources, with no casualties" → REJECTED: cited items name China, France, Virginia; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-10-28 and 2026-11-04, a missile attack will be confirmed in Moscow by at least two independently biased sources, with no casual" → REJECTED: cited items name Iran, Islamic Republic of, Israel, Virginia, zone:iran; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-10-31 and 2026-11-07, a cyberattack exploiting the Node.js Brotli Decoder Bug will result in a public outage of a major cloud s" → REJECTED: resolution offers alternative VENUES joined by 'or' (…otli decoder bug, confirmed by a wire service | or | official statement…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4694 issued all-time across 21 forecaster arms · 3342 open (585 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 457 issued · 216 open · 231 resolved · 70 hits / 161 misses · **Brier 0.211** against its own base rate 30.3% (climatological 0.211) · **skill -0.001**.

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
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 236 | 149 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
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