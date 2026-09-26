**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 262109Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-26_1518.md · forecaster: manual/fable-5.1/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260926-04 | 20% | 2026-12-03 | military/conflict | Between 2026-09-27 and 2026-11-30 the United States and Iranian governments both publicly confirm a ceasefire, truce or Strait of Hormuz reopening agreement concluded between them. | Between 2026-09-27 and 2026-11-30 the White House and the Iranian Foreign Ministry each publicly confirm a US-Iran ceasefire, truce or Hormuz-reopening agreement, corroborated by two of Reuters, AP and AFP; a proposal or talks alone do not count. |
| KKR-20260926-05 | 45% | 2027-01-05 | military/conflict | Between 2026-11-04 and 2026-12-31 US Central Command confirms US strikes on at least one target inside Iran located more than 50 km inland from the Persian Gulf and Gulf of Oman coasts. | A CENTCOM or Department of War release names a US-struck target inside Iran more than 50 km from the Persian Gulf or Gulf of Oman coast, struck between 2026-11-04 and 2026-12-31; vessel and coastal-site strikes are excluded. |
| KKR-20260926-06 | 50% | 2027-01-05 | economics/markets | The 10-year Treasury constant-maturity yield (FRED series DGS10) closes at or above 5.50 percent on at least one trading day between 2026-09-28 and 2026-12-31. Reference: 5.18 percent on the packet date. | FRED series DGS10 shows at least one daily value of 5.50 or higher dated between 2026-09-28 and 2026-12-31 inclusive; reference level 5.18 percent held at packet seal; 5.49 or lower every day is false. |
| KKR-20260926-07 | 25% | 2027-01-08 | economics/markets | The Cushing WTI crude spot price (FRED series DCOILWTICO, EIA daily) settles at or below 75.00 dollars per barrel on at least one trading day between 2026-09-28 and 2026-12-31. Reference: 92.41 dollars on the packet date. | FRED series DCOILWTICO shows at least one daily value of 75.00 or lower dated between 2026-09-28 and 2026-12-31 inclusive; reference level 92.41 dollars per barrel held at packet seal. |
| KKR-20260926-08 | 35% | 2026-11-04 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendorProject or product field names Kiteworks or Accellion, with a dateAdded value between 2026-09-26 and 2026-10-31. | The CISA KEV JSON feed (known_exploited_vulnerabilities.json) contains an entry whose vendorProject or product field includes Kiteworks or Accellion and whose dateAdded is between 2026-09-26 and 2026-10-31 inclusive. |
| KKR-20260926-09 | 15% | 2026-11-04 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose product field names Elementor (the WordPress plugin), with a dateAdded value between 2026-09-26 and 2026-10-31. | The CISA KEV JSON feed contains an entry whose vendorProject or product field includes Elementor and whose dateAdded is between 2026-09-26 and 2026-10-31 inclusive; entries for WordPress core or other plugins do not count. |
| KKR-20260926-10 | 90% | 2026-10-08 | political | In the Brazilian presidential election first round held on 2026-10-04 no candidate wins more than 50 percent of valid votes, so a second round on 2026-10-25 is required. | Official TSE results (tse.jus.br) for the 2026-10-04 presidential first round show no candidate above 50 percent of valid votes and the TSE proceeds to a 2026-10-25 second round between the top two candidates. |
| KKR-20260926-11 | 85% | 2026-10-22 | political | Between 2026-09-27 and 2026-10-19 the Israeli Supreme Court reverses the Central Elections Committee disqualifications of both the Joint List (Hadash, Taal, Balad) and the United Arab List (Raam), clearing both to run in the 2026-10-27 Knesset election. | Supreme Court rulings dated between 2026-09-27 and 2026-10-19 overturn the CEC disqualification of both the Joint List and the United Arab List, and both appear on the official candidate lists for 2026-10-27; either still barred is false. |
| KKR-20260926-12 | 35% | 2026-11-17 | disaster | A FEMA major disaster declaration (declarationType DR) for the State of Hawaii tied to Hurricane Nolo is issued with a declarationDate between 2026-09-26 and 2026-11-13. | The OpenFEMA DisasterDeclarationsSummaries dataset contains a record with state HI, declarationType DR, declarationDate between 2026-09-26 and 2026-11-13 inclusive, and a declarationTitle or incident description naming Nolo; an EM-type declaration alone is false. |
| KKR-20260926-13 | 40% | 2027-01-06 | disaster | Between 2026-09-27 and 2026-12-31 the WHO confirms at least one laboratory-confirmed Bundibugyo Ebola case linked to the 2026 DR Congo outbreak diagnosed in a country other than the Democratic Republic of the Congo, Uganda or France. | A WHO Disease Outbreak News item or WHO AFRO situation report published between 2026-09-27 and 2026-12-31 reports a laboratory-confirmed outbreak-linked Ebola case in a country other than DRC, Uganda or France; suspected or probable cases do not count. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2889 issued all-time across 17 forecaster arms · 2347 open (209 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 200 issued · 183 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1013 | 896 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 320 | 256 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*