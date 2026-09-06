**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062247Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-113 | 35% | 2026-10-05 | political | The official final result certified by the Landeswahlleiter of Saxony-Anhalt for the 2026-09-06 state election, certified between 2026-09-07 and 2026-09-30, allocates AfD at least 42 of the 83 Landtag seats. | TRUE if the amtliches Endergebnis published by the Landeswahlleiter Sachsen-Anhalt between 2026-09-07 and 2026-09-30 shows AfD holding 42 or more of 83 seats. Reference: 41 of 83 in the election-night projection. |
| KKR-20260906-114 | 30% | 2026-10-27 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry naming Adobe Commerce or Magento, with a dateAdded value between 2026-09-07 and 2026-10-23. | TRUE if the CISA KEV JSON feed contains a vulnerability whose vendorProject is Adobe and whose product string contains Commerce or Magento, with dateAdded falling between 2026-09-07 and 2026-10-23 inclusive. |
| KKR-20260906-115 | 30% | 2026-11-24 | cyber | The CISA KEV catalog adds an entry naming VMware Workstation or VMware Fusion with a dateAdded value between 2026-09-07 and 2026-11-20. | TRUE if the CISA KEV JSON feed contains a vulnerability whose product string contains Workstation or Fusion under a vendorProject of Broadcom or VMware, with dateAdded between 2026-09-07 and 2026-11-20 inclusive. |
| KKR-20260906-116 | 49% | 2026-12-16 | military_conflict | Russia and Ukraine jointly announce a signed general ceasefire or armistice covering the entire line of contact, agreed between 2026-09-07 and 2026-12-11. | TRUE if the Kremlin and the Ukrainian presidential office each confirm a signed general ceasefire covering the whole front, agreed in the window, and Reuters and AP both report the signing. |
| KKR-20260906-117 | 49% | 2026-10-21 | military_conflict | US and Iranian forces exchange at least one further direct kinetic strike on a vessel or maritime target in the Persian Gulf, Gulf of Oman, or Strait of Hormuz, occurring between 2026-09-07 and 2026-10-16. | TRUE if a strike in that window is reported by at least two of Reuters, AP, AFP, and BBC, and is acknowledged by either US Central Command or Iranian state media. |
| KKR-20260906-118 | 36% | 2026-10-16 | disaster_infrastructure | The USGS earthquake catalog lists at least one worldwide event of magnitude 7.0 or greater with an origin time between 2026-09-07 and 2026-10-11. | TRUE if a query of the USGS FDSN event service for magnitude 7.0 and above, origin time between 2026-09-07T00:00Z and 2026-10-11T23:59Z, returns one or more events. |
| KKR-20260906-119 | 36% | 2026-10-01 | crime_security | Victoria Police announce the arrest, charging, or confirmed death of the man sought over the alleged axe attack in Victoria, occurring between 2026-09-07 and 2026-09-27. | TRUE if a Victoria Police media release or court listing, reported by two of ABC News, The Age, and Guardian Australia, records the suspect arrested, charged, or confirmed deceased within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the upper bound of the federal funds target range above 3.75 percent at its scheduled meeting concluding 2026-09-16." → REJECTED: event window opens 2026-07-29, before this row is sealed (2026-09-06, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Front-month ICE Brent crude settles at or above USD 105.00 on at least one trading day between 2026-09-08 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The UK Electoral Commission publicly announces a formal investigation into Reform UK donations, opened between 2026-09-07 and 2026-11-06." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ectoral commission register of investigations | or | an official commission statement records a fo…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1610 issued all-time across 16 forecaster arms · 1345 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 484 issued · 456 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 484 | 456 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 224 | 136 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*