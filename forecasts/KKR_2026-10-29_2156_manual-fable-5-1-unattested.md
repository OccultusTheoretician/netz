**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292156Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-29_1513.md · forecaster: manual/fable-5.1/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261029-13 | 85% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one Cisco ASA, FTD, or Secure Firewall vulnerability with a dateAdded between 2026-10-29 and 2026-11-13. | The CISA KEV JSON feed contains an entry with vendorProject Cisco and a product field containing ASA, Adaptive Security Appliance, FTD, Firepower Threat Defense, or Secure Firewall, with dateAdded from 2026-10-29 through 2026-11-13. |
| KKR-20261029-14 | 10% | 2027-01-05 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendorProject field contains Telegram with a dateAdded between 2026-10-29 and 2026-12-31. | The CISA KEV JSON feed contains an entry whose vendorProject field contains Telegram and whose dateAdded is from 2026-10-29 through 2026-12-31. |
| KKR-20261029-15 | 78% | 2026-12-17 | political | Democratic candidates win at least 218 of the 435 seats in the US House of Representatives in the general election of 2026-11-03, as determined by Associated Press race calls made by 2026-12-15. | Associated Press race calls as of 2026-12-15 show Democrats winning 218 or more House seats in the 2026-11-03 general election; uncalled races do not count toward 218. |
| KKR-20261029-16 | 30% | 2027-01-08 | political | When the 120th Congress convenes in January 2027, the Democratic caucus (Democrats plus independents caucusing with them) holds at least 51 of the 100 US Senate seats. | The senate.gov Party Division page, read on 2027-01-06, lists at least 51 senators who are Democrats or independents caucusing with Democrats for the 120th Congress. |
| KKR-20261029-17 | 40% | 2026-12-02 | military/conflict | Between 2026-10-30 and 2026-11-30, at least one merchant vessel is seized, boarded, or struck by a weapon in the Strait of Hormuz, Gulf of Oman, or Persian/Arabian Gulf, as recorded in a UKMTO incident report or advisory. | The UKMTO (ukmto.org) incidents or advisories list includes an entry dated 2026-10-30 through 2026-11-30 describing a merchant vessel seized, boarded, or hit by a projectile or explosive in the Strait of Hormuz, Gulf of Oman, or Persian/Arabian Gulf. |
| KKR-20261029-18 | 65% | 2026-12-01 | crime/security | Between 2026-10-30 and 2026-11-27, the Court of Appeal of the Supreme Court of Victoria delivers a judgment dismissing in full the appeal by Erin Patterson against her murder and attempted murder convictions. | A Victorian Court of Appeal judgment dated 2026-10-30 through 2026-11-27, published on AustLII or the court website, dismisses the Patterson appeal against conviction on every ground; any quashed conviction or retrial order resolves false. |
| KKR-20261029-19 | 20% | 2026-12-02 | disaster | At least one earthquake occurring between 2026-10-30 and 2026-11-30 receives a GDACS alert level of Red. | The GDACS event list (gdacs.org) shows an earthquake entry with alert level Red and an event date from 2026-10-30 through 2026-11-30, as displayed at any time up to the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC statement released on 2026-12-09 sets a federal funds target range whose upper bound is higher than the upper bound of the range in" → REJECTED: event window opens 2026-10-28, before this row is sealed (2026-10-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The ECB monetary policy decision announced on 2026-12-17 leaves the deposit facility rate unchanged from the level announced on 2026-10-29." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-29 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The FRED series DCOILBRENTEU (Brent crude spot price) observation for 2026-12-31 is below 100.00 US dollars per barrel. Reference: Brent 109" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5132 issued all-time across 22 forecaster arms · 3410 open (553 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 467 issued · 352 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 10 | 10 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 137 | 120 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 138 | 136 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 131 | 98 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 467 | 352 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 291 | 277 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*