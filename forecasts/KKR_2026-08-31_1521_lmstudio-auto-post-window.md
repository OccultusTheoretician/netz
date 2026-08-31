**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 311521Z AUG 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-08-31_1519.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260831-01 | 28% | 2026-09-10 | military/conflict | A drone attack on Kyiv, Ukraine, resulting in at least one confirmed casualty, occurs between 2026-09-01 and 2026-09-07. | At least one confirmed casualty from a drone attack on Kyiv, Ukraine, is reported by at least two independent sources from different hostile sides (RU, UA, AXIS) within the event window, with the first report appearing no later than 2026-09-07. |
| KKR-20260831-02 | 45% | 2026-09-24 | cyber | The CISA KEV catalog includes at least one new exploited vulnerability with a public exploit between 2026-09-15 and 2026-09-22. | The CISA KEV catalog carries a date-added value between 2026-09-15 and 2026-09-22 for at least one vulnerability that is marked as actively exploited in the wild. |
| KKR-20260831-03 | 32% | 2026-09-14 | military/conflict | Airstrikes on Gaza City, Gaza Strip, result in at least five confirmed civilian casualties between 2026-09-05 and 2026-09-12. | At least five confirmed civilian casualties from airstrikes on Gaza City are reported by at least two independent sources from different hostile sides (IL, PS, AXIS) within the event window, with the first report appearing no later than 2026-09-12. |
| KKR-20260831-04 | 22% | 2026-09-20 | military/conflict | Iran launches a missile attack on a U.S. military installation in the Persian Gulf region between 2026-09-10 and 2026-09-17. | A missile attack on a U.S. military installation in the Persian Gulf region is confirmed by at least two independent sources from different hostile sides (WEST, AXIS, RU) within the event window, with the first report appearing no later than 2026-09-17. |
| KKR-20260831-05 | 38% | 2026-10-01 | economics/markets | The S&P 500 index closes below 7,500.00 on at least one trading day between 2026-09-21 and 2026-09-28. | The closing value of the S&P 500 index, as reported by the Federal Reserve Economic Data (FRED) or a major exchange, is below 7,500.00 on at least one trading day between 2026-09-21 and 2026-09-28. |
| KKR-20260831-06 | 35% | 2026-09-27 | cyber | A cyberattack exploiting a known vulnerability in Cisco routers, confirmed by CISA, occurs between 2026-09-18 and 2026-09-25. | The CISA KEV catalog includes a vulnerability with a public exploit that is confirmed to have been used in a cyberattack against Cisco routers, with the first report of exploitation appearing between 2026-09-18 and 2026-09-25. |
| KKR-20260831-07 | 25% | 2026-10-10 | disaster | A major flash flood in Nepal results in at least 50 confirmed deaths between 2026-10-01 and 2026-10-08. | At least 50 confirmed deaths from a flash flood in Nepal are reported by at least two independent sources from different hostile sides (PS, WEST, RU) within the event window, with the first report appearing no later than 2026-10-08. |
| KKR-20260831-08 | 27% | 2026-10-29 | cyber | A ransomware attack on a European government agency, confirmed by CISA or a national cybersecurity authority, occurs between 2026-10-20 and 2026-10-27. | A ransomware attack on a European government agency is confirmed by at least two independent sources (CISA, national cybersecurity authority, or major wire service) with a public report confirming the attack between 2026-10-20 and 2026-10-27. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A political scandal involving a U.S. federal official leads to a formal indictment between 2026-10-15 and 2026-10-22." → REJECTED: resolution offers alternative VENUES joined by 'or' (…u.s. department of justice | or | a federal…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A new ceasefire agreement between Israel and Hamas is formally announced by a neutral third party between 2026-11-01 and 2026-11-08." → REJECTED: resolution offers alternative VENUES joined by 'or' (…, un, egypt, qatar) with a public statement | or | press release…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1131 issued all-time across 14 forecaster arms · 970 open (83 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 177 issued · 146 open · 29 resolved · 10 hits / 19 misses · **Brier 0.250** against its own base rate 34.5% (climatological 0.226) · **skill -0.109** · under 30 resolved, this is noise.

*13 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 281 | 264 | 17 | 8 | 9 | 0.275 | 47.1% | 0.249 | -0.105 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 17 | 3 | 1 | 2 | 0.214 | 33.3% | 0.222 | +0.036 |
| lmstudio/auto[post-window] | 177 | 146 | 29 | 10 | 19 | 0.250 | 34.5% | 0.226 | -0.109 |
| lmstudio/auto[pre-verbot] | 60 | 7 | 45 | 13 | 32 | 0.222 | 28.9% | 0.205 | -0.081 |
| manual/fable | 45 | 32 | 13 | 7 | 6 | 0.183 | 53.8% | 0.249 | +0.265 |
| manual/fable-5 | 38 | 34 | 4 | 3 | 1 | 0.086 | 75.0% | 0.188 | +0.540 |
| manual/fable-5/unattested | 114 | 113 | 1 | 1 | 0 | 0.090 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 71 | 3 | 1 | 2 | 0.386 | 33.3% | 0.222 | -0.736 |
| manual/opus-5/unattested | 135 | 132 | 3 | 1 | 2 | 0.141 | 33.3% | 0.222 | +0.366 |
| manual/sonnet-5 | 45 | 25 | 20 | 12 | 8 | 0.231 | 60.0% | 0.240 | +0.037 |
| manual/sonnet-5/unattested | 121 | 113 | 8 | 5 | 3 | 0.174 | 62.5% | 0.234 | +0.257 |
| operator/human | 10 | 6 | 1 | 1 | 0 | 0.122 | 100.0% | 0.000 | — |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*