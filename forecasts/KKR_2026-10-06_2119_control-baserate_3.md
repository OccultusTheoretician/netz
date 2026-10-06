**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062119Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-66 | 69% | 2026-10-23 | military/conflict | At least one merchant vessel is struck by a projectile, drone, mine or explosive in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-08 and 2026-10-21. | YES if UKMTO reports a merchant vessel struck by a projectile, drone, mine or explosive in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-08 and 2026-10-21; NO otherwise. |
| KKR-20261006-67 | 69% | 2026-11-10 | military/conflict | A merchant vessel is struck by an aerial or naval drone or a missile inside the Bulgarian or Romanian Black Sea exclusive economic zone between 2026-10-08 and 2026-11-06. | YES if the Bulgarian or Romanian government, or Reuters or AP citing either, reports a drone or missile strike on a merchant vessel inside the Bulgarian or Romanian Black Sea EEZ between 2026-10-08 and 2026-11-06; NO otherwise. |
| KKR-20261006-68 | 58% | 2026-10-30 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28, lifting the upper bound above 4.00 percent. Reference: 3.75 to 4.00 percent target range at seal on 2026-10-06. | YES if the FOMC statement issued 2026-10-28 for the meeting of 2026-10-27 to 2026-10-28 sets an upper bound above 4.00 percent, per federalreserve.gov or FRED series DFEDTARU. Reference: 4.00 percent at seal. |
| KKR-20261006-69 | 58% | 2026-12-14 | economics/markets | The WTI Cushing spot crude price for 2026-12-01 is below 80.00 dollars per barrel. Reference: WTI 87.77 dollars per barrel in the packet market snapshot on 2026-10-06. | YES if FRED series DCOILWTICO shows a value below 80.00 for 2026-12-01; NO if 80.00 or higher. If no value posts for that date, use the nearest prior trading day. Reference: 87.77 on 2026-10-06. |
| KKR-20261006-70 | 42% | 2026-12-08 | cyber | CISA adds CVE-2026-61500, the Rejetto HFS session forgery flaw that enables unauthenticated remote code execution, to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-10-07 and 2026-12-04. | YES if the CISA KEV catalog JSON feed lists CVE-2026-61500 with a dateAdded value from 2026-10-07 through 2026-12-04 inclusive; NO otherwise. |
| KKR-20261006-71 | 33% | 2027-04-02 | crime/security | The US Army carries out the death sentence of Nidal Hasan, the convicted Fort Hood shooter, between 2026-10-07 and 2027-03-31. | YES if the Army or Pentagon confirms, or AP or Reuters reports, that Nidal Hasan was executed on a date between 2026-10-07 and 2027-03-31; NO otherwise. |
| KKR-20261006-72 | 33% | 2027-04-02 | crime/security | The German Federal Prosecutor General files an indictment against former BND president August Hanning between 2026-10-07 and 2027-03-31. | YES if a Federal Prosecutor General press release, or Reuters, AP or dpa, states that charges were filed against August Hanning at a German court between 2026-10-07 and 2027-03-31; NO otherwise. |
| KKR-20261006-73 | 43% | 2026-12-04 | disaster | The CDC cumulative count of confirmed 2026 US measles cases reaches at least 5,500 in a weekly update published between 2026-10-07 and 2026-12-02. Reference: about 3,880 cases at the start of October 2026. | YES if any CDC Measles Cases and Outbreaks weekly update published from 2026-10-07 through 2026-12-02 shows at least 5,500 confirmed 2026 US cases; NO otherwise. Reference: about 3,880 at start of October. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03, per AP race calls standing on 2" → REJECTED: cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Kenya confirms at least one additional laboratory-confirmed Ebola case, beyond the fatal imported case announced on 2026-10-06, between 2026" → REJECTED: resolution offers alternative VENUES joined by 'or' (…who disease outbreak news | or | situation…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3534 issued all-time across 21 forecaster arms · 2720 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1265 issued · 1064 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1265 | 1064 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*