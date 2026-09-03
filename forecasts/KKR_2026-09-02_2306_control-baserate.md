**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022306Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-02_1520.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-63 | 30% | 2026-10-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendor or product fields reference SonicWall SMA1000, with a dateAdded value between 2026-09-03 and 2026-09-30. | A fetch of the CISA KEV catalog on the deadline shows at least one SMA1000 entry with dateAdded between 2026-09-03 and 2026-09-30 inclusive. |
| KKR-20260902-64 | 21% | 2026-11-03 | economics/markets | Front-month NYMEX WTI crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-09-03 and 2026-10-30. Reference: 90.59 on the packet date. | CME official settlement data show any front-month CL settlement at or above 100.00 inside the window. Reference level at seal: 90.59. |
| KKR-20260902-65 | 21% | 2027-01-05 | economics/markets | The US 10-year Treasury constant maturity yield, FRED series DGS10, records a value at or above 5.00 percent on at least one business day between 2026-09-03 and 2026-12-31. Reference: 4.80 percent on the packet date. | FRED series DGS10 shows at least one daily value at or above 5.00 inside the window. Reference level at seal: 4.80 percent. |
| KKR-20260902-66 | 35% | 2026-10-05 | political | A lapse in US federal appropriations begins on 2026-10-01 because no full-year appropriations act or continuing resolution covering all agencies is enacted on or before 2026-09-30. | Congress.gov shows no enacted government-wide funding measure signed by 2026-09-30 and OPM publicly issues shutdown furlough guidance effective 2026-10-01. |
| KKR-20260902-67 | 49% | 2026-11-04 | military/conflict | A continuous suspension of laden tanker transits through the Strait of Hormuz lasting at least 72 hours begins between 2026-09-03 and 2026-10-31. | At least two of Reuters, AP, Bloomberg, AFP report, citing AIS or tracking data, a continuous 72-hour halt of laden tanker transits beginning inside the window. |
| KKR-20260902-68 | 49% | 2026-09-21 | military/conflict | At least one US military strike on a target inside Iranian territory occurring between 2026-09-03 and 2026-09-16 is acknowledged by US official channels and reported by Iranian state media. | CENTCOM or DoD publicly acknowledges a strike inside Iran occurring in the window, and at least one of IRNA, Tasnim, Press TV reports a strike on Iranian territory in the same window. |
| KKR-20260902-69 | 36% | 2026-09-18 | disaster | A major US grid operator among PJM, MISO, ERCOT, SPP, NYISO, ISO-NE, CAISO declares an Energy Emergency Alert Level 2 or higher effective on a date between 2026-09-03 and 2026-09-16. | The public notices archive of at least one named operator shows an EEA Level 2 or Level 3 declaration, or equivalent maximum generation emergency, effective inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The HHS Office for Civil Rights breach portal lists Aesto Health as covered entity or business associate with at least 9000000 individuals a" → REJECTED: event window opens 2026-08-01, before this row is sealed (2026-09-02, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "US Treasury OFAC publishes at least one new Iran-program designation action, adding or updating SDN entries under an Iran-related authority," → REJECTED: resolution offers alternative VENUES joined by 'or' (…ofac recent actions page | or | the federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Opening statements in the criminal trial of the defendant in the Charlie Kirk homicide case commence on or before 2027-02-26." → REJECTED: the resolution names only a venue or register (AP, BBC, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1308 issued all-time across 14 forecaster arms · 1043 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 351 issued · 323 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 351 | 323 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 192 | 104 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 152 | 131 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*