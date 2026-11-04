**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041719Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-04_1615.md · forecaster: manual/opus-5.5/unattested · 3 accepted / 7 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261104-28 | 64% | 2026-11-13 | political | The ANC finishes below 35.0 percent of the national vote in the South African local government elections held on 2026-11-04, per IEC results declared between 2026-11-05 and 2026-11-11. | TRUE if IEC final results declared between 2026-11-05 and 2026-11-11 show the ANC below 35.0 percent of the national valid vote; FALSE at 35.0 or above. |
| KKR-20261104-29 | 52% | 2027-02-01 | cyber | CISA adds at least one SonicWall vulnerability to the KEV catalog between 2026-11-05 and 2027-01-29. | TRUE if the CISA KEV catalog carries a date-added value between 2026-11-05 and 2027-01-29 for at least one entry with vendor SonicWall. |
| KKR-20261104-30 | 45% | 2027-02-01 | crime/security | The UK Supreme Court hands down judgment in the Ammori appeal against the proscription of Palestine Action between 2026-11-06 and 2027-01-29. | TRUE if the UK Supreme Court case page for UKSC/2026/0099 records a judgment handed down between 2026-11-06 and 2027-01-29, whichever side prevails. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Jim Jordan wins the House Republican Conference vote for party leader in the 120th Congress between 2026-11-09 and 2026-11-20." → REJECTED: resolution offers alternative VENUES joined by 'or' (…eld between 2026-11-09 and 2026-11-20, per ap | or | reuters…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Knesset approves a new Israeli government in a confidence vote between 2026-11-05 and 2027-01-29." → REJECTED: resolution offers alternative VENUES joined by 'or' (…11-05 and 2027-01-29, per the knesset website | or | reuters…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The FOMC raises the federal funds target range to at least 4.00-4.25 percent on 2026-12-09. Reference: 3.75-4.00 percent target range on the" → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-12-11) is 1 day(s) after the window closes (2026-12-10). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "ICE Brent front-month futures settle at or above 110.00 dollars per barrel on at least one trading day between 2026-11-05 and 2026-12-31. Re" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Congress enacts a law raising or suspending the federal debt limit between 2026-11-05 and 2027-01-02, before the new Democratic majorities t" → REJECTED: the resolution names a different subject than the statement — the claim is about Congress, Democratic and the resolution settles on Congress, USC. A row whose resolution checks a different fact can be scored correct while being wrong
- "US forces strike Iranian land or island territory at least once between 2026-11-05 and 2026-11-30, with the strike acknowledged on the recor" → REJECTED: resolution offers alternative VENUES joined by 'or' (…etween 2026-11-05 and 2026-11-30, per reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Russia and Ukraine both confirm a new truce, nationwide or covering energy infrastructure, the Black Sea or a named city, taking effect betw" → REJECTED: resolution offers alternative VENUES joined by 'or' (…reuters | or | ap reports the kremlin and kyiv both confirme…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5332 issued all-time across 22 forecaster arms · 3610 open (1018 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 337 issued · 323 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 72 | 72 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 168 | 151 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 169 | 167 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 149 | 116 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 479 | 364 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 337 | 323 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*