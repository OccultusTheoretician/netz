**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 102324Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-10_1519.md · forecaster: manual/fable-5/unattested · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260910-47 | 40% | 2026-09-21 | economics/markets | The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding 2026-09-16, putting the target upper limit above the level in effect on 2026-09-10. | FRED series DFEDTARU records a value for any date from 2026-09-17 through the deadline strictly greater than the value the series records for 2026-09-10. Reference: the recorded 2026-09-10 series value at seal. |
| KKR-20260910-48 | 40% | 2026-11-18 | economics/markets | The spot price of West Texas Intermediate crude reaches 110.00 USD per barrel or higher on at least one day between 2026-09-11 and 2026-11-13. Reference: 100.05 USD on the packet date. | FRED series DCOILWTICO records a daily value at or above 110.00 for any date from 2026-09-11 through 2026-11-13 inclusive, read on the deadline date. Reference: 100.05 on 2026-09-10. |
| KKR-20260910-49 | 75% | 2026-11-04 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least 20 new entries with dateAdded values between 2026-09-11 and 2026-10-31 inclusive. | The public CISA KEV JSON feed, fetched on the deadline date, contains 20 or more entries whose dateAdded field falls between 2026-09-11 and 2026-10-31 inclusive. |
| KKR-20260910-50 | 55% | 2026-11-04 | military/conflict | Houthi forces take control of at least one additional named town or port on the Red Sea coast of Yemen beyond Mocha between 2026-09-11 and 2026-10-31. | At least two of Reuters, AP, AFP, or BBC report Houthi control of a named Red Sea coastal town or port other than Mocha, with the change of control occurring inside the window. |
| KKR-20260910-51 | 15% | 2026-11-06 | military/conflict | The governments of the United States and Iran both announce a ceasefire or mutual suspension of military operations between 2026-09-11 and 2026-11-03. | Official statements from both governments announcing a ceasefire or suspension, each dated inside the window, are carried by at least two of Reuters, AP, AFP. |
| KKR-20260910-52 | 60% | 2026-11-18 | political | The United Nations Security Council holds a recorded vote on a draft resolution concerning Iran, its nuclear program, or the current conflict between 2026-09-11 and 2026-11-15. | Official UN Security Council meeting records show a recorded vote on such a draft, with the meeting dated inside the window; adoption is not required, and a vetoed or failed vote counts. |
| KKR-20260910-53 | 85% | 2026-12-03 | disaster | GDACS issues at least one Red alert for a tropical cyclone with an alert date between 2026-09-11 and 2026-11-30. | The public GDACS feed or site, read on the deadline date, lists a tropical cyclone event at Red alert level with alert issuance dated inside the window. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "At least one putative class action complaint naming IDScan.net or its corporate parent as defendant over the driver license data breach is f" → REJECTED: the resolution names a different subject than the statement — the claim is about IDScan and the resolution settles on CourtListener, PACER. A row whose resolution checks a different fact can be scored correct while being wrong
- "Saudi Arabia conducts and officially acknowledges at least one airstrike on a target inside Yemen between 2026-09-11 and 2026-12-10." → REJECTED: resolution offers alternative VENUES joined by 'or' (…official saudi government | or | saudi-led coalition…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "At least one of the two people arrested in London on 2026-09-10 on suspicion of assisting the Iranian foreign intelligence service is formal" → REJECTED: the resolution names a different subject than the statement — the claim is about Iranian, London and the resolution settles on Crown, Metropolitan, Police, Prosecution. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1861 issued all-time across 16 forecaster arms · 1525 open (54 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5/unattested`:** 203 issued · 200 open · 3 resolved · 3 hits / 0 misses · **Brier 0.153** against its own base rate 100.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 583 | 545 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 249 | 120 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 37 | 37 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 68 | 68 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 213 | 207 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 205 | 173 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*