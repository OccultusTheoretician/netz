**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112239Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-65 | 26% | 2026-09-18 | economics/markets | The FOMC raises the federal funds target range by 25 basis points to 3.75-4.00 percent at its meeting concluding 2026-09-16. Reference: 3.50-3.75 percent on the packet date. | True if the FOMC statement dated 2026-09-16 on federalreserve.gov sets the federal funds target range at 3.75 to 4.00 percent. Any other range, including a larger hike or a hold, is false. |
| KKR-20260911-66 | 56% | 2026-11-03 | military/conflict | The United States and Iran each publicly accept a mutual ceasefire or cessation of hostilities announced between 2026-09-12 and 2026-10-31. | True if, between 2026-09-12 and 2026-10-31, both the US government and the Iranian government publicly confirm a mutual ceasefire, as reported by at least two of Reuters, AP, and AFP. |
| KKR-20260911-67 | 28% | 2026-11-17 | cyber | CISA adds GitLab CVE-2026-85706 to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-11 and 2026-11-13. Not listed in KEV catalog version 2026.09.10 at seal. | True if the CISA KEV catalog JSON lists CVE-2026-85706 with a dateAdded value from 2026-09-11 through 2026-11-13; false otherwise. |
| KKR-20260911-68 | 28% | 2026-12-14 | cyber | CISA sets knownRansomwareCampaignUse to Known for PaperCut CVE-2026-82078 or CVE-2026-81578 between 2026-09-11 and 2026-12-11. Reference: both Unknown in KEV catalog version 2026.09.10 at seal. | True if the latest CISA KEV catalog version released between 2026-09-11 and 2026-12-11 shows knownRansomwareCampaignUse Known for CVE-2026-82078 or CVE-2026-81578; false if both remain Unknown. |
| KKR-20260911-69 | 35% | 2026-10-12 | political | Zack Polanski of the Green Party wins the Holborn and St Pancras parliamentary by-election polled on 2026-10-08. | True if the returning officer declaration for the Holborn and St Pancras by-election polled on 2026-10-08 names Zack Polanski as elected; false if another candidate is declared or no result is declared by 2026-10-10. |
| KKR-20260911-70 | 35% | 2026-11-25 | political | Democratic candidates win at least 218 of 435 US House seats in the 2026-11-03 general election. | True if Associated Press race calls made by 2026-11-23 credit Democrats with 218 or more House seats from the 2026-11-03 election; false otherwise. |
| KKR-20260911-71 | 31% | 2026-11-17 | disaster | A laboratory-confirmed Bundibugyo virus disease case is diagnosed in a country other than the DRC between 2026-09-12 and 2026-11-13, excluding planned medical evacuations. | True if a WHO Disease Outbreak News item or a national health ministry reports a laboratory-confirmed Bundibugyo case diagnosed outside the DRC, not a planned medical evacuation, between 2026-09-12 and 2026-11-13. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The 10-year Treasury constant-maturity yield for the observation date 2026-10-30 is at or above 5.00 percent. Reference: 4.94 percent on the" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-30 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The EIA weekly U.S. No. 2 on-highway diesel retail price for the week of 2026-10-26 is at or above 6.000 dollars per gallon. Reference: 5.96" → REJECTED: event window opens 2026-09-07, before this row is sealed (2026-09-11, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "A merchant vessel is struck by a missile, drone, projectile, or explosive boat in the Red Sea, Bab al-Mandab, or Gulf of Aden between 2026-0" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about Aden, Bab, Gulf, Mandab and the resolution settles on JMIC, UKMTO. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1951 issued all-time across 16 forecaster arms · 1615 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 625 issued · 587 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 625 | 587 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 211 | 208 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 226 | 220 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 212 | 180 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*