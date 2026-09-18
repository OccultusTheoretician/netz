**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181522Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-18_1518.md · forecaster: lmstudio/realist · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260918-08 | 30% | 2026-10-01 | military/conflict | Between 2026-09-18 and 2026-09-25, no reported casualties will be confirmed in any military or conflict event in the Russia-Ukraine Theatre. | No third-party corroboration from at least two independent sources (e.g., BBC World, Al Jazeera, Reuters) confirms any casualties in any event in the Russia-Ukraine Theatre between 2026-09-18 and 2026-09-25. |
| KKR-20260918-09 | 45% | 2026-09-28 | economics/markets | Between 2026-09-18 and 2026-09-25, the 10-year Treasury yield will exceed 5.10 percent on at least one weekday. | The 10-year Treasury yield exceeds 5.10 percent on at least one weekday between 2026-09-18 and 2026-09-25. |
| KKR-20260918-10 | 25% | 2026-10-01 | cyber | Between 2026-09-18 and 2026-09-25, a cyberattack exploiting CVE-2025-39964 will be confirmed by at least two independent sources. | At least two independent sources (e.g., BleepingComputer, The Hacker News, CISA Advisories) confirm a cyberattack exploiting CVE-2025-39964 between 2026-09-18 and 2026-09-25. |
| KKR-20260918-11 | 15% | 2026-10-01 | disaster | Between 2026-09-18 and 2026-09-25, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in any region. | The USGS Significant Quakes catalog records a magnitude 6.5 or higher earthquake in any region between 2026-09-18 and 2026-09-25. |
| KKR-20260918-12 | 35% | 2026-10-01 | political | Between 2026-09-18 and 2026-09-25, a new political scandal involving a U.S. federal official will be confirmed by at least two independent sources. | At least two independent sources (e.g., Guardian World, CNBC Top News, NPR News) confirm a new political scandal involving a U.S. federal official between 2026-09-18 and 2026-09-25. |
| KKR-20260918-13 | 20% | 2026-10-01 | cyber | Between 2026-09-18 and 2026-09-25, a new cyberattack targeting Microsoft 365 will be confirmed by at least two independent sources. | At least two independent sources (e.g., BleepingComputer, The Hacker News) confirm a new cyberattack targeting Microsoft 365 between 2026-09-18 and 2026-09-25. |
| KKR-20260918-14 | 30% | 2026-10-01 | disaster | Between 2026-09-18 and 2026-09-25, a new flood warning will be issued by the USGS or GDACS for a region in the United States. | The USGS Significant Quakes or GDACS Alerts catalog issues a new flood warning for a region in the United States between 2026-09-18 and 2026-09-25. |
| KKR-20260918-15 | 25% | 2026-10-01 | political | Between 2026-09-18 and 2026-09-25, a new political resignation or indictment involving a senior official in the European Union will be confirmed by at least two independent sources. | At least two independent sources (e.g., Guardian World, BBC World, Al Jazeera) confirm a new political resignation or indictment involving a senior EU official between 2026-09-18 and 2026-09-25. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-18 and 2026-09-25, the CISA KEV catalog will include CVE-2025-39964 and CVE-2026-53266 with a date-added value of 2026-09-18" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-53266 dateAdded 2026-09-18, already inside the claimed window 2026-09-18..2026-09-25
- "Between 2026-09-18 and 2026-09-25, the S&P 500 will close above 7,650 on at least one weekday." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2454 issued all-time across 16 forecaster arms · 1988 open (103 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 89 issued · 84 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 835 | 750 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 293 | 143 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 89 | 84 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 131 | 121 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 283 | 266 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 262 | 214 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*