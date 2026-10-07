**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071520Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-07_1518.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261007-01 | 45% | 2026-10-28 | economics/markets | Between 2026-10-21 and 2026-10-24, the S&P 500 index closes above 7,800 points on at least one trading day, based on the official market close. | The S&P 500 closes at or above 7,800 on at least one day between 2026-10-21 and 2026-10-24, as reported by the NYSE or S&P Global. |
| KKR-20261007-02 | 35% | 2026-10-26 | disaster | Between 2026-10-21 and 2026-10-24, a magnitude 5.0 or higher earthquake is recorded by the USGS in the Alaskan region, with depth between 20km and 100km. | The USGS Significant Quakes catalog carries a magnitude ≥5.0 and depth between 20km and 100km for an event in Alaska between 2026-10-21 and 2026-10-24. |
| KKR-20261007-03 | 30% | 2026-10-28 | political | Between 2026-10-21 and 2026-10-24, a new political scandal involving a senior U.S. government official is reported by at least two major outlets (e.g., BBC World, Guardian World) with a public statement from the official or a congressional inquiry initiated. | At least two major outlets (BBC World, Guardian World) report a new political scandal involving a senior U.S. government official between 2026-10-21 and 2026-10-24, with a public statement or congressional inquiry initiated. |
| KKR-20261007-04 | 25% | 2026-10-28 | disaster | Between 2026-10-21 and 2026-10-24, a tropical cyclone with sustained winds of at least 74 mph (Category 1) is confirmed by GDACS Alerts and reported by at least two independent sources (e.g., BBC World, Al Jazeera). | GDACS Alerts reports a tropical cyclone with sustained winds ≥74 mph between 2026-10-21 and 2026-10-24, and at least two independent sources (BBC World, Al Jazeera) report its occurrence. |
| KKR-20261007-05 | 35% | 2026-10-28 | cyber | Between 2026-10-21 and 2026-10-24, a ransomware attack results in the public disclosure of sensitive data from a major corporation (e.g., Boeing, ASOS), confirmed by two independent sources. | Two independent sources (e.g., BleepingComputer, Krebs on Security) confirm a ransomware attack resulting in public data disclosure from a major corporation (e.g., Boeing, ASOS) between 2026-10-21 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, at least one drone strike with reported casualties occurred in Kyiv, Ukraine, confirmed by at least two i" → REJECTED: cited items name Indonesia, Namibia, United States; the claim is about Ukraine, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-10-21 and 2026-10-24, a cyberattack exploiting a critical Atlassian flaw (CVE-2026-XXXX) is confirmed by at least two independe" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-10-21 and 2026-10-24, India's central bank raises its policy rate by at least 25 basis points, confirmed by a public announceme" → REJECTED: resolution offers alternative VENUES joined by 'or' (…serve bank of india issues a public statement | or | press release confirming a rate hike of at le…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-21 and 2026-10-24, a major cyberattack on a U.S. state or federal agency is confirmed by two independent wire services (e.g." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-21 and 2026-10-24, a new U.S. federal law is passed by Congress and signed by the President, with a public record in the Fed" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3539 issued all-time across 21 forecaster arms · 2725 open (423 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 392 issued · 213 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1265 | 1064 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 392 | 213 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 9 | 9 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 13 | 13 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 185 | 150 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 274 | 241 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 103 | 103 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*