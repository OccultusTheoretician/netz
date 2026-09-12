**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121933Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: manual/opus-5/unattested · 4 accepted / 6 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-54 | 42% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field names Check Point, with a date-added value between 2026-09-14 and 2026-10-31. | TRUE if the CISA KEV catalog contains an entry whose vendorProject or product names Check Point with dateAdded between 2026-09-14 and 2026-10-31 inclusive. |
| KKR-20260912-55 | 65% | 2026-10-20 | military/conflict | Saudi Aramco or the Saudi energy ministry announces resumption of flows on the pipeline shut after the 2026-09-12 drone attack, with the announcement falling between 2026-09-14 and 2026-10-16. | TRUE if Reuters and at least one of BBC or Al Jazeera report an official Saudi announcement of resumed flows on that pipeline dated 2026-09-14 through 2026-10-16. |
| KKR-20260912-56 | 20% | 2026-11-24 | political | The UN Security Council adopts a resolution whose subject is Iran at a meeting held between 2026-09-14 and 2026-11-20. | TRUE if the UN Security Council resolutions register lists a resolution adopted 2026-09-14 through 2026-11-20 whose subject is Iran or the Iran nuclear file. |
| KKR-20260912-57 | 80% | 2026-10-27 | disaster | The USGS earthquake catalog records at least one magnitude 7.0 or greater earthquake worldwide with origin time between 2026-09-14 and 2026-10-24. | TRUE if a USGS ComCat query returns at least one event of magnitude 7.0 or greater with origin time between 2026-09-14 and 2026-10-24 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Front-month NYMEX WTI crude settles at or above 110.00 dollars per barrel on at least one trading day between 2026-09-14 and 2026-10-16. Ref" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The FRED series DGS10 records a value at or above 5.25 percent on at least one business day between 2026-09-14 and 2026-11-13. Reference: 4." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes below 7,200.00 on at least one trading day between 2026-09-14 and 2026-11-13. Reference: 7,656.98 on the packet date 2026" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Non-Houthi forces hold Mayun Island in the Bab al-Mandab strait at some point between 2026-09-14 and 2026-10-31." → REJECTED: cited items name Iran, Islamic Republic of; the claim is about zone:yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Either chamber of the US Congress records a roll call vote on a joint resolution invoking the War Powers Resolution with respect to Iran, he" → REJECTED: resolution offers alternative VENUES joined by 'or' (…recorded house | or | senate…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one of the six Nigerian nationals extradited to the United States over a 6 million dollar online romance scam enters a guilty plea " → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2008 issued all-time across 16 forecaster arms · 1672 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 230 issued · 224 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 645 | 607 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*