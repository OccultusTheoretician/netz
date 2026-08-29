**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 292142Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-29_1537.md · forecaster: manual/sonnet-5/unattested · 6 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260829-43 | 65% | 2026-10-26 | cyber | The CISA Known Exploited Vulnerabilities catalog will add an entry for CVE-2026-81578 or CVE-2026-82078, the actively exploited PaperCut NG/MF flaws, with a dateAdded value between 2026-09-05 and 2026-10-24. | TRUE if the CISA KEV catalog lists CVE-2026-81578 or CVE-2026-82078 with dateAdded inside the window, checked on 2026-10-26; FALSE if neither entry appears by then. |
| KKR-20260829-44 | 25% | 2026-12-02 | cyber | McKesson will file a document on SEC EDGAR, such as a Form 8-K/A or 10-Q, between 2026-09-05 and 2026-11-30 that states a specific number or bounded range of individuals affected by its August 2026 data theft incident. | TRUE if a McKesson SEC EDGAR filing dated in the window states a specific number or bounded range of affected individuals; FALSE if no such filing exists as of 2026-12-02. |
| KKR-20260829-45 | 52% | 2026-10-28 | political | Serbia will hold its snap parliamentary election on 2026-10-25 rather than on 2026-10-18, the two dates floated by President Aleksandar Vucic. | TRUE if Serbian election authorities or two of Reuters, AP, and AFP confirm voting occurred on 2026-10-25; FALSE if the vote is held 2026-10-18 or not confirmed by 2026-10-28. |
| KKR-20260829-46 | 78% | 2026-10-07 | military/conflict | A single Russian missile or drone strike will kill 10 or more people in Kyiv, Ukraine, between 2026-09-05 and 2026-10-05. | TRUE if Ukrainian officials and at least one of Reuters, AP, or AFP report 10 or more deaths from one strike on Kyiv in the window; checked 2026-10-07; FALSE otherwise. |
| KKR-20260829-47 | 75% | 2027-02-03 | military/conflict | Mojtaba Khamenei will still publicly hold the title of Supreme Leader of Iran throughout the window from 2026-09-05 to 2027-01-31. | TRUE if Iranian state media and at least one of Reuters or AP confirm Mojtaba Khamenei still holds this title on 2027-01-31; FALSE if replaced, resigned, or killed before then. |
| KKR-20260829-48 | 52% | 2026-09-22 | disaster | The confirmed death toll from the 26 August 2026 Nepal-Tibet glacial flood disaster will exceed 1,000 people at some point between 2026-09-05 and 2026-09-19. | TRUE if the National Disaster Risk Reduction and Management Authority of Nepal or two of Reuters, AP, and AFP report a confirmed toll above 1,000 in the window; checked 2026-09-22; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Federal Open Market Committee will announce a lower federal funds target range at the conclusion of its September 15-16, 2026 meeting th" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The most-active CBOT corn futures contract will settle at or above 6.00 USD per bushel on 2026-11-30." → REJECTED: the resolution names only a venue or register (CME, group) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "Venezuela will sign a written agreement granting oil exploration or production rights to a named US company under the deal Trump announced o" → REJECTED: the resolution names only a venue or register (AP, Bloomberg, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1093 issued all-time across 14 forecaster arms · 932 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 119 issued · 111 open · 8 resolved · 5 hits / 3 misses · **Brier 0.174** against its own base rate 62.5% (climatological 0.234) · **skill +0.257** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 262 | 245 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 169 | 138 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 113 | 112 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 127 | 124 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 119 | 111 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*