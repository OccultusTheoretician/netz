**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 042115Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-04_1502.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260804-56 | 52% | 2026-08-25 | military_conflict | Between 2026-08-04 and 2026-08-21 the United States and Iran both publicly announce a concluded agreement reopening the Strait of Hormuz to commercial transit. | TRUE if a US government body and an Iranian government body each publicly confirm a concluded Hormuz transit agreement dated between 2026-08-04 and 2026-08-21, per two international wire services. |
| KKR-20260804-57 | 45% | 2026-08-31 | military_conflict | Between 2026-08-05 and 2026-08-25 a single long-range strike incident in Ukraine kills ten or more people. | TRUE if Ukrainian state emergency or prosecution authorities report ten or more killed in one strike incident dated in the window, corroborated by two international wire services. |
| KKR-20260804-58 | 28% | 2026-10-02 | economic | The S&P 500 closes down 3.00 percent or more from the prior close on at least one session between 2026-08-05 and 2026-09-30. | TRUE if official S&P 500 closing values show a single-session close-to-close decline of 3.00 percent or greater on any date between 2026-08-05 and 2026-09-30. |
| KKR-20260804-59 | 18% | 2026-11-03 | cyber | The CISA KEV catalog adds a further N-able N-central vulnerability with a date-added value between 2026-08-05 and 2026-10-31. | TRUE if the CISA KEV catalog contains an N-able N-central CVE other than CVE-2026-18577 and CVE-2026-18556 carrying a dateAdded value between 2026-08-05 and 2026-10-31. |
| KKR-20260804-60 | 85% | 2026-10-20 | political | The United States Senate confirms Todd Blanche as Attorney General in a recorded floor vote held between 2026-08-05 and 2026-10-16. | TRUE if a Congress.gov Senate roll call vote dated between 2026-08-05 and 2026-10-16 records confirmation of the Blanche nomination to be Attorney General. |
| KKR-20260804-61 | 84% | 2026-10-05 | crime_security | The man charged over the largest 2026 Washington state wildfire faces at least one arson count filed and not dismissed at any point between 2026-08-05 and 2026-09-30. | TRUE if the Washington state court docket for that defendant shows an arson count filed and not dismissed on a date between 2026-08-05 and 2026-09-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Front-month ICE Brent crude settles at or below USD 70.00 per barrel on at least one trading session between 2026-08-05 and 2026-09-30." → REJECTED: resolution names alternative venues joined by 'or' — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The FOMC leaves the federal funds target range at 3.50 to 3.75 percent at its scheduled 2026-09-16 decision." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Federal defendants file a notice of appeal of the ruling blocking the New York ban on ICE officers wearing masks, docketed between 2026-08-0" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "GDACS carries a tropical cyclone alert for Dolphin at orange or red level listing Japan among affected countries between 2026-08-04 and 2026" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

316 issued all-time across 14 forecaster arms · 278 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 25 issued · 25 open · nothing resolved yet — this arm earns a score at its first resolution.

*11 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 15 | 15 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 26 | 26 | 7 | 19 | 0.228 | 26.9% | 0.197 | -0.160 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 25 | 25 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*