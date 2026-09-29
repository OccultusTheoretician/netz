**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-29_1517.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260929-01 | 95% | 2026-10-06 | cyber | On 2026-09-30, the CISA KEV catalog will include CVE-2026-86950 with a date-added value of 2026-09-29. | The CISA KEV catalog carries a date-added value of 2026-09-29 for CVE-2026-86950. |
| KKR-20260929-02 | 25% | 2026-10-08 | cyber | Between 2026-09-29 and 2026-10-06, a new vulnerability in the OpenAI GPT-6.1 Astra model is publicly disclosed and exploited in at least one real-world attack. | A new vulnerability in the OpenAI GPT-6.1 Astra model is publicly disclosed and exploited in at least one real-world attack between 2026-09-29 and 2026-10-06. |
| KKR-20260929-03 | 30% | 2026-10-08 | cyber | Between 2026-09-29 and 2026-10-06, a new cyberattack using the JadePuffer agentic AI framework targets Azure cloud infrastructure. | A new cyberattack using the JadePuffer agentic AI framework targets Azure cloud infrastructure between 2026-09-29 and 2026-10-06. |
| KKR-20260929-04 | 15% | 2026-10-08 | political | Between 2026-09-29 and 2026-10-06, a new political scandal involving a US senator and a foreign government is reported by two independent wire services. | A new political scandal involving a US senator and a foreign government is reported by two independent wire services (e.g., Reuters, AP, Bloomberg) between 2026-09-29 and 2026-10-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-28 and 2026-10-05, at least one report from a hostile side confirms an airstrike in Jabalia, Israel-Gaza-Levant Theatre, wit" → REJECTED: event window opens 2026-09-28, before this row is sealed (2026-09-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-29 and 2026-10-06, the S&P 500 closes below 7,500 at the end of the trading day." → REJECTED: market-price resolution with weekend deadline — no settlement exists that day; resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Between 2026-09-28 and 2026-10-05, a flood warning is issued for Yavapai County, Arizona, by the National Weather Service." → REJECTED: event window opens 2026-09-28, before this row is sealed (2026-09-29, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "Between 2026-09-29 and 2026-10-06, the US government announces a new ban on Canadian dairy imports, effective within 30 days." → REJECTED: relative timeframe in statement — use absolute date windows; the deadline field governs and relative phrasing creates adjudication conflict
- "Between 2026-09-29 and 2026-10-06, a new ransomware attack on a critical infrastructure provider in Japan is confirmed by a government agenc" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively
- "Between 2026-09-29 and 2026-10-06, a new nuclear-related statement by Iran is confirmed by both an Iranian state outlet and a Western news w" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

3044 issued all-time across 17 forecaster arms · 2502 open (260 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 340 issued · 190 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1083 | 966 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 340 | 190 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 136 | 131 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 216 | 199 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 40 | 40 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*