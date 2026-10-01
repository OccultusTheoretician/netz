**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011916Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-01_1613.md · forecaster: manual/sonnet-5.5/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261001-44 | 27% | 2026-10-30 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its meeting concluding on 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date. | The FOMC statement released 2026-10-28 sets a target range whose upper bound is above 4.00 percent. Reference: range was 3.75 to 4.00 percent on the packet date. |
| KKR-20261001-45 | 26% | 2026-11-03 | economics/markets | The US 10-year Treasury constant maturity yield (FRED series DGS10) closes at or above 5.50 percent on at least one business day between 2026-10-02 and 2026-10-30. Reference: 5.25 percent on the packet date. | FRED series DGS10 shows at least one daily value of 5.50 or higher dated between 2026-10-02 and 2026-10-30 inclusive. Reference: 5.25 percent on the packet date. |
| KKR-20261001-46 | 50% | 2026-11-09 | political | In the Israeli Knesset election held on 2026-10-27, Likud wins strictly more seats than any other single list. | Israeli Central Elections Committee seat results for the 2026-10-27 election show Likud with more seats than every other list; a tie for first place resolves false. |
| KKR-20261001-47 | 20% | 2026-11-10 | military/conflict | The United States and Iran both publicly confirm an agreement that restores a ceasefire or reopens the Strait of Hormuz to commercial shipping, announced between 2026-10-02 and 2026-11-06. | Both the US government and the Iranian government publicly confirm, between 2026-10-02 and 2026-11-06, an agreement to restore a ceasefire or reopen the Strait of Hormuz, as reported by Reuters and AP. |
| KKR-20261001-48 | 91% | 2026-10-21 | military/conflict | A Ukrainian drone or missile strike damages an oil refinery in Russia or Russian-occupied territory on a date between 2026-10-05 and 2026-10-18. | Reuters or AP reports that a Ukrainian drone or missile strike damaged an oil refinery in Russia or Russian-occupied territory on a date between 2026-10-05 and 2026-10-18, citing Ukrainian or Russian officials. |
| KKR-20261001-49 | 42% | 2026-10-26 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least 22 entries with a dateAdded value between 2026-10-02 and 2026-10-22 inclusive. | The CISA KEV catalog JSON lists at least 22 entries whose dateAdded value falls between 2026-10-02 and 2026-10-22 inclusive. |
| KKR-20261001-50 | 14% | 2026-11-17 | cyber | CISA adds a Kiteworks vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-02 and 2026-11-13 inclusive. | The CISA KEV catalog lists at least one entry with vendorProject Kiteworks and a dateAdded value between 2026-10-02 and 2026-11-13 inclusive. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "A single Russian air attack kills at least 15 people inside the boundaries of Kyiv city on a date between 2026-10-02 and 2026-11-13." → REJECTED: resolution offers alternative VENUES joined by 'or' (…kyiv mayor | or | the ukrainian state emergency…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one of the five men arrested near RAF Fairford on 2026-09-27 is charged with a criminal offence on a date between 2026-10-02 and 20" → REJECTED: resolution offers alternative VENUES joined by 'or' (…local police force | or | the crown prosecution…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The NOAA Climate Prediction Center relative Oceanic Nino Index (RONI) for the three-month season spanning 2026-10-01 to 2026-12-31 is +2.5 C" → REJECTED: event window opens 2026-09-10, before this row is sealed (2026-10-01, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later

## III. LEDGER STANDING

3211 issued all-time across 18 forecaster arms · 2669 open (348 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 24 issued · 24 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1147 | 1030 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 354 | 204 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 154 | 149 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 239 | 222 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 64 | 64 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 24 | 24 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*