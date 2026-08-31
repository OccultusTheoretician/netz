**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 312301Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-30_1516.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-18 | 53% | 2026-09-15 | military_conflict | The confirmed death toll from the Russian strike on a Ukrainian arms depot, reported at 38 on 2026-08-30, will be revised to 45 or higher by a Ukrainian official source or a major wire service between 2026-08-31 and 2026-09-13. | TRUE if Ukrainian officials, Reuters, AP, or AFP report a toll of 45 or more from this depot strike between 2026-08-31 and 2026-09-13; otherwise FALSE at deadline. |
| KKR-20260831-19 | 53% | 2026-10-19 | military_conflict | A commercial vessel transiting the Strait of Hormuz will be attacked, seized, or forcibly diverted, as reported by UKMTO, Reuters, or AP, between 2026-09-01 and 2026-10-15. | TRUE if UKMTO, Reuters, or AP report an attack, seizure, or forced diversion of a commercial vessel in the Strait of Hormuz within the window; otherwise FALSE. |
| KKR-20260831-20 | 44% | 2026-10-14 | political | Niger's military-led government will publicly announce formal charges or the opening of a court-martial against at least one soldier arrested in the late-August 2026 Niamey mutiny attempt, between 2026-08-31 and 2026-10-12. | TRUE if Niger's government, AFP, Reuters, or Al Jazeera report formal charges or a court-martial opened against at least one arrested soldier within the window; otherwise FALSE. |
| KKR-20260831-21 | 33% | 2026-09-29 | cyber | Manchester Airports Group, the ICO, or two independent outlets will confirm a data breach matching FulcrumSec's claimed August 2026 theft of 86 GB of data, between 2026-08-31 and 2026-09-27. | TRUE if MAG, the ICO, or two independent outlets confirm the breach, or verified stolen data surfaces on a leak marketplace, within the window; otherwise FALSE. |
| KKR-20260831-22 | 25% | 2026-11-16 | economic | The Federal Register will publish a rule or notice modifying Section 232 steel or aluminum tariff treatment specifically naming Canada, between 2026-09-01 and 2026-11-13. | TRUE if the Federal Register publishes a rule or notice modifying Section 232 steel or aluminum tariff treatment of Canada within the window; otherwise FALSE. |
| KKR-20260831-23 | 25% | 2026-11-16 | economic | The US Treasury OFAC recent-actions list will show a new or amended Venezuela general or specific license implementing the 65 billion barrel oil deal announced in late August 2026, between 2026-09-01 and 2026-11-13. | TRUE if OFAC's published recent actions list carries a new or amended Venezuela license tied to this deal within the window; otherwise FALSE. |
| KKR-20260831-24 | 52% | 2026-09-15 | disaster_infrastructure | The confirmed death toll from the Northern Cyprus ferry that capsized around 2026-08-30 with roughly 260 to 270 people aboard, six to seven confirmed dead as of 2026-08-30, will reach 15 or more per Cypriot, Turkish, or wire-service reporting, between 2026-08-31 and 2026-09-13. | TRUE if Cypriot or Turkish officials, Reuters, or AP report 15 or more confirmed dead from this ferry capsizing within the window; otherwise FALSE. |
| KKR-20260831-25 | 52% | 2026-09-29 | disaster_infrastructure | The confirmed death toll from the late-August 2026 Nepal-Tibet border floods and landslides, reported at approximately 750 with about 3000 still missing as of 2026-08-30, will exceed 900 per Nepali government or wire-service reporting, between 2026-08-31 and 2026-09-27. | TRUE if Nepal's government, Reuters, AP, or AFP report a confirmed death toll above 900 from this flood and landslide event within the window; otherwise FALSE. |
| KKR-20260831-26 | 43% | 2026-10-14 | crime_security | German prosecutors will file a formal murder (Mord) charge, rather than a lesser homicide charge, against the suspect arrested for the fatal stabbing of a British woman at Rosenheim train station, between 2026-08-31 and 2026-10-12. | TRUE if Bavarian prosecutors or a German wire service report a Mord charge specifically filed against the suspect within the window; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one of the five critical WordPress plugin or theme vulnerabilities reported by The Hacker News on 2026-08-29 will be added to the C" → REJECTED: the resolution names only a venue or register (CISA, KEV, cves) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1149 issued all-time across 14 forecaster arms · 988 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 290 issued · 273 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 290 | 273 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 114 | 113 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 135 | 132 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 130 | 122 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*