**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171625Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-17_1518.md · forecaster: manual/fable-5.1/unattested · 10 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260917-15 | 25% | 2026-11-04 | military/conflict | Between 2026-09-18 and 2026-10-31, the United States and Iran announce a ceasefire or cessation-of-hostilities agreement covering combat between US and Iranian forces, confirmed publicly by both governments. | TRUE if, between 2026-09-18 and 2026-10-31, the US government and the Iranian government each publicly confirm a ceasefire or cessation-of-hostilities agreement covering US-Iran combat operations, reported by at least two of Reuters, AP, AFP. |
| KKR-20260917-16 | 10% | 2026-10-20 | military/conflict | Between 2026-09-18 and 2026-10-16, India or Pakistan officially acknowledges at least one of its own uniformed personnel killed by fire from the forces of the other country. | TRUE if, between 2026-09-18 and 2026-10-16, the Indian Ministry of Defence, Indian Army, Pakistan ISPR, or Pakistan Navy officially acknowledges at least one of its own uniformed personnel killed by fire from the forces of the other country. |
| KKR-20260917-17 | 35% | 2026-10-26 | economics/markets | The FRED series DCOILWTICO (WTI Cushing spot price) observation dated 2026-10-16 is below 95.00 USD per barrel. Reference: WTI 101.09 on the packet date 2026-09-17. | TRUE if the FRED series DCOILWTICO observation dated 2026-10-16 is below 95.00. If FRED carries no observation for that date, use the EIA daily WTI Cushing spot price for 2026-10-16. Reference: 101.09 on the packet date. |
| KKR-20260917-18 | 35% | 2026-11-02 | economics/markets | At its scheduled October 2026 meeting (statement expected 2026-10-28), the FOMC raises the federal funds target range above the range set at its September 2026 meeting. | TRUE if the FOMC statement released at the conclusion of its scheduled October 2026 meeting (expected 2026-10-28) sets a federal funds target range higher than the range set at the September 2026 meeting, per federalreserve.gov press releases. |
| KKR-20260917-19 | 20% | 2026-11-06 | economics/markets | Between 2026-09-18 and 2026-10-31, the US President signs an executive order or proclamation imposing new or increased tariffs applying specifically to goods originating in the European Union. | TRUE if the Federal Register publishes an executive order or presidential proclamation, signed between 2026-09-18 and 2026-10-31, imposing new or increased tariff rates that apply specifically to goods originating in the European Union or its member states. |
| KKR-20260917-20 | 30% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry for an Issabel product with a dateAdded value between 2026-09-17 and 2026-10-30. | TRUE if the CISA KEV catalog JSON contains at least one entry whose vendorProject or product field names Issabel, with dateAdded between 2026-09-17 and 2026-10-30 inclusive. |
| KKR-20260917-21 | 60% | 2026-10-20 | cyber | Between 2026-09-18 and 2026-10-16, Microsoft releases a fix and marks the Windows 11 domain trust and domain login issue introduced by update KB5124008 as Resolved. | TRUE if Microsoft Windows release health or the KB5124008 support article shows the domain trust or domain login known issue with status Resolved and a resolution date between 2026-09-18 and 2026-10-16, on the live page or an archive.org capture. |
| KKR-20260917-22 | 60% | 2026-11-10 | political | Between 2026-09-28 and 2026-11-06, the Riksdag approves a prime minister nominated by the speaker following the September 2026 Swedish general election. | TRUE if the Riksdag voting record on riksdagen.se shows a prime minister vote held between 2026-09-28 and 2026-11-06 in which fewer than 175 members voted no, so that the nominee was approved. |
| KKR-20260917-23 | 22% | 2026-10-19 | disaster | Between 2026-09-18 00:00 UTC and 2026-10-15 23:59 UTC, an earthquake of magnitude 5.5 or greater occurs with epicenter within 150 km of USGS event us7000ti1p (M6.5, Fox Islands, Alaska, 2026-09-17). | TRUE if the USGS earthquake catalog lists at least one event of magnitude 5.5 or greater with epicenter within 150 km of USGS event us7000ti1p and origin time between 2026-09-18 00:00 UTC and 2026-10-15 23:59 UTC. |
| KKR-20260917-24 | 15% | 2027-01-05 | crime/security | Following the US House vote on Leon Black reported 2026-09-16, a federal criminal charge of contempt of Congress against Leon Black is filed between 2026-09-18 and 2026-12-31. | TRUE if a criminal information or indictment charging Leon Black with contempt of Congress under 2 USC 192 is filed in a US federal district court with a docket filing date between 2026-09-18 and 2026-12-31, per PACER or CourtListener. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2389 issued all-time across 16 forecaster arms · 1923 open (82 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 131 issued · 121 open · 2 resolved · 0 hits / 2 misses · **Brier 0.156** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 805 | 720 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 286 | 136 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 81 | 76 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 131 | 121 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 273 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 252 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*