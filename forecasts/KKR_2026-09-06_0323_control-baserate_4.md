**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 060323Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: control/baserate · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-50 | 49% | 2026-12-04 | military_conflict | Russia and Ukraine jointly announce a ceasefire covering the entire line of contact, taking effect between 2026-09-06 and 2026-11-30. | TRUE only if both the Kremlin and the Ukrainian presidency announce a front-wide ceasefire taking effect in the window. Partial, capital-specific, or energy-infrastructure-only pauses do not count. |
| KKR-20260906-51 | 49% | 2026-10-22 | military_conflict | Yemeni government or Saudi-led coalition forces announce the capture of a named district in Houthi-held Hodeidah, al-Jawf, or Saada governorate, between 2026-09-08 and 2026-10-19. | TRUE if a government or coalition claim of capturing a named district in those three governorates in the window is corroborated by Houthi-aligned media or by Reuters, AFP, or AP. |
| KKR-20260906-52 | 30% | 2026-11-24 | cyber | The CISA Known Exploited Vulnerabilities catalog carries an entry for CVE-2026-19490, the Citrix NetScaler authentication bypass, added between 2026-09-06 and 2026-11-20. | TRUE if the CISA KEV JSON feed contains CVE-2026-19490 with a dateAdded value between 2026-09-06 and 2026-11-20 inclusive. |
| KKR-20260906-53 | 36% | 2026-12-15 | crime_security | The Plymouth County District Attorney publicly announces that Massachusetts will retry Lindsay Clancy, between 2026-09-08 and 2026-12-11. | TRUE if that office states in the window that it intends to retry Clancy, reported by at least two of AP, Reuters, Boston Globe, WCVB, WBZ. |
| KKR-20260906-54 | 36% | 2026-10-23 | disaster_infrastructure | The USGS earthquake catalog records at least two events of magnitude 7.0 or greater worldwide between 2026-09-08 and 2026-10-19. | TRUE if a USGS ComCat query bounded by 2026-09-08 and 2026-10-19 returns two or more events of magnitude 7.0 or greater. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "US Central Command announces at least one new strike that disables, destroys, or seizes an Iranian or Iran-linked vessel, occurring between " → REJECTED: resolution offers alternative VENUES joined by 'or' (…centcom | or | defense department…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A Russian missile or drone strike inside Kyiv city limits occurs between 2026-09-09 and 2026-09-30, after the three-day pause on strikes on " → REJECTED: resolution offers alternative VENUES joined by 'or' (…russian-side | or | western…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Front-month Brent crude settles at or above 110.00 US dollars per barrel on at least one trading day between 2026-09-08 and 2026-10-30. Refe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Front-month NYMEX WTI settles at or below 85.00 US dollars per barrel on at least one trading day between 2026-09-08 and 2026-11-13. Referen" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The AfD wins an absolute majority of seats in the Saxony-Anhalt Landtag in the state election held on 2026-09-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1545 issued all-time across 16 forecaster arms · 1280 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 458 issued · 430 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 458 | 430 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 11 | 11 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 168 | 166 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 185 | 179 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 173 | 152 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*