**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121720Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-12_1518.md · forecaster: control/baserate · 6 accepted / 0 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260812-33 | 33% | 2026-09-04 | cyber | A CVE tied to the Microsoft Defender ShieldBreak privilege-escalation flaw disclosed around 11 Aug 2026 will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded between 2026-08-13 and 2026-09-02. | TRUE if the CISA KEV catalog lists a CVE matching the ShieldBreak Defender flaw with dateAdded between 2026-08-13 and 2026-09-02, checked 2026-09-04; otherwise FALSE. |
| KKR-20260812-34 | 33% | 2026-09-04 | military_conflict | A Houthi or other Iran-aligned attack will kill at least one person in Red Sea, Gulf of Aden, or Strait of Hormuz shipping-lane activity between 2026-08-13 and 2026-09-02, beyond the fatalities already reported 12 Aug 2026. | TRUE if two or more wire services report a fatal Houthi or Iran-aligned attack on shipping or shipping-adjacent targets in the Red Sea, Gulf of Aden, or Strait of Hormuz corridor between 2026-08-13 and 2026-09-02, checked 2026-09-04. |
| KKR-20260812-35 | 33% | 2026-09-04 | military_conflict | Russia will board, detain, or seize a European Union-flagged or EU-owned commercial vessel between 2026-08-13 and 2026-09-02, consistent with the tit-for-tat seizure warning reported 12 Aug 2026. | TRUE if two or more wire services or hostile-side channels confirm Russian authorities boarded, detained, or seized an EU-flagged or EU-owned vessel between 2026-08-13 and 2026-09-02, checked 2026-09-04. |
| KKR-20260812-36 | 33% | 2026-08-21 | political | Hakainde Hichilema will be declared winner of Zambia's 13 August 2026 presidential election outright in the first round, with more than 50 percent of valid votes, by 2026-08-21. | TRUE if the Electoral Commission of Zambia declares Hichilema the first-round winner with over 50 percent of valid votes by 2026-08-21; a runoff or another winner resolves FALSE. |
| KKR-20260812-37 | 33% | 2026-09-14 | disaster_infrastructure | A magnitude 6.0 or greater aftershock will be recorded by USGS within the epicentral region of the 12 Aug 2026 M7.4 Colombia earthquake between 2026-08-13 and 2026-09-11. | TRUE if USGS lists a magnitude 6.0-plus event within 200 km of the M7.4 Colombia mainshock, dated between 2026-08-13 and 2026-09-11, checked 2026-09-14; otherwise FALSE. |
| KKR-20260812-38 | 33% | 2026-09-04 | crime_security | The Egyptian student whose kidnapping was livestreamed, per the report dated 12 Aug 2026, will be confirmed located, released, or recovered by two or more sources between 2026-08-13 and 2026-09-02. | TRUE if two or more news sources confirm the student has been located, released, or recovered, dated between 2026-08-13 and 2026-09-02, checked 2026-09-04; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

555 issued all-time across 14 forecaster arms · 499 open (0 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 89 issued · 89 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 89 | 89 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 10 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 57 | 55 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[pre-verbot] | 60 | 16 | 36 | 11 | 25 | 0.234 | 30.6% | 0.212 | -0.101 |
| manual/fable | 45 | 40 | 5 | 2 | 3 | 0.198 | 40.0% | 0.240 | +0.174 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 26 | 26 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 74 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 44 | 44 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 43 | 2 | 1 | 1 | 0.265 | 50.0% | 0.250 | -0.060 |
| manual/sonnet-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| operator/human | 6 | 3 | 0 | — | — | not computed | — | — | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*