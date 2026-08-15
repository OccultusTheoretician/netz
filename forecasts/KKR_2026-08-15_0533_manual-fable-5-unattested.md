**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 150533Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-14_1517.md · forecaster: manual/fable-5/unattested · 2 accepted / 8 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260815-01 | 30% | 2026-09-16 | disaster | The USGS ComCat catalog records at least one earthquake of magnitude 6.0 or greater with epicenter within 300 km of USGS event us6000tjl2 and origin time between 2026-08-15 and 2026-09-14. | A ComCat query on the deadline returns at least one M 6.0 or greater event meeting the distance and origin-time criteria. |
| KKR-20260815-02 | 20% | 2026-12-02 | disaster | The WHO Director-General declares the Democratic Republic of the Congo Ebola outbreak a Public Health Emergency of International Concern between 2026-08-15 and 2026-11-30. | A WHO announcement of a PHEIC determination for the DRC Ebola outbreak, published on who.int within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog adds an entry with vendorProject VMware and a product containing vCenter, with a dateAdded " → REJECTED: the resolution names a different subject than the statement — the claim is about CISA, Exploited, Known, VMware and the resolution settles on CISA, JSON, KEV. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-15 and 2026-10-15, Shell publicly confirms that data was stolen from it or a direct supplier in the incident tied to Clop th" → REJECTED: resolution offers alternative VENUES joined by 'or' (…shell statement | or | regulatory…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-08-15 and 2026-09-30, the armed forces or defence ministry of a NATO member state officially reports intercepting or shooting d" → REJECTED: resolution offers alternative VENUES joined by 'or' (…istry or armed forces confirming an intercept | or | downing in the window, carried by two named i…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Jared Kushner meets Benjamin Netanyahu in person in Israel between 2026-08-14 and 2026-08-31." → REJECTED: event window opens 2026-08-14, before this row is sealed (2026-08-15) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The Electoral Commission of Zambia officially declares a winner of the presidential election between 2026-08-14 and 2026-08-31." → REJECTED: event window opens 2026-08-14, before this row is sealed (2026-08-15) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names a different subject than the statement — the claim is about Commission, Electoral, Zambia and the resolution settles on AFP, AP, BBC, ECZ. A row whose resolution checks a different fact can be scored correct while being wrong
- "A guilty plea by Luigi Mangione is entered on the court record in his federal or New York state case between 2026-08-14 and 2026-10-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…sdny | or | new york state…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-14, before this row is sealed (2026-08-15) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The S&P 500 index closes below 7000 on at least one trading day between 2026-08-17 and 2027-01-29." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "ICE Brent front-month crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-08-17 and 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

602 issued all-time across 14 forecaster arms · 546 open (34 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 35 issued · 35 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 105 | 105 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 70 | 68 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 35 | 35 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 49 | 49 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*