**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201958Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-20_1517.md · forecaster: manual/opus-5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260920-26 | 88% | 2026-11-04 | military_conflict | Russian authorities report drone interceptions over Moscow city or Moscow oblast on at least three separate calendar days between 2026-09-27 and 2026-10-31. | TRUE if drone interception over Moscow city or oblast is reported on three or more distinct dates between 2026-09-27 and 2026-10-31 by a Russian official source and carried by at least one Ukrainian or Western outlet. |
| KKR-20260920-27 | 41% | 2026-11-19 | military_conflict | At least one commercial vessel transiting or near the Strait of Hormuz is struck or seized by Iranian or Iran-aligned forces between 2026-09-27 and 2026-11-15. | TRUE if UKMTO logs an incident of a merchant vessel struck or seized in or near the Strait of Hormuz dated inside the window and at least one major wire service attributes it to Iranian or Iran-aligned forces. |
| KKR-20260920-28 | 37% | 2026-11-17 | economic | Front-month Brent crude settles at or above 110.00 USD per barrel on at least one trading day between 2026-09-28 and 2026-11-13. Reference: 99.29 on the packet date 2026-09-20. | TRUE if the ICE Brent front-month official settlement equals or exceeds 110.00 USD on any trading day from 2026-09-28 through 2026-11-13. Reference level 99.29 at seal. |
| KKR-20260920-29 | 48% | 2026-12-22 | economic | The US 10-year Treasury constant maturity yield prints at or above 5.25 percent on at least one business day between 2026-09-28 and 2026-12-18. Reference: 5.00 percent on the packet date 2026-09-20. | TRUE if the FRED series DGS10 carries a value of 5.25 or higher on any date from 2026-09-28 through 2026-12-18. Reference level 5.00 at seal. |
| KKR-20260920-30 | 13% | 2026-12-15 | cyber | CISA adds at least one vulnerability in an npm-distributed or Node.js ecosystem component to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-28 and 2026-12-11. | TRUE if the CISA KEV JSON feed contains an entry whose dateAdded falls inside the window and whose vendorProject or product identifies an npm package, the npm registry, or Node.js itself. |
| KKR-20260920-31 | 85% | 2026-12-22 | political | The UN General Assembly adopts a resolution appointing the tenth Secretary-General between 2026-09-27 and 2026-12-18. | TRUE if a General Assembly resolution appointing a Secretary-General for the term beginning 2027-01-01 is adopted on a date inside the window and issued in the official UN documents record. |
| KKR-20260920-32 | 10% | 2027-01-05 | political | Friedrich Merz ceases to hold the office of German Federal Chancellor between 2026-09-21 and 2026-12-31. | TRUE if a successor is sworn in as Federal Chancellor, or Merz formally resigns with effect inside the window, as recorded by the Bundesregierung and reported by at least two major German outlets. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The USGS earthquake catalog records at least one earthquake of magnitude 8.0 or greater, anywhere on Earth, with origin time between 2026-09" → REJECTED: the resolution names a different subject than the statement — the claim is about Earth, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "The USGS earthquake catalog records three or more earthquakes of magnitude 7.0 or greater, anywhere on Earth, with origin times between 2026" → REJECTED: the resolution names a different subject than the statement — the claim is about Earth, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "The sister of former Pakistani prime minister Imran Khan detained on 2026-09-20 is released from custody or granted bail, with release takin" → REJECTED: the resolution names a different subject than the statement — the claim is about Imran, Khan, Pakistani and the resolution settles on Dawn, Geo, Jazeera, News. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2578 issued all-time across 16 forecaster arms · 2112 open (164 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 306 issued · 289 open · 7 resolved · 5 hits / 2 misses · **Brier 0.137** against its own base rate 71.4% (climatological 0.204) · **skill +0.329** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 882 | 797 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 309 | 159 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 96 | 91 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 147 | 137 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 306 | 289 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 277 | 229 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*