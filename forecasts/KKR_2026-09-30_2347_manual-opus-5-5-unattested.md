**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 302347Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-30_1517.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260930-27 | 42% | 2026-11-03 | military/conflict | Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack at least once between 2026-10-01 and 2026-10-31. | True if a Ukrainian Air Force daily report, as carried by Reuters or AP, records 500 or more drones and missiles combined launched in one overnight attack between 2026-10-01 and 2026-10-31; otherwise false. |
| KKR-20260930-28 | 44% | 2026-12-03 | military/conflict | US forces strike at least one land target inside Iran, including Iranian islands, between 2026-10-01 and 2026-11-30. | True if CENTCOM or the Pentagon confirms, or Reuters and AP both report citing US officials, a US strike on a land target in Iran between 2026-10-01 and 2026-11-30. Strikes on vessels at sea do not count. |
| KKR-20260930-29 | 82% | 2026-12-03 | military/conflict | North Korea launches at least one ballistic missile between 2026-10-01 and 2026-11-30. | True if the South Korean Joint Chiefs of Staff or the Japanese Ministry of Defense reports a North Korean ballistic missile launch, suspected ballistic included, occurring between 2026-10-01 and 2026-11-30; otherwise false. |
| KKR-20260930-30 | 63% | 2026-10-30 | economics/markets | The FOMC holds the federal funds target range at 3.75 to 4.00 percent at its meeting concluding 2026-10-28. | True if FRED series DFEDTARU reads 4.00 for 2026-10-29, reflecting the 2026-10-28 decision; any other value is false. Reference: 4.00 percent upper bound held at seal on 2026-09-30. |
| KKR-20260930-31 | 30% | 2026-11-03 | economics/markets | The 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date. | True if FRED series DGS10 shows 5.50 or higher for any date between 2026-10-01 and 2026-10-30; otherwise false. Reference: 5.27 percent on 2026-09-30 per the packet market snapshot. |
| KKR-20260930-32 | 45% | 2026-12-02 | cyber | CISA adds at least one more Citrix NetScaler vulnerability to its Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-11-30. | True if the CISA KEV catalog carries an entry with vendorProject Citrix and a NetScaler product whose dateAdded falls between 2026-10-01 and 2026-11-30; otherwise false. |
| KKR-20260930-33 | 50% | 2027-01-05 | crime/security | Law enforcement arrests or charges at least one person identified as a ShinyHunters member or associate, other than the suspect arrested in the Netherlands on 2026-09-15, between 2026-10-01 and 2026-12-31. | True if DOJ, FBI, Europol or a national police force announces, or a court filing shows, an arrest or charge of a ShinyHunters-linked person other than the 2026-09-15 Dutch arrestee between 2026-10-01 and 2026-12-31. |
| KKR-20260930-34 | 12% | 2027-03-29 | crime/security | The Crown Prosecution Service authorises criminal charges against at least one individual or organisation over the Grenfell Tower fire between 2026-10-01 and 2027-03-26. | True if a CPS or Metropolitan Police statement announces criminal charges authorised against any individual or organisation over the Grenfell Tower fire between 2026-10-01 and 2027-03-26; otherwise false. |
| KKR-20260930-35 | 40% | 2026-11-02 | political | The Spanish Congress of Deputies validates Royal Decree-law 26/2026 on housing and eviction protection in a plenary vote held between 2026-10-02 and 2026-10-29. | True if the Congress of Deputies votes to convalidate Royal Decree-law 26/2026 between 2026-10-02 and 2026-10-29, per the Congress voting record or BOE convalidation notice; false if derogated or never voted. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Iranian parliament passes a bill mandating withdrawal from the Nuclear Non-Proliferation Treaty in an open-session vote between 2026-10-" → REJECTED: the resolution names a different subject than the statement — the claim is about Iranian, Non, Nuclear, Proliferation and the resolution settles on AP, IRNA, Majlis, Mehr. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3132 issued all-time across 18 forecaster arms · 2590 open (298 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 57 issued · 57 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1114 | 997 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 345 | 195 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 148 | 143 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 232 | 215 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*