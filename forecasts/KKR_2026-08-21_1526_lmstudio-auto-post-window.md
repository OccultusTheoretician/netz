**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 211526Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260821-01 | 30% | 2026-09-03 | military/conflict | A drone strike targeting a military installation in Kyiv, Ukraine, occurs between 2026-08-22 and 2026-08-28, resulting in at least one confirmed casualty. | At least one confirmed casualty is reported by two independent, hostile-side news outlets (e.g., one Russian and one Ukrainian) within 48 hours of the event window's end, with the strike location confirmed as Kyiv. |
| KKR-20260821-02 | 25% | 2026-09-03 | cyber | The CISA KEV catalog will include at least one new vulnerability with a CVSS score of 10.0 between 2026-08-22 and 2026-08-28. | The CISA KEV catalog carries a date-added value between 2026-08-22 and 2026-08-28 for a vulnerability with a CVSS score of 10.0. |
| KKR-20260821-03 | 20% | 2026-09-03 | disaster | A magnitude 6.0 or greater earthquake will be recorded by the USGS in Indonesia between 2026-08-22 and 2026-08-28. | The USGS Significant Quakes database records a seismic event with magnitude ≥6.0 and depth ≤100km in Indonesia between 2026-08-22 and 2026-08-28. |
| KKR-20260821-04 | 30% | 2026-09-03 | political | A major political scandal involving a U.S. federal official will be reported by at least two major outlets (e.g., CNN, The New York Times, The Guardian) between 2026-08-22 and 2026-08-28. | At least two major news outlets (e.g., CNN, The New York Times, The Guardian) publish a report detailing a political scandal involving a U.S. federal official between 2026-08-22 and 2026-08-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Bitcoin will close above $85,000 on a weekday between 2026-08-22 and 2026-08-28." → REJECTED: resolution offers alternative VENUES joined by 'or' (…than $85,000, as reported by a major exchange | or | financial data provider such as fred or bloom…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A cyberattack exploiting CVE-2026-72530 will be confirmed by CISA or a major news outlet between 2026-08-22 and 2026-08-28." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A wildfire will be reported to have caused at least one fatality in the U.S. between 2026-08-22 and 2026-08-28." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A new U.S. tariff on imported ground beef will be implemented by the Trump administration between 2026-08-22 and 2026-08-28." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively; the resolution names only a venue or register (CNBC, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A cyberattack using AI-generated exploit scripts targeting Siemens S7 PLCs will be confirmed by a major news outlet between 2026-08-22 and 2" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A major cyberattack will be reported to have disrupted a U.S. federal agency's operations between 2026-08-22 and 2026-08-28." → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

831 issued all-time across 14 forecaster arms · 741 open (20 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 117 issued · 105 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

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
| manual/fable-5/unattested | 67 | 67 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 85 | 85 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 77 | 76 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*