**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 241643Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-24_1520.md · forecaster: manual/fable-5.1/unattested · 8 accepted / 2 rejected by validation gate · 3 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260924-06 | 55% | 2026-10-05 | disaster | The Central Pacific Hurricane Center issues a Hurricane Warning (not merely a Watch) covering any part of Hawaii County for tropical cyclone Nolo in a public advisory dated between 2026-09-24 and 2026-10-01. | TRUE if any NHC or CPHC public advisory for Nolo dated 2026-09-24 through 2026-10-01 (NHC text archive) lists a Hurricane Warning in effect for Hawaii County or any of its zones; otherwise FALSE. |
| KKR-20260924-07 | 27% | 2026-11-04 | economics/markets | The 10-year Treasury constant maturity yield (FRED series DGS10) records a daily value of 5.50 percent or higher on at least one business day between 2026-09-25 and 2026-10-30. Reference: 5.14 percent on the packet date. | TRUE if FRED series DGS10 shows any observation dated 2026-09-25 through 2026-10-30 with a value of 5.50 or higher; FALSE otherwise. Reference: 5.14 percent on the packet date. |
| KKR-20260924-08 | 35% | 2026-10-30 | economics/markets | At its scheduled meeting concluding 2026-10-28, the FOMC raises the federal funds target range above the 3.75 to 4.00 percent range in effect on the packet date. | TRUE if the FOMC statement released 2026-10-28 on federalreserve.gov announces a target range whose upper bound exceeds 4.00 percent; FALSE if the range is held, lowered, or no decision is announced that day. |
| KKR-20260924-09 | 45% | 2026-11-03 | military/conflict | Between 2026-09-24 and 2026-10-30 the Ethiopian Council of Ministers declares a federal state of emergency whose scope includes Tigray Region, in response to the TPLF and allied rebel offensive. | TRUE if between 2026-09-24 and 2026-10-30 the Ethiopian Council of Ministers declares a federal state of emergency whose stated scope includes Tigray Region, reported by ENA or Fana and by Reuters or AP; FALSE otherwise. |
| KKR-20260924-10 | 20% | 2026-11-17 | military/conflict | Between 2026-09-25 and 2026-11-13 the United States and Iran both confirm a new ceasefire, written agreement, or Strait of Hormuz reopening arrangement concluded between the two governments. | TRUE if between 2026-09-25 and 2026-11-13 the White House or State Department and the Iranian Foreign Ministry or IRNA each confirm the same concluded US-Iran ceasefire, agreement, or Hormuz reopening arrangement; talks or progress claims alone are FALSE. |
| KKR-20260924-11 | 45% | 2026-12-08 | political | After the 2026-11-03 midterm elections, Democrats plus independents caucusing with them hold at least 51 seats in the Senate that convenes 2027-01-03, as established by Associated Press race calls and any runoff by 2026-12-08. | TRUE if by 2026-12-08 AP race calls for the 2026-11-03 elections and any runoff, plus holdover seats, give Democrats and Democratic-caucusing independents at least 51 seats in the Senate convening 2027-01-03; FALSE otherwise, including 50-50. |
| KKR-20260924-12 | 12% | 2026-11-03 | political | Between 2026-09-25 and 2026-10-30 the US District Court for the District of Columbia enters an order holding the government or any official in contempt, or imposing sanctions, for violating the 2026-09-24 temporary restraining order restoring White House access for CNN, MS NOW and Politico. | TRUE if between 2026-09-25 and 2026-10-30 the D.D.C. docket in the CNN, MS NOW and Politico hard-pass suit shows an order holding any defendant in contempt or imposing sanctions for TRO noncompliance; show-cause orders alone are FALSE. |
| KKR-20260924-13 | 40% | 2026-11-10 | crime/security | Between 2026-09-25 and 2026-11-06 Polish authorities (National Prosecutor Office, ABW, or police) announce the detention or formal charging of at least one person in connection with the 2026-09-23 fire at the Exatel-operated Starlink ground station at Wola Krobowska. | TRUE if between 2026-09-25 and 2026-11-06 Polish prosecutors, ABW, or police announce a detention or formal charge tied specifically to the Wola Krobowska station fire, reported by PAP, Reuters, or AP; FALSE otherwise. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA Known Exploited Vulnerabilities catalog adds at least one Check Point entry (expected: CVE-2026-85102 or CVE-2026-85103, the VPN ce" → REJECTED: event window opens 2026-09-23, before this row is sealed (2026-09-24, desk-local) — part of the window has already elapsed and the outcome may already exist. A commitment made after the fact is retrodiction, not forecast; open the window today or later
- "The UN General Assembly adopts a resolution appointing the next Secretary-General, for the term beginning 2027-01-01, between 2026-09-25 and" → REJECTED: resolution offers alternative VENUES joined by 'or' (… per the un document record (a/res/81 series) | or | un press release…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2780 issued all-time across 16 forecaster arms · 2238 open (170 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 181 issued · 164 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 964 | 847 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 329 | 179 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 113 | 108 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 181 | 164 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 306 | 242 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*