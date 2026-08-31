**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-30_1516.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-47 | 33% | 2026-12-04 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry for a WordPress plugin or theme vulnerability with a dateAdded value between 2026-08-31 and 2026-11-30. | TRUE if a fetch of the CISA KEV JSON feed on the deadline shows any entry whose product or name field identifies a WordPress plugin or theme and whose dateAdded falls between 2026-08-31 and 2026-11-30. |
| KKR-20260831-48 | 25% | 2027-01-06 | economics/markets | The S&P 500 index records an official daily close below 7000.00 on at least one trading day between 2026-09-01 and 2026-12-31. | TRUE if official S&P Dow Jones Indices closing values show any daily close strictly below 7000.00 for a trading date between 2026-09-01 and 2026-12-31. |
| KKR-20260831-49 | 25% | 2027-01-08 | economics/markets | The Federal Register publishes at least one presidential proclamation or executive order modifying United States tariff treatment of Canadian-origin goods with a publication date between 2026-09-01 and 2026-12-31. | TRUE if a federalregister.gov search returns a presidential document published between 2026-09-01 and 2026-12-31 that modifies tariff rates, coverage, or refunds applying to goods of Canadian origin. |
| KKR-20260831-50 | 44% | 2026-12-04 | political | Between 2026-08-31 and 2026-11-30, the head of state of Niger is removed, replaced, or announces resignation, or a new military takeover of the government is completed. | TRUE if at least two of Reuters, AFP, BBC, Al Jazeera, or RFI report a completed change of head of state or completed military takeover in Niger occurring between 2026-08-31 and 2026-11-30. |
| KKR-20260831-51 | 53% | 2026-12-04 | military/conflict | Between 2026-08-31 and 2026-11-30, a commercial vessel transiting or anchored in the Strait of Hormuz or its approaches is struck by weapons fire or seized. | TRUE if UKMTO issues an incident advisory, or at least two of Reuters, AP, or AFP report a strike on or seizure of a commercial vessel in the Strait of Hormuz area between 2026-08-31 and 2026-11-30. |
| KKR-20260831-52 | 53% | 2026-10-05 | military/conflict | Between 2026-09-01 and 2026-09-30, at least one Russian missile or drone strike inside Ukraine kills 10 or more people in a single attack, per official Ukrainian figures. | TRUE if at least two of Reuters, AP, AFP, or BBC report an official Ukrainian death toll of 10 or more from a single Russian strike occurring between 2026-09-01 and 2026-09-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-31 and 2026-10-16, Manchester Airports Group or a UK government body publicly confirms unauthorized access to MAG systems in" → REJECTED: resolution offers alternative VENUES joined by 'or' (…, or the record report an official mag, ncsc, | or | ico statement confirming unauthorized access …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The NYMEX WTI crude front-month contract records an official daily settlement price above 95.00 USD on at least one trading day between 2026" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-31 and 2027-01-29, the Crown Prosecution Service publicly announces a charging decision, to charge or not to charge, concern" → REJECTED: resolution offers alternative VENUES joined by 'or' (…a cps statement | or | at least two of bbc, guardian, reuters, or pa…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about Crown, Prosecution, Service and the resolution settles on BBC, CPS, Guardian, Media. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-08-31 and 2026-10-30, the reported confirmed combined death toll for the August 2026 Nepal and Tibet floods reaches or exceeds " → REJECTED: the resolution names only a venue or register (AFP, Guardian, Jazeera, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1175 issued all-time across 14 forecaster arms · 1014 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 303 issued · 286 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 303 | 286 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 120 | 119 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 142 | 139 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 130 | 122 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*