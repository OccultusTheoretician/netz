**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 301516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-30_1513.md · forecaster: lmstudio/qwen36-realist · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261030-07 | 15% | 2026-11-09 | economics | Reddit shares close below 100.00 on the NYSE between 2026-11-02 and 2026-11-06. | The closing price of Reddit (RDDT) on the NYSE falls below 100.00 on any trading day between 2026-11-02 and 2026-11-06. |
| KKR-20261030-08 | 25% | 2026-11-06 | disaster | The USGS reports a magnitude 6.0 or greater earthquake in the Pacific Ocean between 2026-11-01 and 2026-11-05. | The USGS Significant Quakes catalog lists an event with magnitude 6.0 or greater in the Pacific Ocean with a date between 2026-11-01 and 2026-11-05. |
| KKR-20261030-09 | 10% | 2026-11-16 | political | The UK Home Office issues a travel ban for a specific individual between 2026-11-01 and 2026-11-15. | The UK Home Office publishes a notice of a travel ban for a named individual on or before 2026-11-15. |
| KKR-20261030-10 | 20% | 2027-01-01 | economics | Binance confirms the recovery of more than 50 percent of the stolen assets from the October 2026 hack by 2026-12-31. | Binance issues a public statement confirming the recovery of more than 50 percent of the $6.3 billion stolen in the October 2026 hack on or before 2026-12-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-97229 between 2026-10-29 and 2026-11-05." → REJECTED: event window opens 2026-10-29, before this row is sealed (2026-10-30, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-97229 dateAdded 2026-10-29, already inside the claimed window 2026-10-29..2026-11-05
- "WTI Crude closes above 106.00 on the NYMEX on 2026-11-05." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A forest fire notification is issued by GDACS for Sudan between 2026-10-31 and 2026-11-04." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — green, yellow. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim
- "The European Central Bank appoints a new chief by 2026-11-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A Russian drone strike hits Kyiv between 2026-10-31 and 2026-11-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A ceasefire between Israel and Hamas is announced by Qatari mediators between 2026-11-01 and 2026-11-10." → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-11-11) is 1 day(s) after the window closes (2026-11-10). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days

## III. LEDGER STANDING

5161 issued all-time across 22 forecaster arms · 3439 open (590 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 135 issued · 102 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 23 | 23 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 143 | 126 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 138 | 136 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 135 | 102 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 467 | 352 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 297 | 283 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*