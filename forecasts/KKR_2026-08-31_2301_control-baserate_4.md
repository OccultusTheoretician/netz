**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-31_1519.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-61 | 53% | 2026-10-05 | military_conflict | US Central Command announces at least one new strike on Iranian forces, vessels, or territory occurring between 2026-09-01 and 2026-09-30. | A CENTCOM release or two of Reuters, AP, BBC, Al Jazeera report a US strike on Iranian forces or territory dated between 2026-09-01 and 2026-09-30. |
| KKR-20260831-62 | 53% | 2026-10-20 | military_conflict | A US or Gulf state authority publicly reports a naval mine detected, struck, or cleared in the Strait of Hormuz or its approaches between 2026-09-01 and 2026-10-15. | CENTCOM, the US Navy, or a Gulf state navy states that a mine was found, struck, or cleared in the strait or its approaches within the window. |
| KKR-20260831-63 | 25% | 2026-10-13 | economic | Front-month ICE Brent futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-09. | ICE settlement data for the front-month Brent contract shows a settlement of 100.00 USD or higher on any trading day inside the window. |
| KKR-20260831-64 | 33% | 2026-11-03 | cyber | The CISA KEV catalog carries at least 30 entries with a dateAdded value between 2026-09-01 and 2026-10-30. | The CISA KEV JSON feed counts 30 or more entries whose dateAdded value falls between 2026-09-01 and 2026-10-30 inclusive. |
| KKR-20260831-65 | 33% | 2026-11-03 | cyber | The CISA KEV catalog carries at least one entry naming Cisco as vendorProject with a dateAdded value between 2026-09-01 and 2026-10-30. | The CISA KEV JSON feed contains an entry whose vendorProject is Cisco and whose dateAdded value falls inside that range. |
| KKR-20260831-66 | 52% | 2026-10-20 | disaster_infrastructure | The Nepal disaster authority puts the confirmed death toll from the August 2026 Nepal-Tibet floods at 1500 or more, at some point between 2026-09-01 and 2026-10-15. | An NDRRMA situation report or Nepal government figure dated inside the window states 1500 or more confirmed flood deaths in Nepal. |
| KKR-20260831-67 | 43% | 2026-10-20 | crime_security | German authorities name a suspect, announce an arrest, or announce a warrant in the Leipzig drone attack between 2026-09-01 and 2026-10-15. | The Generalbundesanwalt, the BKA, or Saxony police state that a suspect is named, arrested, or subject to a warrant in the Leipzig drone case within the window. |
| KKR-20260831-68 | 52% | 2026-11-04 | disaster_infrastructure | Ukrenergo or DTEK announces emergency or rolling power cuts affecting Kyiv city on at least one day between 2026-09-15 and 2026-10-31. | An Ukrenergo or DTEK notice dated inside the window states that emergency or rolling outage schedules apply to consumers in Kyiv city. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled 2026-09-16 decision, above the current 3.50 to 3.75 percent." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A lapse in federal appropriations begins 2026-10-01 because no measure funding agencies past 2026-09-30 is enacted." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-01 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1191 issued all-time across 14 forecaster arms · 1030 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 311 issued · 294 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 311 | 294 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 120 | 119 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 150 | 147 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 130 | 122 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*