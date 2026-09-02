**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 020009Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-01_1518.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-09 | 35% | 2026-10-13 | economics_markets | The front-month ICE Brent crude futures contract settles at or above 100.00 US dollars per barrel on at least one trading day between 2026-09-08 and 2026-10-09. Reference: Brent 92.47 at seal on 2026-09-01. | ICE published front-month Brent settlement data shows a settlement at or above 100.00 USD per barrel on at least one trading day from 2026-09-08 through 2026-10-09; reference 92.47 at seal. |
| KKR-20260902-10 | 40% | 2026-11-03 | economics_markets | The US 10-year Treasury constant maturity yield reaches 5.00 percent or higher on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.77 percent at seal on 2026-09-01. | FRED series DGS10 carries a daily observation at or above 5.00 for at least one business day from 2026-09-08 through 2026-10-30; reference 4.77 at seal. |
| KKR-20260902-11 | 22% | 2026-10-30 | economics_markets | The FOMC raises the federal funds target range at the meeting concluding 2026-09-16 or the meeting concluding 2026-10-28. Reference: target range 3.50 to 3.75 percent in effect at seal on 2026-09-01. | The FOMC implementation note for 2026-09-16 or for 2026-10-28 sets a target range whose upper bound exceeds 3.75 percent; reference 3.50 to 3.75 at seal. |
| KKR-20260902-12 | 25% | 2026-12-04 | political | Donald Trump and Vladimir Putin hold an in-person meeting on a date between 2026-09-08 and 2026-11-30. | The White House and the Kremlin each confirm an in-person Trump-Putin meeting held inside the window, and AP or Reuters reports from the venue. |
| KKR-20260902-13 | 50% | 2026-10-13 | military_conflict | A commercial vessel is struck by weapons fire in the Strait of Hormuz or the Gulf of Oman between 2026-09-08 and 2026-10-08. | UKMTO issues an incident advisory for a commercial vessel struck in the Strait of Hormuz or Gulf of Oman inside the window, and Reuters reports the same incident. |
| KKR-20260902-14 | 60% | 2026-12-22 | crime_security | Duane Davis is sentenced in the Eighth Judicial District Court of Clark County, Nevada on a date between 2026-09-08 and 2026-12-18. | The Eighth Judicial District Court docket records a judgment of conviction with a sentence imposed on Duane Davis on a date inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds at least one CVE naming Microsoft Exchange Server to the Known Exploited Vulnerabilities catalog with a date-added value between 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…entry whose vendorproject | or | product field names microsoft…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A single cryptocurrency protocol or exchange exploit causes losses of at least 100 million US dollars, occurring between 2026-09-08 and 2026" → REJECTED: the resolution names only a venue or register (chainalysis, defillama, elliptic, hacks) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A lapse in US federal appropriations affecting at least one Cabinet department is in effect on at least one calendar day between 2026-10-01 " → REJECTED: the resolution names a different subject than the statement — the claim is about Cabinet and the resolution settles on AP, OMB, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "The official confirmed death toll for the 2026 Nepal monsoon flood event reaches 1,400 or more between 2026-09-08 and 2026-10-16. Reference:" → REJECTED: resolution offers alternative VENUES joined by 'or' (…nepal ndrrma | or | un ocha…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1253 issued all-time across 14 forecaster arms · 1092 open (109 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 159 issued · 156 open · 3 resolved · 1 hits / 2 misses · **Brier 0.141** against its own base rate 33.3% (climatological 0.222) · **skill +0.366** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 323 | 306 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 184 | 153 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 138 | 137 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 159 | 156 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 146 | 138 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*