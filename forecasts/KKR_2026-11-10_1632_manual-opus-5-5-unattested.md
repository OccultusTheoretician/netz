**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101632Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-10_1613.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261110-37 | 30% | 2027-01-05 | economics/markets | The Federal Reserve raises the federal funds target range at an FOMC meeting concluding between 2026-11-17 and 2026-12-31. | TRUE if FRED series DFEDTARU shows an upper bound on 2026-12-31 higher than its value on 2026-11-10; FALSE otherwise. |
| KKR-20261110-38 | 50% | 2026-12-15 | economics/markets | The US 10-year Treasury constant-maturity yield closes at or above 5.00 percent on at least one trading day between 2026-11-17 and 2026-12-11. Reference: 4.99 percent on the packet date. | TRUE if FRED series DGS10 records any daily value of 5.00 or higher dated between 2026-11-17 and 2026-12-11 inclusive. |
| KKR-20261110-39 | 50% | 2027-01-05 | economics/markets | The BLS initial release of November 2026 CPI-U shows a seasonally adjusted all-items monthly increase of 0.3 percent or more, published between 2026-12-01 and 2026-12-31. | TRUE if the BLS CPI news release for November 2026, first published between 2026-12-01 and 2026-12-31, reports seasonally adjusted all-items CPI-U change of 0.3 percent or higher. |
| KKR-20261110-40 | 50% | 2027-01-05 | cyber | CISA adds at least one Google Chromium or Chrome vulnerability to the KEV catalog with a date-added value between 2026-11-17 and 2026-12-31. | TRUE if the CISA KEV catalog lists any entry with vendor Google and product Chromium or Chrome whose dateAdded falls between 2026-11-17 and 2026-12-31 inclusive. |
| KKR-20261110-41 | 20% | 2027-03-03 | cyber | The EU adopts restrictive measures naming the Iranian cyber unit Shahid Kaveh or persons tied to it over the French refrigeration-controller attacks, published between 2026-11-17 and 2027-02-28. | TRUE if the Official Journal of the EU (EUR-Lex) publishes a Council decision or implementing regulation between 2026-11-17 and 2027-02-28 listing Shahid Kaveh or a named member of it. |
| KKR-20261110-42 | 15% | 2027-04-05 | political | Pete Hegseth leaves the office of Secretary of Defense through resignation, removal or conviction between 2026-11-17 and 2027-03-31. | TRUE if the defense.gov leadership listing, or a White House announcement reported by Reuters and AP, shows Hegseth no longer serving as Secretary of Defense on or before 2027-03-31. |
| KKR-20261110-43 | 12% | 2027-02-03 | military/conflict | Russia and Ukraine sign a ceasefire or peace agreement between 2026-11-17 and 2027-01-31. | TRUE if both the Russian and Ukrainian governments publicly confirm signing a ceasefire or peace agreement dated 2026-11-17 through 2027-01-31, reported by both Reuters and AP. |
| KKR-20261110-44 | 65% | 2026-12-17 | disaster | USGS records at least one earthquake of magnitude 7.0 or greater anywhere in the world between 2026-11-17 and 2026-12-15. | TRUE if the USGS ComCat catalog lists any event with magnitude 7.0 or higher and origin time between 2026-11-17T00:00Z and 2026-12-15T23:59Z. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude spot closes below 80.00 USD per barrel on at least one trading day between 2026-11-17 and 2026-12-31. Reference: 85.63 on the pack" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The US House adopts at least one article of impeachment against Defense Secretary Pete Hegseth on a roll-call vote held between 2026-11-10 a" → REJECTED: resolution offers alternative VENUES joined by 'or' (…congress.gov | or | house clerk…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5569 issued all-time across 22 forecaster arms · 3847 open (1420 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 372 issued · 358 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 141 | 141 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 198 | 181 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 204 | 202 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 178 | 145 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 518 | 403 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 372 | 358 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*