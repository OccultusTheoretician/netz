**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 262109Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-26_1518.md · forecaster: control/baserate · 7 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260926-49 | 64% | 2026-11-30 | military/conflict | Iran imposes a verified closure or blockade of the Strait of Hormuz to commercial oil tankers, lasting at least 24 continuous hours, with the closure occurring between 2026-10-03 and 2026-11-28. | Reuters, AP, or Lloyd's List Intelligence report commercial tanker transits through the Strait of Hormuz were halted for 24 or more continuous hours due to Iranian military or paramilitary action, within the window. |
| KKR-20260926-50 | 64% | 2026-10-26 | military/conflict | At least one additional militant attack causing five or more fatalities occurs in Pakistan between 2026-10-03 and 2026-10-24. | Two or more of AP, Reuters, AFP, Dawn, or Geo News report a single Pakistan attack in the window killing five or more people, attributed to militant action. |
| KKR-20260926-51 | 48% | 2026-11-13 | economics/markets | The 10-year US Treasury yield closes at or above 5.30 percent on 2026-11-13. Reference: 5.18 percent on 2026-09-26. | Treasury.gov or FRED series DGS10 shows the 10-year Treasury par yield closing at or above 5.30 percent on 2026-11-13. |
| KKR-20260926-52 | 48% | 2026-11-13 | economics/markets | WTI crude oil closes at or above 100.00 USD per barrel on 2026-11-13. Reference: 92.41 USD per barrel on 2026-09-26. | EIA or exchange settlement data shows WTI crude closing at or above 100.00 USD per barrel on 2026-11-13. |
| KKR-20260926-53 | 32% | 2026-11-02 | cyber | The CISA KEV catalog adds a new CVE for a Kiteworks, WSO2, or Adobe Commerce product, dateAdded between 2026-09-27 and 2026-10-31. | The CISA KEV catalog lists a Kiteworks, WSO2, or Adobe Commerce CVE with a dateAdded value between 2026-09-27 and 2026-10-31. |
| KKR-20260926-54 | 39% | 2026-11-16 | political | CNN remains excluded from the standing White House press pool rotation for Air Force One travel as of 2026-11-16. | WHCA statements or two independent outlets confirm CNN is excluded from the standard Air Force One pool rotation on 2026-11-16. |
| KKR-20260926-55 | 29% | 2026-12-17 | crime/security | A US, European, or UK law enforcement body announces an indictment, arrest, or sanctions action against a ShinyHunters- or Clop-linked individual or entity between 2026-10-03 and 2026-12-15. | DOJ, Europol, or NCA publishes an announcement, or a US court unseals an indictment, naming a ShinyHunters or Clop affiliate, dated in the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Brazil's October 4, 2026 presidential election fails to produce a first-round majority winner, triggering a second-round runoff on 2026-10-2" → REJECTED: statement and resolution assert opposite directions - the statement claims an absence and the resolution resolves TRUE on the event occurring. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "FEMA issues a major disaster declaration for at least one Northeast US state tied to the late-September 2026 nor'easter, between 2026-09-27 " → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2931 issued all-time across 17 forecaster arms · 2389 open (209 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1039 issued · 922 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1039 | 922 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 122 | 117 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 200 | 183 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 27 | 27 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 327 | 263 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*