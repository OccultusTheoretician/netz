**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 211517Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-21_1516.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260921-01 | 30% | 2027-01-10 | military/conflict | Between 2026-09-21 and 2026-09-24, a drone attack with reported casualties of 395 occurs in Kyiv, Ukraine, confirmed by at least two independently biased sources from RU and UA sides. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and the event is corroborated by at least two distinct outlets from RU and UA sides, each reporting the attack and casualties. |
| KKR-20260921-02 | 25% | 2027-01-10 | military/conflict | Between 2026-09-21 and 2026-09-24, a missile strike on Moscow, Russia, results in at least one confirmed fatality, verified by two independently biased sources from RU and UA sides. | The event is confirmed by at least two distinct outlets from RU and UA sides, each reporting a missile strike on Moscow with at least one confirmed fatality. |
| KKR-20260921-03 | 35% | 2027-01-10 | cyber | Between 2026-09-21 and 2026-09-24, a cyberattack exploiting a vulnerability listed in the CISA KEV catalog targets a U.S. federal agency, with public confirmation from at least two independent sources. | The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least two independent sources confirm a cyberattack on a U.S. federal agency using that vulnerability. |
| KKR-20260921-04 | 40% | 2027-01-10 | disaster | Between 2026-09-21 and 2026-09-24, a tropical cyclone named POLO-26 causes a Green alert in GDACS with population affected exceeding 1 million, confirmed by GDACS and at least one independent source. | The GDACS Alerts system carries a Green alert for tropical cyclone POLO-26 with population affected exceeding 1 million, and at least one independent source confirms the alert and impact. |
| KKR-20260921-05 | 20% | 2027-01-10 | cyber | Between 2026-09-21 and 2026-09-24, a new vulnerability in Microsoft Excel's copy-paste function is exploited in a widespread attack, confirmed by BleepingComputer and The Hacker News. | BleepingComputer and The Hacker News report a widespread exploit of a Microsoft Excel copy-paste flaw between 2026-09-21 and 2026-09-24, with evidence of active exploitation. |
| KKR-20260921-06 | 30% | 2027-01-10 | political | Between 2026-09-21 and 2026-09-24, Iran's President Pezeshkian delivers a speech at the United Nations General Assembly in New York, confirmed by at least two independent news outlets. | At least two independent news outlets (e.g., BBC, Al Jazeera, CNN) report that Iran's President Pezeshkian delivered a speech at the UNGA in New York between 2026-09-21 and 2026-09-24. |
| KKR-20260921-07 | 35% | 2027-01-10 | cyber | Between 2026-09-21 and 2026-09-24, a new cyberattack campaign using the TASK#STOMP PowerShell backdoor is reported by at least two independent sources, with evidence of data exfiltration. | At least two independent sources (e.g., BleepingComputer, The Hacker News) report a new cyberattack campaign using the TASK#STOMP PowerShell backdoor between 2026-09-21 and 2026-09-24, with evidence of data exfiltration. |
| KKR-20260921-08 | 25% | 2027-01-10 | disaster | Between 2026-09-21 and 2026-09-24, a major earthquake of magnitude 6.0 or higher occurs in Papua New Guinea, confirmed by USGS and at least one independent source. | The USGS Significant Quakes system records an earthquake of magnitude 6.0 or higher in Papua New Guinea between 2026-09-21 and 2026-09-24, and at least one independent source confirms the event. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-24, the S&P 500 index closes above 7,800 points, based on the final settlement price on a weekday." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day
- "Between 2026-09-21 and 2026-09-24, a new political scandal involving a U.S. federal official is reported by CNN, Politico, and MS NOW, with " → REJECTED: resolution offers alternative VENUES joined by 'or' (…ctment is confirmed by a federal court docket | or | official press release…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2607 issued all-time across 16 forecaster arms · 2141 open (167 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 317 issued · 167 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 896 | 811 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 317 | 167 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 96 | 91 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 147 | 137 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 242 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 306 | 289 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 284 | 236 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*