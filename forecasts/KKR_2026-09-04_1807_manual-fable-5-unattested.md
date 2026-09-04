**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041807Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: manual/fable-5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-31 | 85% | 2026-09-22 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium V8 entry with a dateAdded value between 2026-09-04 and 2026-09-18. | Fetch the CISA KEV JSON at the deadline; TRUE if any entry lists vendorProject Google, a product containing Chrome or Chromium V8, and dateAdded between 2026-09-04 and 2026-09-18. |
| KKR-20260904-32 | 30% | 2026-09-29 | cyber | The CISA KEV catalog adds at least one entry with vendorProject CrowdStrike and a dateAdded value between 2026-09-04 and 2026-09-25, following the reported FalconFlank SYSTEM privilege zero-day. | Fetch the CISA KEV JSON at the deadline; TRUE if any entry lists vendorProject CrowdStrike with dateAdded between 2026-09-04 and 2026-09-25; the entry need not be named FalconFlank. |
| KKR-20260904-33 | 40% | 2026-11-04 | economics/markets | The 10-year US Treasury constant maturity yield prints at or above 5.00 percent on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.78 percent on the packet date. | TRUE if FRED series DGS10 records a value of 5.00 or higher for any date between 2026-09-08 and 2026-10-30. Reference: 4.78 at seal. |
| KKR-20260904-34 | 12% | 2026-10-20 | military/conflict | The governments of Russia and Ukraine both announce a ceasefire or a mutual halt of long-range strikes with an effective date between 2026-09-05 and 2026-10-16. | TRUE if Reuters and AP each carry statements from both the Kremlin and the Ukrainian presidential office confirming the same ceasefire or strike-halt agreement effective within the window. |
| KKR-20260904-35 | 60% | 2026-10-06 | disaster | The USGS ComCat catalog records at least one earthquake of magnitude 5.0 or greater within 150 km of the 2026-09-04 M6.3 epicenter near Nikolski, Alaska, with origin time between 2026-09-05 and 2026-10-02. | TRUE if a ComCat query centered on the M6.3 event coordinates, radius 150 km, minimum magnitude 5.0, returns at least one event with origin time inside the window. |
| KKR-20260904-36 | 25% | 2026-10-20 | political | Argentina publishes in the Boletin Oficial a decree or resolution imposing sanctions or restrictive economic measures aimed at the Falkland Islands, companies operating there, or UK entities over the islands, dated between 2026-09-05 and 2026-10-16. | TRUE if the Boletin Oficial de la Republica Argentina carries such an instrument with publication date inside the window; verbal threats without a published instrument do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Front-month NYMEX WTI crude settles at or above 95.00 dollars per barrel on at least one trading day between 2026-09-08 and 2026-10-02. Refe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…official cme daily settlement | or | the eia daily spot…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "UKMTO publishes at least one incident notice of a vessel attacked, struck by a weapon, or subjected to attempted boarding in the Red Sea, Ba" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Alternative fuer Deutschland receives the largest party-list vote share in the Saxony-Anhalt state election held on 2026-09-06." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Philippine Vice President Sara Duterte is taken into custody, surrenders to a court, or posts bail on the arrest order over threats against " → REJECTED: the resolution names a different subject than the statement — the claim is about Duterte, Marcos, Philippine, President and the resolution settles on AFP, AP, Rappler, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1440 issued all-time across 16 forecaster arms · 1175 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 159 issued · 157 open · 2 resolved · 2 hits / 0 misses · **Brier 0.225** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 174 | 168 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*