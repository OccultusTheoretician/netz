**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 251947Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-25_1520.md · forecaster: manual/fable-5.1/unattested · 9 accepted / 1 rejected by validation gate · 4 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260925-07 | 30% | 2026-11-05 | military/conflict | Between 2026-09-26 and 2026-11-02, the United States government and the government of Iran each publicly confirm acceptance of an agreement under which the Strait of Hormuz is reopened to commercial shipping. | TRUE if, between 2026-09-26 and 2026-11-02, both the White House or State Department and the Iranian Foreign Ministry publicly confirm an agreement providing for reopening the Strait of Hormuz, as reported by Reuters and AP. |
| KKR-20260925-08 | 30% | 2026-11-17 | military/conflict | Between 2026-09-26 and 2026-11-13, the Kremlin and the Office of the President of Ukraine each publicly state that Russia and Ukraine have agreed to a mutual halt on strikes against energy infrastructure. | TRUE if, between 2026-09-26 and 2026-11-13, both the Kremlin and the Ukrainian presidential office publicly confirm a bilateral agreement to stop strikes on energy infrastructure, as reported by Reuters and AP; unilateral or US-only announcements do not count. |
| KKR-20260925-09 | 35% | 2026-11-17 | military/conflict | Between 2026-09-26 and 2026-11-13, the Ethiopian federal government declares a state of emergency covering all or part of the Tigray, Amhara, or Afar regions. | TRUE if, between 2026-09-26 and 2026-11-13, the Ethiopian Council of Ministers or federal parliament issues a state of emergency declaration covering any part of Tigray, Amhara, or Afar, reported by Reuters and AP. |
| KKR-20260925-10 | 65% | 2026-10-30 | economics/markets | The FOMC statement released on 2026-10-28 raises the federal funds target range above 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date. | TRUE if the FOMC statement dated 2026-10-28 on federalreserve.gov sets a federal funds target range whose upper bound exceeds 4.00 percent; a hold or a cut resolves FALSE. Reference: 3.75 to 4.00 percent on the packet date. |
| KKR-20260925-11 | 30% | 2026-11-02 | economics/markets | The ICE Brent crude front-month futures settlement price on 2026-10-30 is below 90.00 USD per barrel. Reference: 99.46 USD on the packet date. | TRUE if the official ICE Futures Europe settlement price for the front-month Brent crude contract on 2026-10-30 is below 90.00 USD per barrel. Reference: 99.46 USD on the packet date. |
| KKR-20260925-12 | 45% | 2026-10-27 | cyber | Between 2026-09-26 and 2026-10-23, CISA adds CVE-2026-48842 (Roundcube Webmail virtuser_query pre-authentication SQL injection) to the Known Exploited Vulnerabilities catalog. | TRUE if the CISA KEV catalog JSON feed lists CVE-2026-48842 with a dateAdded value between 2026-09-26 and 2026-10-23 inclusive. |
| KKR-20260925-13 | 88% | 2026-12-04 | political | Democratic candidates win at least 218 seats in the US House of Representatives in the 2026-11-03 general election, as called by the Associated Press. | TRUE if, by 2026-12-04, the Associated Press has called at least 218 US House races from the 2026-11-03 general election for Democratic candidates. |
| KKR-20260925-14 | 20% | 2027-03-23 | political | Between 2026-09-26 and 2027-03-19, a royal proclamation dissolving the UK Parliament and calling a general election is published in the London Gazette. | TRUE if the London Gazette publishes a proclamation dissolving Parliament for a UK general election with a publication date between 2026-09-26 and 2027-03-19 inclusive. |
| KKR-20260925-15 | 40% | 2026-11-10 | disaster | Between 2026-09-26 and 2026-11-06, the President issues a Major Disaster Declaration for the State of Hawaii for Hurricane Nolo, as listed in the FEMA disaster declarations database. | TRUE if the FEMA declarations database on fema.gov lists a Major Disaster Declaration (DR number) for Hawaii whose incident description names Nolo or its late-September 2026 rainfall, declared between 2026-09-26 and 2026-11-06. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "Between 2026-09-26 and 2026-10-09, Pakistani authorities suspend mobile internet service in Islamabad in connection with the PTI march on th" → REJECTED: resolution offers alternative VENUES joined by 'or' (…suspension of mobile internet | or | mobile data…) — name ONE source of record or define the venue class; an adjudicator must not choose the venue after the fact

## III. LEDGER STANDING

2839 issued all-time across 17 forecaster arms · 2297 open (189 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `manual/fable-5.1/unattested`:** 190 issued · 173 open · 9 resolved · 6 hits / 3 misses · **Brier 0.176** against its own base rate 66.7% (climatological 0.222) · **skill +0.209** · under 30 resolved, this is noise.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 990 | 873 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
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
| manual/opus-5.5/unattested | 10 | 10 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5/unattested | 314 | 250 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*