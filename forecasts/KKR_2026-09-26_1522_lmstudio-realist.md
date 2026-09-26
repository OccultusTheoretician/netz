**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 261522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-26_1518.md · forecaster: lmstudio/realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260926-01 | 30% | 2026-10-07 | military/conflict | Between 2026-09-26 and 2026-10-03, at least one Grade A or Grade B kinetic event will be reported in the Russia-Ukraine Theatre involving a missile strike on Kyiv. | At least one Grade A or Grade B kinetic event involving a missile strike on Kyiv will be reported in the Russia-Ukraine Theatre between 2026-09-26 and 2026-10-03. |
| KKR-20260926-02 | 20% | 2026-10-08 | military/conflict | Between 2026-09-26 and 2026-10-03, the Strait of Hormuz will be closed to commercial shipping for at least 48 hours due to a confirmed Iranian military action. | A confirmed Iranian military action will result in the Strait of Hormuz being closed to commercial shipping for at least 48 consecutive hours between 2026-09-26 and 2026-10-03. |
| KKR-20260926-03 | 35% | 2026-10-07 | disaster | Between 2026-09-26 and 2026-10-03, Bangkok will report at least one confirmed flood-related fatality. | At least one confirmed flood-related fatality will be reported in Bangkok between 2026-09-26 and 2026-10-03. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-27, the CISA KEV catalog will carry a date-added value for CVE-2026-67279 between 2026-09-25 and 2026-09-26." → REJECTED: event window opens 2026-09-25, before this row is sealed (2026-09-26, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-67279 dateAdded 2026-09-25, already inside the claimed window 2026-09-25..2026-09-26
- "Between 2026-09-26 and 2026-10-03, the S&P 500 will close above 7,800 on at least one day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-26 and 2026-10-03, at least one confirmed cyberattack exploiting CVE-2026-65660 will be reported by a wire service." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "On 2026-10-01, the 10-year Treasury yield will exceed 5.25 percent." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-01 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-02, the USGS Significant Quakes catalog will list an earthquake of magnitude 6.0 or higher in the Pacific region." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-02 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-26 and 2026-10-03, at least one major cyberattack will be reported to have compromised a U.S. federal agency's network." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-03, the Federal Register will publish a notice of a new U.S. sanctions list targeting Iranian entities related to missile develop" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-03 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2879 issued all-time across 17 forecaster arms · 2337 open (209 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 122 issued · 117 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1013 | 896 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 122 | 117 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 190 | 173 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 320 | 256 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*