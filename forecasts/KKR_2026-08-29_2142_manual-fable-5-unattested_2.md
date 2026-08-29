**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292142Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-29_1537.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-36 | 80% | 2026-10-05 | military/conflict | Between 2026-09-01 and 2026-09-30, at least one Russian strike event in Kyiv city or Kyiv oblast kills 10 or more people according to Ukrainian state authorities. | Ukrainian state authorities attribute 10 or more deaths to a single strike event in Kyiv city or oblast occurring between 2026-09-01 and 2026-09-30, carried by two international news agencies. |
| KKR-20260829-37 | 30% | 2026-12-03 | political | Between 2026-08-30 and 2026-11-30, the US and Iranian governments both publicly confirm a specific round of direct or mediated negotiations, with venue or date named. | The US State Department or White House and the Iranian foreign ministry each publicly confirm a negotiation round with named venue or date occurring between 2026-08-30 and 2026-11-30, per two international outlets. |
| KKR-20260829-38 | 50% | 2026-11-03 | disaster | By 2026-10-30, the combined official confirmed death toll from the August 2026 Nepal-Tibet glacial outburst floods, per Nepali and Chinese authorities, reaches at least 1,000. | AP, Reuters, AFP, or BBC report official Nepali plus Chinese confirmed-dead figures for the August 2026 flood totaling 1,000 or more, dated on or before 2026-10-30. |
| KKR-20260829-39 | 65% | 2026-10-02 | cyber | A PaperCut vulnerability is added to the CISA KEV catalog with a dateAdded value between 2026-08-29 and 2026-09-30. | The CISA KEV catalog JSON contains at least one entry naming PaperCut with dateAdded between 2026-08-29 and 2026-09-30 inclusive. |
| KKR-20260829-40 | 45% | 2026-12-01 | economics/markets | ICE Brent crude front-month futures settle at or above 95.00 USD per barrel on at least one trading day between 2026-09-01 and 2026-11-27. | Official ICE Brent front-month daily settlement prices show at least one settlement at or above 95.00 USD between 2026-09-01 and 2026-11-27. |
| KKR-20260829-41 | 55% | 2026-12-03 | political | Between 2026-08-29 and 2026-11-30, Treasury OFAC publishes a new or amended Venezuela general license authorizing petroleum-sector transactions. | The OFAC Venezuela sanctions page carries a general license, new or amended, dated between 2026-08-29 and 2026-11-30, whose text authorizes petroleum-sector transactions. |
| KKR-20260829-42 | 30% | 2026-11-03 | crime/security | Between 2026-08-29 and 2026-10-31, US authorities remove Milo Yiannopoulos from the United States. | Two international outlets, citing DHS, ICE, or court records, report Yiannopoulos removed or deported from the US on a date between 2026-08-29 and 2026-10-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-01 and 2026-11-30, an attack on or seizure of a commercial vessel in the Strait of Hormuz or Gulf of Oman is publicly logged" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The HHS OCR breach portal lists a filing by McKesson or a McKesson subsidiary, submitted between 2026-08-01 and 2026-11-30, covering 500 or " → REJECTED: resolution offers alternative VENUES joined by 'or' (…entry naming mckesson | or | a subsidiary with…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; event window opens 2026-08-01, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The FOMC statement of 2026-09-16 leaves the federal funds target range at or above the pre-meeting range of 3.50 to 3.75 percent." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names a different subject than the statement — the claim is about FOMC and the resolution settles on Federal, Reserve. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1087 issued all-time across 14 forecaster arms · 926 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 113 issued · 112 open · 1 resolved · 1 hits / 0 misses · **Brier 0.090** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 262 | 245 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 113 | 112 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 127 | 124 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 113 | 105 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*