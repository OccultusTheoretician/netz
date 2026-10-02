**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-02_1519.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261002-01 | 28% | 2026-10-28 | military/conflict | A drone strike targeting a military installation in Kyiv, Ukraine, occurs between 2026-10-21 and 2026-10-24, resulting in at least one confirmed casualty. | The CISA KEV catalog carries a date-added value between 2026-10-21 and 2026-10-24, and at least one corroborating report from a hostile side (RU or UA) confirms a drone strike on a military installation in Kyiv with at least one confirmed casualty. |
| KKR-20261002-02 | 18% | 2026-10-28 | disaster | A major earthquake with magnitude 5.0 or higher occurs in the Pacific Northwest between 2026-10-21 and 2026-10-24, confirmed by USGS Significant Quakes. | The USGS Significant Quakes catalog carries a magnitude 5.0 or higher earthquake event with a location in the Pacific Northwest (Washington, Oregon, or adjacent coastal zones) between 2026-10-21 and 2026-10-24. |
| KKR-20261002-03 | 25% | 2026-10-28 | economics/markets | A new G7 oil reserve release of at least 100 million barrels is announced by the G7 nations between 2026-10-21 and 2026-10-24, confirmed by at least two independent sources. | At least two independent sources (e.g., Guardian World, Al Jazeera, CNBC) report a G7 announcement of a new oil reserve release of 100 million barrels or more between 2026-10-21 and 2026-10-24. |
| KKR-20261002-04 | 22% | 2026-10-28 | disaster | A major wildfire in California, confirmed by GDACS Alerts, occurs between 2026-10-21 and 2026-10-24, with a green alert issued and at least one fatality reported. | The GDACS Alerts catalog carries a green forest fire notification for California between 2026-10-21 and 2026-10-24, and at least one fatality is confirmed by two independent sources (e.g., BBC, Al Jazeera). |
| KKR-20261002-05 | 35% | 2026-10-28 | political | A political protest in France results in the closure of at least 100 schools between 2026-10-21 and 2026-10-24, confirmed by two independent sources. | Two independent sources (e.g., Al Jazeera, Guardian World) confirm that political protests in France led to the closure of at least 100 schools between 2026-10-21 and 2026-10-24. |
| KKR-20261002-06 | 27% | 2026-10-28 | military/conflict | A drone strike on a civilian infrastructure site in Gaza City, Palestine, occurs between 2026-10-21 and 2026-10-24, resulting in at least one confirmed casualty, as reported by two independent sources. | Two independent sources (e.g., Al Jazeera, BBC) report a drone strike on a civilian infrastructure site in Gaza City between 2026-10-21 and 2026-10-24, with at least one confirmed casualty. |
| KKR-20261002-07 | 20% | 2026-10-28 | cyber | A ransomware attack on a U.S. state government system, confirmed by CISA KEV, occurs between 2026-10-21 and 2026-10-24, with a public disclosure from the affected state. | The CISA KEV catalog carries a date-added value between 2026-10-21 and 2026-10-24 for a vulnerability exploited in a U.S. state government system, and a public disclosure is made by the affected state within 48 hours of the event. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A cyberattack exploiting CVE-2026-104286 in Fortinet FortiMail systems is confirmed by two independent sources in the CISA KEV catalog betwe" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104286 dateAdded 2026-10-01, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The S&P 500 index closes above 7,800 points on or before 2026-10-24, based on the prior close of 7,714.13." → REJECTED: the named venue is introduced by 'such as', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A cyberattack on a U.S. federal government system, confirmed by the CISA KEV catalog, occurs between 2026-10-21 and 2026-10-24, with a publi" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3225 issued all-time across 18 forecaster arms · 2683 open (391 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 361 issued · 211 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1154 | 1037 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 361 | 211 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 154 | 149 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 239 | 222 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 64 | 64 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*