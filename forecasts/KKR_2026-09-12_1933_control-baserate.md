**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121933Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: control/baserate · 6 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-20 | 26% | 2026-10-20 | economic | WTI crude front-month futures settle at or above 110.00 USD per barrel on any trading day between 2026-09-19 and 2026-10-17. Reference: 100.05 USD per barrel on 2026-09-12, the packet date | TRUE if any NYMEX WTI front-month settlement or EIA daily spot price in the window is 110.00 USD per barrel or higher; FALSE otherwise |
| KKR-20260912-21 | 28% | 2026-10-20 | cyber | CISA adds at least one Check Point-vendor CVE to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-19 and 2026-10-17 | TRUE if the CISA KEV catalog lists a Check Point-vendor CVE with dateAdded in the window; FALSE otherwise |
| KKR-20260912-22 | 35% | 2026-10-20 | political | OpenAI, Google DeepMind, or Meta issues an official statement or a named spokesperson is quoted by a major outlet addressing Dario Amodei's proposal to slow AI development, between 2026-09-19 and 2026-10-17 | TRUE if Reuters, AP, Bloomberg, CNBC, Guardian, or BBC quotes an official OpenAI, Google DeepMind, or Meta statement addressing the proposal in the window; FALSE otherwise |
| KKR-20260912-23 | 35% | 2026-10-20 | political | Ireland's Taoiseach or the Department of Foreign Affairs issues an on-record statement addressing Donald Trump's 12 September 2026 unified-Ireland remarks, between 2026-09-19 and 2026-10-17 | TRUE if RTE, Irish Times, or a wire service reports an on-record statement from the Taoiseach's office or Department of Foreign Affairs addressing the remarks in the window; FALSE otherwise |
| KKR-20260912-24 | 10% | 2026-10-20 | crime_security | Spanish or Catalan authorities confirm 5 or more arrests connected to the 12 September 2026 Barcelona Catalan national day clashes, in a statement or report between 2026-09-19 and 2026-10-17 | TRUE if a Spanish government, Catalan regional police, or wire-service report in the window states 5 or more arrests tied to the incident; FALSE otherwise |
| KKR-20260912-25 | 31% | 2026-09-26 | disaster_infrastructure | Indonesia's BNPB or BMKG attributes at least 1 fatality to the 12 September 2026 M6.5 earthquake near Teluknaga (USGS event us7000tgrk), in a report published by 2026-09-26 | TRUE if BNPB, BMKG, or a wire service attributes at least one fatality to this earthquake by the deadline; FALSE otherwise |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Yemeni government or Saudi-led coalition forces regain physical control of Mayun Island in the Bab al-Mandeb Strait at any point between 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…yemeni | or | saudi government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Israel and Lebanon confirm at least one resumed negotiating session on the track reported postponed on 12 September 2026, between 2026-09-19" → REJECTED: resolution offers alternative VENUES joined by 'or' (…israeli | or | lebanese government…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1976 issued all-time across 16 forecaster arms · 1640 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 631 issued · 593 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 631 | 593 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 211 | 208 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 226 | 220 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*