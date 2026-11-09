**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 092054Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-09_1611.md · forecaster: control/trailing · 9 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261109-35 | 55% | 2026-12-02 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for the OpenSSH flaw reported as SSHole with a dateAdded value between 2026-11-09 and 2026-11-30. | The CISA KEV JSON feed contains an entry with vendorProject OpenSSH matching the SSHole flaw and dateAdded between 2026-11-09 and 2026-11-30 inclusive. |
| KKR-20261109-36 | 69% | 2027-01-05 | economics/markets | Nvidia files a Form 8-K with the SEC between 2026-11-09 and 2026-12-31 disclosing that Jensen Huang has resigned, been removed, or taken leave as CEO. | SEC EDGAR shows an Nvidia Form 8-K dated between 2026-11-09 and 2026-12-31 reporting Huang departure or leave of absence from the CEO role under Item 5.02. |
| KKR-20261109-37 | 69% | 2027-01-04 | economics/markets | ICE Brent front-month crude settles at or above 100.00 USD on at least one trading day between 2026-11-10 and 2026-12-31. Reference: 94.80 on the packet date. | ICE Brent front-month official daily settlement price is at or above 100.00 USD on any trading day from 2026-11-10 to 2026-12-31 inclusive. |
| KKR-20261109-38 | 69% | 2027-01-04 | economics/markets | The US 10-year Treasury par yield for 2026-12-31 is at or below 4.50 percent. Reference: 4.88 percent on the packet date. | US Treasury Daily Par Yield Curve table shows a 10-year value at or below 4.50 for the 2026-12-31 entry. |
| KKR-20261109-39 | 42% | 2027-01-05 | political | The European Council announces a nominee to succeed Christine Lagarde as ECB President between 2026-11-09 and 2026-12-31. | A press release on consilium.europa.eu dated between 2026-11-09 and 2026-12-31 names a nominee or appointee for ECB President. |
| KKR-20261109-40 | 65% | 2026-12-02 | military/conflict | Official delegations of Russia, the United States, and Ukraine meet together in Abu Dhabi between 2026-11-09 and 2026-11-30. | Both the Kremlin website and the Office of the President of Ukraine publish statements confirming a trilateral meeting in Abu Dhabi held between 2026-11-09 and 2026-11-30. |
| KKR-20261109-41 | 65% | 2026-11-25 | military/conflict | UKMTO logs at least one new incident of a commercial vessel attacked or seized in the Strait of Hormuz or Gulf of Oman between 2026-11-10 and 2026-11-23. | The UKMTO incident list shows at least one attack, strike, or seizure of a merchant vessel in the Strait of Hormuz or Gulf of Oman dated 2026-11-10 to 2026-11-23 inclusive. |
| KKR-20261109-42 | 57% | 2026-12-09 | crime/security | Russell Brand lodges an appeal against conviction or sentence with the Court of Appeal of England and Wales between 2026-11-09 and 2026-12-07. | At least two of BBC, Guardian, Reuters, PA Media, or Al Jazeera report that Brand lawyers lodged an appeal application dated between 2026-11-09 and 2026-12-07. |
| KKR-20261109-43 | 69% | 2027-04-02 | economics/markets | Thames Water Utilities Ltd is placed into special administration by the High Court between 2026-11-09 and 2027-03-31. | A High Court order appointing special administrators for Thames Water Utilities Ltd is dated between 2026-11-09 and 2027-03-31, as shown on Companies House or the judiciary website. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5517 issued all-time across 22 forecaster arms · 3795 open (1345 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 124 issued · 124 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 124 | 124 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 195 | 178 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 196 | 194 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 171 | 138 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 509 | 394 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 364 | 350 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*