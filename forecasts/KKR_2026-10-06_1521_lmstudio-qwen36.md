**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061521Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: lmstudio/qwen36 · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-10 | 30% | 2026-10-26 | economics | WTI Crude oil closes below 80.00 USD per barrel on the NYMEX settlement date between 2026-10-20 and 2026-10-23. | The NYMEX WTI Crude settlement price on any date between 2026-10-20 and 2026-10-23 is strictly less than 80.00 USD. |
| KKR-20261006-11 | 25% | 2026-10-24 | military_conflict | Ukraine launches a drone attack resulting in confirmed casualties in Moscow between 2026-10-15 and 2026-10-22. | Two independent hostile sides report confirmed casualties from a Ukrainian drone attack in Moscow within the event window. |
| KKR-20261006-12 | 35% | 2026-10-19 | disaster | Kenya confirms a second Ebola death between 2026-10-10 and 2026-10-17. | The WHO or Kenya Ministry of Health confirms a second Ebola death in Kenya within the event window. |
| KKR-20261006-13 | 20% | 2026-10-29 | political | The European Union formally adopts a 15-year probation period for new member states as part of its enlargement policy between 2026-10-20 and 2026-10-27. | The EU Council or Commission publishes a formal legislative act or official communication establishing a 15-year probation period for new member states. |
| KKR-20261006-14 | 40% | 2026-10-19 | economics | Anduril Industries receives a final Navy contract award exceeding 2.9 billion USD for a submarine shipyard project between 2026-10-10 and 2026-10-17. | The US Department of Defense publishes a contract award notice for Anduril Industries exceeding 2.9 billion USD for a submarine shipyard project. |
| KKR-20261006-15 | 25% | 2026-11-07 | economics | The US Federal Reserve announces a rate cut of at least 25 basis points at its meeting between 2026-10-29 and 2026-11-05. | The Federal Reserve announces a rate cut of at least 25 basis points at its meeting between 2026-10-29 and 2026-11-05. |
| KKR-20261006-16 | 30% | 2026-10-19 | disaster | A significant earthquake (magnitude 6.0 or higher) occurs in Indonesia between 2026-10-10 and 2026-10-17. | The USGS or EMSC reports a magnitude 6.0 or higher earthquake in Indonesia within the event window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value between 2026-10-06 and 2026-10-13 for a critical remote code execution vulnerability in Reje" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A major cyberattack disrupts the operations of a top-tier US bank between 2026-10-15 and 2026-10-22." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "France implements a nationwide school closure for more than one day between 2026-10-10 and 2026-10-17." → REJECTED: the resolution names a different subject than the statement — the claim is about France and the resolution settles on Education, French, Ministry. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3477 issued all-time across 21 forecaster arms · 2663 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 9 issued · 9 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1242 | 1041 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*