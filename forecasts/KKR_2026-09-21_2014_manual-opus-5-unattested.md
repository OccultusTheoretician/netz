**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 212014Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-21_1516.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260921-14 | 7% | 2026-10-01 | political | Donald Trump and Masoud Pezeshkian meet in person between 2026-09-22 and 2026-09-29, when both are expected in New York for the UN General Assembly high-level week. | TRUE if the White House or Iranian presidency confirms, or two of Reuters, AP and AFP report, a face-to-face Trump-Pezeshkian meeting held between 2026-09-22 and 2026-09-29. Phone calls, passing handshakes and intermediary talks do not count. |
| KKR-20260921-15 | 55% | 2026-10-02 | political | The US and China announce agreement to establish or launch a dedicated intergovernmental AI dialogue, channel or hotline between 2026-09-23 and 2026-09-30, around the Trump-Xi White House summit. | TRUE if a White House, PRC Foreign Ministry or Xinhua readout, fact sheet or joint statement issued between 2026-09-23 and 2026-09-30 says both sides agreed to establish or launch a dedicated government-to-government AI dialogue, channel or hotline. |
| KKR-20260921-16 | 18% | 2026-10-23 | military/conflict | US forces carry out at least one strike on a target located on Iranian land territory between 2026-09-22 and 2026-10-21. | TRUE if CENTCOM or the Pentagon announces, or two of Reuters, AP and AFP report, a US strike on a target on Iranian soil conducted between 2026-09-22 and 2026-10-21. Strikes on vessels at sea do not count. |
| KKR-20260921-17 | 30% | 2026-10-26 | economics/markets | ICE Brent front-month (December 2026) crude futures settle below 90.00 dollars per barrel on 2026-10-23. Reference: 100.27 dollars on the packet date. | TRUE if the ICE Futures Europe official settlement price of the front-month (December 2026) Brent crude contract on 2026-10-23 is below 90.00 dollars per barrel; FALSE otherwise. Reference: 100.27 on the packet date. |
| KKR-20260921-18 | 85% | 2026-10-26 | cyber | CISA adds at least one new Cisco vulnerability to the Known Exploited Vulnerabilities catalog between 2026-09-22 and 2026-10-23. | TRUE if the CISA KEV catalog carries at least one entry with vendorProject Cisco and a dateAdded value between 2026-09-22 and 2026-10-23 inclusive; FALSE otherwise. |
| KKR-20260921-19 | 50% | 2027-02-01 | political | Elif Eralp is elected Governing Mayor of Berlin by the Abgeordnetenhaus between 2026-09-22 and 2027-01-29. | TRUE if the Berlin Abgeordnetenhaus elects Elif Eralp Governing Mayor in a plenary vote held between 2026-09-22 and 2027-01-29, per the official plenary record or two of Reuters, AP, AFP and dpa. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "An earthquake of magnitude 6.0 or greater occurs within 300 km of 52.859N 171.376W, epicenter of the 2026-09-17 M6.5 event near Nikolski, Al" → REJECTED: the resolution names a different subject than the statement — the claim is about Alaska, Nikolski and the resolution settles on ComCat, USGS. A row whose resolution checks a different fact can be scored correct while being wrong
- "US forces conduct at least one lethal strike on an alleged drug-trafficking vessel in the Caribbean or Eastern Pacific between 2026-09-22 an" → REJECTED: the resolution names a different subject than the statement — the claim is about Caribbean, Eastern, Pacific and the resolution settles on Command, Pentagon, Southern. A row whose resolution checks a different fact can be scored correct while being wrong
- "A federal judge orders the White House to restore access for CNN, Politico or MS NOW journalists between 2026-09-22 and 2026-10-23." → REJECTED: the resolution narrows the claim with a qualifier the statement never makes — preliminary. The forecaster is graded on the statement; a severity or status qualifier living only in the resolution is invisible to anyone reading the claim; the resolution requires court, hard-pass and the failure condition does not mention them — an outcome missing them satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements
- "The FOMC raises the federal funds target range at its meeting concluding 2026-10-28. Reference: 3.75 to 4.00 percent on the packet date." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

2618 issued all-time across 16 forecaster arms · 2152 open (167 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 312 issued · 295 open · 7 resolved · 5 hits / 2 misses · **Brier 0.137** against its own base rate 71.4% (climatological 0.204) · **skill +0.329** · under 30 resolved, this is noise.

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
| manual/opus-5/unattested | 312 | 295 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 284 | 236 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*