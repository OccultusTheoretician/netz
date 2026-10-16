**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162053Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-27 | 75% | 2026-11-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry with vendorProject BeyondTrust and a dateAdded between 2026-10-16 and 2026-10-30, following the Remote Support zero-day disclosed on 2026-10-16. | The KEV JSON feed at cisa.gov contains an entry whose vendorProject field is BeyondTrust and whose dateAdded is between 2026-10-16 and 2026-10-30 inclusive. Any BeyondTrust product qualifies. |
| KKR-20261016-28 | 55% | 2026-11-18 | military/conflict | Between 2026-10-19 and 2026-11-15 at least one Houthi missile or drone attack on Saudi Arabian territory is both claimed by the Houthi military spokesman and confirmed as an interception or impact by Saudi authorities or by Reuters, AP, or AFP. | A Houthi claim and an independent confirmation (Saudi Press Agency, Saudi Defense Ministry, Reuters, AP, or AFP) both describe a missile or drone attack on Saudi territory dated 2026-10-19 to 2026-11-15. |
| KKR-20261016-29 | 30% | 2026-11-24 | military/conflict | Between 2026-10-19 and 2026-11-20 the US Department of Defense or US Central Command publicly announces a US military strike on at least one target located inside the internationally recognized territory of Iran. | An official DoD or CENTCOM release, briefing, or official account post acknowledges a US strike on a target inside Iran conducted between 2026-10-19 and 2026-11-20. Strikes on proxies or vessels outside Iran do not count. |
| KKR-20261016-30 | 10% | 2027-01-19 | political | Edi Rama ceases to hold the office of Prime Minister of Albania, by resignation, dismissal, or a successful no-confidence vote, between 2026-10-16 and 2027-01-15. | An official Albanian government or parliamentary announcement, confirmed by Reuters, AP, or AFP, records that Rama left or was removed from the office of Prime Minister on a date between 2026-10-16 and 2027-01-15 inclusive. |
| KKR-20261016-31 | 60% | 2026-11-17 | political | The Republican nominee wins the Texas United States Senate general election held on 2026-11-03, as called by the Associated Press. | The Associated Press race call for the 2026-11-03 Texas US Senate general election names the Republican nominee as winner. A race uncalled by AP as of the deadline resolves false. |
| KKR-20261016-32 | 40% | 2026-12-03 | crime/security | Between 2026-10-16 and 2026-11-30 the Turkish broadcast regulator RTUK imposes a broadcast suspension (screen blackout) of any duration on Halk TV or revokes its license. | An RTUK decision suspending Halk TV broadcasts for any period, or cancelling its license, is announced between 2026-10-16 and 2026-11-30 and reported by Reuters, AP, or AFP. Fines alone resolve false. |
| KKR-20261016-33 | 15% | 2026-12-22 | crime/security | Between 2026-10-16 and 2026-12-18 Israeli prosecutors file an indictment against at least one Israeli civilian for the West Bank attack on olive harvesters reported on 2026-10-16 in which Washington Post journalist Heidi Levine was injured. | An indictment of an Israeli civilian for that attack is filed in an Israeli court between 2026-10-16 and 2026-12-18, reported by Times of Israel or Haaretz and by Reuters, AP, or AFP. Arrests alone resolve false. |
| KKR-20261016-34 | 45% | 2026-11-18 | disaster | At least one wildfire igniting between 2026-10-17 and 2026-11-15 in Los Angeles, Ventura, Orange, Riverside, San Bernardino, San Diego, or Santa Barbara County reaches 10,000 acres or more per CAL FIRE incident data. | The CAL FIRE incidents register lists a fire in one of the seven named counties with a start date from 2026-10-17 through 2026-11-15 and acreage of at least 10,000 as of the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC statement released at the close of the meeting scheduled for 2026-10-27 to 2026-10-28 announces a change to the federal funds targe" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The EIA daily Cushing OK WTI spot price (series RWTC) prints at or above 100.00 dollars per barrel on at least one trading day between 2026-" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4277 issued all-time across 21 forecaster arms · 3166 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 362 issued · 304 open · 50 resolved · 34 hits / 16 misses · **Brier 0.248** against its own base rate 68.0% (climatological 0.218) · **skill -0.140**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1501 | 1205 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 184 | 179 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 138 | 138 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*