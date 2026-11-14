**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 142354Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-14_1613.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261114-16 | 55% | 2026-11-24 | political | Donald Trump, Vladimir Putin and Xi Jinping hold an in-person trilateral meeting, all three present together, in China between 2026-11-17 and 2026-11-21, around the APEC Leaders Meeting in Shenzhen on 2026-11-18 and 2026-11-19. | True if at least two of Reuters, AP, BBC or Xinhua report that the three leaders met together in person in China between 2026-11-17 and 2026-11-21. |
| KKR-20261114-17 | 25% | 2027-02-02 | economics/markets | The Europe Brent spot price (EIA, FRED series DCOILBRENTEU) closes above 110.00 USD per barrel on at least one trading day between 2026-11-16 and 2027-01-29. Reference: 95.84 USD on the packet date. | True if FRED DCOILBRENTEU shows any daily value above 110.00 dated between 2026-11-16 and 2027-01-29. Reference: 95.84 on 2026-11-14. |
| KKR-20261114-18 | 92% | 2026-11-23 | economics/markets | Grand Theft Auto VI launches on PlayStation 5 and Xbox Series X|S on its scheduled release date of 2026-11-19. | True if Rockstar Games or Take-Two Interactive confirms the game launched and became playable on 2026-11-19, with the PlayStation Store listing it as released on that date. |
| KKR-20261114-19 | 10% | 2027-03-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds a PostgreSQL vulnerability with a dateAdded value between 2026-11-16 and 2027-02-26. | True if the CISA KEV catalog JSON carries an entry with vendorProject PostgreSQL and dateAdded between 2026-11-16 and 2027-02-26. |
| KKR-20261114-20 | 20% | 2027-03-02 | cyber | The US Department of Justice announces criminal charges against at least one named individual tied to the North Korean campaign behind the roughly 400 million USD crypto theft, between 2026-11-16 and 2027-02-26. | True if a justice.gov press release dated between 2026-11-16 and 2027-02-26 announces an indictment or criminal complaint naming a defendant tied to that campaign. |
| KKR-20261114-21 | 40% | 2027-01-19 | crime/security | At least one person is criminally charged in state or federal court in connection with the bomb found at the Illinois ethanol plant near Peoria, with charges filed between 2026-11-15 and 2027-01-15. | True if a DOJ press release, federal docket or Illinois court record shows charges filed between 2026-11-15 and 2027-01-15 over the device found at the plant. |
| KKR-20261114-22 | 15% | 2027-03-03 | political | South Sudan opens polling for its first national general election on any day between 2027-02-01 and 2027-02-28. | True if South Sudan's National Elections Commission and at least one of the UN, AU or IGAD observer missions report polls opened for the national election between 2027-02-01 and 2027-02-28. |
| KKR-20261114-23 | 8% | 2027-02-03 | military/conflict | Russia and Ukraine both announce a general ceasefire covering the entire front line that takes effect between 2026-11-16 and 2027-01-31. | True if the Kremlin and the Office of the President of Ukraine each announce a front-wide ceasefire taking effect between 2026-11-16 and 2027-01-31, reported by Reuters and AP. |
| KKR-20261114-24 | 68% | 2026-12-18 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 7.0 or greater anywhere in the world with an origin time between 2026-11-16 and 2026-12-15. | True if a USGS ComCat query returns at least one event of magnitude 7.0 or greater with origin time between 2026-11-16T00:00Z and 2026-12-15T23:59Z. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Bank of England Monetary Policy Committee raises Bank Rate above the level in force on 2026-11-14 at a scheduled announcement between 20" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5744 issued all-time across 23 forecaster arms · 4022 open (1721 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 397 issued · 383 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 198 | 198 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 215 | 198 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 220 | 218 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 205 | 172 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 397 | 383 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*