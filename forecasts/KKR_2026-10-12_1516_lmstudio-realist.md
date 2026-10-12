**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: lmstudio/realist · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-07 | 30% | 2026-10-23 | cyber | On 2026-10-15, the CISA KEV catalog will include at least one vulnerability with a CVSS score of 10.0 that has been exploited in at least three distinct public attacks between 2026-10-12 and 2026-10-18. | The CISA KEV catalog will carry a date-added value between 2026-10-12 and 2026-10-18 for a vulnerability with a CVSS score of 10.0 that has been exploited in at least three distinct public attacks, as confirmed by at least two independent sources (e.g., BleepingComputer, The Hacker News, or CISA advisories). |
| KKR-20261012-08 | 30% | 2026-10-23 | military/conflict | Between 2026-10-15 and 2026-10-21, at least one major military strike will be confirmed by cross-bias corroboration (Grade A or B) in the Russia-Ukraine Theatre, involving the use of a cruise missile or drone, resulting in at least one casualty. | At least one military strike in the Russia-Ukraine Theatre between 2026-10-15 and 2026-10-21, involving a cruise missile or drone, will be confirmed by cross-bias corroboration (Grade A or B) and result in at least one casualty, as verified by at least two independent sources (e.g., Al Jazeera, BBC World, Guardian World). |
| KKR-20261012-09 | 20% | 2026-10-20 | political | On 2026-10-17, the U.S. Department of State will issue a formal statement condemning Iran for threatening to disrupt maritime traffic in the Strait of Hormuz, citing a prior intelligence assessment. | The U.S. Department of State will issue a formal statement on or before 2026-10-17 condemning Iran for threatening to disrupt maritime traffic in the Strait of Hormuz, referencing a prior intelligence assessment, as confirmed by a transcript on the State Department website. |
| KKR-20261012-10 | 45% | 2026-10-22 | disaster | On 2026-10-19, the U.S. Federal Aviation Administration will issue a new safety advisory for flights over Saudi Arabia, citing increased risk from Houthi attacks, as published in the FAA's official advisory database. | The FAA's official advisory database will publish a new safety advisory for flights over Saudi Arabia on or before 2026-10-19, citing increased risk from Houthi attacks, as confirmed by the FAA's official website. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-13 and 2026-10-19, at least one major financial institution in the United States will publicly disclose a cyberattack result" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively; the resolution names a different subject than the statement — the claim is about States, United and the resolution settles on 8-k, Bloomberg, Form, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "On 2026-10-18, the S&P 500 will close below 7,750.00, based on the market close on that date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-18 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-10-14 and 2026-10-20, the Brent crude oil price will exceed $110.00 per barrel at the close of any trading day, based on the IC" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "On 2026-10-16, the U.S. Federal Reserve will announce a 25 basis point increase in the federal funds rate, as reported by the Federal Reserv" → REJECTED: cited items name United Kingdom; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-14 and 2026-10-20, at least one country in the European Union will announce new sanctions against Russia related to the war " → REJECTED: cited items name China; the claim is about Russian Federation, Ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-10-15 and 2026-10-21, at least one major cyberattack will be reported by a U.S. federal agency or a major news outlet as target" → REJECTED: resolution offers alternative VENUES joined by 'or' (…u.s. federal agency | or | a major…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3944 issued all-time across 21 forecaster arms · 2916 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 215 issued · 171 open · 43 resolved · 29 hits / 14 misses · **Brier 0.350** against its own base rate 67.4% (climatological 0.220) · **skill -0.592**.

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
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
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