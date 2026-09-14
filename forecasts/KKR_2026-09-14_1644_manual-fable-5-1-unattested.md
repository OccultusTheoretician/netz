**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141644Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: manual/fable-5.1/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260914-23 | 35% | 2026-09-21 | political | On 2026-09-15 the US Senate holds a recorded roll-call vote on the CLARITY Act digital asset market structure bill (H.R. 3633 or its Senate vehicle) and the motion, whether cloture, motion to proceed, or passage, is agreed to. | True if senate.gov roll-call records show a vote dated 2026-09-15 on cloture, the motion to proceed, or passage of the CLARITY Act or its Senate market-structure vehicle, with a result of Agreed to or Passed. Otherwise false. |
| KKR-20260914-24 | 50% | 2026-10-02 | military/conflict | Between 2026-09-15 and 2026-09-30 a Ukrainian drone or missile strike causes fire or damage at an oil refinery inside internationally recognized Russian territory, acknowledged by a Russian governor, regional authority, or the operator, and claimed by the Ukrainian General Staff, SBU, or HUR. | True if, for a strike dated 2026-09-15 to 2026-09-30, a Russian governor, regional authority, or the operator acknowledges fire or damage at a named refinery in Russia and a Ukrainian military or intelligence body claims it. Otherwise false. |
| KKR-20260914-25 | 45% | 2026-10-16 | cyber | The CISA Known Exploited Vulnerabilities catalog contains at least 20 entries with a dateAdded value between 2026-09-15 and 2026-10-14 inclusive. | True if the CISA KEV JSON feed contains 20 or more entries whose dateAdded falls between 2026-09-15 and 2026-10-14 inclusive. False if 19 or fewer. |
| KKR-20260914-26 | 30% | 2026-10-19 | military/conflict | Between 2026-09-15 and 2026-10-15 foreign ministers or higher-ranking officials of Iran and at least three Gulf Cooperation Council member states attend the same in-person meeting with Strait of Hormuz transit on its stated agenda, as reported by two of Reuters, AP, AFP, Al Jazeera. | True if two of Reuters, AP, AFP, or Al Jazeera report an in-person meeting dated 2026-09-15 to 2026-10-15 of foreign ministers or above from Iran and three or more GCC states with Hormuz on the stated agenda. Otherwise false. |
| KKR-20260914-27 | 10% | 2026-11-18 | military/conflict | Between 2026-09-15 and 2026-11-13 Houthi (Ansar Allah) forces take control of Marib city, capital of Marib governorate in Yemen, as reported by at least two of Reuters, AP, AFP, and Al Jazeera. | True if at least two of Reuters, AP, AFP, or Al Jazeera report, citing the event as occurring between 2026-09-15 and 2026-11-13, that Houthi forces control the center of Marib city. Otherwise false. |
| KKR-20260914-28 | 20% | 2027-03-03 | crime/security | Between 2026-09-15 and 2027-03-01 the Criminal Cases Review Commission announces that it has referred one or more convictions of Lucy Letby to the Court of Appeal. | True if a CCRC press release or statement on ccrc.gov.uk, dated between 2026-09-15 and 2027-03-01, states the Commission has referred at least one conviction of Lucy Letby to the Court of Appeal. Otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Nasdaq Composite closing level for 2026-10-30, as published in FRED series NASDAQCOM, is below 24000.00, more than 8 percent under the r" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-14 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The 10-year US Treasury par yield for 2026-10-30, as published in the Treasury daily par yield curve and FRED series DGS10, is at or above 5" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-14 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "The FRED series DCOILWTICO (EIA Cushing WTI spot price) observation dated 2026-10-30 is below 90.00 dollars per barrel. Reference: WTI 103.3" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-14 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "Between 2026-09-15 and 2026-11-13 the Riksdag approves Magdalena Andersson as Prime Minister of Sweden on the proposal of the Speaker, with " → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — proposed. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim

## III. LEDGER STANDING

2097 issued all-time across 16 forecaster arms · 1761 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 96 issued · 96 open · nothing resolved yet — this arm earns a score at its first resolution.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 682 | 644 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 222 | 219 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*