**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 220330Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-21_1524.md · forecaster: manual/opus-5/unattested · 4 accepted / 0 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260822-17 | 55% | 2026-10-30 | cyber | The CISA Known Exploited Vulnerabilities catalog carries an entry for CVE-2026-19478 with a dateAdded value between 2026-08-21 and 2026-10-23. | TRUE if the CISA KEV JSON feed contains cveID CVE-2026-19478 with a dateAdded on or after 2026-08-21 and on or before 2026-10-23; otherwise FALSE. |
| KKR-20260822-18 | 18% | 2026-12-04 | cyber | CISA adds at least one vulnerability whose vendorProject field is Siemens to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-21 and 2026-11-27. | TRUE if the CISA KEV JSON feed holds at least one record with vendorProject equal to Siemens and dateAdded inside that range; otherwise FALSE. |
| KKR-20260822-19 | 65% | 2027-01-22 | political | At least one Hong Kong Alliance vigil organiser convicted on 2026-08-21 receives an unsuspended custodial sentence handed down between 2026-08-21 and 2027-01-15. | TRUE if a Hong Kong court imposes imprisonment, not wholly suspended, on at least one convicted organiser inside that range, per two of Reuters, AFP, AP, BBC, SCMP; otherwise FALSE. |
| KKR-20260822-20 | 45% | 2026-12-18 | crime_security | Swedish prosecutors file an indictment against at least one suspect over the 2026-08-21 Swedish school sword attack, with the filing occurring between 2026-08-21 and 2026-12-11. | TRUE if Swedish Prosecution Authority or court records show an indictment filed inside that range for this attack, confirmed by two of SVT, TT, Reuters, BBC, AFP; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

851 issued all-time across 14 forecaster arms · 761 open (32 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 92 issued · 92 open · nothing resolved yet — this arm earns a score at its first resolution.

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
| manual/fable-5/unattested | 72 | 72 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 92 | 92 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 85 | 84 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*