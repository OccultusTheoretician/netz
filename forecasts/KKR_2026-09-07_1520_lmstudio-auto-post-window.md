**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-07_1518.md · forecaster: lmstudio/auto · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260907-01 | 45% | 2026-09-28 | economics/markets | Between 2026-09-21 and 2026-09-24, the S&P 500 closes above 7,800 points on at least one trading day. | The S&P 500 closes above 7,800 points on at least one trading day between 2026-09-21 and 2026-09-24, as reported by the Federal Reserve Economic Data (FRED) or Bloomberg. |
| KKR-20260907-02 | 25% | 2026-10-01 | political | Between 2026-09-21 and 2026-09-24, a new political party in Germany gains more than 10% of the vote in a regional election, as confirmed by official election results from the German Federal Returning Officer. | The German Federal Returning Officer publishes official election results showing a new political party receiving more than 10% of the vote in a regional election between 2026-09-21 and 2026-09-24. |
| KKR-20260907-03 | 20% | 2026-09-28 | cyber | Between 2026-09-21 and 2026-09-24, a new cyberattack targets a U.S. federal agency using a previously unpatched vulnerability, as confirmed by a CISA KEV entry and a government press release. | The CISA KEV catalog carries a new entry for a previously unpatched vulnerability exploited in a cyberattack against a U.S. federal agency, with a date-added value between 2026-09-21 and 2026-09-24, and a U.S. federal agency issues a public press release confirming the breach. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, at least one drone strike with reported casualties occurs in Kyiv, Ukraine, as confirmed by at least two " → REJECTED: resolution offers alternative VENUES joined by 'or' (…cisa kev catalog | or | major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-21 and 2026-09-24, a publicly disclosed cyberattack exploits a vulnerability in N-able's N-central software, leading to at l" → REJECTED: resolution offers alternative VENUES joined by 'or' (…government | or | critical infrastructure…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-21 and 2026-09-24, a new earthquake of magnitude 5.5 or higher occurs in Indonesia, with at least 100 people reported injure" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-21 and 2026-09-24, Iran issues a formal statement declaring a restricted zone in the Strait of Hormuz, as confirmed by both " → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-21 and 2026-09-24, a new data breach affects over 1 million users of a major cloud service provider, as confirmed by a publi" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-21 and 2026-09-24, a tropical storm or hurricane causes at least 100 fatalities in the United States, as confirmed by the Na" → REJECTED: resolution offers alternative VENUES joined by 'or' (…national weather service | or | noaa issues a final…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-21 and 2026-09-24, a major oil company reports a significant disruption in fuel supply due to conflict in the Strait of Horm" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

1613 issued all-time across 16 forecaster arms · 1348 open (90 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 227 issued · 139 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 484 | 456 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 227 | 139 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*