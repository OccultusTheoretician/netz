**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 221748Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-22_1518.md · forecaster: manual/opus-5/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260922-26 | 52% | 2026-10-27 | cyber | The CISA KEV catalog carries at least one entry whose vendorProject or product field names VeloCloud or SD-WAN Orchestrator, with a dateAdded value between 2026-09-23 and 2026-10-23. | TRUE if the CISA KEV catalog JSON contains a record whose vendorProject or product names VeloCloud or SD-WAN Orchestrator with dateAdded between 2026-09-23 and 2026-10-23 inclusive; otherwise FALSE. |
| KKR-20260922-27 | 28% | 2026-12-18 | cyber | The CISA KEV catalog carries at least one entry with vendorProject D-Link and a dateAdded value between 2026-09-23 and 2026-12-15. | TRUE if the CISA KEV catalog JSON contains a record with vendorProject D-Link and dateAdded between 2026-09-23 and 2026-12-15 inclusive; otherwise FALSE. |
| KKR-20260922-28 | 80% | 2026-11-04 | economic | The S&P 500 sets a new all-time closing high on at least one session between 2026-09-23 and 2026-10-30. Reference: 7,764.88 close on the packet date, up 2.36 percent. | TRUE if S&P 500 daily close data show a close above the all-time closing high standing on 2026-09-22, on any session from 2026-09-23 through 2026-10-30; otherwise FALSE. |
| KKR-20260922-29 | 22% | 2027-01-06 | economic | Front-month Brent crude settles at or above 120.00 US dollars a barrel on at least one trading day between 2026-09-23 and 2026-12-31. Reference: 100.03 on the packet date. | TRUE if ICE front-month Brent settlement data show a settlement at or above 120.00 on any trading day from 2026-09-23 through 2026-12-31; otherwise FALSE. |
| KKR-20260922-30 | 45% | 2026-12-03 | economic | Front-month WTI crude settles below 75.00 US dollars a barrel on at least one trading day between 2026-09-23 and 2026-11-30. Reference: 91.16 on the packet date, down 10.55 percent. | TRUE if NYMEX front-month WTI settlement data show a settlement below 75.00 on any trading day from 2026-09-23 through 2026-11-30; otherwise FALSE. |
| KKR-20260922-31 | 18% | 2026-12-22 | military_conflict | Russia and Ukraine both publicly confirm a mutual halt on strikes against each other's energy infrastructure, announced between 2026-09-23 and 2026-12-18. | TRUE if statements from both the Russian and Ukrainian governments, reported by Reuters and AP, confirm a mutual moratorium on energy-infrastructure strikes announced inside the window; otherwise FALSE. |
| KKR-20260922-32 | 62% | 2026-12-04 | military_conflict | A single incident or single-day battle in Yemen kills 100 or more people, combatant or civilian, between 2026-09-23 and 2026-11-30. | TRUE if Reuters or AP, and Al Jazeera, both report a single Yemen incident or single-day battle inside the window with a death toll of 100 or more; otherwise FALSE. |
| KKR-20260922-33 | 70% | 2026-12-11 | political | Democrats win at least 218 seats in the US House of Representatives in the general election held 2026-11-03. | TRUE if AP race calls as of the deadline show Democrats winning 218 or more House seats in the 2026-11-03 general election; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "FRED series DGS10 prints at or above 5.25 percent on at least one business day between 2026-09-23 and 2026-12-31. Reference: 4.96 percent on" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The NOAA CPC Oceanic Nino Index table carries a Sep-Oct-Nov 2026 seasonal value at or above plus 2.0 degrees Celsius." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

2689 issued all-time across 16 forecaster arms · 2223 open (193 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 320 issued · 303 open · 7 resolved · 5 hits / 2 misses · **Brier 0.137** against its own base rate 71.4% (climatological 0.204) · **skill +0.329** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 926 | 841 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 324 | 174 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 103 | 98 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 164 | 154 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 320 | 303 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 291 | 243 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*