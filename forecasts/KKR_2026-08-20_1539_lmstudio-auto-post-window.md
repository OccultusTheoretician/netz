**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 201539Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-20_1537.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260820-01 | 25% | 2026-09-02 | disaster | Between 2026-08-21 and 2026-08-24, a magnitude 5.5 or higher earthquake will be recorded by the USGS in the region of Dunhuang, China. | The USGS Significant Quakes feed records a magnitude 5.5 or higher earthquake with a location within 100 km of Dunhuang, China, between 2026-08-21 and 2026-08-24. |
| KKR-20260820-02 | 35% | 2026-09-03 | cyber | Between 2026-08-21 and 2026-08-24, a coordinated cyberattack exploiting the Zimbra SNMP flaw will be confirmed by two independent sources. | Two independent sources confirm a cyberattack exploiting the Zimbra SNMP flaw (CVE-2026-XXXXX) occurred between 2026-08-21 and 2026-08-24. |
| KKR-20260820-03 | 60% | 2026-08-28 | economics/markets | Between 2026-08-21 and 2026-08-24, the US Treasury will announce a bond buyback operation exceeding $4 billion. | The US Treasury announces a bond buyback operation with a total value exceeding $4 billion between 2026-08-21 and 2026-08-24. |
| KKR-20260820-04 | 40% | 2026-09-02 | military/conflict | Between 2026-08-21 and 2026-08-24, a new military offensive will be reported in the Zaporizhzhia region with confirmed casualties. | Two or more independent sources report a new military offensive in the Zaporizhzhia region with confirmed casualties between 2026-08-21 and 2026-08-24. |
| KKR-20260820-05 | 30% | 2026-09-03 | disaster | Between 2026-08-21 and 2026-08-24, a tropical cyclone with Category 3 or higher intensity will be reported by GDACS. | GDACS Alerts records a tropical cyclone with Category 3 or higher intensity between 2026-08-21 and 2026-08-24. |
| KKR-20260820-06 | 20% | 2026-09-02 | political | Between 2026-08-21 and 2026-08-24, a new ceasefire agreement will be reported in the Israel-Gaza-Levant Theatre with confirmation from both Israeli and Palestinian sources. | Two independent sources, one from Israel and one from Palestine, confirm the establishment of a ceasefire agreement in the Israel-Gaza-Levant Theatre between 2026-08-21 and 2026-08-24. |
| KKR-20260820-07 | 35% | 2026-09-03 | cyber | Between 2026-08-21 and 2026-08-24, a major cyberattack on a critical infrastructure system in the United States will be confirmed by CISA. | CISA issues a public advisory confirming a major cyberattack on a critical infrastructure system in the United States between 2026-08-21 and 2026-08-24. |
| KKR-20260820-08 | 45% | 2026-08-28 | political | Between 2026-08-21 and 2026-08-24, a new political scandal involving a senior U.S. official will be reported by two major wire services. | Two major wire services report a new political scandal involving a senior U.S. official between 2026-08-21 and 2026-08-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-21 and 2026-08-24, the CISA KEV catalog will include CVE-2026-64849 with a date-added value of 2026-08-19." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-64849 dateAdded 2026-08-19, before the claimed window 2026-08-21..2026-08-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-08-21 and 2026-08-24, the S&P 500 will close above 7,700 points on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

803 issued all-time across 14 forecaster arms · 713 open (14 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 113 issued · 101 open · 10 resolved · 2 hits / 8 misses · **Brier 0.240** against its own base rate 20.0% (climatological 0.160) · **skill -0.502** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 186 | 178 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 113 | 101 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 69 | 68 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*