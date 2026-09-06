**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051519Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-05_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260905-01 | 65% | 2026-10-05 | economics/markets | Between 2026-09-21 and 2026-09-28, the S&P 500 index will close above 7,750.00 on at least one trading day. | The S&P 500 closes at or above 7,750.00 on at least one trading day between 2026-09-21 and 2026-09-28, based on the official market close from a major exchange. |
| KKR-20260905-02 | 40% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-28, at least one new vulnerability in the PostgreSQL database system will be publicly disclosed and listed in the CISA KEV catalog. | The CISA KEV catalog includes at least one new vulnerability affecting PostgreSQL, with a date-added value between 2026-09-21 and 2026-09-28. |
| KKR-20260905-03 | 55% | 2026-10-05 | economics/markets | Between 2026-09-21 and 2026-09-28, the US dollar will trade above 1.17 against the euro on at least one trading day. | The EUR/USD exchange rate exceeds 1.17 on at least one trading day between 2026-09-21 and 2026-09-28, based on the official market close from a major exchange. |
| KKR-20260905-04 | 25% | 2026-10-05 | disaster | Between 2026-09-21 and 2026-09-28, a new earthquake of magnitude 6.0 or greater will be recorded by the USGS in the Pacific Ring of Fire region. | The USGS Significant Quakes database records at least one earthquake with magnitude 6.0 or greater in the Pacific Ring of Fire region between 2026-09-21 and 2026-09-28. |
| KKR-20260905-05 | 35% | 2026-10-05 | disaster | Between 2026-09-21 and 2026-09-28, at least one new forest fire in Africa will be reported by GDACS Alerts with a green or yellow alert level. | GDACS Alerts reports at least one new forest fire in Africa with a green or yellow alert level between 2026-09-21 and 2026-09-28. |
| KKR-20260905-06 | 20% | 2026-10-05 | cyber | Between 2026-09-21 and 2026-09-28, a major cyberattack exploiting the Citrix NetScaler auth bypass vulnerability will be confirmed by two or more independent sources. | At least two independently biased sources (e.g., western, iranian, pro-ukraine, pro-russia) confirm a cyberattack exploiting the Citrix NetScaler auth bypass vulnerability (CVE-2026-XXXX) between 2026-09-21 and 2026-09-28. |
| KKR-20260905-07 | 15% | 2026-10-05 | military/conflict | Between 2026-09-21 and 2026-09-28, the US will launch a new military operation in the Middle East targeting Iranian proxies, confirmed by at least two independent outlets. | At least two independently biased outlets (e.g., western, iranian, pro-ukraine, pro-russia) confirm a new US military operation in the Middle East targeting Iranian proxies between 2026-09-21 and 2026-09-28. |
| KKR-20260905-08 | 45% | 2026-10-05 | political | Between 2026-09-21 and 2026-09-28, a new political scandal involving a US government official will be reported by two or more major news outlets with differing political leanings. | At least two major news outlets with differing political leanings (e.g., BBC World, Guardian World, CNBC Top News, Al Jazeera) report a new political scandal involving a US government official between 2026-09-21 and 2026-09-28. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-21 and 2026-09-28, the CISA KEV catalog will include CVE-2026-85046 with a date-added value of 2026-09-04 or earlier." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-85046 dateAdded 2026-09-04, before the claimed window 2026-09-21..2026-09-28; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "Between 2026-09-21 and 2026-09-28, at least one of the following will be reported by two or more independently biased outlets: a drone strik" → REJECTED: the named venue is introduced by 'e.g.', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

1484 issued all-time across 16 forecaster arms · 1219 open (87 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 216 issued · 128 open · 83 resolved · 15 hits / 68 misses · **Brier 0.183** against its own base rate 18.1% (climatological 0.148) · **skill -0.234**.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 431 | 403 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 216 | 128 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 159 | 157 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 180 | 174 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*