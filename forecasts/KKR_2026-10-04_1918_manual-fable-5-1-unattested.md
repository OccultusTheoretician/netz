**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041918Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-04_1517.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261004-18 | 42% | 2026-10-28 | political | Luiz Inacio Lula da Silva wins the 2026 Brazilian presidential election, either outright in the first round held on 2026-10-04 or in the runoff scheduled for 2026-10-25. | TRUE if official Superior Electoral Court results at resultados.tse.jus.br show Lula elected: over 50 percent of valid votes on 2026-10-04, or the most valid votes in the 2026-10-25 runoff. |
| KKR-20261004-19 | 23% | 2026-10-30 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding on 2026-10-28. Reference: target range of 3.75 to 4.00 percent on the packet date. | TRUE if the FOMC statement of 2026-10-28 lifts the target range upper limit above 4.00 percent, so that FRED series DFEDTARU reads above 4.00 on 2026-10-29. Reference: 4.00 percent on the packet date. |
| KKR-20261004-20 | 37% | 2026-11-03 | economics/markets | The ICE Brent December 2026 crude futures contract settles at or above 110.00 dollars per barrel on at least one trading day between 2026-10-05 and 2026-10-30. Reference: 102.25 dollars on the packet date. | TRUE if any daily ICE settlement of the Brent December 2026 contract between 2026-10-05 and 2026-10-30 is 110.00 dollars or higher. Reference: 102.25 dollars, the prior-session close on the packet date. |
| KKR-20261004-21 | 46% | 2026-12-08 | military/conflict | The United States carries out at least one air or missile strike on a target inside Iranian territory between 2026-10-05 and 2026-12-04. | TRUE if the White House, Pentagon or US Central Command confirms a US strike on a target inside Iran conducted between 2026-10-05 and 2026-12-04, and Reuters or AP reports that confirmation. |
| KKR-20261004-22 | 85% | 2026-10-28 | military/conflict | At least one further Russian drone or missile strike hits a road or rail bridge over the Dnipro inside Kyiv city between 2026-10-05 and 2026-10-25. | TRUE if Kyiv city authorities or the Ukrainian government confirm a Russian strike hitting any Dnipro bridge inside Kyiv between 2026-10-05 and 2026-10-25, and at least one of Reuters, AP or BBC reports it. |
| KKR-20261004-23 | 12% | 2026-11-18 | military/conflict | Houthi forces take control of the centre of Taiz city in Yemen from government forces between 2026-10-05 and 2026-11-15. | TRUE if at least two of Reuters, AP and AFP report that Houthi forces took control of Taiz city centre from Yemeni government forces at any time between 2026-10-05 and 2026-11-15. |
| KKR-20261004-24 | 20% | 2026-12-01 | cyber | US federal prosecutors make public criminal charges against at least one named person they describe as a member or associate of the ShinyHunters hacking group between 2026-10-05 and 2026-11-27. | TRUE if a justice.gov press release or unsealed US federal court filing dated between 2026-10-05 and 2026-11-27 charges a named defendant described by prosecutors as a ShinyHunters member or associate. |
| KKR-20261004-25 | 68% | 2026-11-04 | crime/security | Japanese prosecutors indict the US Marine arrested in Okinawa on 2026-10-04 on a charge of murder or robbery resulting in death between 2026-10-05 and 2026-10-30. | TRUE if the Naha District Public Prosecutors Office indicts the arrested Marine for murder or robbery-murder between 2026-10-05 and 2026-10-30, as reported by Kyodo, NHK, AP or Stars and Stripes. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Democrats and independents who caucus with them win enough seats in the US Senate elections of 2026-11-03, including any runoff held through" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The USGS catalog records at least one earthquake of magnitude 6.5 or greater in the Indonesia region, defined as latitude -11 to 6 and longi" → REJECTED: the resolution names a different subject than the statement — the claim is about Indonesia, USGS and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3347 issued all-time across 18 forecaster arms · 2805 open (502 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 258 issued · 241 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1193 | 1076 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 376 | 226 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 175 | 170 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 258 | 241 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 78 | 78 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*