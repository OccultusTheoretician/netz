**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 262315Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-26_1513.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261026-52 | 63% | 2027-01-05 | military/conflict | US military forces strike at least one target on Iranian territory, mainland or islands, between 2026-10-27 and 2026-12-31. | TRUE if the White House or Pentagon confirms, or both AP and Reuters report, a US military strike on a target on Iranian territory occurring between 2026-10-27 and 2026-12-31; otherwise FALSE. |
| KKR-20261026-53 | 63% | 2026-11-18 | military/conflict | Houthi forces launch at least one missile or drone at Saudi Arabian territory between 2026-11-02 and 2026-11-15. | TRUE if an official Saudi or Saudi-led coalition statement, or reporting by two of Reuters, AP and AFP, confirms a Houthi missile or drone launched at Saudi territory between 2026-11-02 and 2026-11-15, intercepted or not. |
| KKR-20261026-54 | 59% | 2027-01-08 | economics/markets | The WTI crude oil spot price closes at or below 85.00 US dollars per barrel on at least one day between 2026-11-02 and 2026-12-31. Reference: 100.93 on the packet date. | TRUE if FRED series DCOILWTICO shows any daily value at or below 85.00 dated between 2026-11-02 and 2026-12-31 inclusive; otherwise FALSE. Reference: 100.93 on the packet date. |
| KKR-20261026-55 | 59% | 2026-12-14 | economics/markets | Anthropic Class A common stock begins trading on the Nasdaq under ticker ANT between 2026-11-09 and 2026-12-11. | TRUE if Nasdaq trading records show the first regular trading session for ticker ANT, Anthropic Class A stock, on a date between 2026-11-09 and 2026-12-11 inclusive; otherwise FALSE. |
| KKR-20261026-56 | 42% | 2027-02-02 | political | A new Israeli government formed after the 2026-10-27 Knesset election wins a Knesset confidence vote between 2026-11-02 and 2027-01-29. | TRUE if the Knesset holds a successful confidence vote installing a new government formed after the 2026-10-27 election on a date between 2026-11-02 and 2027-01-29, per Knesset records; otherwise FALSE. |
| KKR-20261026-57 | 45% | 2026-11-16 | cyber | CISA adds CVE-2026-109618 or CVE-2026-109619, the PHP2Shell remote code execution flaws, to its Known Exploited Vulnerabilities catalog between 2026-10-26 and 2026-11-13. | TRUE if the CISA KEV catalog lists CVE-2026-109618 or CVE-2026-109619 with a dateAdded value between 2026-10-26 and 2026-11-13 inclusive; otherwise FALSE. |
| KKR-20261026-58 | 44% | 2027-04-20 | crime/security | The first trial session for the US Marine indicted over the October 2026 robbery and killing of a woman in Naha, Okinawa, is held at Naha District Court between 2026-10-27 and 2027-04-16. | TRUE if Kyodo, NHK, AP or Reuters report the first public trial session for the indicted US Marine in the Naha killing case was held at Naha District Court between 2026-10-27 and 2027-04-16; otherwise FALSE. |
| KKR-20261026-59 | 44% | 2026-12-22 | crime/security | The Southwark Crown Court jury in the Russell Brand sexual offences trial returns a verdict on at least one count between 2026-10-27 and 2026-12-18. | TRUE if BBC, Guardian, AP or Reuters report that the jury in the Brand trial at Southwark Crown Court returned a verdict on at least one count between 2026-10-27 and 2026-12-18; otherwise FALSE. |
| KKR-20261026-60 | 38% | 2026-12-02 | disaster | USGS records at least one magnitude 6.0 or greater earthquake in the Bonin Islands region, latitude 24.0N to 30.0N and longitude 137.0E to 145.0E, between 2026-10-27 and 2026-11-30. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater inside latitude 24.0N to 30.0N and longitude 137.0E to 145.0E with origin time between 2026-10-27 and 2026-11-30 UTC; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Democratic candidates win at least 218 of 435 US House seats in the general election held on 2026-11-03, as called between 2026-11-03 and 20" → REJECTED: cited items name Brazil, France, Serbia; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

5024 issued all-time across 21 forecaster arms · 3310 open (347 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1770 issued · 1261 open · 477 resolved · 273 hits / 204 misses · **Brier 0.300** against its own base rate 57.2% (climatological 0.245) · **skill -0.226**.

*88 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1770 | 1261 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 116 | 105 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 123 | 121 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 122 | 91 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 447 | 332 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 276 | 262 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*