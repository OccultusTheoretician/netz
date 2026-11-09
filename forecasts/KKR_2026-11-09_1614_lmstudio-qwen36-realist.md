**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091614Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-09_1611.md · forecaster: lmstudio/qwen36-realist · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261109-08 | 25% | 2026-11-20 | cyber | The CISA KEV catalog carries a date-added value between 2026-11-09 and 2026-11-16 for a vulnerability with CVE identifier matching the SSHole flaw described in item 19. | True if the CISA KEV catalog lists the CVE with a date-added value within the window; False if the CVE is absent from the catalog by the deadline. |
| KKR-20261109-09 | 30% | 2026-11-20 | economics/markets | WTI Crude closes above 95.00 USD per barrel on at least one trading day between 2026-11-10 and 2026-11-17. | True if the closing price of WTI Crude exceeds 95.00 USD on any day in the window; False if it remains at or below 95.00 USD for the entire window. |
| KKR-20261109-10 | 40% | 2027-01-04 | political | The European Central Bank announces a new chief by 2026-12-31. | True if the ECB officially announces the appointment of a new chief by the deadline; False if no announcement is made by the deadline. |
| KKR-20261109-11 | 45% | 2026-11-20 | economics/markets | Nvidia stock closes below 110 USD per share on at least one trading day between 2026-11-10 and 2026-11-17. | True if Nvidia stock closes below 110 USD on any day in the window; False if it remains at or above 110 USD for the entire window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A major power outage affecting more than 100,000 customers is reported in the United States between 2026-11-10 and 2026-11-17." → REJECTED: cited items name Ethiopia, Solomon Islands; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…wire service | or | utility…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The US Department of Justice files an indictment against former OpenAI engineer Thomas Kohn between 2026-11-10 and 2026-11-17." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a federal court docket | or | doj press release confirms the filing of an i…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Russia launches a ballistic missile strike on Kyiv resulting in at least one confirmed civilian casualty between 2026-11-10 and 2026-11-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A magnitude 6.0 or greater earthquake occurs in Japan between 2026-11-10 and 2026-11-17." → REJECTED: cited items name Solomon Islands; the claim is about Japan — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "The UK House of Commons passes a motion of no confidence in the government between 2026-11-10 and 2026-11-17." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Iran closes the Strait of Hormuz to commercial shipping for more than 24 hours between 2026-11-10 and 2026-11-17." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count

## III. LEDGER STANDING

5485 issued all-time across 22 forecaster arms · 3763 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 171 issued · 138 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 115 | 115 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 195 | 178 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 190 | 188 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 171 | 138 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 500 | 385 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 356 | 342 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*