**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241517Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-24_1512.md · forecaster: lmstudio/qwen36 · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261024-10 | 15% | 2026-11-09 | disaster | A magnitude 6.5 or greater earthquake occurs in Vanuatu between 2026-11-02 and 2026-11-06 | The USGS Significant Quakes catalog carries an event with magnitude 6.5 or greater in Vanuatu with an event date between 2026-11-02 and 2026-11-06 |
| KKR-20261024-11 | 25% | 2026-11-09 | military | Israel imposes a full military lockdown on the West Bank between 2026-11-02 and 2026-11-06 | Two wire services report that Israel imposes a full military lockdown on the West Bank with an effective date between 2026-11-02 and 2026-11-06 |
| KKR-20261024-12 | 10% | 2026-11-09 | military | Iran conducts a kinetic strike on a US warship in the Strait of Hormuz between 2026-11-02 and 2026-11-06 | Two wire services report that Iran conducts a kinetic strike on a US warship in the Strait of Hormuz with an event date between 2026-11-02 and 2026-11-06 |
| KKR-20261024-13 | 10% | 2026-11-09 | disaster | A magnitude 7.0 or greater earthquake occurs in China between 2026-11-02 and 2026-11-06 | The USGS Significant Quakes catalog carries an event with magnitude 7.0 or greater in China with an event date between 2026-11-02 and 2026-11-06 |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "CISA adds a new CVE to the KEV catalog with a date-added value between 2026-10-27 and 2026-10-30" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "WTI Crude closes above 105.00 on any weekday between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "France passes a law or decree that explicitly suspends or overrides the right to strike in the public sector between 2026-11-02 and 2026-11-" → REJECTED: resolution offers alternative VENUES joined by 'or' (…french federal register | or | equivalent official…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact; the resolution names a different subject than the statement — the claim is about France and the resolution settles on Federal, French, Register. A row whose resolution checks a different fact can be scored correct while being wrong
- "Brent Crude closes above 115.00 on any weekday between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A new CVE is added to the CISA KEV catalog with a date-added value between 2026-11-02 and 2026-11-06" → REJECTED: the resolution names only a venue or register (CISA, KEV) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "S&P 500 closes below 7,500 on any weekday between 2026-11-02 and 2026-11-06" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

4849 issued all-time across 21 forecaster arms · 3497 open (681 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 108 issued · 107 open · 1 resolved · 1 hits / 0 misses · **Brier 0.722** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1701 | 1318 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 470 | 229 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 108 | 107 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 105 | 105 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 113 | 106 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 247 | 160 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 420 | 339 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 251 | 240 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 205 | 202 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*