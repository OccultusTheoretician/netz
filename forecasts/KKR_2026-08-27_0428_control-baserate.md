**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 270428Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-25_1517.md · forecaster: control/baserate · 4 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260827-45 | 50% | 2026-12-02 | military/conflict | Between 2026-08-26 and 2026-11-30, a Russian presidential decree ordering a new general or partial mobilization of citizens into the armed forces is published on the official legal portal publication.pravo.gov.ru. | TRUE if publication.pravo.gov.ru carries a presidential decree dated 2026-08-26 through 2026-11-30 ordering general or partial mobilization of citizens; routine conscription-campaign and reservist training-assembly decrees do not count. |
| KKR-20260827-46 | 25% | 2026-09-01 | economics/markets | Nvidia (NVDA) official Nasdaq closing price on 2026-08-27, the session after its scheduled 2026-08-26 after-close earnings release, is more than 5.0 percent above or below its 2026-08-26 official close. | TRUE if the Nasdaq official closing price of NVDA on 2026-08-27 differs from the 2026-08-26 official close by more than 5.0 percent in either direction; a move of exactly 5.0 percent or less is FALSE. |
| KKR-20260827-47 | 23% | 2026-11-03 | cyber | Between 2026-08-26 and 2026-10-31, CISA adds to the Known Exploited Vulnerabilities catalog at least one Zimbra Collaboration vulnerability other than CVE-2026-73570. | TRUE if the CISA KEV catalog JSON contains an entry whose vendorProject or product field includes Zimbra, with a dateAdded value 2026-08-26 through 2026-10-31, and a cveID other than CVE-2026-73570. |
| KKR-20260827-48 | 33% | 2026-10-19 | disaster | On at least one day between 2026-08-26 and 2026-10-15, the Singapore National Environment Agency 24-hour PSI for at least one of the five reporting regions reaches 101 or higher. | TRUE if NEA published 24-hour PSI data (data.gov.sg historical PSI or NEA haze page) shows a value of 101 or higher for any region on any day 2026-08-26 through 2026-10-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-25 and 2026-10-31, the HHS Office for Civil Rights breach portal posts an entry naming Nutex Health or a Nutex-affiliated ho" → REJECTED: event window opens 2026-08-25, before this row is sealed (2026-08-26, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

971 issued all-time across 14 forecaster arms · 881 open (75 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 212 issued · 204 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 212 | 204 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 152 | 140 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 114 | 114 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 102 | 101 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*