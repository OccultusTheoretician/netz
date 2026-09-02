**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 020022Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-01_1518.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-22 | 53% | 2027-01-05 | military/conflict | Between 2026-09-02 and 2026-12-31, a general ceasefire covering the entire front line in Ukraine takes effect, announced by both the Ukrainian and Russian governments. | True if president.gov.ua and kremlin.ru both publish statements confirming a general front-wide ceasefire in effect on a date between 2026-09-02 and 2026-12-31; localized, energy-only, or humanitarian pauses do not count. |
| KKR-20260902-23 | 44% | 2026-11-04 | political | Between 2026-09-02 and 2026-10-31, Donald Trump and Vladimir Putin meet in person, with the meeting confirmed by both the White House and the Kremlin. | True if whitehouse.gov and kremlin.ru both carry official confirmation or readouts of an in-person Trump-Putin meeting held between 2026-09-02 and 2026-10-31; phone or video calls do not count. |
| KKR-20260902-24 | 44% | 2026-10-05 | political | A lapse in US federal appropriations (government shutdown) begins on 2026-10-01 because no full-year or continuing appropriations covering that date is enacted beforehand. | True if OMB or OPM publishes lapse-in-appropriations (shutdown) guidance effective 2026-10-01, or Congress.gov shows no enacted full-year or continuing appropriations covering 2026-10-01 for any federal agency. |
| KKR-20260902-25 | 25% | 2026-11-04 | economics/markets | The 10-year US Treasury constant maturity yield closes at or above 5.00 percent on at least one trading day between 2026-09-02 and 2026-10-30. Reference: 4.77 percent on 2026-09-01. | True if FRED series DGS10 shows a daily value of 5.00 or higher for any date from 2026-09-02 through 2026-10-30; the Treasury daily par yield curve is the tiebreaker if FRED is unavailable. |
| KKR-20260902-26 | 25% | 2026-11-04 | economics/markets | The WTI crude oil spot price at Cushing settles at or above 100.00 dollars per barrel on at least one trading day between 2026-09-02 and 2026-10-30. Reference: 88.02 dollars on 2026-09-01. | True if FRED series DCOILWTICO (EIA Cushing WTI spot) shows a daily value of 100.00 or higher for any date from 2026-09-02 through 2026-10-30; the EIA daily spot price table is the tiebreaker. |
| KKR-20260902-27 | 33% | 2026-10-02 | cyber | Between 2026-09-02 and 2026-09-30, CISA adds at least one Microsoft Exchange Server vulnerability to the Known Exploited Vulnerabilities catalog. | True if the CISA KEV catalog JSON contains at least one entry with vendorProject Microsoft, product containing Exchange, and dateAdded between 2026-09-02 and 2026-09-30 inclusive. |
| KKR-20260902-28 | 43% | 2026-10-02 | crime/security | Between 2026-09-01 and 2026-09-30, the [withheld] Fourth District Court orders Tyler Robinson bound over for trial on the aggravated murder charge in the killing of Charlie Kirk. | True if the [withheld] Fourth District Court docket, or the [withheld] County Attorney office, records a bindover order on the aggravated murder count dated 2026-09-01 through 2026-09-30; dismissal of that count or no ruling by 2026-09-30 resolves false. |
| KKR-20260902-29 | 43% | 2026-09-15 | crime/security | The jury in the Lindsay Clancy murder trial in Plymouth County, Massachusetts returns a verdict on at least one count between 2026-09-01 and 2026-09-11, rather than the judge declaring a mistrial for deadlock. | True if a verdict on any count (including not guilty by reason of insanity) is entered by Plymouth Superior Court, or reported by AP and the Boston Globe, dated 2026-09-01 through 2026-09-11; mistrial or no verdict resolves false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-02 and 2026-09-15, at least one additional commercial merchant vessel is attacked, struck by a weapon, or seized in the Stra" → REJECTED: resolution offers alternative VENUES joined by 'or' (…describes a merchant vessel attacked, struck, | or | seized in that area, or reuters and ap both r…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Nepal government official death toll for the floods that began in late August 2026 reaches at least 1400 by 2026-09-15. Reference: repor" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-01 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

1268 issued all-time across 14 forecaster arms · 1107 open (109 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 338 issued · 321 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 338 | 321 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 184 | 153 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 138 | 137 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 159 | 156 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 146 | 138 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*