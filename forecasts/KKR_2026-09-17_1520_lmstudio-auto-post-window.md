**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-17_1518.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260917-01 | 35% | 2026-10-02 | disaster | Between 2026-09-21 and 2026-09-24, a new flood warning for Marion County, Florida, will be issued by the National Weather Service and confirmed by at least two independent news outlets. | The National Weather Service issues a flood warning for Marion County, Florida, between 2026-09-21 and 2026-09-24, and this is confirmed by at least two independent news outlets. |
| KKR-20260917-02 | 40% | 2026-10-02 | political | Between 2026-09-21 and 2026-09-24, a new political scandal involving a U.S. government official will be reported by at least two major outlets with independent corroboration. | At least two major outlets (e.g., Guardian, BBC, Al Jazeera, CNBC) report a new political scandal involving a U.S. government official, with corroboration from a third source. |
| KKR-20260917-03 | 20% | 2026-10-02 | disaster | Between 2026-09-21 and 2026-09-24, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in the Aleutian Islands. | The USGS records an earthquake of magnitude 6.5 or higher in the Aleutian Islands between 2026-09-21 and 2026-09-24. |
| KKR-20260917-04 | 35% | 2026-10-02 | cyber | Between 2026-09-21 and 2026-09-24, a new cyberattack using the SparroWocky backdoor will be confirmed by at least two independent sources targeting government systems in Latin America. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24 for a vulnerability linked to the SparroWocky backdoor, and at least two independent sources confirm its use in attacks on government systems in Latin America. |
| KKR-20260917-05 | 25% | 2026-10-02 | political | Between 2026-09-21 and 2026-09-24, a new political resignation in a European country will be confirmed by at least two major news outlets. | At least two major news outlets (e.g., BBC, Guardian, Al Jazeera) confirm a new political resignation in a European country between 2026-09-21 and 2026-09-24. |
| KKR-20260917-06 | 40% | 2026-10-02 | military/conflict | Between 2026-09-21 and 2026-09-24, a new military escalation in the Russia-Ukraine conflict will be confirmed by at least two hostile sides with cross-bias agreement. | At least two hostile sides (e.g., RU, UA, WEST) confirm a new military escalation in the Russia-Ukraine conflict between 2026-09-21 and 2026-09-24, with cross-bias agreement. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, a drone strike using a Shahed-136 or equivalent weapon will be confirmed by at least two independent sour" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-09-21 and 2026-09-24, a cyberattack exploiting CVE-2026-76460 in Cisco Identity Services Engine will be publicly reported by at" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-76460 dateAdded 2026-09-16, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, the S&P 500 index will close above 7,700 points on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-21 and 2026-09-24, a new critical vulnerability in Google Pixel devices will be publicly disclosed and exploited in the wild" → REJECTED: the resolution names a different subject than the statement — the claim is about Google, Pixel and the resolution settles on CISA, CVE, KEV, cve-2026-58704. A row whose resolution checks a different fact can be scored correct while being wrong; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-58704 dateAdded 2026-09-16, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

2371 issued all-time across 16 forecaster arms · 1905 open (82 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 286 issued · 136 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 805 | 720 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 286 | 136 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 121 | 111 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 273 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 252 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*