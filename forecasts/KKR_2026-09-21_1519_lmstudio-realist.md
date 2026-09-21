**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 211519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-21_1516.md · forecaster: lmstudio/realist · 5 accepted / 5 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260921-09 | 15% | 2026-10-01 | economics/markets | On or before 2026-09-26, the U.S. Federal Reserve will announce a 25 basis point increase in the federal funds rate, as confirmed by the Federal Reserve's official press release. | The Federal Reserve's official press release confirms a 25 basis point increase in the federal funds rate on or before 2026-09-26. |
| KKR-20260921-10 | 20% | 2026-10-03 | disaster | Between 2026-09-25 and 2026-09-28, a major earthquake of magnitude 6.5 or higher will be recorded in the Pacific Ring of Fire, as confirmed by the USGS Significant Quakes feed. | The USGS Significant Quakes feed records a magnitude 6.5 or higher earthquake in the Pacific Ring of Fire between 2026-09-25 and 2026-09-28. |
| KKR-20260921-11 | 40% | 2026-10-04 | political | Between 2026-09-26 and 2026-09-29, a new political alliance between seven Ethiopian rebel groups will be confirmed by at least two independent news outlets (one from a Western source, one from an African source). | At least two independent news outlets (one from a Western source, one from an African source) confirm the formation of a new political alliance among seven Ethiopian rebel groups between 2026-09-26 and 2026-09-29. |
| KKR-20260921-12 | 30% | 2026-10-05 | cyber | Between 2026-09-27 and 2026-10-01, a cyberattack targeting a U.S. federal agency will be confirmed by two or more independent sources (one from a Western outlet, one from a non-Western outlet), with the attack involving a PowerShell backdoor. | Two or more independent sources (one from a Western outlet, one from a non-Western outlet) confirm a cyberattack on a U.S. federal agency involving a PowerShell backdoor between 2026-09-27 and 2026-10-01. |
| KKR-20260921-13 | 35% | 2026-10-06 | disaster | Between 2026-09-30 and 2026-10-04, a major flood event in the U.S. Midwest will be confirmed by the National Weather Service, with at least one flood warning or watch issued for a county in Iowa or Ohio. | The National Weather Service issues at least one flood warning or watch for a county in Iowa or Ohio between 2026-09-30 and 2026-10-04. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "On 2026-09-22, a drone strike targeting a military installation in Kyiv, Ukraine, will be confirmed by at least two independently biased sou" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-23 and 2026-09-25, the S&P 500 will close above 7,800 points on at least one trading day, based on the prior-session close o" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-24 and 2026-09-27, a cyberattack exploiting a vulnerability in Microsoft Office applications will be confirmed by at least t" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Between 2026-09-28 and 2026-10-02, a new U.S. military strike on a drone launch site in Syria will be confirmed by at least two independentl" → REJECTED: negated-observation clause — 'with no X reported' is a claim about the source record, not about the event. The war desk prints it to describe its own reports; it cannot be adjudicated as a property of the world
- "Between 2026-09-29 and 2026-10-03, a new cyberattack exploiting a zero-day vulnerability in Cisco networking devices will be confirmed by at" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

2612 issued all-time across 16 forecaster arms · 2146 open (167 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/realist`:** 101 issued · 96 open · 5 resolved · 4 hits / 1 misses · **Brier 0.373** against its own base rate 80.0% (climatological 0.160) · **skill -1.334** · under 30 resolved, this is noise.

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
| lmstudio/realist | 101 | 96 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
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