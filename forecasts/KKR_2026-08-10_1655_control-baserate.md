**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 101655Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-10_1516.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260810-31 | 31% | 2026-10-05 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry with vendorProject Progress Software carrying a dateAdded value between 2026-08-10 and 2026-09-30. | TRUE if the CISA KEV catalog JSON contains at least one vulnerability record whose vendorProject field is Progress Software and whose dateAdded field falls between 2026-08-10 and 2026-09-30 inclusive. |
| KKR-20260810-32 | 31% | 2027-01-08 | cyber | LexisNexis Risk Solutions reports a data breach affecting 100000 or more individuals to the Maine Attorney General between 2026-08-11 and 2026-12-31. | TRUE if the Maine AG data breach notification database lists a filing by LexisNexis Risk Solutions or a LexisNexis entity, dated 2026-08-11 through 2026-12-31, with total affected of 100000 or more. |
| KKR-20260810-33 | 18% | 2026-12-02 | economics/markets | NYMEX front-month WTI crude settles at or below 72.00 dollars per barrel on at least one trading day between 2026-08-11 and 2026-11-30. | TRUE if CME official settlement data for the front-month NYMEX WTI light sweet crude contract shows a settlement price of 72.00 or lower on any trading day from 2026-08-11 through 2026-11-30. |
| KKR-20260810-34 | 18% | 2026-11-03 | economics/markets | NYMEX front-month WTI crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-08-11 and 2026-10-30. | TRUE if CME official settlement data for the front-month NYMEX WTI light sweet crude contract shows a settlement price of 100.00 or higher on any trading day from 2026-08-11 through 2026-10-30. |
| KKR-20260810-35 | 31% | 2026-10-05 | military/conflict | Iranian forces seize or forcibly board at least one commercial merchant vessel in the Strait of Hormuz or Gulf of Oman between 2026-08-11 and 2026-09-30. | TRUE if UKMTO issues an incident advisory describing an Iranian seizure or boarding of a merchant vessel in that area within the window and at least one of Reuters, AP, or AFP reports the same incident. |
| KKR-20260810-36 | 30% | 2026-11-04 | political | The Israeli cabinet or security cabinet formally approves the United States 15-point Gaza plan between 2026-08-11 and 2026-10-31. | TRUE if the Israeli Prime Minister Office or Government Press Office announces cabinet approval of that plan within the window and both Reuters and AP report the approval. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

456 issued all-time across 14 forecaster arms · 404 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 46 issued · 46 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 46 | 46 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 44 | 42 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 18 | 34 | 10 | 24 | 0.226 | 29.4% | 0.208 | -0.088 |
| manual/fable | 45 | 42 | 3 | 1 | 2 | 0.266 | 33.3% | 0.222 | -0.198 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*