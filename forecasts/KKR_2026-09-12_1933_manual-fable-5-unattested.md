**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 121933Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-12_1654.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260912-40 | 20% | 2026-12-15 | military/conflict | Yemeni government or Saudi-led coalition forces take control of Mayun Island between 2026-09-13 and 2026-12-11. | At least two of Reuters, AP, BBC, Al Jazeera independently report Yemeni government or coalition forces in control of Mayun Island, with the reported capture dated inside the window. |
| KKR-20260912-41 | 12% | 2026-11-06 | military/conflict | Iran and the United States or Israel announce a ceasefire or cessation of hostilities between 2026-09-13 and 2026-11-03. | Official statements from the Iranian government and from the US or Israeli government, each carried by two of Reuters, AP, BBC, Al Jazeera, announce a ceasefire taking effect on or before 2026-11-03. |
| KKR-20260912-42 | 45% | 2026-11-17 | cyber | CISA adds at least one Check Point vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-13 and 2026-11-13. | The public CISA KEV catalog JSON contains at least one entry whose vendorProject names Check Point and whose dateAdded falls between 2026-09-13 and 2026-11-13 inclusive. |
| KKR-20260912-43 | 72% | 2026-11-20 | political | Democratic candidates win control of the US House of Representatives in the scheduled 2026-11-03 midterm elections. | By 2026-11-20, at least two of AP, NBC News, CNN, Fox News project Democrats holding at least 218 US House seats from the 2026-11-03 elections. |
| KKR-20260912-44 | 25% | 2027-01-05 | political | A US congressional committee holds a hearing with a witness affiliated with Anthropic between 2026-09-13 and 2026-12-31. | Congress.gov or an official committee page lists a hearing held inside the window whose published witness list includes a person identified as an Anthropic executive or employee. |
| KKR-20260912-45 | 55% | 2027-01-08 | disaster | A WHO or DRC health ministry publication dated between 2026-09-13 and 2026-12-31 reports cumulative cases in the DRC Ebola epidemic at or above 10,000. | A WHO Disease Outbreak News item, WHO AFRO bulletin, or DRC health ministry situation report dated inside the window states cumulative confirmed plus probable cases of at least 10,000. |
| KKR-20260912-46 | 25% | 2026-12-15 | disaster | USGS catalogs at least one magnitude 6.0 or greater earthquake within 300 km of USGS event us7000tgrk with origin time between 2026-09-13 and 2026-12-12. | A USGS ComCat query returns at least one event of magnitude 6.0 or greater within 300 km of the us7000tgrk epicenter with origin time inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "NYMEX front-month WTI crude oil settles at or above 85.00 USD on Friday 2026-12-18. Reference: 100.05 USD at prior-session close on the pack" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Saudi authorities or Saudi Aramco announce resumption of operations on the oil pipeline shut on 2026-09-12 after the drone attack, between 2" → REJECTED: resolution offers alternative VENUES joined by 'or' (…official saudi government | or | aramco…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "A complaint concerning the Florida DMV database breach confirmed on 2026-09-11 is filed in a US federal district court between 2026-09-13 an" → REJECTED: resolution offers alternative VENUES joined by 'or' (…florida dmv | or | flhsmv breach with a…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1997 issued all-time across 16 forecaster arms · 1661 open (77 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 218 issued · 215 open · 3 resolved · 3 hits / 0 misses · **Brier 0.153** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 638 | 600 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 259 | 130 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 53 | 53 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 82 | 82 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 218 | 215 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 226 | 220 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 218 | 186 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*