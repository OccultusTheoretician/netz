**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121658Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: lmstudio/realist · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-06 | 25% | 2026-09-23 | military/conflict | Between 2026-09-13 and 2026-09-19, at least one of the following will be reported in two or more independent wire services: a drone strike on a Ukrainian military target in Kyiv or a missile strike on a Russian military installation in Moscow. | At least one of the following will be reported in two or more independent wire services: a drone strike on a Ukrainian military target in Kyiv or a missile strike on a Russian military installation in Moscow, with the event window falling between 2026-09-13 and 2026-09-19. |
| KKR-20260912-07 | 35% | 2026-09-23 | disaster | Between 2026-09-15 and 2026-09-22, the USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Indonesia. | The USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Indonesia between 2026-09-15 and 2026-09-22. |
| KKR-20260912-08 | 40% | 2026-09-25 | military/conflict | Between 2026-09-16 and 2026-09-23, at least one of the following will be reported in two or more independent outlets: a Houthi attack on a commercial vessel in the Red Sea or a Saudi-led coalition airstrike on a Houthi position in Yemen. | At least one of the following will be reported in two or more independent outlets: a Houthi attack on a commercial vessel in the Red Sea or a Saudi-led coalition airstrike on a Houthi position in Yemen, with the event window falling between 2026-09-16 and 2026-09-23. |
| KKR-20260912-09 | 30% | 2026-09-25 | economics/markets | Between 2026-09-17 and 2026-09-24, the 10-year U.S. Treasury yield will close above 5.0 percent on at least one weekday. | The 10-year U.S. Treasury yield will close above 5.0 percent on at least one weekday between 2026-09-17 and 2026-09-24. |
| KKR-20260912-10 | 35% | 2026-09-27 | disaster | Between 2026-09-18 and 2026-09-25, the GDACS Alerts system will issue a Red or Orange alert for a forest fire in Russia or Kazakhstan. | The GDACS Alerts system will issue a Red or Orange alert for a forest fire in Russia or Kazakhstan between 2026-09-18 and 2026-09-25. |
| KKR-20260912-11 | 15% | 2026-09-28 | political | Between 2026-09-19 and 2026-09-26, the European Parliament will adopt a resolution calling for the immediate suspension of all EU military aid to Ukraine. | The European Parliament will adopt a resolution calling for the immediate suspension of all EU military aid to Ukraine between 2026-09-19 and 2026-09-26. |
| KKR-20260912-12 | 45% | 2026-09-29 | cyber | Between 2026-09-20 and 2026-09-27, at least one of the following will be reported in two or more independent outlets: a cyberattack on a U.S. federal agency using a vulnerability from the CISA KEV catalog or a ransomware attack on a U.S. hospital system. | At least one of the following will be reported in two or more independent outlets: a cyberattack on a U.S. federal agency using a vulnerability from the CISA KEV catalog or a ransomware attack on a U.S. hospital system, with the event window falling between 2026-09-20 and 2026-09-27. |
| KKR-20260912-13 | 50% | 2026-09-30 | economics/markets | Between 2026-09-21 and 2026-09-28, the Brent crude oil price will close above $105 per barrel on at least one weekday. | The Brent crude oil price will close above $105 per barrel on at least one weekday between 2026-09-21 and 2026-09-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-13, the CISA KEV catalog will carry a date-added value between 2026-09-11 and 2026-09-12 for CVE-2026-84869." → REJECTED: event window opens 2026-09-11, before this row is sealed (2026-09-12, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-84869 dateAdded 2026-09-11, already inside the claimed window 2026-09-11..2026-09-12
- "Between 2026-09-14 and 2026-09-21, the S&P 500 will close above 7,700 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

1964 issued all-time across 16 forecaster arms · 1628 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 53 issued · 53 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
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