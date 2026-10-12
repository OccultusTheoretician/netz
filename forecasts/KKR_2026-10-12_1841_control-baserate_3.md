**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121841Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-12_1513.md · forecaster: control/baserate · 9 accepted / 1 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261012-72 | 66% | 2026-11-04 | military/conflict | Ukraine strikes a refinery, oil depot, oil terminal, or power plant in Russia or Russian-occupied territory with drones or missiles between 2026-10-13 and 2026-10-31. | YES if Ukrainian military or security officials claim, and Russian federal, regional, or occupation officials acknowledge, an attack on the same refinery, oil depot, oil terminal, or power plant dated between 2026-10-13 and 2026-10-31. |
| KKR-20261012-73 | 66% | 2027-01-05 | military/conflict | Russia and Ukraine agree to a general ceasefire covering all front lines, open-ended or lasting at least 30 days, that takes effect between 2026-10-13 and 2026-12-31. | YES if the Kremlin and the Ukrainian presidential office each publicly confirm a ceasefire covering all front lines, open-ended or of at least 30 days, taking effect between 2026-10-13 and 2026-12-31. |
| KKR-20261012-74 | 66% | 2026-11-10 | military/conflict | A merchant vessel is seized, boarded without authorization, or hit by a projectile, drone, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-10-13 and 2026-11-06. | YES if UKMTO reports a merchant vessel seized, boarded without authorization, or hit by a projectile, drone, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman, with incident date between 2026-10-13 and 2026-11-06. |
| KKR-20261012-75 | 60% | 2026-11-02 | economics/markets | The ICE Brent December 2026 futures contract settles below 100.00 USD per barrel on 2026-10-29. Reference: 106.95 USD on the packet date. | YES if the ICE Futures Europe settlement price for the Brent December 2026 contract on 2026-10-29 is below 100.00 USD per barrel. Reference: 106.95 USD on the packet date. |
| KKR-20261012-76 | 60% | 2026-11-24 | economics/markets | The 10-year US Treasury constant-maturity yield is at or above 5.50 percent on 2026-11-20. Reference: 5.24 percent on the packet date. | YES if FRED series DGS10 shows a value of 5.50 or higher for 2026-11-20. Reference: 5.24 percent on the packet date. |
| KKR-20261012-77 | 45% | 2026-11-17 | cyber | CISA adds a SonicWall SMA 1000 series vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-13 and 2026-11-13. | YES if the CISA KEV catalog carries an entry with vendorProject SonicWall, a product field naming SMA 1000 or SMA1000, and a dateAdded value between 2026-10-13 and 2026-11-13. |
| KKR-20261012-78 | 45% | 2026-12-15 | cyber | CISA adds a GitLab vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-13 and 2026-12-11. | YES if the CISA KEV catalog carries an entry with vendorProject GitLab and a dateAdded value between 2026-10-13 and 2026-12-11. |
| KKR-20261012-79 | 42% | 2027-01-19 | political | A member of the House Democratic Caucus is elected Speaker of the 120th Congress in a House roll call held between 2027-01-03 and 2027-01-15. | YES if the Clerk of the House roll call electing the Speaker of the 120th Congress, held between 2027-01-03 and 2027-01-15, elects a member of the Democratic Caucus. |
| KKR-20261012-80 | 44% | 2026-11-16 | disaster | An earthquake of magnitude 6.0 or greater occurs within 150 km of the epicenter of USGS event us6000u18k, the M7.7 Panama earthquake, between 2026-10-13 and 2026-11-12 UTC. | YES if the USGS ComCat catalog lists an event of magnitude 6.0 or greater within 150 km of the us6000u18k epicenter with an origin time between 2026-10-13 and 2026-11-12 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Saudi Arabia or the Saudi-led coalition conducts airstrikes on Houthi-held territory in Yemen between 2026-10-13 and 2026-11-06." → REJECTED: cited items name Saudi Arabia; the claim is about Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…saudi officials, the saudi press agency, | or | coalition command announce, or reuters or ap …) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4014 issued all-time across 21 forecaster arms · 2986 open (356 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1424 issued · 1150 open · 242 resolved · 152 hits / 90 misses · **Brier 0.316** against its own base rate 62.8% (climatological 0.234) · **skill -0.354**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1424 | 1150 | 242 | 152 | 90 | 0.316 | 62.8% | 0.234 | -0.354 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 413 | 197 | 207 | 61 | 146 | 0.209 | 29.5% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 43 | 43 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 40 | 40 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 51 | 51 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 215 | 171 | 43 | 29 | 14 | 0.350 | 67.4% | 0.220 | -0.592 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 21 | 17 | 9 | 8 | 0.153 | 52.9% | 0.249 | +0.386 |
| manual/fable-5.1/unattested | 328 | 272 | 48 | 32 | 16 | 0.254 | 66.7% | 0.222 | -0.142 |
| manual/fable-5/unattested | 258 | 186 | 63 | 45 | 18 | 0.191 | 71.4% | 0.204 | +0.062 |
| manual/opus-5 | 74 | 50 | 24 | 13 | 11 | 0.203 | 54.2% | 0.248 | +0.180 |
| manual/opus-5.5/unattested | 158 | 154 | 4 | 2 | 2 | 0.445 | 50.0% | 0.250 | -0.780 |
| manual/opus-5/unattested | 326 | 271 | 45 | 30 | 15 | 0.190 | 66.7% | 0.222 | +0.143 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 113 | 113 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 217 | 120 | 68 | 52 | 0.264 | 56.7% | 0.246 | -0.075 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*