**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232215Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-23_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260923-50 | 64% | 2026-10-12 | military_conflict | Between 2026-09-24 and 2026-10-08, Russia and Ukraine jointly implement a verified pause in strikes on each other's energy infrastructure, confirmed by wire reporting from both Russian- and Ukrainian-aligned sources. | Independent wire reporting, corroborated across both Russian- and Ukrainian-aligned channels, confirms an actually implemented halt to energy-infrastructure strikes by both sides during the window; a proposal or one-sided pause is a MISS. |
| KKR-20260923-51 | 48% | 2026-10-16 | economic | Reference: 5.06 percent on 2026-09-23 (packet date, per the report market snapshot). The FRED DGS10 10-Year Treasury constant maturity yield closes at or above 5.20 percent on 2026-10-14. | FRED series DGS10 shows a value at or above 5.20 percent for 2026-10-14, or, if that date is not a trading day, for the next trading day; any lower value is a MISS. |
| KKR-20260923-52 | 32% | 2026-10-12 | cyber | Between 2026-09-24 and 2026-10-08, CISA adds a networking, VPN, or security-gateway appliance product from a vendor other than Arista, F5, or Check Point to the Known Exploited Vulnerabilities catalog. | The CISA KEV catalog carries a date-added value between 2026-09-24 and 2026-10-08 for an entry in the networking, VPN, or security-gateway appliance category from a vendor other than Arista, F5, or Check Point. |
| KKR-20260923-53 | 32% | 2026-10-12 | cyber | Between 2026-09-24 and 2026-10-08, the FBI or DOJ issues an on-record statement confirming a data breach of FBI personnel or case records consistent with the ShinyHunters breach claim. | A wire service (Reuters, AP) reports an on-record FBI or DOJ statement confirming the breach during the window; a no-comment, denial, or silence through the deadline is a MISS. |
| KKR-20260923-54 | 39% | 2026-10-12 | political | Between 2026-09-24 and 2026-10-08, US Treasury OFAC designates at least one new individual or entity under an Iran-related sanctions program. | OFAC's Recent Actions page or SDN list shows a new Iran-program designation dated in the window; no such listing by the deadline is a MISS. |
| KKR-20260923-55 | 29% | 2026-10-12 | crime_security | Between 2026-09-24 and 2026-10-08, the South African Police Service publicly announces the arrest of at least one suspect in the eleven-fatality house shooting reported 2026-09-23. | SAPS or a wire service reports a named arrest tied to this specific shooting during the window; an investigation continuing with no suspect in custody by the deadline is a MISS. |
| KKR-20260923-56 | 31% | 2026-10-05 | disaster_infrastructure | Between 2026-09-25 and 2026-10-02, the National Weather Service issues a Coastal Flood Warning, High Wind Warning, or Storm Warning for a New York City or Boston metro forecast zone. | The NWS public alerts archive shows at least one such warning issued for an NYC or Boston metro zone inside the window; no such warning issued is a MISS. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-24 and 2026-10-08, Ethiopian federal or allied forces and Tigray-aligned forces engage in at least one wire-reported armed c" → REJECTED: the resolution names only a venue or register (AFP, AP, BBC, Jazeera) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Reference: 91.30 USD/bbl on 2026-09-23 (packet date, prior-session close). WTI crude front-month futures settle at or above 100.00 USD/bbl o" → REJECTED: resolution offers alternative VENUES joined by 'or' (…cme | or | eia settlement data shows a wti front-month c…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-24 and 2026-10-15, a federal court issues a ruling granting or denying a preliminary injunction or restraining order in liti" → REJECTED: the resolution names a different subject than the statement — the claim is about CNN, House, MS, NOW and the resolution settles on MISS, TRO. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2767 issued all-time across 16 forecaster arms · 2225 open (153 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 964 issued · 847 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 964 | 847 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 108 | 103 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 173 | 156 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 306 | 242 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*