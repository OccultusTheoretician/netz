**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121656Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-01 | 25% | 2026-10-07 | disaster | Between 2026-09-22 and 2026-09-29, the USGS Significant Quakes feed will report a magnitude 6.0 or higher earthquake in Indonesia with a depth of less than 100 km. | The USGS Significant Quakes feed reports a magnitude 6.0 or higher earthquake in Indonesia with a depth of less than 100 km between 2026-09-22 and 2026-09-29. |
| KKR-20260912-02 | 35% | 2026-10-09 | political | Between 2026-09-24 and 2026-10-01, the Federal Register will publish a rulemaking notice related to AI safety or regulation. | The Federal Register publishes a rulemaking notice related to AI safety or regulation between 2026-09-24 and 2026-10-01. |
| KKR-20260912-03 | 40% | 2026-10-11 | economics | Between 2026-09-26 and 2026-10-03, the Brent crude oil price will exceed $105 per barrel on at least one weekday. | The Brent crude oil price exceeds $105 per barrel on at least one weekday between 2026-09-26 and 2026-10-03. |
| KKR-20260912-04 | 20% | 2026-10-12 | military/conflict | Between 2026-09-27 and 2026-10-04, the Iranian government will publicly confirm the capture of Mayun Island in the Red Sea. | The Iranian government publicly confirms the capture of Mayun Island in the Red Sea between 2026-09-27 and 2026-10-04. |
| KKR-20260912-05 | 25% | 2026-10-13 | disaster | Between 2026-09-28 and 2026-10-05, the USGS Significant Quakes feed will report a magnitude 6.0 or higher earthquake in the Russian Federation with a depth of less than 100 km. | The USGS Significant Quakes feed reports a magnitude 6.0 or higher earthquake in the Russian Federation with a depth of less than 100 km between 2026-09-28 and 2026-10-05. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-28, the CISA KEV catalog will include CVE-2026-84869 with a date-added value of 2026-09-11." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-84869 dateAdded 2026-09-11, before the claimed window 2026-09-21..2026-09-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-23 and 2026-09-30, the S&P 500 will close above 7,700 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-25 and 2026-10-02, the CISA KEV catalog will include CVE-2026-42016 with a date-added value of 2026-09-11." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-42016 dateAdded 2026-09-11, before the claimed window 2026-09-25..2026-10-02; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-29 and 2026-10-06, the CISA KEV catalog will include CVE-2026-42018 with a date-added value of 2026-09-11." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-42018 dateAdded 2026-09-11, before the claimed window 2026-09-29..2026-10-06; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-30 and 2026-10-07, the S&P 500 will close below 7,600 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1956 issued all-time across 16 forecaster arms · 1620 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 259 issued · 130 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 625 | 587 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 211 | 208 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 226 | 220 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 212 | 180 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*