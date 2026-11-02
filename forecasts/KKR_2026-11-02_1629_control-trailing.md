**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 021629Z NOV 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-11-02_1612.md · forecaster: control/trailing · 6 accepted / 0 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261102-26 | 57% | 2026-11-13 | political | Democrat Abdul El-Sayed defeats Republican Mike Rogers in the Michigan US Senate election held on 2026-11-03. | True if the Associated Press calls the 2026-11-03 Michigan US Senate race for El-Sayed by 2026-11-13. False if it calls the race for Rogers or has made no call. |
| KKR-20261102-27 | 57% | 2027-01-11 | political | Senators in the Democratic caucus, including independents who caucus with Democrats, hold at least 51 seats in the US Senate between 2027-01-03 and 2027-01-08. | True if the official Senate.gov party division page shows at least 51 Democrats plus caucusing independents on any day between 2027-01-03 and 2027-01-08. Otherwise false. |
| KKR-20261102-28 | 57% | 2026-12-21 | economics | ICE Brent front-month futures settle at or above 120.00 dollars on at least one trading day between 2026-11-04 and 2026-12-18. | True if an ICE Brent front-month daily settlement is at or above 120.00 between 2026-11-04 and 2026-12-18. Reference: 105.99 on the packet date. Otherwise false. |
| KKR-20261102-29 | 57% | 2027-01-04 | economics | The S&P 500 closes at or above 7,800 on 2026-12-31. | True if FRED series SP500 shows a 2026-12-31 close at or above 7,800. Reference: 7,631.17 on the packet date. Otherwise false. |
| KKR-20261102-30 | 57% | 2026-12-14 | military | US forces conduct at least one kinetic strike on a target on Iranian land territory between 2026-11-04 and 2026-12-11. | True if CENTCOM or the Pentagon acknowledges a US strike on Iranian land territory occurring between 2026-11-04 and 2026-12-11, and both Reuters and AP report it. Otherwise false. |
| KKR-20261102-31 | 57% | 2026-12-07 | cyber | CISA adds GitLab vulnerability CVE-2026-110264 to the Known Exploited Vulnerabilities catalog between 2026-11-03 and 2026-12-04. | True if the CISA KEV catalog carries CVE-2026-110264 with a date-added value between 2026-11-03 and 2026-12-04. Otherwise false. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

Nothing rejected — every projection cleared the gate.

## III. LEDGER STANDING

5273 issued all-time across 22 forecaster arms · 3551 open (721 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/trailing`:** 59 issued · 59 open · nothing resolved yet — this arm earns a score at its first resolution.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| control/trailing | 59 | 59 | 0 | — | — | not computed | — | — | — |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 155 | 138 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 157 | 155 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 144 | 111 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 473 | 358 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 327 | 313 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*