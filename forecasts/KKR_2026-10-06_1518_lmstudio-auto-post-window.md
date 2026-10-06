**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 061518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-06_1516.md · forecaster: lmstudio/auto · 4 accepted / 6 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261006-01 | 30% | 2026-11-03 | cyber | Between 2026-10-21 and 2026-10-28, the CISA KEV catalog will carry a date-added value for a vulnerability in Rejetto HFS servers with a critical RCE flaw. | The CISA KEV catalog will list a vulnerability with a date-added value between 2026-10-21 and 2026-10-28 that is related to Rejetto HFS and involves a critical remote code execution flaw. |
| KKR-20261006-02 | 20% | 2026-11-07 | disaster | Between 2026-10-24 and 2026-10-31, a wildfire will be reported in the Democratic Republic of Congo with a confirmed area burned exceeding 100 km². | The GDACS Alerts system will report a wildfire in the Democratic Republic of Congo with a confirmed area burned exceeding 100 km², as documented in a machine-readable alert. |
| KKR-20261006-03 | 15% | 2026-11-09 | disaster | Between 2026-10-26 and 2026-11-02, a major earthquake with magnitude 6.0 or higher will be recorded by the USGS in the Pacific Northwest. | The USGS Significant Quakes database will record an earthquake with magnitude 6.0 or higher in the Pacific Northwest (defined as Washington, Oregon, or adjacent offshore zones) between 2026-10-26 and 2026-11-02. |
| KKR-20261006-04 | 25% | 2026-11-13 | cyber | Between 2026-10-30 and 2026-11-06, a ransomware attack will be confirmed on a critical infrastructure provider in the United States, with a public disclosure by the company and at least two independent sources. | A ransomware attack on a critical infrastructure provider in the United States will be confirmed by the company's public disclosure and at least two independent sources from different outlets, with no conflicting denial. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-22 and 2026-10-29, a drone attack on Moscow will be confirmed by at least two independently biased sources from hostile side" → REJECTED: cited items name Saudi Arabia; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-23 and 2026-10-30, the S&P 500 will close above 7,900 on at least one trading day." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…ted by a machine-readable source such as fred | or | a major exchange…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-25 and 2026-11-01, Iran will issue a public statement claiming a successful cyberattack on a U.S. government system, confirm" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-27 and 2026-11-03, the European Central Bank will announce a policy shift increasing the benchmark interest rate by 0.5 perc" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; resolution offers alternative VENUES joined by 'or' (…ne-readable source such as ecb press releases | or | fred…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-10-28 and 2026-11-04, a major offensive operation will be confirmed in the Zaporizhzhia region by at least two independently bi" → REJECTED: cited items name Saudi Arabia; the claim is about zone:russia_ukraine — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else
- "Between 2026-10-29 and 2026-11-05, a political scandal involving a U.S. federal official will result in a formal indictment by a grand jury." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

3465 issued all-time across 21 forecaster arms · 2651 open (358 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 387 issued · 208 open · 170 resolved · 45 hits / 125 misses · **Brier 0.205** against its own base rate 26.5% (climatological 0.195) · **skill -0.056**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1242 | 1041 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 387 | 208 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 95 | 95 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*