**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 181516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: lmstudio/qwen36 · 6 accepted / 4 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-11 | 30% | 2026-11-04 | military_conflict | A drone strike hits a Russian military base in Belgorod Oblast between 2026-10-26 and 2026-11-02. | A drone strike hits a Russian military base in Belgorod Oblast between 2026-10-26 and 2026-11-02. |
| KKR-20261018-12 | 15% | 2026-11-04 | disaster | A forest fire in South Africa causes GDACS to issue a Red alert between 2026-10-26 and 2026-11-02. | A forest fire in South Africa causes GDACS to issue a Red alert between 2026-10-26 and 2026-11-02. |
| KKR-20261018-13 | 20% | 2026-11-09 | economics | The Nasdaq closes below 25,000 on a weekday between 2026-11-02 and 2026-11-06. | The Nasdaq closes below 25,000 on a weekday between 2026-11-02 and 2026-11-06. Reference: 26,140.03 on the packet date. |
| KKR-20261018-14 | 10% | 2026-11-04 | political | A US court docket records an indictment of a senior Iranian official for cyber operations between 2026-10-26 and 2026-11-02. | A US court docket records an indictment of a senior Iranian official for cyber operations between 2026-10-26 and 2026-11-02. |
| KKR-20261018-15 | 15% | 2026-11-04 | disaster | A M6.0+ earthquake occurs in Pakistan between 2026-10-26 and 2026-11-02. | A M6.0+ earthquake occurs in Pakistan between 2026-10-26 and 2026-11-02. |
| KKR-20261018-16 | 25% | 2026-11-04 | cyber | Microsoft issues a critical security update for a zero-day exploit in Windows between 2026-10-26 and 2026-11-02. | Microsoft issues a critical security update for a zero-day exploit in Windows between 2026-10-26 and 2026-11-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog carries a date-added value for a critical infrastructure vulnerability between 2026-10-26 and 2026-11-02." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "WTI Crude closes above 105.00 on a weekday between 2026-11-02 and 2026-11-06." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "France's government falls via a no-confidence vote or resignation between 2026-10-26 and 2026-11-02." → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "Israel launches a major ground offensive into Lebanon between 2026-10-26 and 2026-11-02." → REJECTED: cited items name Egypt, Iran, Islamic Republic of, Saudi Arabia; the claim is about Lebanon — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

4422 issued all-time across 21 forecaster arms · 3311 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 81 issued · 81 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1556 | 1260 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 79 | 79 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 372 | 314 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 203 | 198 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 156 | 156 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*