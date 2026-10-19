**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 192211Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-19_1513.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261019-48 | 42% | 2026-10-28 | political | Flavio Bolsonaro defeats incumbent President Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25. | TRUE if official TSE totals for the 2026-10-25 runoff give Flavio Bolsonaro more than 50 percent of valid votes; FALSE if Lula da Silva receives more than 50 percent. |
| KKR-20261019-49 | 66% | 2026-11-25 | military/conflict | Donald Trump, Vladimir Putin and Xi Jinping hold an in-person three-way meeting, with no other leader taking part, between 2026-11-14 and 2026-11-22 around the APEC summit in Shenzhen. | TRUE if official readouts from at least two of the White House, Kremlin and Xinhua confirm Trump, Putin and Xi met together in person, with no other leader taking part, between 2026-11-14 and 2026-11-22. |
| KKR-20261019-50 | 36% | 2026-12-02 | crime/security | The French government declares a state of emergency under the law of 3 April 1955 for all or part of metropolitan France between 2026-10-20 and 2026-11-30. | TRUE if Legifrance shows a decree declaring the state of emergency under law 55-385 of 3 April 1955 for any part of metropolitan France, published in the Journal officiel from 2026-10-20 through 2026-11-30; otherwise FALSE. |
| KKR-20261019-51 | 42% | 2026-12-11 | political | Democratic Party candidates win at least 218 of the 435 US House seats in the midterm election held on 2026-11-03. | TRUE if AP race calls published by the deadline credit Democratic candidates with 218 or more House seats in the 2026-11-03 election; FALSE otherwise. |
| KKR-20261019-52 | 60% | 2026-12-14 | economics/markets | The upper limit of the federal funds target range is 4.25 percent or higher on 2026-12-10, after the FOMC decisions of 2026-10-28 and 2026-12-09. Reference: 4.00 percent upper limit on 2026-10-19. | TRUE if FRED series DFEDTARU shows 4.25 or higher for 2026-12-10, the day after the 2026-12-09 FOMC decision; FALSE if the 2026-12-10 value is 4.00 or lower. |
| KKR-20261019-53 | 66% | 2027-01-04 | military/conflict | The United States announces the lifting or suspension of its naval blockade of Iranian ports between 2026-10-20 and 2026-12-31. | TRUE if the US President, White House, Pentagon or CENTCOM announces between 2026-10-20 and 2026-12-31 that the blockade of Iranian ports is lifted or suspended, as reported by at least two of Reuters, AP and AFP. |
| KKR-20261019-54 | 46% | 2027-01-19 | cyber | CISA adds at least one of the critical F5 NGINX flaws CVE-2026-15176, CVE-2026-93479 or CVE-2026-97205 to its Known Exploited Vulnerabilities catalog between 2026-10-20 and 2027-01-15. | TRUE if the CISA KEV catalog lists CVE-2026-15176, CVE-2026-93479 or CVE-2026-97205 with a dateAdded value from 2026-10-20 through 2027-01-15; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The Likud list wins more Knesset seats than any other single list in the Israeli election held on 2026-10-27." → REJECTED: measurable claim without a numeric threshold — a row about a quantity must state the number next to its comparator; identifier digits (H.15, S&P 500) do not count
- "Kenya records a cumulative total of 15 or more laboratory-confirmed Ebola cases at any point between 2026-10-20 and 2026-11-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a kenya ministry of health statement | or | who situation report issued from 2026-10-20 t…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The S&P 500 index closes below 7000 on at least one trading day between 2026-10-20 and 2026-12-31. Reference: 7712.71 on 2026-10-19." → REJECTED: the resolution names only a venue or register (FRED, sp) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

4535 issued all-time across 21 forecaster arms · 3183 open (313 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1597 issued · 1214 open · 351 resolved · 216 hits / 135 misses · **Brier 0.316** against its own base rate 61.5% (climatological 0.237) · **skill -0.337**.

*87 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1597 | 1214 | 351 | 216 | 135 | 0.316 | 61.5% | 0.237 | -0.337 |
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
| manual/opus-5.5/unattested | 219 | 208 | 11 | 5 | 6 | 0.362 | 45.5% | 0.248 | -0.460 |
| manual/opus-5/unattested | 326 | 247 | 69 | 48 | 21 | 0.195 | 69.6% | 0.212 | +0.078 |
| manual/sonnet-5 | 45 | 4 | 40 | 22 | 18 | 0.256 | 55.0% | 0.247 | -0.033 |
| manual/sonnet-5.5/unattested | 165 | 162 | 3 | 3 | 0 | 0.009 | 100.0% | 0.000 | — |
| manual/sonnet-5/unattested | 342 | 179 | 158 | 83 | 75 | 0.251 | 52.5% | 0.249 | -0.006 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*