**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 071749Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-07_1747.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260807-01 | 32% | 2026-08-21 | military/conflict | A drone strike in Zaporizhzhia, Ukraine, results in at least one casualty between 2026-08-10 and 2026-08-17. | At least one report from a credible news outlet (BBC World, Al Jazeera, or Guardian World) published between 2026-08-12 and 2026-08-19 confirms a drone strike in Zaporizhzhia with at least one casualty. |
| KKR-20260807-02 | 25% | 2026-08-21 | military/conflict | A ceasefire agreement between Israel and Hamas is confirmed by both sides via a joint statement between 2026-08-10 and 2026-08-17. | A joint statement from both Israel and Hamas, published by at least two independent outlets (e.g., BBC World, Al Jazeera, Guardian World), confirms a ceasefire agreement between 2026-08-10 and 2026-08-17. |
| KKR-20260807-03 | 30% | 2026-08-21 | disaster | A new tropical cyclone named CHAN-HOM-26 causes at least one fatality in a country affected by the storm between 2026-08-10 and 2026-08-17. | At least one credible news report (BBC World, Al Jazeera, Guardian World) published between 2026-08-12 and 2026-08-19 confirms a fatality linked to CHAN-HOM-26 in a country affected by the storm. |
| KKR-20260807-04 | 22% | 2026-08-21 | political | A new political scandal involving Todd Blanche, U.S. Attorney General nominee, is confirmed by two independent outlets between 2026-08-10 and 2026-08-17. | Two independent news outlets (e.g., Guardian World, CNBC, BBC World) publish reports between 2026-08-12 and 2026-08-19 confirming a new political scandal involving Todd Blanche. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A cyberattack exploiting CVE-2026-8037 in Progress LoadMaster occurs between 2026-08-10 and 2026-08-17, resulting in unauthorized access to " → REJECTED: the resolution names a different subject than the statement — the claim is about CVE, LoadMaster, Progress and the resolution settles on CISA, KEV. A row whose resolution checks a different fact can be scored correct while being wrong; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-8037 dateAdded 2026-08-07, before the claimed window 2026-08-10..2026-08-17; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "A new cyberattack chain targeting Microsoft 365 users via AitM phishing is confirmed by a third-party security firm between 2026-08-10 and 2" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "The S&P 500 closes above 7,800 on a single trading day between 2026-08-10 and 2026-08-17." → REJECTED: resolution offers alternative VENUES joined by 'or' (…d by the federal reserve economic data (fred) | or | a major financial exchange…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The European Central Bank announces a 0.25 percentage point interest rate increase between 2026-08-10 and 2026-08-17." → REJECTED: resolution offers alternative VENUES joined by 'or' (…the ecb's official website | or | a major financial news outlet (e…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about Bank, Central, European and the resolution settles on BBC, CNBC, ECB, World. A row whose resolution checks a different fact can be scored correct while being wrong
- "A major cyberattack disrupts operations at a U.S. port, confirmed by a federal agency or major news outlet between 2026-08-10 and 2026-08-17" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "A new drought-related power disruption occurs in a Danube country, confirmed by a government or international agency report between 2026-08-" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

364 issued all-time across 14 forecaster arms · 319 open (2 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 27 issued · 25 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 40 | 40 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 27 | 25 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 21 | 31 | 9 | 22 | 0.222 | 29.0% | 0.206 | -0.075 |
| manual/fable | 45 | 44 | 1 | 1 | 0 | 0.360 | 100.0% | 0.000 | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 12 | 12 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 31 | 31 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*