**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 032113Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-03_1517.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261003-27 | 57% | 2026-10-20 | military/conflict | Between 2026-10-04 and 2026-10-17, a Russian drone or missile strike damages at least one Kyiv Dnipro road bridge other than Pivdennyi and Pivnichnyi, namely the Paton, Metro, Darnytskyi or Podilskyi bridge. | TRUE if Reuters, AP or BBC, citing Kyiv city authorities, report a Russian strike damaging the Paton, Metro, Darnytskyi or Podilskyi bridge between 2026-10-04 and 2026-10-17; otherwise FALSE. |
| KKR-20261003-28 | 65% | 2026-10-28 | military/conflict | Between 2026-10-04 and 2026-10-25, Ethiopian federal forces or the allied Tigray Peace Force take control of Mekelle city itself, not only its Alula Aba Nega airport. | TRUE if AP, Reuters or BBC report between 2026-10-04 and 2026-10-25 that Ethiopian federal forces or the Tigray Peace Force control Mekelle city, beyond the airport; otherwise FALSE. |
| KKR-20261003-29 | 48% | 2026-10-28 | political | Luiz Inacio Lula da Silva is elected president of Brazil, either outright in the 2026-10-04 first round or in the scheduled 2026-10-25 runoff. | TRUE if official TSE results show Lula above 50 percent of valid votes on 2026-10-04 or winning the 2026-10-25 runoff; any other outcome is FALSE. |
| KKR-20261003-30 | 10% | 2026-11-10 | political | In the scheduled 2026-10-27 Knesset election, Likud, Shas, United Torah Judaism, Otzma Yehudit and Religious Zionism-Zehut together win 61 or more of the 120 seats. | TRUE if Central Elections Committee official final results for the 2026-10-27 election give Likud, Shas, United Torah Judaism, Otzma Yehudit and Religious Zionism-Zehut a combined 61 or more seats; otherwise FALSE. |
| KKR-20261003-31 | 52% | 2026-11-17 | economics/markets | The ICE Brent front-month futures contract settles below 100.00 USD per barrel on 2026-11-13. Reference: 102.25 on the packet date. | TRUE if the ICE Futures Europe Brent front-month settlement price for 2026-11-13 is below 100.00 USD per barrel; 100.00 or higher is FALSE. Reference: 102.25 on the packet date. |
| KKR-20261003-32 | 33% | 2026-12-03 | disaster | Between 2026-10-04 and 2026-11-30, the National Hurricane Center classifies at least one Atlantic-basin tropical cyclone as a hurricane. | TRUE if an NHC advisory issued between 2026-10-04 and 2026-11-30 UTC assigns hurricane intensity, sustained winds of 64 knots or more, to any Atlantic-basin cyclone; otherwise FALSE. |
| KKR-20261003-33 | 6% | 2027-02-02 | cyber | Between 2026-10-04 and 2027-01-29, CISA adds at least one of the six newly patched Dell Container Storage Modules vulnerabilities, including CVSS 10.0 CVE-2026-63688 and CVE-2026-63692, to the KEV catalog. | TRUE if the CISA KEV catalog lists a dateAdded between 2026-10-04 and 2027-01-29 for CVE-2026-63688, CVE-2026-63692, CVE-2026-54472, CVE-2026-61421, CVE-2026-67269 or CVE-2026-67273; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At its scheduled 2026-10-27 to 2026-10-28 meeting, the FOMC raises the federal funds target range above 3.75 to 4.00 percent. Reference: 3.7" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-10-30) is 1 day(s) after the window closes (2026-10-29). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "Between 2026-10-04 and 2026-12-31, a royal decree dissolving the Cortes Generales and calling an early Spanish general election is published" → REJECTED: the resolution names a different subject than the statement — the claim is about Boletin, Cortes, Estado, Generales and the resolution settles on BOE, Congress, Deputies, Senate. A row whose resolution checks a different fact can be scored correct while being wrong
- "Between 2026-10-04 and 2026-12-31, at least one person arrested over the 2026-09-27 RAF Fairford incident is charged with a criminal offence" → REJECTED: cited items name Iran, Islamic Republic of; the claim is about United Kingdom — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3303 issued all-time across 18 forecaster arms · 2761 open (497 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 78 issued · 78 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1180 | 1063 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 368 | 218 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 166 | 161 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 250 | 233 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 78 | 78 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*