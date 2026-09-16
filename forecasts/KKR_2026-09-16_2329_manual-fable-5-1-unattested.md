**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 162329Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-16_1517.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 2 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260916-94 | 35% | 2026-10-20 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one entry for an Acronis product with a dateAdded value between 2026-09-17 and 2026-10-16. | True if the CISA KEV JSON feed contains at least one entry whose vendorProject or product field contains Acronis, case-insensitive, with dateAdded between 2026-09-17 and 2026-10-16 inclusive. |
| KKR-20260916-95 | 50% | 2026-12-15 | political | Democrats plus independents caucusing with them win at least 51 of 100 US Senate seats for the 120th Congress in the 2026-11-03 general election, including any subsequent runoff. | True if Associated Press race calls published by 2026-12-11 show Democrats and Democratic-caucusing independents holding at least 51 of 100 Senate seats when the 120th Congress convenes. |
| KKR-20260916-96 | 10% | 2027-01-05 | political | Friedrich Merz ceases to hold the office of Federal Chancellor of Germany at some point between 2026-09-17 and 2026-12-31. | True if German federal government or Bundestag records show Merz ceased to hold the office of Federal Chancellor between 2026-09-17 and 2026-12-31; serving as caretaker after a lost confidence vote counts as holding office. |
| KKR-20260916-97 | 90% | 2027-01-05 | crime/security | The defence of Hashim Thaci files a notice of appeal against the Kosovo Specialist Chambers trial judgment of 2026-09-16 between 2026-09-17 and 2026-12-31. | True if the public case record on scp-ks.org shows a notice of appeal filed by the Thaci defence, dated between 2026-09-17 and 2026-12-31 inclusive; a filing that only requests extra time does not count. |
| KKR-20260916-98 | 55% | 2026-12-22 | crime/security | ICC Pre-Trial Chamber I issues a decision confirming at least one charge against Rodrigo Duterte, dated between 2026-09-17 and 2026-12-18. | True if the ICC court records for the Duterte case (ICC-01/21-01/25) show a Pre-Trial Chamber decision on the confirmation of charges, dated between 2026-09-17 and 2026-12-18 inclusive, confirming at least one charge. |
| KKR-20260916-99 | 25% | 2026-10-21 | economics/markets | The FRED series DCOILWTICO (WTI spot, Cushing) observation dated 2026-10-16 is at or above 110.00 USD per barrel. Reference: WTI 101.87 on the packet date. | True if the FRED DCOILWTICO observation dated 2026-10-16 is 110.00 or higher; if no observation exists for that date, use the next posted trading-day observation. |
| KKR-20260916-100 | 38% | 2026-11-02 | economics/markets | At the FOMC meeting concluding 2026-10-28, the Committee raises the federal funds target range above the range in effect on 2026-10-27. | True if the FRED series DFEDTARU (federal funds target range upper limit) observation dated 2026-10-29 is higher than its observation dated 2026-10-27. |
| KKR-20260916-101 | 35% | 2026-10-06 | disaster | Between 2026-09-17 and 2026-10-02, an official Sudanese source reports a death toll of at least 100 from the West Kordofan gold mine collapse reported on 2026-09-16. | True if Reuters, AFP, or Al Jazeera reports in the window a death toll of at least 100 for that collapse, attributed to the Sudanese Mineral Resources Company, a state government, or a Sudanese health authority. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Saudi Arabia conducts at least one airstrike or missile strike against Houthi targets inside Yemen between 2026-09-17 and 2026-10-16, with t" → REJECTED: resolution offers alternative VENUES joined by 'or' (…saudi ministry of defense | or | a houthi-controlled…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The United States and Iran each publicly announce a ceasefire or cessation of hostilities between them between 2026-09-17 and 2026-10-31." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ent statement and an iranian foreign ministry | or | irna statement each announce a ceasefire, tru…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2327 issued all-time across 16 forecaster arms · 1925 open (61 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 121 issued · 119 open · 2 resolved · 0 hits / 2 misses · **Brier 0.156** against its own base rate 0.0% (climatological 0.000) · **skill —** · under 30 resolved, this is noise.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 782 | 729 | 53 | 25 | 28 | 0.267 | 47.2% | 0.249 | -0.071 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 13 | 7 | 1 | 6 | 0.155 | 14.3% | 0.122 | -0.269 |
| lmstudio/auto[post-window] | 280 | 130 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 73 | 68 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 30 | 8 | 5 | 3 | 0.066 | 62.5% | 0.234 | +0.717 |
| manual/fable-5.1/unattested | 121 | 119 | 2 | 0 | 2 | 0.156 | 0.0% | 0.000 | — |
| manual/fable-5/unattested | 258 | 251 | 7 | 7 | 0 | 0.178 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 263 | 256 | 7 | 5 | 2 | 0.137 | 71.4% | 0.204 | +0.329 |
| manual/sonnet-5 | 45 | 11 | 33 | 18 | 15 | 0.249 | 54.5% | 0.248 | -0.004 |
| manual/sonnet-5/unattested | 247 | 204 | 43 | 21 | 22 | 0.207 | 48.8% | 0.250 | +0.172 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*