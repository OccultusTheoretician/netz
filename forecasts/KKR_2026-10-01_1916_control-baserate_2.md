**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011916Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-01_1613.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261001-37 | 48% | 2026-10-09 | economics/markets | Tesla Q3 2026 total vehicle deliveries, published in its production and deliveries release between 2026-10-01 and 2026-10-06, come in below the Q3 2025 record of 497,099. Reference: Q2 2026 deliveries were 480,126. | True if the total deliveries figure in the Tesla Q3 2026 production and deliveries release (ir.tesla.com or SEC Form 8-K) issued between 2026-10-01 and 2026-10-06 is 497,098 or lower; false otherwise. |
| KKR-20261001-38 | 39% | 2026-11-13 | political | In the Knesset election held on 2026-10-27, lists containing Likud, Shas, United Torah Judaism, Otzma Yehudit or Religious Zionism (the Netanyahu bloc) win a combined 61 or more of the 120 seats. | True if Central Elections Committee official final results for the 2026-10-27 Knesset election give lists containing Likud, Shas, United Torah Judaism, Otzma Yehudit or Religious Zionism a combined 61 or more seats; false otherwise. |
| KKR-20261001-39 | 64% | 2026-12-04 | military/conflict | The United States and Iran both publicly confirm a mutually agreed ceasefire or agreement ending hostilities between 2026-10-02 and 2026-11-30. | True if between 2026-10-02 and 2026-11-30 the White House and the Iranian government each publicly confirm a mutually agreed US-Iran ceasefire or end-of-war deal, per Reuters or AP; unilateral pauses do not count. |
| KKR-20261001-40 | 48% | 2027-01-06 | economics/markets | The 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one trading day between 2026-10-02 and 2026-12-31. Reference: 5.25 percent on the packet date. | True if FRED series DGS10 shows any daily value of 5.50 or higher dated between 2026-10-02 and 2026-12-31 inclusive; false otherwise. |
| KKR-20261001-41 | 32% | 2027-01-06 | cyber | CISA adds CVE-2026-102489 or CVE-2026-102490, the Zammad zero-days DIVD says were exploited in its breach, to the Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-12-31. | True if the CISA KEV catalog carries CVE-2026-102489 or CVE-2026-102490 with a dateAdded value between 2026-10-01 and 2026-12-31 inclusive; false otherwise. |
| KKR-20261001-42 | 32% | 2027-01-06 | cyber | CISA adds a Kiteworks vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-12-31, following the patch for a maximum-severity code injection flaw in its email protection gateway. | True if the CISA KEV catalog carries an entry with vendorProject Kiteworks or Accellion and a dateAdded value between 2026-10-01 and 2026-12-31 inclusive; false otherwise. |
| KKR-20261001-43 | 29% | 2027-03-29 | crime/security | Tennessee carries out at least one execution between 2026-10-02 and 2027-03-24, after Governor Bill Lee halted the remaining 2026 execution following the failed Christa Pike lethal injection. | True if the Death Penalty Information Center execution database lists any Tennessee execution dated between 2026-10-02 and 2027-03-24 inclusive; false otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At its scheduled 2026-10-28 decision, the FOMC raises the federal funds target range above 3.75-4.00 percent. Reference: target range 3.75-4" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "After the 2026-11-03 US midterm elections, Democrats plus independents caucusing with them hold at least 51 seats in the Senate of the 120th" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The NOAA CPC Relative Oceanic Nino Index for October-December 2026 reaches +2.5 C or higher, a strength CPC says no El Nino since 1950 has r" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2027-01-15 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

3204 issued all-time across 18 forecaster arms · 2662 open (348 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1147 issued · 1030 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1147 | 1030 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 354 | 204 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 154 | 149 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 239 | 222 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 64 | 64 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 17 | 17 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*