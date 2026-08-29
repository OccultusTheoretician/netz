**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292142Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-28_1518.md · forecaster: control/baserate · 2 accepted / 8 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-28 | 25% | 2026-09-18 | economic | The FOMC will leave the federal funds target range unchanged at its scheduled meeting concluding 2026-09-16, despite the hawkish Jackson Hole remarks in items 53, 55, and 56. | True if the FOMC statement released 2026-09-16 at 2pm ET sets the same target range in effect entering the meeting, per federalreserve.gov or a wire report. |
| KKR-20260829-29 | 52% | 2026-10-18 | disaster_infrastructure | A second, distinct flash-flood or lake-outburst event from the barrier lake in items 43 and 46 will hit Nepal or Tibet, separate from the flooding already reported as of 2026-08-28, between 2026-09-04 and 2026-10-15. | True if Nepal disaster authorities, Chinese state media, or two wire services report a new flood or outburst event from this barrier lake, distinct from the ongoing flooding, in that window, checked at the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A CVE tied to the actively exploited PaperCut zero-day in item 12 will be added to the CISA Known Exploited Vulnerabilities catalog with a d" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "At least one of the three CVSS 10.0 ServiceNow vulnerabilities in items 18 and 20 will be added to the CISA KEV catalog with a dateAdded val" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "A new, specifically named acquirer will submit or confirm a takeover offer for PayPal Holdings after the prior bid in item 59 reportedly col" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "USDA or FSIS will publish a Federal Register entry or formal notice implementing the ranch and farm self-processing policy in item 60, dated" → REJECTED: resolution offers alternative VENUES joined by 'or' (…entry with a publication date in that window, | or | usda issues a press release confirming the ru…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The United States and Iran, or Israel and Iran, will announce a mutually acknowledged ceasefire or armistice in the war referenced in items " → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "US naval forces enforcing the Iran oil-export blockade in item 97 will exchange direct fire with Iranian military or IRGC naval units, first" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Austrian police will publicly name at least one arrested suspect in the 673-diamond necklace theft in item 9, reported between 2026-08-28 an" → REJECTED: resolution offers alternative VENUES joined by 'or' (…landespolizeidirektion wien | or | a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names a different subject than the statement — the claim is about Austrian and the resolution settles on AP, APA, Landespolizeidirektion, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "Incumbent Edward Markey will win the Massachusetts Democratic US Senate primary held 2026-09-01, referenced in item 127." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-01 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1074 issued all-time across 14 forecaster arms · 913 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 256 issued · 239 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 256 | 239 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 106 | 105 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 127 | 124 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 113 | 105 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*