**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-28_1515.md · forecaster: lmstudio/qwen36-realist · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261028-08 | 15% | 2026-12-01 | political | The UK government publishes legislation or statutory instrument that formally increases the defense spending target to 2.5 percent of GDP. | A UK government publication or Hansard record confirms the formal defense spending target is raised to 2.5 percent of GDP. |
| KKR-20261028-09 | 20% | 2026-11-09 | political | The Federal Election Commission (FEC) website is offline for more than 48 continuous hours between 2026-11-01 and 2026-11-07. | Public monitoring confirms the FEC website is inaccessible for more than 48 continuous hours. |
| KKR-20261028-10 | 35% | 2026-12-13 | political | The US Congress passes a continuing resolution to fund the federal government past 2026-12-11. | The US Congress passes a continuing resolution to fund the federal government past 2026-12-11. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for CVE-2026-48356 between 2026-10-28 and 2026-11-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-48356 dateAdded 2026-10-27, before the claimed window 2026-10-28..2026-11-04; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Wendy's shares close above $140 on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A magnitude 6.0 or greater earthquake occurs in the Reykjanes Ridge region between 2026-11-01 and 2026-11-07." → REJECTED: resolution offers alternative VENUES joined by 'or' (…usgs | or | gdacs…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Brent crude oil closes below $105 per barrel on at least one trading day between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A major airline grounded its entire fleet in Australia due to a safety or regulatory issue between 2026-11-01 and 2026-11-07." → REJECTED: cited items name Cambodia; the claim is about Australia — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "A new critical vulnerability with a CVSS score of 9.0 or higher is added to the CISA KEV catalog between 2026-11-01 and 2026-11-07." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Spain announces a formal inquiry into the high-speed train crash with findings released between 2026-11-01 and 2026-11-07." → REJECTED: the resolution names a different subject than the statement — the claim is about Spain and the resolution settles on Spanish. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

5090 issued all-time across 21 forecaster arms · 3368 open (448 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 129 issued · 96 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 132 | 115 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 130 | 128 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 129 | 96 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 455 | 340 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 286 | 272 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*