**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152210Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-45 | 56% | 2026-11-04 | military/conflict | Between 2026-09-16 and 2026-10-31, the governments of the United States and Iran both publicly commit to a ceasefire or cessation of hostilities between the two countries. | TRUE if, between 2026-09-16 and 2026-10-31, the US President or White House and the Iranian government each publicly confirm a US-Iran ceasefire or cessation of hostilities, as reported by Reuters or AP. |
| KKR-20260915-46 | 56% | 2026-10-02 | military/conflict | Between 2026-09-16 and 2026-09-29, at least one merchant vessel is attacked or seized by armed forces or armed attackers in the Persian Gulf, Strait of Hormuz, or Gulf of Oman. | TRUE if UKMTO reports a merchant vessel struck by projectile, drone, mine, or explosive, fired upon, or seized in the Persian Gulf, Strait of Hormuz, or Gulf of Oman, with an incident date between 2026-09-16 and 2026-09-29. |
| KKR-20260915-47 | 56% | 2026-10-19 | military/conflict | Between 2026-09-16 and 2026-10-15, at least one NATO member state formally requests consultations under Article 4 of the North Atlantic Treaty. | TRUE if NATO or the requesting government publicly confirms a formal Article 4 consultation request made between 2026-09-16 and 2026-10-15; otherwise FALSE. |
| KKR-20260915-48 | 26% | 2026-11-12 | economics/markets | The EIA Cushing WTI crude spot price (FRED series DCOILWTICO) is at or below 90.00 dollars per barrel on at least one observation date between 2026-09-16 and 2026-10-30. Reference: WTI 104.64 dollars per barrel in the 2026-09-15 packet market snapshot. | TRUE if FRED series DCOILWTICO shows a daily value at or below 90.00 for any observation date between 2026-09-16 and 2026-10-30; otherwise FALSE. Reference: 104.64 on 2026-09-15. |
| KKR-20260915-49 | 26% | 2026-11-04 | economics/markets | The 10-year Treasury constant-maturity yield (FRED series DGS10) is 5.50 percent or higher on at least one observation date between 2026-09-16 and 2026-10-30. Reference: 10-year yield 4.99 percent in the 2026-09-15 packet market snapshot. | TRUE if FRED series DGS10 shows a daily value of 5.50 or higher for any observation date between 2026-09-16 and 2026-10-30; otherwise FALSE. Reference: 4.99 percent on 2026-09-15. |
| KKR-20260915-50 | 28% | 2026-10-22 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Microsoft Windows vulnerability with a dateAdded value between 2026-10-13 and 2026-10-19, the week of the October 2026 Patch Tuesday. | TRUE if the CISA KEV JSON feed lists at least one entry with vendorProject Microsoft, a product field containing Windows or Win32k, and dateAdded between 2026-10-13 and 2026-10-19; otherwise FALSE. |
| KKR-20260915-51 | 28% | 2026-11-04 | cyber | CISA issues at least one new Emergency Directive between 2026-09-16 and 2026-10-30. | TRUE if the Cybersecurity Directives listing on cisa.gov shows an Emergency Directive with an issue date between 2026-09-16 and 2026-10-30; otherwise FALSE. |
| KKR-20260915-52 | 31% | 2026-10-26 | disaster | Between 2026-09-22 and 2026-10-21, Catania Fontanarossa airport suspends or restricts flight operations because of volcanic ash from Mount Etna on at least one day. | TRUE if airport operator SAC or aviation authority ENAC announces, or ANSA reports, an Etna-ash suspension or restriction of Catania airport operations on any day between 2026-09-22 and 2026-10-21; otherwise FALSE. |
| KKR-20260915-53 | 10% | 2026-10-20 | crime/security | Between 2026-09-16 and 2026-10-16, Dutch police or prosecutors announce at least one arrest in connection with the suspected sabotage that disrupted Netherlands rail services, reported on 2026-09-15. | TRUE if Dutch police (politie.nl) or the Public Prosecution Service (om.nl) announce an arrest, made between 2026-09-16 and 2026-10-16, linked to the rail sabotage reported on 2026-09-15; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-16 and 2026-10-30, the US government files a notice of appeal or a motion for a stay pending appeal against the federal cour" → REJECTED: resolution offers alternative VENUES joined by 'or' (…district | or | appellate…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2192 issued all-time across 16 forecaster arms · 1856 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 724 issued · 686 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

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
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*