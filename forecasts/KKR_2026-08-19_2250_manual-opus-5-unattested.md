**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192250Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-19_1519.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260819-14 | 92% | 2026-12-02 | cyber | CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value in the window 2026-08-26 to 2026-11-30. | The CISA KEV catalog contains at least one entry with vendorProject Microsoft and a dateAdded value between 2026-08-26 and 2026-11-30 inclusive. |
| KKR-20260819-15 | 93% | 2026-11-04 | disaster | At least one earthquake of magnitude 7.0 or greater occurs worldwide with origin time in the window 2026-08-26 to 2026-10-31 UTC. | The USGS ComCat catalog lists at least one event of magnitude 7.0 or greater with origin time between 2026-08-26T00:00Z and 2026-10-31T23:59Z. |
| KKR-20260819-16 | 52% | 2026-10-19 | military/conflict | The UAE government publicly attributes a missile or drone impact on UAE territory or territorial waters to Iran, for an impact in the window 2026-08-26 to 2026-10-15. | Reuters and Agence France-Presse both report a UAE government statement attributing a missile or drone impact on UAE territory or territorial waters to Iran within the window. |
| KKR-20260819-17 | 18% | 2026-12-04 | military/conflict | Iran publicly agrees to permit unrestricted commercial transit of the Strait of Hormuz under an agreement announced in the window 2026-08-26 to 2026-11-30. | Reuters and the Associated Press both report an agreement, announced within the window, under which Iran permits unrestricted commercial transit of the Strait of Hormuz. |
| KKR-20260819-18 | 33% | 2026-12-15 | crime/security | Croatia surrenders to German custody the Ukrainian diver arrested in Pula on 2026-08-19 over the Nord Stream blasts, in the window 2026-08-26 to 2026-12-11. | The German Federal Public Prosecutor confirms the suspect has been surrendered by Croatia and brought before a judge of the Federal Court of Justice within the window. |
| KKR-20260819-19 | 52% | 2026-12-04 | political | NABU or SAPO issues a formal notice of suspicion to a serving or former official of the Ukrainian Office of the President in the window 2026-08-26 to 2026-11-30. | NABU or SAPO publicly announces a notice of suspicion naming a serving or former Office of the President official, reported by Reuters and Ukrainska Pravda. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC leaves the federal funds target range unchanged at 3.50 to 3.75 percent at its scheduled meeting of 2026-09-15 to 2026-09-16." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "ICE Brent front-month futures settle at or above 100.00 USD per barrel on at least one trading day in the window 2026-08-26 to 2026-10-30." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds at least one PTC vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value in the window 2026-08-26 to " → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Cumulative confirmed Bundibugyo virus cases in the DRC and Uganda outbreak reach 10,000 or more in WHO data covering the period through 2026" → REJECTED: cited items name Congo; the claim is about Congo, The Democratic Republic of the, Uganda — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; the named venue is introduced by 'including', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively; single-day resolution window for an unscheduled event — the row requires this to occur on 2026-10-25 exactly. Price a day, not a window: widen the window or state why the date is fixed; the resolution names only a venue or register (WHO, afro) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

767 issued all-time across 14 forecaster arms · 677 open (11 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 75 issued · 75 open · nothing resolved yet — this arm earns a score at its first resolution.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 165 | 157 | 8 | 1 | 7 | 0.125 | 12.5% | 0.109 | -0.143 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 20 | 0 | — | — | not computed | — | — | — |
| lmstudio/auto[post-window] | 105 | 93 | 10 | 2 | 8 | 0.240 | 20.0% | 0.160 | -0.502 |
| lmstudio/auto[pre-verbot] | 60 | 13 | 39 | 12 | 27 | 0.225 | 30.8% | 0.213 | -0.054 |
| manual/fable | 45 | 36 | 9 | 4 | 5 | 0.190 | 44.4% | 0.247 | +0.232 |
| manual/fable-5 | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 61 | 61 | 0 | — | — | not computed | — | — | — |
| manual/opus-5 | 74 | 72 | 2 | 1 | 1 | 0.243 | 50.0% | 0.250 | +0.030 |
| manual/opus-5/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5 | 45 | 39 | 6 | 3 | 3 | 0.270 | 50.0% | 0.250 | -0.081 |
| manual/sonnet-5/unattested | 62 | 61 | 1 | 0 | 1 | 0.040 | 0.0% | 0.000 | — |
| operator/human | 6 | 2 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*