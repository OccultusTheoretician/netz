**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212014Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-21_1516.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260921-33 | 29% | 2026-10-08 | cyber | The CISA KEV catalog will add a Cisco-vendor entry with dateAdded between 2026-09-21 and 2026-10-05. | True if CISA's KEV catalog lists an entry with vendorProject Cisco and dateAdded between 2026-09-21 and 2026-10-05, checked 2026-10-08. |
| KKR-20260921-34 | 24% | 2026-10-16 | economic | The US 10-Year Treasury yield will close below 4.70 percent on 2026-10-16. Reference: 4.96 percent on 2026-09-21. | True if Treasury.gov's Daily Par Yield Curve Rates or FRED series DGS10 shows the 10-Year yield below 4.70 percent on 2026-10-16. |
| KKR-20260921-35 | 40% | 2027-01-04 | political | Friedrich Merz will leave the German Chancellorship, by resignation, a successful no-confidence vote, or coalition collapse, between 2026-09-28 and 2026-12-31. | True if Reuters, dpa, or the Bundestag record report Merz left office via those routes between 2026-09-28 and 2026-12-31. |
| KKR-20260921-36 | 61% | 2026-11-17 | military_conflict | The White House or Chinese MFA will announce a formal US-China AI hotline in a statement issued between 2026-09-28 and 2026-11-15. | True if a White House readout or Chinese MFA briefing between 2026-09-28 and 2026-11-15 announces a bilateral AI crisis-communication channel. |
| KKR-20260921-37 | 23% | 2026-10-07 | crime_security | South Africa's NPA will file formal charges against at least one of the three men held in the murder case, between 2026-09-21 and 2026-10-05. | True if the NPA or a South African court record, per Reuters/BBC, shows charges filed against at least one man in that window. |
| KKR-20260921-38 | 23% | 2026-09-30 | crime_security | NSW Police will announce an arrest in the shooting of the 11-year-old boy in Sydney, occurring between 2026-09-21 and 2026-09-28. | True if NSW Police or a wire service (Guardian/BBC/AAP) reports an arrest in this case between 2026-09-21 and 2026-09-28. |
| KKR-20260921-39 | 29% | 2026-09-30 | disaster_infrastructure | Japanese authorities will confirm 10 or more fatalities from Typhoon Dujuan, for the period 2026-09-21 to 2026-09-28. | True if Japan's FDMA, NHK, or a wire service (Kyodo/Reuters/AP) reports 10+ confirmed Dujuan-attributed deaths for that window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "NYMEX WTI front-month crude will settle below 90.00 USD/barrel at close on 2026-10-15. Reference: 92.25 USD/barrel on 2026-09-21." → REJECTED: resolution offers alternative VENUES joined by 'or' (…settlement price on 2026-10-15, per cme group | or | a wire service, is below 90…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A federal court will enter a ruling in the CNN/MS NOW/Politico lawsuit against the Trump administration over White House press access, betwe" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date; the resolution names only a venue or register (PACER, courtlistener) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "USGS will record an M6.0+ earthquake within 300km of the Nikolski, Alaska M6.5 epicenter (us7000ti1p), between 2026-09-21 and 2026-09-28." → REJECTED: the resolution names only a venue or register (USGS) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

2638 issued all-time across 16 forecaster arms · 2172 open (167 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 909 issued · 824 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

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
| manual/fable-5.1/unattested | 147 | 137 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*