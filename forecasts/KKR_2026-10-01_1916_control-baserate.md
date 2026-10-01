**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 011916Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-01_1613.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261001-23 | 48% | 2026-11-02 | economics/markets | The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28, lifting the upper limit to 4.25 percent or higher. Reference: upper limit 4.00 percent on the packet date. | FRED series DFEDTARU shows 4.25 or higher for 2026-10-29, the day after the 2026-10-27 to 2026-10-28 meeting. Reference: 4.00 on the packet date. |
| KKR-20261001-24 | 48% | 2026-11-03 | economics/markets | The 10-year Treasury constant maturity yield stands at or above 5.50 percent on 2026-10-30. Reference: 5.25 percent on the packet date. | FRED series DGS10 shows 5.50 or higher for 2026-10-30. Reference: 5.25 percent on the packet date. |
| KKR-20261001-25 | 32% | 2026-11-03 | cyber | CISA adds at least 40 vulnerabilities to its Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-10-31. Reference: 43 entries carry a September 2026 date-added value in catalog version 2026.09.30. | The CISA KEV catalog feed carries 40 or more entries with a dateAdded value between 2026-10-01 and 2026-10-31 inclusive. |
| KKR-20261001-26 | 32% | 2026-11-03 | cyber | CISA adds at least one Zammad vulnerability to its Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-10-31. | The CISA KEV catalog feed carries at least one entry naming Zammad in vendorProject or product with a dateAdded value between 2026-10-01 and 2026-10-31 inclusive. |
| KKR-20261001-27 | 64% | 2026-10-19 | military/conflict | Ukrainian forces strike at least one oil refinery on internationally recognized Russian territory between 2026-10-02 and 2026-10-15. | Reuters, AP or the Kyiv Independent reports a Ukrainian strike on a named oil refinery on Russian territory occurring between 2026-10-02 and 2026-10-15, confirmed by the General Staff of Ukraine, the SBU or Russian officials. |
| KKR-20261001-28 | 64% | 2026-11-03 | military/conflict | Ethiopian federal forces or allied militias enter Mekelle city between 2026-10-02 and 2026-10-31. | Reuters, AP or AFP reports, citing the Ethiopian government or independent sources, that federal or allied forces entered Mekelle city on a date between 2026-10-02 and 2026-10-31. |
| KKR-20261001-29 | 39% | 2026-11-05 | political | In the Knesset election scheduled for 2026-10-27, the lists of the outgoing Netanyahu coalition (Likud, Shas, United Torah Judaism, Otzma Yehudit, Religious Zionism) win a combined 61 seats or more. | Israeli Central Elections Committee final results for the 2026-10-27 election give the lists of Likud, Shas, United Torah Judaism, Otzma Yehudit and Religious Zionism, including joint lists containing them, a combined 61 seats or more. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "United States forces strike at least one target on Iranian land territory or islands between 2026-10-02 and 2026-10-23." → REJECTED: resolution offers alternative VENUES joined by 'or' (…al command public release, pentagon statement | or | white house statement confirms united states …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The FBI publicly attributes the September 2026 theft of about 387.5 million dollars from the Bitget exchange to North Korean actors between " → REJECTED: resolution offers alternative VENUES joined by 'or' (…fbi press release | or | ic3 public…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "An earthquake of magnitude 5.0 or greater occurs within 100 km of the 2026-09-30 magnitude 5.6 epicenter off Costa Rica (9.808 N, 86.436 W) " → REJECTED: the resolution names only a venue or register (ComCat, USGS, usgs) and no subject - the register is where to look, not what is claimed; name the subject inside it

## III. LEDGER STANDING

3190 issued all-time across 18 forecaster arms · 2648 open (348 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1140 issued · 1023 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1140 | 1023 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 57 | 57 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 17 | 17 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*