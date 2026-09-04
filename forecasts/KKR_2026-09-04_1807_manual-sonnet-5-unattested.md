**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 041807Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-04_1518.md · forecaster: manual/sonnet-5/unattested · 9 accepted / 1 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260904-13 | 85% | 2026-09-11 | political | The UN General Assembly will adopt the Togo-sponsored resolution replacing the Mercator projection with the Equal Earth projection at its scheduled vote on 2026-09-04. | TRUE if the UN's official record shows the map resolution adopted, by vote or consensus, on September 4, 2026; otherwise FALSE. |
| KKR-20260904-14 | 27% | 2026-09-11 | political | The AfD will win an outright majority, at least 42 of the 83 seats, in the Saxony-Anhalt Landtag election held 2026-09-06, exceeding its pre-election polling average of roughly 39 projected seats. | TRUE if Sachsen-Anhalt's official results from the September 6, 2026 election allocate 42 or more of 83 seats to AfD; otherwise FALSE. |
| KKR-20260904-15 | 55% | 2026-09-18 | military/conflict | US envoys representing the Trump administration will hold in-person meetings with senior government officials in both Moscow and Kyiv between 2026-09-05 and 2026-09-16 as part of the announced mediation relaunch. | TRUE if two or more of Reuters, AP, BBC, or Al Jazeera report the same US envoy team meeting senior officials in both Moscow and Kyiv between 2026-09-05 and 2026-09-16; otherwise FALSE. |
| KKR-20260904-16 | 12% | 2026-09-18 | economics/markets | The FOMC will cut its federal funds target range below the current 3.50-3.75 percent range, held through a 9-3 vote at the July 29, 2026 meeting, at its next meeting on September 16, 2026. | TRUE if the Federal Reserve's September 16, 2026 statement sets the target range below 3.50-3.75 percent; otherwise FALSE. |
| KKR-20260904-17 | 85% | 2026-09-22 | economics/markets | Treasury/OFAC will publish at least one additional Iran-related sanctions designation under Operation Economic Outcast between 2026-09-05 and 2026-09-19, continuing the near-weekly cadence announced by Secretary Bessent. | TRUE if OFAC's Recent Actions page lists a new Iran-related designation dated between 2026-09-05 and 2026-09-19; otherwise FALSE. |
| KKR-20260904-18 | 14% | 2026-09-22 | disaster | GDACS will upgrade at least one of its four Green forest-fire alerts logged 2026-09-04 (Mozambique event 1031563, DR Congo event 1031500, Zambia event 1031562, Ethiopia event 1031529) to Orange or Red between 2026-09-05 and 2026-09-19. | TRUE if the GDACS page for any of the four listed events shows Orange or Red level between 2026-09-05 and 2026-09-19; otherwise FALSE. |
| KKR-20260904-19 | 78% | 2026-09-29 | cyber | The actively exploited Chrome V8 vulnerability CVE-2026-85046, patched by Google on 2026-09-03, will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-05 and 2026-09-25. | TRUE if the CISA KEV catalog lists CVE-2026-85046 with a dateAdded value between 2026-09-05 and 2026-09-25; otherwise FALSE. |
| KKR-20260904-20 | 15% | 2026-09-29 | political | Sara Duterte will be held in physical government custody for more than 24 continuous hours under the Quezon City Regional Trial Court arrest warrant, at any point between 2026-09-05 and 2026-09-25. | TRUE if two or more of AP, Reuters, or Al Jazeera report Duterte held in custody beyond 24 continuous hours between 2026-09-05 and 2026-09-25; otherwise FALSE. |
| KKR-20260904-21 | 20% | 2026-10-07 | military/conflict | Houthi forces will be reported to have gained physical control of coastal territory directly on the Bab el-Mandeb Strait, beyond their existing inland and Hodeida-area positions, with the advance occurring between 2026-09-05 and 2026-10-05. | TRUE if two or more of Reuters, AP, AFP, or Al Jazeera report Houthi control of strait-front territory, not just Hodeida or inland areas, between 2026-09-05 and 2026-10-05; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "WTI crude oil will close at or above 100.00 USD per barrel on at least one trading day between 2026-09-08 and 2026-10-06. Reference: 90.35 o" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim

## III. LEDGER STANDING

1425 issued all-time across 16 forecaster arms · 1160 open (57 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5/unattested`:** 167 issued · 146 open · 21 resolved · 10 hits / 11 misses · **Brier 0.214** against its own base rate 47.6% (climatological 0.249) · **skill +0.141** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 401 | 373 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 208 | 120 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 4 | 4 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 15 | 15 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 153 | 151 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 174 | 168 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 167 | 146 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*