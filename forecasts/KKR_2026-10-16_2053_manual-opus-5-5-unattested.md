**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162053Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-16_1513.md · forecaster: manual/opus-5.5/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261016-59 | 82% | 2026-11-12 | military/conflict | A Ukrainian drone or missile strike causes fire or damage at an oil refinery inside internationally recognized Russian territory between 2026-10-19 and 2026-11-08, acknowledged by a Russian official. | Resolves true if Reuters or AP reports a Russian governor, ministry, or company official acknowledging fire or damage at a refinery inside Russia from a Ukrainian strike occurring between 2026-10-19 and 2026-11-08. |
| KKR-20261016-60 | 16% | 2026-12-03 | military/conflict | The United States and Iran each publicly confirm a bilateral ceasefire or truce that takes effect between 2026-10-19 and 2026-11-30. | Resolves true if Reuters and AP both report that the US and Iranian governments each confirmed a bilateral ceasefire or truce taking effect between 2026-10-19 and 2026-11-30. |
| KKR-20261016-61 | 24% | 2026-11-02 | economics/markets | The FOMC raises the federal funds target range at its meeting concluding on 2026-10-28, lifting the upper limit above 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date. | Resolves true if FRED series DFEDTARU, the federal funds target range upper limit, reads above 4.00 for 2026-10-29 following the decision announced 2026-10-28. Reference: 4.00 percent on the packet date. |
| KKR-20261016-62 | 41% | 2027-01-06 | economics/markets | The 10-year Treasury constant-maturity yield recorded for 2026-12-31 is at or above 5.25 percent. Reference: 5.10 percent on the packet date. | Resolves true if FRED series DGS10, the 10-year Treasury constant-maturity yield, shows a value at or above 5.25 for 2026-12-31. Reference: 5.10 percent on the packet date. |
| KKR-20261016-63 | 85% | 2026-11-02 | cyber | CISA adds a BeyondTrust vulnerability to its Known Exploited Vulnerabilities catalog between 2026-10-16 and 2026-10-30, following the exploited Remote Support zero-day patched in October 2026. | Resolves true if the CISA KEV catalog JSON contains an entry with vendorProject BeyondTrust and a dateAdded value between 2026-10-16 and 2026-10-30 inclusive; otherwise false. |
| KKR-20261016-64 | 7% | 2027-01-19 | cyber | CISA adds CVE-2026-99999, the Linux kernel guest-to-host flaw publicized as PwnEscape, to its Known Exploited Vulnerabilities catalog between 2026-10-16 and 2027-01-15. | Resolves true if the CISA KEV catalog JSON lists CVE-2026-99999 with a dateAdded value between 2026-10-16 and 2027-01-15 inclusive; otherwise false. |
| KKR-20261016-65 | 6% | 2027-01-05 | political | Edi Rama resigns or announces his resignation as Prime Minister of Albania, loses a parliamentary confidence vote, or is replaced, between 2026-10-19 and 2026-12-31. | Resolves true if Reuters or AP reports that Edi Rama resigned or announced his resignation as Prime Minister, lost a parliamentary confidence vote, or was replaced, between 2026-10-19 and 2026-12-31. |
| KKR-20261016-66 | 56% | 2026-11-13 | political | James Talarico receives the most votes in the Texas US Senate general election held on 2026-11-03, defeating Ken Paxton. | Resolves true if Texas Secretary of State returns available at the deadline show Talarico with the most votes for US Senate in the 2026-11-03 general election. |
| KKR-20261016-67 | 65% | 2026-11-18 | disaster | At least one earthquake of magnitude 7.0 or greater occurs anywhere in the world between 2026-10-19 and 2026-11-15 UTC. | Resolves true if the USGS ComCat catalog, queried at the deadline, lists at least one event of magnitude 7.0 or greater with origin time between 2026-10-19 and 2026-11-15 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Federal prosecutors file an indictment or information in the criminal case against the Saudi national OpenAI engineer charged with bugging a" → REJECTED: resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4310 issued all-time across 21 forecaster arms · 3199 open (525 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 193 issued · 188 open · 5 resolved · 3 hits / 2 misses · **Brier 0.440** against its own base rate 60.0% (climatological 0.240) · **skill -0.835** · under 30 resolved, this is noise.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1517 | 1221 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 432 | 209 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 71 | 71 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 64 | 64 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 72 | 72 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 224 | 165 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 362 | 304 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 193 | 188 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 146 | 146 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*