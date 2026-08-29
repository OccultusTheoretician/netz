**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292146Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-29_1537.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-68 | 33% | 2026-10-20 | cyber | The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-82078 or CVE-2026-81578 with a date_added value between 2026-08-29 and 2026-10-16. | TRUE if the CISA KEV catalog contains an entry for CVE-2026-82078 or CVE-2026-81578 carrying a dateAdded value between 2026-08-29 and 2026-10-16 inclusive. |
| KKR-20260829-69 | 33% | 2026-11-04 | cyber | Stolen City of Berlin administrative data is published on an extortion leak site between 2026-08-29 and 2026-10-31. | TRUE if at least two of BBC, Reuters, dpa, Tagesspiegel or Heise report that data taken from Berlin city systems was published by the extortion group in that window. |
| KKR-20260829-70 | 25% | 2026-12-03 | economics | Front-month ICE Brent crude settles at or above 100.00 USD per barrel on at least one trading day between 2026-09-01 and 2026-11-30. | TRUE if ICE publishes a front-month Brent futures settlement price of 100.00 USD or higher for any trading day inside that window. |
| KKR-20260829-71 | 44% | 2027-02-17 | political | A petition for a writ of certiorari arising from the 2026-08-28 Ninth Circuit prediction-market ruling is docketed at the US Supreme Court between 2026-08-29 and 2027-02-13. | TRUE if the Supreme Court electronic docket lists a certiorari petition naming Kalshi and Nevada gaming regulators, docketed on or before 2027-02-13. |
| KKR-20260829-72 | 53% | 2026-10-19 | military | The Ukrainian Air Force reports at least 500 Russian drones and missiles launched in one overnight attack between 2026-09-01 and 2026-10-15. | TRUE if a Ukrainian Air Force overnight air-situation report covering a night inside that window states a combined launch total of 500 or more munitions. |
| KKR-20260829-73 | 52% | 2026-11-04 | disaster | The confirmed death toll in Nepal from the 2026-08-26 Rasuwa flood reaches at least 1000 between 2026-08-30 and 2026-10-31. | TRUE if Nepal Police or the NDRRMA give a confirmed Nepal death toll of 1000 or more inside that window, carried by two of Reuters, AP, AFP or BBC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At the scheduled 2026-09-16 FOMC decision the Committee raises the federal funds target range to 3.75 to 4.00 percent." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The UK government announces activation of Operation Safeguard or a new prison early release measure between 2026-09-01 and 2026-11-20." → REJECTED: resolution offers alternative VENUES joined by 'or' (…gov.uk press release | or | written ministerial…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A single Russian strike on Kyiv city or Kyiv oblast kills at least 15 people between 2026-09-01 and 2026-10-10." → REJECTED: the resolution names a different subject than the statement — the claim is about Kyiv, Russian and the resolution settles on AFP, AP, BBC, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "The CFTC announces a new enforcement action over misuse of nonpublic information in event contracts between 2026-09-01 and 2026-12-31." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1118 issued all-time across 14 forecaster arms · 957 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 281 issued · 264 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 281 | 264 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 113 | 112 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 133 | 130 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 119 | 111 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*