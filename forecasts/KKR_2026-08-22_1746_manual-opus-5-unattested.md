**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221746Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-22_1516.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-40 | 65% | 2026-10-05 | economics | Canadian counter-tariffs on US-origin goods take legal effect between 2026-08-24 and 2026-09-30 in response to the 50 percent US duties imposed 2026-08-22. | Canada Gazette Part II or a Department of Finance Canada order shows a surtax on US-origin goods with an effective date between 2026-08-24 and 2026-09-30. |
| KKR-20260822-41 | 72% | 2026-10-21 | political | A complaint challenging the lawfulness of the Section 338 tariffs on Canadian goods is filed in a US federal court between 2026-08-24 and 2026-10-16. | A US Court of International Trade or federal district court docket shows a complaint filed in that window seeking to invalidate or enjoin the Section 338 duties on Canadian imports. |
| KKR-20260822-42 | 12% | 2027-02-05 | military_conflict | A general ceasefire in the Russia-Ukraine war takes effect between 2026-08-24 and 2027-01-31. | Both the Russian and Ukrainian governments announce a general cessation of hostilities taking effect inside the window, reported by Reuters and the Associated Press. |
| KKR-20260822-43 | 62% | 2026-11-04 | cyber | The CISA Known Exploited Vulnerabilities catalog gains at least one entry with vendorProject Microsoft and a dateAdded between 2026-08-24 and 2026-10-31. | The CISA KEV catalog JSON contains at least one record where vendorProject is Microsoft and dateAdded falls between 2026-08-24 and 2026-10-31. |
| KKR-20260822-44 | 32% | 2026-11-06 | cyber | A single npm registry supply-chain compromise affecting 100 or more distinct packages occurs between 2026-08-24 and 2026-10-31. | Two of BleepingComputer, The Hacker News, and Socket describe one npm campaign in which 100 or more distinct packages were published carrying malicious code. |
| KKR-20260822-45 | 58% | 2026-10-21 | crime_security | A jury returns a guilty verdict on the murder count against Duane Davis in the Clark County, Nevada prosecution over the 1996 killing of Tupac Shakur, between 2026-08-24 and 2026-10-16. | The Clark County District Court docket records a jury verdict of guilty on the murder count, entered inside that window. |
| KKR-20260822-46 | 55% | 2026-10-28 | disaster | USGS catalogs at least one earthquake of magnitude 7.5 or greater with an origin time between 2026-08-24 and 2026-10-23. | The USGS ComCat catalog lists at least one event with magnitude 7.5 or above and an origin time between 2026-08-24 and 2026-10-23. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range above 3.50 to 3.75 percent at the meeting concluding 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "ICE Brent front-month futures settle at or above 105.00 US dollars per barrel on at least one trading day between 2026-08-24 and 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The United States and Iran announce an agreement providing for resumption of routine commercial transit through the Strait of Hormuz, announ" → REJECTED: the resolution names only a venue or register (Reuters, associated, press) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

877 issued all-time across 14 forecaster arms · 787 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 99 issued · 99 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 122 | 110 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 81 | 81 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 99 | 99 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 90 | 89 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*