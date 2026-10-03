**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-03_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261003-08 | 30% | 2026-10-14 | military/conflict | Between 2026-10-04 and 2026-10-10, at least one Grade A kinetic event will be confirmed in the Russia-Ukraine Theatre involving a drone strike on Kyiv with casualties claimed by a hostile side. | At least one Grade A kinetic event involving a drone strike on Kyiv in the Russia-Ukraine Theatre is confirmed by three or more hostile sides with casualties claimed in at least one corroborating report. |
| KKR-20261003-09 | 25% | 2026-10-16 | disaster | Between 2026-10-06 and 2026-10-13, a magnitude 5.0 or greater earthquake will be recorded by the USGS in the Pacific Northwest region (Washington, Oregon, or California) with a depth of less than 50 km. | The USGS Significant Quakes feed reports a magnitude 5.0 or greater earthquake in the Pacific Northwest region (Washington, Oregon, or California) with a depth of less than 50 km between 2026-10-06 and 2026-10-13. |
| KKR-20261003-10 | 40% | 2026-10-19 | disaster | Between 2026-10-09 and 2026-10-16, a major flood event will be reported in Bangkok, Thailand, with at least one official source confirming water levels exceeding 1.5 meters in central districts. | At least one official source confirms water levels exceeding 1.5 meters in central districts of Bangkok, Thailand, due to flooding between 2026-10-09 and 2026-10-16. |
| KKR-20261003-11 | 20% | 2026-10-20 | political | Between 2026-10-10 and 2026-10-17, a political scandal involving a U.S. federal official will be reported by at least two major wire services (e.g., Reuters, AP, Bloomberg) with a public resignation or indictment by the deadline. | At least two major wire services report a political scandal involving a U.S. federal official with a public resignation or indictment by 2026-10-17. |
| KKR-20261003-12 | 35% | 2026-10-22 | military/conflict | Between 2026-10-12 and 2026-10-19, a military escalation in the Israel-Gaza-Levant Theatre will result in a confirmed airstrike on Gaza City with casualties reported by at least two hostile sides. | A confirmed airstrike on Gaza City in the Israel-Gaza-Levant Theatre with casualties reported by at least two hostile sides occurs between 2026-10-12 and 2026-10-19. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-08, the CISA KEV catalog will include CVE-2026-102490 with a date-added value of 2026-10-02." → REJECTED: event window opens 2026-10-02, before this row is sealed (2026-10-03, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-10-05 and 2026-10-12, the S&P 500 will close below 7,700 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-07 and 2026-10-14, a cyberattack exploiting CVE-2026-102489 will be reported by at least two independent sources in the CISA" → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | the hacker news…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-08 and 2026-10-15, the 10Y Yield will close above 5.30 percent on at least one weekday." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-10-11 and 2026-10-18, a cyberattack on a U.S. state government system will be confirmed by both CISA and a major news outlet (e" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3282 issued all-time across 18 forecaster arms · 2740 open (497 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 166 issued · 161 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1173 | 1056 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 368 | 218 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 166 | 161 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 243 | 226 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 71 | 71 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*