**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171813Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-17_1537.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-54 | 85% | 2026-09-21 | military/conflict | Between 2026-08-18 and 2026-09-17 at least one drone attack on Moscow city or Moscow oblast is reported by the Moscow mayor or the Russian Ministry of Defense and by at least one Ukrainian or Western outlet. | True if a drone attack on Moscow city or oblast occurring 2026-08-18 through 2026-09-17 is reported by Russian official channels and by at least one of Reuters, AP, BBC, or a Ukrainian outlet. |
| KKR-20260817-55 | 10% | 2026-10-02 | military/conflict | Between 2026-08-18 and 2026-09-30 the United States conducts a military strike on targets inside the territory of Oman. | True if at least two of Reuters, AP, AFP, or BBC report a US military strike on targets inside Omani territory occurring between 2026-08-18 and 2026-09-30. |
| KKR-20260817-56 | 18% | 2026-12-02 | military/conflict | Between 2026-08-18 and 2026-11-30 United States ground forces conduct combat operations inside the internationally recognized territory of Iran. | True if at least two of Reuters, AP, AFP, or BBC report US ground forces engaged in combat operations inside Iran between 2026-08-18 and 2026-11-30. |
| KKR-20260817-57 | 40% | 2026-12-02 | economics/markets | The US 10-year Treasury constant maturity yield published in FRED series DGS10 is at or above 5.00 percent for at least one business day between 2026-08-18 and 2026-11-30. | True if any DGS10 daily value published by FRED for dates 2026-08-18 through 2026-11-30 is at or above 5.00. |
| KKR-20260817-58 | 60% | 2026-10-19 | cyber | A CVE identifier for the Microsoft Defender vulnerability publicly tracked as ShieldBreak is added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-18 and 2026-10-16. | True if the CISA KEV catalog gains an entry for a Microsoft Defender vulnerability, identified in vendor or CISA documentation as ShieldBreak, with dateAdded between 2026-08-18 and 2026-10-16. |
| KKR-20260817-59 | 25% | 2026-12-02 | disaster | Between 2026-08-18 and 2026-11-30 the WHO Director-General declares the Democratic Republic of the Congo Ebola outbreak a Public Health Emergency of International Concern. | True if WHO publishes a Director-General statement declaring the DRC Ebola outbreak a PHEIC, dated between 2026-08-18 and 2026-11-30. |
| KKR-20260817-60 | 75% | 2026-10-09 | political | No candidate wins a majority of valid votes in the first round of the Brazilian presidential election held on 2026-10-04, sending the contest to a second round per official TSE results. | True if official TSE first-round results for the 2026-10-04 Brazilian presidential election show no candidate above 50 percent of valid votes, requiring a second round. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The ICE Brent crude front-month futures contract settles at or above 100.00 US dollars per barrel on at least one trading day between 2026-0" → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; cited items name Iran, Islamic Republic of; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-08-18 and 2026-09-18 the USGS earthquake catalog records at least one earthquake of magnitude 6.0 or greater with an epicenter " → REJECTED: the resolution names a different subject than the statement — the claim is about Ende, Indonesia, USGS and the resolution settles on True, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-18 and 2027-01-29 the federal trial in California between Meta and state attorneys general over youth social media harms con" → REJECTED: resolution offers alternative VENUES joined by 'or' (…neral trial records a jury verdict, judgment, | or | settlement notice dated…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

694 issued all-time across 14 forecaster arms · 604 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 47 issued · 47 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 138 | 130 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 92 | 80 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 47 | 47 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 58 | 57 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*