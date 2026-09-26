**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 262109Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-26_1518.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260926-33 | 39% | 2026-10-07 | political | Luiz Inacio Lula da Silva receives more valid votes than Flavio Bolsonaro in the first round of the Brazilian presidential election held on 2026-10-04. | TRUE if the TSE official first-round totals for 2026-10-04 show Luiz Inacio Lula da Silva with more valid votes than Flavio Bolsonaro. |
| KKR-20260926-34 | 39% | 2026-10-27 | political | The Israeli Supreme Court overturns the Central Elections Committee disqualification of both the Raam (United Arab List) slate and the Joint List slate, in rulings issued between 2026-09-28 and 2026-10-23. | TRUE if Supreme Court of Israel docket rulings issued between 2026-09-28 and 2026-10-23 permit both the Raam slate and the Joint List slate to run in the 2026-10-27 Knesset election. |
| KKR-20260926-35 | 31% | 2026-10-28 | disaster | An earthquake of magnitude 6.0 or greater occurs within 150 km of the epicenter of the 2026-09-26 M6.6 event near Tadine, New Caledonia (USGS us6000txpi), between 2026-09-28 and 2026-10-25 UTC. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater within 150 km of the us6000txpi epicenter with origin time between 2026-09-28 and 2026-10-25 UTC. |
| KKR-20260926-36 | 29% | 2026-10-28 | crime/security | A single suicide attack in Pakistan kills at least 10 people, excluding the attackers, between 2026-09-28 and 2026-10-25. | TRUE if at least two of Reuters, AP, AFP and Dawn report one attack involving a suicide bomber in Pakistan between 2026-09-28 and 2026-10-25 that killed at least 10 people, excluding attackers. |
| KKR-20260926-37 | 48% | 2026-10-30 | economics/markets | The FOMC raises the federal funds target range by at least 25 basis points at its meeting ending 2026-10-28. Reference: 4.00 percent upper bound on the packet date. | TRUE if FRED series DFEDTARU reads 4.25 or higher for 2026-10-29, reflecting the 2026-10-28 FOMC decision. Reference: 4.00 percent upper bound on the packet date. |
| KKR-20260926-38 | 48% | 2026-11-03 | economics/markets | NYMEX WTI crude front-month futures settle at or above 100.00 dollars per barrel on at least one trading day between 2026-09-28 and 2026-10-30. Reference: 92.41 on the packet date (2026-09-25 settlement). | TRUE if the CME NYMEX WTI front-month daily settlement is 100.00 or higher on any trading day from 2026-09-28 through 2026-10-30. Reference: 92.41 settlement on the packet date. |
| KKR-20260926-39 | 39% | 2026-11-05 | political | The US and Iranian governments both announce, between 2026-09-28 and 2026-11-03, an agreement or memorandum under which Iran commits to reopening the Strait of Hormuz. | TRUE if the White House or State Department and the Iranian Foreign Ministry each publicly confirm, between 2026-09-28 and 2026-11-03, an agreement that includes Iran reopening the Strait of Hormuz, per Reuters, AP or AFP. |
| KKR-20260926-40 | 32% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry whose vendorProject or product names Kiteworks, with a dateAdded value between 2026-09-28 and 2026-11-13. | TRUE if the CISA KEV JSON feed contains an entry with vendorProject or product containing Kiteworks and dateAdded between 2026-09-28 and 2026-11-13 inclusive. |
| KKR-20260926-41 | 31% | 2026-12-01 | disaster | A laboratory-confirmed Bundibugyo virus disease case is confirmed in a country other than DR Congo, Uganda and France between 2026-09-28 and 2026-11-27, excluding patients medically evacuated after diagnosis in DR Congo. | TRUE if WHO Disease Outbreak News, WHO AFRO, or a national health ministry confirms a Bundibugyo case in a new country (not DR Congo, Uganda, France; medevacs excluded) dated 2026-09-28 to 2026-11-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US military forces strike at least one target on Iranian land territory, including Iranian islands, on any day between 2026-11-04 and 2026-1" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a us central command or pentagon statement, | or | at least two of reuters, ap   afp, report a u…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2917 issued all-time across 17 forecaster arms · 2375 open (209 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1032 issued · 915 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1032 | 915 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/sonnet-5/unattested | 320 | 256 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*