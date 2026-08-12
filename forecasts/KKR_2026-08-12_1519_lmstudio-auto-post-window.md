**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121519Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-12_1518.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260812-01 | 32% | 2026-08-22 | disaster | A major earthquake of magnitude 6.0 or higher occurs in the South Sandwich Islands region between 2026-08-13 and 2026-08-19, with a depth of less than 50km. | The USGS Significant Quakes database records an event with magnitude ≥6.0, depth <50km, and location within the South Sandwich Islands region between 2026-08-13 and 2026-08-19. |
| KKR-20260812-02 | 38% | 2026-08-22 | cyber | A cyberattack exploiting the vulnerability CVE-2026-20349 in Cisco Secure Firewall ASA/FTD is confirmed by two independent sources (e.g., BleepingComputer, The Hacker News) between 2026-08-13 and 2026-08-19. | Two independent, non-aligned sources (e.g., BleepingComputer, The Hacker News) report a confirmed exploitation of CVE-2026-20349 in Cisco Secure Firewall ASA/FTD between 2026-08-13 and 2026-08-19. |
| KKR-20260812-03 | 26% | 2026-08-22 | cyber | A coordinated cyberattack targeting U.S. water utilities is confirmed by two independent sources (e.g., NPR News, CISA) between 2026-08-13 and 2026-08-19. | Two independent sources (e.g., NPR News, CISA) report a confirmed cyberattack targeting U.S. water utilities between 2026-08-13 and 2026-08-19. |
| KKR-20260812-04 | 30% | 2026-08-22 | military/conflict | A major offensive operation by Iran or its proxies in the Israel-Gaza-Levant theatre is confirmed by two hostile sides (IL, PS, AXIS) between 2026-08-13 and 2026-08-19. | Two hostile sides (IL, PS, or AXIS) confirm a major offensive operation in the Israel-Gaza-Levant theatre between 2026-08-13 and 2026-08-19, with at least one dedicated report from each side. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A drone strike targeting a military installation in Novorossiysk, Russia, occurs between 2026-08-13 and 2026-08-19, resulting in at least on" → REJECTED: the resolution names a different subject than the statement — the claim is about Novorossiysk, Russia and the resolution settles on AXIS, BBC, Jazeera, RU. A row whose resolution checks a different fact can be scored correct while being wrong
- "The CISA KEV catalog will include a new entry for CVE-2026-72898 with a date-added value between 2026-08-12 and 2026-08-18." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-72898 dateAdded 2026-08-11, before the claimed window 2026-08-12..2026-08-18; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The S&P 500 index closes above 7,800.00 on a weekday between 2026-08-19 and 2026-08-26." → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-08-27) is 1 day(s) after the window closes (2026-08-26). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "A political scandal involving a U.S. cabinet member is confirmed by two major wire services (e.g., Reuters, AP) between 2026-08-13 and 2026-" → REJECTED: the resolution names a different subject than the statement — the claim is about AP, Reuters and the resolution settles on Associated, Press, Reuters, Two. A row whose resolution checks a different fact can be scored correct while being wrong
- "A wildfire in Australia is confirmed by GDACS Alerts as active and affecting at least 10,000 hectares between 2026-08-13 and 2026-08-19." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green, yellow. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "The U.S. Federal Reserve announces a 0.25 percentage point interest rate hike between 2026-08-19 and 2026-08-26, confirmed by a machine-read" → REJECTED: resolution offers alternative VENUES joined by 'or' (…the federal reserve's official website | or | fred records a confirmed announcement of a 0…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-08-27) is 1 day(s) after the window closes (2026-08-26). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days

## III. LEDGER STANDING

521 issued all-time across 14 forecaster arms · 465 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 57 issued · 55 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 72 | 72 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 57 | 55 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 39 | 39 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*