**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011617Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-01_1613.md · forecaster: lmstudio/realist · 6 accepted / 4 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261001-10 | 30% | 2026-10-10 | military/conflict | On 2026-10-02, a drone attack targeting a civilian facility in Kyiv, Ukraine, results in at least one confirmed fatality, as verified by at least two independent outlets from hostile sides (RU, UA) reporting the event with casualty details. | At least one confirmed fatality is reported in a drone attack on a civilian facility in Kyiv, Ukraine, between 2026-10-02 and 2026-10-08, as confirmed by at least two independent outlets from hostile sides (RU, UA) in corroborating reports that include casualty counts. |
| KKR-20261001-11 | 25% | 2026-10-10 | cyber | Between 2026-10-01 and 2026-10-07, at least one verified cyberattack exploiting CVE-2026-76504 will be reported in public sources from at least two independent outlets across hostile sides (WEST, RU). | At least one verified cyberattack exploiting CVE-2026-76504 is reported in public sources from at least two independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07. |
| KKR-20261001-12 | 30% | 2026-10-10 | military/conflict | Between 2026-10-01 and 2026-10-07, a confirmed attack using a Shahed drone will be reported in the Gaza City area, with at least one casualty, as verified by at least two independent outlets from hostile sides (IL, PS). | A confirmed attack using a Shahed drone in Gaza City is reported with at least one casualty, as verified by at least two independent outlets from hostile sides (IL, PS) between 2026-10-01 and 2026-10-07. |
| KKR-20261001-13 | 20% | 2026-10-10 | cyber | On 2026-10-08, the Metamask security incident will result in the permanent exit of at least 500 Ethereum validators from the network, as confirmed by a public blockchain analytics report. | The Metamask security incident results in the permanent exit of at least 500 Ethereum validators from the network, as confirmed by a public blockchain analytics report on 2026-10-08. |
| KKR-20261001-14 | 28% | 2026-10-10 | cyber | Between 2026-10-01 and 2026-10-07, a confirmed cyberattack using the RedFlick technique will be reported in public sources from at least two independent outlets across hostile sides (WEST, RU). | A confirmed cyberattack using the RedFlick technique is reported in public sources from at least two independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07. |
| KKR-20261001-15 | 22% | 2026-10-10 | military/conflict | Between 2026-10-01 and 2026-10-07, a confirmed drone strike on a civilian facility in Tehran, Iran, will result in at least one fatality, as verified by at least two independent outlets from hostile sides (AXIS, WEST). | A confirmed drone strike on a civilian facility in Tehran, Iran, results in at least one fatality, as verified by at least two independent outlets from hostile sides (AXIS, WEST) between 2026-10-01 and 2026-10-07. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-01 and 2026-10-07, the CISA KEV catalog will include CVE-2026-76504 with a date-added value of 2026-09-30." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-76504 dateAdded 2026-09-30, before the claimed window 2026-10-01..2026-10-07; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "On 2026-10-05, the 10-year U.S. Treasury yield will exceed 5.30 percent, based on the close of the U.S. bond market." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-05 exactly. Price a day, not a window: widen the window or state why the date is fixed
- "On 2026-10-06, the S&P 500 will close below 7,600 points, based on the final settlement of the U.S. stock market." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "On 2026-10-07, the U.S. 30-year mortgage rate will rise to 7.5 percent or higher, based on the final settlement of the U.S. mortgage market." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

3176 issued all-time across 18 forecaster arms · 2634 open (348 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 154 issued · 149 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1133 | 1016 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 354 | 204 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 154 | 149 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 232 | 215 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 17 | 17 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*