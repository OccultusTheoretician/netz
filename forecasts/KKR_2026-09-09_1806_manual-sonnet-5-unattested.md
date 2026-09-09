**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091806Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-09_1530.md · forecaster: manual/sonnet-5/unattested · 7 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260909-06 | 85% | 2026-10-13 | military/conflict | US or Iranian forces will conduct at least one additional confirmed kinetic engagement (missile, drone, naval gunfire, or boarding/seizure action) against the other sides vessels or forces in the Strait of Hormuz, Persian Gulf, or Gulf of Oman theater, in the window between 2026-09-10 and 2026-10-09. | At least two independent outlets (from the packets AXIS, IL, RU, or WEST corroboration sides, or a CENTCOM/DoD or Iranian government statement) report a new US-Iran kinetic engagement beyond the tanker-destruction and submarine-dispute incidents already logged as of 2026-09-09, occurring inside the window; checked 2026-10-13. |
| KKR-20260909-07 | 15% | 2026-11-11 | military/conflict | A US-Iran ceasefire or truce covering the Strait of Hormuz theater will be publicly announced by a government on either side AND hold with zero further reported US-Iran kinetic incidents for at least 14 consecutive days, within the window between 2026-09-10 and 2026-11-08. | A wire-service or official (White House, CENTCOM, or Iranian foreign ministry) ceasefire or truce announcement is on record AND no US-Iran kinetic incident in this theater is reported by any tracked outlet for the 14 days following that announcement, with the 14-day window closing inside 2026-09-10 to 2026-11-08; checked 2026-11-11. |
| KKR-20260909-08 | 38% | 2026-11-10 | economics/markets | ICE Brent crude will settle at or above 110.00 USD per barrel on at least one trading day between 2026-09-10 and 2026-11-06. Reference: 101.13 USD per barrel on the packet date of 2026-09-09. | ICE Brent front-month futures settlement price, as reported by ICE, the EIA, or a Reuters/Bloomberg market-close report, reaches or exceeds 110.00 USD per barrel on any trading day in the window; checked against the settlement record on 2026-11-10. |
| KKR-20260909-09 | 70% | 2026-10-02 | cyber | The Chrome V8 zero-day reported on 2026-09-09 as exploited in the wild and enabling code execution will be added to the CISA Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-10 and 2026-09-30. | The CISA KEV catalog at cisa.gov/known-exploited-vulnerabilities-catalog carries an entry for a Google Chrome or Chromium V8 vulnerability with a date-added value between 2026-09-10 and 2026-09-30 inclusive; checked 2026-10-02. |
| KKR-20260909-10 | 32% | 2026-10-13 | cyber | The Microsoft Defender zero-day covered in 2026-09-08 to 09 reporting under the names ShieldCrash and ShieldBreak, granting SYSTEM access, will be added to the CISA Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-10 and 2026-10-08. | The CISA KEV catalog carries an entry for a Microsoft Defender vulnerability matching the ShieldCrash/ShieldBreak coverage, with a date-added value between 2026-09-10 and 2026-10-08 inclusive; checked 2026-10-13. |
| KKR-20260909-11 | 65% | 2026-11-06 | political | Chris Pappas, the Democratic nominee, will win the New Hampshire US Senate general election held 2026-11-03 against Republican nominee John E. Sununu for the seat being vacated by retiring Senator Jeanne Shaheen. | The Associated Press or the New Hampshire Secretary of State declares Chris Pappas the winner of the 2026-11-03 US Senate general election in New Hampshire; checked 2026-11-06. |
| KKR-20260909-12 | 18% | 2026-12-18 | crime/security | The Metropolitan Police inquiry into alleged overseas donations to Reform UK, opened in the week of 2026-09-09, will reach a publicly announced conclusion, either referral for charge or prosecution, or formal closure without action, within the window between 2026-09-16 and 2026-12-16. | The Metropolitan Police issues a statement, or one is reported by at least two of Reuters, PA Media, the BBC, or the Guardian, that the Reform UK overseas-donations inquiry has concluded, either by referral for charge/prosecution or formal closure without action, within the window; checked 2026-12-18. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 will close at or above 8,000.00 on at least one trading day between 2026-09-10 and 2027-02-26. Reference: 7,627.27 on the packet" → REJECTED: the resolution names a different subject than the statement — the claim is about Reference and the resolution settles on Bloomberg, Dow, Indices, Jones. A row whose resolution checks a different fact can be scored correct while being wrong
- "At least one of the four Green-rated GDACS forest fire alerts logged on 2026-09-09 in Angola (event 1031789), the Democratic Republic of Con" → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

1755 issued all-time across 16 forecaster arms · 1419 open (47 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 199 issued · 167 open · 32 resolved · 16 hits / 16 misses · **Brier 0.224** against its own base rate 50.0% (climatological 0.250) · **skill +0.105**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 537 | 499 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 240 | 111 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 188 | 185 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 206 | 200 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*