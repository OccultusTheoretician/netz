**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 131514Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-13_1512.md · forecaster: lmstudio/auto · 6 accepted / 4 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261013-01 | 30% | 2026-10-29 | cyber | Between 2026-10-21 and 2026-10-24, a cyberattack on French supermarkets will result in refrigerators being heated to 50°C or higher. | At least one French supermarket reports refrigerators being heated to 50°C or higher due to a cyberattack between 2026-10-21 and 2026-10-24. |
| KKR-20261013-02 | 25% | 2026-10-29 | disaster | Between 2026-10-21 and 2026-10-24, a magnitude 6.0 or higher earthquake will occur in the Mid-Atlantic Ridge. | The USGS Significant Quakes catalog records an earthquake of magnitude 6.0 or higher in the Mid-Atlantic Ridge between 2026-10-21 and 2026-10-24. |
| KKR-20261013-03 | 35% | 2026-10-28 | economics/markets | Between 2026-10-21 and 2026-10-24, the 10-year U.S. Treasury yield will fall below 5.15 percent. | The 10-year U.S. Treasury yield falls to 5.15 percent or lower on the last trading day of the window, 2026-10-24. |
| KKR-20261013-04 | 10% | 2026-10-29 | crime/security | Between 2026-10-21 and 2026-10-24, a French court will issue a verdict in the case of the Buffalo supermarket shooting trial. | A French court issues a verdict in the Buffalo supermarket shooting trial between 2026-10-21 and 2026-10-24. |
| KKR-20261013-05 | 30% | 2026-10-28 | economics/markets | Between 2026-10-21 and 2026-10-24, the U.S. Treasury will issue a new bond with a yield of 5.25 percent or higher. | The U.S. Treasury issues a new bond with a yield of 5.25 percent or higher between 2026-10-21 and 2026-10-24. |
| KKR-20261013-06 | 25% | 2026-10-29 | cyber | Between 2026-10-21 and 2026-10-24, a cyberattack will exploit the Ivanti Connect Secure authentication bypass vulnerability (CVE-2026-104935) in a public-facing system. | A public report confirms a cyberattack exploiting CVE-2026-104935 in a public-facing system between 2026-10-21 and 2026-10-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-104935 with a date-added value of 2026-10-13." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-24, a Russian ballistic missile strike will hit Kyiv with no casualties reported in corroborating sources." → REJECTED: cited items name United States; the claim is about Russian Federation, zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-10-21 and 2026-10-24, the S&P 500 will close below 7,750 points." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-10-21 and 2026-10-24, a Houthi airstrike on Sanaa will result in no casualties reported in corroborating sources." → REJECTED: cited items name Australia, China, Mongolia; the claim is about zone:yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world

## III. LEDGER STANDING

4020 issued all-time across 21 forecaster arms · 2909 open (332 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 419 issued · 196 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1128 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 419 | 196 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 156 | 58 | 30 | 28 | 0.293 | 51.7% | 0.250 | -0.173 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 328 | 270 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 158 | 153 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*