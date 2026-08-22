**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220321Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/fable-5/unattested · 3 accepted / 7 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-01 | 30% | 2026-10-02 | economics/markets | The 10-year Treasury constant-maturity yield (FRED series DGS10, 4.65 on 2026-08-19 after a 20-month high near 4.75 that week) records a daily value of 5.00 percent or higher on at least one day between 2026-08-24 and 2026-09-30. | FRED series DGS10 shows at least one observation dated 2026-08-24 through 2026-09-30 inclusive with a value of 5.00 or greater. |
| KKR-20260822-02 | 25% | 2026-09-09 | military/conflict | US Central Command publicly announces US strikes on land targets inside Iran conducted on at least one day between 2026-08-24 and 2026-09-06, ending the kinetic pause that has held since the cancelled campaign of 2026-08-01 while the administration pivots to economic warfare. | A CENTCOM press release on centcom.mil or an official CENTCOM social media post states that US forces struck land targets inside Iran on a date from 2026-08-24 through 2026-09-06 inclusive; blockade actions against vessels do not count. |
| KKR-20260822-03 | 45% | 2026-11-17 | crime/security | Jury selection in United States v. Jeffries et al. (E.D.N.Y., Central Islip, Judge Nusrat Choudhury), set for late October after the 2026-08-20 competency ruling, begins on a date between 2026-10-01 and 2026-11-13. | The E.D.N.Y. docket for United States v. Jeffries et al. records a minute entry for jury selection or commencement of trial dated 2026-10-01 through 2026-11-13 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds CVE-2026-19478, the GitLab CE/EE GraphQL code-injection flaw (CVSS 9.4) reported exploited in the wild on 2026-08-19, to the Known" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "CISA adds CVE-2026-69836, the Microsoft Entra ID deserialization remote code execution flaw (CVSS 10.0) that Microsoft says was exploited an" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "At its scheduled 2026-09-15 to 2026-09-16 meeting the FOMC raises the federal funds target range above the current 3.50 to 3.75 percent, fol" → REJECTED: event window opens 2026-07-29, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The additional 50 percent US tariff on the roughly 20 billion USD list of Canadian goods, set to switch on at 12:01 a.m. ET on 2026-08-22 ab" → REJECTED: resolution offers alternative VENUES joined by 'or' (…cbp csms message | or | a federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A presidential proclamation or executive order implementing the 2026-08-21 announcement that up to 300,000 metric tons of ground beef may be" → REJECTED: resolution offers alternative VENUES joined by 'or' (…presidential proclamation | or | executive order with a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "An earthquake of magnitude 6.0 or greater occurs within 100 km of the epicenter of the 2026-08-20 M6.7 intermediate-depth mainshock near Ani" → REJECTED: event window opens 2026-08-21, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later; the resolution names only a venue or register (ComCat, USGS, usgs) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Cumulative deaths among confirmed Bundibugyo Ebola cases in the DRC, 2,516 for data through 2026-08-19, reach at least 4,000 in a DRC INSP, " → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-08-19 exactly. Price a day, not a window: widen the window or state why the date is fixed; event window opens 2026-08-19, before this row is sealed (2026-08-22) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

834 issued all-time across 14 forecaster arms · 744 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 70 issued · 70 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 117 | 105 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 70 | 70 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 85 | 85 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 77 | 76 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*