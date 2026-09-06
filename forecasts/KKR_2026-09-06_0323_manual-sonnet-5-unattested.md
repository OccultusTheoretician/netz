**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060323Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-01 | 38% | 2026-09-22 | military_conflict | Cumulative fatalities from the Yemen government-Houthi fighting referenced in the 2026-09-05 packet (ground combat, missile strikes) exceed 100 people, tallied at any point between 2026-09-06 and 2026-09-20. | TRUE if at least two of Reuters, AP, Al Jazeera, or BBC report a cumulative Yemen fatality count above 100 for this conflict phase between 2026-09-06 and 2026-09-20, confirmed as of 2026-09-22; FALSE otherwise. |
| KKR-20260906-02 | 9% | 2026-10-19 | military_conflict | Russia and Ukraine, or their authorized representatives, publicly announce a signed ceasefire or peace agreement covering the active front line, following the 2026-09-05 arrival of US envoys Witkoff and Kushner in Moscow, at any point between 2026-09-06 and 2026-10-15. | TRUE if at least two of Reuters, AP, BBC, or a joint Russian-Ukrainian government statement confirm a signed ceasefire between 2026-09-06 and 2026-10-15, confirmed as of 2026-10-19; FALSE otherwise. |
| KKR-20260906-03 | 52% | 2026-09-21 | cyber | The CISA Known Exploited Vulnerabilities catalog adds a new entry for a Citrix NetScaler authentication-bypass vulnerability, with a Date Added value between 2026-09-06 and 2026-09-19, following the 2026-09-04 BleepingComputer report of active exploitation. | TRUE if the CISA KEV catalog at cisa.gov lists a Citrix NetScaler authentication-bypass CVE with a Date Added value in that window, checked as of 2026-09-21; FALSE otherwise. |
| KKR-20260906-04 | 8% | 2026-11-02 | political | Pete Hegseth leaves his Pentagon leadership role (resignation, removal, or reassignment), following the criticism referenced in the 2026-09-05 Guardian report, at any point between 2026-09-06 and 2026-10-31. | TRUE if at least two of AP, Reuters, or BBC report that Hegseth has left his Pentagon leadership post between 2026-09-06 and 2026-10-31, confirmed as of 2026-11-02; FALSE otherwise. |
| KKR-20260906-05 | 68% | 2026-12-07 | crime_security | Prosecutors formally move to retry Lindsay Clancy, or a court schedules a retrial date, following the mistrial declared per the 2026-09-04 and 2026-09-05 reporting, at any point between 2026-09-06 and 2026-12-05. | TRUE if at least one of Guardian or BBC reports that prosecutors have moved to retry Lindsay Clancy or that a retrial date is set, dated between 2026-09-06 and 2026-12-05, confirmed as of 2026-12-07; FALSE otherwise. |
| KKR-20260906-06 | 13% | 2026-09-21 | disaster_infrastructure | GDACS raises its alert level for Tropical Cyclone TWENTYTHREE-26 (event ID 1001319) from Green to Orange or Red before the system dissipates, at any point between 2026-09-06 and 2026-09-19. Reference: Green alert as of 2026-09-04. | TRUE if the GDACS event page for event ID 1001319 shows an Orange or Red alert level at any point between 2026-09-06 and 2026-09-19, checked as of 2026-09-21; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Iran or an Iran-aligned proxy force conducts an attack against a US military vessel, base, or personnel in the Middle East (Persian Gulf, St" → REJECTED: the resolution names only a venue or register (AP, BBC, CENTCOM, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI crude oil (Nymex front-month futures) settles at or above 100.00 USD per barrel at close on 2026-09-25, a Friday. Reference: 91.48 USD c" → REJECTED: event window opens 2026-09-04, before this row is sealed (2026-09-05, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The S&P 500 index closes below 7500.00 at settlement on 2026-09-30, a Wednesday. Reference: 7718.60 close on 2026-09-04 (plus 0.09 percent d" → REJECTED: event window opens 2026-09-04, before this row is sealed (2026-09-05, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names only a venue or register (Bloomberg, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A cybersecurity outlet reports the number of ClickFix-payload-hosting compromised websites in the blockchain-hosted campaign has grown to ex" → REJECTED: the resolution names a different subject than the statement — the claim is about ClickFix, Reference and the resolution settles on BleepingComputer, Hacker, News. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1497 issued all-time across 16 forecaster arms · 1232 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 173 issued · 152 open · 21 resolved · 10 hits / 11 misses · **Brier 0.214** against its own base rate 47.6% (climatological 0.249) · **skill +0.141** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 431 | 403 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 173 | 152 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*