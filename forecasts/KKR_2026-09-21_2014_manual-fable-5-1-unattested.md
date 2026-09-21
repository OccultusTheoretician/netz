**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212014Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-21_1516.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260921-40 | 35% | 2026-10-20 | economics/markets | NYMEX front-month WTI crude settles below 85.00 USD per barrel on at least one trading day between 2026-09-22 and 2026-10-16. Reference: 92.25 on the packet date. | CME NYMEX official daily settlement for the front-month CL contract prints below 85.00 on any trading day 2026-09-22 through 2026-10-16. |
| KKR-20260921-41 | 25% | 2026-11-03 | economics/markets | The US 10-year Treasury constant-maturity yield (FRED DGS10) closes below 4.60 percent on at least one day between 2026-09-22 and 2026-10-30. Reference: 4.96 percent on the packet date. | FRED series DGS10 shows a daily value below 4.60 for any date 2026-09-22 through 2026-10-30. |
| KKR-20260921-42 | 15% | 2026-12-22 | political | Friedrich Merz ceases to be German chancellor, or loses a Bundestag confidence vote, between 2026-09-22 and 2026-12-18. | Bundestag plenary record shows a lost Vertrauensfrage, or Bundespraesident appoints a successor chancellor, dated 2026-09-22 through 2026-12-18, confirmed by Reuters or DW. |
| KKR-20260921-43 | 45% | 2026-11-17 | political | A federal court grants a temporary restraining order or preliminary injunction against the White House access ban on CNN, MS NOW and Politico between 2026-09-22 and 2026-11-13. | Docket entry on CourtListener or PACER in the suit filed by CNN, MS NOW and Politico grants TRO or preliminary injunction, dated 2026-09-22 through 2026-11-13. |
| KKR-20260921-44 | 60% | 2026-10-15 | cyber | The CISA KEV catalog adds at least one Cisco product vulnerability with a dateAdded value between 2026-09-22 and 2026-10-12. | The CISA KEV JSON feed contains an entry with vendorProject Cisco and dateAdded between 2026-09-22 and 2026-10-12 inclusive. |
| KKR-20260921-45 | 30% | 2026-10-05 | disaster | Typhoon Dujuan causes 10 or more confirmed deaths in Japan between 2026-09-21 and 2026-09-30. | Japan Fire and Disaster Management Agency or NHK reports a cumulative Dujuan death toll in Japan of 10 or more for deaths occurring 2026-09-21 through 2026-09-30. |
| KKR-20260921-46 | 65% | 2026-10-23 | disaster | USGS records at least one earthquake of magnitude 7.0 or greater anywhere on Earth between 2026-09-22 and 2026-10-21. | The USGS earthquake catalog lists an event with reviewed magnitude 7.0 or greater and origin time 2026-09-22 through 2026-10-21 UTC. |
| KKR-20260921-47 | 70% | 2026-10-01 | military/conflict | Iranian President Pezeshkian delivers a speech in person at the UN General Assembly general debate in New York between 2026-09-22 and 2026-09-29. | UN Web TV archive or UN Journal lists Pezeshkian speaking in person in the General Assembly Hall on a date 2026-09-22 through 2026-09-29. |
| KKR-20260921-48 | 20% | 2026-11-04 | military/conflict | The US and Iranian governments announce a ceasefire or cessation-of-hostilities agreement, confirmed by both governments, between 2026-09-22 and 2026-10-31. | Official statements from both the White House or State Department and the Iranian presidency or foreign ministry confirm a ceasefire agreement dated 2026-09-22 through 2026-10-31, reported by Reuters and Al Jazeera. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog adds 15 or more entries with dateAdded values between 2026-09-22 and 2026-10-19 inclusive." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A federal immigration agent involved in the 2026-09-20 Austin, Texas shooting is criminally charged between 2026-09-21 and 2026-12-18." → REJECTED: resolution offers alternative VENUES joined by 'or' (…texas state | or | federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2647 issued all-time across 16 forecaster arms · 2181 open (167 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 156 issued · 146 open · 2 resolved · 0 hits / 2 misses · **Brier 0.156** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 909 | 824 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 317 | 167 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 101 | 96 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 156 | 146 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*