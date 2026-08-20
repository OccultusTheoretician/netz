**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 202336Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-20_1537.md · forecaster: manual/fable-5/unattested · 6 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260820-09 | 65% | 2026-09-22 | cyber | The CISA Known Exploited Vulnerabilities catalog adds a CVE affecting Zimbra Collaboration with a dateAdded value between 2026-08-21 and 2026-09-18. | The CISA KEV catalog JSON contains an entry whose vendorProject or product field names Zimbra and whose dateAdded falls between 2026-08-21 and 2026-09-18 inclusive. |
| KKR-20260820-10 | 40% | 2026-10-20 | disaster | The USGS ComCat catalog records an earthquake of magnitude 6.0 or greater with epicenter within 150 km of USGS event us6000tkt2 near Ende, Indonesia, with origin time between 2026-08-21 and 2026-10-16. | A USGS ComCat query centered on event us6000tkt2 with a 150 km radius returns at least one magnitude 6.0 or greater event with origin time between 2026-08-21 and 2026-10-16 UTC. |
| KKR-20260820-11 | 88% | 2026-12-14 | disaster | The NOAA Climate Prediction Center ENSO diagnostic discussion scheduled for 2026-12-10 carries an active El Nino Advisory status. | The CPC ENSO diagnostic discussion published on or about 2026-12-10 states an El Nino Advisory is in effect; an ENSO-neutral or La Nina status grades false. |
| KKR-20260820-12 | 50% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures record an official daily settlement at or above 100.00 USD per barrel on at least one trading day between 2026-08-21 and 2026-10-30. | Published ICE Brent front-month official settlement prices show at least one value at or above 100.00 USD between 2026-08-21 and 2026-10-30 inclusive. |
| KKR-20260820-13 | 30% | 2026-12-22 | political | Congress.gov records Senate passage of a bill whose short title includes CLARITY Act between 2026-08-21 and 2026-12-18. | Congress.gov shows a passed-Senate action, by roll call or voice vote, on a bill whose short title includes CLARITY Act, with the action dated between 2026-08-21 and 2026-12-18. |
| KKR-20260820-14 | 70% | 2026-09-23 | military/conflict | A Russian missile or drone strike on the city of Kyiv occurring between 2026-08-21 and 2026-09-20 kills five or more people. | At least two of Reuters, AP, AFP report a single Russian strike on Kyiv city between 2026-08-21 and 2026-09-20 with an officially stated death toll of five or more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The HHS OCR breach portal lists an entry naming CareCloud with 3,000,000 or more individuals affected and a submission date between 2026-06-" → REJECTED: event window opens 2026-06-01, before this row is sealed (2026-08-20) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "US Treasury OFAC publishes at least one Iran-related sanctions designation action dated between 2026-08-21 and 2026-09-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ofac recent actions register | or | the federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Ukrainian authorities formally schedule a presidential election with a set voting date, with the scheduling act occurring between 2026-08-21" → REJECTED: the resolution names a different subject than the statement — the claim is about Ukrainian and the resolution settles on AFP, AP, Central, Commission. A row whose resolution checks a different fact can be scored correct while being wrong
- "An attack on, or seizure of, a commercial merchant vessel occurs in the Strait of Hormuz or Gulf of Oman between 2026-08-21 and 2026-10-20." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…a ukmto advisory | or | at least two of reuters, ap, afp report a spe…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

809 issued all-time across 14 forecaster arms · 719 open (14 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 67 issued · 67 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 113 | 101 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 67 | 67 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 69 | 68 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*