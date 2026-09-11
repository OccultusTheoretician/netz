**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-01 | 40% | 2026-09-28 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield exceeds 5.0% on at least one weekday. | The 10-year U.S. Treasury yield on a weekday between 2026-09-21 and 2026-09-24 is greater than 5.0%. |
| KKR-20260911-02 | 20% | 2026-09-26 | disaster | Between 2026-09-21 and 2026-09-24, a Green flood alert is issued for Spain by GDACS and remains active through 2026-09-24. | The GDACS Alerts system carries a Green flood alert for Spain with a status of active on 2026-09-24. |
| KKR-20260911-03 | 35% | 2026-09-28 | economics/markets | Between 2026-09-21 and 2026-09-24, the U.S. dollar strengthens to a 1.17 exchange rate against the euro on at least one weekday. | The EUR/USD exchange rate on a weekday between 2026-09-21 and 2026-09-24 is less than or equal to 1.17. |
| KKR-20260911-04 | 15% | 2026-09-26 | disaster | Between 2026-09-21 and 2026-09-24, a new earthquake of magnitude 5.0 or higher is recorded in Indonesia with a depth less than 100 km, as confirmed by USGS. | The USGS Significant Quakes system records an earthquake with magnitude ≥5.0 and depth <100 km in Indonesia between 2026-09-21 and 2026-09-24. |
| KKR-20260911-05 | 20% | 2026-09-28 | political | Between 2026-09-21 and 2026-09-24, a new political statement by a U.S. government official about Iran's nuclear program is confirmed by at least two independent news outlets (e.g., BBC, Guardian, Al Jazeera). | Two or more independent news outlets report a public statement by a U.S. government official on Iran's nuclear program between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, at least one drone strike targeting a fuel station in Kyiv is confirmed by at least three independently b" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-21 and 2026-09-24, the S&P 500 closes below 7,600 at the end of trading on a weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog includes a new entry for a vulnerability in MikroTik RouterOS with a date-added valu" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-21 and 2026-09-24, a new vulnerability in PaperCut software is exploited in at least 100 organizations, as confirmed by two " → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-21 and 2026-09-24, a new AI-powered cyberattack exploits a vulnerability in a widely used software platform, resulting in a " → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1885 issued all-time across 16 forecaster arms · 1549 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 254 issued · 125 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 596 | 558 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*