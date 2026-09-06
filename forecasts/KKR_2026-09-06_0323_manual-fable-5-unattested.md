**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060323Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: manual/fable-5/unattested · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-14 | 65% | 2026-10-02 | military/conflict | US forces conduct at least one additional military strike on Iranian military, IRGC, or Iranian state-owned assets between 2026-09-06 and 2026-09-30, following the 2026-09-05 strikes on three Iranian oil tankers. | At least two of Reuters, AP, BBC, Al Jazeera report a US strike on Iranian military, IRGC, or state-owned assets occurring between 2026-09-06 and 2026-09-30. |
| KKR-20260906-15 | 25% | 2026-10-08 | military/conflict | Iranian military or IRGC forces attack, board, or seize a commercial merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman between 2026-09-06 and 2026-10-05. | At least two of Reuters, AP, BBC, Al Jazeera report Iranian military or IRGC forces attacking, boarding, or seizing a commercial merchant vessel in those waters between 2026-09-06 and 2026-10-05. |
| KKR-20260906-16 | 75% | 2026-10-06 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for the Citrix NetScaler ADC or NetScaler Gateway authentication bypass with a dateAdded value between 2026-09-05 and 2026-10-02. | The public CISA KEV catalog contains an entry naming Citrix NetScaler ADC or NetScaler Gateway with an authentication bypass description and dateAdded between 2026-09-05 and 2026-10-02. |
| KKR-20260906-17 | 60% | 2027-03-04 | political | The Federal Register publishes a US Fish and Wildlife Service or Interior Department document proposing or finalizing removal of Endangered Species Act protections for the gray wolf, with publication date between 2026-09-08 and 2027-03-01. | federalregister.gov contains a FWS or Interior document proposing or finalizing gray wolf ESA delisting with publication date between 2026-09-08 and 2027-03-01. |
| KKR-20260906-18 | 50% | 2026-12-08 | crime/security | The Plymouth County District Attorney announces the office will retry Lindsay Clancy, or a retrial date is entered on the court docket, between 2026-09-06 and 2026-12-04. | An on-record DA retrial announcement carried by two of AP, Reuters, BBC, Boston Globe, or a Plymouth Superior Court docket entry scheduling retrial, dated between 2026-09-06 and 2026-12-04. |
| KKR-20260906-19 | 20% | 2027-03-02 | crime/security | The criminal trial of Andrew and Tristan Tate on the Romanian trafficking indictment opens with a first hearing on the merits between 2026-09-06 and 2027-02-26. | At least two of BBC, Reuters, AP report the Tate brothers criminal trial in Romania has held its opening hearing on the merits between 2026-09-06 and 2027-02-26. |
| KKR-20260906-20 | 12% | 2026-12-08 | political | The governments of Russia and Ukraine both announce a signed general ceasefire agreement between 2026-09-06 and 2026-12-04. | Official statements from both the Russian and Ukrainian governments announcing a signed general ceasefire, each carried by at least two of Reuters, AP, BBC, dated between 2026-09-06 and 2026-12-04. |
| KKR-20260906-21 | 20% | 2026-10-07 | disaster | USGS ComCat lists at least one earthquake of magnitude 6.0 or greater with epicenter between 50N and 55N latitude and 175W and 164W longitude, with origin time between 2026-09-06 and 2026-10-05 UTC. | The public USGS ComCat catalog contains at least one M6.0 or greater event inside the stated latitude-longitude box with origin time between 2026-09-06 and 2026-10-05 UTC. |
| KKR-20260906-22 | 15% | 2027-03-04 | political | An AfD politician is elected minister-president of a German state, or the AfD formally enters a state governing coalition, between 2026-09-06 and 2027-03-01. | At least two of Reuters, AP, Deutsche Welle, BBC report an AfD minister-president election or formal AfD entry into a state governing coalition between 2026-09-06 and 2027-03-01. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent crude front-month futures settle at or above 100.00 USD on at least one trading day between 2026-09-08 and 2026-10-09. Reference: " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1513 issued all-time across 16 forecaster arms · 1248 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 168 issued · 166 open · 2 resolved · 2 hits / 0 misses · **Brier 0.225** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 431 | 403 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 168 | 166 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 173 | 152 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*