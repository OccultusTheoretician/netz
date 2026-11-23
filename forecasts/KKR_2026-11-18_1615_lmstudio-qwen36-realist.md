**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181615Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-18_1613.md · forecaster: lmstudio/qwen36-realist · 6 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261118-11 | 90% | 2026-11-23 | cyber | The CISA KEV catalog carries a date-added value for CVE-2026-114938 between 2026-11-18 and 2026-11-21. | The CISA KEV catalog lists CVE-2026-114938 with a date-added value falling within the window 2026-11-18 to 2026-11-21. |
| KKR-20261118-12 | 85% | 2026-11-25 | political | Hakeem Jeffries is elected Speaker of the House of Representatives between 2026-11-20 and 2026-11-23. | A roll call vote recorded on Congress.gov confirms Hakeem Jeffries received a majority of votes cast for Speaker of the House between 2026-11-20 and 2026-11-23. |
| KKR-20261118-13 | 20% | 2026-11-26 | political | The ICJ issues a ruling on the Rohingya genocide case against Myanmar between 2026-11-20 and 2026-11-24. | The International Court of Justice publishes a judgment document regarding the Rohingya genocide case against Myanmar with a date between 2026-11-20 and 2026-11-24. |
| KKR-20261118-14 | 25% | 2026-11-26 | disaster | The USGS Significant Quakes catalog records an earthquake of magnitude 6.0 or greater between 2026-11-20 and 2026-11-24. | The USGS Significant Quakes catalog records an event with a magnitude of 6.0 or greater with a date between 2026-11-20 and 2026-11-24. |
| KKR-20261118-15 | 60% | 2026-11-26 | political | Jensen Huang appears before the Senate Banking Committee between 2026-11-20 and 2026-11-24. | A Senate Banking Committee hearing transcript or schedule confirms Jensen Huang testified or appeared before the committee on a date between 2026-11-20 and 2026-11-24. |
| KKR-20261118-16 | 30% | 2026-11-26 | political | The EU formally approves the €45 billion loan to Ukraine between 2026-11-20 and 2026-11-24. | The European Union publishes an official decision or press release formally approving the €45 billion loan to Ukraine with a date between 2026-11-20 and 2026-11-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI Crude closes above $85.00 per barrel on 2026-11-24." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "North Korea conducts a nuclear test between 2026-11-20 and 2026-11-24." → REJECTED: resolution offers alternative VENUES joined by 'or' (… nuclear-test-ban treaty organization (ctbto) | or | the usgs significant quakes catalog records a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about Korea, North and the resolution settles on Ban, CTBTO, Comprehensive, Nuclear. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

5853 issued all-time across 23 forecaster arms · 4131 open (1972 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36-realist`:** 225 issued · 192 open · 31 resolved · 10 hits / 21 misses · **Brier 0.242** against its own base rate 32.3% (climatological 0.219) · **skill -0.106**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 227 | 227 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 241 | 224 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 234 | 232 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 225 | 192 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 29 | 29 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*