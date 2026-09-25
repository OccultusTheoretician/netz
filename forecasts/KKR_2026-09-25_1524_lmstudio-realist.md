**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251524Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-25_1520.md · forecaster: lmstudio/realist · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260925-01 | 25% | 2026-10-04 | disaster | Between 2026-09-26 and 2026-10-02, the USGS Significant Quakes feed will report a magnitude 6.0 or higher earthquake in the Pacific Ring of Fire. | The USGS Significant Quakes feed reports a magnitude 6.0 or higher earthquake in the Pacific Ring of Fire between 2026-09-26 and 2026-10-02. |
| KKR-20260925-02 | 75% | 2026-10-04 | cyber | Between 2026-09-26 and 2026-10-02, the CISA KEV catalog will list at least one new exploited vulnerability in a critical infrastructure system. | The CISA KEV catalog carries at least one new exploited vulnerability in a critical infrastructure system between 2026-09-26 and 2026-10-02. |
| KKR-20260925-03 | 55% | 2026-10-04 | economics | Between 2026-09-26 and 2026-10-02, the 10-year Treasury yield will exceed 5.30 percent. | The 10-year Treasury yield exceeds 5.30 percent on or before 2026-10-02. |
| KKR-20260925-04 | 40% | 2026-10-06 | disaster | Between 2026-09-26 and 2026-10-02, a new tropical cyclone will be designated as a Category 3 or higher storm by the National Hurricane Center. | The National Hurricane Center designates a new tropical cyclone as Category 3 or higher between 2026-09-26 and 2026-10-02. |
| KKR-20260925-05 | 35% | 2026-10-04 | economics | Between 2026-09-26 and 2026-10-02, the U.S. Strategic Petroleum Reserve will report a level below 350 million barrels. | The U.S. Strategic Petroleum Reserve reports a level below 350 million barrels on or before 2026-10-02. |
| KKR-20260925-06 | 20% | 2026-10-06 | military/conflict | Between 2026-09-26 and 2026-10-02, a new military escalation in the Russia-Ukraine conflict will be confirmed by at least two hostile sides. | At least two hostile sides confirm a new military escalation in the Russia-Ukraine conflict between 2026-09-26 and 2026-10-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-26 and 2026-10-02, the CISA KEV catalog will include CVE-2026-5430 with a date-added value of 2026-09-24." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-5430 dateAdded 2026-09-24, before the claimed window 2026-09-26..2026-10-02; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-26 and 2026-10-02, the CISA KEV catalog will include CVE-2026-71362 with a date-added value of 2026-09-24." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-71362 dateAdded 2026-09-24, before the claimed window 2026-09-26..2026-10-02; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-26 and 2026-10-02, the S&P 500 will close above 7,750." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-26 and 2026-10-02, a new cyberattack targeting a U.S. federal agency will be confirmed by two independent sources." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2830 issued all-time across 17 forecaster arms · 2288 open (189 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 119 issued · 114 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 990 | 873 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 119 | 114 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 181 | 164 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 10 | 10 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 314 | 250 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*