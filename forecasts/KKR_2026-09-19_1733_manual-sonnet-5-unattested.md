**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191733Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-19_1516.md · forecaster: manual/sonnet-5/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260919-33 | 65% | 2026-10-19 | cyber | CISA will add at least one Linux Kernel entry to its Known Exploited Vulnerabilities catalog with dateAdded between 2026-09-26 and 2026-10-17. | TRUE if the CISA KEV catalog lists a Linux Kernel entry with dateAdded in 2026-09-26 to 2026-10-17, checked 2026-10-19; else FALSE. |
| KKR-20260919-34 | 12% | 2026-10-12 | disaster_infrastructure | GDACS event 1032222, the Australia forest fire tracked Green since day 60 of coverage, will be upgraded to Orange or Red between 2026-09-26 and 2026-10-10. | TRUE if the GDACS report page for event 1032222 shows Orange or Red alert level at any point in the window, checked 2026-10-12; else FALSE. |
| KKR-20260919-35 | 22% | 2026-10-12 | disaster_infrastructure | USGS will record at least one magnitude 5.0+ aftershock within 200 km of event us7000ti1p, the 19 Sep M6.5 Nikolski Alaska quake, between 2026-09-26 and 2026-10-10. | TRUE if the USGS catalog lists an M5.0+ quake within 200 km of us7000ti1p dated 2026-09-26 to 2026-10-10, checked 2026-10-12; else FALSE. |
| KKR-20260919-36 | 30% | 2026-10-26 | economic | The 10-year Treasury yield, FRED series DGS10, will close at or above 5.15 percent, Reference: 5.00 percent on the 2026-09-19 packet date, between 2026-09-28 and 2026-10-23. | TRUE if FRED series DGS10 shows a daily value of 5.15 or higher for any date 2026-09-28 to 2026-10-23, checked 2026-10-26; else FALSE. |
| KKR-20260919-37 | 35% | 2026-10-19 | military_conflict | The Polish Ministry of National Defence, its Operational Command, or NATO will confirm a Russian-origin drone or missile entered Polish airspace between 2026-09-26 and 2026-10-17. | TRUE if Polish authorities or NATO officially confirm a Russian-origin airspace incursion dated 2026-09-26 to 2026-10-17, wire-reported by 2026-10-19; else FALSE. |
| KKR-20260919-38 | 25% | 2026-10-13 | crime_security | The Saudi Press Agency or Saudi Ministry of Defence will publicly attribute the 19 Sep 2026 Riyadh alerts and airport-area smoke to hostile launch or false alarm, between 2026-09-26 and 2026-10-10. | TRUE if SPA or the Saudi MOD states a cause, hostile launch or false alarm, in the window, confirmed by Reuters or AP, checked 2026-10-13; else FALSE. |
| KKR-20260919-39 | 48% | 2026-12-21 | political | Trump and Xi will hold a confirmed bilateral meeting, in person or virtual, between 2026-09-26 and 2026-12-18. | TRUE if the White House or the Chinese Foreign Ministry issues an official readout confirming a Trump-Xi meeting occurred within the window, checked 2026-12-21; else FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude front-month will settle below 90.00 USD per barrel, Reference: 96.08 on the 2026-09-19 packet date, on any session between 2026-09" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…cme | or | eia settlement data show wti front-month belo…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "MS NOW, CNN, or Politico will file a US federal lawsuit over the September 2026 White House press-access ban between 2026-09-26 and 2026-11-" → REJECTED: resolution offers alternative VENUES joined by 'or' (…federal court docket | or | wire…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Nscale, the AI cloud infrastructure provider that filed to go public, will begin trading on a public stock exchange between 2026-09-26 and 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…xchange within the window, per listing notice | or | sec edgar, checked 2026-12-21…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2539 issued all-time across 16 forecaster arms · 2073 open (157 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 277 issued · 229 open · 43 resolved · 21 hits / 22 misses · **Brier 0.207** against its own base rate 48.8% (climatological 0.250) · **skill +0.172**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 869 | 784 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 301 | 151 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 91 | 86 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 141 | 131 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 299 | 282 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 277 | 229 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*