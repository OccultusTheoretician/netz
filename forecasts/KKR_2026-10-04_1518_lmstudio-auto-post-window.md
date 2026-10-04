**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041518Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-04_1517.md · forecaster: lmstudio/auto · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261004-01 | 65% | 2026-10-13 | military/conflict | A drone strike on Kyiv's central bridge occurred between 2026-10-04 and 2026-10-11, causing structural damage and disrupting traffic for at least 72 hours. | The CISA KEV catalog carries a date-added value between 2026-10-04 and 2026-10-11, and the USGS Significant Quakes catalog records a magnitude 4.0 or higher earthquake in Kyiv between 2026-10-04 and 2026-10-11. |
| KKR-20261004-02 | 40% | 2026-10-13 | political | Iran will close the Strait of Hormuz to commercial shipping between 2026-10-04 and 2026-10-11, as stated in a public declaration by an Iranian official. | At least two independent, non-aligned news outlets report that Iran has officially declared a closure of the Strait of Hormuz to commercial shipping between 2026-10-04 and 2026-10-11. |
| KKR-20261004-03 | 30% | 2026-10-13 | cyber | A cyberattack exploiting a vulnerability in Microsoft Windows will be publicly reported in the CISA KEV catalog between 2026-10-04 and 2026-10-11. | The CISA KEV catalog carries a date-added value between 2026-10-04 and 2026-10-11, and the vulnerability is linked to Microsoft Windows. |
| KKR-20261004-04 | 55% | 2026-10-13 | economics/markets | The S&P 500 will close below 7,600 points on at least one trading day between 2026-10-04 and 2026-10-11. | The S&P 500 closes below 7,600 points on at least one trading day between 2026-10-04 and 2026-10-11, as recorded in the MarketWatch historical data feed. |
| KKR-20261004-05 | 25% | 2026-10-13 | disaster | A magnitude 5.0 or higher earthquake will be recorded in the Volcano Islands, Japan Region, between 2026-10-04 and 2026-10-11. | The USGS Significant Quakes catalog records a magnitude 5.0 or higher earthquake in the Volcano Islands, Japan Region, between 2026-10-04 and 2026-10-11. |
| KKR-20261004-06 | 45% | 2026-10-13 | disaster | A major forest fire in Brazil will be reported by GDACS Alerts with a green alert level between 2026-10-04 and 2026-10-11. | The GDACS Alerts catalog carries a green alert for a forest fire in Brazil between 2026-10-04 and 2026-10-11. |
| KKR-20261004-07 | 30% | 2026-10-13 | political | The 2026 Brazilian presidential election will result in a runoff between Lula and Bolsonaro, with Lula winning at least 50% of the vote in the first round between 2026-10-04 and 2026-10-11. | Official election results from Brazil's Superior Electoral Court (TSE) confirm that Lula received at least 50% of the valid votes in the first round of the 2026 presidential election between 2026-10-04 and 2026-10-11. |
| KKR-20261004-08 | 20% | 2026-10-13 | cyber | A new vulnerability in Google Gemini will be publicly disclosed in the CISA KEV catalog between 2026-10-04 and 2026-10-11. | The CISA KEV catalog carries a date-added value between 2026-10-04 and 2026-10-11, and the vulnerability is linked to Google Gemini. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A US Marine arrested in Japan on suspicion of murder will be formally charged by a Japanese court between 2026-10-04 and 2026-10-11." → REJECTED: resolution offers alternative VENUES joined by 'or' (…a public court filing | or | official press release from the japanese mini…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Green Party of the UK will pass a resolution equating Zionism with racism between 2026-10-04 and 2026-10-11." → REJECTED: resolution offers alternative VENUES joined by 'or' (…rd from the uk green party's official website | or | a major uk news outlet confirms the passage o…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3330 issued all-time across 18 forecaster arms · 2788 open (502 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `lmstudio/auto[post-window]`:** 376 issued · 226 open · 141 resolved · 35 hits / 106 misses · **Brier 0.202** against its own base rate 24.8% (climatological 0.187) · **skill -0.081**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1193 | 1076 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 376 | 226 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 166 | 161 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 250 | 233 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 78 | 78 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 38 | 38 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*