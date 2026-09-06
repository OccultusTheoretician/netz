**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 062247Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-06_1517.md · forecaster: control/baserate · 7 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260906-94 | 49% | 2026-10-15 | military_conflict | Between 2026-09-13 and 2026-10-13, CENTCOM, the U.S. Department of Defense, or the Israeli Defense Forces will confirm at least one coalition service member killed or wounded in action from Iranian or IRGC-aligned action in the Strait of Hormuz, Gulf of Oman, or wider Persian Gulf theater. | TRUE if CENTCOM, DoD, or IDF confirms, with wire-service corroboration (Reuters, AP, or AFP), a coalition KIA or WIA from Iranian or IRGC-aligned action in the Hormuz theater between 2026-09-13 and 2026-10-13. FALSE otherwise by 2026-10-15. |
| KKR-20260906-95 | 35% | 2026-11-15 | political | Between 2026-09-13 and 2026-11-13, the governments of Ukraine and Russia will both publicly confirm a mutual ceasefire or comprehensive halt to hostilities in the Russia-Ukraine war, following the Witkoff-Kushner shuttle diplomacy in Kyiv. | TRUE if both Ukraine's government and Russia's government confirm, with independent wire corroboration, a mutual ceasefire or halt to hostilities between 2026-09-13 and 2026-11-13. FALSE otherwise by 2026-11-15. |
| KKR-20260906-96 | 35% | 2026-11-15 | political | Between 2026-09-13 and 2026-11-13, the UK Electoral Commission will confirm it has opened a formal investigation into Reform UK over the overseas donations reporting Nigel Farage acknowledged looked damaging on 2026-09-06. | TRUE if the Electoral Commission confirms, corroborated by a UK national outlet, an open formal investigation into Reform UK's donation reporting between 2026-09-13 and 2026-11-13. FALSE otherwise by 2026-11-15. |
| KKR-20260906-97 | 21% | 2026-09-16 | economic | On 2026-09-16, the Federal Open Market Committee will raise its federal funds target range above the current 3.50 to 3.75 percent range. Reference: 3.50-3.75 percent target range in effect on the packet date, 2026-09-06. | TRUE if the FOMC statement released 2026-09-16 sets a new target range with a lower bound above 3.50 percent, i.e. any hike. FALSE if the range is held at 3.50-3.75 percent or cut. |
| KKR-20260906-98 | 21% | 2026-11-02 | economic | Between 2026-09-13 and 2026-11-01, Freddie Mac's Primary Mortgage Market Survey will report a weekly average 30-year fixed mortgage rate of 7.25 percent or higher on at least one release. Reference: approximately 7.00 percent as reported 2026-09-05. | TRUE if any Freddie Mac PMMS release between 2026-09-13 and 2026-11-01 reports the 30-year fixed average at or above 7.25 percent. FALSE if every release in the window is below 7.25 percent. |
| KKR-20260906-99 | 30% | 2026-10-27 | cyber | Between 2026-09-13 and 2026-10-27, the CISA Known Exploited Vulnerabilities catalog will add an entry for Adobe Commerce or Magento Open Source tied to the zero-day exploitation reported on 2026-09-05. | TRUE if the CISA KEV catalog lists an Adobe Commerce or Magento Open Source entry with dateAdded between 2026-09-13 and 2026-10-27. FALSE if no such entry appears by then. |
| KKR-20260906-100 | 36% | 2026-10-15 | disaster_infrastructure | Between 2026-09-13 and 2026-10-13, a further eruption of Mount Anak Krakatau will trigger a new suspension of flight operations at Soekarno-Hatta International Airport near Jakarta, following the multi-airport disruption on 2026-09-06. | TRUE if Angkasa Pura, Indonesia's transport ministry, or a NOTAM confirms a new Anak Krakatau ash suspension at Soekarno-Hatta, corroborated by a wire service, between 2026-09-13 and 2026-10-13. FALSE otherwise by 2026-10-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-13 and 2026-10-04, Victoria Police will confirm the arrest of the suspect sought over the 2026-09-06 alleged axe attack that" → REJECTED: resolution offers alternative VENUES joined by 'or' (…wire | or | national…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1591 issued all-time across 16 forecaster arms · 1326 open (89 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 465 issued · 437 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 465 | 437 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 224 | 136 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 16 | 16 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 173 | 171 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 192 | 186 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 180 | 159 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*