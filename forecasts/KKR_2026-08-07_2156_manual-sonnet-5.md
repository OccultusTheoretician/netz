**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 072156Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-07_1747.md · forecaster: manual/sonnet-5 · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260807-15 | 25% | 2026-08-27 | political | Spain will move beyond its stated threat and implement reciprocal entry checks on travelers from Italy, between 2026-08-10 and 2026-08-24. | TRUE if the Spanish Interior Ministry announces active reciprocal checks on Italy-origin travelers between 2026-08-10 and 2026-08-24, confirmed by at least two of Al Jazeera, BBC, or DW; FALSE otherwise. |
| KKR-20260807-16 | 22% | 2026-09-01 | military_conflict | Houthi forces will be reported to have captured or besieged a district-level administrative center in Marib or Hodeidah governorate, between 2026-08-14 and 2026-08-28. | TRUE if at least two of Al Jazeera, Reuters, AP, or the Yemeni government report Houthi capture or siege of a named district center between 2026-08-14 and 2026-08-28; FALSE otherwise. |
| KKR-20260807-17 | 42% | 2026-09-01 | military_conflict | The ELN will be reported responsible for an attack killing at least one Colombian security-force member, between 2026-08-14 and 2026-08-28. | TRUE if the Colombian Defense Ministry or at least two of Reuters, AP, or El Tiempo report an ELN-attributed killing of a security-force member between 2026-08-14 and 2026-08-28; FALSE otherwise. |
| KKR-20260807-18 | 30% | 2026-09-15 | economic | BLS will report a second consecutive month of net job losses for August 2026, in the Employment Situation release published between 2026-09-01 and 2026-09-12. | TRUE if the BLS Employment Situation report covering August 2026, released between 2026-09-01 and 2026-09-12, shows negative net nonfarm payroll change; FALSE otherwise. |
| KKR-20260807-19 | 60% | 2026-09-15 | political | The US Senate will vote to confirm Todd Blanche as Attorney General between 2026-08-10 and 2026-09-11. | TRUE if the Senate confirms Blanche by roll-call vote between 2026-08-10 and 2026-09-11, per congress.gov or at least two of NPR, CNBC, or Guardian; FALSE if rejected, withdrawn, or no vote occurs. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index will close at a fresh all-time high on at least one trading day between 2026-08-07 and 2026-08-14." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "GDACS will upgrade its alert level for Tropical Cyclone CHAN-HOM-26 from Green to Orange or Red at some point between 2026-08-07 and 2026-08" → REJECTED: resolution offers alternative VENUES joined by 'or' (…orange | or | red…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "North Carolina Ports will publicly confirm the cyberattack disrupting its operations was ransomware, between 2026-08-08 and 2026-08-22." → REJECTED: resolution offers alternative VENUES joined by 'or' (…fbi | or | cisa…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one of the 78 people arrested in the Spain-led Mediterranean smuggling-network raid will be formally charged, between 2026-08-10 an" → REJECTED: the resolution names a different subject than the statement — the claim is about Mediterranean, Spain and the resolution settles on BBC, Interior, Jazeera, Ministry. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Russia sanctions bill the Senate passed on 2026-08-07 will be signed into law between 2026-08-10 and 2026-09-25." → REJECTED: the resolution names a different subject than the statement — the claim is about Russia, Senate and the resolution settles on Federal, Law, Public, Register. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

379 issued all-time across 14 forecaster arms · 332 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5`:** 23 issued · 22 open · 1 resolved · 0 hits / 1 misses · **Brier 0.336** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 27 | 25 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 20 | 32 | 9 | 23 | 0.221 | 28.1% | 0.202 | -0.093 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 23 | 22 | 1 | 0 | 1 | 0.336 | 0.0% | 0.000 | — |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*