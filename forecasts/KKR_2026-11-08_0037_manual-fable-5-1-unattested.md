**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 080037Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-07_1612.md · forecaster: manual/fable-5.1/unattested · 6 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261108-01 | 60% | 2026-11-24 | military/conflict | Between 2026-11-08 and 2026-11-21 inclusive, US or Israeli forces conduct at least one new airstrike or missile strike on Iranian territory, corroborated by at least two of Reuters, AP, and AFP. | True if at least two of Reuters, AP, AFP report a US or Israeli strike on Iranian soil occurring between 2026-11-08 and 2026-11-21. Strikes before 2026-11-08 do not count. |
| KKR-20261108-02 | 78% | 2027-01-11 | political | Hakeem Jeffries is elected Speaker of the US House on the first ballot of the 120th Congress, with the vote held between 2027-01-03 and 2027-01-07 inclusive. | True if the House Clerk roll call record shows Jeffries winning a majority of votes cast for a person on the first Speaker ballot held between 2027-01-03 and 2027-01-07. |
| KKR-20261108-03 | 30% | 2026-12-07 | economics/markets | Front-month WTI crude settles above 100.00 USD per barrel on at least one NYMEX trading day between 2026-11-09 and 2026-12-04 inclusive. Reference: 90.83 on the packet date. | True if CME NYMEX publishes a front-month WTI daily settlement price strictly above 100.00 for any trading day from 2026-11-09 through 2026-12-04. |
| KKR-20261108-04 | 40% | 2027-04-02 | economics/markets | Anthropic common shares begin trading on the NYSE or Nasdaq between 2026-11-09 and 2027-03-31 inclusive. | True if NYSE or Nasdaq exchange records show a first trading day for Anthropic shares between 2026-11-09 and 2027-03-31, confirmed by an SEC EDGAR filing. |
| KKR-20261108-05 | 50% | 2026-12-01 | cyber | The CISA KEV catalog adds at least one CVE affecting a QNAP product with a date-added value between 2026-11-08 and 2026-11-28 inclusive. | True if the CISA KEV JSON feed contains an entry with vendorProject QNAP and dateAdded between 2026-11-08 and 2026-11-28 inclusive. |
| KKR-20261108-06 | 30% | 2026-12-09 | disaster | USGS records at least one earthquake of magnitude 6.5 or greater with an epicenter in Japan or within 200 km of its coast between 2026-11-08 and 2026-12-07 inclusive. | True if the USGS earthquake catalog lists an M6.5 or greater event between 2026-11-08 and 2026-12-07 whose location string names Japan or whose epicenter lies within 200 km of Japan. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-11-08 and 2026-11-21 inclusive, Ukrenergo or the Kyiv City Military Administration announces emergency power outages in Kyiv ci" → REJECTED: resolution offers alternative VENUES joined by 'or' (…administration statement, reported by reuters | or | ap, attributes emergency outages in kyiv to a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new New Zealand government is sworn in by the Governor-General between 2026-11-08 and 2026-12-11 inclusive." → REJECTED: resolution offers alternative VENUES joined by 'or' (… 2026-12-11, per the governor-general website | or | reuters…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The S&P 500 closes below 7,000.00 on at least one trading day between 2026-11-09 and 2026-12-18 inclusive. Reference: 7,376.86 on the packet" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the resolution names only a venue or register (dow, indices, jones) and no subject - the register is where to look, not what is claimed; name the subject inside it; the resolution names a different subject than the statement — the claim is about Reference and the resolution settles on Dow, Indices, Jones. A row whose resolution checks a different fact can be scored correct while being wrong
- "The CISA KEV catalog adds at least 15 entries with date-added values between 2026-11-08 and 2026-12-05 inclusive." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Polish prosecutors announce that at least one person has been formally charged in connection with the 2026-11-07 Krakow shooting, with the c" → REJECTED: resolution offers alternative VENUES joined by 'or' (…-11-08 and 2026-11-21, is reported by reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5439 issued all-time across 22 forecaster arms · 3717 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 500 issued · 385 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 102 | 102 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 183 | 166 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 184 | 182 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 163 | 130 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 500 | 385 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 349 | 335 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*