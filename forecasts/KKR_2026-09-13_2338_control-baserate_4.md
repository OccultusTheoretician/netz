**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 132338Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: control/baserate · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260913-53 | 56% | 2026-10-16 | military_conflict | Between 2026-09-14 and 2026-10-12, UKMTO publishes at least one incident advisory reporting a merchant vessel struck, attacked, or boarded in the Strait of Hormuz or Gulf of Oman. | TRUE if the UKMTO incident advisory list carries at least one entry with an incident date between 2026-09-14 and 2026-10-12 placing a vessel attack in the Strait of Hormuz or Gulf of Oman. |
| KKR-20260913-54 | 28% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog carries at least 20 entries with a dateAdded value between 2026-09-14 and 2026-11-13 inclusive. | TRUE if a fetch of the CISA KEV catalog JSON counts 20 or more entries whose dateAdded field falls between 2026-09-14 and 2026-11-13 inclusive. |
| KKR-20260913-55 | 35% | 2027-03-11 | political | Legislation authorizing a payment of at least 5000 USD per eligible person, characterized as a dividend or rebate, is signed into United States law between 2026-09-14 and 2027-03-05. | TRUE if Congress.gov lists a public law enacted inside the window authorizing per-person payments of 5000 USD or more characterized as a dividend or rebate. |
| KKR-20260913-56 | 10% | 2027-02-26 | crime_security | A Spanish court or the Spanish Council of Ministers issues a decision granting the United States extradition request for James Fergie Chambers, with the decision taken between 2026-09-14 and 2027-02-19. | TRUE if a Spanish judicial or government decision granting the US extradition request is issued inside the window and reported by two independent outlets. |
| KKR-20260913-57 | 31% | 2026-10-20 | disaster | Indonesian authorities state a death toll of 50 or more from the Java Sea passenger ship that capsized on 2026-09-13, with the statement issued between 2026-09-14 and 2026-10-14. | TRUE if Basarnas or another Indonesian government body states a confirmed or recovered toll of at least 50 dead for this vessel, corroborated by two independent wire services. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-14 and 2026-11-15, NATO announces Article 4 consultations convened at the request of Poland following a Russian strike, dron" → REJECTED: resolution offers alternative VENUES joined by 'or' (…nato press release | or | official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "ICE Brent front-month crude futures settle at or above 120.00 USD per barrel on at least one trading day between 2026-09-14 and 2026-11-30. " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "FRED series DGS10 records a value of 5.25 percent or higher on at least one business day between 2026-09-14 and 2026-12-15. Reference: 4.97 " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes at or below 7000.00 on at least one trading day between 2026-09-14 and 2026-12-18. Reference: 7656.98 at the packet-date " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Swedish Riksdag holds a prime ministerial vote after the 2026-09-13 general election and installs a prime minister, with the vote occurr" → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition

## III. LEDGER STANDING

2069 issued all-time across 16 forecaster arms · 1733 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 674 issued · 636 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 674 | 636 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*