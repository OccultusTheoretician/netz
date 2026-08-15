**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 150533Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-14_1517.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260815-11 | 33% | 2026-11-17 | cyber | The CISA KEV catalog adds at least one VMware vCenter Server entry, listed under vendorProject VMware or Broadcom, with a dateAdded value between 2026-08-17 and 2026-11-13. | TRUE if a KEV entry naming VMware vCenter Server in its product field carries a dateAdded between 2026-08-17 and 2026-11-13 inclusive. |
| KKR-20260815-12 | 18% | 2027-01-05 | economics | The FRED series DGS10 records a daily value at or above 5.00 percent on at least one business day between 2026-08-17 and 2026-12-31. | TRUE if any non-missing DGS10 observation dated inside the window is 5.00 or greater as published in the FRED series. |
| KKR-20260815-13 | 33% | 2026-10-19 | military_conflict | A NATO member state formally requests Article 4 consultations between 2026-08-17 and 2026-10-15. | TRUE if NATO publishes a statement confirming Article 4 consultations were invoked, and Reuters and the Associated Press both report the request, dated inside the window. |
| KKR-20260815-14 | 33% | 2027-01-05 | political | The UK Electoral Commission publishes a concluded investigation outcome naming Reform UK on its enforcement register between 2026-08-17 and 2026-12-31. | TRUE if the Electoral Commission enforcement outcomes register carries an entry naming Reform UK with a published date inside the window. |
| KKR-20260815-15 | 33% | 2026-12-18 | disaster | The World Health Organization declares the Democratic Republic of the Congo Ebola outbreak a Public Health Emergency of International Concern between 2026-08-17 and 2026-12-15. | TRUE if WHO publishes an IHR Emergency Committee statement or Director-General declaration designating this outbreak a PHEIC, dated inside the window. |
| KKR-20260815-16 | 33% | 2026-12-04 | crime_security | Luigi Mangione enters a guilty plea to at least one count in the New York state prosecution between 2026-08-17 and 2026-11-30. | TRUE if the New York state court docket in that prosecution records a guilty plea entered by the defendant on a date inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

616 issued all-time across 14 forecaster arms · 560 open (34 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 113 issued · 113 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 113 | 113 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 70 | 68 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 35 | 35 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 55 | 55 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*