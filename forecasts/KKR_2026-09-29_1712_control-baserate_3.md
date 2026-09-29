**NOTHING CLASSIFIED OR PRIVILEGED**

# KAOS KONTROL REPORT — 291712Z SEP 26

**KKR is the Kaos Kontrol Report** — the daily forecasting stage of the Prescient Desk. It reads the open-source collation, elicits falsifiable projections from a named forecaster arm, runs them through a mechanical gate that publishes its rejections with reasons, and seals what survives into the ledger before any outcome exists.

Window: this run · source: battle_report_2026-09-29_1517.md · forecaster: control/baserate · 7 accepted / 3 rejected by validation gate · 1 rated below 35% (base-rate discipline)

## I. VALIDATED PROJECTIONS

| id | p | deadline | domain | statement | resolves on |
|---|---|---|---|---|---|
| KKR-20260929-51 | 64% | 2026-11-04 | military/conflict | Between 2026-10-01 and 2026-10-31, the United States government and the Iranian government both publicly confirm an agreed arrangement under which Iran reopens the Strait of Hormuz to commercial shipping. | Official statements from both Washington and Tehran dated 2026-10-01 through 2026-10-31, corroborated by at least two of Reuters, AP and AFP, confirm an agreed arrangement for Iran to reopen the Strait of Hormuz to commercial shipping. |
| KKR-20260929-52 | 64% | 2026-12-04 | military/conflict | Between 2026-10-01 and 2026-11-30, Vladimir Putin signs a presidential decree that sets the authorized strength of the Russian armed forces above the 2,441,630 total personnel (1,550,500 active servicemen) fixed by the decree of 2026-09-28. | A decree dated 2026-10-01 through 2026-11-30 on the official Russian legal portal, or reported by Reuters or TASS, sets total armed forces personnel above 2,441,630 or active servicemen above 1,550,500. |
| KKR-20260929-53 | 64% | 2026-10-23 | military/conflict | Between 2026-10-06 and 2026-10-20, US forces strike at least one target on Iranian land territory or on an Iranian island, as publicly confirmed by US Central Command or the US Department of Defense. | US Central Command or the US Department of Defense publicly confirms US strikes on targets in Iran, on land or on Iranian islands and not solely on vessels at sea, dated 2026-10-06 through 2026-10-20. |
| KKR-20260929-54 | 39% | 2026-11-03 | political | Between 2026-09-30 and 2026-10-30, Estonia formally expels, or declares persona non grata, at least one Russian diplomat accredited in Estonia. | The Estonian Ministry of Foreign Affairs, or two of Reuters, AP and ERR, confirm that at least one Russian diplomat was expelled or declared persona non grata by Estonia between 2026-09-30 and 2026-10-30. |
| KKR-20260929-55 | 29% | 2026-11-17 | crime/security | Between 2026-09-30 and 2026-11-13, UK police or the Crown Prosecution Service charge at least one of the five men arrested near RAF Fairford on or about 2026-09-27 with a criminal offence. | Counter Terrorism Policing, a UK police force or the CPS announces a criminal charge against at least one of the five men arrested near RAF Fairford, with the charge dated 2026-09-30 through 2026-11-13. |
| KKR-20260929-56 | 48% | 2026-11-04 | economics/markets | FRED series DGS10 records a 10-year Treasury constant maturity yield of 5.50 percent or higher on at least one date between 2026-10-01 and 2026-10-30. Reference: 5.26 percent in the packet market snapshot dated 2026-09-29. | FRED series DGS10 shows a daily value of 5.50 or higher for any date from 2026-10-01 through 2026-10-30 inclusive. Reference level: 5.26 percent on the packet date 2026-09-29. |
| KKR-20260929-57 | 39% | 2026-11-16 | political | Between 2026-10-01 and 2026-11-06, the US President signs an executive order or proclamation that suspends, lifts or terminates the ban on imports of Canadian alcohol, dairy products or motorcycles that took effect on 2026-09-29. | A presidential document signed 2026-10-01 through 2026-11-06 that suspends, lifts or terminates the import ban on Canadian alcohol, dairy or motorcycles appears on federalregister.gov or whitehouse.gov by the deadline. |

## II. REJECTED BY THE GATE — AUDIT TRAIL

- "The CISA KEV catalog adds at least one entry with vendorProject Apple and a dateAdded value between 2026-10-01 and 2026-10-21 inclusive, sep" → REJECTED: the packet already decides this claim; a forecast must be open at seal -- the packet states CVE-2026-86950 dateAdded 2026-09-29, before the claimed window 2026-10-01..2026-10-21; dateAdded is single-valued and a fresh in-window value would require removal-and-relisting, which has no documented precedent (removals exist: CVE-2022-28958, removed 2023-12-01)
- "On 2026-10-28 the FOMC announces a federal funds target range whose upper bound is above 4.00 percent. Reference: the range set on 2026-09-1" → REJECTED: cited items share no substantive vocabulary with the claim — a citation that does not support its entry makes the 4.02f priors unreadable and forces the keyed/keyless call to default; cite an item that grounds THIS claim
- "Tennessee carries out the execution by lethal injection of Christa Pike on 2026-09-30." → REJECTED: single-day resolution window for an unscheduled event — the row requires this to occur on 2026-09-30 exactly. Price a day, not a window: widen the window or state why the date is fixed

## III. LEDGER STANDING

3097 issued all-time across 18 forecaster arms · 2555 open (260 past deadline — run `python kkr.py --resolve`). **No pooled score is published** — a Brier score belongs to one forecaster; an average across arms is nobody's record.

**This arm — `control/baserate`:** 1106 issued · 989 open · 85 resolved · 50 hits / 35 misses · **Brier 0.327** against its own base rate 58.8% (climatological 0.242) · **skill -0.352**.

*85 projection(s) voided — terminated as unadjudicable, never edited; each is itemised with its reason in [the ledger](ledger.html).*

**STANDING BY ARM** — segregated per RPAS 5.04; no pooled figure exists.

| forecaster arm | issued | open | resolved | hits | misses | Brier | base rate | climatological | skill |
|---|---|---|---|---|---|---|---|---|---|
| control/baserate | 1106 | 989 | 85 | 50 | 35 | 0.327 | 58.8% | 0.242 | -0.352 |
| fogsim/scenario | 1 | 1 | 0 | — | — | not computed | — | — | — |
| kfk/halflife | 10 | 9 | 1 | 0 | 1 | 0.250 | 0.0% | 0.000 | — |
| lmstudio/auto[post-verbot] | 20 | 12 | 8 | 1 | 7 | 0.144 | 12.5% | 0.109 | -0.314 |
| lmstudio/auto[post-window] | 340 | 190 | 141 | 35 | 106 | 0.202 | 24.8% | 0.187 | -0.081 |
| lmstudio/auto[pre-verbot] | 60 | 6 | 46 | 13 | 33 | 0.220 | 28.3% | 0.203 | -0.085 |
| lmstudio/realist | 143 | 138 | 5 | 4 | 1 | 0.373 | 80.0% | 0.160 | -1.334 |
| manual/fable | 45 | 27 | 18 | 10 | 8 | 0.189 | 55.6% | 0.247 | +0.235 |
| manual/fable-5 | 38 | 27 | 11 | 6 | 5 | 0.101 | 54.5% | 0.248 | +0.591 |
| manual/fable-5.1/unattested | 224 | 207 | 9 | 6 | 3 | 0.176 | 66.7% | 0.222 | +0.209 |
| manual/fable-5/unattested | 258 | 237 | 12 | 11 | 1 | 0.214 | 91.7% | 0.076 | -1.797 |
| manual/opus-5 | 74 | 64 | 10 | 3 | 7 | 0.193 | 30.0% | 0.210 | +0.082 |
| manual/opus-5.5/unattested | 48 | 48 | 0 | — | — | not computed | — | — | — |
| manual/opus-5/unattested | 326 | 301 | 15 | 11 | 4 | 0.235 | 73.3% | 0.196 | -0.199 |
| manual/sonnet-5 | 45 | 9 | 35 | 18 | 17 | 0.247 | 51.4% | 0.250 | +0.009 |
| manual/sonnet-5.5/unattested | 7 | 7 | 0 | — | — | not computed | — | — | — |
| manual/sonnet-5/unattested | 342 | 278 | 59 | 31 | 28 | 0.238 | 52.5% | 0.249 | +0.047 |
| operator/human | 10 | 5 | 2 | 1 | 1 | 0.186 | 50.0% | 0.250 | +0.255 |


Full ledger: ledger.html (paged viewer) · ledger_full.html (complete static table) · ledger.json (the record)

---
**NOTHING CLASSIFIED OR PRIVILEGED** · *the gate is mechanical; the ledger is permanent; the system gets scored, not the operator.*