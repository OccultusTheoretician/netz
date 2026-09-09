**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 091806Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-09_1530.md · forecaster: manual/fable-5/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260909-36 | 40% | 2026-10-14 | economics/markets | The US EIA daily Europe Brent spot price records at least one value at or above 110.00 USD per barrel on a day between 2026-09-10 and 2026-10-09. Reference: Brent 101.13 on the packet date. | TRUE if FRED series DCOILBRENTEU shows any daily observation at or above 110.00 dated 2026-09-10 through 2026-10-09 inclusive; otherwise FALSE. |
| KKR-20260909-37 | 25% | 2026-12-03 | economics/markets | The US EIA daily Europe Brent spot price records at least one value at or below 85.00 USD per barrel on a day between 2026-09-10 and 2026-11-30. Reference: Brent 101.13 on the packet date. | TRUE if FRED series DCOILBRENTEU shows any daily observation at or below 85.00 dated 2026-09-10 through 2026-11-30 inclusive; otherwise FALSE. |
| KKR-20260909-38 | 65% | 2026-10-13 | economics/markets | Between 2026-09-10 and 2026-10-09, the Government of Canada announces new retaliatory trade measures responding to the US import ban on Canadian goods disclosed 2026-09-09. | TRUE if an official Government of Canada announcement of retaliatory trade measures made in the window is reported by at least two of Reuters, AP, Bloomberg, or CBC; otherwise FALSE. |
| KKR-20260909-39 | 15% | 2026-11-12 | military/conflict | Commercial tanker transit through the Strait of Hormuz is halted or suspended for at least 48 consecutive hours at some point between 2026-09-10 and 2026-11-09. | TRUE if Reuters plus at least one of Bloomberg or Lloyds List report a suspension of commercial tanker transits through the strait lasting 48 or more consecutive hours within the window; otherwise FALSE. |
| KKR-20260909-40 | 85% | 2026-12-11 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE with vendor Google and product Chrome or Chromium V8 carrying a dateAdded value between 2026-09-10 and 2026-12-08. | TRUE if the public CISA KEV JSON contains an entry with vendorProject Google, product containing Chrome or Chromium, and dateAdded between 2026-09-10 and 2026-12-08 inclusive; otherwise FALSE. |
| KKR-20260909-41 | 65% | 2026-10-20 | cyber | At least one Microsoft CVE from the scheduled October 2026 Patch Tuesday release of 2026-10-13 is added to the CISA KEV catalog with a dateAdded value between 2026-10-13 and 2026-10-16. | TRUE if the public CISA KEV JSON shows a Microsoft-vendor CVE published 2026-10-13 with dateAdded between 2026-10-13 and 2026-10-16 inclusive; otherwise FALSE. |
| KKR-20260909-42 | 60% | 2026-11-13 | political | The Associated Press declares Chris Pappas the winner of the 2026 US Senate general election in New Hampshire held on the scheduled date of 2026-11-03. | TRUE if the AP race call names Pappas the winner of the New Hampshire US Senate general election; FALSE if it names any other candidate or no AP call exists by the deadline. |
| KKR-20260909-43 | 55% | 2026-12-04 | disaster | The USGS earthquake catalog records at least one earthquake of magnitude 6.0 or greater with epicenter between latitude 50 and 56 north and longitude 160 and 180 west, with origin time between 2026-09-10 and 2026-11-30. | TRUE if a USGS ComCat query returns at least one event of magnitude 6.0 or greater inside the stated coordinate box with origin time in the window; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-10 and 2026-10-09, US forces conduct at least one new strike on Iranian territory, Iranian military assets, or Iranian-flagg" → REJECTED: resolution offers alternative VENUES joined by 'or' (…centcom | or | pentagon…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-10 and 2027-03-01, UK authorities announce criminal charges against at least one named individual or corporate entity in the" → REJECTED: resolution offers alternative VENUES joined by 'or' (…metropolitan police | or | crown prosecution…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1786 issued all-time across 16 forecaster arms · 1450 open (47 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 196 issued · 193 open · 3 resolved · 3 hits / 0 misses · **Brier 0.153** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 552 | 514 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 240 | 111 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 32 | 32 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 58 | 58 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 196 | 193 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 206 | 200 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 199 | 167 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*