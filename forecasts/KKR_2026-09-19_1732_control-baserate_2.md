**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191732Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-19_1516.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260919-27 | 40% | 2026-10-06 | political | United Russia wins at least 300 of 450 State Duma seats in the election held 2026-09-18 to 2026-09-20, per final results the Central Election Commission approves between 2026-09-21 and 2026-10-02. | TRUE if final results approved by the Russian Central Election Commission (cikrf.ru) between 2026-09-21 and 2026-10-02 allocate United Russia 300 or more of 450 seats, list and single-mandate combined; otherwise FALSE. |
| KKR-20260919-28 | 24% | 2026-11-02 | economics/markets | The FOMC raises the federal funds target range at its scheduled 2026-10-27 to 2026-10-28 meeting. Reference: 3.75 to 4.00 percent at seal, FRED DFEDTARU 4.00. | TRUE if FRED series DFEDTARU for 2026-10-29 exceeds 4.00, reflecting a target-range increase announced in the FOMC statement of 2026-10-28; otherwise FALSE. |
| KKR-20260919-29 | 29% | 2026-11-17 | cyber | CISA adds CVE-2026-58138, the Orkes Conductor unauthenticated remote code execution flaw, to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-21 and 2026-11-13. | TRUE if the CISA KEV JSON feed lists CVE-2026-58138 with a dateAdded value between 2026-09-21 and 2026-11-13 inclusive; otherwise FALSE. |
| KKR-20260919-30 | 29% | 2026-12-22 | cyber | Have I Been Pwned loads the Gyazo (Helpfeel) breach of 2026-09-11, with an AddedDate between 2026-09-21 and 2026-12-18. | TRUE if the HIBP breaches API (haveibeenpwned.com/api/v3/breaches) lists a Gyazo breach with AddedDate between 2026-09-21 and 2026-12-18; otherwise FALSE. |
| KKR-20260919-31 | 23% | 2026-11-24 | crime/security | South African police arrest a suspect they publicly link to one or more of the nine Ekurhuleni killings of women, with the arrest made between 2026-09-21 and 2026-11-20, excluding the July 2026 Kempton Park arrest. | TRUE if SAPS announces, and Reuters, AP, AFP, or News24 reports, an arrest made between 2026-09-21 and 2026-11-20 of a suspect SAPS links to any of the nine Ekurhuleni killings; otherwise FALSE. |
| KKR-20260919-32 | 61% | 2027-01-19 | military/conflict | The US formally notifies Congress of at least one Foreign Military Sale to Taiwan, published by DSCA as a Major Arms Sale naming the Taipei Economic and Cultural Representative Office, between 2026-09-25 and 2027-01-15. | TRUE if the DSCA Major Arms Sales listing (dsca.mil) carries at least one TECRO notification dated between 2026-09-25 and 2027-01-15; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CNN, Politico, or MS NOW, or journalists from any of them, file a federal lawsuit challenging the White House access ban announced 2026-09-1" → REJECTED: resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "ICE Brent front-month futures settle at or above 115.00 USD per barrel on at least one trading day between 2026-09-21 and 2026-11-20. Refere" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "US forces strike Houthi targets inside Yemen at least once between 2026-09-21 and 2026-11-06, with the strike publicly confirmed by US Centr" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Cuban national electric grid suffers a new total collapse, announced by the Ministry of Energy and Mines or Union Electrica, between 202" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

2532 issued all-time across 16 forecaster arms · 2066 open (157 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 869 issued · 784 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 869 | 784 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 301 | 151 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 91 | 86 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 141 | 131 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 299 | 282 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 270 | 222 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*