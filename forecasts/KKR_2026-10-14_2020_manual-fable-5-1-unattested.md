**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 142020Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-23 | 80% | 2026-10-30 | military/conflict | Between 2026-10-15 and 2026-10-28, Saudi authorities or the Saudi-led coalition confirm at least one further Houthi missile or drone launched toward Saudi territory, following the 2026-10-14 Aramco building strike and the Riyadh interception. | Reuters or AP carries an SPA, Saudi defence ministry, or coalition statement confirming a Houthi missile or drone intercepted over or impacting Saudi territory on a date between 2026-10-15 and 2026-10-28. |
| KKR-20261014-24 | 75% | 2026-11-03 | military/conflict | Between 2026-10-15 and 2026-10-31, at least one merchant vessel is struck by a projectile, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman, as logged by UKMTO. | A UKMTO incident notice or advisory records a merchant vessel struck, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman with an incident date between 2026-10-15 and 2026-10-31. |
| KKR-20261014-25 | 55% | 2026-11-17 | economics/markets | The FRED daily WTI spot series DCOILWTICO prints at or above 100.00 dollars per barrel on at least one business day between 2026-10-15 and 2026-11-13. Reference: 94.99 on the packet date. | FRED series DCOILWTICO shows a value of 100.00 or higher for at least one business day dated between 2026-10-15 and 2026-11-13. Reference level: 94.99 on 2026-10-14. |
| KKR-20261014-26 | 20% | 2026-11-16 | cyber | Between 2026-10-15 and 2026-11-13, CISA adds a Ghostscript vulnerability to the KEV catalog. | The CISA KEV catalog JSON contains an entry whose vendorProject or product field contains Ghostscript, with dateAdded between 2026-10-15 and 2026-11-13 inclusive. |
| KKR-20261014-27 | 65% | 2026-12-02 | crime/security | A federal grand jury returns an indictment against the Saudi national arrested in October 2026 for allegedly planting a listening device at OpenAI offices, with the indictment filed between 2026-10-15 and 2026-11-30. | A US district court docket entry or Department of Justice release shows a grand jury indictment of that defendant filed on a date between 2026-10-15 and 2026-11-30. |
| KKR-20261014-28 | 60% | 2026-12-11 | political | Incumbent Republican Roger Marshall receives the most votes in the Kansas US Senate general election held on 2026-11-03. | Official results published by the Kansas Secretary of State show Roger Marshall with the highest vote total among candidates for US Senate in the 2026-11-03 general election. |
| KKR-20261014-29 | 20% | 2026-12-17 | political | The Japanese journalist whose arrest on espionage suspicion Russia announced on 2026-10-14 is released from Russian custody, deported, or exchanged on a date between 2026-10-15 and 2026-12-15. | Reuters, AP, or Kyodo reports the journalist leaving Russian custody by release, deportation, or exchange on a date between 2026-10-15 and 2026-12-15, with the Japanese government confirming. |
| KKR-20261014-30 | 40% | 2026-11-16 | disaster | An earthquake of magnitude 6.0 or greater occurs within 150 km of the USGS epicenter of the M7.7 Panama event us6000u18k, with origin time between 2026-10-15 and 2026-11-13 UTC. | The USGS ComCat catalog lists an event of magnitude 6.0 or greater with epicenter within 150 km of event us6000u18k and origin time between 2026-10-15 00:00 UTC and 2026-11-13 23:59 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At the FOMC meeting of 2026-10-27 and 2026-10-28, the Federal Reserve raises the federal funds target range above the range in effect on 202" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Between 2026-10-15 and 2026-11-13, CISA adds to the KEV catalog at least one Ivanti Connect Secure vulnerability other than CVE-2026-104935." → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-15..2026-11-13; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)

## III. LEDGER STANDING

4125 issued all-time across 21 forecaster arms · 3014 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 345 issued · 287 open · 50 resolved · 34 hits / 16 misses · **Brier 0.248** against its own base rate 68.0% (climatological 0.218) · **skill -0.140**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1452 | 1156 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 1 | 9 | 0 | 9 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 11 | 9 | 1 | 8 | 0.146 | 11.1% | 0.099 | -0.474 |
| lmstudio/auto[post-window] | 422 | 199 | 214 | 63 | 151 | 0.209 | 29.4% | 0.208 | -0.007 |
| lmstudio/auto[pre-verbot] | 60 | 4 | 48 | 13 | 35 | 0.214 | 27.1% | 0.197 | -0.085 |
| lmstudio/qwen36 | 57 | 57 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-abliterated | 52 | 52 | 0 | — | — | not computed | — | — | — |
| lmstudio/qwen36-realist | 58 | 58 | 0 | — | — | not computed | — | — | — |
| lmstudio/realist | 220 | 161 | 58 | 31 | 27 | 0.296 | 53.4% | 0.249 | -0.191 |
| manual/fable | 45 | 18 | 27 | 14 | 13 | 0.180 | 51.9% | 0.250 | +0.279 |
| manual/fable-5 | 38 | 20 | 18 | 10 | 8 | 0.164 | 55.6% | 0.247 | +0.334 |
| manual/fable-5.1/unattested | 345 | 287 | 50 | 34 | 16 | 0.248 | 68.0% | 0.218 | -0.140 |
| manual/fable-5/unattested | 258 | 179 | 70 | 47 | 23 | 0.190 | 67.1% | 0.221 | +0.138 |
| manual/opus-5 | 74 | 44 | 30 | 14 | 16 | 0.210 | 46.7% | 0.249 | +0.156 |
| manual/opus-5.5/unattested | 168 | 163 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 122 | 122 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*