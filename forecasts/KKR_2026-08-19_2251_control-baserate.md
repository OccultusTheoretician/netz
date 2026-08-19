**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192251Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-19_1519.md · forecaster: control/baserate · 8 accepted / 0 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260819-27 | 23% | 2026-10-02 | cyber | CISA adds at least one new Microsoft-product vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-08-20 and 2026-09-30. | The CISA KEV JSON feed contains at least one entry with vendorProject Microsoft and dateAdded between 2026-08-20 and 2026-09-30 inclusive; zero such entries grades MISS. |
| KKR-20260819-28 | 25% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-20 and 2026-10-30. | The official ICE Brent front-month settlement price is at or above 100.00 USD on any trading day from 2026-08-20 through 2026-10-30; otherwise MISS. |
| KKR-20260819-29 | 25% | 2027-01-05 | economics/markets | The US 10-year Treasury constant maturity yield closes at or above 5.00 percent on at least one day between 2026-08-20 and 2026-12-31. | FRED series DGS10 records a value at or above 5.00 for at least one date between 2026-08-20 and 2026-12-31; otherwise MISS. |
| KKR-20260819-30 | 50% | 2026-09-23 | military/conflict | At least one missile or drone strike on United Arab Emirates territory attributed to Iran or Iran-aligned forces occurs between 2026-08-20 and 2026-09-20. | At least two of Reuters, AP, AFP, or BBC report a strike on UAE territory within the window attributed to Iran or Iran-aligned forces; no machine-readable register exists for this class. |
| KKR-20260819-31 | 29% | 2026-12-02 | political | Voting in Palestinian national legislative or presidential elections takes place on at least one day between 2026-11-01 and 2026-11-30. | At least two of Reuters, AP, AFP, or Al Jazeera report ballots cast in Palestinian national elections within the window; postponement or cancellation grades MISS. |
| KKR-20260819-32 | 29% | 2027-01-05 | political | A Federal Register document published between 2026-08-20 and 2026-12-31 imposes a 50 percent tariff on a broad class of Canadian imports. | Federalregister.gov contains a presidential proclamation or agency notice published within the window that imposes a 50 percent tariff rate on Canadian imports broadly; otherwise MISS. |
| KKR-20260819-33 | 31% | 2027-02-03 | crime/security | At least one of the two Ukrainian nationals arrested in August 2026 over the Nord Stream sabotage enters German custody between 2026-08-20 and 2027-01-31. | At least two of Reuters, AP, AFP, or DW report the transfer of either suspect to German custody within the window; a German federal court docket entry also suffices. |
| KKR-20260819-34 | 33% | 2026-11-02 | disaster | The USGS catalog records at least one magnitude 6.0 or greater earthquake within 250 km of event us6000tkt2 with origin time between 2026-08-20 and 2026-10-31 UTC. | A USGS FDSN event query centered on the us6000tkt2 epicenter with 250 km radius, minimum magnitude 6.0, and the window dates returns at least one event; zero events grades MISS. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

782 issued all-time across 14 forecaster arms · 692 open (11 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 173 issued · 165 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 173 | 165 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 105 | 93 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 69 | 68 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*