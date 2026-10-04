**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-04_1517.md · forecaster: lmstudio/realist · 9 accepted / 1 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261004-09 | 30% | 2026-10-13 | cyber | Between 2026-10-05 and 2026-10-11, the CISA KEV catalog will carry at least one new entry with a date-added value between 2026-10-04 and 2026-10-11. | The CISA KEV catalog contains at least one vulnerability entry with a date-added value in the range 2026-10-04 to 2026-10-11, as recorded in the official CISA KEV API response. |
| KKR-20261004-10 | 45% | 2026-10-13 | economics/markets | Between 2026-10-05 and 2026-10-11, the S&P 500 will close below 7,650.00 on at least one trading day. | The S&P 500 closes below 7,650.00 on at least one weekday between 2026-10-05 and 2026-10-11, based on the official closing price from a major exchange. |
| KKR-20261004-11 | 25% | 2026-10-13 | military/conflict | Between 2026-10-05 and 2026-10-11, at least one Grade A or B kinetic event will be reported in the Kyiv or Dnipro area of the Russia-Ukraine Theatre with a weapon type of cruise missile or ballistic missile. | At least one Grade A or B kinetic event in the Kyiv or Dnipro area, reported between 2026-10-05 and 2026-10-11, includes the weapon type 'cruise missile' or 'ballistic missile' as verified by at least two independently biased sources. |
| KKR-20261004-12 | 35% | 2026-10-13 | economics/markets | Between 2026-10-05 and 2026-10-11, the 10-year U.S. Treasury yield will exceed 5.40 percent on at least one trading day. | The 10-year U.S. Treasury yield exceeds 5.40 percent on at least one weekday between 2026-10-05 and 2026-10-11, as reported by the U.S. Department of the Treasury or FRED. |
| KKR-20261004-13 | 20% | 2026-10-13 | military/conflict | Between 2026-10-05 and 2026-10-11, a Grade A or B event will be reported in the Gaza City or Khan Younis area of the Israel-Gaza-Levant Theatre involving an airstrike or drone strike with casualties claimed by at least one side. | At least one Grade A or B event in Gaza City or Khan Younis, reported between 2026-10-05 and 2026-10-11, involves an airstrike or drone strike and includes a casualty claim by at least one side, verified by two independently biased sources. |
| KKR-20261004-14 | 30% | 2026-10-13 | disaster | Between 2026-10-05 and 2026-10-11, the USGS Significant Quakes catalog will record at least one earthquake of magnitude 5.0 or higher with a depth of less than 50 km. | The USGS Significant Quakes catalog records at least one earthquake with a magnitude of 5.0 or higher and a depth of less than 50 km between 2026-10-05 and 2026-10-11, as verified by the USGS API. |
| KKR-20261004-15 | 15% | 2026-10-13 | cyber | Between 2026-10-05 and 2026-10-11, a new cyberattack targeting a U.S. federal agency will be confirmed by at least two independent sources, including one from a Western outlet and one from a non-aligned outlet. | A cyberattack targeting a U.S. federal agency is confirmed by at least two independent sources between 2026-10-05 and 2026-10-11, with one source from a Western outlet and one from a non-aligned outlet, as verified by public reporting. |
| KKR-20261004-16 | 20% | 2026-10-13 | political | Between 2026-10-05 and 2026-10-11, the German Chancellor will publicly announce a new military aid package to Ukraine during a visit to Kyiv. | The German Chancellor publicly announces a new military aid package to Ukraine during a visit to Kyiv between 2026-10-05 and 2026-10-11, as confirmed by at least two independent Western news outlets. |
| KKR-20261004-17 | 25% | 2026-10-13 | military/conflict | Between 2026-10-05 and 2026-10-11, the Sanaa area in Yemen will report a Grade A or B event involving an airstrike or missile strike with casualties claimed by at least one side. | A Grade A or B event in Sanaa, Yemen, involving an airstrike or missile strike with casualties claimed by at least one side is confirmed by two independently biased sources between 2026-10-05 and 2026-10-11. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-05 and 2026-10-11, the Brazilian presidential election will result in a runoff between Lula and Bolsonaro, with the final vo" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

3339 issued all-time across 18 forecaster arms · 2797 open (502 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 175 issued · 170 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1193 | 1076 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 376 | 226 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 175 | 170 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 250 | 233 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 78 | 78 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*