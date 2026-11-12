**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121804Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-12_1613.md · forecaster: manual/fable-5.2/unattested · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261112-48 | 55% | 2026-12-15 | political | Official Russian and Ukrainian delegations meet in person for at least one further US-mediated negotiating session held between 2026-11-16 and 2026-12-11. | Reuters and AP both report that Russian and Ukrainian government delegations met in person with US mediators present on a date between 2026-11-16 and 2026-12-11. |
| KKR-20261112-49 | 20% | 2026-12-22 | economics/markets | The 10-year Treasury constant maturity yield is at or above 5.25 percent on 2026-12-18. Reference: 5.07 percent on the packet date 2026-11-12. | FRED series DGS10 shows a value at or above 5.25 for 2026-12-18. Reference level at seal: 5.07 percent in the packet market snapshot of 2026-11-12. |
| KKR-20261112-50 | 28% | 2027-01-04 | cyber | CISA adds at least one Citrix vulnerability to its Known Exploited Vulnerabilities catalog between 2026-11-13 and 2026-12-31. | The CISA KEV catalog JSON carries at least one entry with vendorProject Citrix and a dateAdded value between 2026-11-13 and 2026-12-31. |
| KKR-20261112-51 | 15% | 2027-01-12 | cyber | CISA adds the Windows privilege escalation flaw publicly known as SignDrop to its Known Exploited Vulnerabilities catalog between 2026-11-13 and 2027-01-08. | The CISA KEV catalog carries a dateAdded value between 2026-11-13 and 2027-01-08 for the CVE that Microsoft or BleepingComputer identifies as the SignDrop flaw. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US forces carry out at least one kinetic strike on a target on Iranian land territory between 2026-11-13 and 2026-12-11." → REJECTED: resolution offers alternative VENUES joined by 'or' (…uters and ap both report, citing us officials | or | a pentagon  centcom statement, a us strike on…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Indonesian MPR (the national consultative assembly) votes to elect a new vice president, filling the vacancy left by the resignation rep" → REJECTED: resolution offers alternative VENUES joined by 'or' (…antara and at least one of reuters | or | ap report that the mpr elected a vice preside…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The FOMC statement issued at the scheduled meeting concluding 2026-12-09 raises the federal funds target range above the range in effect on " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Nvidia files a Form 8-K between 2026-11-13 and 2027-03-31 reporting the appointment of a chief executive officer who is not designated inter" → REJECTED: statement and resolution assert opposite directions - the statement claims an absence and the resolution resolves TRUE on the event occurring. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition
- "Administrators are formally appointed over Poundland Limited between 2026-11-13 and 2026-12-11." → REJECTED: resolution offers alternative VENUES joined by 'or' (…gazette | or | the companies house…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one of the two Iranian men convicted in a UK court of spying on journalists for Iran, verdicts reported 2026-11-12, receives a cust" → REJECTED: the resolution names a different subject than the statement — the claim is about Iran, Iranian, UK and the resolution settles on CPS, Counter, Policing, Terrorism. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

5699 issued all-time across 23 forecaster arms · 3977 open (1628 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.2/unattested`:** 16 issued · 16 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 194 | 194 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 207 | 190 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 212 | 210 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 189 | 156 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 388 | 374 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*