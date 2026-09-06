**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062247Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: manual/fable-5/unattested · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-82 | 60% | 2026-10-20 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for the Adobe Commerce or Magento vulnerability disclosed 2026-09-05, with a dateAdded value between 2026-09-07 and 2026-10-16. | The public CISA KEV JSON feed contains an entry naming Adobe Commerce or Magento with dateAdded between 2026-09-07 and 2026-10-16 inclusive. |
| KKR-20260906-83 | 35% | 2026-09-18 | economics/markets | The FOMC statement issued 2026-09-16 announces an increase in the federal funds target range. Reference: range of 3.50 to 3.75 percent in effect on the packet date. | The Federal Reserve policy statement dated 2026-09-16 states the Committee decided to raise the target range for the federal funds rate. |
| KKR-20260906-84 | 30% | 2027-01-05 | economics/markets | The LBMA Gold Price PM prints at or above 5000.00 USD per troy ounce on at least one business day between 2026-09-08 and 2026-12-31. Reference: 4476.60 on the packet date. | The published LBMA Gold Price PM benchmark is at or above 5000.00 USD per troy ounce on any business day between 2026-09-08 and 2026-12-31 inclusive. |
| KKR-20260906-85 | 80% | 2026-10-09 | military/conflict | Between 2026-09-07 and 2026-10-07 at least one commercial vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman is attacked, struck, or seized in an incident attributed to US or Iranian forces. | A CENTCOM release, or reports from at least two of Reuters, AP, AFP, identify a specific vessel attacked or seized in the named waters within the window, attributed to US or Iranian forces. |
| KKR-20260906-86 | 35% | 2027-01-05 | disaster | The USGS earthquake catalog records at least one magnitude 6.0 or greater event within 300 km of the 2026-09-06 M6.3 Nikolski, Alaska epicenter between 2026-09-07 and 2026-12-31. | A USGS catalog query returns at least one M 6.0 or greater event with origin time in the window and epicenter within 300 km of the referenced M6.3 event. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-30. " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-09-07 and 2026-12-31 the governments of Russia and Ukraine each publicly confirm agreement to a general ceasefire or a signed f" → REJECTED: the resolution names only a venue or register (AFP, AP, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-07 and 2026-12-31 the Iranian government or IRGC issues a formal announcement declaring the Strait of Hormuz closed to comme" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Alternative fuer Deutschland records the largest party share of second votes in the official result of the Saxony-Anhalt Landtag election he" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "Between 2026-09-07 and 2026-12-31 the UK Electoral Commission publicly announces it has opened a formal investigation into donations to Refo" → REJECTED: resolution offers alternative VENUES joined by 'or' (…electoral commission publication | or | press…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1577 issued all-time across 16 forecaster arms · 1312 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 173 issued · 171 open · 2 resolved · 2 hits / 0 misses · **Brier 0.225** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 458 | 430 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 224 | 136 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 185 | 179 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*