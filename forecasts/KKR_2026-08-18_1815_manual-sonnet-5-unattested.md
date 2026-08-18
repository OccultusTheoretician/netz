**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181815Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-18_1516.md · forecaster: manual/sonnet-5/unattested · 4 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260818-21 | 6% | 2026-08-28 | military/conflict | The United States will carry out a military strike on a target inside Oman between 2026-08-19 and 2026-08-26. | TRUE if the US government, the Omani government, or two independent wire services confirm a US military strike inside Oman during the window; adjudicated 2026-08-28. |
| KKR-20260818-22 | 10% | 2026-09-18 | cyber | CVE-2026-19478, the critical GitLab GraphQL flaw patched 2026-08-17, will be added to the CISA KEV catalog between 2026-08-19 and 2026-09-16. | TRUE if CISA's Known Exploited Vulnerabilities catalog lists CVE-2026-19478 with a date-added value inside the window; adjudicated 2026-09-18. |
| KKR-20260818-23 | 45% | 2026-09-28 | crime/security | A jury will return a verdict, guilty or not guilty, in the Duane Keffe D Davis murder trial in Clark County, Nevada, between 2026-09-07 and 2026-09-25. | TRUE if Clark County District Court or at least two independent wire services report a jury verdict in the Davis trial inside the window; a hung jury counts as FALSE; adjudicated 2026-09-28. |
| KKR-20260818-24 | 55% | 2026-08-28 | disaster | USGS will record a magnitude 6.0 or greater earthquake within 150 km of the M7.7 Ende, Indonesia mainshock (2026-08-17, 22:29 UTC), between 2026-08-19 and 2026-08-26. | TRUE if the USGS Earthquake Catalog lists any magnitude 6.0 or greater event within 150 km of the Ende mainshock epicenter, origin time inside the window; adjudicated 2026-08-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Russia will conduct a missile or drone strike hitting within Kyiv city limits between 2026-08-19 and 2026-08-26." → REJECTED: resolution offers alternative VENUES joined by 'or' (… or an independent wire service (reuters, ap, | or | afp) report a russian missile or drone strike…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The 30-year US Treasury par yield will close at or above 5.30 percent on 2026-09-15." → REJECTED: resolution offers alternative VENUES joined by 'or' (…fred series dgs30 | or | the us treasury daily par yield curve reports…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-15 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "WTI crude will settle at or above 90.00 USD per barrel on at least one day between 2026-08-19 and 2026-09-02." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "All 16 typosquatted RubyGems packages named in the 2026-08-18 report on credential and wallet theft will be removed from RubyGems.org betwee" → REJECTED: resolution offers alternative VENUES joined by 'or' (…org index | or | api by the deadline…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Incumbent Senator Dan Sullivan will place first among candidates in Alaska's nonpartisan top-four primary for US Senate held on 2026-08-18." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

732 issued all-time across 14 forecaster arms · 642 open (6 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 62 issued · 61 open · 1 resolved · 0 hits / 1 misses · **Brier 0.040** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 149 | 141 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 100 | 88 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 69 | 69 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 62 | 61 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*