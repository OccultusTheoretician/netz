**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231517Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-23_1515.md · forecaster: lmstudio/auto · 9 accepted / 1 rejected by validation gate · 8 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260823-01 | 28% | 2026-09-02 | military/conflict | A drone strike targeting Kyiv, Ukraine, occurs between 2026-08-24 and 2026-08-30, resulting in at least one confirmed casualty. | At least one confirmed casualty is reported in a drone strike on Kyiv, Ukraine, between 2026-08-24 and 2026-08-30, as verified by two independent, hostile-side news outlets (e.g., Al Jazeera and BBC World). |
| KKR-20260823-02 | 32% | 2026-09-04 | cyber | A cyberattack exploiting a vulnerability listed in the CISA KEV catalog occurs between 2026-08-25 and 2026-09-01, disrupting a critical infrastructure provider in the UK. | The CISA KEV catalog carries a date-added value between 2026-08-25 and 2026-09-01, and a public report confirms a cyberattack disrupting a UK critical infrastructure provider during that window. |
| KKR-20260823-03 | 22% | 2026-09-05 | disaster | A magnitude 6.0 or greater earthquake strikes Japan between 2026-08-26 and 2026-09-02, with at least 10 fatalities reported. | The USGS Significant Quakes database records a magnitude 6.0 or greater earthquake in Japan between 2026-08-26 and 2026-09-02, with at least 10 fatalities confirmed by two independent news outlets. |
| KKR-20260823-04 | 35% | 2026-09-06 | economics/markets | A new US economic sanction against Iran is formally announced by the Treasury Department between 2026-08-27 and 2026-09-03, with a public press release issued. | The U.S. Department of the Treasury issues a public press release announcing a new economic sanction against Iran between 2026-08-27 and 2026-09-03. |
| KKR-20260823-05 | 26% | 2026-09-07 | military/conflict | A major offensive operation by Russian forces in the Kursk region of Ukraine begins between 2026-08-28 and 2026-09-04, confirmed by two hostile-side reports with independent corroboration. | Two reports from hostile sides (RU and UA) with independent channels confirm a major offensive operation by Russian forces in the Kursk region of Ukraine between 2026-08-28 and 2026-09-04. |
| KKR-20260823-06 | 30% | 2026-09-09 | political | A new political crisis emerges in the UK Parliament over the recognition of Israel's actions in Gaza, with a formal motion of no confidence tabled between 2026-08-30 and 2026-09-06. | A formal motion of no confidence in the UK Parliament regarding recognition of Israel's actions in Gaza is tabled between 2026-08-30 and 2026-09-06, as confirmed by two independent news outlets. |
| KKR-20260823-07 | 20% | 2026-09-10 | disaster | A major wildfire breaks out in California, USA, between 2026-08-31 and 2026-09-07, with at least 500 homes destroyed, confirmed by two independent sources. | Two independent sources (e.g., NPR News and Al Jazeera) confirm a major wildfire in California, USA, between 2026-08-31 and 2026-09-07, with at least 500 homes destroyed. |
| KKR-20260823-08 | 24% | 2026-09-11 | economics/markets | A new round of sanctions on Russia is imposed by the European Union, with a formal press release issued between 2026-09-01 and 2026-09-08, confirmed by two independent news outlets. | The European Commission issues a formal press release announcing new sanctions on Russia between 2026-09-01 and 2026-09-08, confirmed by two independent news outlets (e.g., BBC World and Al Jazeera). |
| KKR-20260823-09 | 27% | 2026-09-12 | military/conflict | A drone strike on a military facility in Damascus, Syria, results in at least one confirmed casualty between 2026-09-02 and 2026-09-09, confirmed by two hostile-side reports. | Two reports from hostile sides (PS, AXIS, WEST) with independent channels confirm a drone strike on a military facility in Damascus, Syria, between 2026-09-02 and 2026-09-09, with at least one confirmed casualty. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A coordinated cyberattack using a previously unknown exploit disrupts a major financial institution in the United States between 2026-08-29 " → REJECTED: the resolution names a different subject than the statement — the claim is about States, United and the resolution settles on CNBC, MarketWatch, News, Top. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

886 issued all-time across 14 forecaster arms · 796 open (37 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 131 issued · 119 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 131 | 119 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 81 | 81 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 99 | 99 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 90 | 89 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*