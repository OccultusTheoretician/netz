**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 112239Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-11_1518.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 5 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260911-35 | 35% | 2026-10-13 | political | The Green Party candidate Zack Polanski wins the Holborn and St Pancras parliamentary by-election held on 2026-10-08. | TRUE if the declared result of the 2026-10-08 Holborn and St Pancras by-election, per BBC or the UK Parliament website, shows the Green Party candidate elected; otherwise FALSE. |
| KKR-20260911-36 | 35% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 seats in the US House of Representatives in the general election held on 2026-11-03. | TRUE if Associated Press race calls or Clerk of the House official results show Democratic candidates won 218 or more House seats in the 2026-11-03 general election; otherwise FALSE. |
| KKR-20260911-37 | 26% | 2026-09-18 | economics/markets | The FOMC statement released on 2026-09-16 raises the federal funds target range above the range in effect on the packet date. Reference: 3.50 to 3.75 percent on 2026-09-11. | TRUE if the FOMC statement released by the Federal Reserve on 2026-09-16 sets a federal funds target range whose upper bound exceeds 3.75 percent; otherwise FALSE. |
| KKR-20260911-38 | 26% | 2026-10-14 | economics/markets | The EIA daily WTI Cushing spot price (FRED series DCOILWTICO) records at least one value at or above 110.00 dollars for a date between 2026-09-14 and 2026-10-09. Reference: WTI 99.63 on the packet date. | TRUE if FRED series DCOILWTICO contains any observation dated 2026-09-14 through 2026-10-09 with a value of 110.00 or higher; otherwise FALSE. Reference: 99.63 on the packet date. |
| KKR-20260911-39 | 26% | 2026-10-16 | economics/markets | The BLS September 2026 CPI release, scheduled for 2026-10-14, reports a 12-month all-items CPI-U increase (not seasonally adjusted) of 3.6 percent or higher. Reference: 3.4 percent for August 2026 on the packet date. | TRUE if the BLS September 2026 CPI news release, scheduled for 2026-10-14, states the all-items CPI-U rose 3.6 percent or more over the 12 months ending September 2026, not seasonally adjusted; otherwise FALSE. |
| KKR-20260911-40 | 28% | 2026-10-20 | cyber | CISA adds CVE-2026-85706 (GitLab repository commits API path traversal) to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-12 and 2026-10-16. | TRUE if the CISA KEV catalog JSON contains an entry for CVE-2026-85706 whose dateAdded is between 2026-09-12 and 2026-10-16 inclusive; otherwise FALSE. |
| KKR-20260911-41 | 31% | 2026-10-21 | disaster | The DRC Ministry of Health, WHO, or ECDC reports a cumulative total of at least 10,000 confirmed Bundibugyo Ebola cases in the DRC for a data date on or before 2026-10-16. Reference: 6,942 confirmed cases as of 2026-09-09 on the packet date. | TRUE if a DRC Ministry of Health, WHO, or ECDC report states DRC cumulative confirmed Bundibugyo Ebola cases of 10,000 or more with data through a date no later than 2026-10-16; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "United States forces conduct at least one kinetic strike on Houthi targets inside Yemen between 2026-09-12 and 2026-10-09, publicly confirme" → REJECTED: resolution offers alternative VENUES joined by 'or' (…centcom | or | department of defense…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Forces of the internationally recognised Yemen government or the Saudi-led coalition regain control of the Red Sea port city of Mocha (al-Ma" → REJECTED: resolution offers alternative VENUES joined by 'or' (…yemen government | or | saudi coalition…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "The UN Security Council adopts a resolution addressing the Iran nuclear programme or the 2026 Iran war between 2026-09-12 and 2026-10-16." → REJECTED: resolution offers alternative VENUES joined by 'or' (…the un security council resolutions register | or | a un press release records adoption…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

1921 issued all-time across 16 forecaster arms · 1585 open (63 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 610 issued · 572 open · 38 resolved · 18 hits / 20 misses · **Brier 0.280** against its own base rate 47.4% (climatological 0.249) · **skill -0.124**.

*21 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 610 | 572 | 38 | 18 | 20 | 0.280 | 47.4% | 0.249 | -0.124 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 254 | 125 | 120 | 26 | 94 | 0.195 | 21.7% | 0.170 | -0.151 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 45 | 45 | 0 | — | — | not computed | — | — | — |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 31 | 7 | 5 | 2 | 0.063 | 71.4% | 0.204 | +0.692 |
| manual/fable-5.1/unattested | 75 | 75 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 203 | 200 | 3 | 3 | 0 | 0.153 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 219 | 213 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 13 | 31 | 17 | 14 | 0.239 | 54.8% | 0.248 | +0.036 |
| manual/sonnet-5/unattested | 212 | 180 | 32 | 16 | 16 | 0.224 | 50.0% | 0.250 | +0.105 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*