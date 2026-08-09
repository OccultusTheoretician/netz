**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092008Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-09_1516.md · forecaster: manual/fable-5 · 4 accepted / 6 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260809-03 | 90% | 2026-08-27 | military/conflict | At least one Russian missile or drone strike on Odesa city or oblast occurs between 2026-08-10 and 2026-08-24. | At least two of Reuters, AP, AFP, BBC, Al Jazeera report, citing Ukrainian officials, a Russian strike on Odesa city or oblast occurring between 2026-08-10 and 2026-08-24. |
| KKR-20260809-04 | 35% | 2026-11-04 | military/conflict | An attack on or seizure of a commercial vessel in the Strait of Hormuz or Gulf of Oman, attributed to Iran or Iran-aligned forces, occurs between 2026-08-10 and 2026-10-31. | At least two of Reuters, AP, AFP, BBC report an in-window attack on or seizure of a commercial vessel in those waters, attributing it to Iran or Iran-aligned forces. |
| KKR-20260809-05 | 92% | 2026-10-12 | disaster | The USGS earthquake catalog lists at least one magnitude 7.0 or greater earthquake worldwide with origin time between 2026-08-10 and 2026-10-08. | The USGS catalog at earthquake.usgs.gov, queried on the deadline, lists at least one event of magnitude 7.0 or greater with origin time inside the window. |
| KKR-20260809-06 | 65% | 2026-08-19 | disaster | Typhoon Dolphin makes landfall on the coast of mainland China or Hainan, excluding Taiwan, between 2026-08-09 and 2026-08-16. | CMA or JMA bulletins, or at least two of Reuters, AP, AFP, report the storm center making landfall on mainland China or Hainan, excluding Taiwan, within the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Saudi or Aramco officials acknowledge a new Houthi-claimed attack, or an intercepted attack, on Saudi territory occurring between 2026-08-10" → REJECTED: resolution offers alternative VENUES joined by 'or' (…saudi government | or | aramco…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Israeli government publicly accepts a Gaza agreement based on the Trump 15-point framework, in original or amended form, between 2026-08" → REJECTED: resolution offers alternative VENUES joined by 'or' (…israeli prime minister office | or | cabinet…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The UN General Assembly adopts a resolution appointing a woman as the next Secretary-General for the term beginning 2027-01-01, between 2026" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The company Irregular or its officers are named on the OFAC SDN list, or in an unsealed US federal indictment concerning AI-system intrusion" → REJECTED: cited items name Israel; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Israel; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The FRED series DCOILBRENTEU records a Brent spot price at or above 90.00 US dollars for at least one date between 2026-08-10 and 2026-11-27" → REJECTED: cited items name Iran, Islamic Republic of, Oman, Saudi Arabia, United Arab Emirates, Yemen; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Iran, Islamic Republic of, Oman, Saudi Arabia, United Arab Emirates, Yemen; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Daniel Kinahan makes a first appearance before a court in Ireland between 2026-08-10 and 2026-09-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…courts service of ireland listings, | or | at least two of rte, bbc, irish times, reuter…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

409 issued all-time across 14 forecaster arms · 357 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5`:** 33 issued · 33 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 35 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 62 | 62 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 30 | 28 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*