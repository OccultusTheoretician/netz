**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182120Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-49 | 41% | 2026-11-04 | cyber | Between 2026-10-19 and 2026-11-01, CISA adds a SiteGuard WAF vulnerability to its Known Exploited Vulnerabilities catalog. | The CISA KEV catalog JSON carries an entry whose vendorProject, product, or shortDescription field contains SiteGuard, with a dateAdded value between 2026-10-19 and 2026-11-01 inclusive. |
| KKR-20261018-50 | 60% | 2026-11-10 | economics/markets | Between 2026-10-19 and 2026-11-06, the US 10-year Treasury constant-maturity yield closes at or above 5.25 percent on at least one business day. Reference: 5.10 percent on the packet date (prior-session close). | FRED series DGS10 shows a value of 5.25 or higher for at least one date between 2026-10-19 and 2026-11-06 inclusive. Reference: 5.10 percent on the packet date. |
| KKR-20261018-51 | 60% | 2026-11-10 | economics/markets | Between 2026-10-19 and 2026-11-06, the CME NYMEX WTI crude futures contract nearest expiry settles at or above 110.00 dollars per barrel on at least one trading day. Reference: 99.02 dollars on the packet date (prior-session close). | CME Group settlement data for the WTI contract nearest expiry shows a daily settlement of 110.00 or higher on at least one trading day between 2026-10-19 and 2026-11-06 inclusive. Reference: 99.02 on the packet date. |
| KKR-20261018-52 | 64% | 2026-11-04 | military/conflict | Between 2026-10-19 and 2026-11-01, a Ukrainian drone attack damages an energy facility in Saint Petersburg or Leningrad Oblast. | At least two of Reuters, AP, BBC, and Al Jazeera report a Ukrainian drone attack that damaged an oil, fuel, port, or power facility in Saint Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-01. |
| KKR-20261018-53 | 64% | 2026-11-04 | military/conflict | Between 2026-10-19 and 2026-11-01, Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack. | The Ukrainian Air Force reports at least 500 drones and missiles combined launched in one overnight attack between 2026-10-19 and 2026-11-01, confirmed by at least two of Reuters, AP, BBC, and Al Jazeera. |
| KKR-20261018-54 | 64% | 2026-11-04 | military/conflict | Between 2026-10-19 and 2026-11-01, United States or Israeli forces strike a target inside Iran and the US or Israeli government publicly acknowledges the strike. | At least two of Reuters, AP, BBC, and Al Jazeera report an air, missile, or drone strike on a target inside Iran between 2026-10-19 and 2026-11-01, acknowledged by the US or Israeli government. |
| KKR-20261018-55 | 42% | 2026-11-04 | disaster | Between 2026-10-19 and 2026-11-01, an earthquake of magnitude 5.0 or greater strikes within 100 km of Khuzdar, Pakistan. | The USGS ComCat catalog lists an earthquake of magnitude 5.0 or greater with epicenter within 100 km of 27.80 N 66.62 E and origin time between 2026-10-19 00:00 UTC and 2026-11-01 23:59 UTC. |
| KKR-20261018-56 | 42% | 2026-10-29 | disaster | Between 2026-10-19 and 2026-10-26, the center of Hurricane Trudy makes landfall on the Mexican coast with maximum sustained winds of at least 74 mph. | NHC advisories or the NHC Tropical Cyclone Report for Trudy state that its center crossed the Mexican coast between 2026-10-19 and 2026-10-26 with maximum sustained winds of at least 74 mph. |
| KKR-20261018-57 | 39% | 2026-11-04 | crime/security | Between 2026-10-19 and 2026-11-01, an official French figure puts cumulative arrests in the student-led protest wave at 3,000 or more. Reference: 1,800 arrests reported by 2026-10-18. | A French Interior Ministry, police, or prosecutor figure published between 2026-10-19 and 2026-11-01 and relayed by two of Reuters, AP, AFP, and the Guardian puts cumulative protest-related arrests at 3,000 or more. Reference: 1,800 on 2026-10-18. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-19 and 2026-11-08, the person serving as French Prime Minister on 2026-10-18 resigns, is dismissed, or is replaced." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4463 issued all-time across 21 forecaster arms · 3352 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1571 issued · 1275 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1571 | 1275 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 86 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 378 | 320 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 165 | 165 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*