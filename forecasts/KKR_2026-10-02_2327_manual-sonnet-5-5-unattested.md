**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022327Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-02_1519.md · forecaster: manual/sonnet-5.5/unattested · 8 accepted / 2 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261002-37 | 40% | 2026-10-21 | military/conflict | Between 2026-10-05 and 2026-10-18, Russia will launch at least 500 drones and missiles combined against Ukraine in a single overnight attack, as tallied by the Ukrainian Air Force. | A Ukrainian Air Force tally of Russian drones plus missiles launched in one overnight attack, dated between 2026-10-05 and 2026-10-18, is at least 500, reported by at least two of Reuters, AP, Kyiv Independent. |
| KKR-20261002-38 | 12% | 2026-11-03 | military/conflict | Between 2026-10-05 and 2026-10-30, Ethiopian and Eritrean state forces will fight each other directly, including cross-border fire or air strikes on each other. | At least two of Reuters, AP, AFP, BBC report Ethiopian and Eritrean state forces fought each other directly between 2026-10-05 and 2026-10-30, beyond one government accusing the other of backing rebels. |
| KKR-20261002-39 | 10% | 2026-10-30 | economics/markets | At its meeting of 2026-10-27 to 2026-10-28, the FOMC will raise the federal funds target range above 3.75 to 4.00 percent, with the decision announced on 2026-10-28. Reference: 3.75 to 4.00 percent on the packet date. | The Federal Reserve FOMC statement released 2026-10-28 sets a federal funds target range above 3.75 to 4.00 percent. Reference: 3.75 to 4.00 percent on the packet date. |
| KKR-20261002-40 | 30% | 2026-11-03 | economics/markets | ICE Brent December 2026 futures will settle below 90.00 USD per barrel on at least one trading day between 2026-10-05 and 2026-10-30. Reference: 100.27 in the packet market snapshot. | ICE published settlement for Brent December 2026 futures is below 90.00 USD per barrel on at least one trading day between 2026-10-05 and 2026-10-30 inclusive. Reference: 100.27 on the packet date. |
| KKR-20261002-41 | 8% | 2026-11-17 | cyber | CISA will add at least one of the two maximum-severity Dell Container Storage Modules flaws, CVE-2026-63688 or CVE-2026-63692, to its KEV catalog with a date-added value between 2026-10-05 and 2026-11-13. | The CISA KEV JSON feed lists CVE-2026-63688 or CVE-2026-63692 with a dateAdded value between 2026-10-05 and 2026-11-13 inclusive. |
| KKR-20261002-42 | 6% | 2026-11-10 | political | Between 2026-10-05 and 2026-11-06, the United States will formally prohibit or license-restrict exports of diesel or distillate fuel oil, through an executive order, proclamation, or Commerce rule published in the Federal Register. | The Federal Register carries an executive order, proclamation, or Commerce rule published between 2026-10-05 and 2026-11-06 that prohibits or license-restricts US exports of diesel or distillate fuel oil, either generally or to European countries. |
| KKR-20261002-43 | 15% | 2026-12-15 | crime/security | Between 2026-10-05 and 2026-12-11, at least one person will be criminally charged by indictment or felony complaint over the alleged October 2024 sexual assault at a Cornell University fraternity house. | A New York Attorney General release or New York court record shows at least one person charged by indictment or felony complaint over the alleged October 2024 Cornell fraternity assault, filed between 2026-10-05 and 2026-12-11. |
| KKR-20261002-44 | 62% | 2026-11-03 | disaster | Between 2026-10-05 and 2026-10-30, Congolese health authorities will report a cumulative Ebola death toll of at least 4,700 in the ongoing outbreak. Reference: 4,018 deaths reported on 2026-10-02. | Reuters, AP, or WHO publish a Congolese government cumulative Ebola death count of at least 4,700, dated between 2026-10-05 and 2026-10-30. Reference: 4,018 deaths reported on 2026-10-02. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The BLS Employment Situation for October 2026, scheduled for release on 2026-11-06, will report a negative first-published change in total n" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim; measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "The CISA KEV catalog will add at least one Fortinet vulnerability, other than CVE-2026-104286, with a date-added value between 2026-10-05 an" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104286 dateAdded 2026-10-01, before the claimed window 2026-10-05..2026-10-30; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

3262 issued all-time across 18 forecaster arms · 2720 open (391 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 32 issued · 32 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1165 | 1048 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 71 | 71 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*