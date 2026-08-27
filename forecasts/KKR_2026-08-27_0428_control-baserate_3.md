**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270428Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-25_1517.md · forecaster: control/baserate · 4 accepted / 0 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-55 | 50% | 2026-10-05 | military/conflict | The government of Iran submits or publicly announces formal withdrawal from the Nuclear Non-Proliferation Treaty between 2026-08-26 and 2026-09-30. | TRUE if Iran files a withdrawal notice under NPT Article X or a wire service (Reuters, AP, AFP) reports such an announcement, dated between 2026-08-26 and 2026-09-30; else FALSE. |
| KKR-20260827-56 | 29% | 2026-10-02 | political | A New York state court issues any order or ruling, including on a preliminary motion, in the business-group lawsuit against the city-owned grocery store initiative, between 2026-08-26 and 2026-09-30. | TRUE if the case docket in the New York court e-filing system shows a judicial order or ruling entered between 2026-08-26 and 2026-09-30 in this case; FALSE if no order is entered. |
| KKR-20260827-57 | 31% | 2026-09-11 | crime/security | A named law-enforcement agency (Europol, FBI, or a national police force) announces additional arrests connected to the global cybercrime crackdown, between 2026-08-26 and 2026-09-08. | TRUE if Europol, the FBI, or a national police agency issues a press release naming additional arrests tied to this operation, dated 2026-08-26 through 2026-09-08; FALSE if no such release appears. |
| KKR-20260827-58 | 33% | 2026-09-10 | disaster | GDACS raises tropical cyclone JULIO-26 from Green to Orange or Red alert level before the system is marked dissipated, between 2026-08-26 and 2026-09-08. | TRUE if the GDACS event page for JULIO-26 shows an Orange or Red alert level at any point between 2026-08-26 and 2026-09-08; FALSE if it stays Green or is closed without upgrade. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

981 issued all-time across 14 forecaster arms · 891 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 222 issued · 214 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 222 | 214 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 114 | 114 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*