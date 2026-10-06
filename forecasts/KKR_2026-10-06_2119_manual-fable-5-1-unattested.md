**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062119Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-28 | 35% | 2026-11-17 | cyber | CISA adds CVE-2026-61500, the Rejetto HFS session-cookie signing flaw now being scanned for, to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-07 and 2026-11-13. | The CISA KEV catalog lists CVE-2026-61500 with a dateAdded value between 2026-10-07 and 2026-11-13 inclusive. |
| KKR-20261006-29 | 30% | 2026-11-17 | cyber | CISA adds CVE-2026-21589, the critical unauthenticated file-read flaw in Atlassian Data Center products, to its Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-07 and 2026-11-13. | The CISA KEV catalog lists CVE-2026-21589 with a dateAdded value between 2026-10-07 and 2026-11-13 inclusive. |
| KKR-20261006-30 | 83% | 2026-10-30 | economics/markets | The FOMC statement released on 2026-10-28 leaves the federal funds target range unchanged at 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date. | The Federal Reserve statement of 2026-10-28, or FRED series DFEDTARU for 2026-10-29, shows the target range upper limit at 4.00 percent. Reference: 4.00 percent on the packet date. |
| KKR-20261006-31 | 55% | 2027-01-05 | political | The Landtag of Saxony-Anhalt elects AfD lead candidate Ulrich Siegmund as Minister-President in a ballot held between 2026-10-07 and 2026-12-31. | The official record of the Landtag of Saxony-Anhalt shows Ulrich Siegmund elected Minister-President in a ballot held between 2026-10-07 and 2026-12-31. |
| KKR-20261006-32 | 7% | 2027-03-31 | crime/security | The US Army carries out the execution of Fort Hood shooter Nidal Hasan between 2026-10-07 and 2027-03-26. | The US Army or the Pentagon confirms that Nidal Hasan was executed on a date between 2026-10-07 and 2027-03-26, as reported by the Associated Press or Reuters. |
| KKR-20261006-33 | 33% | 2026-11-17 | military/conflict | US forces conduct air or missile strikes on targets on Iranian soil between 2026-10-08 and 2026-11-13. | US Central Command or the Pentagon confirms US air or missile strikes on targets on Iranian soil conducted between 2026-10-08 and 2026-11-13, as reported by Reuters or the Associated Press. |
| KKR-20261006-34 | 28% | 2026-11-04 | military/conflict | At least one more commercial vessel is struck by an aerial or naval drone inside the exclusive economic zone or territorial sea of Bulgaria or Romania between 2026-10-08 and 2026-10-31. | Bulgarian or Romanian authorities state that a commercial vessel was struck by a drone inside the exclusive economic zone or territorial sea of either country between 2026-10-08 and 2026-10-31, as reported by Reuters or AP. |
| KKR-20261006-35 | 20% | 2026-11-10 | disaster | Kenya records at least one additional laboratory-confirmed case of Ebola disease (Bundibugyo virus), beyond the imported case announced on 2026-10-06, with confirmation announced between 2026-10-07 and 2026-11-06. | The Kenya Ministry of Health or a WHO Disease Outbreak News report states that a second laboratory-confirmed Ebola (Bundibugyo virus) case in Kenya was confirmed between 2026-10-07 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "NYMEX front-month WTI crude futures settle below 80.00 dollars per barrel on 2026-11-06. Reference: 87.77 on the packet date." → REJECTED: resolution offers alternative VENUES joined by 'or' (…the cme settlement price, | or | eia series rclc1, for front-month wti crude o…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03." → REJECTED: cited items name Russian Federation; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3496 issued all-time across 21 forecaster arms · 2682 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 274 issued · 241 open · 25 resolved · 20 hits / 5 misses · **Brier 0.207** against its own base rate 80.0% (climatological 0.160) · **skill -0.296** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1242 | 1041 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
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
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*