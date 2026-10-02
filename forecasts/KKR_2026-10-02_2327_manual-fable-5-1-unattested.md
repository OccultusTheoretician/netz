**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022327Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-02_1519.md · forecaster: manual/fable-5.1/unattested · 4 accepted / 6 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261002-15 | 35% | 2026-11-02 | economics/markets | The ICE Brent December 2026 futures contract settles below 95.00 dollars per barrel on at least one trading day between 2026-10-05 and 2026-10-29. Reference: 100.27 on the packet date. | The ICE daily settlement price for Brent December 2026 futures is below 95.00 on any trading day between 2026-10-05 and 2026-10-29. Reference: 100.27 on the packet date. |
| KKR-20261002-16 | 50% | 2026-11-02 | military/conflict | Ethiopian federal forces or the allied Tigray Peace Forces take control of Mekelle, the Tigray regional capital, on a date between 2026-10-03 and 2026-10-30. | At least two of Reuters, AFP, AP and BBC report federal or allied forces holding Mekelle on a date between 2026-10-03 and 2026-10-30, citing residents, the TPLF or their own reporters rather than a government claim alone. |
| KKR-20261002-17 | 22% | 2026-11-02 | disaster | The DR Congo health ministry cumulative death toll for the Ebola outbreak declared 2026-05-15 reaches 5,000 or more in figures published between 2026-10-03 and 2026-10-30. Reference: 4,018 in figures published 2026-10-01. | At least two of AP, Reuters and AFP report a DR Congo health ministry cumulative Ebola death toll of 5,000 or more, published between 2026-10-03 and 2026-10-30. Reference: 4,018 on 2026-10-01. |
| KKR-20261002-18 | 6% | 2027-01-04 | cyber | CISA adds at least one of the six Dell Container Storage Modules flaws patched 2026-10-01 to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-03 and 2026-12-31. | The CISA KEV catalog JSON lists any of CVE-2026-63688, CVE-2026-63692, CVE-2026-67269, CVE-2026-54472, CVE-2026-61421 or CVE-2026-67273 with a dateAdded value between 2026-10-03 and 2026-12-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC leaves the federal funds target range unchanged at 3.75 to 4.00 percent at its scheduled meeting ending 2026-10-28. Reference: uppe" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds at least one further Fortinet vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104286 dateAdded 2026-10-01, before the claimed window 2026-10-05..2026-11-06; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "The BLS Employment Situation report scheduled for 2026-11-06 shows a first-print October 2026 change in total nonfarm payroll employment bel" → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "A royal decree dissolving the Cortes Generales and calling an early general election in Spain is published in the Boletin Oficial del Estado" → REJECTED: the resolution names a different subject than the statement — the claim is about Boletin, Cortes, Estado, Generales and the resolution settles on BOE, Congreso, Decreto, Diputados. A row whose resolution checks a different fact can be scored correct while being wrong
- "The French National Assembly adopts a motion of censure against the sitting government on a date between 2026-10-05 and 2026-12-18." → REJECTED: the resolution requires absolute, date, members and the failure condition does not mention them — an outcome missing them satisfies neither clause and the row has no verdict. 4.03 tests that a failure condition exists; it does not test that it complements
- "A New South Wales Supreme Court jury finds Beau Lamarre-Condon guilty of murder on both counts, for the deaths of Jesse Baird and Luke Davie" → REJECTED: the resolution names a different subject than the statement — the claim is about Baird, Beau, Condon, Court and the resolution settles on AAP, ABC, Australia, Guardian. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

3236 issued all-time across 18 forecaster arms · 2694 open (391 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 243 issued · 226 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1154 | 1037 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 361 | 211 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 161 | 156 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 243 | 226 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 64 | 64 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*