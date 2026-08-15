**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141519Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-14_1517.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260814-01 | 25% | 2026-08-28 | disaster | Between 2026-08-22 and 2026-08-25, a significant earthquake of magnitude 5.0 or higher will be recorded by the USGS in the Pacific Northwest, with a location within 50 km of the San Andreas Fault. | The USGS Significant Quakes database will list an event with magnitude ≥5.0 and location within 50 km of the San Andreas Fault between 2026-08-22 and 2026-08-25. |
| KKR-20260814-02 | 60% | 2026-08-26 | economics/markets | On 2026-08-23, the S&P 500 will close above 7,800 points, based on the final settlement price from the NYSE. | The S&P 500 closes at or above 7,800 points on 2026-08-23, as reported by the NYSE final settlement price. |
| KKR-20260814-03 | 35% | 2026-08-27 | cyber | Between 2026-08-21 and 2026-08-24, a data breach involving the exposure of over 1 million user accounts will be confirmed by two independent sources in the United States, with the breach linked to a RingCentral system. | Two independent U.S.-based sources will confirm a data breach affecting over 1 million user accounts linked to RingCentral between 2026-08-21 and 2026-08-24. |
| KKR-20260814-04 | 20% | 2026-08-28 | cyber | Between 2026-08-22 and 2026-08-25, a major cyberattack will be reported by at least two hostile sides in the Iran Theatre, with the attack targeting critical infrastructure and involving a known exploit chain. | At least two hostile sides (AXIS, WEST) will report a cyberattack on critical infrastructure in the Iran Theatre between 2026-08-22 and 2026-08-25, with the attack involving a known exploit chain. |
| KKR-20260814-05 | 40% | 2026-08-27 | political | Between 2026-08-21 and 2026-08-24, a new government policy will be announced in the United Kingdom that imposes a temporary ban on disposable barbecues in areas classified as 'tinderbox' due to extreme heat risk. | A government-issued policy in the United Kingdom, confirmed by two independent news outlets, will impose a temporary ban on disposable barbecues in areas classified as 'tinderbox' due to extreme heat risk between 2026-08-21 and 2026-08-24. |
| KKR-20260814-06 | 30% | 2026-08-28 | military/conflict | Between 2026-08-22 and 2026-08-25, a new military alliance will be formally announced by Saudi Arabia and its regional partners, with the stated purpose of defending the Red Sea from maritime threats. | A formal announcement of a new military alliance for Red Sea defense will be made by Saudi Arabia and at least two regional partners between 2026-08-22 and 2026-08-25, confirmed by two independent news outlets. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-08-22, the CISA KEV catalog will include a new entry for a critical VMware vCenter RCE flaw exploited for reverse SSH access, with a" → REJECTED: event window opens 2026-08-13, before this row is sealed (2026-08-14) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-08-21 and 2026-08-24, a drone attack will be confirmed by at least two hostile sides in the Kyiv region, with weapons reported " → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-08-21 and 2026-08-24, a new political scandal involving a U.S. politician will be reported by two major wire services, with the" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-08-22 and 2026-08-25, a new data center project in space will be publicly announced by a major tech firm, with the claim that i" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

600 issued all-time across 14 forecaster arms · 544 open (23 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 70 issued · 68 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 105 | 105 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 70 | 68 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 33 | 33 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 49 | 49 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*