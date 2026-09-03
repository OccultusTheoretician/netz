**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 030031Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-02_1520.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260903-08 | 49% | 2026-11-03 | military/conflict | Between 2026-09-03 and 2026-10-31 the United States government and the government of Iran each publicly confirm a ceasefire, truce, or mutual halt to strikes between the two states. | TRUE if official statements from both the US government (White House, State Department, or Pentagon) and Iran (Foreign Ministry, SNSC, or Supreme Leader office) confirm a bilateral ceasefire or halt to strikes announced between 2026-09-03 and 2026-10-31. |
| KKR-20260903-09 | 21% | 2026-10-06 | economics/markets | The EIA daily WTI Cushing spot price (FRED series DCOILWTICO) is at or above 100.00 dollars per barrel on at least one observation date between 2026-09-03 and 2026-10-02. Reference: WTI 90.59 on the packet date 2026-09-02. | TRUE if the FRED series DCOILWTICO (EIA Cushing WTI spot, daily) shows a value of 100.00 or higher for any observation date from 2026-09-03 through 2026-10-02 inclusive. |
| KKR-20260903-10 | 21% | 2026-09-09 | economics/markets | The BLS Employment Situation release scheduled for 2026-09-04 reports a first-estimate change in total nonfarm payroll employment for August 2026 below +75,000. Reference: ADP private payrolls +38,000 for August, reported 2026-09-02. | TRUE if the seasonally adjusted change in total nonfarm payroll employment for August 2026, as first printed in the BLS Employment Situation news release dated 2026-09-04, is less than +75,000; later revisions are ignored. |
| KKR-20260903-11 | 30% | 2026-09-18 | cyber | The CISA Known Exploited Vulnerabilities catalog adds at least one CVE with vendorProject SonicWall and a product field naming SMA1000 or SMA 1000 series appliances, with dateAdded between 2026-09-02 and 2026-09-16. | TRUE if the CISA KEV catalog JSON feed contains an entry with vendorProject SonicWall, product containing SMA1000 or SMA 1000, and dateAdded between 2026-09-02 and 2026-09-16 inclusive. |
| KKR-20260903-12 | 35% | 2026-10-06 | political | A lapse in US federal appropriations begins on 2026-10-01: no law providing FY2027 appropriations, full-year or continuing, for every federal department is enacted by the end of 2026-09-30, and OMB or at least one department issues lapse or shutdown guidance effective 2026-10-01. | TRUE if Congress.gov shows no enacted law providing FY2027 appropriations, full-year or continuing, for every federal department by 2026-09-30, and OMB or at least one department publishes lapse or shutdown guidance effective 2026-10-01. |
| KKR-20260903-13 | 35% | 2026-11-03 | political | Between 2026-09-03 and 2026-10-30 the Council of the EU adopts a new numbered package of sanctions against Russia over the war in Ukraine, with the legal acts published in the Official Journal of the European Union. | TRUE if the Official Journal (EUR-Lex) publishes Council legal acts, dated between 2026-09-03 and 2026-10-30, that the Council press release describes as a new numbered sanctions package against Russia; extensions or delistings alone do not count. |
| KKR-20260903-14 | 36% | 2026-10-19 | disaster | The combined official confirmed death toll (excluding missing) from the Nepal-Tibet flood disaster reported from late August 2026 reaches at least 1,500 on any date between 2026-09-03 and 2026-10-15. Reference: reported passing 1,000 on 2026-09-01. | TRUE if Nepal NDRRMA figures, or two of Reuters, AP, AFP citing officials, put the combined confirmed death toll (excluding missing) for the late-August 2026 Nepal-Tibet floods at 1,500 or more on any date from 2026-09-03 through 2026-10-15. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-03 and 2026-09-30 at least one commercial merchant vessel is damaged by a mine, missile, or drone in the Strait of Hormuz, G" → REJECTED: resolution offers alternative VENUES joined by 'or' (…ukmto | or | jmic…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-03 and 2026-11-30 the Government of India issues a formal written notice terminating, withdrawing from, or abrogating the 19" → REJECTED: resolution offers alternative VENUES joined by 'or' (…mea | or | pib…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact
- "Between 2026-09-03 and 2026-12-31 the [withheld] state court presiding over the prosecution of the defendant charged with the September 2025" → REJECTED: the resolution names a different subject than the statement — the claim is about Charlie, Kirk and the resolution settles on AP, Court, Deseret, District. A row whose resolution checks a different fact can be scored correct while being wrong

## III. LEDGER STANDING

1334 issued all-time across 15 forecaster arms · 1069 open (31 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 370 issued · 342 open · 28 resolved · 14 hits / 14 misses · **Brier 0.297** against its own base rate 50.0% (climatological 0.250) · **skill -0.187** · under 30 resolved, this is noise.

*16 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 370 | 342 | 28 | 14 | 14 | 0.297 | 50.0% | 0.250 | -0.187 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 16 | 4 | 1 | 3 | 0.183 | 25.0% | 0.188 | +0.023 |
| lmstudio/auto[post-window] | 192 | 104 | 83 | 15 | 68 | 0.183 | 18.1% | 0.148 | -0.234 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| manual/fable | 45 | 29 | 16 | 9 | 7 | 0.186 | 56.2% | 0.246 | +0.244 |
| manual/fable-5 | 38 | 32 | 6 | 4 | 2 | 0.070 | 66.7% | 0.222 | +0.687 |
| manual/fable-5.1/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/fable-5/unattested | 145 | 143 | 2 | 2 | 0 | 0.225 | 100.0% | 0.000 | — |
| manual/opus-5 | 74 | 65 | 9 | 2 | 7 | 0.213 | 22.2% | 0.173 | -0.230 |
| manual/opus-5/unattested | 165 | 159 | 6 | 4 | 2 | 0.157 | 66.7% | 0.222 | +0.293 |
| manual/sonnet-5 | 45 | 20 | 25 | 14 | 11 | 0.231 | 56.0% | 0.246 | +0.064 |
| manual/sonnet-5/unattested | 152 | 131 | 21 | 10 | 11 | 0.214 | 47.6% | 0.249 | +0.141 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*