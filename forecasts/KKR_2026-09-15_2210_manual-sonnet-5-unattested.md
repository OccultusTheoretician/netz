**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152210Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: manual/sonnet-5/unattested · 8 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-54 | 58% | 2026-10-02 | military_conflict | A Houthi-attributed strike hits Saudi Arabian oil or port infrastructure, or a vessel in the Red Sea or Gulf of Aden, between 2026-09-16 and 2026-09-30. | TRUE if Reuters, AP, or Al Jazeera report and two of those outlets corroborate a Houthi-attributed strike on Saudi oil, port, or Red Sea shipping targets between 2026-09-16 and 2026-09-30, checked by 2026-10-02. |
| KKR-20260915-55 | 32% | 2026-10-08 | military_conflict | A NATO member state government attributes an intercepted, engaged, or shot-down aircraft or drone violating its airspace to Russia or a Russia-aligned actor, between 2026-09-16 and 2026-10-06. | TRUE if a NATO member government or Reuters/AP/BBC reports the state intercepted or engaged an aircraft or drone violating its airspace and attributed it to Russia between 2026-09-16 and 2026-10-06, checked by 2026-10-08. |
| KKR-20260915-56 | 62% | 2026-10-02 | cyber | The National Vulnerability Database lists a CVE entry for the Chrome zero-day used in the GRIMWEDGE deployment chain from item 25, published between 2026-09-16 and 2026-09-30. | TRUE if nvd.nist.gov publishes a CVE entry referencing the Chrome zero-day exploited in the GRIMWEDGE chain from item 25, with a publication date between 2026-09-16 and 2026-09-30, checked 2026-10-02. |
| KKR-20260915-57 | 25% | 2026-09-29 | disaster_infrastructure | GDACS upgrades its alert level for Tropical Cyclone TWENTYFOUR-26 from Green to Orange or Red, between 2026-09-16 and 2026-09-25. | TRUE if gdacs.org shows an alert-level upgrade to Orange or Red for Tropical Cyclone TWENTYFOUR-26 dated between 2026-09-16 and 2026-09-25, checked 2026-09-29. |
| KKR-20260915-58 | 38% | 2026-10-15 | economic | The 10-year US Treasury yield closes at or above 5.25 percent on any trading day between 2026-09-16 and 2026-10-15. Reference: 4.99 percent on 2026-09-15. | TRUE if the 10-year Treasury yield (FRED series DGS10) closes at or above 5.25 percent on any trading day between 2026-09-16 and 2026-10-15. |
| KKR-20260915-59 | 33% | 2026-10-15 | economic | WTI crude oil closes below 98.00 dollars per barrel on any trading day between 2026-09-16 and 2026-10-15. Reference: 104.64 dollars on 2026-09-15. | TRUE if WTI crude (EIA daily spot price) closes below 98.00 dollars per barrel on any trading day between 2026-09-16 and 2026-10-15. |
| KKR-20260915-60 | 22% | 2026-10-19 | political | The Trump administration or DOJ files a petition for rehearing or a new emergency application with the Supreme Court on the mail ballot ruling from items 102, 103, and 124, between 2026-09-16 and 2026-10-15. | TRUE if the Supreme Court docket shows a rehearing petition or new emergency application from the Trump administration or DOJ on this specific ruling, filed between 2026-09-16 and 2026-10-15, checked 2026-10-19. |
| KKR-20260915-61 | 20% | 2026-10-19 | political | The UK government publishes a new or expanded sanctions measure targeting Israeli individuals, entities, or settlement-linked goods, between 2026-09-16 and 2026-10-15. | TRUE if gov.uk publishes a new Statutory Instrument or Foreign Office notice expanding sanctions on Israeli individuals, entities, or settlement goods, dated between 2026-09-16 and 2026-10-15, checked 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one Black Axe-affiliated defendant extradited to the US per the charges in item 12 enters a guilty plea or is convicted, between 20" → REJECTED: resolution offers alternative VENUES joined by 'or' (…doj press release | or | federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2200 issued all-time across 16 forecaster arms · 1864 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 242 issued · 210 open · 32 resolved · 16 hits / 16 misses · **Brier 0.224** against its own base rate 50.0% (climatological 0.250) · **skill +0.105**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 724 | 686 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 273 | 144 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 69 | 69 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 240 | 237 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 253 | 247 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 242 | 210 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*