**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102324Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 4 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-15 | 15% | 2026-09-28 | military_conflict | The Saudi-led coalition conducts an airstrike on Houthi forces in or near Mocha, Yemen, between 2026-09-17 and 2026-09-24. | TRUE if confirmed by one Saudi or coalition-aligned source and one Houthi-aligned source, or by two wire services among Reuters, AP, and AFP, reporting a strike near Mocha. |
| KKR-20260910-16 | 32% | 2026-09-17 | economic | The Federal Open Market Committee raises the federal funds rate target range above 3.50 to 3.75 percent at its meeting concluding 2026-09-16 (Reference: range held at 3.50 to 3.75 percent since the 2026-07-29 meeting). | TRUE per the Federal Reserve Board's official post-meeting statement at federalreserve.gov, released 2:00 PM ET on 2026-09-16, showing a target range with lower bound above 3.50 percent. |
| KKR-20260910-17 | 18% | 2026-10-19 | cyber | Anthropic or another frontier AI developer discloses a new AI-orchestrated hacking incident, distinct from the Claude Opus 4.6 incident reported 2026-09-10, between 2026-09-17 and 2026-10-17. | TRUE if a frontier AI developer's official disclosure, or two outlets among Reuters, Bloomberg, The Hacker News, and BleepingComputer, report a new incident in the window distinct from the 2026-09-10 one. |
| KKR-20260910-18 | 8% | 2026-11-19 | political | Congress enacts legislation, or the federal government begins disbursing, a direct per-adult payment of approximately 5000 US dollars described as a dividend, between 2026-09-17 and 2026-11-17. | TRUE if the Federal Register, a signed law at congress.gov, or a Treasury or IRS notice confirms enactment or disbursement in the window. A proposal or promise alone does not satisfy this. |
| KKR-20260910-19 | 12% | 2026-10-19 | political | A court order or legislative action reinstates the 2025 Republican-redrawn congressional map for Missouri's November 2026 election, occurring between 2026-09-17 and 2026-10-15 (Reference: the US Supreme Court twice declined to reinstate that map, on 2026-09-08 and 2026-09-10). | TRUE if the Missouri Secretary of State, or two wire services among AP and Reuters, confirm a reinstatement of the 2025 map for the November election within the window. |
| KKR-20260910-20 | 28% | 2026-11-17 | crime_security | The Crown Prosecution Service or Metropolitan Police confirm that either person arrested 2026-09-09 in London on suspicion of assisting Iran's foreign intelligence service has been formally charged, between 2026-10-15 and 2026-11-15. | TRUE if the Metropolitan Police or CPS confirm a charge against either individual in the window, or two outlets among Reuters, PA Media, and BBC report it citing official confirmation. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The United States conducts a military strike on Iran's Pickaxe Mountain facility, the underground site near Natanz also called Kuh-e Kolang " → REJECTED: resolution offers alternative VENUES joined by 'or' (…us dod | or | centcom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "WTI crude oil settles at or above 108.00 US dollars per barrel on at least one trading day between 2026-09-17 and 2026-10-01 (Reference: 100" → REJECTED: resolution offers alternative VENUES joined by 'or' (…cme group | or | us eia daily price data show a nymex wti fron…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "CISA adds at least 4 new entries to its Known Exploited Vulnerabilities catalog, each with a dateAdded value between 2026-09-17 and 2026-09-" → REJECTED: the resolution names only a venue or register (CISA, KEV, json) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "The National Weather Service issues at least one new Extreme Heat Warning for a continental US location between 2026-09-17 and 2026-09-24 (R" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1828 issued all-time across 16 forecaster arms · 1492 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 205 issued · 173 open · 32 resolved · 16 hits / 16 misses · **Brier 0.224** against its own base rate 50.0% (climatological 0.250) · **skill +0.105**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 567 | 529 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*