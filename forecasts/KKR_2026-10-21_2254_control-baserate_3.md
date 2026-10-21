**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212254Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-21_1512.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261021-52 | 60% | 2026-10-30 | economics/markets | At the conclusion of its meeting on 2026-10-27 to 2026-10-28, the Federal Open Market Committee raises the federal funds target range above 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on 2026-10-21. | The FOMC policy statement released 2026-10-28 on federalreserve.gov sets a target range with an upper bound above 4.00 percent. |
| KKR-20261021-53 | 42% | 2026-11-02 | disaster | The eastern Pacific tropical cyclone listed by GDACS as TWENTY-TWO-E-26 (event TC 1001341), under any name NHC later assigns, is rated Category 3 or stronger (maximum sustained winds of at least 115 mph) in an NHC advisory issued between 2026-10-22 and 2026-10-29. | An NHC advisory issued from 2026-10-22 through 2026-10-29 for the system GDACS lists as TC 1001341 gives maximum sustained winds of at least 115 mph, or NHC best-track data confirm 100 knots or higher in that period. |
| KKR-20261021-54 | 46% | 2026-11-06 | cyber | CISA adds a vulnerability in PHP itself to its Known Exploited Vulnerabilities catalog with a date added between 2026-10-22 and 2026-11-04. | The CISA KEV catalog JSON contains an entry whose vendorProject is PHP Group or whose product is PHP, with a dateAdded value from 2026-10-22 through 2026-11-04. |
| KKR-20261021-55 | 66% | 2026-11-23 | military/conflict | US military forces carry out at least one airstrike or missile strike on Houthi targets inside Yemen between 2026-10-22 and 2026-11-19. | CENTCOM or the Pentagon confirms a US strike on Houthi targets in Yemen between 2026-10-22 and 2026-11-19, or Reuters and the Associated Press both report US forces conducted one in that period. |
| KKR-20261021-56 | 42% | 2026-12-04 | political | Candidates of the Democratic Party win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03. | Associated Press race calls or certified state results, counted as of 2026-12-04, show Democratic candidates winning at least 218 House seats in the 2026-11-03 general election. |
| KKR-20261021-57 | 36% | 2026-12-22 | crime/security | The man charged over the 2026-10-19 vehicle attack on Australian MP Helen Haines is charged with a terrorism offence under Part 5.3 of the Criminal Code Act 1995 between 2026-10-22 and 2026-12-18. | AFP, Victoria Police or the Commonwealth Director of Public Prosecutions announces a terrorism charge under Part 5.3 of the Criminal Code Act 1995 against the accused in the Haines attack, dated 2026-10-22 through 2026-12-18. |
| KKR-20261021-58 | 66% | 2027-01-05 | military/conflict | Donald Trump and Vladimir Putin meet face to face, in a bilateral or multilateral setting, between 2026-10-22 and 2026-12-31. | The Associated Press and Reuters both report that Trump and Putin met face to face on a date from 2026-10-22 through 2026-12-31; phone calls, video calls and envoy meetings do not count. |
| KKR-20261021-59 | 42% | 2027-01-05 | political | The sitting Prime Minister of France ceases to hold office, through a censure motion, a lost confidence vote or resignation, even if later reappointed, between 2026-10-22 and 2026-12-31. | The Journal Officiel publishes a decree ending the functions of the Prime Minister who held office on 2026-10-21, or Assemblee nationale scrutin records show a censure motion adopted, dated 2026-10-22 through 2026-12-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-24 and 2026-10-27, at the ESMO 2026 Congress (Presidential Symposium scheduled for 2026-10-24), Merck and Moderna report an " → REJECTED: resolution offers alternative VENUES joined by 'or' (…merck | or | moderna…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The 10-year US Treasury constant maturity yield for 2026-11-13 is above 5.30 percent. Reference: 5.11 percent in the packet market snapshot," → REJECTED: event window opens 2026-10-20, before this row is sealed (2026-10-21, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

4690 issued all-time across 21 forecaster arms · 3338 open (544 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1657 issued · 1274 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1657 | 1274 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 453 | 212 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 92 | 91 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 91 | 91 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 100 | 93 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 236 | 149 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 406 | 325 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 237 | 226 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 189 | 186 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*