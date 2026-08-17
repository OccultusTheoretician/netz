**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171813Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-17_1537.md · forecaster: manual/opus-5/unattested · 3 accepted / 7 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-69 | 70% | 2026-11-03 | cyber | CISA adds the exploited VMware vCenter flaw CVE-2026-59310 to the Known Exploited Vulnerabilities catalog between 2026-08-18 and 2026-10-31. | The CISA KEV JSON feed contains an entry with cveID CVE-2026-59310 whose dateAdded value falls between 2026-08-18 and 2026-10-31 inclusive. |
| KKR-20260817-70 | 6% | 2026-11-04 | military/conflict | US forces conduct a military strike on Omani territory or Omani territorial waters between 2026-08-18 and 2026-10-31. | The US Defense Department or CENTCOM acknowledges a strike on Omani territory or territorial waters occurring in that window, and both Reuters and Agence France-Presse report it. |
| KKR-20260817-71 | 55% | 2026-10-05 | disaster | USGS catalogs an earthquake of magnitude 6.0 or greater within 250 km of the epicenter of event us6000tkt2 between 2026-08-18 and 2026-09-30. | A USGS ComCat query for magnitude 6.0 or greater events within 250 km of the us6000tkt2 epicenter, origin times between 2026-08-18 and 2026-09-30 UTC, returns at least one event. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC lowers its federal funds target range at its scheduled September 2026 meeting concluding 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Brent crude records a daily spot price at or above 100.00 US dollars per barrel on at least one date between 2026-08-18 and 2026-10-30." → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "GE HealthCare Technologies files an SEC Form 8-K reporting a material cybersecurity incident under Item 1.05 between 2026-08-18 and 2026-11-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "No candidate exceeds 50 percent of valid votes in the Brazilian presidential first round held 2026-10-04, sending the race to the 2026-10-25" → REJECTED: the resolution names a different subject than the statement — the claim is about Brazilian and the resolution settles on Official, TSE. A row whose resolution checks a different fact can be scored correct while being wrong
- "The Democratic Party wins at least 218 seats in the US House of Representatives in the 2026-11-03 midterm elections." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-03 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The United States publicly announces the lifting or suspension of its naval blockade of Iranian ports between 2026-08-18 and 2026-10-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (… in that window announces the blockade lifted | or | suspended, and both reuters and the associate…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Cumulative confirmed Ebola cases in the Democratic Republic of the Congo outbreak reach 15,000 or more on or before 2026-11-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…who situation report | or | ecdc communicable disease threats…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-30 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution names a different subject than the statement — the claim is about Congo, Cumulative, Democratic, Ebola and the resolution settles on Bundibugyo, DRC, ECDC, WHO. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

705 issued all-time across 14 forecaster arms · 615 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 63 issued · 63 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 146 | 138 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 92 | 80 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 47 | 47 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 63 | 63 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 58 | 57 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*