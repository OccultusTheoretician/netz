**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182321Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-18_1518.md · forecaster: control/baserate · 5 accepted / 5 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260918-21 | 29% | 2026-10-20 | cyber | The critical Check Point root code-execution flaw reported 18 Sep 2026 is added to the CISA KEV catalog with a date-added value between 2026-09-18 and 2026-10-16. | TRUE if the CISA KEV JSON feed lists a Check Point entry with dateAdded between 2026-09-18 and 2026-10-16 inclusive matching the flaw in item 12; FALSE otherwise. |
| KKR-20260918-22 | 24% | 2026-10-20 | economics/markets | A Russian presidential decree placing Nestle Russian assets under temporary state management is published on the official legal portal publication.pravo.gov.ru between 2026-09-18 and 2026-10-16. | TRUE if publication.pravo.gov.ru or kremlin.ru carries a decree dated 2026-09-18 to 2026-10-16 inclusive naming Nestle entities for temporary management or asset transfer; FALSE otherwise. |
| KKR-20260918-23 | 61% | 2026-10-20 | military/conflict | The Philippine Coast Guard publicly reports a new collision, ramming, or water-cannon incident involving a Chinese government vessel in the South China Sea between 2026-09-19 and 2026-10-16. | TRUE if an official Philippine Coast Guard statement describes such an incident occurring 2026-09-19 to 2026-10-16 inclusive and at least one wire service (Reuters, AP, or AFP) reports it; FALSE otherwise. |
| KKR-20260918-24 | 61% | 2026-10-20 | military/conflict | UKMTO or JMIC issues an incident advisory for an attack on a merchant vessel in the Red Sea, Bab al-Mandeb, or Gulf of Aden occurring between 2026-09-19 and 2026-10-16. | TRUE if the UKMTO or JMIC public advisory feed records a projectile, drone, or boarding attack on a merchant vessel in those waters dated 2026-09-19 to 2026-10-16 inclusive; FALSE otherwise. |
| KKR-20260918-25 | 40% | 2026-10-22 | political | The US government files a notice of appeal against the district court ruling blocking demolition of the Kennedy Center, docketed between 2026-09-18 and 2026-10-19. | TRUE if the relevant federal district court docket on PACER or CourtListener shows a notice of appeal by the federal defendants entered 2026-09-18 to 2026-10-19 inclusive; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog adds at least one further Linux Kernel CVE, beyond CVE-2025-39964 and CVE-2026-53266, with a date-added value between 2" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2025-39964 dateAdded 2026-09-18, before the claimed window 2026-09-19..2026-10-16; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "ICE Brent front-month crude settles at or above 110.00 USD on at least one trading session between 2026-09-21 and 2026-10-30. Reference: 99." → REJECTED: resolution offers alternative VENUES joined by 'or' (…00 usd per barrel per ice | or | fred dcoilbrenteu…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Philippine prosecutors file criminal charges against a named suspect in the 18 Sep 2026 Philippines school shooting between 2026-09-18 and 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (… news agency and at least one of reuters, ap, | or | afp report a criminal complaint or informatio…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "USGS records an earthquake of magnitude 6.0 or greater within 300 km of the 18 Sep 2026 M6.5 Nikolski, Alaska event between 2026-09-18 and 2" → REJECTED: the resolution names a different subject than the statement — the claim is about Alaska, Nikolski, Sep, USGS and the resolution settles on USGS, us7000ti1p. A row whose resolution checks a different fact can be scored correct while being wrong
- "GDACS issues an Orange or Red tropical cyclone alert for a storm affecting Japan between 2026-09-18 and 2026-09-25." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ropical cyclone event with alert level orange | or | red listing japan among affected countries an…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2464 issued all-time across 16 forecaster arms · 1998 open (103 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 840 issued · 755 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 840 | 755 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 293 | 143 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 89 | 84 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 136 | 126 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 283 | 266 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 262 | 214 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*