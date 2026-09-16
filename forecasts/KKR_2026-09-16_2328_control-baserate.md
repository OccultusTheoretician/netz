**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162328Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-85 | 24% | 2026-11-12 | economics/markets | The Federal Reserve raises its federal funds target range at a scheduled FOMC decision between 2026-10-16 and 2026-11-06, lifting the target range upper bound by at least 25 basis points. | FRED daily series DFEDTARU shows its 2026-11-06 value at least 0.25 percentage points above its 2026-10-16 value, covering any FOMC decision between 2026-10-16 and 2026-11-06. |
| KKR-20260916-86 | 24% | 2027-01-13 | economics/markets | EIA daily Cushing WTI spot price prints at or above 120.00 USD on at least one date between 2026-09-17 and 2026-12-31. Reference: WTI last 101.87 at packet seal 2026-09-16. | EIA series RWTC, Cushing OK WTI spot FOB, records any daily value at or above 120.00 USD dated 2026-09-17 through 2026-12-31 inclusive. Reference at seal: 101.87. |
| KKR-20260916-87 | 29% | 2026-11-03 | cyber | The CISA Known Exploited Vulnerabilities catalog adds an entry for an Acronis product vulnerability with a dateAdded between 2026-09-16 and 2026-10-30. | The CISA KEV JSON feed contains at least one entry whose vendorProject or product field contains Acronis and whose dateAdded falls between 2026-09-16 and 2026-10-30 inclusive. |
| KKR-20260916-88 | 29% | 2026-11-20 | cyber | At least one putative class action over the CenterPoint Energy cyberattack and customer data theft is filed in a United States federal district court between 2026-09-17 and 2026-11-16. | A US federal district court docket on PACER shows a putative class action naming CenterPoint Energy as defendant, arising from the disclosed data breach, filed 2026-09-17 through 2026-11-16. |
| KKR-20260916-89 | 40% | 2027-03-05 | political | The European Council or the Council of the European Union adopts conclusions or a decision establishing or formally offering associate member status for Canada between 2026-09-17 and 2027-03-01. | Council conclusions or a Council decision published on consilium.europa.eu, dated 2026-09-17 through 2027-03-01, explicitly creates or offers an EU associate membership status for Canada. |
| KKR-20260916-90 | 29% | 2026-11-18 | disaster | GDACS lists at least one wildfire event in Indonesia at Orange or Red alert level with an event start or update date between 2026-09-17 and 2026-11-15. | The public GDACS feed shows a WF event for Indonesia at Orange or Red alert with a start or update date 2026-09-17 through 2026-11-15. |
| KKR-20260916-91 | 61% | 2026-10-21 | military/conflict | Saudi official channels acknowledge at least one Houthi-attributed drone or missile impact or interception over Saudi territory occurring between 2026-09-17 and 2026-10-17. | Saudi Press Agency, the Saudi defense ministry, or Saudi civil defense acknowledges an impact or interception dated 2026-09-17 through 2026-10-17, and Reuters, AP, or AFP carries the acknowledgment by the deadline. |
| KKR-20260916-92 | 61% | 2027-01-06 | military/conflict | Commercial vessel transit through the Strait of Hormuz is suspended or effectively halted for at least 48 consecutive hours at any point between 2026-09-17 and 2026-12-31. | UKMTO advisories or Lloyds List document a suspension or effective halt of commercial Hormuz transit lasting 48 or more consecutive hours between 2026-09-17 and 2026-12-31, corroborated by Reuters or AP. |
| KKR-20260916-93 | 23% | 2027-01-20 | crime/security | The US Department of Justice announces criminal charges against at least one named defendant over a Russia-directed plot to kill or injure a Ukrainian national outside Ukraine, between 2026-09-17 and 2027-01-15. | A justice.gov press release or an indictment unsealed on a federal docket, dated 2026-09-17 through 2027-01-15, charges at least one named person in such a plot. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The United States Senate holds at least one recorded roll call vote on a joint or concurrent resolution directing removal of US armed forces" → REJECTED: the named venue is introduced by 'including', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

2319 issued all-time across 16 forecaster arms · 1917 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 782 issued · 729 open · 53 resolved · 25 hits / 28 misses · **Brier 0.267** against its own base rate 47.2% (climatological 0.249) · **skill -0.071**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 782 | 729 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 113 | 111 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 251 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 263 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 247 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*