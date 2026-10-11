**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 111831Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-11_1517.md · forecaster: manual/sonnet-5.5/unattested · 9 accepted / 1 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261011-41 | 60% | 2026-10-28 | military/conflict | Saudi Arabia or the Saudi-led coalition conducts at least one air or missile strike on a target in Houthi-held Yemen between 2026-10-11 and 2026-10-25. | At least two of Reuters, AP, AFP, BBC or Al Jazeera report a Saudi or coalition air or missile strike on a target in Houthi-held Yemen occurring between 2026-10-11 and 2026-10-25 inclusive. |
| KKR-20261011-42 | 50% | 2026-10-27 | economics/markets | ICE front-month Brent futures settle above 110.00 USD per barrel on at least one trading day between 2026-10-12 and 2026-10-23. Reference: 104.72 at the prior-session close in the packet dated 2026-10-11. | ICE front-month Brent daily settlement exceeds 110.00 on any trading day from 2026-10-12 through 2026-10-23 inclusive, per ICE settlement data. Reference: 104.72 at prior-session close in the packet dated 2026-10-11. |
| KKR-20261011-43 | 27% | 2026-11-17 | economics/markets | The US 10-year Treasury yield published by FRED as series DGS10 exceeds 5.50 percent on at least one date between 2026-10-13 and 2026-11-13. Reference: 5.24 percent at the prior-session close in the packet dated 2026-10-11. | FRED series DGS10 shows a value above 5.50 for at least one observation date from 2026-10-13 through 2026-11-13 inclusive. Reference: 5.24 percent at prior-session close in the packet dated 2026-10-11. |
| KKR-20261011-44 | 42% | 2026-11-10 | cyber | CISA adds at least one Apple product vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-12 and 2026-11-06. | The CISA KEV catalog JSON carries at least one entry with vendorProject Apple and a dateAdded value between 2026-10-12 and 2026-11-06 inclusive. |
| KKR-20261011-45 | 42% | 2026-10-28 | disaster | An earthquake of magnitude 6.5 or greater occurs within 300 km of USGS event us6000u18k, the Panama M7.7 quake, with origin time between 2026-10-12 00:00 UTC and 2026-10-25 23:59 UTC. | USGS ComCat lists an earthquake of magnitude 6.5 or greater within 300 km of event us6000u18k with origin time between 2026-10-12 00:00 UTC and 2026-10-25 23:59 UTC. |
| KKR-20261011-46 | 65% | 2026-10-21 | disaster | Hurricane Simon makes landfall on the Mexican coast with sustained winds of at least 74 mph between 2026-10-11 and 2026-10-18. | US National Hurricane Center advisories or best-track data record the center of Simon crossing the Mexican coast with maximum sustained winds of at least 74 mph between 2026-10-11 and 2026-10-18. |
| KKR-20261011-47 | 88% | 2026-10-21 | political | Pope Leo XIV undergoes surgery on his lung between 2026-10-12 and 2026-10-18. | The Holy See Press Office or Vatican News confirms that Pope Leo XIV underwent lung surgery dated between 2026-10-12 and 2026-10-18 inclusive. |
| KKR-20261011-48 | 40% | 2026-10-21 | political | Between 2026-10-11 and 2026-10-18, both the Kremlin and the Ukrainian presidential office publicly say their side has agreed to or will observe a halt on strikes on energy infrastructure. | Reuters or AP reports statements dated 2026-10-11 to 2026-10-18 in which both a Kremlin official and Zelensky or his office say their side agreed to or will observe a halt on strikes on energy infrastructure. |
| KKR-20261011-49 | 32% | 2026-10-28 | crime/security | Polish police or prosecutors detain or formally charge at least one suspect over the alleged plot to attack Prime Minister Donald Tusk or the defence minister between 2026-10-12 and 2026-10-25. | Reuters, AP or PAP report Polish police or prosecutors detained or charged at least one suspect over the alleged plot against Tusk or the defence minister, action dated 2026-10-12 to 2026-10-25. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "United States forces conduct at least one military strike on a target in Houthi-held Yemen between 2026-10-11 and 2026-10-25." → REJECTED: cited items name Iran, Islamic Republic of, Saudi Arabia; the claim is about United States, Yemen — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else

## III. LEDGER STANDING

3905 issued all-time across 21 forecaster arms · 3091 open (566 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/sonnet-5.5/unattested`:** 104 issued · 104 open · nothing resolved yet — this arm earns a score at its first resolution.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1380 | 1179 | 169 | 106 | 63 | 0.324 | 62.7% | 0.234 | -0.386 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 407 | 228 | 170 | 45 | 125 | 0.205 | 26.5% | 0.195 | -0.056 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/qwen36 | 37 | 37 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 33 | 33 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 211 | 176 | 34 | 26 | 8 | 0.383 | 76.5% | 0.180 | -1.128 |
| manual/fable | 45 | 20 | 25 | 13 | 12 | 0.190 | 52.0% | 0.250 | +0.241 |
| manual/fable-5 | 38 | 23 | 15 | 8 | 7 | 0.130 | 53.3% | 0.249 | +0.479 |
| manual/fable-5.1/unattested | 320 | 287 | 25 | 20 | 5 | 0.207 | 80.0% | 0.160 | -0.296 |
| manual/fable-5/unattested | 258 | 202 | 47 | 36 | 11 | 0.210 | 76.6% | 0.179 | -0.169 |
| manual/opus-5 | 74 | 55 | 19 | 11 | 8 | 0.188 | 57.9% | 0.244 | +0.228 |
| manual/opus-5.5/unattested | 139 | 139 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 286 | 30 | 20 | 10 | 0.217 | 66.7% | 0.222 | +0.025 |
| manual/sonnet-5 | 45 | 7 | 37 | 19 | 18 | 0.250 | 51.4% | 0.250 | +0.000 |
| manual/sonnet-5.5/unattested | 104 | 104 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 237 | 100 | 56 | 44 | 0.263 | 56.0% | 0.246 | -0.069 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*