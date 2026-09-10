**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102324Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-37 | 26% | 2026-09-18 | economics/markets | The FOMC raises the target range for the federal funds rate at its scheduled 2026-09-16 decision. Reference: 3.50 to 3.75 percent in effect on the packet date. | The FOMC statement dated 2026-09-16 on federalreserve.gov announces a target range whose upper bound exceeds 3.75 percent. Reference: 3.50 to 3.75 percent on 2026-09-10. |
| KKR-20260910-38 | 26% | 2026-10-13 | economics/markets | The front-month NYMEX WTI crude futures contract settles at or above 100.00 dollars per barrel on 2026-10-09. Reference: 100.05 on the packet date. | The CME Group published settlement price for the nearest-expiry NYMEX Light Sweet Crude Oil (CL) futures contract on 2026-10-09 is greater than or equal to 100.00. Reference: 100.05 on 2026-09-10. |
| KKR-20260910-39 | 26% | 2026-11-02 | economics/markets | The ECB Governing Council raises the deposit facility rate above 2.50 percent at its scheduled 2026-10-29 monetary policy meeting. Reference: 2.50 percent after the 2026-09-10 decision. | The ECB monetary policy decisions press release dated 2026-10-29 on ecb.europa.eu states a deposit facility rate greater than 2.50 percent. Reference: 2.50 percent on 2026-09-10. |
| KKR-20260910-40 | 28% | 2026-10-13 | cyber | CISA adds at least one Check Point vulnerability to the Known Exploited Vulnerabilities catalog between 2026-09-11 and 2026-10-09. | The CISA KEV catalog JSON contains at least one entry with vendorProject value Check Point (any product) and a dateAdded value between 2026-09-11 and 2026-10-09 inclusive. |
| KKR-20260910-41 | 28% | 2026-10-13 | cyber | A putative class action over the IDScan driver license breach is filed against IDScan.net in a US federal district court between 2026-09-10 and 2026-10-09. | A complaint pleaded as a class action, naming IDScan.net or its parent or affiliate as defendant and referencing the driver license data breach, appears on CourtListener or PACER with a filing date between 2026-09-10 and 2026-10-09. |
| KKR-20260910-42 | 56% | 2026-10-13 | military/conflict | Saudi forces conduct at least one airstrike inside Yemen between 2026-09-11 and 2026-10-09, ending the Saudi restraint that has held since the 2022 truce. | At least two of Reuters, AP and AFP report an airstrike on a target inside Yemen with a strike date between 2026-09-11 and 2026-10-09, attributed to Saudi forces by Saudi officials or the Saudi-led coalition. |
| KKR-20260910-43 | 56% | 2026-11-04 | military/conflict | The UN Security Council adopts a resolution addressing Iran between 2026-09-11 and 2026-10-30. | The UN Security Council 2026 resolutions list on un.org shows a resolution adopted between 2026-09-11 and 2026-10-30 with Iran in its title or with operative paragraphs on the Iranian nuclear programme or the US-Iran conflict. |
| KKR-20260910-44 | 35% | 2026-12-04 | political | Republicans retain control of the US House of Representatives in the 2026-11-03 midterm election. | By 2026-12-04 the Associated Press has called at least 218 of the 435 House races in the 2026-11-03 general election for Republican candidates. |
| KKR-20260910-45 | 10% | 2026-09-21 | crime/security | Daniel Owen Conahan Jr., the inmate convicted in the Hog Trail murders case, is executed by the State of Florida between 2026-09-10 and 2026-09-17. | The Florida Department of Corrections execution list records Daniel Owen Conahan Jr. as executed on a date between 2026-09-10 and 2026-09-17 inclusive. |
| KKR-20260910-46 | 31% | 2026-09-23 | disaster | GDACS raises tropical cyclone NORBERT-26 (eventid 1001320) to Orange or Red alert level at some point between 2026-09-10 and 2026-09-20. | The GDACS event page for tropical cyclone NORBERT-26 (eventtype TC, eventid 1001320) lists at least one episode dated between 2026-09-10 and 2026-09-20 with alert level Orange or Red. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

1854 issued all-time across 16 forecaster arms · 1518 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 583 issued · 545 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 583 | 545 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*