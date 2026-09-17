**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-17_1518.md · forecaster: lmstudio/realist · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260917-07 | 25% | 2026-09-26 | disaster | Between 2026-09-18 and 2026-09-24, the USGS Significant Quakes feed will report a magnitude 6.5 or higher earthquake in the Fox Islands, Aleutian Islands, with a depth of 100 km or more. | The USGS Significant Quakes feed reports a magnitude 6.5 or higher earthquake in the Fox Islands, Aleutian Islands, with a depth of 100 km or more. |
| KKR-20260917-08 | 35% | 2026-09-26 | military/conflict | Between 2026-09-18 and 2026-09-24, at least one of the following will occur: a drone strike on Kyiv confirmed by two hostile sides, or a ballistic missile attack on Kharkiv confirmed by two hostile sides. | At least one of the following occurs: a drone strike on Kyiv confirmed by two hostile sides, or a ballistic missile attack on Kharkiv confirmed by two hostile sides. |
| KKR-20260917-09 | 30% | 2026-09-26 | cyber | Between 2026-09-18 and 2026-09-24, a new vulnerability in Cisco Identity Services Engine (ISE) will be exploited in at least one confirmed cyberattack, as reported by two independent sources. | A new vulnerability in Cisco Identity Services Engine (ISE) is exploited in at least one confirmed cyberattack, as reported by two independent sources. |
| KKR-20260917-10 | 20% | 2026-09-26 | political | Between 2026-09-18 and 2026-09-24, the European Union will formally propose associate membership for Canada, as confirmed by two independent news outlets. | The European Union formally proposes associate membership for Canada, as confirmed by two independent news outlets. |
| KKR-20260917-11 | 45% | 2026-09-26 | disaster | Between 2026-09-18 and 2026-09-24, at least one of the following will occur: a flood warning issued in the Upper Rio Grande Valley, or a flash flood warning issued in the Eastern San Juan Mountains. | At least one of the following occurs: a flood warning issued in the Upper Rio Grande Valley, or a flash flood warning issued in the Eastern San Juan Mountains. |
| KKR-20260917-12 | 35% | 2026-09-26 | economics/markets | Between 2026-09-18 and 2026-09-24, the Bank of England will leave interest rates unchanged, as confirmed by a press release from the Bank. | The Bank of England leaves interest rates unchanged, as confirmed by a press release from the Bank. |
| KKR-20260917-13 | 25% | 2026-09-26 | political | Between 2026-09-18 and 2026-09-24, the U.S. House will vote to hold billionaire Epstein associate Leon Black in contempt of Congress, as confirmed by a roll call vote on Congress.gov. | The U.S. House votes to hold billionaire Epstein associate Leon Black in contempt of Congress, as confirmed by a roll call vote on Congress.gov. |
| KKR-20260917-14 | 20% | 2026-09-26 | cyber | Between 2026-09-18 and 2026-09-24, a new AI-powered data breach will be reported in Spain, as confirmed by a public statement from Spain's data agency. | A new AI-powered data breach is reported in Spain, as confirmed by a public statement from Spain's data agency. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-18 and 2026-09-24, the CISA KEV catalog will include CVE-2026-58704 with a date-added value of 2026-09-16." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-58704 dateAdded 2026-09-16, before the claimed window 2026-09-18..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-18 and 2026-09-24, the S&P 500 will close below 7,500 points on at least one weekday." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2379 issued all-time across 16 forecaster arms · 1913 open (82 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 81 issued · 76 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 805 | 720 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 286 | 136 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 81 | 76 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 121 | 111 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 273 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 252 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*