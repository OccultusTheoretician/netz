**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251947Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-25_1520.md · forecaster: manual/opus-5.5/unattested · 8 accepted / 2 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260925-25 | 33% | 2026-10-26 | cyber | CISA adds the Roundcube Webmail pre-authentication SQL injection flaw CVE-2026-48842 to its Known Exploited Vulnerabilities catalog between 2026-09-25 and 2026-10-23. | TRUE if the CISA KEV catalog JSON feed lists CVE-2026-48842 with a dateAdded value from 2026-09-25 through 2026-10-23; FALSE if the CVE is absent or its dateAdded falls outside that span. |
| KKR-20260925-26 | 27% | 2026-11-02 | military/conflict | Between 2026-09-26 and 2026-10-30, President Trump or the White House announces or confirms an agreement or ceasefire with Iran under which Iran is to reopen the Strait of Hormuz to commercial shipping. | TRUE if AP and Reuters both report that the US president or White House announced or confirmed, between 2026-09-26 and 2026-10-30, an agreement or ceasefire with Iran including reopening of the Strait of Hormuz; otherwise FALSE. |
| KKR-20260925-27 | 42% | 2026-11-04 | military/conflict | Government delegations of the United States, Russia and Ukraine meet in person in a trilateral negotiating session between 2026-09-28 and 2026-10-31. | TRUE if at least two of AP, Reuters and AFP report that US, Russian and Ukrainian government delegations met together in person in one session between 2026-09-28 and 2026-10-31; otherwise FALSE. |
| KKR-20260925-28 | 35% | 2026-11-10 | military/conflict | The Ethiopian federal government declares a new state of emergency covering Tigray, Afar, Amhara or the whole country between 2026-09-26 and 2026-11-06. | TRUE if Reuters, AP or AFP reports that the Ethiopian Council of Ministers or federal parliament declared or approved a new state of emergency covering Tigray, Afar, Amhara or all of Ethiopia between 2026-09-26 and 2026-11-06; otherwise FALSE. |
| KKR-20260925-29 | 25% | 2026-11-10 | military/conflict | Between 2026-09-26 and 2026-11-06, Pakistan or Turkiye officially announces strikes on Houthi targets or a deployment of additional combat or air-defence units to Saudi Arabia. | TRUE if the government or military of Pakistan or Turkiye announces, between 2026-09-26 and 2026-11-06, strikes on Houthi targets or deployment of additional combat or air-defence units to Saudi Arabia, as reported by Reuters or AP; otherwise FALSE. |
| KKR-20260925-30 | 30% | 2026-11-16 | disaster | The President approves a major disaster declaration for the State of Hawaii covering Hurricane Nolo impacts between 2026-09-26 and 2026-11-13. | TRUE if OpenFEMA DisasterDeclarationsSummaries lists a DR declaration for Hawaii with declarationDate from 2026-09-26 through 2026-11-13 and an incident period touching 2026-09-24 through 2026-09-28; otherwise FALSE. |
| KKR-20260925-31 | 38% | 2026-11-24 | economics/markets | The 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one business day between 2026-09-28 and 2026-11-20. Reference: 5.21 percent on the packet date. | TRUE if FRED series DGS10 shows a value of 5.50 or higher for any date from 2026-09-28 through 2026-11-20; FALSE if every value in that span is below 5.50. Reference: 5.21 percent at seal. |
| KKR-20260925-32 | 88% | 2026-12-18 | political | Democratic candidates win at least 218 of the 435 US House seats in the general election held on 2026-11-03. | TRUE if, as of the deadline, AP race calls award at least 218 House seats in the 2026-11-03 general election to Democratic candidates; otherwise FALSE. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The FOMC raises the federal funds target range at its scheduled meeting concluding 2026-10-28. Reference: target range 3.75 to 4.00 percent," → REJECTED: deadline leaves no settling margin — resolution requires third-party confirmation and the deadline (2026-10-30) is 1 day(s) after the window closes (2026-10-29). Cross-bias confirmation does not exist yet on the morning the resolver walks the row; allow >= 2 days
- "The FBI publicly attributes the roughly USD 351.6 million Bitget exchange theft to North Korea between 2026-09-25 and 2026-10-30." → REJECTED: resolution offers alternative VENUES joined by 'or' (…ress release, ic3 public service announcement | or | on-record fbi statement issued…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2856 issued all-time across 17 forecaster arms · 2314 open (189 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/opus-5.5/unattested`:** 18 issued · 18 open · nothing resolved yet — this arm earns a score at its first resolution.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 999 | 882 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 119 | 114 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 190 | 173 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 18 | 18 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 314 | 250 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*