**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271658Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-27_1517.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-99 | 53% | 2026-10-13 | military_conflict | The United States and Iran, directly or through the mediating states of Qatar, Oman, or Pakistan named in current shuttle diplomacy, announce a ceasefire, truce, or negotiated framework ending active hostilities in the ongoing Iran war, with that announcement first reported between 2026-09-10 and 2026-10-10. | At least two independently owned wire services, or the US State Department and the Iranian foreign ministry both, confirm a ceasefire, truce, or framework agreement ending active US-Iran hostilities was announced within the stated window, checked by 2026-10-13. |
| KKR-20260827-100 | 53% | 2026-10-06 | military_conflict | Russian military forces conduct a strike, using missile, drone, or other kinetic means, that lands on the sovereign territory of a NATO member state, including the UK, between 2026-09-03 and 2026-10-03. | At least two independently owned news organizations, or a NATO member government and NATO itself, confirm a Russian-origin strike landed on NATO member territory within the window, checked by 2026-10-06. |
| KKR-20260827-101 | 33% | 2026-10-19 | cyber | The CISA Known Exploited Vulnerabilities catalog entry for CVE-2026-8452, the Citrix NetScaler ADC and Gateway flaw added 2026-08-26, has its knownRansomwareCampaignUse field changed to Yes between 2026-09-03 and 2026-10-15. | The public CISA KEV catalog feed at cisa.gov shows knownRansomwareCampaignUse equal to Yes for CVE-2026-8452, with the change falling inside the window, checked by 2026-10-19. |
| KKR-20260827-102 | 33% | 2026-10-21 | cyber | Boston Scientific files a Form 8-K Item 1.05 material cybersecurity incident disclosure with the SEC regarding the cyberattack disclosed 2026-08-26, between 2026-09-03 and 2026-10-17. | SEC EDGAR shows a Boston Scientific Form 8-K containing Item 1.05 filed within the window, checked by 2026-10-21. |
| KKR-20260827-103 | 25% | 2026-09-16 | economics_markets | The Federal Open Market Committee raises the target federal funds rate range at the conclusion of its September 15-16, 2026 meeting. | The Federal Reserve post-meeting statement released 2026-09-16 shows a target federal funds rate range higher than the range in effect entering the meeting. |
| KKR-20260827-104 | 43% | 2027-02-04 | crime_security | The military commission trial date for Khalid Sheikh Mohammed and co-defendants, currently set for June, is reported as vacated, postponed, or otherwise materially altered by a commission ruling, DOD announcement, or appellate court order, between 2026-09-03 and 2027-01-31. | A DOD, Office of Military Commissions, or major wire service report confirms the June trial date no longer stands as scheduled, with that report dated within the window, checked by 2027-02-04. |
| KKR-20260827-105 | 52% | 2026-10-03 | disaster | The confirmed death toll from the August 2026 Nepal-Tibet flash flood and glacial lake outburst event reaches at least 800, as reported by the government of Nepal, Chinese authorities, or UN OCHA, between 2026-09-03 and 2026-09-30. | A government of Nepal, Chinese government, or UN OCHA situation report states a confirmed fatality count of 800 or more tied to this event, dated within the window, checked by 2026-10-03. |
| KKR-20260827-106 | 43% | 2026-11-04 | crime_security | At least one individual arrested in the TeamPCP supply-chain hacking case is formally charged by an Australian prosecutorial authority or a foreign partner agency, between 2026-09-03 and 2026-10-31. | An AFP, CDPP, DOJ, or equivalent prosecutorial press release, or a court filing, confirms formal charges were laid against at least one TeamPCP suspect within the window, checked by 2026-11-04. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The reported 12.9 billion dollar Nvidia acquisition of Hugging Face is confirmed closed, meaning the transaction has legally completed, betw" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The Alternative for Germany wins an outright majority of at least 42 of the 83 seats in the Landtag of Saxony-Anhalt in the state election h" → REJECTED: resolution offers alternative VENUES joined by 'or' (…saxony-anhalt state returning officer | or | a major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1029 issued all-time across 14 forecaster arms · 868 open (4 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 239 issued · 222 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 239 | 222 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 160 | 129 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 101 | 100 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 120 | 117 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 110 | 102 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*