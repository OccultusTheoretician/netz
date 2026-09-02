**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 020022Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-01_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-15 | 44% | 2026-09-08 | political | Ed Markey defeats Seth Moulton in the Massachusetts Democratic primary for United States Senate held September 1, 2026. | TRUE if Massachusetts Secretary of the Commonwealth results, as reported by AP or a Massachusetts wire service, show Ed Markey receiving more votes than Seth Moulton in the September 1, 2026 Democratic Senate primary. FALSE otherwise. |
| KKR-20260902-16 | 43% | 2026-09-08 | crime/security | District Judge Tony Graf rules that Tyler Robinson is bound over for trial specifically on the aggravated murder count in the killing of Charlie Kirk, following the September 1, 2026 preliminary hearing ruling in Provo, [withheld]. | TRUE if Judge Graf's ruling, as reported by AP, NBC News, or the [withheld] state courts spokesperson, binds Robinson over on the aggravated murder count. FALSE if that count is dismissed or reduced to a lesser charge, or no ruling issues by the deadline. |
| KKR-20260902-17 | 53% | 2026-09-18 | military/conflict | At least one additional commercial vessel is struck, attacked, boarded, or seized in the Strait of Hormuz or Gulf of Oman between 2026-09-02 and 2026-09-16. | TRUE if at least two of Reuters, AP, a UKMTO advisory, or a flag-state government statement report a vessel struck, attacked, boarded, or seized in the Strait of Hormuz or Gulf of Oman during the window. FALSE otherwise. |
| KKR-20260902-18 | 25% | 2026-10-02 | economics/markets | WTI crude oil front-month futures settle at or above 95.00 USD per barrel on any trading day between 2026-09-02 and 2026-09-30. Reference: 88.02 USD per barrel on the packet date, 2026-09-01. | TRUE if the NYMEX WTI front-month settlement price closes at or above 95.00 USD per barrel on any trading day from 2026-09-02 through 2026-09-30 inclusive, per EIA or NYMEX settlement data. FALSE otherwise. |
| KKR-20260902-19 | 25% | 2026-10-19 | economics/markets | The US 10-year Treasury yield closes at or above 5.00 percent on any trading day between 2026-09-02 and 2026-10-15. Reference: 4.77 percent on the packet date, 2026-09-01. | TRUE if the US 10-year Treasury constant maturity yield, per the Treasury daily par yield curve or the FRED DGS10 series, closes at or above 5.00 percent on any date in the window. FALSE otherwise. |
| KKR-20260902-20 | 33% | 2026-09-25 | cyber | CISA adds at least one new Microsoft Exchange Server vulnerability to the Known Exploited Vulnerabilities catalog between 2026-09-02 and 2026-09-23. | TRUE if the CISA KEV catalog shows a dateAdded value in the window for a CVE with vendorProject Microsoft and a product field containing Exchange. FALSE otherwise. |
| KKR-20260902-21 | 52% | 2026-09-17 | disaster | The confirmed or officially reported Nepal flood death toll reaches 1300 or more at any point between 2026-09-02 and 2026-09-15. | TRUE if Nepal disaster authorities, the Red Cross, or a wire service report a confirmed or officially estimated Nepal flood death toll of 1300 or more on or before 2026-09-15. FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The United States federal government enters a lapse in appropriations, a shutdown, beginning October 1, 2026, because Congress has not enact" → REJECTED: the resolution names a different subject than the statement — the claim is about Congress, States, United and the resolution settles on AP, Budget, Management, Office. A row whose resolution checks a different fact can be scored correct while being wrong
- "The United States military conducts a new overt airstrike or missile strike against a target inside Iranian territory between 2026-09-02 and" → REJECTED: resolution offers alternative VENUES joined by 'or' (…us or western government | or | military…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A third distinct PaperCut NG/MF CVE, beyond CVE-2026-82078 and CVE-2026-81578, is added to the CISA Known Exploited Vulnerabilities catalog " → REJECTED: statement and resolution assert opposite directions - the statement claims the event occurs and the resolution resolves TRUE on its absence. A row scored on its complement records the forecast backwards; align the resolution's primary clause with the claim and keep any inverse in the failure condition; the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-82078 dateAdded 2026-08-31, before the claimed window 2026-09-02..2026-09-23; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

1260 issued all-time across 14 forecaster arms · 1099 open (109 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 330 issued · 313 open · 17 resolved · 8 hits / 9 misses · **Brier 0.275** against its own base rate 47.1% (climatological 0.249) · **skill -0.105** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 330 | 313 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 184 | 153 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 138 | 137 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 159 | 156 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 146 | 138 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*