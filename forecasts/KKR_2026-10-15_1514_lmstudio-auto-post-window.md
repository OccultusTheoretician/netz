**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151514Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-15_1512.md · forecaster: lmstudio/auto · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261015-01 | 35% | 2026-10-27 | economics/markets | Between 2026-10-21 and 2026-10-24, the S&P 500 closes below 7,600 points at the end of the trading day. | The S&P 500 closes at or below 7,600 points on the last trading day of the event window, as reported by the NYSE or a major financial data provider. |
| KKR-20261015-02 | 15% | 2026-10-28 | disaster | Between 2026-10-21 and 2026-10-24, the USGS Significant Quakes catalog records a magnitude 6.0 or higher earthquake in the United States. | The USGS Significant Quakes catalog lists an earthquake with magnitude 6.0 or higher in the United States between 2026-10-21 and 2026-10-24. |
| KKR-20261015-03 | 20% | 2026-10-28 | cyber | Between 2026-10-21 and 2026-10-24, a new vulnerability in Palo Alto Networks PAN-OS is actively exploited in at least one confirmed cyberattack. | At least one confirmed cyberattack between 2026-10-21 and 2026-10-24 exploits a vulnerability in Palo Alto Networks PAN-OS, as reported by CISA, BleepingComputer, or The Hacker News. |
| KKR-20261015-04 | 30% | 2026-10-28 | political | Between 2026-10-21 and 2026-10-24, the European Union issues a formal statement condemning Russia's actions in Ukraine and imposing new sanctions. | A formal statement issued by the European Union between 2026-10-21 and 2026-10-24 condemns Russia's actions in Ukraine and announces new sanctions, as confirmed by BBC World, Deutsche Welle, or Al Jazeera. |
| KKR-20261015-05 | 10% | 2026-10-28 | disaster | Between 2026-10-21 and 2026-10-24, a school roof collapse in Pakistan results in at least 20 fatalities. | A school roof collapse in Pakistan between 2026-10-21 and 2026-10-24 results in at least 20 fatalities, as confirmed by BBC World, NPR News, or Al Jazeera. |
| KKR-20261015-06 | 40% | 2026-10-27 | economics/markets | Between 2026-10-21 and 2026-10-24, the U.S. Treasury yields on the 10-year bond fall below 4.95 percent. | The 10-year U.S. Treasury yield falls below 4.95 percent on the last trading day of the event window, as reported by FRED or a major financial data provider. |
| KKR-20261015-07 | 18% | 2026-10-28 | cyber | Between 2026-10-21 and 2026-10-24, a major cyberattack on a U.S. government agency is confirmed by the FBI and reported by at least two independent outlets. | A major cyberattack on a U.S. government agency between 2026-10-21 and 2026-10-24 is confirmed by the FBI and reported by at least two independent outlets (e.g., BleepingComputer, The Hacker News, Al Jazeera). |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-21 and 2026-10-24, the CISA KEV catalog will include CVE-2026-105134 with a date-added value of 2026-10-14." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-105134 dateAdded 2026-10-14, before the claimed window 2026-10-21..2026-10-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-10-21 and 2026-10-24, at least one report from a hostile side confirms a drone strike on Kyiv with casualties reported." → REJECTED: cited items name China, Korea, Democratic People's Republic of; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-21 and 2026-10-24, a new ceasefire agreement is brokered between Israel and Hamas and confirmed by both sides through indepe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4170 issued all-time across 21 forecaster arms · 3059 open (481 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 429 issued · 206 open · 214 resolved · 63 hits / 151 misses · **Brier 0.209** against its own base rate 29.4% (climatological 0.208) · **skill -0.007**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1475 | 1179 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 429 | 206 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 52 | 52 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 345 | 287 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 174 | 169 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*