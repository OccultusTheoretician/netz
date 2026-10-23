**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 232056Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: manual/opus-5.5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-95 | 27% | 2026-10-30 | political | Luiz Inacio Lula da Silva wins re-election as president of Brazil, defeating Flavio Bolsonaro in the runoff held on 2026-10-25. | TSE official totals for the 2026-10-25 presidential runoff, as published on the TSE results site at the deadline, show Lula with more than 50 percent of valid votes. Flavio Bolsonaro above 50 percent resolves false. |
| KKR-20261023-96 | 75% | 2026-11-23 | cyber | CISA adds at least one PHP2Shell vulnerability, CVE-2026-109618 or CVE-2026-109619, to the Known Exploited Vulnerabilities catalog between 2026-10-23 and 2026-11-20. | The CISA KEV catalog JSON feed lists CVE-2026-109618 or CVE-2026-109619 with a dateAdded value between 2026-10-23 and 2026-11-20 inclusive. |
| KKR-20261023-97 | 60% | 2026-11-23 | military/conflict | Russian, Ukrainian and US government delegations hold a trilateral negotiating session, in Abu Dhabi or elsewhere, between 2026-11-01 and 2026-11-20. | True if at least two of the three governments, or both Reuters and AP, confirm that a session with Russian, Ukrainian and US delegations all present took place between 2026-11-01 and 2026-11-20. |
| KKR-20261023-98 | 55% | 2026-12-18 | military/conflict | US military forces strike at least one target on Iranian land territory between 2026-10-24 and 2026-12-15. | True if the White House, the Pentagon, or US Central Command acknowledges a US strike, alone or jointly with Israel, on a target on Iranian land territory carried out between 2026-10-24 and 2026-12-15. |
| KKR-20261023-99 | 28% | 2027-01-05 | economics/markets | The 10-year US Treasury constant-maturity yield is at or above 5.25 percent on 2026-12-31. Reference: 4.99 percent on the packet date. | FRED series DGS10 value for 2026-12-31 is 5.25 or higher. Reference: 4.99 percent on the packet date. If no value is posted for that date, use the last value posted before it. |
| KKR-20261023-100 | 15% | 2027-01-15 | economics/markets | The WTI Cushing spot crude price is at or above 120 dollars per barrel on 2026-12-31. Reference: 102.11 dollars per barrel on the packet date. | FRED series DCOILWTICO value for 2026-12-31 is 120.00 or higher. Reference: WTI 102.11 dollars on the packet date. If no value is posted for that date, use the last value posted before it. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The SNS-led list of Aleksandar Vucic wins more votes than the student-backed Student List in the Serbian parliamentary election held on 2026" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Jordanian authorities arrest or kill at least one of the gunmen who attacked a funeral at the Greek Orthodox church in Hamoud, Karak governo" → REJECTED: cited items name Jordan; the claim is about Greece — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Nigeria laboratory-confirms at least one additional Ebola case, beyond the Abuja index patient confirmed on 2026-10-20, between 2026-10-24 a" → REJECTED: resolution offers alternative VENUES joined by 'or' (…who disease outbreak news | or | situation…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "An earthquake of magnitude 6.0 or greater strikes within 200 km of the 2026-10-22 M7.0 Baqen County, Nagqu, Tibet epicenter between 2026-10-" → REJECTED: the resolution names a different subject than the statement — the claim is about Baqen, County, Nagqu, Tibet and the resolution settles on ComCat, USGS, us6000u43g. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

4812 issued all-time across 21 forecaster arms · 3460 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 251 issued · 240 open · 11 resolved · 5 hits / 6 misses · **Brier 0.362** against its own base rate 45.5% (climatological 0.248) · **skill -0.460** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1686 | 1303 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 104 | 103 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 105 | 105 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 113 | 106 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 242 | 155 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 420 | 339 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 251 | 240 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*