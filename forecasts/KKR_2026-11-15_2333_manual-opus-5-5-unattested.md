**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 152333Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-15_1612.md · forecaster: manual/opus-5.5/unattested · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261115-15 | 60% | 2026-12-02 | military/conflict | Iran launches at least one drone or missile attack at Bahraini territory, including US facilities in Bahrain, between 2026-11-16 and 2026-11-29. | TRUE if the government of Bahrain or US Central Command states that Iranian drones or missiles were launched at Bahraini territory between 2026-11-16 and 2026-11-29, as reported by at least two of Reuters, AP, AFP, BBC. Otherwise FALSE. |
| KKR-20261115-16 | 35% | 2026-12-02 | military/conflict | US forces strike at least one target on Iranian land territory, mainland or islands, between 2026-11-16 and 2026-11-29. | TRUE if the Pentagon, US Central Command or the White House confirms, or at least two of Reuters, AP, AFP report citing US officials, a US strike on Iranian land territory between 2026-11-16 and 2026-11-29. Otherwise FALSE. |
| KKR-20261115-17 | 78% | 2026-11-23 | economics/markets | Nvidia reports revenue of at least 110.16 billion dollars, the top of its own guidance range, for its fiscal Q3 2027 quarter ended 2026-10-25, in results scheduled for release on 2026-11-17. | TRUE if revenue for the quarter ended 2026-10-25, in Nvidia results filed on SEC EDGAR between 2026-11-17 and 2026-11-23, is at least 110.16 billion dollars. Reference: guidance 108.0 billion plus or minus 2 percent. Otherwise FALSE. |
| KKR-20261115-18 | 50% | 2027-01-04 | political | A new Israeli government headed by Gadi Eisenkot wins a Knesset confidence vote between 2026-11-16 and 2026-12-31. | TRUE if the Knesset approves a government headed by Gadi Eisenkot in a confidence vote held between 2026-11-16 and 2026-12-31, per the official Knesset record or both Reuters and AP. Otherwise FALSE. |
| KKR-20261115-19 | 20% | 2026-11-30 | political | The United States, China and Russia issue one joint written statement agreed by all three governments in connection with the Trump-Xi-Putin meeting scheduled for 2026-11-19 in Shenzhen, published between 2026-11-18 and 2026-11-25. | TRUE if one joint statement text of the United States, China and Russia is published between 2026-11-18 and 2026-11-25 on at least two of whitehouse.gov, kremlin.ru, mfa.gov.cn. Separate national readouts do not count. Otherwise FALSE. |
| KKR-20261115-20 | 40% | 2027-02-03 | crime/security | Between 2026-11-15 and 2027-01-31, a person is criminally charged in federal or Illinois state court over the explosive device found on 2026-11-13 at the BioUrja Renewables ethanol plant in Peoria, Illinois. | TRUE if a DOJ or US Attorney press release, a court docket, or the Peoria County prosecutor shows charges filed between 2026-11-15 and 2027-01-31 against a person over the Peoria BioUrja explosive device. Otherwise FALSE. |
| KKR-20261115-21 | 45% | 2027-01-11 | disaster | The CDC cumulative count of confirmed 2026 US measles cases reaches at least 7,000 in a CDC update published between 2026-11-16 and 2027-01-08. Reference: 5,412 cases as of 2026-11-12. | TRUE if any CDC measles cases and outbreaks update published between 2026-11-16 and 2027-01-08 reports at least 7,000 confirmed 2026 US cases. Reference: 5,412 as of 2026-11-12. Otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The WTI spot price at Cushing, FRED series DCOILWTICO, is at or above 95.00 dollars per barrel on at least one trading day between 2026-11-1" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "The FOMC raises the federal funds target range by at least 50 basis points, to an upper bound of 4.50 percent or higher, at its meeting conc" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "In its judgment delivered on 2026-11-19 in The Gambia v. Myanmar, the International Court of Justice finds that Myanmar committed genocide a" → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-11-19 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

5788 issued all-time across 23 forecaster arms · 4066 open (1723 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 404 issued · 390 open · 14 resolved · 8 hits / 6 misses · **Brier 0.312** against its own base rate 57.1% (climatological 0.245) · **skill -0.275** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 214 | 214 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 221 | 204 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 224 | 222 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 209 | 176 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 535 | 420 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 23 | 23 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 404 | 390 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*