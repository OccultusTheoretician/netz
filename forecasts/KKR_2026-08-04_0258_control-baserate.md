**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 040258Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-03_1501.md · forecaster: control/baserate · 7 accepted / 0 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260804-42 | 25% | 2026-08-27 | military/conflict | Israel and Palestinian armed factions in Gaza will be reported to have observed a continuous halt in strikes lasting at least 48 hours, beginning between 2026-08-04 and 2026-08-24. | True if two or more wire services or the UN report a Gaza ceasefire holding at least 48 continuous hours with a start date between 2026-08-04 and 2026-08-24, confirmed by 2026-08-27. |
| KKR-20260804-43 | 25% | 2026-08-28 | crime/security | A UN body, the ICC, or a major human rights organization will announce it has opened a formal investigation into the 2026-08-03 Sudan army drone strike on a court session, between 2026-08-04 and 2026-08-25. | True if the UN, ICC, or a named human rights organization publicly announces a formal investigation or fact-finding inquiry into the strike, with the announcement dated between 2026-08-04 and 2026-08-25, confirmed by 2026-08-28. |
| KKR-20260804-44 | 25% | 2026-09-08 | economics/markets | AstraZeneca and Bristol Myers Squibb will announce a signed definitive merger or acquisition agreement between 2026-08-04 and 2026-09-04. | True if both companies issue a joint press release or regulatory filing confirming a signed definitive agreement, dated between 2026-08-04 and 2026-09-04, confirmed by 2026-09-08. |
| KKR-20260804-45 | 25% | 2027-01-06 | economics/markets | The Federal Reserve will raise its federal funds target range above the level in effect on 2026-08-03, in an FOMC decision announced between 2026-08-10 and 2026-12-31. | True if an FOMC post-meeting statement dated between 2026-08-10 and 2026-12-31 raises the target range above its 2026-08-03 level, confirmed via the Federal Reserve press release by 2027-01-06. |
| KKR-20260804-46 | 25% | 2026-08-21 | cyber | The CISA Known Exploited Vulnerabilities catalog will add an entry for the N-able N-central vulnerability described in the 2026-08-03 report, with the addition dated between 2026-08-04 and 2026-08-18. | True if the CISA KEV catalog lists an N-able N-central CVE with a date-added field between 2026-08-04 and 2026-08-18, confirmed by checking the catalog on 2026-08-21. |
| KKR-20260804-47 | 25% | 2026-08-24 | political | The US Senate will hold a floor vote resulting in confirmation or rejection of the pending nomination of Todd Blanche, between 2026-08-04 and 2026-08-21. | True if the Senate floor vote record (Congress.gov or a wire service) shows a confirmation or rejection vote on the nomination of Todd Blanche dated between 2026-08-04 and 2026-08-21, confirmed by 2026-08-24. |
| KKR-20260804-48 | 25% | 2026-08-24 | disaster | The wildfire(s) reported destroying homes and forcing evacuations near Spokane, Washington on 2026-08-03 will reach full containment, as reported by state or federal fire authorities, between 2026-08-04 and 2026-08-21. | True if Washington state fire authorities or InciWeb report the Spokane-area wildfire(s) at 100 percent containment, with the containment date between 2026-08-04 and 2026-08-21, confirmed by 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

303 issued all-time across 14 forecaster arms · 268 open (3 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 25 issued · 25 open · nothing resolved yet — this arm earns a score at its first resolution.

*11 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 25 | 25 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 8 | 8 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 28 | 24 | 6 | 18 | 0.224 | 25.0% | 0.188 | -0.197 |
| manual/fable | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable-5 | 20 | 20 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 5 | 5 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 50 | 50 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 19 | 19 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 16 | 16 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*