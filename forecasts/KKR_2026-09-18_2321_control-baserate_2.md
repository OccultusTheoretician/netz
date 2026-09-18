**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182321Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-18_1518.md · forecaster: control/baserate · 10 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260918-36 | 29% | 2026-11-23 | cyber | CISA adds Check Point CVE-2026-91843, the pre-authentication root code-execution flaw in Security Management Server and Log Server, to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-19 and 2026-11-20. | TRUE if the CISA KEV catalog JSON lists CVE-2026-91843 with a dateAdded value between 2026-09-19 and 2026-11-20 inclusive; FALSE otherwise. |
| KKR-20260918-37 | 29% | 2026-11-23 | cyber | CISA adds at least one further Linux Kernel vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-21 and 2026-11-20, continuing the kernel additions logged on 2026-09-18. | TRUE if the CISA KEV catalog JSON lists at least one entry with vendorProject Linux and product Kernel whose dateAdded falls between 2026-09-21 and 2026-11-20 inclusive. |
| KKR-20260918-38 | 24% | 2026-11-24 | economics/markets | The 10-year US Treasury constant-maturity yield prints at or above 5.25 percent on at least one trading day between 2026-09-21 and 2026-11-20. Reference: 5.00 percent on the packet date. | TRUE if FRED series DGS10 shows a daily value of 5.25 or higher on any date from 2026-09-21 through 2026-11-20. Reference: 5.00 percent on the packet date. |
| KKR-20260918-39 | 24% | 2026-11-30 | economics/markets | WTI crude at Cushing prints at or below 85.00 USD per barrel on at least one trading day between 2026-09-21 and 2026-11-20. Reference: 96.92 USD in the packet snapshot; the front-month contract settled at 100.30 USD on 2026-09-18. | TRUE if FRED series DCOILWTICO (EIA Cushing WTI spot) shows a daily value of 85.00 or lower on any date from 2026-09-21 through 2026-11-20. Reference: 96.92 USD on the packet date. |
| KKR-20260918-40 | 40% | 2026-12-18 | political | Democrats win control of the US Senate in the 2026-11-03 midterm elections, holding at least 51 seats together with independents Angus King and Bernie Sanders on Associated Press race calls made between 2026-11-03 and 2026-12-16. | TRUE if the AP balance-of-power tally, from race calls for the 2026-11-03 election made by 2026-12-16, shows Democrats plus independents King and Sanders holding at least 51 Senate seats. |
| KKR-20260918-41 | 40% | 2026-10-05 | political | United Russia receives 50.00 percent or more of the federal party-list vote in the State Duma election held 2026-09-18 to 2026-09-20, per final results certified by the Russian Central Election Commission between 2026-09-21 and 2026-10-02. | TRUE if final results certified by the Russian Central Election Commission between 2026-09-21 and 2026-10-02 give United Russia 50.00 percent or more of the federal party-list vote. |
| KKR-20260918-42 | 61% | 2026-11-03 | military/conflict | US forces strike at least one target on Iranian land territory, including Iranian islands, between 2026-09-21 and 2026-10-31; strikes limited to vessels at sea do not count. | TRUE if the Pentagon or CENTCOM confirms, or both Reuters and AP report, a US strike on a target on Iranian land territory, islands included, occurring between 2026-09-21 and 2026-10-31. |
| KKR-20260918-43 | 61% | 2026-11-03 | military/conflict | A Chinese coast guard, navy, or maritime militia vessel fires a water cannon at, rams, or collides with a Philippine government vessel in the South China Sea between 2026-09-21 and 2026-10-31. | TRUE if the Philippine Coast Guard or Armed Forces of the Philippines reports a Chinese water-cannon, ramming or collision incident against a Philippine government vessel dated 2026-09-21 to 2026-10-31, carried by Reuters or AP. |
| KKR-20260918-44 | 23% | 2026-11-03 | crime/security | A single non-state militant attack in Pakistan kills at least 10 people, not counting the attackers, between 2026-09-21 and 2026-10-31. | TRUE if Reuters or AP reports a non-state militant attack in Pakistan, occurring between 2026-09-21 and 2026-10-31, with a death toll from officials of at least 10 excluding attackers. |
| KKR-20260918-45 | 29% | 2026-11-23 | disaster | An earthquake of magnitude 6.0 or greater strikes within 250 km of the epicenter of the M6.5 event 169 km west of Nikolski, Alaska (USGS event us7000ti1p) between 2026-09-21 and 2026-11-20 UTC. | TRUE if the USGS ComCat catalog lists an event of magnitude 6.0 or greater within 250 km of the us7000ti1p epicenter with origin time between 2026-09-21 and 2026-11-20 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

2484 issued all-time across 16 forecaster arms · 2018 open (103 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 850 issued · 765 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 850 | 765 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 293 | 143 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 89 | 84 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 136 | 126 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 293 | 276 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 262 | 214 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*