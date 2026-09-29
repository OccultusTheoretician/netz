**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-29_1517.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260929-05 | 25% | 2026-10-10 | military/conflict | Between 2026-10-01 and 2026-10-07, at least one report from a hostile side will confirm that a drone strike occurred in Jabalia, Gaza City, with casualties claimed by at least one side. | At least one report from a hostile side (IL, PS, or AXIS) will confirm a drone strike in Jabalia, Gaza City, during the window, with casualties claimed in at least one corroborating report |
| KKR-20260929-06 | 45% | 2026-10-15 | economics/markets | Between 2026-10-05 and 2026-10-11, the S&P 500 will close below 7,500.00 on at least one weekday. | The S&P 500 will close below 7,500.00 on at least one weekday between 2026-10-05 and 2026-10-11, inclusive, as reported by the NYSE or Bloomberg |
| KKR-20260929-07 | 30% | 2026-10-18 | military/conflict | Between 2026-10-08 and 2026-10-14, at least one report from a hostile side will confirm that a cruise missile was launched from Zaporizhzhia toward Kyiv. | At least one report from a hostile side (RU or UA) will confirm a cruise missile launch from Zaporizhzhia toward Kyiv during the window, with weapons reported in at least one corroborating report |
| KKR-20260929-08 | 15% | 2026-10-30 | cyber | Between 2026-10-20 and 2026-10-26, at least one report from a hostile side will confirm that a cyberattack exploited CVE-2026-86950 in a real-world attack. | At least one report from a hostile side (AXIS, WEST, RU, or IL) will confirm that CVE-2026-86950 was exploited in a real-world cyberattack during the window |
| KKR-20260929-09 | 35% | 2026-11-02 | economics/markets | Between 2026-10-22 and 2026-10-28, the 10-year US Treasury yield will close above 5.50 percent on at least one weekday. | The 10-year US Treasury yield will close above 5.50 percent on at least one weekday between 2026-10-22 and 2026-10-28, inclusive, as reported by FRED or Bloomberg |
| KKR-20260929-10 | 28% | 2026-11-05 | military/conflict | Between 2026-10-25 and 2026-10-31, at least one report from a hostile side will confirm that a new military mobilization order was issued by Russia. | At least one report from a hostile side (RU or UA) will confirm a new military mobilization order issued by Russia during the window |
| KKR-20260929-11 | 42% | 2026-11-10 | economics/markets | Between 2026-11-01 and 2026-11-07, the EUR/USD exchange rate will close below 1.10 on at least one weekday. | The EUR/USD exchange rate will close below 1.10 on at least one weekday between 2026-11-01 and 2026-11-07, inclusive, as reported by Bloomberg or Reuters |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-30, the CISA KEV catalog will carry a date-added value for CVE-2026-86950 between 2026-09-29 and 2026-10-01." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-86950 dateAdded 2026-09-29, already inside the claimed window 2026-09-29..2026-10-01
- "On 2026-10-12, the US Treasury will publish a new sanctions list targeting Iranian individuals and entities related to the Houthis." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-12 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-15 and 2026-10-21, the Brent crude oil price will close above 105.00 per barrel on at least one weekday." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day

## III. LEDGER STANDING

3051 issued all-time across 17 forecaster arms · 2509 open (260 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 143 issued · 138 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1083 | 966 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 340 | 190 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 143 | 138 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 216 | 199 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*