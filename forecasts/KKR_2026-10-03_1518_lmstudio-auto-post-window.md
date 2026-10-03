**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 031518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-03_1517.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261003-01 | 25% | 2026-11-05 | military/conflict | Between 2026-10-21 and 2026-10-28, a drone strike with reported casualties of 955 will be confirmed by at least three independent sources across hostile sides in the Kyiv theatre. | At least three independent sources from distinct hostile sides (RU, UA, AXIS) will report a drone strike in Kyiv with claimed casualties of 955, corroborated by at least one additional source outside the initial reporting cluster. |
| KKR-20261003-02 | 35% | 2026-11-05 | disaster | Between 2026-10-21 and 2026-10-28, a magnitude 5.0 or greater earthquake will be recorded in the USGS Significant Quakes database with a depth of less than 50km and epicenter within 100km of Washington state. | The USGS Significant Quakes database will list an event with magnitude ≥ 5.0, depth < 50km, and epicenter within 100km of Washington state between 2026-10-21 and 2026-10-28. |
| KKR-20261003-03 | 20% | 2026-11-05 | political | Between 2026-10-21 and 2026-10-28, the US Treasury will release a public notice announcing the launch of a new savings account program for children under 18, with a minimum initial deposit of $100. | The US Treasury publishes a public notice on a government website confirming the launch of a new savings account program for children under 18, with a minimum initial deposit of $100. |
| KKR-20261003-04 | 30% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-28, a cyberattack exploiting CVE-2026-102489 will be reported by at least two independent sources in the CISA KEV or The Hacker News feed. | At least two independent sources (e.g., CISA KEV, The Hacker News) report a cyberattack exploiting CVE-2026-102489 between 2026-10-21 and 2026-10-28. |
| KKR-20261003-05 | 35% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-28, a ransomware attack targeting a water utility or telecom operator will be confirmed by BleepingComputer with a public report detailing the use of Warlock ransomware. | BleepingComputer publishes a report between 2026-10-21 and 2026-10-28 confirming a ransomware attack on a water utility or telecom operator using Warlock ransomware. |
| KKR-20261003-06 | 25% | 2026-11-05 | political | Between 2026-10-21 and 2026-10-28, a political scandal involving a US federal official will be reported by both the Guardian World and BBC World with a claim of misuse of public funds. | Both Guardian World and BBC World publish a report between 2026-10-21 and 2026-10-28 confirming a political scandal involving a US federal official, including a claim of misuse of public funds. |
| KKR-20261003-07 | 30% | 2026-11-05 | cyber | Between 2026-10-21 and 2026-10-28, a new cyberattack campaign targeting AI gateway services will be confirmed by The Hacker News with a report citing GitLab's AI Gateway vulnerability as the entry point. | The Hacker News publishes a report between 2026-10-21 and 2026-10-28 confirming a new cyberattack campaign targeting AI gateway services, citing GitLab's AI Gateway vulnerability as the entry point. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-28, the CISA KEV catalog will include CVE-2026-102490 and CVE-2026-102489 with a date-added value of 2026-10-" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-102489 dateAdded 2026-10-02, before the claimed window 2026-10-21..2026-10-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-28, the S&P 500 will close above 7,800 points on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-21 and 2026-10-28, a major flood event in Bangkok, Thailand, will be confirmed by GDACS Alerts with a green alert level and " → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3277 issued all-time across 18 forecaster arms · 2735 open (497 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 368 issued · 218 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

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
| lmstudio/realist | 161 | 156 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
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