**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 191518Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-19_1516.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260919-01 | 25% | 2026-10-01 | disaster | Between 2026-09-21 and 2026-09-24, the USGS Significant Quakes catalog will record a magnitude 6.5 or higher earthquake in the Kermadec Islands Region. | The USGS Significant Quakes catalog records a magnitude 6.5 or higher earthquake in the Kermadec Islands Region with a date within the event window. |
| KKR-20260919-02 | 35% | 2026-10-01 | military/conflict | Between 2026-09-21 and 2026-09-24, at least one drone strike will be reported in Kyiv, Ukraine, with a corroborated report from both Russian and Ukrainian sources. | At least one drone strike is reported in Kyiv, Ukraine, with a corroborated report from both Russian and Ukrainian sources during the event window. |
| KKR-20260919-03 | 30% | 2026-10-01 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield will exceed 5.10 percent at market close on at least one day. | The 10-year U.S. Treasury yield exceeds 5.10 percent at market close on at least one day between 2026-09-21 and 2026-09-24. |
| KKR-20260919-04 | 20% | 2026-10-01 | cyber | Between 2026-09-21 and 2026-09-24, a new exploit for CVE-2026-53266 will be publicly disclosed in a security advisory. | A new public exploit for CVE-2026-53266 is disclosed in a security advisory between 2026-09-21 and 2026-09-24. |
| KKR-20260919-05 | 25% | 2026-10-01 | political | Between 2026-09-21 and 2026-09-24, the European Union will issue a public statement urging the United States to lift the travel ban on the Palestinian delegation to the UN General Assembly. | The European Union issues a public statement urging the United States to lift the travel ban on the Palestinian delegation to the UN General Assembly between 2026-09-21 and 2026-09-24. |
| KKR-20260919-06 | 30% | 2026-10-01 | crime/security | Between 2026-09-21 and 2026-09-24, Saudi Arabia will issue a second air raid alert for Riyadh, confirmed by at least two independent news outlets. | Saudi Arabia issues a second air raid alert for Riyadh, confirmed by at least two independent news outlets between 2026-09-21 and 2026-09-24. |
| KKR-20260919-07 | 20% | 2026-10-01 | cyber | Between 2026-09-21 and 2026-09-24, a major cyberattack exploiting the Orkes Conductor Workflow Platform vulnerability (CVE-2025-39964) will be confirmed by CISA. | CISA confirms a major cyberattack exploiting CVE-2025-39964 in the Orkes Conductor Workflow Platform between 2026-09-21 and 2026-09-24. |
| KKR-20260919-08 | 35% | 2026-10-01 | military/conflict | Between 2026-09-21 and 2026-09-24, the U.S. and Denmark will publicly announce the implementation of a new military presence in Greenland under the security deal. | The U.S. and Denmark publicly announce the implementation of a new military presence in Greenland under the security deal between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2025-39964 with a date-added value of 2026-09-18." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2025-39964 dateAdded 2026-09-18, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, the S&P 500 index will close above 7,700 points on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2508 issued all-time across 16 forecaster arms · 2042 open (157 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 301 issued · 151 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 858 | 773 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 301 | 151 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 89 | 84 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 136 | 126 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 293 | 276 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 270 | 222 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*