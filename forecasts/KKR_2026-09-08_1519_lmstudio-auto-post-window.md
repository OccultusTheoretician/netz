**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 8 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-01 | 25% | 2026-10-07 | economics/markets | Between 2026-09-22 and 2026-09-25, Brent crude oil exceeds $100 per barrel at the close of a trading day on a major exchange (e.g., ICE Futures Europe). | The ICE Futures Europe settlement price for Brent crude oil futures on any trading day between 2026-09-22 and 2026-09-25 is equal to or greater than $100.00 per barrel. |
| KKR-20260908-02 | 15% | 2026-10-08 | cyber | Between 2026-09-23 and 2026-09-30, the CISA KEV catalog adds at least one new vulnerability with a CVSS score of 9.0 or higher that is actively exploited in the wild. | The CISA KEV catalog carries a date-added value between 2026-09-23 and 2026-09-30 for a vulnerability with a CVSS score of 9.0 or higher and a 'Status' of 'Exploited in the Wild'. |
| KKR-20260908-03 | 10% | 2026-10-09 | disaster | Between 2026-09-24 and 2026-10-01, a major earthquake of magnitude 6.0 or higher occurs in the Pacific Northwest region (Washington, Oregon, or Northern California). | The USGS Significant Quakes feed records an earthquake with magnitude ≥6.0 and location within the Pacific Northwest (latitude 39.0-49.0, longitude -124.0 to -116.0) between 2026-09-24 and 2026-10-01. |
| KKR-20260908-04 | 20% | 2026-10-10 | political | Between 2026-09-25 and 2026-10-02, a new political scandal involving a U.S. federal official is confirmed by at least two independent news outlets (e.g., Guardian, BBC, Al Jazeera) and results in a formal investigation by a congressional committee. | At least two independent news outlets (Guardian World, BBC World, Al Jazeera) report a new political scandal involving a U.S. federal official, and a U.S. congressional committee publicly announces a formal investigation into the matter between 2026-09-25 and 2026-10-02. |
| KKR-20260908-05 | 5% | 2026-10-12 | military/conflict | Between 2026-09-27 and 2026-10-04, a new ceasefire agreement is signed between Israel and Hamas, verified by at least two neutral international bodies (e.g., UN, Qatar, Egypt). | At least two neutral international organizations (e.g., UN, Qatar, Egypt) issue a public statement confirming the signing of a new ceasefire agreement between Israel and Hamas between 2026-09-27 and 2026-10-04. |
| KKR-20260908-06 | 12% | 2026-10-13 | disaster | Between 2026-09-28 and 2026-10-05, a major wildfire in Australia burns over 100,000 hectares and is confirmed by the GDACS Alerts feed. | The GDACS Alerts feed records a wildfire event in Australia with a burned area of at least 100,000 hectares between 2026-09-28 and 2026-10-05. |
| KKR-20260908-07 | 22% | 2026-10-14 | economics/markets | Between 2026-09-29 and 2026-10-06, a new economic policy shift in Canada results in a 3% or greater increase in the Canadian dollar against the U.S. dollar at the close of a trading day. | The exchange rate for the Canadian dollar (CAD) against the U.S. dollar (USD) reaches or exceeds 1.4000 at the close of any trading day between 2026-09-29 and 2026-10-06. |
| KKR-20260908-08 | 8% | 2026-10-15 | crime/security | Between 2026-09-30 and 2026-10-07, a new criminal indictment is issued by a U.S. federal court against a high-profile political figure, confirmed by a public docket entry in the PACER system. | A public docket entry in the PACER system (https://pacer.uscourts.gov) confirms a new criminal indictment against a U.S. federal political figure between 2026-09-30 and 2026-10-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, at least one drone strike targeting Kyiv is confirmed by two or more independently biased sources (RU, UA" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-26 and 2026-10-03, a cyberattack targeting a U.S. federal agency results in the public exposure of at least 1 million sensit" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

1686 issued all-time across 16 forecaster arms · 1421 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 235 issued · 147 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 512 | 484 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 235 | 147 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 180 | 178 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 199 | 193 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 187 | 166 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*