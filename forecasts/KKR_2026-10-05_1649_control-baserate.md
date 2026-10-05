**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 051649Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-05_1516.md · forecaster: control/baserate · 8 accepted / 2 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261005-47 | 69% | 2026-11-17 | military/conflict | US forces conduct at least one strike on a target located on Iranian land territory or Iranian-held islands between 2026-10-06 and 2026-11-13. | CENTCOM, the Pentagon, or the White House acknowledges, or both Reuters and AP report, a US strike on Iranian land or island territory dated between 2026-10-06 and 2026-11-13. |
| KKR-20261005-48 | 58% | 2026-11-17 | economics/markets | ICE Brent front-month futures settle at or above 120.00 USD per barrel on at least one trading day between 2026-10-06 and 2026-11-13. Reference: 101.99 USD per barrel on the packet date. | ICE Brent front-month daily settlement is at or above 120.00 USD per barrel on any trading day between 2026-10-06 and 2026-11-13. Reference: 101.99 on the packet date. |
| KKR-20261005-49 | 58% | 2026-11-17 | economics/markets | The US 10-year Treasury constant-maturity yield is at or above 5.75 percent on at least one trading day between 2026-10-06 and 2026-11-13. Reference: 5.32 percent on the packet date. | FRED series DGS10 reports a daily value at or above 5.75 for any date between 2026-10-06 and 2026-11-13. Reference: 5.32 percent on the packet date. |
| KKR-20261005-50 | 42% | 2026-10-29 | cyber | CISA adds at least one Fortinet product vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-06 and 2026-10-26. | The CISA KEV catalog JSON feed lists at least one entry with vendorProject Fortinet and a dateAdded value between 2026-10-06 and 2026-10-26 inclusive. |
| KKR-20261005-51 | 41% | 2026-12-03 | political | In the Spanish general election held on 2026-11-29, the Partido Popular wins more Congress of Deputies seats than the PSOE. | Official Spanish Interior Ministry results for the general election held on 2026-11-29 show the Partido Popular with more Congress of Deputies seats than the PSOE. |
| KKR-20261005-52 | 41% | 2026-10-28 | political | Flavio Bolsonaro defeats Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25. | The Superior Electoral Court (TSE) official tally for the presidential runoff held on 2026-10-25 shows Flavio Bolsonaro with more valid votes than Lula. |
| KKR-20261005-53 | 33% | 2026-11-03 | crime/security | Japanese prosecutors formally indict the US Marine arrested in Okinawa in October 2026 over the killing of a woman in Naha, on any charge arising from her death, between 2026-10-06 and 2026-10-30. | NHK, Kyodo, Reuters, or AP reports that Naha prosecutors filed an indictment against the arrested Marine on any charge arising from the death of the woman, dated between 2026-10-06 and 2026-10-30. |
| KKR-20261005-54 | 43% | 2026-10-23 | disaster | Russian federal or Irkutsk regional health authorities, or WHO, officially confirm plague infection in at least one human case in Irkutsk Oblast between 2026-10-06 and 2026-10-19. | Rospotrebnadzor, the Russian health ministry, the Irkutsk regional government, or WHO publishes a statement dated between 2026-10-06 and 2026-10-19 naming laboratory-confirmed plague in a human case in Irkutsk Oblast. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The United Arab Emirates Public Prosecution announces criminal charges against, or a trial referral of, the FlyDubai flight FZ1073 co-pilot " → REJECTED: resolution offers alternative VENUES joined by 'or' (…uae attorney general | or | state…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The Global Disaster Alert and Coordination System assigns Red alert level to at least one tropical cyclone on any date between 2026-10-06 an" → REJECTED: resolution offers alternative VENUES joined by 'or' (…   feed, shows alert level red for an episode | or | bulletin dated…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

3445 issued all-time across 21 forecaster arms · 2631 open (238 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1234 issued · 1033 open · 169 resolved · 106 hits / 63 misses · **Brier 0.324** against its own base rate 62.7% (climatological 0.234) · **skill -0.386**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1234 | 1033 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 383 | 204 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 2 | 2 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 5 | 5 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 180 | 145 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 266 | 233 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 87 | 87 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 54 | 54 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*