**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 132338Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-13_1712.md · forecaster: manual/fable-5/unattested · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260913-40 | 30% | 2027-01-05 | economics/markets | ICE Brent crude front-month futures settle at or above 125.00 USD per barrel on at least one trading day between 2026-09-14 and 2026-12-31. Reference: 104.61 at packet seal. | Official ICE daily settlement prices show at least one front-month Brent settlement at or above 125.00 USD within the window. |
| KKR-20260913-41 | 15% | 2026-11-17 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for a vulnerability in any Tencent product with dateAdded between 2026-09-14 and 2026-11-13. | The public CISA KEV JSON feed contains an entry whose vendorProject or product field names Tencent with a dateAdded value inside the window. |
| KKR-20260913-42 | 70% | 2026-12-04 | political | Democratic candidates win a majority of seats, at least 218, in the US House of Representatives in the midterm elections held 2026-11-03. | AP race calls or certified results available by the deadline show Democratic candidates winning 218 or more House seats in the 2026 general election. |
| KKR-20260913-43 | 35% | 2027-01-04 | political | A new Swedish government wins its Riksdag confirmation vote with the Sweden Democrats holding at least one cabinet ministry, formation occurring between 2026-09-14 and 2026-12-31. | Riksdag or regeringen.se records show a government approved within the window whose cabinet list includes at least one Sweden Democrat minister; support-party status without a ministry resolves false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US Central Command publicly announces at least one US military strike on Houthi targets in Yemen conducted between 2026-09-14 and 2026-10-14" → REJECTED: resolution offers alternative VENUES joined by 'or' (…centcom press release | or | official centcom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "NATO confirms that one or more member states requested consultations under Article 4 of the North Atlantic Treaty between 2026-09-14 and 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…an official nato statement | or | press release confirms an article 4 consultat…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The US 10-year Treasury constant-maturity yield, FRED series DGS10, prints at or above 5.25 percent on at least one business day between 202" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A federal statute authorizing one-time direct payments of at least 5000 dollars per eligible individual is signed into law between 2026-09-1" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "USGS catalogs at least one earthquake of magnitude 5.0 or greater with epicenter within 200 km of the 2026-09-12 M6.5 event near Teluknaga, " → REJECTED: the resolution names a different subject than the statement — the claim is about Indonesia, Teluknaga, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "The person arrested for the 2026-09-13 Louisiana stabbing spree is indicted by a grand jury on at least one count of first- or second-degree" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2055 issued all-time across 16 forecaster arms · 1719 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 222 issued · 219 open · 3 resolved · 3 hits / 0 misses · **Brier 0.153** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 665 | 627 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 90 | 90 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 230 | 224 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 226 | 194 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*