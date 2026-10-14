**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 142020Z OCT 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-10-14_1513.md · forecaster: control/baserate · 6 accepted / 4 rejected by validation gate · 0 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20261014-63 | 60% | 2026-12-22 | economics/markets | The ICE Brent front-month futures contract settles at or above 120.00 USD per barrel on at least one trading day between 2026-10-21 and 2026-12-18. Reference: Brent 105.75 USD in the packet market snapshot on 2026-10-14. | An ICE Futures Europe daily settlement for the front-month Brent crude contract is at or above 120.00 USD per barrel on any trading day between 2026-10-21 and 2026-12-18. |
| KKR-20261014-64 | 41% | 2026-11-19 | cyber | CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog between 2026-11-10 and 2026-11-17, the week opening with the November 2026 Patch Tuesday. | The CISA KEV JSON feed lists at least one entry with vendorProject Microsoft and a dateAdded value between 2026-11-10 and 2026-11-17. |
| KKR-20261014-65 | 40% | 2026-12-04 | political | Democratic candidates win at least 218 of the 435 US House seats in the midterm general election held on 2026-11-03. | AP race calls, or certified state results where AP has not called a race, show Democratic candidates winning 218 or more House seats in the 2026-11-03 general election. |
| KKR-20261014-66 | 64% | 2026-11-03 | military/conflict | A Ukrainian drone or missile strike causes a fire or damage at an oil refinery inside Russia on at least one day between 2026-10-15 and 2026-10-31. | Reuters or AP report a strike attributed to Ukraine by Ukrainian or Russian officials that caused fire or damage at an oil refinery in Russia, excluding occupied Ukraine, occurring between 2026-10-15 and 2026-10-31. |
| KKR-20261014-67 | 64% | 2027-01-04 | military/conflict | US forces conduct airstrikes or missile strikes on targets on Iranian land territory on at least one day between 2026-11-04 and 2026-12-31. | The Pentagon or CENTCOM confirms, or Reuters and AP both report, US airstrikes or missile strikes on targets on Iranian land territory occurring between 2026-11-04 and 2026-12-31. |
| KKR-20261014-68 | 42% | 2026-11-18 | disaster | An earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M7.7 Panama mainshock, USGS event us6000u18k, between 2026-10-15 and 2026-11-14. | USGS ComCat lists an event with preferred magnitude 6.0 or greater, epicenter within 200 km of the us6000u18k epicenter, and origin time between 2026-10-15 and 2026-11-14 UTC. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at the meeting concluding on 2026-10-28, lifting the upper bound above 4.00 percent. Referenc" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "CISA adds at least one Ivanti vulnerability other than CVE-2026-104935 to the Known Exploited Vulnerabilities catalog between 2026-10-14 and" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-104935 dateAdded 2026-10-13, before the claimed window 2026-10-14..2026-12-15; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "In the Knesset election held on 2026-10-27, Likud, Shas, United Torah Judaism, Religious Zionism and Otzma Yehudit together win 61 or more o" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "A federal grand jury indictment or criminal information against Abdulrahman Alfozan, the OpenAI engineer charged by complaint over an allege" → REJECTED: cited items name Saudi Arabia; the claim is about California — not one cited item concerns the geography of this claim, so the declared prior is a prior about somewhere else; resolution offers alternative VENUES joined by 'or' (…pacer | or | courtlistener…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

4163 issued all-time across 21 forecaster arms · 3052 open (438 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1475 issued · 1179 open · 264 resolved · 161 hits / 103 misses · **Brier 0.313** against its own base rate 61.0% (climatological 0.238) · **skill -0.317**.

*86 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1475 | 1179 | 264 | 161 | 103 | 0.313 | 61.0% | 0.238 | -0.317 |
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
| manual/opus-5.5/unattested | 174 | 169 | 5 | 3 | 2 | 0.440 | 60.0% | 0.240 | -0.835 |
| manual/opus-5/unattested | 326 | 265 | 51 | 34 | 17 | 0.182 | 66.7% | 0.222 | +0.182 |
| manual/sonnet-5 | 45 | 5 | 39 | 21 | 18 | 0.262 | 53.8% | 0.249 | -0.055 |
| manual/sonnet-5.5/unattested | 131 | 131 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 206 | 131 | 69 | 62 | 0.249 | 52.7% | 0.249 | +0.000 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*