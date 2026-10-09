**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092303Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-09_1516.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261009-26 | 62% | 2026-10-20 | disaster | Hurricane Isaias makes landfall on the US Gulf Coast between 2026-10-09 and 2026-10-16 with a National Hurricane Center landfall intensity of at least 111 mph maximum sustained winds (Category 3 or stronger). | True if the NHC advisory archive for Isaias (Tropical Cyclone Update or public advisory) gives maximum sustained winds of 111 mph or more at a US Gulf Coast landfall between 2026-10-09 and 2026-10-16; otherwise false. |
| KKR-20261009-27 | 70% | 2026-11-10 | cyber | CISA adds the SonicWall SMA1000 vulnerability CVE-2026-102255 to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-09 and 2026-11-06. | True if the CISA KEV catalog JSON lists CVE-2026-102255 with a dateAdded value between 2026-10-09 and 2026-11-06 inclusive; otherwise false. |
| KKR-20261009-28 | 40% | 2026-11-17 | cyber | CISA adds the Citrix NetScaler ADC and Gateway vulnerability CVE-2026-107406 to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-09 and 2026-11-13. | True if the CISA KEV catalog JSON lists CVE-2026-107406 with a dateAdded value between 2026-10-09 and 2026-11-13 inclusive; otherwise false. |
| KKR-20261009-29 | 30% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-10-12 and 2026-10-30. Reference: 104.81 on the packet date 2026-10-09. | True if any daily ICE Brent front-month settlement from 2026-10-12 through 2026-10-30 is 110.00 USD or higher; otherwise false. Reference level at seal: 104.81. |
| KKR-20261009-30 | 63% | 2027-01-08 | political | After the US Senate elections of 2026-11-03, the Democratic caucus (Democrats plus independents who caucus with them) holds at least 51 of 100 Senate seats when the 120th Congress convenes on 2027-01-03. | True if the Senate.gov party division record shows 51 or more senators in the Democratic caucus at the convening of the 120th Congress on 2027-01-03, following the 2026-11-03 elections; otherwise false. |
| KKR-20261009-31 | 35% | 2026-11-20 | political | Florida voters approve the constitutional amendment cutting homestead property taxes with at least 60 percent yes votes in the general election of 2026-11-03. | True if official Florida Division of Elections results for the 2026-11-03 general election show the homestead property tax amendment with a yes share of 60.00 percent or more; otherwise false. |
| KKR-20261009-32 | 7% | 2026-11-05 | military/conflict | The United States carries out an air, missile or drone strike on targets located on Iranian land territory, mainland or islands, between 2026-10-10 and 2026-11-02. | True if US Central Command or the Pentagon confirms, or at least two of Reuters, AP and AFP report, a US strike on Iranian land territory occurring between 2026-10-10 and 2026-11-02; otherwise false. |
| KKR-20261009-33 | 35% | 2026-11-12 | military/conflict | Ethiopian federal forces carry out an air or drone strike or a ground incursion inside the internationally recognized territory of Eritrea between 2026-10-10 and 2026-11-08. | True if at least two of Reuters, AP, AFP and BBC report an Ethiopian strike or ground incursion on Eritrean territory occurring between 2026-10-10 and 2026-11-08, citing either government, the UN or ACLED; otherwise false. |
| KKR-20261009-34 | 30% | 2027-01-05 | crime/security | The US Army carries out the execution of Fort Hood gunman Nidal Hasan between 2026-10-10 and 2026-12-31. | True if the Army or the Pentagon officially confirms, as carried by AP or Reuters, that Nidal Hasan was executed on a date between 2026-10-10 and 2026-12-31; otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Open Market Committee raises the federal funds target range in its policy statement of 2026-10-28, issued at the close of the me" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

3734 issued all-time across 21 forecaster arms · 2920 open (527 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 302 issued · 269 open · 25 resolved · 20 hits / 5 misses · **Brier 0.207** against its own base rate 80.0% (climatological 0.160) · **skill -0.296** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1320 | 1119 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 405 | 226 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 21 | 21 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 23 | 23 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 200 | 165 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 302 | 269 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 121 | 121 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 80 | 80 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*