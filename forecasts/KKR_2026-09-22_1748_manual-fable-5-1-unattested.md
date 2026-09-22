**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221748Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-22_1518.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260922-10 | 40% | 2026-10-16 | economics/markets | ICE Brent front-month futures settle above 100.00 USD per barrel on 2026-10-16. Reference: 100.03 on the packet date. | True if the ICE Brent front-month settlement price published for 2026-10-16 is strictly above 100.00. Reference: 100.03 on the packet date. |
| KKR-20260922-11 | 55% | 2026-10-08 | cyber | The CISA KEV catalog adds an entry for the VeloCloud Orchestrator vulnerability with a date-added value between 2026-09-22 and 2026-10-06. | True if the CISA KEV catalog contains an entry whose product field references VeloCloud Orchestrator or VeloCloud SD-WAN Orchestrator and whose dateAdded is between 2026-09-22 and 2026-10-06 inclusive. |
| KKR-20260922-12 | 40% | 2026-10-15 | cyber | The CISA KEV catalog adds an entry for a D-Link DIR-822A router vulnerability with a date-added value between 2026-09-22 and 2026-10-13. | True if the CISA KEV catalog contains an entry whose product or description field references DIR-822A and whose dateAdded is between 2026-09-22 and 2026-10-13 inclusive. |
| KKR-20260922-13 | 30% | 2026-10-22 | cyber | The CISA KEV catalog adds an entry for a Microsoft Defender or Windows Defender vulnerability with a date-added value between 2026-09-22 and 2026-10-20. | True if the CISA KEV catalog contains an entry whose product field references Microsoft Defender or Windows Defender and whose dateAdded is between 2026-09-22 and 2026-10-20 inclusive. |
| KKR-20260922-14 | 30% | 2026-10-22 | military/conflict | Between 2026-09-22 and 2026-10-20, at least two of Reuters, AP, AFP, and BBC report that Houthi forces have taken control of the Kahboub Mountains in Yemen. | True if at least two of Reuters, AP, AFP, BBC publish reports dated 2026-09-22 to 2026-10-20 stating Houthi forces control the Kahboub Mountains or Kahboub heights. |
| KKR-20260922-15 | 45% | 2026-11-13 | political | In the federal lawsuit filed by CNN, MS NOW, and Politico against the Trump administration over press access, the court docket records a ruling on a motion for temporary restraining order or preliminary injunction between 2026-09-22 and 2026-11-10. | True if the PACER docket for the CNN, MS NOW, Politico press-access suit shows an order granting or denying a TRO or preliminary injunction entered between 2026-09-22 and 2026-11-10 inclusive. |
| KKR-20260922-16 | 50% | 2026-11-03 | crime/security | Between 2026-09-22 and 2026-10-30, a Sri Lankan court hands down sentences to at least one of the 15 men convicted on 2026-09-22 over the 2019 Easter Sunday bombings, as reported by at least two of Reuters, AP, AFP, and BBC. | True if at least two of Reuters, AP, AFP, BBC report, dated 2026-09-22 to 2026-10-30, a sentence pronounced on at least one of the 15 convicted defendants. |
| KKR-20260922-17 | 30% | 2026-10-08 | disaster | Between 2026-09-22 and 2026-10-06, the confirmed death toll in Japan attributed to Typhoon Dujuan reaches at least 10, per Japan Fire and Disaster Management Agency figures or two of Reuters, AP, AFP, and NHK. | True if the FDMA or two of Reuters, AP, AFP, NHK report, dated 2026-09-22 to 2026-10-06, a confirmed Typhoon Dujuan death toll in Japan of 10 or more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FRED DGS10 series value for 2026-10-15 is at or above 5.00 percent. Reference: 4.96 percent on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-09-22 and 2026-10-20, at least two of Reuters, AP, AFP, and Bloomberg report an official Iranian government statement declaring" → REJECTED: resolution offers alternative VENUES joined by 'or' (…26-09-22 to 2026-10-20, an iranian government | or | irgc statement that the strait of hormuz is r…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2673 issued all-time across 16 forecaster arms · 2207 open (193 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 164 issued · 154 open · 2 resolved · 0 hits / 2 misses · **Brier 0.156** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 918 | 833 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 324 | 174 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 103 | 98 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 164 | 154 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*