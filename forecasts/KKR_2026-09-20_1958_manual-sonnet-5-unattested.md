**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201958Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-20_1517.md · forecaster: manual/sonnet-5/unattested · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260920-40 | 55% | 2026-09-30 | military/conflict | Ukraine launches another single-wave strike of at least 100 drones toward the Moscow region between 2026-09-21 and 2026-09-28, matching the tempo of the 20 September attack described as the largest on Moscow to date. | Two independently-biased channels (Russian, Ukrainian, or a wire service) report a single launch of at least 100 UAVs toward Moscow region between 2026-09-21 and 2026-09-28. |
| KKR-20260920-41 | 15% | 2026-10-21 | military/conflict | A formal ceasefire or truce between the United States and Iran, confirmed by matching statements from the US State Department or White House and the Iranian Foreign Ministry, is announced between 2026-09-21 and 2026-10-19. | Official US and Iranian government channels each issue a statement describing a ceasefire, truce, or armistice ending hostilities between 2026-09-21 and 2026-10-19, corroborated by a wire service. |
| KKR-20260920-42 | 8% | 2026-10-28 | political | Following the 20 September 2026 German state elections referenced as testing the position of Chancellor Friedrich Merz, a formal constructive vote of no confidence against Merz is tabled in the Bundestag between 2026-09-21 and 2026-10-26. | The Bundestag plenary record (bundestag.de) or a wire service reports a constructive no-confidence motion against Chancellor Merz tabled or voted on between 2026-09-21 and 2026-10-26. |
| KKR-20260920-43 | 93% | 2026-09-30 | political | Russia Central Election Commission official results confirm United Russia, party list plus single-mandate seats combined, retains an outright majority of State Duma seats following the election that concluded 20 September 2026, published by 2026-09-30. | The Russian Central Election Commission (cikrf.ru) or a wire service reports United Russia holding more than 225 of 450 State Duma seats by 2026-09-30. |
| KKR-20260920-44 | 20% | 2026-10-21 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry, with dateAdded between 2026-09-21 and 2026-10-19, for a vulnerability in the class of AI coding-agent sandbox escapes or malicious npm package supply-chain compromise, matching the techniques reported 20 September 2026. | The CISA KEV catalog lists a CVE with dateAdded between 2026-09-21 and 2026-10-19 whose description matches sandbox-escape or npm supply-chain compromise techniques. |
| KKR-20260920-45 | 38% | 2026-10-02 | disaster | USGS records at least one aftershock of magnitude 5.0 or greater within 150 km of the 20 September 2026 M6.5 Nikolski, Alaska mainshock, USGS event us7000ti1p, between 2026-09-21 and 2026-09-30. | The USGS earthquake catalog lists an event of M5.0 or greater within 150 km of the Nikolski epicenter, origin time between 2026-09-21 and 2026-09-30. |
| KKR-20260920-46 | 48% | 2026-12-21 | political | The Upper Tribunal or relevant UK court publicly lists a hearing date for the legal challenge brought by Meta against Ofcom over the Online Safety Act, reported 20 September 2026, between 2026-09-21 and 2026-12-19. | A UK court or tribunal public cause list, or a wire service report, shows a scheduled hearing date for the Meta v Ofcom challenge between 2026-09-21 and 2026-12-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "OpenAI issues a public statement, blog post, or on-the-record comment to a wire service or major tech outlet addressing the staff account co" → REJECTED: resolution offers alternative VENUES joined by 'or' (…wire service | or | major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "WTI crude oil settles below 90.00 USD per barrel at NYMEX close on 2026-10-30. Reference: 96.08 USD per barrel on the packet date, 2026-09-2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…price on 2026-10-30, as reported by cme group | or | a financial wire service, closes below 90…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-10-30) is 0 day(s) after the window closes (2026-10-30). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "The S&P 500 index closes below 7400.00 at the NYSE session close on 2026-10-16. Reference: 7650.50 on the packet date, 2026-09-20." → REJECTED: resolution offers alternative VENUES joined by 'or' (…0-16, as reported by a financial wire service | or | exchange data, is below 7400…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-10-16) is 0 day(s) after the window closes (2026-10-16). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days

## III. LEDGER STANDING

2592 issued all-time across 16 forecaster arms · 2126 open (164 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 284 issued · 236 open · 43 resolved · 21 hits / 22 misses · **Brier 0.207** against its own base rate 48.8% (climatological 0.250) · **skill +0.172**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 889 | 804 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 309 | 159 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 96 | 91 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 147 | 137 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 306 | 289 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 284 | 236 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*