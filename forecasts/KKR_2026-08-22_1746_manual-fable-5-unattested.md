**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221746Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-22_1516.md · forecaster: manual/fable-5/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-26 | 10% | 2026-09-25 | disaster | USGS records an earthquake of magnitude 5.5 or greater within 100 km of the 2026-08-20 M6.7 Aniso, Peru epicenter (14.641 S, 73.524 W) with origin time between 2026-08-24 and 2026-09-23. | The USGS ComCat catalog lists an event of magnitude 5.5 or greater, any depth, within 100 km of 14.641 S 73.524 W, origin time 2026-08-24 00:00 UTC to 2026-09-23 23:59 UTC. |
| KKR-20260822-27 | 22% | 2027-01-19 | political | A Labor MP holds office as Premier of Victoria on 2027-01-15, meaning Labor retained government at the 2026-11-28 Victorian state election. | On 2027-01-15 the Parliament of Victoria or Victorian Government official listing shows the sitting Premier as a member of the Australian Labor Party. |
| KKR-20260822-28 | 25% | 2026-10-06 | military/conflict | Between 2026-08-23 and 2026-10-02 the governments of the United States and Iran both publicly confirm an agreement (ceasefire or settlement) whose announced terms include reopening the Strait of Hormuz to commercial shipping. | Statements from both the US government and the government of Iran, dated 2026-08-23 to 2026-10-02, confirm one agreement whose published terms include reopening Hormuz to commercial shipping; confirmed by Reuters and AP. |
| KKR-20260822-29 | 30% | 2026-10-13 | economics/markets | Between 2026-08-23 and 2026-10-02 the United States and Canada both announce an agreement that rescinds or suspends the 50 percent US tariffs on Canadian goods that took effect 2026-08-22, and US implementation is published by 2026-10-09. | Both governments announce the agreement between 2026-08-23 and 2026-10-02, and a Federal Register document or CBP CSMS message published by 2026-10-09 removes or suspends the 50 percent tariffs for all or most covered Canadian goods. |
| KKR-20260822-30 | 40% | 2026-11-03 | economics/markets | The 10-year US Treasury constant-maturity yield closes at or above 5.00 percent on at least one trading day between 2026-08-24 and 2026-10-30. | FRED series DGS10 shows a value of 5.00 or higher for at least one observation dated between 2026-08-24 and 2026-10-30 inclusive. |
| KKR-20260822-31 | 45% | 2026-09-15 | cyber | The CISA KEV catalog adds at least two distinct Microsoft CVEs in the September 2026 Patch Tuesday week, with dateAdded values between 2026-09-08 and 2026-09-11. | The CISA KEV JSON feed contains at least two distinct CVE entries with vendorProject Microsoft and dateAdded between 2026-09-08 and 2026-09-11 inclusive. |
| KKR-20260822-32 | 50% | 2026-09-16 | military/conflict | A single Russian strike on one Ukrainian locality, occurring between 2026-08-24 and 2026-09-13, produces an official Ukrainian death toll of 15 or more. | Ukrainian State Emergency Service, National Police, or regional military administration states 15 or more killed from one Russian strike on one locality on one day within 2026-08-24 to 2026-09-13, as reported by Reuters or AP. |
| KKR-20260822-33 | 60% | 2026-10-13 | crime/security | Between 2026-08-24 and 2026-10-09 the Clark County, Nevada jury in the Tupac Shakur murder trial returns a verdict of guilty of murder (first or second degree) against Duane Davis. | The Eighth Judicial District Court (Clark County) docket, or Reuters or AP, records a jury verdict of guilty of first- or second-degree murder against Duane Davis returned between 2026-08-24 and 2026-10-09. |
| KKR-20260822-34 | 80% | 2026-12-04 | political | Democrats win a majority of the US House of Representatives in the 2026-11-03 midterm election, with the Associated Press calling control of the chamber for Democrats by 2026-12-01. | By 2026-12-01 the Associated Press has called House control for Democrats, crediting Democratic candidates with at least 218 of 435 seats in the 2026-11-03 general election. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Cumulative confirmed Bundibugyo virus disease cases in the Democratic Republic of the Congo reach 10,000 or more in official reporting with " → REJECTED: event window opens 2026-08-19, before this row is sealed (2026-08-22, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

865 issued all-time across 14 forecaster arms · 775 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 81 issued · 81 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/opus-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 85 | 84 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*