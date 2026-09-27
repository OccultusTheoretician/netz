**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 271520Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-27_1517.md · forecaster: lmstudio/realist · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260927-01 | 30% | 2026-10-20 | military/conflict | Between 2026-10-10 and 2026-10-17, at least one drone strike using a Shahed-type UAV will be reported by two or more independently biased sources in the Odesa region of Ukraine. | At least one drone strike using a Shahed-type UAV in the Odesa region will be reported by two or more sources from distinct hostile sides (RU, UA, WEST) with no overlap in channel ownership. |
| KKR-20260927-02 | 10% | 2026-10-30 | disaster | Between 2026-10-20 and 2026-10-27, the USGS will record a magnitude 6.0 or higher earthquake in the Pacific Northwest region (Washington, Oregon, or Northern California). | The USGS Significant Quakes feed will list a magnitude 6.0 or higher earthquake with epicenter in Washington, Oregon, or Northern California between 2026-10-20 and 2026-10-27. |
| KKR-20260927-03 | 20% | 2026-11-17 | economics/markets | On 2026-11-15, the 10-year Treasury yield will exceed 5.50% at the close of trading. | The 10-year Treasury yield on 2026-11-15 will be greater than 5.50% as reported by FRED or the U.S. Treasury. |
| KKR-20260927-04 | 35% | 2026-10-10 | cyber | Between 2026-10-01 and 2026-10-08, at least one confirmed cyberattack exploiting the Citrix NetScaler RCE vulnerability (CVE-2026-XXXX) will be reported by two or more independent sources. | At least one cyberattack exploiting the Citrix NetScaler RCE vulnerability (CVE-2026-XXXX) will be reported by two or more sources from distinct hostile sides (e.g., RU, WEST, IL) during the event window. |
| KKR-20260927-05 | 40% | 2026-10-21 | political | Between 2026-10-12 and 2026-10-19, the White House will issue a formal statement rejecting Iran's proposal to reopen the Strait of Hormuz within seven days. | A formal statement issued by the White House on or before 2026-10-19 will explicitly reject Iran's seven-day peace proposal to reopen the Strait of Hormuz. |
| KKR-20260927-06 | 25% | 2026-10-14 | military/conflict | Between 2026-10-05 and 2026-10-12, at least one confirmed airstrike using a Patriot missile system will be reported by two or more independently biased sources in the Tehran region. | At least one airstrike using a Patriot missile system in the Tehran region will be reported by two or more sources from distinct hostile sides (AXIS, IL, WEST) with no channel overlap. |
| KKR-20260927-07 | 15% | 2026-10-24 | economics/markets | Between 2026-10-15 and 2026-10-22, the European Central Bank will announce a 0.5 percentage point increase in the main refinancing rate. | The European Central Bank will announce a 0.5 percentage point increase in the main refinancing rate during the event window, as confirmed by ECB press release. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-10-05, the CISA KEV catalog will carry a date-added value between 2026-09-20 and 2026-09-26 for a vulnerability with a CVSS score of" → REJECTED: event window opens 2026-09-20, before this row is sealed (2026-09-27, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "On 2026-11-03, the S&P 500 will close below 7,500 points, with a daily move exceeding 2% in either direction." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-11-01, the Dow Jones Industrial Average will close above 53,000 points." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-01 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

2938 issued all-time across 17 forecaster arms · 2396 open (226 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 129 issued · 124 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1039 | 922 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 129 | 124 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 200 | 183 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 27 | 27 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 327 | 263 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*