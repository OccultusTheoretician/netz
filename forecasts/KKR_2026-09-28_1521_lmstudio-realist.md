**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281521Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-28_1516.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260928-08 | 30% | 2026-10-20 | cyber | Between 2026-10-10 and 2026-10-17, at least one confirmed cyberattack exploiting CVE-2026-88771 or CVE-2026-88772 will be reported by two independent sources with hostile bias. | At least one confirmed cyberattack exploiting CVE-2026-88771 or CVE-2026-88772 is reported by two independent sources with hostile bias between 2026-10-10 and 2026-10-17. |
| KKR-20260928-09 | 45% | 2026-10-26 | economics/markets | Between 2026-10-15 and 2026-10-22, the U.S. Treasury will issue a new 10-year note with a yield above 5.4 percent. | The U.S. Treasury issues a new 10-year note with a yield above 5.4 percent between 2026-10-15 and 2026-10-22. |
| KKR-20260928-10 | 15% | 2026-10-30 | disaster | Between 2026-10-20 and 2026-10-27, a new volcanic eruption will be reported in the CISA KEV catalog as a confirmed event. | The CISA KEV catalog carries a date-added value between 2026-10-20 and 2026-10-27 for a new volcanic eruption event. |
| KKR-20260928-11 | 25% | 2026-11-03 | economics/markets | Between 2026-10-25 and 2026-11-01, the U.S. Federal Reserve will announce a 50 basis point rate hike. | The U.S. Federal Reserve announces a 50 basis point rate hike between 2026-10-25 and 2026-11-01. |
| KKR-20260928-12 | 55% | 2026-11-20 | economics/markets | Between 2026-11-10 and 2026-11-17, the U.S. dollar will trade above 1.15 against the euro. | The EUR/USD exchange rate closes above 1.15 on at least one trading day between 2026-11-10 and 2026-11-17. |
| KKR-20260928-13 | 35% | 2026-11-24 | disaster | Between 2026-11-15 and 2026-11-22, a new flood alert will be issued by GDACS for a location in Southeast Asia. | GDACS issues a new flood alert for a location in Southeast Asia between 2026-11-15 and 2026-11-22. |
| KKR-20260928-14 | 40% | 2026-11-30 | political | Between 2026-11-20 and 2026-11-27, a new political scandal involving a U.S. government official will be reported by two independent sources with hostile bias. | A new political scandal involving a U.S. government official is reported by two independent sources with hostile bias between 2026-11-20 and 2026-11-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-01, the CISA KEV catalog will include CVE-2026-88772 with a date-added value of 2026-09-27." → REJECTED: event window opens 2026-09-27, before this row is sealed (2026-09-28, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-10-05 and 2026-10-12, the S&P 500 will close above 7,750 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-11-05 and 2026-11-12, a confirmed cyberattack will be reported by two independent sources with hostile bias, exploiting a vulne" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3002 issued all-time across 17 forecaster arms · 2460 open (232 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 136 issued · 131 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1064 | 947 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 336 | 186 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 136 | 131 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 210 | 193 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 34 | 34 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 335 | 271 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*