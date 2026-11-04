**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041719Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-04_1615.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261104-22 | 55% | 2026-12-07 | cyber | Between 2026-11-05 and 2026-12-04 inclusive, CISA adds at least one Android or Pixel vulnerability (KEV vendorProject Android, or Google with product Android or Pixel) to its Known Exploited Vulnerabilities catalog. | The CISA KEV catalog JSON carries an entry whose vendorProject is Android, or whose vendorProject is Google with product Android or Pixel, with dateAdded between 2026-11-05 and 2026-12-04 inclusive. |
| KKR-20261104-23 | 69% | 2027-01-05 | economics/markets | The 10-year US Treasury constant maturity yield (FRED series DGS10) for 2026-12-31 is below 4.75 percent. Reference: 4.91 percent on the packet date, 2026-11-04. | The FRED DGS10 observation dated 2026-12-31 is strictly below 4.75. Reference level at seal: 4.91 percent on 2026-11-04. If no observation exists for that date, the last prior observation governs. |
| KKR-20261104-24 | 42% | 2027-05-03 | political | Between 2027-01-03 and 2027-04-30 inclusive, President Trump vetoes at least one bill or joint resolution passed by the 120th Congress. | The US Senate Vetoes by President page or Congress.gov records a presidential veto (regular or pocket) of a 120th Congress measure dated between 2027-01-03 and 2027-04-30 inclusive. |
| KKR-20261104-25 | 42% | 2027-01-19 | political | Between 2026-11-05 and 2027-01-15 inclusive, the Knesset approves a new Israeli government in a vote of confidence and that government is sworn in. | A Knesset vote of confidence approves a new government, and the government is sworn in, on a date between 2026-11-05 and 2027-01-15 inclusive, as reported by at least two of Reuters, AP, AFP, Times of Israel. |
| KKR-20261104-26 | 65% | 2026-12-11 | military/conflict | Between 2026-11-05 and 2026-12-04 inclusive, a single Russian missile or drone strike on Ukraine kills 20 or more people according to the Ukrainian official death toll. | Ukrainian national or regional authorities state a death toll of 20 or more from one Russian strike that occurred between 2026-11-05 and 2026-12-04 inclusive, as reported by at least two of Reuters, AP, AFP, BBC. |
| KKR-20261104-27 | 65% | 2027-01-05 | military/conflict | Between 2026-11-05 and 2026-12-31 inclusive, US forces carry out at least one kinetic strike on a target inside Iranian territory that the US government publicly confirms. | An official statement from the Pentagon, CENTCOM or the White House confirms a US strike on a target on Iranian soil conducted between 2026-11-05 and 2026-12-31 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5329 issued all-time across 22 forecaster arms · 3607 open (1018 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 72 issued · 72 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 72 | 72 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 168 | 151 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 169 | 167 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 149 | 116 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 479 | 364 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 334 | 320 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*