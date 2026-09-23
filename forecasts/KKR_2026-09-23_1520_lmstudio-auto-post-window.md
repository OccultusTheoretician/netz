**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-23_1518.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260923-01 | 45% | 2026-10-07 | military/conflict | Between 2026-09-23 and 2026-09-24, at least one drone strike will be reported in Kyiv, Ukraine, with cross-bias corroboration from at least two hostile sides. | At least one drone strike is reported in Kyiv, Ukraine, between 2026-09-23 and 2026-09-24, with corroborating reports from at least two hostile sides (RU, UA). |
| KKR-20260923-02 | 25% | 2026-10-07 | disaster | Between 2026-09-23 and 2026-09-24, a confirmed earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific Northwest. | The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Northwest between 2026-09-23 and 2026-09-24. |
| KKR-20260923-03 | 35% | 2026-10-07 | cyber | Between 2026-09-23 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-94127 will be reported by at least two independent sources. | A confirmed cyberattack exploiting CVE-2026-94127 is reported by at least two independent sources between 2026-09-23 and 2026-09-24. |
| KKR-20260923-04 | 20% | 2026-10-07 | crime/security | Between 2026-09-23 and 2026-09-24, a mass shooting resulting in four or more fatalities will be reported in South Africa with corroboration from at least two independent outlets. | A mass shooting resulting in four or more fatalities is reported in South Africa between 2026-09-23 and 2026-09-24, with corroboration from at least two independent outlets. |
| KKR-20260923-05 | 30% | 2026-10-07 | disaster | Between 2026-09-23 and 2026-09-24, a tropical cyclone named SURIGAE-26 will make landfall in Southeast Asia with a population of at least 1 million affected. | A tropical cyclone named SURIGAE-26 makes landfall in Southeast Asia between 2026-09-23 and 2026-09-24, with a population of at least 1 million affected, as confirmed by GDACS. |
| KKR-20260923-06 | 15% | 2026-10-07 | political | Between 2026-09-23 and 2026-09-24, the UN General Assembly will adopt a resolution calling for a ceasefire in the Israel-Gaza conflict, with support from at least three permanent members. | The UN General Assembly adopts a resolution calling for a ceasefire in the Israel-Gaza conflict between 2026-09-23 and 2026-09-24, with support from at least three permanent members. |
| KKR-20260923-07 | 28% | 2026-10-07 | cyber | Between 2026-09-23 and 2026-09-24, a confirmed ransomware attack using the Ryuk variant will be reported by a major cybersecurity firm. | A confirmed ransomware attack using the Ryuk variant is reported by a major cybersecurity firm between 2026-09-23 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-24, the CISA KEV catalog will include CVE-2026-93952 with a date-added value of 2026-09-22." → REJECTED: event window opens 2026-09-22, before this row is sealed (2026-09-23, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-23 and 2026-09-24, the S&P 500 will close above 7,750." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-23 and 2026-09-24, the 10-year Treasury yield will exceed 5.10 percent at market close." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day

## III. LEDGER STANDING

2718 issued all-time across 16 forecaster arms · 2176 open (153 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 329 issued · 179 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 942 | 825 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 103 | 98 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 164 | 147 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 320 | 295 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 299 | 235 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*