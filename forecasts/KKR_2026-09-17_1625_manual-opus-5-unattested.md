**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171625Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-17_1518.md · forecaster: manual/opus-5/unattested · 10 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260917-35 | 45% | 2026-10-30 | economics/markets | The FOMC raises the federal funds target range above 3.75 to 4.00 percent at its scheduled meeting concluding 2026-10-28. Reference: upper limit 4.00 percent at seal on 2026-09-17. | The Federal Reserve FOMC statement dated 2026-10-28 announces an increase to the federal funds target range; FRED DFEDTARU for 2026-10-29 exceeds 4.00. Reference: upper limit 4.00 percent at seal. |
| KKR-20260917-36 | 55% | 2026-11-09 | economics/markets | The Bank of England MPC raises Bank Rate above 3.75 percent at its scheduled announcement on 2026-11-05. Reference: Bank Rate 3.75 percent at seal on 2026-09-17. | The Bank of England Monetary Policy Summary dated 2026-11-05 announces Bank Rate above 3.75 percent, and Bank of England database series IUDBEDR for 2026-11-06 exceeds 3.75. Reference: 3.75 percent at seal. |
| KKR-20260917-37 | 47% | 2026-12-01 | economics/markets | The EIA Cushing WTI spot price falls below 90.00 dollars per barrel on at least one trading day between 2026-09-18 and 2026-11-20. Reference: WTI 101.09 in the packet market snapshot on 2026-09-17. | FRED series DCOILWTICO shows at least one daily value below 90.00 dated between 2026-09-18 and 2026-11-20 inclusive. Reference: WTI 101.09 per packet snapshot at seal. |
| KKR-20260917-38 | 40% | 2026-11-03 | political | The Riksdag elects Magdalena Andersson prime minister of Sweden in a vote held between 2026-09-18 and 2026-10-30. | Riksdagen.se records a prime-ministerial vote held between 2026-09-18 and 2026-10-30 in which the Speaker proposal of Magdalena Andersson is not rejected, meaning fewer than 175 members vote no. |
| KKR-20260917-39 | 45% | 2026-12-14 | political | Democrat James Talarico receives more votes than Republican Ken Paxton in the Texas US Senate general election held on 2026-11-03. | The Texas Secretary of State official canvass of the 2026-11-03 general election shows Talarico with more US Senate votes than Paxton. |
| KKR-20260917-40 | 85% | 2026-10-23 | political | The Russia sanctions and secondary-tariff bill named for the late Senator Lindsey Graham, which cleared the House 262-159 on 2026-09-16, becomes public law between 2026-09-17 and 2026-10-16. | Congress.gov shows the bill passed by the House 262-159 on 2026-09-16 with a Signed by President or Became Public Law action dated between 2026-09-17 and 2026-10-16. |
| KKR-20260917-41 | 25% | 2026-12-22 | crime/security | A federal criminal charge of contempt of Congress under 2 U.S.C. 192 is filed against Leon Black in the US District Court for the District of Columbia between 2026-09-17 and 2026-12-18. | The D.D.C. docket via PACER or CourtListener shows a criminal case against Leon Black charging 2 U.S.C. 192, with a filing date between 2026-09-17 and 2026-12-18. |
| KKR-20260917-42 | 35% | 2026-12-02 | cyber | CISA adds CVE-2026-89026, the Issabel Framework hard-coded JWT signing key flaw, to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-17 and 2026-11-30. | The CISA KEV catalog JSON lists CVE-2026-89026 with a dateAdded value between 2026-09-17 and 2026-11-30 inclusive. |
| KKR-20260917-43 | 20% | 2026-11-24 | military/conflict | The United States and Iran conclude a ceasefire or cessation-of-hostilities agreement between 2026-09-18 and 2026-11-20 that both governments publicly confirm. | Reuters or AP reports that the US government and the Iranian government each confirmed a US-Iran ceasefire or cessation-of-hostilities agreement concluded between 2026-09-18 and 2026-11-20. |
| KKR-20260917-44 | 14% | 2026-12-02 | disaster | An earthquake of magnitude 6.0 or greater occurs within 250 km of the epicenter of the 2026-09-17 M6.5 event 165 km W of Nikolski, Alaska (USGS us7000ti1p) between 2026-09-18 and 2026-11-30 UTC. | The USGS ComCat catalog lists at least one event of magnitude 6.0 or greater within 250 km of the us7000ti1p epicenter with an origin time between 2026-09-18 and 2026-11-30 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2409 issued all-time across 16 forecaster arms · 1943 open (82 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 283 issued · 266 open · 7 resolved · 5 hits / 2 misses · **Brier 0.137** against its own base rate 71.4% (climatological 0.204) · **skill +0.329** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 815 | 730 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
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
| manual/opus-5/unattested | 283 | 266 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 252 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*