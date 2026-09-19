**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191732Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-19_1516.md · forecaster: control/baserate · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260919-16 | 29% | 2026-10-13 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field names Orkes Conductor, with a date-added value between 2026-09-19 and 2026-10-09. | The CISA KEV JSON feed contains an entry with vendorProject or product matching Orkes or Conductor and dateAdded between 2026-09-19 and 2026-10-09 inclusive. |
| KKR-20260919-17 | 29% | 2026-10-20 | cyber | The CISA KEV catalog adds the SolarWinds ARM hard-coded key vulnerability disclosed 2026-09-19, with a date-added value between 2026-09-19 and 2026-10-16. | The CISA KEV JSON feed contains an entry with vendorProject SolarWinds and product Access Rights Manager or ARM whose dateAdded falls between 2026-09-19 and 2026-10-16 inclusive. |
| KKR-20260919-18 | 24% | 2026-11-03 | economics/markets | The 10-year US Treasury constant-maturity yield closes at or above 5.25 percent on at least one business day between 2026-09-21 and 2026-10-30. Reference: 5.00 percent on the packet date. | FRED series DGS10 (Treasury H.15) records a value of 5.25 or higher for any date between 2026-09-21 and 2026-10-30 inclusive. |
| KKR-20260919-19 | 40% | 2026-10-20 | political | The Federal Register publishes an executive order or OFAC notice terminating or removing Eritrea-related sanctions with a publication date between 2026-09-19 and 2026-10-16. | federalregister.gov shows a document whose title or abstract names Eritrea and terminates, revokes or removes sanctions authorities or designations, with publication_date between 2026-09-19 and 2026-10-16 inclusive. |
| KKR-20260919-20 | 29% | 2026-10-22 | disaster | Cuba suffers another full collapse of its national electrical grid between 2026-09-20 and 2026-10-20, publicly acknowledged by the Union Electrica or the Ministry of Energy and Mines. | Union Electrica or Cuba's Ministry of Energy and Mines acknowledges a total disconnection of the Sistema Electroenergetico Nacional occurring between 2026-09-20 and 2026-10-20 inclusive, corroborated by at least two of Reuters, AP, AFP and EFE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI front-month crude settles below 90.00 dollars per barrel on at least one NYMEX trading day between 2026-09-21 and 2026-10-09. Reference:" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Saudi Arabia officially confirms the interception or impact of at least one further missile or drone directed at Riyadh Province between 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a saudi press agency | or | saudi ministry of defense statement dated 202…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A US federal district court enters a temporary restraining order or preliminary injunction requiring the White House to restore press-pool o" → REJECTED: resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Nigeria at federal or Niger State level announces a formal judicial panel or commission of inquiry into the deaths of detainees at the Minna" → REJECTED: cited items name Nigeria; the claim is about Niger — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "USGS records an earthquake of magnitude 6.0 or greater within 300 km of the 2026-09-16 M6.5 event west of Nikolski, Alaska, occurring betwee" → REJECTED: the resolution names a different subject than the statement — the claim is about Alaska, Nikolski, USGS and the resolution settles on USGS, us7000ti1p. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2520 issued all-time across 16 forecaster arms · 2054 open (157 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 863 issued · 778 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 863 | 778 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
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
| manual/opus-5/unattested | 293 | 276 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 270 | 222 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*