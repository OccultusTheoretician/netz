**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 281516Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-28_1515.md · forecaster: lmstudio/qwen36 · 7 accepted / 3 rejected by validation gate · 6 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261028-01 | 25% | 2026-11-10 | cyber | The CISA KEV catalog carries a date-added value for a critical zero-day vulnerability affecting Oracle E-Business Suite between 2026-11-01 and 2026-11-07 | A new entry in the CISA Known Exploited Vulnerabilities catalog lists Oracle E-Business Suite with a date-added value within the window |
| KKR-20261028-02 | 30% | 2026-11-10 | political | The UK government publishes legislation or a statutory instrument formally increasing the defense spending target to 2.5 percent of GDP between 2026-11-01 and 2026-11-07 | A UK statutory instrument or Act of Parliament is published with a date of enactment or laying within the window that formally sets the defense spending target at 2.5 percent of GDP |
| KKR-20261028-03 | 65% | 2026-11-10 | disaster | A magnitude 6.0 or greater earthquake is recorded by the USGS between 2026-11-01 and 2026-11-07 | The USGS Significant Earthquakes report lists an event with magnitude 6.0 or higher with a date within the window |
| KKR-20261028-04 | 10% | 2026-11-10 | political | The Federal Election Commission publishes a formal report or press release confirming a successful recovery of campaign finance data lost in the October hack between 2026-11-01 and 2026-11-07 | The FEC website publishes a press release or official report confirming the recovery of the lost campaign finance data within the window |
| KKR-20261028-05 | 5% | 2026-11-10 | economics | The European Commission publishes a regulation or directive formally restricting the import of Chinese-made electric vehicles between 2026-11-01 and 2026-11-07 | The European Commission publishes a regulation or directive formally restricting the import of Chinese-made electric vehicles with a date within the window |
| KKR-20261028-06 | 15% | 2026-11-10 | political | The US Department of Justice files an indictment against a senior official of the Iranian government for cyber operations between 2026-11-01 and 2026-11-07 | The US Department of Justice publishes an indictment document naming a senior Iranian government official for cyber operations with a filing date within the window |
| KKR-20261028-07 | 20% | 2026-11-10 | disaster | A wildfire in Australia reaches a size of 50,000 hectares or more between 2026-11-01 and 2026-11-07 | An official Australian fire authority report or GDACS alert confirms a wildfire in Australia with a size of 50,000 hectares or more with a date within the window |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The S&P 500 index closes below 7,500.00 on any trading day between 2026-11-02 and 2026-11-06" → REJECTED: resolution names no source of record — a stranger must know exactly where to look on the deadline date
- "A ransomware group affiliated with the Nefilim or Hive syndicate publishes a new data leak or extortion campaign between 2026-11-01 and 2026" → REJECTED: resolution offers alternative VENUES joined by 'or' (…threat intelligence report | or | wire…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Bank of England raises the base interest rate by 25 basis points or more between 2026-11-01 and 2026-11-07" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

5087 issued all-time across 21 forecaster arms · 3365 open (448 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/qwen36`:** 132 issued · 115 open · 11 resolved · 4 hits / 7 misses · **Brier 0.227** against its own base rate 36.4% (climatological 0.231) · **skill +0.020** · under 30 resolved, this is noise.

*96 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1788 | 1279 | 477 | 273 | 204 | 0.300 | 57.2% | 0.245 | -0.226 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 9 | 11 | 1 | 10 | 0.123 | 9.1% | 0.083 | -0.490 |
| lmstudio/auto[post-window] | 470 | 201 | 259 | 75 | 184 | 0.204 | 29.0% | 0.206 | +0.009 |
| lmstudio/auto[pre-verbot] | 60 | 3 | 49 | 13 | 36 | 0.212 | 26.5% | 0.195 | -0.086 |
| lmstudio/qwen36 | 132 | 115 | 11 | 4 | 7 | 0.227 | 36.4% | 0.231 | +0.020 |
| lmstudio/qwen36-abliterated | 130 | 128 | 2 | 2 | 0 | 0.381 | 100.0% | 0.000 | — |
| lmstudio/qwen36-realist | 126 | 93 | 31 | 10 | 21 | 0.242 | 32.3% | 0.219 | -0.106 |
| lmstudio/realist | 249 | 128 | 119 | 66 | 53 | 0.317 | 55.5% | 0.247 | -0.285 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 14 | 24 | 14 | 10 | 0.164 | 58.3% | 0.243 | +0.325 |
| manual/fable-5.1/unattested | 455 | 340 | 107 | 61 | 46 | 0.211 | 57.0% | 0.245 | +0.140 |
| manual/fable-5/unattested | 258 | 147 | 102 | 65 | 37 | 0.203 | 63.7% | 0.231 | +0.121 |
| manual/opus-5 | 74 | 39 | 35 | 18 | 17 | 0.213 | 51.4% | 0.250 | +0.146 |
| manual/opus-5.5/unattested | 286 | 272 | 14 | 8 | 6 | 0.312 | 57.1% | 0.245 | -0.275 |
| manual/opus-5/unattested | 326 | 221 | 95 | 61 | 34 | 0.208 | 64.2% | 0.230 | +0.097 |
| manual/sonnet-5 | 45 | 3 | 41 | 22 | 19 | 0.250 | 53.7% | 0.249 | -0.007 |
| manual/sonnet-5.5/unattested | 222 | 207 | 15 | 10 | 5 | 0.122 | 66.7% | 0.222 | +0.451 |
| manual/sonnet-5/unattested | 342 | 141 | 196 | 98 | 98 | 0.245 | 50.0% | 0.250 | +0.019 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*