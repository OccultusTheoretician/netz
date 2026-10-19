**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192211Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-19_1513.md · forecaster: manual/fable-5.1/unattested · 10 accepted / 0 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261019-21 | 45% | 2026-11-19 | military/conflict | Between 2026-10-20 and 2026-11-16, a single air or drone strike in Sudan kills at least 50 people. | True if Reuters, AP, or UN OCHA reports a single air or drone strike in Sudan, occurring between 2026-10-20 and 2026-11-16, with a death toll of at least 50 as of the deadline. |
| KKR-20261019-22 | 65% | 2026-11-19 | military/conflict | Between 2026-10-20 and 2026-11-16, UKMTO records at least one incident in which a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf is fired upon, struck, or seized. | True if a UKMTO incident report dated between 2026-10-20 and 2026-11-16 describes a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf being fired upon, struck by a projectile or mine, or seized. |
| KKR-20261019-23 | 32% | 2026-11-24 | economics/markets | The S&P 500 closes below 7300.00 on at least one trading day between 2026-10-20 and 2026-11-20. Reference: 7712.71 on the packet date 2026-10-19. | True if the S&P 500 official daily close (S&P Dow Jones Indices, FRED series SP500) is below 7300.00 on any trading day from 2026-10-20 through 2026-11-20 inclusive. Reference level: 7712.71 on 2026-10-19. |
| KKR-20261019-24 | 30% | 2026-11-24 | economics/markets | WTI crude front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-10-20 and 2026-11-20. Reference: 97.75 on the packet date 2026-10-19. | True if the official CME NYMEX settlement price for the front-month WTI crude futures contract is at or above 110.00 USD per barrel on any trading day from 2026-10-20 through 2026-11-20. Reference: 97.75 on 2026-10-19. |
| KKR-20261019-25 | 73% | 2026-12-04 | political | Democratic candidates win a majority (at least 218) of US House seats in the 2026-11-03 general election. | True if, by the deadline, the Associated Press has called at least 218 of the 435 US House seats contested in the 2026-11-03 general election for Democratic candidates. |
| KKR-20261019-26 | 56% | 2026-10-28 | political | Flavio Bolsonaro wins the Brazilian presidential run-off held on 2026-10-25. | True if the TSE official totalization (tse.jus.br) for the 2026-10-25 presidential second round shows Flavio Bolsonaro with more valid votes than Luiz Inacio Lula da Silva. |
| KKR-20261019-27 | 55% | 2026-11-13 | political | In the 2026-10-19 Alberta referendum, the option that Alberta should remain a province of Canada receives at least 70.0 percent of valid ballots on the separation-process question. | True if Elections Alberta official results for the 2026-10-19 referendum question on remaining in Canada versus commencing a binding separation referendum process show the remain option at or above 70.0 percent of valid ballots. |
| KKR-20261019-28 | 30% | 2027-01-05 | political | Between 2026-10-19 and 2026-12-31, the French prime minister in office on 2026-10-19 is replaced by a different prime minister, or the Assemblee nationale adopts a motion de censure against the government. | True if, between 2026-10-19 and 2026-12-31, the Journal officiel publishes a decree appointing a different prime minister, or the Assemblee nationale records an adopted motion de censure (at least 289 votes). |
| KKR-20261019-29 | 30% | 2026-12-02 | cyber | Between 2026-10-19 and 2026-11-30, CISA adds at least one NGINX vulnerability to the KEV catalog, following the October 2026 F5 out-of-band NGINX patches. | True if the CISA KEV catalog JSON contains an entry with NGINX in its vendorProject or product field and a dateAdded value between 2026-10-19 and 2026-11-30 inclusive. |
| KKR-20261019-30 | 20% | 2026-11-23 | disaster | Between 2026-10-20 and 2026-11-19, an earthquake of magnitude 6.5 or greater occurs within 300 km of the epicenter of the 2026-10-19 07:49 UTC M6.0 Vanuatu earthquake. | True if the USGS ComCat catalog lists an earthquake of magnitude 6.5 or greater with origin time from 2026-10-20 00:00 UTC through 2026-11-19 23:59 UTC and epicenter within 300 km of the 2026-10-19 07:49 UTC Vanuatu M6.0 epicenter. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

4511 issued all-time across 21 forecaster arms · 3159 open (313 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 388 issued · 307 open · 73 resolved · 47 hits / 26 misses · **Brier 0.233** against its own base rate 64.4% (climatological 0.229) · **skill -0.015**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1580 | 1197 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 445 | 204 | 231 | 70 | 161 | 0.211 | 30.3% | 0.211 | -0.001 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 88 | 87 | 1 | 1 | 0 | 0.722 | 100.0% | 0.000 | — |
| lmstudio/qwen36-abliterated | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 92 | 85 | 7 | 3 | 4 | 0.297 | 42.9% | 0.245 | -0.215 |
| lmstudio/realist | 231 | 144 | 86 | 49 | 37 | 0.321 | 57.0% | 0.245 | -0.311 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 15 | 23 | 13 | 10 | 0.170 | 56.5% | 0.246 | +0.307 |
| manual/fable-5.1/unattested | 388 | 307 | 73 | 47 | 26 | 0.233 | 64.4% | 0.229 | -0.015 |
| manual/fable-5/unattested | 258 | 165 | 84 | 57 | 27 | 0.193 | 67.9% | 0.218 | +0.116 |
| manual/opus-5 | 74 | 42 | 32 | 15 | 17 | 0.204 | 46.9% | 0.249 | +0.182 |
| manual/opus-5.5/unattested | 212 | 201 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 165 | 162 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*