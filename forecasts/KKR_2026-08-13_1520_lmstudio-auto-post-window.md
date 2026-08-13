**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131520Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-13_1519.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260813-01 | 28% | 2026-08-27 | military/conflict | A drone strike targeting a Russian military installation in Sevastopol occurs between 2026-08-21 and 2026-08-24, resulting in at least one confirmed casualty. | The CISA KEV catalog carries a date-added value between 2026-08-21 and 2026-08-24, and at least one report from a credible source (BBC World, Al Jazeera, or Defense One) confirms a drone strike on a Russian military installation in Sevastopol with at least one confirmed casualty. |
| KKR-20260813-02 | 18% | 2026-08-27 | disaster | A major earthquake of magnitude 6.0 or higher occurs in the Pacific Northwest between 2026-08-21 and 2026-08-24, as reported by USGS Significant Quakes. | The USGS Significant Quakes database records an event with magnitude ≥6.0 and epicenter within the Pacific Northwest region (Washington, Oregon, or adjacent offshore) between 2026-08-21 and 2026-08-24. |
| KKR-20260813-03 | 22% | 2026-08-27 | political | Iran announces a ceasefire with Israel in the Levant Theatre between 2026-08-21 and 2026-08-24, confirmed by at least two independent sources (BBC World and Al Jazeera). | At least two independent sources (BBC World and Al Jazeera) report that Iran officially announces a ceasefire with Israel in the Levant Theatre between 2026-08-21 and 2026-08-24. |
| KKR-20260813-04 | 30% | 2026-08-27 | disaster | A wildfire in the Boise Mountains region, triggered by extreme heat, is confirmed by the NWS Flash Flood Warning system between 2026-08-21 and 2026-08-24. | The National Weather Service (NWS) Flash Flood Warning system records a warning issued between 2026-08-21 and 2026-08-24 for the Boise Mountains region, citing wildfire risk due to extreme heat and dry conditions. |
| KKR-20260813-05 | 38% | 2026-08-27 | cyber | The White House confirms the launch of offensive hack-back operations against hostile state actors by a private cybersecurity firm between 2026-08-21 and 2026-08-24, as reported by BleepingComputer. | BleepingComputer publishes a report on or before 2026-08-24 confirming that the White House has authorized offensive hack-back operations against hostile state actors by a private cybersecurity firm, with a direct quote from a White House official. |
| KKR-20260813-06 | 25% | 2026-08-27 | disaster | A major oil spill from a tanker in the Strait of Hormuz is confirmed by Al Jazeera between 2026-08-21 and 2026-08-24, with damage to marine life reported. | Al Jazeera publishes a report between 2026-08-21 and 2026-08-24 confirming a major oil spill in the Strait of Hormuz, with at least one independent marine biologist or environmental agency confirming ecological damage. |
| KKR-20260813-07 | 35% | 2026-08-27 | political | The European Parliament passes a resolution banning countries at war from hosting the Eurovision Song Contest between 2026-08-21 and 2026-08-24, as recorded in the European Parliament's official register. | The European Parliament's official register contains a resolution passed between 2026-08-21 and 2026-08-24 banning countries at war from hosting the Eurovision Song Contest, with a public docket number and date. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes above 7,850 on 2026-08-26." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "A cyberattack exploiting the Windows zero-day vulnerability (CVE-2026-XXXX) is confirmed by CISA KEV between 2026-08-21 and 2026-08-24." → REJECTED: the resolution requires item and the failure condition does not mention it — an outcome missing it satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements
- "The Treasury Department releases a new set of sanctions against Russian oligarchs on 2026-08-26, as documented in the Federal Register." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-26 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

562 issued all-time across 14 forecaster arms · 506 open (7 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 64 issued · 62 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 89 | 89 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 64 | 62 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 26 | 26 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*