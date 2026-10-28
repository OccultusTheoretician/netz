**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 282353Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-28_1515.md · forecaster: manual/opus-5.5/unattested · 5 accepted / 5 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261028-24 | 60% | 2026-12-11 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting concluding on 2026-12-09. | TRUE if the FOMC statement released on 2026-12-09 announces a higher target range, equivalently FRED series DFEDTARU for 2026-12-10 exceeds its 2026-12-08 value; FALSE if the range is held or cut. |
| KKR-20261028-25 | 35% | 2027-01-13 | economics/markets | WTI crude (FRED series DCOILWTICO) records a daily value below 90.00 dollars per barrel on at least one day between 2026-11-02 and 2026-12-31. Reference: WTI 102.60 on the packet date. | TRUE if any DCOILWTICO daily observation dated 2026-11-02 through 2026-12-31, as published on FRED at the deadline, is below 90.00; FALSE otherwise. Reference: 102.60 dollars per barrel at seal. |
| KKR-20261028-26 | 55% | 2026-12-15 | cyber | CISA adds at least one Oracle E-Business Suite vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-28 and 2026-12-11. | TRUE if the CISA KEV JSON feed, fetched on the deadline, holds an entry with vendorProject Oracle, product E-Business Suite, and dateAdded from 2026-10-28 through 2026-12-11 inclusive; FALSE otherwise. |
| KKR-20261028-27 | 40% | 2027-01-15 | cyber | A University of New Mexico health entity submits a HIPAA breach report to the HHS Office for Civil Rights with a breach submission date between 2026-10-28 and 2027-01-08. | TRUE if the HHS OCR breach portal, checked on the deadline, lists a covered entity whose name contains UNM or University of New Mexico with a breach submission date between 2026-10-28 and 2027-01-08; FALSE otherwise. |
| KKR-20261028-28 | 15% | 2026-11-24 | political | No candidate wins more than 50 percent in the 2026-11-03 Georgia US Senate general election, sending the race to a runoff. | TRUE if Georgia Secretary of State results (certified, or final unofficial if certification is pending) for the 2026-11-03 US Senate general election show no candidate above 50 percent; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The United States and Iran each publicly confirm a newly concluded agreement to end their war or halt hostilities between 2026-10-29 and 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…agreement between the two states, per reuters | or | ap…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new Israeli government formed after the 2026-10-27 Knesset election wins a Knesset confidence vote between 2026-10-29 and 2027-02-26." → REJECTED: resolution offers alternative VENUES joined by 'or' (… 2027-02-26, per the knesset official website | or | reuters, times of israel, or haaretz reportin…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Oscar Puente leaves office as the Spanish Minister of Transport and Sustainable Mobility between 2026-10-29 and 2026-12-31." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The Southwark Crown Court jury in the Russell Brand sexual offences trial returns a verdict on at least one count between 2026-10-29 and 202" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ell brand, as reported by bbc news, pa media, | or | the guardian…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Cumulative confirmed Ebola cases in the Democratic Republic of the Congo reach 12500 or more, with data up to a date between 2026-10-29 and " → REJECTED: cited items name Israel; the claim is about Congo, Congo, The Democratic Republic of the — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

5108 issued all-time across 22 forecaster arms · 3386 open (448 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 291 issued · 277 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 5 | 5 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 132 | 115 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 133 | 131 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 129 | 96 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 460 | 345 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 291 | 277 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*