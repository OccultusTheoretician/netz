**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-22_1518.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260922-01 | 25% | 2026-10-05 | military/conflict | Between 2026-09-22 and 2026-09-28, at least one report from a hostile side confirms a drone strike on Kyiv with casualties reported. | At least one report from a hostile side (RU or UA) confirms a drone strike on Kyiv during the window with casualties stated in the corroborating report. |
| KKR-20260922-02 | 45% | 2026-10-07 | economics/markets | Between 2026-09-22 and 2026-09-28, the 10-year Treasury yield falls below 4.90 percent. | The 10-year Treasury yield closes below 4.90 percent on the last trading day of the window. |
| KKR-20260922-03 | 35% | 2026-10-05 | disaster | Between 2026-09-22 and 2026-09-28, the USGS reports a significant earthquake (M ≥ 6.0) in the Pacific Northwest. | The USGS Significant Quakes feed reports an earthquake with magnitude ≥ 6.0 in the Pacific Northwest region during the window. |
| KKR-20260922-04 | 40% | 2026-10-07 | political | Between 2026-09-22 and 2026-09-28, Iran's delegation to the UN General Assembly delivers a statement asserting that the Strait of Hormuz is open and secure. | Iran's delegation to the UN General Assembly delivers a statement during the window asserting that the Strait of Hormuz is open and secure. |
| KKR-20260922-05 | 30% | 2026-10-05 | military/conflict | Between 2026-09-22 and 2026-09-28, the Houthis launch a coordinated attack on a Red Sea port in Yemen resulting in at least one casualty. | At least one report from a hostile side confirms a coordinated attack by the Houthis on a Red Sea port in Yemen during the window with at least one casualty stated. |
| KKR-20260922-06 | 25% | 2026-10-07 | military/conflict | Between 2026-09-22 and 2026-09-28, the US government announces a new military base in Greenland with a public statement from the White House. | The White House issues a public statement during the window announcing the establishment of a new military base in Greenland. |
| KKR-20260922-07 | 35% | 2026-10-05 | cyber | Between 2026-09-22 and 2026-09-28, a new vulnerability with CVSS score 10.0 is added to the CISA KEV catalog. | The CISA KEV catalog includes a new vulnerability with a CVSS score of 10.0 during the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-22 and 2026-09-28, the CISA KEV catalog will include CVE-2026-7273 with a date-added value of 2026-09-21." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-7273 dateAdded 2026-09-21, before the claimed window 2026-09-22..2026-09-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-22 and 2026-09-28, the S&P 500 closes above 7,800 points." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-22 and 2026-09-28, at least one major cyberattack exploits CVE-2026-7273 in a government or critical infrastructure system." → REJECTED: resolution offers alternative VENUES joined by 'or' (…government | or | critical infrastructure…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2663 issued all-time across 16 forecaster arms · 2197 open (193 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 324 issued · 174 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 918 | 833 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 324 | 174 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 101 | 96 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 156 | 146 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*