**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 182120Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-18_1512.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261018-58 | 35% | 2027-01-04 | military/conflict | Between 2026-10-19 and 2026-12-31, US military forces conduct at least one strike on a target located on Iranian land territory, including Iranian islands. | YES if the Pentagon, CENTCOM or the White House confirms, or Reuters and AP both report, a US strike on a target on Iranian land territory or islands occurring between 2026-10-19 and 2026-12-31. |
| KKR-20261018-59 | 55% | 2026-11-25 | military/conflict | Between 2026-10-19 and 2026-11-22, a Ukrainian drone or missile strike causes fire or damage at an oil refinery, oil terminal or fuel depot in St Petersburg city or Leningrad Oblast. | YES if Reuters or AP, citing Russian regional or Ukrainian officials, reports a Ukrainian strike causing fire or damage at an oil refinery, oil terminal or fuel depot in St Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-22. |
| KKR-20261018-60 | 15% | 2026-10-30 | economics/markets | At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range. Reference: target range upper bound 4.00 percent on the packet date. | YES if FRED series DFEDTARU for 2026-10-29 is higher than its value for 2026-10-27, reflecting a target-range increase announced at the meeting concluding 2026-10-28. |
| KKR-20261018-61 | 22% | 2026-12-02 | economics/markets | The US 10-year Treasury constant-maturity yield prints at or above 5.50 percent on at least one trading day between 2026-10-19 and 2026-11-30. Reference: 5.10 percent on the packet date. | YES if FRED series DGS10 records a value of 5.50 or higher for any date from 2026-10-19 through 2026-11-30. Reference: 5.10 percent on the packet date. |
| KKR-20261018-62 | 38% | 2026-12-02 | economics/markets | ICE Brent front-month crude futures settle at or above 120.00 USD per barrel on at least one trading day between 2026-10-19 and 2026-11-30. Reference: 109.86 USD on the packet date. | YES if any ICE Futures Europe Brent front-month daily settlement price dated 2026-10-19 through 2026-11-30 is 120.00 USD per barrel or higher. Reference: 109.86 USD on the packet date. |
| KKR-20261018-63 | 22% | 2027-01-04 | political | Between 2026-10-19 and 2026-12-31, the government of French Prime Minister Sebastien Lecornu ends through a censure motion adopted by the National Assembly or a decree terminating his functions as Prime Minister. | YES if the Assemblee nationale adopts a censure motion against the Lecornu government, or the Journal officiel publishes a decree ending his functions as Prime Minister, dated 2026-10-19 through 2026-12-31. |
| KKR-20261018-64 | 10% | 2026-12-04 | political | Democrat Scott Colom defeats incumbent Republican Senator Cindy Hyde-Smith in the Mississippi US Senate general election held on 2026-11-03. | YES if, as of the deadline, AP has called the 2026-11-03 Mississippi US Senate race for Colom or certified state results show Colom winning. |
| KKR-20261018-65 | 85% | 2026-12-04 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | YES if, as of the deadline, AP race calls credit Democratic candidates with 218 or more US House seats from the 2026-11-03 general election. |
| KKR-20261018-66 | 45% | 2026-12-02 | disaster | Between 2026-10-19 and 2026-11-30, the center of an eastern North Pacific tropical storm or hurricane, Trudy included, makes landfall on mainland Mexico or Baja California. | YES if an NHC advisory or update states that the center of an eastern North Pacific tropical storm or hurricane made landfall in mainland Mexico or Baja California between 2026-10-19 and 2026-11-30. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-10-19 and 2026-11-30, CISA adds a SiteGuard vulnerability, such as the exploited Server Edition command-injection flaw CVE-2026" → REJECTED: the named venue is introduced by 'for example', which makes it an example rather than the source of record — the adjudicator still chooses. Strike the softener or name the class exhaustively

## III. LEDGER STANDING

4472 issued all-time across 21 forecaster arms · 3361 open (547 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 212 issued · 207 open · 5 resolved · 3 hits / 2 misses · **Brier 0.440** against its own base rate 60.0% (climatological 0.240) · **skill -0.835** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1571 | 1275 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 444 | 221 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 81 | 81 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 76 | 76 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 86 | 86 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 230 | 171 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 378 | 320 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 212 | 207 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 165 | 165 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*