**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051842Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-05_1613.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261105-24 | 42% | 2026-11-16 | political | Israeli President Isaac Herzog formally tasks Gadi Eisenkot with forming the next government between 2026-11-05 and 2026-11-13. | TRUE if the Office of the President of Israel, or at least two of Reuters, AP and Times of Israel, report the mandate conferred on Eisenkot between 2026-11-05 and 2026-11-13; otherwise FALSE. |
| KKR-20261105-25 | 55% | 2026-12-08 | cyber | The CISA Known Exploited Vulnerabilities catalog carries a Zyxel entry with a date-added value between 2026-11-05 and 2026-12-04. | TRUE if the CISA KEV catalog JSON contains at least one entry with vendorProject Zyxel and dateAdded between 2026-11-05 and 2026-12-04 inclusive; otherwise FALSE. |
| KKR-20261105-26 | 69% | 2026-12-14 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding 2026-12-09. | TRUE if FRED series DFEDTARU, the target range upper limit, is higher for 2026-12-10 than for 2026-12-09; FALSE if equal or lower. |
| KKR-20261105-27 | 42% | 2026-12-15 | political | Mississippi certifies Democrat Scott Colom as winner of the 2026 US Senate election over Senator Cindy Hyde-Smith, with statewide certification issued between 2026-11-06 and 2026-12-11. | TRUE if certified statewide results issued by the Mississippi Secretary of State between 2026-11-06 and 2026-12-11 show Colom with the most votes; FALSE if Hyde-Smith leads or no statewide certification is issued in that window. |
| KKR-20261105-28 | 69% | 2026-12-15 | economics/markets | The 10-year US Treasury constant maturity yield is at or above 5.00 percent on 2026-12-11. Reference: 4.84 percent on the packet date. | TRUE if FRED series DGS10 for 2026-12-11 is 5.00 or higher; FALSE if lower. Reference: 4.84 percent at seal on 2026-11-05. |
| KKR-20261105-29 | 42% | 2027-04-02 | political | At least one chamber of the US Congress passes a joint resolution or bill directing the removal of US armed forces from hostilities against Iran between 2027-01-03 and 2027-03-31. | TRUE if Congress.gov records House or Senate passage, between 2027-01-03 and 2027-03-31, of a joint resolution or bill directing removal of US armed forces from hostilities against Iran; concurrent resolutions do not count. Otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5364 issued all-time across 22 forecaster arms · 3642 open (1220 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 81 issued · 81 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 81 | 81 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 175 | 158 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 173 | 171 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 155 | 122 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 485 | 370 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 337 | 323 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*