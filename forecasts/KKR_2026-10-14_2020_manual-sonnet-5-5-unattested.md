**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 142020Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: manual/sonnet-5.5/unattested · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-39 | 12% | 2026-11-18 | military/conflict | Saudi Arabia and the Houthis, directly or via Oman or the UN envoy, announce a ceasefire, truce or de-escalation agreement covering cross-border attacks between 2026-10-15 and 2026-11-13. | Reuters and AP both report an announced ceasefire, truce or de-escalation agreement between Saudi Arabia and the Houthis, with the announcement dated between 2026-10-15 and 2026-11-13; unilateral pledges do not count. |
| KKR-20261014-40 | 25% | 2026-11-09 | military/conflict | SpaceX or the Ukrainian government publicly states that the restriction on Ukrainian military Starlink access reported on 2026-10-14 has been lifted or reversed, with the statement dated between 2026-10-15 and 2026-11-04. | Two major outlets report a SpaceX or Ukrainian government statement, dated between 2026-10-15 and 2026-11-04, that the Starlink restriction on Ukrainian military access reported on 2026-10-14 was lifted or reversed. |
| KKR-20261014-41 | 25% | 2026-11-17 | economics/markets | The US 10-year Treasury constant maturity yield is at or above 5.50 percent on at least one business day between 2026-10-15 and 2026-11-13. Reference: 5.26 percent on the packet date 2026-10-14. | FRED series DGS10 shows a daily value of 5.50 or higher for at least one date between 2026-10-15 and 2026-11-13 inclusive. Reference: 5.26 percent on 2026-10-14. |
| KKR-20261014-42 | 27% | 2026-11-17 | economics/markets | The ICE front-month Brent futures daily settlement price is at or above 115.00 USD per barrel on at least one trading day between 2026-10-15 and 2026-11-13. Reference: 105.75 USD on the packet date 2026-10-14. | ICE Futures Europe front-month Brent settlement at or above 115.00 USD per barrel on at least one trading day between 2026-10-15 and 2026-11-13, per ICE data or Reuters. Reference: 105.75 on 2026-10-14. |
| KKR-20261014-43 | 82% | 2026-11-16 | cyber | CISA adds at least one Microsoft vulnerability to the KEV catalog with a date-added value between 2026-11-10 and 2026-11-12, around the scheduled November 2026 Patch Tuesday on 2026-11-10. | The CISA KEV catalog carries at least one entry with vendorProject Microsoft and a dateAdded value between 2026-11-10 and 2026-11-12 inclusive. |
| KKR-20261014-44 | 80% | 2026-11-24 | political | Democratic candidates win or lead in at least 218 of 435 US House districts in the general election held on 2026-11-03, per Associated Press results compiled between 2026-11-03 and 2026-11-20. | Associated Press House results as of 2026-11-20, covering vote counting between 2026-11-03 and 2026-11-20, show Democratic candidates having won or leading in at least 218 of 435 districts. |
| KKR-20261014-45 | 10% | 2026-12-22 | political | The White House transmits to the US Senate a nomination of a successor US Ambassador to Greece between 2026-10-15 and 2026-12-18. | Congress.gov nominations records show a PN entry for Ambassador Extraordinary and Plenipotentiary to the Hellenic Republic with a date received in the Senate between 2026-10-15 and 2026-12-18 inclusive. |
| KKR-20261014-46 | 55% | 2026-11-18 | crime/security | A federal indictment or prosecutor information charging the Saudi national arrested on 2026-10-13 over a recording device planted at OpenAI offices is filed between 2026-10-15 and 2026-11-13. | The federal court docket in the OpenAI recording-device case, via CourtListener or PACER, shows an indictment or information filed between 2026-10-15 and 2026-11-13 inclusive; a criminal complaint alone does not count. |
| KKR-20261014-47 | 42% | 2026-11-17 | disaster | USGS lists at least one earthquake of magnitude 6.0 or greater within 300 km of the epicenter of the M7.7 Panama earthquake (event us6000u18k), with origin time between 2026-10-15 and 2026-11-13 UTC. | A USGS ComCat search returns an event other than us6000u18k, magnitude 6.0 or greater, within 300 km of its epicenter, with origin time between 2026-10-15T00:00Z and 2026-11-13T23:59Z. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds at least one Ivanti vulnerability other than CVE-2026-104935 to the KEV catalog with a date-added value between 2026-10-15 and 202" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-15..2026-11-13; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

4142 issued all-time across 21 forecaster arms · 3031 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 131 issued · 131 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1460 | 1164 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 52 | 52 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 345 | 287 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*