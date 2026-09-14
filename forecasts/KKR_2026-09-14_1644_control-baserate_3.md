**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 141644Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-14_1516.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260914-44 | 26% | 2026-10-20 | economics/markets | The FRED DGS10 10-year US Treasury constant maturity yield prints 5.00 percent or higher on at least one business day between 2026-09-15 and 2026-10-16. Reference: 4.99 percent at packet seal. | FRED series DGS10 shows a daily value of 5.00 or higher for at least one business day between 2026-09-15 and 2026-10-16 inclusive. Reference: 4.99 at packet seal. |
| KKR-20260914-45 | 26% | 2026-11-03 | economics/markets | ICE Brent crude front-month futures settle at or above 125.00 USD per barrel on at least one trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 at packet seal. | ICE settlement data show a Brent front-month daily settlement at or above 125.00 on any trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 at packet seal. |
| KKR-20260914-46 | 35% | 2026-10-06 | political | The Swedish Election Authority certifies the 2026 Riksdag result between 2026-09-15 and 2026-10-02 with the Social Democrats, Left Party, Greens, and Centre Party holding a combined 175 or more of 349 seats. | Valmyndigheten final certified seat allocation, published between 2026-09-15 and 2026-10-02, gives the Social Democrats, Left, Greens, and Centre combined at least 175 of 349 seats. |
| KKR-20260914-47 | 35% | 2026-09-28 | political | The US Senate records a cloture or passage roll call vote on the Clarity Act digital asset bill between 2026-09-15 and 2026-09-25 and the motion receives at least 60 yea votes. | Senate.gov roll call records show a cloture or passage vote on the Clarity Act between 2026-09-15 and 2026-09-25 receiving 60 or more yeas. |
| KKR-20260914-48 | 28% | 2026-10-19 | cyber | Microsoft ships a fix dated between 2026-09-15 and 2026-10-15 for the September 2026 update issue causing Remote Desktop Services failures on Windows Server, reflected as resolved on Windows release health. | Microsoft Windows release health documentation lists the September Windows Server RDS failure issue as resolved by an update released between 2026-09-15 and 2026-10-15. |
| KKR-20260914-49 | 56% | 2026-11-17 | military/conflict | The government of Iran issues an official announcement closing the Strait of Hormuz to commercial shipping, dated between 2026-09-15 and 2026-11-13 and corroborated by at least two of Reuters, AP, and AFP. | At least two of Reuters, AP, or AFP report an official Iranian government announcement closing the Strait of Hormuz to commercial shipping, announcement dated between 2026-09-15 and 2026-11-13. |
| KKR-20260914-50 | 31% | 2026-10-16 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 6.5 or greater anywhere on Earth with origin time between 2026-09-15 and 2026-10-14 UTC. | The USGS event catalog, queried at the deadline, lists at least one magnitude 6.5 or greater earthquake with origin time between 2026-09-15 and 2026-10-14 UTC. |
| KKR-20260914-51 | 26% | 2027-03-02 | economics/markets | Shares of Anthropic record a first day of trading on the Nasdaq exchange between 2026-09-15 and 2027-02-26. | Nasdaq listing records and at least one major wire report confirm Anthropic shares traded with a first trade date between 2026-09-15 and 2027-02-26. |
| KKR-20260914-52 | 35% | 2027-01-05 | political | The Federal Register publishes an EPA proposed or final rule rescinding or replacing carbon dioxide emission standards for existing fossil fuel power plants, with a publication date between 2026-09-15 and 2026-12-31. | The Federal Register carries an EPA proposed or final rule rescinding or replacing power plant carbon dioxide standards with publication date between 2026-09-15 and 2026-12-31. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A drone strike causing fire or damage at a named oil refinery inside Russia occurs between 2026-09-15 and 2026-10-15, acknowledged by at lea" → REJECTED: resolution offers alternative VENUES joined by 'or' (…russian official | or | state…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2121 issued all-time across 16 forecaster arms · 1785 open (79 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 697 issued · 659 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 697 | 659 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 265 | 136 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 60 | 60 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 96 | 96 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 231 | 228 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 235 | 229 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 234 | 202 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*