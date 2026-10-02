**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021523Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-02_1519.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261002-08 | 30% | 2026-10-16 | military/conflict | Between 2026-10-03 and 2026-10-09, at least one drone strike with reported casualties occurs in Kyiv, Ukraine, as confirmed by at least two independently biased sources (RU, UA) reporting the same incident with casualty figures. | The CISA KEV catalog carries a date-added value between 2026-10-01 and 2026-10-09, and the event is corroborated by at least two sources from different hostile sides (RU, UA) reporting the same incident with casualty figures. |
| KKR-20261002-09 | 40% | 2026-10-20 | economics/markets | Between 2026-10-08 and 2026-10-15, the UK diesel price exceeds £2.10 per litre, as reported by the Guardian World and BBC World. | The Guardian World and BBC World report the UK diesel price exceeding £2.10 per litre on a weekday between 2026-10-08 and 2026-10-15. |
| KKR-20261002-10 | 20% | 2026-10-22 | cyber | Between 2026-10-10 and 2026-10-17, a cyberattack using autonomous AI agents targets a U.S. federal government website, confirmed by BleepingComputer and The Hacker News. | BleepingComputer and The Hacker News report a cyberattack using autonomous AI agents targeting a U.S. federal government website between 2026-10-10 and 2026-10-17. |
| KKR-20261002-11 | 30% | 2026-10-23 | political | Between 2026-10-11 and 2026-10-18, France's parliament passes a new housing decree, as confirmed by Al Jazeera and BBC World. | Al Jazeera and BBC World report that France's parliament passes a new housing decree between 2026-10-11 and 2026-10-18. |
| KKR-20261002-12 | 15% | 2026-10-25 | disaster | Between 2026-10-12 and 2026-10-19, a major earthquake of magnitude 5.0 or higher occurs in the Pacific Northwest, as reported by USGS Significant Quakes. | The USGS Significant Quakes catalog reports an earthquake of magnitude 5.0 or higher in the Pacific Northwest between 2026-10-12 and 2026-10-19. |
| KKR-20261002-13 | 25% | 2026-10-26 | political | Between 2026-10-13 and 2026-10-20, Iran announces a new nuclear agreement with the UN, as confirmed by both AXIS and WEST sources. | Both AXIS and WEST sources report Iran announcing a new nuclear agreement with the UN between 2026-10-13 and 2026-10-20. |
| KKR-20261002-14 | 35% | 2026-10-28 | cyber | Between 2026-10-14 and 2026-10-21, a major cyberattack on a critical infrastructure system in Europe is confirmed by CISA KEV and BleepingComputer. | The CISA KEV catalog and BleepingComputer report a cyberattack on a critical infrastructure system in Europe between 2026-10-14 and 2026-10-21. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-05 and 2026-10-12, the S&P 500 closes above 7,800 on a weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-06 and 2026-10-13, a zero-day exploit in Fortinet FortiMail (CVE-2026-104286) is used in a cyberattack against a government " → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104286 dateAdded 2026-10-01, before the claimed window 2026-10-06..2026-10-13; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-07 and 2026-10-14, a major flood event in the United States results in at least 100,000 displaced persons, as reported by tw" → REJECTED: the resolution names a different subject than the statement — the claim is about Guardian, NPR, States, United and the resolution settles on Alerts, GDACS, Guardian, NPR. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3232 issued all-time across 18 forecaster arms · 2690 open (391 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 161 issued · 156 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1154 | 1037 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 361 | 211 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 161 | 156 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 239 | 222 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 64 | 64 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*