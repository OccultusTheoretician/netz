**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 082338Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-08_1517.md · forecaster: manual/fable-5.1/unattested · 10 accepted / 0 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261008-32 | 90% | 2026-10-15 | political | The Labour Party candidate wins the Holborn and St Pancras parliamentary by-election held on 2026-10-08. | The official declared result for the Holborn and St Pancras by-election of 2026-10-08, published by Camden Council or the UK Parliament website, names the Labour Party candidate as elected. |
| KKR-20261008-33 | 50% | 2026-10-19 | disaster | Hurricane Isaias makes its first US Gulf Coast landfall between 2026-10-08 and 2026-10-15 with maximum sustained winds of at least 96 mph, Category 2 or stronger. | A National Hurricane Center advisory or tropical cyclone update issued between 2026-10-08 and 2026-10-15 UTC reports Isaias maximum sustained winds of at least 96 mph at its first US Gulf Coast landfall. |
| KKR-20261008-34 | 17% | 2026-10-30 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding 2026-10-28. Reference: target range upper bound 4.00 percent on the packet date. | FRED series DFEDTARU shows a value above 4.00 for 2026-10-29, reflecting a target range increase announced in the FOMC statement of 2026-10-28. |
| KKR-20261008-35 | 38% | 2026-11-02 | economics/markets | The ICE Brent December 2026 crude futures contract settles at or above 110.00 USD per barrel on at least one trading day between 2026-10-09 and 2026-10-29. Reference: 105.68 on the packet date. | ICE end-of-day settlement data show the Brent December 2026 futures contract settling at or above 110.00 USD on at least one trading day between 2026-10-09 and 2026-10-29. |
| KKR-20261008-36 | 20% | 2026-11-05 | military/conflict | The United States carries out at least one military strike on a target on Iranian land territory, islands included and vessels at sea excluded, between 2026-10-09 and 2026-11-02 UTC. | US Central Command, the Pentagon or the White House publicly confirms a US strike on a target on Iranian land territory, islands included, conducted between 2026-10-09 and 2026-11-02 UTC, as carried by Reuters or AP. |
| KKR-20261008-37 | 30% | 2026-11-10 | economics/markets | The 10-year US Treasury constant maturity yield is at or above 5.50 percent on at least one business day between 2026-10-09 and 2026-11-06. Reference: 5.30 percent on the packet date. | FRED series DGS10 shows a value of 5.50 or higher for at least one date between 2026-10-09 and 2026-11-06. |
| KKR-20261008-38 | 45% | 2026-11-12 | military/conflict | At least one further single Russian attack on one locality in Ukraine kills 20 or more people between 2026-10-09 and 2026-11-08. | At least two of Reuters, AP and BBC report a death toll of 20 or more from a single Russian attack on one locality in Ukraine that occurred between 2026-10-09 and 2026-11-08. |
| KKR-20261008-39 | 30% | 2026-11-23 | cyber | CISA adds CVE-2026-102255, the SonicWall SMA1000 pre-authentication SSRF flaw, to its Known Exploited Vulnerabilities catalog between 2026-10-09 and 2026-11-20. | The CISA KEV catalog lists CVE-2026-102255 with a dateAdded value between 2026-10-09 and 2026-11-20. |
| KKR-20261008-40 | 82% | 2026-12-04 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | By 2026-12-04 the Associated Press has called at least 218 US House races from the 2026-11-03 general election for Democratic candidates. |
| KKR-20261008-41 | 45% | 2027-04-02 | crime/security | Jonathan Spalletta, convicted in the Uranium Finance hack case, is sentenced to at least 60 months in prison between 2026-10-09 and 2027-03-31. | The SDNY docket in United States v. Spalletta records a sentence imposed between 2026-10-09 and 2027-03-31 that includes a prison term of at least 60 months. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

3653 issued all-time across 21 forecaster arms · 2839 open (485 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 293 issued · 260 open · 25 resolved · 20 hits / 5 misses · **Brier 0.207** against its own base rate 80.0% (climatological 0.160) · **skill -0.296** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1292 | 1091 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 400 | 221 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 17 | 17 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 26 | 26 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 197 | 162 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 293 | 260 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 112 | 112 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*