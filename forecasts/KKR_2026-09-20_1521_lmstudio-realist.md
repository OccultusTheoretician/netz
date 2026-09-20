**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-20_1517.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260920-09 | 35% | 2026-09-28 | economics/markets | On 2026-09-25, the S&P 500 will close below 7,500.00 points. | The closing price of the S&P 500 on 2026-09-25 will be less than 7,500.00 points, based on the official market close. |
| KKR-20260920-10 | 28% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-09-27, a military escalation in the Russia-Ukraine Theatre will result in a confirmed drone strike on Kyiv with at least one casualty. | At least one report from two hostile sides (RU, UA) will confirm a drone strike on Kyiv during the window, with at least one casualty reported in a corroborating source. |
| KKR-20260920-11 | 15% | 2026-10-07 | disaster | Between 2026-09-21 and 2026-09-27, a natural disaster in the U.S. will trigger a federal emergency declaration by the President. | The President of the United States will issue a federal emergency declaration for a natural disaster occurring in the U.S. between 2026-09-21 and 2026-09-27, as confirmed by a public statement from the White House. |
| KKR-20260920-12 | 40% | 2026-09-28 | economics/markets | On 2026-09-23, the 10-year U.S. Treasury yield will close above 5.10 percent. | The closing yield of the 10-year U.S. Treasury note on 2026-09-23 will be greater than 5.10 percent, based on the official market close. |
| KKR-20260920-13 | 22% | 2026-10-07 | political | Between 2026-09-21 and 2026-09-27, a political scandal involving a U.S. federal official will result in a formal indictment by a grand jury. | A U.S. federal grand jury will formally indict a sitting or former federal official for a crime related to official conduct, with the indictment publicly announced between 2026-09-21 and 2026-09-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-21, the CISA KEV catalog will carry a date-added value between 2026-09-15 and 2026-09-20 for a vulnerability exploited in a criti" → REJECTED: event window opens 2026-09-15, before this row is sealed (2026-09-20, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-21 and 2026-09-27, a missile strike from Iran will result in at least one confirmed casualty in the Israel-Gaza-Levant Theat" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-21 and 2026-09-27, a cyberattack targeting a U.S. financial institution will result in a public disclosure of data breach by" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-09-26, a major earthquake of magnitude 6.5 or higher will be recorded in the Pacific Ring of Fire, with at least one fatality report" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-26 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-21 and 2026-09-27, a cyberattack on a European government system will result in a public admission of compromise by the affe" → REJECTED: resolution offers alternative VENUES joined by 'or' (…-21 and 2026-09-27 via official press release | or | statement…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2559 issued all-time across 16 forecaster arms · 2093 open (164 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 96 issued · 91 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 876 | 791 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 309 | 159 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 96 | 91 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 141 | 131 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 299 | 282 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 277 | 229 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*