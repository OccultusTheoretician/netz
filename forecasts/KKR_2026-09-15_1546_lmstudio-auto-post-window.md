**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 151546Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-15_1544.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260915-01 | 25% | 2026-10-07 | military/conflict | Between 2026-09-21 and 2026-09-24, at least one drone strike will be reported in Gaza City by two or more independently biased sources across hostile sides. | At least one drone strike in Gaza City is reported by two or more independently biased sources across hostile sides (AXIS, IL, PS) within the event window. |
| KKR-20260915-02 | 45% | 2026-10-08 | economics/markets | Between 2026-09-21 and 2026-09-24, the 10-year Treasury yield will exceed 5.00 percent at the close of any trading day. | The 10-year Treasury yield exceeds 5.00 percent at the close of any trading day between 2026-09-21 and 2026-09-24. |
| KKR-20260915-03 | 35% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting the VMware vCenter RCE flaw (CVE-2026-76461) will be reported by two or more independent sources. | Two or more independent sources report a confirmed cyberattack exploiting CVE-2026-76461 in the wild between 2026-09-21 and 2026-09-24. |
| KKR-20260915-04 | 20% | 2026-10-07 | disaster | Between 2026-09-21 and 2026-09-24, a major flood warning will be issued by the US National Weather Service for at least one county in Iowa. | The US National Weather Service issues a major flood warning for at least one county in Iowa between 2026-09-21 and 2026-09-24. |
| KKR-20260915-05 | 30% | 2026-10-07 | political | Between 2026-09-21 and 2026-09-24, the US Supreme Court will issue a ruling rejecting a challenge to mail-in voting procedures. | The US Supreme Court issues a ruling rejecting a challenge to mail-in voting procedures between 2026-09-21 and 2026-09-24. |
| KKR-20260915-06 | 25% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a confirmed attack on a critical infrastructure system in the United States will be reported by two or more independent sources. | Two or more independent sources report a confirmed attack on a critical infrastructure system in the United States between 2026-09-21 and 2026-09-24. |
| KKR-20260915-07 | 15% | 2026-10-07 | political | Between 2026-09-21 and 2026-09-24, Iran will announce a new diplomatic initiative involving China and the United States. | Iran announces a new diplomatic initiative involving China and the United States between 2026-09-21 and 2026-09-24. |
| KKR-20260915-08 | 20% | 2026-10-08 | cyber | Between 2026-09-21 and 2026-09-24, a confirmed cyberattack using the BambooToken malware will be reported by two or more independent sources. | Two or more independent sources report a confirmed cyberattack using BambooToken malware between 2026-09-21 and 2026-09-24. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include CVE-2026-76461 with a date-added value of 2026-09-14." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-76461 dateAdded 2026-09-14, before the claimed window 2026-09-21..2026-09-24; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-24, the S&P 500 will close below 7,500.00 on at least one trading day." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date

## III. LEDGER STANDING

2147 issued all-time across 16 forecaster arms · 1811 open (101 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 273 issued · 144 open · 120 resolved · 26 hits / 94 misses · **Brier 0.195** against its own base rate 21.7% (climatological 0.170) · **skill -0.151**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 706 | 668 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 273 | 144 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 231 | 228 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 244 | 238 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*