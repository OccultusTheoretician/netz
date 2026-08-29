**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292142Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-28_1518.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-17 | 65% | 2026-09-18 | economics_markets | The FOMC raises the federal funds target range by 25 basis points at its scheduled 2026-09-15 to 2026-09-16 meeting, lifting the range to 3.75-4.00 percent. | The FOMC policy statement dated 2026-09-16 on federalreserve.gov sets the federal funds target range at 3.75 to 4.00 percent. A hold, a cut, or any other size of move resolves false. |
| KKR-20260829-18 | 78% | 2026-10-05 | military_conflict | Ukrainian authorities report Russian drone or missile impacts inside Kyiv city on at least six separate calendar days between 2026-09-01 and 2026-09-30. | Kyiv City Military Administration or Ukrainian Air Force statements, each carried by Reuters, AFP, or AP, place drone or missile impacts inside Kyiv city on six or more distinct days in the window. |
| KKR-20260829-19 | 7% | 2027-01-05 | military_conflict | Iran halts commercial transit through the Strait of Hormuz for at least 72 consecutive hours at some point between 2026-09-01 and 2026-12-31. | Two of Reuters, Lloyds List, and AP report that commercial traffic through the Strait of Hormuz was suspended by Iranian action for 72 or more consecutive hours inside the window. |
| KKR-20260829-20 | 35% | 2026-12-03 | political | The United States and Iran hold direct, publicly acknowledged government-to-government talks between 2026-09-01 and 2026-11-30. | Officials of both governments publicly confirm a direct meeting between US and Iranian representatives held inside the window, reported by two of Reuters, AP, and AFP. Indirect mediation only resolves false. |
| KKR-20260829-21 | 45% | 2026-11-04 | disaster | Combined confirmed deaths from the Nepal-Tibet glacial outburst flood reach 1,000 or more at some point between 2026-08-29 and 2026-10-31. | Nepal Police and Chinese authority tolls, as reported by two of Reuters, AP, and AFP, sum to 1,000 or more confirmed dead on any date inside the window. |
| KKR-20260829-22 | 44% | 2026-12-03 | crime_security | Austrian authorities announce at least one arrest in the Vienna museum theft of the 673-diamond necklace between 2026-08-29 and 2026-11-30. | Vienna police or the Austrian public prosecutor announce an arrest or detention connected to the necklace theft, reported by two of Reuters, AP, AFP, and DPA, inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "ICE Brent front-month crude posts an official settlement at or above 100.00 US dollars per barrel on at least one trading day between 2026-0" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds CVE-2026-81578 or CVE-2026-82078, the actively exploited PaperCut NG and MF flaws, to the Known Exploited Vulnerabilities catalog " → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "CISA adds at least one ServiceNow vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-08-28 and 2026-" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The USGS Geographic Names Information System records Lake America as the official feature name for the waterbody currently named Lake Ontari" → REJECTED: event window opens 2026-08-28, before this row is sealed (2026-08-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

1067 issued all-time across 14 forecaster arms · 906 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 127 issued · 124 open · 3 resolved · 1 hits / 2 misses · **Brier 0.141** against its own base rate 33.3% (climatological 0.222) · **skill +0.366** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 249 | 232 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 106 | 105 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 127 | 124 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 113 | 105 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*