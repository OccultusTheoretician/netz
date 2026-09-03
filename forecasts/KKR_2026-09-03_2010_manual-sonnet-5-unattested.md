**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032010Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-03_1518.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-23 | 30% | 2026-09-21 | military_conflict | Iran or an Iran-aligned force conducts another confirmed strike (drone, missile, or cruise) against a target inside Kuwait or another Gulf Cooperation Council state between 2026-09-05 and 2026-09-19. | Two independently-biased outlets (for example a Western wire service and a Gulf or Iran-aligned channel) confirm a Kuwait or GCC-territory strike attributed to Iran or an Iran-aligned force occurring between 2026-09-05 and 2026-09-19, checked by 2026-09-21. |
| KKR-20260903-24 | 22% | 2026-10-05 | military_conflict | A named Ukrainian government body announces disciplinary action, criminal charges, or a completed inquiry finding against personnel involved in the September 2, 2026 SBU-HUR shootout in Kyiv, with the announcement occurring between 2026-09-05 and 2026-10-03. | A Ukrainian official body publicly announces a named finding, charge, or disciplinary measure tied to the incident, occurring between 2026-09-05 and 2026-10-03, confirmed by two outlets by 2026-10-05. |
| KKR-20260903-25 | 60% | 2026-09-25 | economic | ICE Brent crude front-month futures settle at or above 90.00 USD/bbl on 2026-09-25. Reference: 96.70 on the packet date (2026-09-03). | ICE Brent front-month futures daily settlement price on 2026-09-25 is 90.00 USD/bbl or higher, per exchange settlement data. |
| KKR-20260903-26 | 68% | 2026-09-25 | economic | COMEX gold front-month futures settle at or above 4300.00 USD/oz on 2026-09-25. Reference: 4546.20 on the packet date (2026-09-03). | COMEX gold front-month futures daily settlement price on 2026-09-25 is 4300.00 USD/oz or higher, per exchange settlement data. |
| KKR-20260903-27 | 72% | 2026-09-16 | economic | The FOMC holds its federal funds target range unchanged at its September 15-16, 2026 meeting. Reference: 3.50-3.75 percent target range in effect on the packet date. | The FOMC post-meeting statement released 2026-09-16 states the target range is unchanged from 3.50-3.75 percent. |
| KKR-20260903-28 | 25% | 2026-10-19 | political | Leon Black either appears for a rescheduled House Oversight Committee deposition or is formally held in contempt of Congress in connection with the Epstein-probe subpoena, between 2026-09-05 and 2026-10-17. | House Oversight Committee records or a wire-service report confirm either a completed Leon Black deposition or a committee contempt vote or referral occurring between 2026-09-05 and 2026-10-17, checked by 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds at least one additional SonicWall-vendor CVE to the Known Exploited Vulnerabilities catalog between 2026-09-05 and 2026-09-26, bey" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-83549 dateAdded 2026-09-02, before the claimed window 2026-09-05..2026-09-26; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "New South Wales Police announce a charge or arrest in the second suspected mistaken-identity killing under investigation in Sydney, between " → REJECTED: resolution offers alternative VENUES joined by 'or' (…nsw police media release | or | australian…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Nepali disaster-response authorities publicly confirm the fate, rescued alive or recovered deceased, of the workers trapped in the Rasuwagad" → REJECTED: resolution offers alternative VENUES joined by 'or' (…nepali government agency | or | two independent…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1348 issued all-time across 15 forecaster arms · 1083 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 158 issued · 137 open · 21 resolved · 10 hits / 11 misses · **Brier 0.214** against its own base rate 47.6% (climatological 0.249) · **skill +0.141** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 370 | 342 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 200 | 112 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 158 | 137 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*