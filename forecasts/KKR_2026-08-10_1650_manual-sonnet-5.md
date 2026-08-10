**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101650Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-10_1516.md · forecaster: manual/sonnet-5 · 10 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260810-21 | 60% | 2026-08-26 | cyber | The CISA Known Exploited Vulnerabilities (KEV) catalog will add an entry for a SonicWall SMA1000 vulnerability with a dateAdded value between 2026-08-10 and 2026-08-24. | TRUE if the CISA KEV catalog lists a SonicWall SMA1000 CVE with dateAdded between 2026-08-10 and 2026-08-24 inclusive, checked as of 2026-08-26; FALSE otherwise. |
| KKR-20260810-22 | 30% | 2026-09-02 | military_conflict | Iran will seize, board, or fire upon a commercial vessel transiting the Strait of Hormuz between 2026-08-17 and 2026-08-31. | TRUE if UKMTO, the US Fifth Fleet or IMSC, Reuters, or AP report an Iranian seizure, boarding, or attack on a commercial vessel in the Strait of Hormuz between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-23 | 33% | 2026-09-02 | economic | WTI crude oil NYMEX front-month settlement price will close at or above 85.00 USD per barrel on at least one trading day between 2026-08-17 and 2026-08-31. | TRUE if any CME/NYMEX WTI front-month settlement between 2026-08-17 and 2026-08-31 is 85.00 USD/bbl or higher; FALSE if all settlements in that span stay below 85.00. |
| KKR-20260810-24 | 47% | 2026-09-02 | military_conflict | Ukraine will conduct a further confirmed drone or missile strike on an oil refinery or energy facility in Tatarstan, Bashkortostan, or Samara Oblast between 2026-08-17 and 2026-08-31. | TRUE if Reuters, AP, RFE/RL, or the Institute for the Study of War report a Ukrainian strike on a refinery or energy facility in Tatarstan, Bashkortostan, or Samara Oblast between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-25 | 45% | 2026-09-02 | crime_security | An Irish court will issue a bail ruling, either granting or denying bail, for Daniel Kinahan between 2026-08-17 and 2026-08-31. | TRUE if RTE, the Irish Times, or BBC report an Irish court bail ruling, grant or denial, for Daniel Kinahan issued between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-26 | 18% | 2026-09-02 | political | The Israeli government will publicly announce acceptance, in full or amended form, of the Trump-backed 15-point Gaza plan it rejected around 2026-08-10, between 2026-08-17 and 2026-08-31. | TRUE if Reuters, AP, Times of Israel, or Haaretz report an Israeli government statement accepting the 15-point plan, in full or amended form, issued between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-27 | 40% | 2026-08-19 | disaster_infrastructure | The confirmed death toll from the 2026-08-10 M7.4 earthquake in western Colombia will reach 50 or more, as reported by Colombia UNGRD, Reuters, or AP, at any point between 2026-08-10 and 2026-08-17. | TRUE if Colombia UNGRD, Reuters, or AP report a cumulative confirmed toll of 50 or more for the 2026-08-10 western Colombia earthquake between 2026-08-10 and 2026-08-17; FALSE if it stays below 50. |
| KKR-20260810-28 | 32% | 2026-09-02 | cyber | LexisNexis will publicly confirm that consumer or customer personal data was accessed or exfiltrated in the server incident disclosed around 2026-08-10, via an SEC filing, a state attorney general breach-notification portal, or a company statement, between 2026-08-17 and 2026-08-31. | TRUE if LexisNexis, a state attorney general breach-notification filing, or an SEC EDGAR filing confirms personal data was accessed or exfiltrated in this incident, with that confirmation occurring between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-29 | 58% | 2026-09-02 | economic | Intel Corporation will price and close the 15 billion USD stock offering referenced in reporting on 2026-08-10, as confirmed by an SEC EDGAR filing, between 2026-08-17 and 2026-08-31. | TRUE if Intel files an SEC EDGAR Form 424B or 8-K confirming pricing and closing of the referenced stock offering between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260810-30 | 42% | 2027-02-03 | political | Ofcom will publish a decision, either finding a breach or clearing GB News, regarding the guest remarks on pride and paedophilia referenced in reporting on 2026-08-10, between 2026-10-01 and 2027-01-31. | TRUE if an Ofcom Broadcast and On Demand Bulletin decision on this complaint or segment is published between 2026-10-01 and 2027-01-31; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

450 issued all-time across 14 forecaster arms · 398 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5`:** 45 issued · 43 open · 2 resolved · 1 hits / 1 misses · **Brier 0.265** against its own base rate 50.0% (climatological 0.250) · **skill -0.060** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 44 | 42 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*