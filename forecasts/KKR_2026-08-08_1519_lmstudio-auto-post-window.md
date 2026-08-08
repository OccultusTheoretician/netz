**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 081519Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-08_1517.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260808-01 | 30% | 2026-08-26 | military/conflict | Between 2026-08-21 and 2026-08-24, a drone attack using a Shahed-type UAV will be confirmed by at least two independently biased sources (one from RU, one from UA) targeting a civilian infrastructure site in Donetsk, Ukraine, resulting in at least one structural damage report. | The CISA KEV catalog does not carry a date-added value between 2026-08-21 and 2026-08-24 for a vulnerability exploited in a drone attack on a civilian infrastructure site in Donetsk, Ukraine, and no two independently biased sources (one from RU, one from UA) corroborate a drone attack with structural damage during that window. |
| KKR-20260808-02 | 15% | 2026-09-04 | disaster | Between 2026-08-24 and 2026-08-31, a major earthquake of magnitude 6.0 or higher will occur in the United States, as recorded by the USGS Significant Quakes feed. | The USGS Significant Quakes feed records a magnitude 6.0 or higher earthquake in the United States between 2026-08-24 and 2026-08-31. |
| KKR-20260808-03 | 85% | 2026-09-05 | political | Between 2026-08-25 and 2026-08-31, the US Senate will pass a resolution to confirm Todd Blanche as Attorney General, as recorded in the official Congressional Record. | The Congressional Record contains a formal vote confirming Todd Blanche as Attorney General of the United States between 2026-08-25 and 2026-08-31. |
| KKR-20260808-04 | 20% | 2026-09-07 | disaster | Between 2026-08-27 and 2026-09-03, a new wildfire will be reported in the United States by the GDACS Alerts feed, with a confirmed area burned exceeding 10,000 acres. | The GDACS Alerts feed records a new wildfire in the United States between 2026-08-27 and 2026-09-03 with a confirmed area burned exceeding 10,000 acres. |
| KKR-20260808-05 | 18% | 2026-09-08 | cyber | Between 2026-08-28 and 2026-09-04, a coordinated cyberattack targeting at least three financial institutions in Europe will be confirmed by two independent cybersecurity sources, resulting in data exfiltration. | Two independent cybersecurity sources confirm a coordinated cyberattack targeting at least three financial institutions in Europe between 2026-08-28 and 2026-09-04, resulting in data exfiltration. |
| KKR-20260808-06 | 28% | 2026-09-09 | political | Between 2026-08-29 and 2026-09-05, a new political scandal involving a US senator will be reported by two major wire services (e.g., Reuters, AP), with allegations of corruption or misuse of funds. | Two major wire services (e.g., Reuters, AP) report a new political scandal involving a US senator between 2026-08-29 and 2026-09-05, with allegations of corruption or misuse of funds. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-22 and 2026-08-28, the S&P 500 index will close above 7,800 on at least one trading day, based on the official NYSE closing " → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-08-23 and 2026-08-30, a zero-day vulnerability in Metabase will be exploited in the wild, resulting in unauthorized access to a" → REJECTED: the resolution names a different subject than the statement — the claim is about Metabase and the resolution settles on CISA, KEV. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-26 and 2026-09-02, a cyberattack exploiting CVE-2026-8037 in Progress LoadMaster will be confirmed by at least two independe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…government | or | critical infrastructure…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-8037 dateAdded 2026-08-07, before the claimed window 2026-08-26..2026-09-02; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-30 and 2026-09-06, a major cyberattack on a US state government system will be confirmed by two independent sources, resulti" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

385 issued all-time across 14 forecaster arms · 335 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 33 issued · 31 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 33 | 31 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 20 | 32 | 9 | 23 | 0.221 | 28.1% | 0.202 | -0.093 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 23 | 21 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*