**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-08_1518.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260908-09 | 25% | 2027-02-28 | cyber | Between 2026-09-22 and 2026-09-25, a cyberattack exploiting the Adobe Magento zero-day vulnerability (CVE-2026-XXXX) is confirmed to have compromised at least 500 servers in the United States, as documented in the CISA KEV catalog with a date-added value between 2026-09-22 and 2026-09-25. | The CISA KEV catalog carries a record with a date-added value between 2026-09-22 and 2026-09-25, listing the vulnerability as actively exploited in the United States, with a confirmed impact on at least 500 servers. |
| KKR-20260908-10 | 15% | 2027-02-27 | disaster | Between 2026-09-24 and 2026-09-27, a major earthquake of magnitude 6.5 or higher occurs in the Pacific Northwest, confirmed by the USGS Significant Quakes feed with a location within 100 km of Seattle, Washington. | The USGS Significant Quakes feed carries a report with a magnitude of 6.5 or higher and a location within 100 km of Seattle, Washington, with a timestamp between 2026-09-24 and 2026-09-27. |
| KKR-20260908-11 | 20% | 2027-02-25 | political | Between 2026-09-25 and 2026-09-28, the Iranian Foreign Ministry issues a formal statement declaring a new diplomatic initiative to reopen the Strait of Hormuz unconditionally, confirmed by two independent sources (one from AXIS, one from WEST) with identical wording and timestamp. | Two independently biased sources (one from AXIS, one from WEST) publish a statement from the Iranian Foreign Ministry on the same date, declaring a new diplomatic initiative to reopen the Strait of Hormuz unconditionally, with identical wording and timestamp. |
| KKR-20260908-12 | 18% | 2027-03-05 | cyber | Between 2026-09-26 and 2026-09-29, a coordinated cyberattack on U.S. federal agencies exploits the SAP OVERPASS kernel vulnerability (CVE-2026-XXXX), resulting in at least one confirmed breach of a classified system, as reported in the CISA KEV catalog with a date-added value between 2026-09-26 and 2026-09-29. | The CISA KEV catalog carries a record with a date-added value between 2026-09-26 and 2026-09-29, listing the SAP OVERPASS kernel vulnerability as actively exploited in a U.S. federal agency, with a confirmed breach of a classified system. |
| KKR-20260908-13 | 40% | 2027-02-26 | political | Between 2026-09-27 and 2026-09-30, a new wave of political protests erupts in the West Bank, leading to the arrest of at least 150 individuals by Israeli security forces, confirmed by two independent news outlets (one from IL, one from PS) reporting the event with a specific date and number. | Two independently biased outlets (one from IL, one from PS) publish a report on the same date, confirming that at least 150 individuals were arrested by Israeli security forces in the West Bank during a new wave of political protests between 2026-09-27 and 2026-09-30. |
| KKR-20260908-14 | 22% | 2027-02-28 | disaster | Between 2026-09-28 and 2026-10-01, a major wildfire breaks out in the Australian state of Victoria, confirmed by the GDACS Alerts feed with a green alert issued for the region and a reported area burned exceeding 10,000 hectares. | The GDACS Alerts feed carries a green alert for a wildfire in Victoria, Australia, with a reported area burned exceeding 10,000 hectares, issued between 2026-09-28 and 2026-10-01. |
| KKR-20260908-15 | 38% | 2027-03-06 | economics/markets | Between 2026-09-29 and 2026-10-02, a new round of sanctions is imposed by the United States on Iranian airlines, confirmed by a press release from the U.S. Department of the Treasury with a timestamp between 2026-09-29 and 2026-10-02. | The U.S. Department of the Treasury issues a press release with a timestamp between 2026-09-29 and 2026-10-02, imposing new sanctions on Iranian airlines. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, a drone strike originating from the Russia-Ukraine Theatre hits a civilian infrastructure target in Kyiv," → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | a public…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-23 and 2026-09-26, Brent crude oil futures settle above $105 per barrel on the ICE Futures exchange, confirmed by the final " → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-09-30 and 2026-10-03, a cyberattack on a major U.S. financial institution uses AI-powered credential theft frameworks, resultin" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1693 issued all-time across 16 forecaster arms · 1428 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 32 issued · 32 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
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