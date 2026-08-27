**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270428Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-25_1517.md · forecaster: control/baserate · 6 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-49 | 25% | 2026-12-02 | economic | The LBMA Gold Price PM auction fixes at or above 5000.00 dollars per troy ounce on at least one business day between 2026-09-01 and 2026-11-30. | TRUE if any LBMA Gold Price PM fix dated between 2026-09-01 and 2026-11-30 is 5000.00 dollars or higher in the published LBMA price record. |
| KKR-20260827-50 | 25% | 2026-12-03 | economic | The US Federal Register publishes a presidential document imposing or raising tariffs on Canadian-origin goods, with a publication date between 2026-08-26 and 2026-11-30. | TRUE if federalregister.gov returns a presidential document published inside that window whose operative text imposes or increases duties on goods of Canada. |
| KKR-20260827-51 | 29% | 2026-12-03 | political | OFAC adds at least one entity with a listed address in mainland China or Hong Kong to the SDN list under an Iran-related program between 2026-09-01 and 2026-11-30. | TRUE if an OFAC action inside that window designates an entity addressed in China or Hong Kong carrying an Iran-related program tag such as IRAN, IFSR, or IRGC. |
| KKR-20260827-52 | 50% | 2027-01-05 | military_conflict | A Russian presidential decree ordering a new partial or general mobilization is published on pravo.gov.ru with a signature date between 2026-09-01 and 2026-12-31. | TRUE if the official Russian legal portal pravo.gov.ru carries a presidential ukaz signed inside that window ordering mobilization of reservists beyond the standing conscription cycle. |
| KKR-20260827-53 | 50% | 2026-10-05 | military_conflict | At least four distinct Russian oil refineries are struck in drone attacks between 2026-09-01 and 2026-09-30, each acknowledged by a Russian regional governor, ministry, or federal agency. | TRUE if four or more separately named Russian refineries are reported hit inside that window with acknowledgment from a Russian governor, ministry, or Rosaviatsia statement. |
| KKR-20260827-54 | 31% | 2027-01-06 | crime_security | The US District Court for the District of Columbia docket in the Lockerbie bombing prosecution carries an order setting a new trial date, entered between 2026-08-26 and 2026-12-31. | TRUE if a docket entry in that case, dated inside the window, fixes a specific new trial date, as shown on PACER or CourtListener. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The HHS Office for Civil Rights breach portal posts a hacking or IT incident breach filed by an entity whose name contains Nutex, with a sub" → REJECTED: event window opens 2026-08-25, before this row is sealed (2026-08-26, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

977 issued all-time across 14 forecaster arms · 887 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 218 issued · 210 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 218 | 210 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 114 | 114 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*