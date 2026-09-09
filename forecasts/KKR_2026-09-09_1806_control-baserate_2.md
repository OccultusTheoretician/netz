**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091806Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-09_1530.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260909-28 | 28% | 2026-09-25 | cyber | CISA adds the Chrome V8 zero-day CVE-2026-87491, disclosed by Google on 2026-09-08 as exploited in the wild, to its Known Exploited Vulnerabilities catalog between 2026-09-09 and 2026-09-23. | The CISA KEV catalog JSON feed contains an entry for CVE-2026-87491 with a dateAdded value between 2026-09-09 and 2026-09-23 inclusive. |
| KKR-20260909-29 | 28% | 2026-10-20 | cyber | Following the public ShieldCrash proof-of-concept, CISA adds at least one Microsoft Defender or Malware Protection Engine vulnerability to the Known Exploited Vulnerabilities catalog with a date-added between 2026-09-09 and 2026-10-16. | The CISA KEV catalog JSON feed contains an entry with vendorProject Microsoft whose product or vulnerabilityName names Defender or Malware Protection Engine, with dateAdded between 2026-09-09 and 2026-10-16 inclusive. |
| KKR-20260909-30 | 26% | 2026-09-21 | economics/markets | The FOMC raises the federal funds target range at its scheduled 2026-09-16 meeting. Reference: target range 3.50 to 3.75 percent at seal. | The FOMC statement dated 2026-09-16 on federalreserve.gov announces a target range whose upper bound is 4.00 percent or higher; equivalently, FRED series DFEDTARU reads at or above 4.00 for 2026-09-17. |
| KKR-20260909-31 | 26% | 2026-10-21 | economics/markets | Brent crude spot reaches 110.00 dollars per barrel or higher on at least one trading day between 2026-09-10 and 2026-10-09. Reference: Brent 101.13 on the packet date. | FRED series DCOILBRENTEU (EIA Europe Brent spot price FOB) records a daily value at or above 110.00 for at least one date between 2026-09-10 and 2026-10-09 inclusive. |
| KKR-20260909-32 | 56% | 2026-10-13 | military/conflict | Between 2026-09-10 and 2026-10-09, the US Department of Defense or US Central Command publicly confirms that a US Navy or US Coast Guard vessel was struck by an Iranian missile, drone, mine, or gunfire. | An official DoD or CENTCOM release, statement, or on-record briefing confirms an Iranian weapon struck a US Navy or Coast Guard vessel, the strike occurring between 2026-09-10 and 2026-10-09. Interceptions and near misses do not count. |
| KKR-20260909-33 | 35% | 2026-10-06 | political | Between 2026-09-10 and 2026-10-02, German Chancellor Friedrich Merz and US President Donald Trump hold a phone call or in-person bilateral meeting, as confirmed by an official German or US government readout. | The German federal government (bundesregierung.de or the government spokesperson) or the White House publishes a readout or statement confirming a Merz-Trump call or bilateral meeting held between 2026-09-10 and 2026-10-02. |
| KKR-20260909-34 | 35% | 2026-11-24 | political | Chris Pappas wins the 2026-11-03 US Senate general election in New Hampshire, defeating John Sununu. | Official results published by the New Hampshire Secretary of State (sos.nh.gov) for the 2026-11-03 US Senate general election show Pappas receiving more votes than any other candidate. |
| KKR-20260909-35 | 10% | 2027-01-05 | crime/security | Between 2026-09-10 and 2026-12-31, the Metropolitan Police arrest at least one person in connection with their inquiry into alleged overseas donations to Reform UK. | A Metropolitan Police statement, or reports from at least two of BBC, Guardian, Reuters, PA, confirm an arrest made between 2026-09-10 and 2026-12-31 in connection with the Reform UK donations inquiry. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-10 and 2026-10-30, the United States and Iran announce a ceasefire or cessation of hostilities, confirmed by both the US exe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…iranian foreign ministry | or | supreme national security council…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A federal Major Disaster Declaration for the State of Hawaii covering Hurricane Lowell is issued between 2026-09-09 and 2026-10-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…penfema disasterdeclarationssummaries dataset | or | fema…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1778 issued all-time across 16 forecaster arms · 1442 open (47 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 552 issued · 514 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 552 | 514 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 240 | 111 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 188 | 185 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 206 | 200 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*