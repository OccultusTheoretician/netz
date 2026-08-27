**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271658Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-27_1517.md · forecaster: manual/fable-5/unattested · 9 accepted / 1 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-67 | 40% | 2026-09-18 | economics/markets | The FOMC raises the target range for the federal funds rate above 3.50-3.75 percent at its scheduled 2026-09-16 meeting. | The FOMC statement dated 2026-09-16 on federalreserve.gov announces an increase in the target range; equivalently FRED series DFEDTARU shows a value above 3.75 on 2026-09-17. |
| KKR-20260827-68 | 55% | 2026-10-02 | economics/markets | Nvidia or Hugging Face officially confirms a definitive agreement for Nvidia to acquire Hugging Face between 2026-08-27 and 2026-09-30. | A press release, SEC filing by NVIDIA Corp, or official company blog post dated between 2026-08-27 and 2026-09-30 states that Nvidia has entered a definitive agreement to acquire Hugging Face. |
| KKR-20260827-69 | 85% | 2026-10-06 | cyber | At least one civil complaint naming Carhartt Inc as defendant over the 2026 customer data breach is filed in a US federal district court between 2026-08-27 and 2026-10-02. | PACER or CourtListener shows a complaint filed between 2026-08-27 and 2026-10-02 in any US federal district court that names Carhartt Inc as defendant and alleges harm from the 2026 data breach of about 12.9 million accounts. |
| KKR-20260827-70 | 25% | 2026-11-03 | cyber | CISA adds a vulnerability in the Avada WordPress theme to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-08-28 and 2026-10-30. | The CISA KEV catalog JSON contains an entry whose vendorProject, product, or vulnerabilityName field includes Avada, with dateAdded between 2026-08-28 and 2026-10-30 inclusive. |
| KKR-20260827-71 | 40% | 2026-10-02 | disaster | Official confirmed deaths from the 2026-08-26 Bhotekoshi-Trishuli flash flood, Nepal and Tibet combined, reach at least 1,000 by 2026-09-30. | Reuters, AP, or AFP reports that official confirmed deaths from the 2026-08-26 flood, Nepal police or NDRRMA figures plus Chinese official figures for Gyirong county, total at least 1,000 as of a date no later than 2026-09-30. |
| KKR-20260827-72 | 70% | 2026-09-14 | political | The Norwegian Royal House announces the death of King Harald V occurring between 2026-08-27 and 2026-09-10. | An official statement from the Royal House of Norway (kongehuset.no) or NTB reports the death of King Harald V on a date between 2026-08-27 and 2026-09-10 inclusive. |
| KKR-20260827-73 | 20% | 2026-11-03 | military/conflict | The United States and Iran both publicly confirm signing a final agreement ending the war that began on 2026-02-28, with the signing occurring between 2026-08-28 and 2026-10-30. | The White House or State Department and the Iranian Foreign Ministry or IRNA each confirm a signed final agreement ending the war, distinct from a ceasefire, memorandum, or framework, signed between 2026-08-28 and 2026-10-30. |
| KKR-20260827-74 | 55% | 2026-10-02 | military/conflict | UKMTO publishes at least three separate incident reports of merchant vessels struck by a projectile, mine, or other weapon in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-08-28 and 2026-09-30. | The UKMTO incidents page (ukmto.org) lists at least three distinct incident references dated 2026-08-28 to 2026-09-30, each stating a vessel was struck, hit, or impacted in the Strait of Hormuz, Gulf of Oman, or Persian Gulf. |
| KKR-20260827-75 | 45% | 2026-11-03 | crime/security | Spanish authorities (Guardia Civil or Policia Nacional) announce at least one arrest in the 2026-08-27 Villena Treasure theft between 2026-08-27 and 2026-10-30. | An official Guardia Civil or Policia Nacional communication, or Reuters, AP, AFP, or EFE citing such officials, reports at least one person arrested (detenido) for the Villena Museum theft, with the arrest dated between 2026-08-27 and 2026-10-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The AfD receives at least 40.0 percent of Zweitstimmen in the Saxony-Anhalt Landtag election held on 2026-09-06." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

998 issued all-time across 14 forecaster arms · 837 open (4 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 101 issued · 100 open · 1 resolved · 1 hits / 0 misses · **Brier 0.090** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 222 | 205 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 160 | 129 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 101 | 100 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 114 | 111 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 102 | 94 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*