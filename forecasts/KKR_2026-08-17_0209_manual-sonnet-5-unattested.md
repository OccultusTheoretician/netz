**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 170209Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-16_1516.md · forecaster: manual/sonnet-5/unattested · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-21 | 15% | 2026-09-22 | military/conflict | Between 2026-08-17 and 2026-09-20, Qatar and Iran issue public statements that converge on a single account of the fate of the three Iranian pilots Qatar allegedly shot down in March 2026, either confirming them alive and held or confirming their deaths. | TRUE if Qatar and Iran state the same outcome for the three named pilots, reported by Reuters, AP, or AFP, between 2026-08-17 and 2026-09-20; otherwise FALSE. |
| KKR-20260817-22 | 6% | 2026-09-17 | military/conflict | Between 2026-08-17 and 2026-09-15, the United States government takes a formal, documented action asserting a sovereignty or territorial claim over any part of the Strait of Hormuz, beyond rhetorical statements by the President. | TRUE if the Federal Register, a State Department notice, or a wire service reports a formal US filing or action claiming sovereignty over Hormuz waters between 2026-08-17 and 2026-09-15; otherwise FALSE. |
| KKR-20260817-23 | 32% | 2026-09-02 | cyber | Between 2026-08-17 and 2026-08-31, a cybersecurity vendor or outlet other than BleepingComputer, such as Krebs on Security, The Hacker News, Malwarebytes, SentinelOne, or Objective-See, publishes independent research naming and attributing the AmnesiaStealer macOS malware campaign. | TRUE if a named second security vendor or outlet publishes independent attribution of AmnesiaStealer between 2026-08-17 and 2026-08-31; otherwise FALSE. |
| KKR-20260817-24 | 40% | 2026-09-22 | political | Between 2026-08-17 and 2026-09-20, the US Navy or Department of Defense publicly confirms that USS George Washington has relieved USS Abraham Lincoln on its Middle East deployment station. | TRUE if DoD or Navy public affairs, or a wire service citing an on-record defense official, confirms the Lincoln to George Washington handover between 2026-08-17 and 2026-09-20; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-08-19, Target Corporation common stock closes with a single-session price change of 5.0 percent or greater, up or down, relative to " → REJECTED: the resolution names a different subject than the statement — the claim is about Corporation, Target and the resolution settles on NYSE, TGT. A row whose resolution checks a different fact can be scored correct while being wrong
- "WTI crude oil does not settle above 90.00 USD per barrel on the NYMEX on any trading day between 2026-08-17 and 2026-09-15." → REJECTED: statement and resolution assert opposite directions - the statement claims an absence and the resolution resolves TRUE on the event occurring. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "Between 2026-08-17 and 2026-08-31, Chesterfield County Police or Virginia State University publicly identify and announce the arrest of a se" → REJECTED: resolution offers alternative VENUES joined by 'or' (…wire service | or | local…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-08-17 and 2026-08-31, Zimbabwean authorities or a wire service report a confirmed death toll from the August 2026 Zimbabwe boat" → REJECTED: resolution offers alternative VENUES joined by 'or' (…wire service | or | zimbabwean government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-08-17 and 2026-08-24, the USGS earthquake catalog records at least one aftershock of magnitude 5.0 or greater within 100 km of " → REJECTED: the resolution names a different subject than the statement — the claim is about Ende, Indonesia, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-17 and 2026-08-24, the High Fens wildfire burns across the Belgium-Germany border into confirmed German territory." → REJECTED: resolution offers alternative VENUES joined by 'or' (…german civil-protection authority | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

658 issued all-time across 14 forecaster arms · 568 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 51 issued · 50 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 126 | 118 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 82 | 70 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 51 | 50 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*