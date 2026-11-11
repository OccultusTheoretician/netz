**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112113Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-11_1613.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261111-14 | 55% | 2026-12-03 | cyber | The CISA KEV catalog adds an entry for the Xen Orchestra authentication bypass vulnerability with a date-added value between 2026-11-12 and 2026-11-30. | The CISA KEV catalog JSON contains an entry whose vendor or product field names Xen Orchestra or Vates with dateAdded between 2026-11-12 and 2026-11-30 inclusive. |
| KKR-20261111-15 | 65% | 2026-12-08 | military/conflict | Russia and Ukraine carry out a prisoner exchange of at least 100 persons per side between 2026-11-12 and 2026-12-04, following the Abu Dhabi agreement. | Both the Ukrainian Coordination Headquarters and the Russian Ministry of Defence publish statements confirming an exchange of at least 100 persons each way occurring between 2026-11-12 and 2026-12-04. |
| KKR-20261111-16 | 15% | 2026-12-14 | military/conflict | The United States and Iran announce a signed agreement or formal ceasefire that suspends or lifts the US naval blockade of Iran between 2026-11-12 and 2026-12-10. | Official statements from both the US government and the Iranian government, dated within the window, confirm an agreement that suspends or lifts the blockade; carried by at least two wire services. |
| KKR-20261111-17 | 30% | 2026-12-15 | economics/markets | The 10-year US Treasury yield closes at or above 5.25 percent on at least one trading day between 2026-11-12 and 2026-12-11. Reference: 5.00 percent on the packet date. | FRED series DGS10 shows a daily value of 5.25 or higher for at least one date between 2026-11-12 and 2026-12-11 inclusive. |
| KKR-20261111-18 | 20% | 2026-12-22 | economics/markets | The Federal Open Market Committee lowers the federal funds target range at its December 2026 meeting, scheduled to conclude on or about 2026-12-09. | The Federal Reserve Board press release for the December 2026 FOMC meeting states a target range lower than the range in effect on 2026-11-11. |
| KKR-20261111-19 | 50% | 2026-12-22 | economics/markets | Anthropic common stock begins trading on a US exchange between 2026-11-12 and 2026-12-18. | NYSE or Nasdaq listing records and at least two wire services show a first trading day for Anthropic common stock dated between 2026-11-12 and 2026-12-18 inclusive. |
| KKR-20261111-20 | 78% | 2026-12-08 | political | The Mississippi Secretary of State certifies Scott Colom as the winner of the 2026 US Senate general election over Cindy Hyde-Smith by 2026-12-04. | Certified results published on the Mississippi Secretary of State website on or before 2026-12-04 show Colom with more votes than Hyde-Smith. |
| KKR-20261111-21 | 60% | 2027-01-19 | disaster | WHO or the Kenya Ministry of Health declares the Kenya Ebola outbreak over between 2026-12-20 and 2027-01-15. | A WHO Disease Outbreak News post, WHO AFRO release, or Kenya Ministry of Health statement dated between 2026-12-20 and 2027-01-15 declares the outbreak ended. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 closes at or below 7223.71, five percent below the packet reference, on at least one trading day between 2026-11-12 and 2026-12-" → REJECTED: the resolution names only a venue or register (FRED, dow, indices, jones) and no subject - the register is where to look, not what is claimed; name the subject inside it; the resolution names a different subject than the statement — the claim is about Reference and the resolution settles on Dow, FRED, Indices, Jones. A row whose resolution checks a different fact can be scored correct while being wrong
- "A federal grand jury indictment is docketed against the US soldier arrested for spying for Russia between 2026-11-12 and 2026-12-18." → REJECTED: resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

5614 issued all-time across 23 forecaster arms · 3892 open (1598 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 526 issued · 411 open · 107 resolved · 61 hits / 46 misses · **Brier 0.211** against its own base rate 57.0% (climatological 0.245) · **skill +0.140**.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 157 | 157 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 201 | 184 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 209 | 207 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 183 | 150 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 526 | 411 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5.2/unattested | 8 | 8 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 372 | 358 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*