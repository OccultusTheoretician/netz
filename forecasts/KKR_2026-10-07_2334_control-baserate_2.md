**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 072334Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-52 | 42% | 2026-10-22 | cyber | CISA adds at least one Atlassian product vulnerability to its Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-07 and 2026-10-20. | The CISA KEV catalog JSON contains at least one entry with vendorProject Atlassian and a dateAdded value between 2026-10-07 and 2026-10-20 inclusive. |
| KKR-20261007-53 | 69% | 2026-10-22 | military/conflict | Donald Trump and Vladimir Putin hold a direct phone call or in-person meeting between 2026-10-07 and 2026-10-20. | A White House or Kremlin official readout, or reports by at least two of Reuters, AP, and BBC, confirm a direct Trump-Putin call or meeting held between 2026-10-07 and 2026-10-20. |
| KKR-20261007-54 | 41% | 2026-11-10 | political | A Democratic Party candidate wins the Texas US Senate election held on 2026-11-03. | As of 2026-11-10, Texas Secretary of State unofficial results show a Democratic Party candidate with the most votes in the US Senate election held on 2026-11-03. |
| KKR-20261007-55 | 43% | 2026-11-12 | disaster | A second laboratory-confirmed Ebola case in Kenya, beyond the first case reported on or before 2026-10-07, is confirmed between 2026-10-08 and 2026-11-08. | WHO, Africa CDC, or the Kenya Ministry of Health reports, in a statement dated between 2026-10-08 and 2026-11-08, a laboratory-confirmed Ebola case in Kenya other than the first case reported on or before 2026-10-07. |
| KKR-20261007-56 | 58% | 2026-11-30 | economics/markets | ICE Brent front-month futures settle at or above 115.00 US dollars per barrel on at least one trading day between 2026-10-08 and 2026-11-25. Reference: 101.67 dollars on the packet date 2026-10-07. | ICE Brent front-month settlement is at or above 115.00 USD per barrel on at least one trading day between 2026-10-08 and 2026-11-25. Reference: 101.67 USD on the packet date 2026-10-07. |
| KKR-20261007-57 | 58% | 2026-11-30 | economics/markets | The US 10-year Treasury constant-maturity yield closes at or above 5.60 percent on at least one trading day between 2026-10-08 and 2026-11-25. Reference: 5.30 percent on the packet date 2026-10-07. | FRED series DGS10 shows a daily value at or above 5.60 on at least one date between 2026-10-08 and 2026-11-25. Reference: 5.30 percent on the packet date 2026-10-07. |
| KKR-20261007-58 | 69% | 2026-12-03 | military/conflict | A single Russian missile or drone attack on one Ukrainian city or town kills at least 30 people, with the attack occurring between 2026-10-08 and 2026-11-30. | At least two of Reuters, AP, and BBC report, citing Ukrainian officials, a death toll of at least 30 from one Russian attack on one Ukrainian city or town occurring between 2026-10-08 and 2026-11-30. |
| KKR-20261007-59 | 58% | 2026-12-21 | economics/markets | The US government publishes in the Federal Register an executive order, proclamation, or Commerce Department rule that prohibits or restricts exports of diesel fuel or distillate from the United States, with publication dated between 2026-10-08 and 2026-12-14. | A Federal Register document published between 2026-10-08 and 2026-12-14 contains an executive order, proclamation, or Commerce Department rule that prohibits or restricts United States exports of diesel fuel or distillate. |
| KKR-20261007-60 | 33% | 2027-03-24 | crime/security | German federal prosecutors file an indictment against the former head of a German intelligence service reported arrested for treason on or before 2026-10-07, with the filing dated between 2026-10-08 and 2027-03-19. | A Generalbundesanwalt press release or court announcement dated between 2026-10-08 and 2027-03-19 states that an indictment was filed against the former intelligence chief reported arrested for treason on or before 2026-10-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The French National Assembly brings down the sitting government by adopting a censure motion or rejecting a confidence vote on a date betwee" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3594 issued all-time across 21 forecaster arms · 2780 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1283 issued · 1082 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1283 | 1082 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 19 | 19 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 192 | 157 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 283 | 250 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*