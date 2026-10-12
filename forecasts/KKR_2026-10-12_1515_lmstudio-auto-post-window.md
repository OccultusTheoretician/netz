**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121515Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-01 | 25% | 2026-10-28 | cyber | Between 2026-10-21 and 2026-10-24, a cyberattack exploiting the CVSS 10.0 Bricksforge WordPress vulnerability will be confirmed by at least two independent sources (e.g., BleepingComputer, The Hacker News) with evidence of exploitation. | The CISA KEV catalog carries a date-added value between 2026-10-21 and 2026-10-24, and at least two independent sources (e.g., BleepingComputer, The Hacker News) report active exploitation of the Bricksforge WordPress vulnerability (CVE-2026-XXXX) with unauthenticated remote code execution. |
| KKR-20261012-02 | 15% | 2026-10-28 | disaster | Between 2026-10-21 and 2026-10-24, a major earthquake of magnitude 6.0 or higher will be recorded by USGS in the Pacific region, with a depth of less than 100 km. | The USGS Significant Quakes feed records a magnitude 6.0 or higher earthquake in the Pacific region (latitude ±30, longitude ±180) with depth less than 100 km, and the event is confirmed by at least two independent sources (e.g., Al Jazeera, BBC World) within the window. |
| KKR-20261012-03 | 20% | 2026-10-28 | cyber | Between 2026-10-21 and 2026-10-24, a new cyberattack on a U.S. financial institution will result in a system outage lasting over 24 hours, confirmed by at least two independent sources. | The CISA KEV catalog carries a date-added value between 2026-10-21 and 2026-10-24, and at least two independent sources (e.g., BleepingComputer, CNBC Top News) confirm a cyberattack on a U.S. financial institution causing a system outage lasting more than 24 hours. |
| KKR-20261012-04 | 35% | 2026-10-29 | economics/markets | Between 2026-10-21 and 2026-10-24, a new oil price surge will occur, with Brent crude exceeding $115 per barrel, confirmed by a market close on a weekday. | The Brent crude oil price, as reported by the CME Group, exceeds $115.00 per barrel on a weekday market close between 2026-10-21 and 2026-10-24. |
| KKR-20261012-05 | 40% | 2026-10-28 | political | Between 2026-10-21 and 2026-10-24, a new political scandal involving a U.S. federal official will be confirmed by at least two independent sources, with a public indictment or resignation. | At least two independent sources (e.g., BBC World, Guardian World) confirm a public indictment or resignation of a U.S. federal official related to a political scandal, with the event occurring between 2026-10-21 and 2026-10-24. |
| KKR-20261012-06 | 20% | 2026-10-28 | military/conflict | Between 2026-10-21 and 2026-10-24, a new military escalation in the Russia-Ukraine conflict will be confirmed by at least two independently biased sources (RU, UA, WEST), with a reported casualty count of 10 or more. | At least two independently biased sources (RU, UA, WEST) confirm a new military escalation in the Russia-Ukraine conflict (e.g., missile, drone, cruise attack) with a reported casualty count of 10 or more, and the event occurs between 2026-10-21 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, a drone attack targeting Kyiv, Ukraine, will be confirmed by at least two independently biased sources (U" → REJECTED: cited items name Australia, Mozambique; the claim is about Ukraine, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, a new terrorist attack in the Middle East will be confirmed by at least two independently biased sources " → REJECTED: cited items name Russian Federation, United Kingdom; the claim is about Palestine, State of, zone:israel_gaza — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, a new cyberattack on a critical infrastructure system in Europe will be confirmed by at least two indepen" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-21 and 2026-10-24, a new natural disaster in the U.S. will be confirmed by at least two independent sources (e.g., NWS, GDAC" → REJECTED: cited items name France, Panama; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3940 issued all-time across 21 forecaster arms · 2912 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 413 issued · 197 open · 207 resolved · 61 hits / 146 misses · **Brier 0.209** against its own base rate 29.5% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1399 | 1125 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 167 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 320 | 264 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 149 | 145 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*