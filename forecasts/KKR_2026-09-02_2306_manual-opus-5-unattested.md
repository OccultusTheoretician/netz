**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 022306Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-02_1520.md · forecaster: manual/opus-5/unattested · 6 accepted / 4 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260902-51 | 35% | 2026-11-02 | economic | ICE Brent front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-09-03 and 2026-10-30. Reference: 95.33 on the packet date 2026-09-02. | TRUE if the ICE Brent front-month official settlement price equals or exceeds 110.00 on any trading day from 2026-09-03 through 2026-10-30. Reference level 95.33 at seal. |
| KKR-20260902-52 | 48% | 2026-12-02 | economic | The US Treasury 10-year constant maturity par yield closes at or above 5.15 percent on at least one business day between 2026-09-03 and 2026-11-30. Reference: 4.80 percent on 2026-09-02. | TRUE if FRED series DGS10 or the Treasury daily par yield curve records a 10-year value of 5.15 or higher on any date from 2026-09-03 through 2026-11-30. Reference 4.80 at seal. |
| KKR-20260902-53 | 70% | 2026-10-19 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one SonicWall vulnerability with a dateAdded value between 2026-09-03 and 2026-10-15. | TRUE if the CISA KEV catalog JSON contains at least one entry with vendorProject SonicWall and dateAdded from 2026-09-03 through 2026-10-15 inclusive. |
| KKR-20260902-54 | 40% | 2026-12-18 | cyber | The HHS Office for Civil Rights breach portal lists an Aesto Health breach affecting 9,500,000 or more individuals, posted between 2026-09-03 and 2026-12-15. | TRUE if the HHS OCR breach portal shows a single entry naming Aesto Health with individuals affected of 9,500,000 or more and a submission date in that window. |
| KKR-20260902-55 | 85% | 2026-10-05 | military_conflict | Russian official sources confirm UAV interception or debris over Moscow city or Moscow oblast on at least three separate calendar days between 2026-09-03 and 2026-09-30. | TRUE if Russian Ministry of Defence or Moscow mayoral statements, echoed by Reuters or AFP, name three or more distinct dates in that window with UAV interception over Moscow. |
| KKR-20260902-56 | 30% | 2026-10-19 | disaster_infrastructure | A UN OCHA or Nepal NDRRMA report published between 2026-09-03 and 2026-10-15 states a confirmed death toll of 1,500 or more from the 2026 Nepal-Tibet floods. | TRUE if an OCHA situation report on ReliefWeb or an NDRRMA bulletin, published in that window, states 1,500 or more confirmed deaths from the 2026 Nepal flood event. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one commercial vessel is struck by a mine, missile, or drone in the Strait of Hormuz or Gulf of Oman between 2026-09-03 and 2026-09" → REJECTED: the resolution names a different subject than the statement — the claim is about Gulf, Hormuz, Oman, Strait and the resolution settles on AP, Intelligence, Lloyds, Reuters. A row whose resolution checks a different fact can be scored correct while being wrong
- "The US Department of Justice unseals a federal criminal charge over bulk sale of US drivers license data, filed between 2026-09-03 and 2026-" → REJECTED: the resolution names only a venue or register (PACER) and no subject - the register is where to look, not what is claimed; name the subject inside it
- "A lapse in federal appropriations begins between 2026-10-01 and 2026-11-30, triggering furloughs of non-excepted US federal employees." → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Donald Trump and Vladimir Putin meet in person between 2026-09-03 and 2026-11-30." → REJECTED: the resolution names only a venue or register (AFP, AP, Reuters) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

1295 issued all-time across 14 forecaster arms · 1030 open (5 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5/unattested`:** 165 issued · 159 open · 6 resolved · 4 hits / 2 misses · **Brier 0.157** against its own base rate 66.7% (climatological 0.222) · **skill +0.293** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 344 | 316 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 192 | 104 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 146 | 125 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*