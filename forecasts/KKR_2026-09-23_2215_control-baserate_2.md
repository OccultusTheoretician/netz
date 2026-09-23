**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232215Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-23_1518.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260923-37 | 48% | 2026-11-16 | economics | The US Treasury 10-year par yield closes at or above 5.25 percent on at least one business day between 2026-09-24 and 2026-11-13. Reference: 5.06 percent on the packet date, 2026-09-23. | TRUE if the Daily Treasury Par Yield Curve Rates series carries a 10-year value of 5.25 or greater on any business day dated 2026-09-24 through 2026-11-13 inclusive. |
| KKR-20260923-38 | 32% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one entry with vendorProject Google and a product value naming Chromium or Chrome, with a dateAdded value between 2026-09-24 and 2026-11-14. | TRUE if the CISA KEV JSON feed contains a vulnerability whose vendorProject is Google, whose product names Chromium or Chrome, and whose dateAdded falls between 2026-09-24 and 2026-11-14 inclusive. |
| KKR-20260923-39 | 32% | 2026-12-03 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least one entry with vendorProject Oracle and a product value naming PeopleSoft, with a dateAdded value between 2026-09-24 and 2026-11-30. | TRUE if the CISA KEV JSON feed contains a vulnerability whose vendorProject is Oracle, whose product names PeopleSoft, and whose dateAdded falls between 2026-09-24 and 2026-11-30 inclusive. |
| KKR-20260923-40 | 64% | 2026-11-18 | military_conflict | A reciprocal Russia-Ukraine halt on strikes against energy infrastructure takes effect between 2026-09-24 and 2026-11-15, with both governments confirming it. | TRUE if the Kremlin or Russian MFA and the Ukrainian Presidential Office each publicly confirm a reciprocal energy-strike moratorium in force with a start date between 2026-09-24 and 2026-11-15, carried by at least two of Reuters, AP, and AFP. |
| KKR-20260923-41 | 64% | 2026-12-03 | military_conflict | Ethiopia declares a state of emergency whose geographic scope includes the Tigray region, taking effect between 2026-09-24 and 2026-11-30. | TRUE if the Ethiopian Council of Ministers or the House of Peoples Representatives adopts a state of emergency naming Tigray within its scope, effective between 2026-09-24 and 2026-11-30, carried by at least two of Reuters, AP, AFP, and the BBC. |
| KKR-20260923-42 | 39% | 2026-11-24 | political | Direct US-Iran bilateral talks at foreign-minister level or above convene between 2026-09-24 and 2026-11-20, acknowledged by both governments. | TRUE if the US State Department or White House and the Iranian foreign ministry each confirm a direct bilateral meeting at or above foreign-minister level held between 2026-09-24 and 2026-11-20, carried by at least two of Reuters, AP, and AFP. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range to at least 4.00 to 4.25 percent at its scheduled decision on 2026-10-28. Reference: the rang" → REJECTED: event window opens 2026-09-16, before this row is sealed (2026-09-23, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Front-month NYMEX WTI crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-09-24 and 2026-10-30. Ref" → REJECTED: the resolution names a different subject than the statement — the claim is about Front, NYMEX, Reference, WTI and the resolution settles on CME, Group. A row whose resolution checks a different fact can be scored correct while being wrong
- "A US federal district court enters an order granting a temporary restraining order or preliminary injunction restoring White House press acc" → REJECTED: the resolution requires access, house, outlets, restoration, three, white and the failure condition does not mention them — an outcome missing them satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements
- "The National Weather Service issues at least one Coastal Flood Warning for a forecast zone in New York State or Massachusetts, with an issua" → REJECTED: the named venue is introduced by 'such as', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

2753 issued all-time across 16 forecaster arms · 2211 open (153 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 957 issued · 840 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 957 | 840 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 108 | 103 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 173 | 156 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 299 | 235 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*