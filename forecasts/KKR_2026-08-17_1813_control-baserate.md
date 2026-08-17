**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 171813Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-17_1537.md · forecaster: control/baserate · 8 accepted / 3 rejected by validation gate · 7 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260817-46 | 23% | 2026-09-02 | cyber | Between 2026-08-17 and 2026-08-31, a cybersecurity vendor or outlet other than BleepingComputer, such as Krebs on Security, The Hacker News, Malwarebytes, SentinelOne, or Objective-See, publishes independent research naming and attributing the AmnesiaStealer macOS malware campaign. | TRUE if a named second security vendor or outlet publishes independent attribution of AmnesiaStealer between 2026-08-17 and 2026-08-31; otherwise FALSE. |
| KKR-20260817-47 | 50% | 2026-09-17 | military/conflict | The United States military strikes a target inside Oman between 2026-08-17 and 2026-09-14. | TRUE if Reuters, AP, or BBC report a US military strike on Omani territory or territorial waters between 2026-08-17 and 2026-09-14; FALSE otherwise. |
| KKR-20260817-48 | 25% | 2026-10-19 | economics/markets | WTI crude oil settles at or above 90.00 USD per barrel on any trading day between 2026-08-17 and 2026-10-15. | TRUE if the CME/NYMEX WTI front-month settlement price is at or above 90.00 USD per barrel on any trading day between 2026-08-17 and 2026-10-15; FALSE otherwise. |
| KKR-20260817-49 | 23% | 2026-09-17 | cyber | CISA adds a VMware vCenter Server CVE to the Known Exploited Vulnerabilities catalog with a Date Added value between 2026-08-17 and 2026-09-14. | TRUE if the CISA KEV catalog lists a VMware vCenter Server entry with Date Added between 2026-08-17 and 2026-09-14; FALSE otherwise. |
| KKR-20260817-50 | 23% | 2026-10-05 | cyber | Philips or GE publicly confirms data theft from the Clop-attributed breach between 2026-08-17 and 2026-09-30. | TRUE if a company statement, SEC filing, or wire report quotes Philips or GE confirming data theft between 2026-08-17 and 2026-09-30; FALSE if both remain in investigating or denied status. |
| KKR-20260817-51 | 29% | 2026-09-03 | political | Zambian prosecutors file formal criminal charges against at least one arrested opposition figure between 2026-08-17 and 2026-08-31. | TRUE if Reuters, AP, or BBC report formal charges filed against an arrested Zambian opposition figure between 2026-08-17 and 2026-08-31; FALSE otherwise. |
| KKR-20260817-52 | 33% | 2026-11-17 | disaster | The World Health Organization declares the Democratic Republic of the Congo Ebola outbreak a Public Health Emergency of International Concern between 2026-08-17 and 2026-11-14. | TRUE if the WHO Director-General publishes a PHEIC declaration naming the DRC Ebola outbreak between 2026-08-17 and 2026-11-14; FALSE otherwise. |
| KKR-20260817-53 | 31% | 2026-09-17 | crime/security | Virginia prosecutors file adult criminal charges against the campus shooting suspect between 2026-08-17 and 2026-09-14. | TRUE if a Virginia court record, AP, or BBC report states the suspect faces adult criminal charges between 2026-08-17 and 2026-09-14; FALSE if the case remains exclusively juvenile. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-08-17 and 2026-09-20, Qatar and Iran issue public statements that converge on a single account of the fate of the three Iranian" → REJECTED: cited items overlap the claim only on vocabulary common across the whole report — shared words are not shared content, and a prior that fits every item grounds none of them; cite an item carrying something specific to THIS claim; cited items overlap the claim only on vocabulary common across the whole report — shared words are not shared content, and a prior that fits every item grounds none of them; cite an item carrying something specific to THIS claim
- "Between 2026-08-17 and 2026-09-15, the United States government takes a formal, documented action asserting a sovereignty or territorial cla" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-08-17 and 2026-09-20, the US Navy or Department of Defense publicly confirms that USS George Washington has relieved USS Abraha" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

687 issued all-time across 14 forecaster arms · 597 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 138 issued · 130 open · 8 resolved · 1 hits / 7 misses · **Brier 0.125** against its own base rate 12.5% (climatological 0.109) · **skill -0.143** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 138 | 130 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 92 | 80 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 58 | 57 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*