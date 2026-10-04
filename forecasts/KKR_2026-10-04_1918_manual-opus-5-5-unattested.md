**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041918Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-04_1517.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261004-34 | 62% | 2026-10-28 | military/conflict | Between 2026-10-05 and 2026-10-25, Russia launches at least 500 drones and missiles combined at Ukraine in a single attack period covered by one Ukrainian Air Force summary. | TRUE if any Ukrainian Air Force summary for an attack period between 2026-10-05 and 2026-10-25, as carried by Reuters, AP or Kyiv Independent, totals 500 or more drones and missiles launched; otherwise FALSE. |
| KKR-20261004-35 | 22% | 2026-12-03 | military/conflict | Between 2026-10-05 and 2026-11-30, the US and Iranian governments both publicly confirm a ceasefire, memorandum or deal under which Iran commits to reopen the Strait of Hormuz to commercial shipping. | TRUE if, between 2026-10-05 and 2026-11-30, both the US government and the Iranian government publicly confirm an agreement committing Iran to reopen Hormuz to commercial shipping, as reported by Reuters or AP; otherwise FALSE. |
| KKR-20261004-36 | 10% | 2027-01-04 | military/conflict | Between 2026-10-05 and 2026-12-31, Yemeni government or government-aligned forces retake control of the Red Sea port city of Mocha in Taiz governorate from Houthi forces. | TRUE if Reuters or AP report as fact, between 2026-10-05 and 2026-12-31, that Yemeni government or government-aligned forces have taken control of Mocha city from the Houthis; otherwise FALSE. |
| KKR-20261004-37 | 18% | 2026-10-30 | economics/markets | At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range above 3.75 to 4.00 percent (Reference: upper bound 4.00 percent on the packet date). | TRUE if the FOMC statement issued on 2026-10-28 sets the federal funds target range upper bound above 4.00 percent, per federalreserve.gov or FRED series DFEDTARU; otherwise FALSE. Reference: 4.00 percent at seal. |
| KKR-20261004-38 | 38% | 2026-12-02 | economics/markets | Between 2026-10-05 and 2026-11-30, the ICE Brent front-month futures contract settles at or below 90.00 USD per barrel on at least one trading day (Reference: 102.25 USD, the 2026-10-02 settlement held at seal on the packet date). | TRUE if any ICE Futures Europe front-month Brent daily settlement price dated between 2026-10-05 and 2026-11-30 is 90.00 USD or lower; otherwise FALSE. Reference: 102.25 USD at seal. |
| KKR-20261004-39 | 55% | 2026-10-28 | political | Flavio Bolsonaro is elected President of Brazil in the 2026 election, decided either in the first round on 2026-10-04 or in the runoff scheduled for 2026-10-25. | TRUE if official TSE results show Flavio Bolsonaro winning more than 50 percent of valid votes in the 2026-10-04 first round or in the 2026-10-25 runoff; otherwise FALSE. |
| KKR-20261004-40 | 40% | 2026-11-10 | political | In the Knesset election held on 2026-10-27, Likud wins strictly more seats than any other single list. | TRUE if final official results of the 2026-10-27 Knesset election published by the Israeli Central Elections Committee give Likud more seats than every other list; a tie for first is FALSE. |
| KKR-20261004-41 | 80% | 2026-11-23 | crime/security | Between 2026-10-05 and 2026-11-20, Japanese prosecutors indict the US Marine arrested by Okinawa police over the killing of a woman at a Naha hotel, on any charge connected to her death or robbery. | TRUE if Kyodo, NHK or The Japan Times report the Naha District Public Prosecutors Office indicted the Marine on any charge connected to the death or robbery of the woman between 2026-10-05 and 2026-11-20; otherwise FALSE. |
| KKR-20261004-42 | 40% | 2027-01-04 | cyber | Between 2026-10-05 and 2026-12-31, the US Department of Justice publicly announces or unseals federal criminal charges against at least one person identified as a member of the ShinyHunters hacking group. | TRUE if, between 2026-10-05 and 2026-12-31, DOJ announces on justice.gov or unseals in federal court charges against a defendant that DOJ, the FBI, Reuters or AP identify as a ShinyHunters member; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-05 and 2026-12-31, the Spanish government publishes a royal decree in the Boletin Oficial del Estado dissolving the Cortes G" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3364 issued all-time across 18 forecaster arms · 2822 open (502 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 87 issued · 87 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1201 | 1084 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*