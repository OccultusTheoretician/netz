**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 231516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-23_1514.md · forecaster: lmstudio/auto · 9 accepted / 1 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261023-45 | 30% | 2027-04-21 | military/conflict | Between 2026-11-01 and 2026-11-07, a confirmed attack using a drone or UAV will occur in Kyiv, Ukraine, with at least one casualty reported in corroborating reports from at least two hostile sides. | A confirmed attack in Kyiv, Ukraine, between 2026-11-01 and 2026-11-07 involving a drone or UAV, with at least one casualty, as reported by at least two distinct channels from two hostile sides (RU, UA, or WEST) in public sources. |
| KKR-20261023-46 | 25% | 2027-04-21 | cyber | Between 2026-11-10 and 2026-11-16, the CISA KEV catalog will include at least one new entry for a critical vulnerability in Arista VeloCloud software exploited in the wild. | The CISA KEV catalog carries a date-added value between 2026-11-10 and 2026-11-16 for a vulnerability in Arista VeloCloud software that is actively exploited in the wild. |
| KKR-20261023-47 | 35% | 2027-04-21 | economics/markets | Between 2026-12-01 and 2026-12-07, the 10-year U.S. Treasury yield will close above 5.00 percent on at least one weekday. | The 10-year U.S. Treasury yield, as reported by FRED, exceeds 5.00 percent on at least one weekday between 2026-12-01 and 2026-12-07. |
| KKR-20261023-48 | 15% | 2027-04-21 | disaster | Between 2026-11-20 and 2026-11-26, a magnitude 7.0 or greater earthquake will be reported by the USGS in the China-Tibet region with at least 10 fatalities confirmed in public reports. | The USGS reports a magnitude 7.0 or greater earthquake in the China-Tibet region between 2026-11-20 and 2026-11-26, with at least 10 fatalities confirmed in public reporting from at least two independent sources. |
| KKR-20261023-49 | 20% | 2027-04-21 | cyber | Between 2026-12-15 and 2026-12-21, a confirmed cyberattack using a zero-day exploit in the Node.js build system will be reported by The Hacker News and BleepingComputer. | The Hacker News and BleepingComputer report a confirmed cyberattack exploiting a zero-day vulnerability in the Node.js build system between 2026-12-15 and 2026-12-21. |
| KKR-20261023-50 | 30% | 2027-04-21 | military/conflict | Between 2026-11-05 and 2026-11-11, a new ceasefire agreement will be publicly confirmed in the Russia-Ukraine conflict, with at least two hostile sides (RU, UA, or WEST) reporting it. | A new ceasefire agreement in the Russia-Ukraine conflict is confirmed by at least two distinct channels from two hostile sides (RU, UA, or WEST) in public reporting between 2026-11-05 and 2026-11-11. |
| KKR-20261023-51 | 25% | 2027-04-21 | disaster | Between 2026-11-15 and 2026-11-21, a confirmed outbreak of Ebola in Nigeria will be reported by the BBC World and NPR News with at least one confirmed fatality. | BBC World and NPR News report a confirmed Ebola outbreak in Nigeria with at least one fatality between 2026-11-15 and 2026-11-21. |
| KKR-20261023-52 | 35% | 2027-04-21 | political | Between 2026-12-10 and 2026-12-16, a major political scandal involving a U.S. presidential candidate will be reported by Al Jazeera and BBC World with at least one indictment or formal charge. | Al Jazeera and BBC World report a major political scandal involving a U.S. presidential candidate between 2026-12-10 and 2026-12-16, with at least one indictment or formal charge filed. |
| KKR-20261023-53 | 20% | 2027-04-21 | cyber | Between 2026-11-25 and 2026-12-01, a confirmed cyberattack on a U.S. government system will be reported by CISA and The Hacker News with a CVSS score of 9.0 or higher. | CISA and The Hacker News report a confirmed cyberattack on a U.S. government system between 2026-11-25 and 2026-12-01 with a CVSS score of 9.0 or higher. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-12-05 and 2026-12-11, the S&P 500 will close below 7,500 points on at least one weekday." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…026-12-05 and 2026-12-11, as reported by fred | or | a major exchange…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4765 issued all-time across 21 forecaster arms · 3413 open (638 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 466 issued · 225 open · 231 resolved · 70 hits / 161 misses · **Brier 0.211** against its own base rate 30.3% (climatological 0.211) · **skill -0.001**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1679 | 1296 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 466 | 225 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 95 | 94 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 97 | 97 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 107 | 100 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 238 | 151 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 413 | 332 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 245 | 234 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 196 | 193 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*