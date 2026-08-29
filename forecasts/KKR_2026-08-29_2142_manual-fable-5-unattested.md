**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292142Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-28_1518.md · forecaster: manual/fable-5/unattested · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-10 | 93% | 2026-10-02 | military/conflict | Russian forces conduct at least one drone or missile strike on Kyiv between 2026-09-01 and 2026-09-30. | At least two of Reuters, AP, AFP, or BBC report a Russian drone or missile strike on Kyiv occurring between 2026-09-01 and 2026-09-30. |
| KKR-20260829-11 | 40% | 2026-12-02 | military/conflict | The United States and Iran convene at least one publicly acknowledged round of direct or mediated negotiations between 2026-08-29 and 2026-11-30. | Both the US and Iranian governments publicly acknowledge that direct or mediated negotiations between their officials convened on at least one date between 2026-08-29 and 2026-11-30. |
| KKR-20260829-12 | 40% | 2027-01-04 | cyber | CISA adds a ServiceNow vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-29 and 2026-12-31. | The CISA Known Exploited Vulnerabilities catalog contains at least one entry with vendorProject ServiceNow and a dateAdded value between 2026-08-29 and 2026-12-31. |
| KKR-20260829-13 | 55% | 2026-10-19 | disaster | The combined confirmed death toll from the Nepal-Tibet flash floods reaches at least 1000 between 2026-08-29 and 2026-10-15. | Official Nepali government figures or OCHA reporting state a combined Nepal and Tibet confirmed death toll of at least 1000 from the August 2026 flash floods, on or before 2026-10-15. |
| KKR-20260829-14 | 30% | 2026-10-02 | disaster | The barrier lake at the Nepal-China border produces a further outburst or overflow causing new evacuations, damage, or deaths between 2026-08-29 and 2026-09-30. | At least two of BBC, Guardian, Al Jazeera, Reuters, or AP report a new outburst or overflow from the Nepal-China barrier lake between 2026-08-29 and 2026-09-30 causing fresh evacuations, damage, or deaths. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Front-month Brent crude settles above 100 US dollars on at least one trading day between 2026-09-01 and 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The S&P 500 closes below 7000 on at least one trading day between 2026-09-01 and 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds a PaperCut vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-28 and 2026-10-30." → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "A presidential document renaming Lake Ontario as Lake America is published in the Federal Register with a publication date between 2026-08-2" → REJECTED: event window opens 2026-08-27, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Austrian authorities announce at least one arrest connected to the Vienna museum diamond necklace theft between 2026-08-29 and 2026-12-31." → REJECTED: cited items name Egypt; the claim is about Austria — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

1059 issued all-time across 14 forecaster arms · 898 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 106 issued · 105 open · 1 resolved · 1 hits / 0 misses · **Brier 0.090** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 249 | 232 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 106 | 105 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 121 | 118 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 111 | 103 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*