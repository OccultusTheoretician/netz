**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 072155Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-07_1747.md · forecaster: manual/fable-5 · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260807-05 | 88% | 2026-10-02 | political | The US Senate confirms Todd Blanche as Attorney General by recorded roll call vote between 2026-08-07 and 2026-09-30. | Congress.gov or senate.gov roll call record shows a Senate vote confirming Todd Blanche as United States Attorney General with a vote date between 2026-08-07 and 2026-09-30. |
| KKR-20260807-06 | 15% | 2027-01-19 | military/conflict | Houthi forces take control of Marib city, Yemen, between 2026-08-08 and 2027-01-15. | At least two of Reuters, AP, AFP, or Al Jazeera report Marib city under Houthi control, or the Yemeni government concedes its loss, with event dates inside the window. |
| KKR-20260807-07 | 10% | 2026-12-02 | cyber | A vulnerability in Claude Code or Gemini CLI disclosed in early August 2026 is added to the CISA KEV catalog with a dateAdded between 2026-08-08 and 2026-11-30. | The CISA KEV JSON feed lists a CVE whose product or description names Claude Code or Gemini CLI, with dateAdded between 2026-08-08 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Russia sanctions bill passed by the US Senate on 2026-08-07 is enacted into US public law between 2026-08-07 and 2026-11-06." → REJECTED: cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The Colombian government or the ELN publicly and formally declares the bilateral peace process or ceasefire suspended or ended between 2026-" → REJECTED: resolution offers alternative VENUES joined by 'or' (…official colombian government | or | eln…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Front-month WTI crude futures settle at or above 95.00 USD per barrel on at least one NYMEX trading day between 2026-08-10 and 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The FOMC lowers the federal funds target range at its scheduled September 2026 meeting." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The CISA Known Exploited Vulnerabilities catalog adds at least 8 CVE entries with dateAdded values between 2026-08-10 and 2026-09-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Meta files an appeal or notice of appeal of the 567 million USD New Mexico child-safety judgment between 2026-08-08 and 2026-11-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…new mexico 567 million usd child-safety case, | or | two of reuters, ap, bloomberg report the fili…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "GDACS raises tropical cyclone CHAN-HOM-26 to Orange or Red alert level between 2026-08-08 and 2026-08-21." → REJECTED: resolution offers alternative VENUES joined by 'or' (…orange | or | red…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

367 issued all-time across 14 forecaster arms · 320 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5`:** 23 issued · 23 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 17 | 1 | 0 | 1 | 0.336 | 0.0% | 0.000 | — |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*