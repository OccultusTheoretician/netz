**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: lmstudio/auto · 5 accepted / 5 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-01 | 35% | 2026-11-04 | cyber | Between 2026-10-21 and 2026-10-28, a cyberattack exploiting CVE-2026-88779 will be reported by two or more independent sources in the CISA KEV or The Hacker News. | A cyberattack exploiting CVE-2026-88779 is reported by two or more independent sources in the CISA KEV catalog or The Hacker News between 2026-10-21 and 2026-10-28. |
| KKR-20261005-02 | 20% | 2026-11-04 | political | Between 2026-10-21 and 2026-10-28, Iran will publicly announce a toll for oil transit through the Strait of Hormuz. | Iran publicly announces a toll for oil transit through the Strait of Hormuz between 2026-10-21 and 2026-10-28. |
| KKR-20261005-03 | 30% | 2026-11-04 | disaster | Between 2026-10-21 and 2026-10-28, a new earthquake of magnitude 4.0 or higher will be recorded by USGS in the Pacific Northwest. | A new earthquake of magnitude 4.0 or higher is recorded by USGS in the Pacific Northwest between 2026-10-21 and 2026-10-28. |
| KKR-20261005-04 | 25% | 2026-11-04 | disaster | Between 2026-10-21 and 2026-10-28, a new tropical cyclone named KOGUMA-26 will be reported by GDACS with a population affected of over 100,000. | A new tropical cyclone named KOGUMA-26 is reported by GDACS with a population affected of over 100,000 between 2026-10-21 and 2026-10-28. |
| KKR-20261005-05 | 30% | 2026-11-04 | cyber | Between 2026-10-21 and 2026-10-28, a new cyberattack targeting a financial institution in South Korea will be confirmed by BleepingComputer and The Hacker News. | A new cyberattack targeting a financial institution in South Korea is confirmed by BleepingComputer and The Hacker News between 2026-10-21 and 2026-10-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-28, the CISA KEV catalog will include CVE-2026-88779 with a date-added value of 2026-10-04." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-88779 dateAdded 2026-10-04, before the claimed window 2026-10-21..2026-10-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-28, the S&P 500 will close above 7,800 points on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-21 and 2026-10-28, a drone strike will be confirmed in Kyiv by at least two independent sources from hostile sides (RU, UA, " → REJECTED: cited items name Brazil; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-28, a new flood alert will be issued by GDACS for a location in the United States." → REJECTED: cited items name France; the claim is about United States — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-28, a new drone strike will be confirmed in Gaza City by at least two independent sources from hostile sides " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3396 issued all-time across 18 forecaster arms · 2582 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 383 issued · 204 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1218 | 1017 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 175 | 140 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 258 | 225 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 46 | 46 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*