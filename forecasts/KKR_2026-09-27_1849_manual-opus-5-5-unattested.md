**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271849Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-27_1517.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260927-28 | 76% | 2026-10-05 | crime/security | The State of Tennessee carries out the scheduled execution of Christa Pike between 2026-09-30 and 2026-10-02. | TRUE if the Tennessee Department of Correction, or AP or Reuters citing it, confirms Pike was executed on a date between 2026-09-30 and 2026-10-02; FALSE on clemency, stay, reprieve, or postponement past 2026-10-02. |
| KKR-20260927-29 | 75% | 2026-10-19 | cyber | CISA adds at least one new Citrix NetScaler ADC or Gateway CVE to the KEV catalog between 2026-09-28 and 2026-10-16. | TRUE if the CISA KEV JSON feed carries an entry with vendorProject Citrix, product naming NetScaler, a CVE other than CVE-2026-19490 or CVE-2026-19489, and dateAdded between 2026-09-28 and 2026-10-16. |
| KKR-20260927-30 | 25% | 2026-11-18 | economics/markets | The Brent spot price is below 90.00 USD per barrel on 2026-11-13. Reference: Brent 97.44 on the packet date. | TRUE if FRED series DCOILBRENTEU (EIA Europe Brent spot FOB) prints a value below 90.00 for 2026-11-13; FALSE if 90.00 or above. |
| KKR-20260927-31 | 12% | 2026-11-05 | political | The United States and Iran both publicly confirm a ceasefire or agreement providing for reopening of the Strait of Hormuz between 2026-09-28 and 2026-11-02. | TRUE if the White House or State Department and the Iranian foreign ministry each confirm an agreed ceasefire or Hormuz reopening deal between 2026-09-28 and 2026-11-02, reported by both Reuters and AP. |
| KKR-20260927-32 | 38% | 2026-12-18 | military/conflict | US forces conduct at least one strike on Iranian land territory between 2026-11-04 and 2026-12-15. | TRUE if the Pentagon, CENTCOM, or the White House acknowledges a US strike on a target on Iranian land territory occurring between 2026-11-04 and 2026-12-15, reported by Reuters or AP. |
| KKR-20260927-33 | 72% | 2026-10-07 | political | Luiz Inacio Lula da Silva finishes first in valid votes in the first round of the Brazilian presidential election on 2026-10-04. | TRUE if final first-round results published by the Tribunal Superior Eleitoral show Lula with more valid votes than any other presidential candidate; FALSE otherwise. |
| KKR-20260927-34 | 52% | 2026-12-15 | political | Amy Acton defeats Vivek Ramaswamy in the Ohio gubernatorial election held 2026-11-03. | TRUE if official results published by the Ohio Secretary of State show Acton receiving more votes than Ramaswamy for governor; FALSE if Ramaswamy receives more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one of the five men arrested near RAF Fairford on 2026-09-27 is criminally charged between 2026-09-27 and 2026-10-11." → REJECTED: the resolution names a different subject than the statement — the claim is about Fairford, RAF and the resolution settles on Counter, Crown, Policing, Prosecution. A row whose resolution checks a different fact can be scored correct while being wrong
- "The FOMC raises the federal funds target range by 25 basis points to 4.00-4.25 percent at its scheduled 2026-10-28 decision. Reference: rang" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "An earthquake of magnitude 6.0 or greater occurs within 150 km of the 2026-09-26 M6.6 New Caledonia epicenter between 2026-09-28 and 2026-10" → REJECTED: the resolution names a different subject than the statement — the claim is about Caledonia, New and the resolution settles on ComCat, USGS, us6000txpi. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

2965 issued all-time across 17 forecaster arms · 2423 open (226 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 34 issued · 34 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1049 | 932 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 129 | 124 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 210 | 193 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 327 | 263 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*