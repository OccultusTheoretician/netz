# KKR RESOLUTION AUDIT PACKET
Generated 111846Z OCT 26 · 207 projections (part 2 of 2; packet total 566) past deadline, awaiting adjudication.

## YOUR TASK (independent auditor)

For EACH projection below, search public reporting and determine whether its
resolution criterion was met. You are auditing forecasts you did not make.

RULES:
1. Work the RESOLUTION CRITERION as written, not the statement's spirit. If the
   criterion demands two independent sources, one is not enough.
2. Search for DISCONFIRMING evidence as hard as confirming evidence. Note both.
3. If the evidence is genuinely ambiguous or you cannot verify, say so — do NOT
   guess. AMBIGUOUS is a valid verdict and is the correct one when the record is
   unclear.
4. Cite what you found: outlet, date, and what it said. Never assert without a source.
5. You do not know who made these forecasts or at what probability. Do not speculate.
6. HELD-EVIDENCE RULE. Where a projection carries a PYTHON-HELD EVIDENCE
   block, it is the instrument's own fetched, hashed reading of the named
   public source; weigh it above anything you recall. If you have NO search
   capability and a projection carries NO held evidence, return ABSTAIN —
   do not construct evidence from memory. A resolution nobody can re-fetch
   is an assertion, not a verdict. ABSTAIN is a valid and honorable verdict.

Return ONLY a JSON array, no commentary, no markdown fences. Use plain ASCII
straight quotes and do not put quotation marks inside any string value:

[{"id": "KKR-YYYYMMDD-NN", "verdict": "HIT" | "MISS" | "AMBIGUOUS" | "ABSTAIN",
  "confidence": "high" | "moderate" | "low",
  "evidence": "what you found, with outlet and date, 1-3 sentences",
  "disconfirming": "contrary evidence found, or: none found",
  "note": "one line an adjudicator should know before ruling"}]

## PROJECTIONS AWAITING AUDIT


_adjudication-prompt sha256: d5b4fff5dfc1e0dddded2267997363f0c11a462e55ccb7f70f1c6516a4cebfdd_

### KKR-20260901-02
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** A lapse in federal appropriations begins 2026-10-01 because no measure funding agencies past 2026-09-30 is enacted.
- **Resolution criterion:** Congress.gov shows no continuing resolution or appropriations act funding federal agencies past 2026-09-30 signed into law on or before 2026-09-30.
- **Failure condition:** A continuing resolution or appropriations act covering federal agencies past 2026-09-30 becomes public law on or before that date.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-07
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** A lapse in United States federal appropriations begins on 2026-10-01, with agency shutdown procedures taking effect that day.
- **Resolution criterion:** True if no enacted appropriations act or continuing resolution covers 2026-10-01 and OMB directs agencies to execute shutdown plans that day; Congress.gov enacted-legislation records govern.
- **Failure condition:** Enacted appropriations or a continuing resolution covers 2026-10-01 and no agency executes OMB-directed shutdown procedures that day.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-03
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** A lapse in US federal appropriations (government shutdown) begins on 2026-10-01 because no full-year or continuing appropriations covering that date is enacted beforehand.
- **Resolution criterion:** True if OMB or OPM publishes lapse-in-appropriations (shutdown) guidance effective 2026-10-01, or Congress.gov shows no enacted full-year or continuing appropriations covering 2026-10-01 for any federal agency.
- **Failure condition:** Appropriations covering all federal agencies for 2026-10-01 are enacted on or before 2026-09-30 and no shutdown begins on 2026-10-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-36
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, the CISA KEV catalog will include at least one entry for a zero-day vulnerability in SonicWall SMA1000 devices that was actively exploited in the wild.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24 for a vulnerability with CVE identifier or exploit description matching SonicWall SMA1000 zero-day flaws.
- **Failure condition:** The CISA KEV catalog does not contain any entry for a SonicWall SMA1000 zero-day vulnerability with a date-added value in the specified window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184600ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SonicWall SMA1000 zero-day flaws', 'SonicWall SMA1000'] with dateAdded in [2026-09-21..2026-09-24] across 1739 catalog rows

### KKR-20260902-47
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** A lapse in US federal appropriations begins on 2026-10-01 because no full-year appropriations act or continuing resolution covering all agencies is enacted on or before 2026-09-30.
- **Resolution criterion:** Congress.gov shows no enacted government-wide funding measure signed by 2026-09-30 and OPM publicly issues shutdown furlough guidance effective 2026-10-01.
- **Failure condition:** A funding measure covering all agencies is enacted by 2026-09-30, so no lapse begins on 2026-10-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-55
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-05
- **Domain:** military_conflict
- **Claim:** Russian official sources confirm UAV interception or debris over Moscow city or Moscow oblast on at least three separate calendar days between 2026-09-03 and 2026-09-30.
- **Resolution criterion:** TRUE if Russian Ministry of Defence or Moscow mayoral statements, echoed by Reuters or AFP, name three or more distinct dates in that window with UAV interception over Moscow.
- **Failure condition:** Fewer than three distinct calendar days in that window carry an official Russian UAV interception claim over Moscow.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-19
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the Brent crude oil price will exceed $100 per barrel on at least one trading day.
- **Resolution criterion:** The Brent crude oil price exceeds $100 per barrel on at least one trading day between 2026-09-21 and 2026-09-24.
- **Failure condition:** The Brent crude oil price never exceeds $100 per barrel during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-24
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-05
- **Domain:** military_conflict
- **Claim:** A named Ukrainian government body announces disciplinary action, criminal charges, or a completed inquiry finding against personnel involved in the September 2, 2026 SBU-HUR shootout in Kyiv, with the announcement occurring between 2026-09-05 and 2026-10-03.
- **Resolution criterion:** A Ukrainian official body publicly announces a named finding, charge, or disciplinary measure tied to the incident, occurring between 2026-09-05 and 2026-10-03, confirmed by two outlets by 2026-10-05.
- **Failure condition:** No Ukrainian official body publicly announces a named finding, charge, or disciplinary measure tied to the incident in the 2026-09-05 to 2026-10-03 window as of 2026-10-05.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-01
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** A drone strike on Kyiv's security services headquarters occurs between 2026-09-21 and 2026-09-24, resulting in at least one confirmed casualty.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least one report from a hostile side (RU, UA, AXIS) confirms a drone strike on Kyiv's security services HQ with at least one confirmed casualty in corroborating reports.
- **Failure condition:** No report from a hostile side (RU, UA, AXIS) confirms a drone strike on Kyiv's security services HQ with at least one confirmed casualty between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-02
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** A cyberattack exploiting the Chrome V8 zero-day vulnerability is confirmed by at least two independent sources between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least two independent sources (e.g., BleepingComputer, The Hacker News) confirm exploitation of the Chrome V8 zero-day vulnerability during that window.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-09-21 and 2026-09-24, or fewer than two independent sources confirm exploitation of the Chrome V8 zero-day vulnerability during that window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184603ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Chrome V8'] with dateAdded in [2026-09-21..2026-09-24] across 1739 catalog rows

### KKR-20260904-03
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** A major earthquake of magnitude 6.0 or higher occurs in the United States between 2026-09-21 and 2026-09-24, with at least one fatality reported.
- **Resolution criterion:** The USGS Significant Quakes catalog carries a magnitude 6.0 or higher event with a depth of 70km or less, and at least one fatality is reported in corroborating sources (e.g., BBC World, Al Jazeera) between 2026-09-21 and 2026-09-24.
- **Failure condition:** No magnitude 6.0 or higher earthquake with a depth of 70km or less is recorded in the USGS Significant Quakes catalog between 2026-09-21 and 2026-09-24, or no fatality is reported in corroborating sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-04
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** The S&P 500 index closes below 7,600 on at least one trading day between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** The S&P 500 index closes below 7,600 on at least one trading day between 2026-09-21 and 2026-09-24, as recorded in the Market Snapshot data.
- **Failure condition:** The S&P 500 index closes at or above 7,600 on all trading days between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-05
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** A new vulnerability in Microsoft Teams is exploited in a coordinated attack on at least 100 organizations between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24, and at least 100 organizations are confirmed to have been compromised via the Microsoft Teams vulnerability in corroborating reports.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-09-21 and 2026-09-24, or fewer than 100 organizations are confirmed compromised via the Microsoft Teams vulnerability.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184605ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Microsoft Teams'] with dateAdded in [2026-09-21..2026-09-24] across 1739 catalog rows

### KKR-20260904-06
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** A political scandal involving a U.S. presidential candidate leads to a formal indictment by a federal grand jury between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** A federal grand jury issues a formal indictment against a U.S. presidential candidate, confirmed by at least two independent sources (e.g., Guardian World, NPR News) between 2026-09-21 and 2026-09-24.
- **Failure condition:** No federal grand jury issues a formal indictment against a U.S. presidential candidate, confirmed by at least two independent sources, between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-07
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** Iran announces a new military offensive in the Strait of Hormuz between 2026-09-21 and 2026-09-24, confirmed by at least two hostile sides (AXIS, WEST).
- **Resolution criterion:** At least two hostile sides (AXIS, WEST) confirm Iran announces a new military offensive in the Strait of Hormuz between 2026-09-21 and 2026-09-24, as reported in corroborating sources.
- **Failure condition:** No report from at least two hostile sides (AXIS, WEST) confirms Iran announces a new military offensive in the Strait of Hormuz between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-08
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** The 10-year U.S. Treasury yield exceeds 5.0% on at least one trading day between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 5.0% on at least one trading day between 2026-09-21 and 2026-09-24, as recorded in the Market Snapshot data.
- **Failure condition:** The 10-year U.S. Treasury yield remains at or below 5.0% on all trading days between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261011T184607ZZ - sha256 4dcf56a3652624c8...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.00; 2 day(s) satisfying

### KKR-20260905-01
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-28, the S&P 500 index will close above 7,750.00 on at least one trading day.
- **Resolution criterion:** The S&P 500 closes at or above 7,750.00 on at least one trading day between 2026-09-21 and 2026-09-28, based on the official market close from a major exchange.
- **Failure condition:** The S&P 500 never closes at or above 7,750.00 on any trading day between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-02
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-28, at least one new vulnerability in the PostgreSQL database system will be publicly disclosed and listed in the CISA KEV catalog.
- **Resolution criterion:** The CISA KEV catalog includes at least one new vulnerability affecting PostgreSQL, with a date-added value between 2026-09-21 and 2026-09-28.
- **Failure condition:** No new PostgreSQL vulnerability is listed in the CISA KEV catalog with a date-added value between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184610ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['PostgreSQL'] with dateAdded in [2026-09-21..2026-09-28] across 1739 catalog rows

### KKR-20260905-03
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-28, the US dollar will trade above 1.17 against the euro on at least one trading day.
- **Resolution criterion:** The EUR/USD exchange rate exceeds 1.17 on at least one trading day between 2026-09-21 and 2026-09-28, based on the official market close from a major exchange.
- **Failure condition:** The EUR/USD exchange rate never exceeds 1.17 on any trading day between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-04
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-28, a new earthquake of magnitude 6.0 or greater will be recorded by the USGS in the Pacific Ring of Fire region.
- **Resolution criterion:** The USGS Significant Quakes database records at least one earthquake with magnitude 6.0 or greater in the Pacific Ring of Fire region between 2026-09-21 and 2026-09-28.
- **Failure condition:** No earthquake of magnitude 6.0 or greater is recorded in the USGS Significant Quakes database in the Pacific Ring of Fire region between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-05
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-28, at least one new forest fire in Africa will be reported by GDACS Alerts with a green or yellow alert level.
- **Resolution criterion:** GDACS Alerts reports at least one new forest fire in Africa with a green or yellow alert level between 2026-09-21 and 2026-09-28.
- **Failure condition:** No new forest fire in Africa is reported by GDACS Alerts with a green or yellow alert level between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-06
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-28, a major cyberattack exploiting the Citrix NetScaler auth bypass vulnerability will be confirmed by two or more independent sources.
- **Resolution criterion:** At least two independently biased sources (e.g., western, iranian, pro-ukraine, pro-russia) confirm a cyberattack exploiting the Citrix NetScaler auth bypass vulnerability (CVE-2026-XXXX) between 2026-09-21 and 2026-09-28.
- **Failure condition:** No cyberattack exploiting the Citrix NetScaler auth bypass vulnerability is confirmed by two or more independently biased sources between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-07
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-28, the US will launch a new military operation in the Middle East targeting Iranian proxies, confirmed by at least two independent outlets.
- **Resolution criterion:** At least two independently biased outlets (e.g., western, iranian, pro-ukraine, pro-russia) confirm a new US military operation in the Middle East targeting Iranian proxies between 2026-09-21 and 2026-09-28.
- **Failure condition:** No new US military operation targeting Iranian proxies in the Middle East is confirmed by two or more independently biased outlets between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260905-08
- **Issued:** 2026-09-05  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-28, a new political scandal involving a US government official will be reported by two or more major news outlets with differing political leanings.
- **Resolution criterion:** At least two major news outlets with differing political leanings (e.g., BBC World, Guardian World, CNBC Top News, Al Jazeera) report a new political scandal involving a US government official between 2026-09-21 and 2026-09-28.
- **Failure condition:** No new political scandal involving a US government official is reported by two or more major news outlets with differing political leanings between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-76
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** Between 2026-09-07 and 2026-09-30 inclusive, UKMTO publishes at least one advisory reporting an attack on, boarding of, or seizure of a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf.
- **Resolution criterion:** True if the UKMTO advisories archive contains at least one advisory dated 2026-09-07 through 2026-09-30 describing an attack, boarding, or seizure of a merchant vessel in the Strait of Hormuz, Gulf of Oman, or Persian Gulf.
- **Failure condition:** No attack, boarding, or seizure of a merchant vessel occurs in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-09-07 and 2026-09-30, as adjudicated by the UKMTO advisories archive.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-87
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** The official final result certified by the Landeswahlleiter of Saxony-Anhalt for the 2026-09-06 state election, certified between 2026-09-07 and 2026-09-30, allocates AfD at least 42 of the 83 Landtag seats.
- **Resolution criterion:** TRUE if the amtliches Endergebnis published by the Landeswahlleiter Sachsen-Anhalt between 2026-09-07 and 2026-09-30 shows AfD holding 42 or more of 83 seats. Reference: 41 of 83 in the election-night projection.
- **Failure condition:** The certified final seat allocation gives AfD 41 or fewer of the 83 seats, leaving it short of an absolute majority.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-20
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** NYMEX WTI front-month crude settles at or above 100.00 USD per barrel on 2026-10-02. Reference: 91.48 on the packet date 2026-09-07.
- **Resolution criterion:** CME Group official settlement price of the front-month NYMEX WTI (CL) contract for trade date 2026-10-02 is at or above 100.00 USD. Reference: 91.48 on the packet date 2026-09-07. Any settlement below 100.00 resolves false.
- **Failure condition:** The front-month WTI settlement for trade date 2026-10-02 is below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-56
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-05
- **Domain:** military_conflict
- **Claim:** Saudi Arabia conducts acknowledged military strikes on Houthi-controlled territory in Yemen between 2026-09-09 and 2026-09-30.
- **Resolution criterion:** TRUE if two of Reuters, AP, AFP, BBC and Al Jazeera report Saudi strikes inside Houthi-held Yemen occurring in the window, with Saudi or Houthi attribution.
- **Failure condition:** No Saudi strike inside Houthi-held Yemen occurs within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-03
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a ransomware attack exploiting CVE-2026-20079 will be confirmed by CISA.
- **Resolution criterion:** CISA issues a public advisory confirming a ransomware attack exploiting CVE-2026-20079 between 2026-09-21 and 2026-09-24.
- **Failure condition:** CISA does not issue a public advisory confirming a ransomware attack exploiting CVE-2026-20079 between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-28
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** The CME NYMEX WTI crude oil November 2026 futures contract (CLX26) settles at or above 110.00 USD per barrel on 2026-10-02. Reference: 100.05 front-month WTI on the packet date.
- **Resolution criterion:** TRUE if the official CME Group settlement price for CLX26 on 2026-10-02 is 110.00 or higher; FALSE if below 110.00. Reference: 100.05 front-month WTI on the packet date.
- **Failure condition:** CLX26 settles below 110.00 USD per barrel on 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-06
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-30 and 2026-10-03, a major data breach at Revolut exposes financial information and passport details of at least 500,000 users, as confirmed by a CISA KEV entry and a press release from Revolut.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-30 and 2026-10-03, and Revolut issues a public press release confirming the exposure of financial information and passport details of at least 500,000 users.
- **Failure condition:** No CISA KEV entry is published between 2026-09-30 and 2026-10-03 linking to a confirmed breach of Revolut with 500,000 or more users affected.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184613ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Revolut'] with dateAdded in [2026-09-30..2026-10-03] across 1739 catalog rows

### KKR-20260916-02
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-16 and 2026-09-23, a green forest fire notification will be issued for Spain via GDACS Alerts.
- **Resolution criterion:** GDACS Alerts issues a green forest fire notification for Spain between 2026-09-16 and 2026-09-23.
- **Failure condition:** No green forest fire notification for Spain is issued by GDACS Alerts between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-03
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** Between 2026-09-16 and 2026-09-23, the US House of Representatives will vote to end the Iran war for a third time.
- **Resolution criterion:** The US House of Representatives votes to end the Iran war for a third time between 2026-09-16 and 2026-09-23.
- **Failure condition:** The US House of Representatives does not vote to end the Iran war for a third time between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-04
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** economics/markets
- **Claim:** Between 2026-09-16 and 2026-09-23, the EUR/USD exchange rate will close above 1.1600 on at least one trading day.
- **Resolution criterion:** The EUR/USD exchange rate closes above 1.1600 on at least one trading day between 2026-09-16 and 2026-09-23.
- **Failure condition:** The EUR/USD exchange rate closes at or below 1.1600 on every trading day between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-05
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-16 and 2026-09-23, a critical ScreenConnect vulnerability (CVE-2026-XXXXX) will be actively exploited in attacks, as confirmed by at least two independent sources.
- **Resolution criterion:** At least two independent sources confirm that a critical ScreenConnect vulnerability (CVE-2026-XXXXX) is actively exploited in attacks between 2026-09-16 and 2026-09-23.
- **Failure condition:** No independent source confirms active exploitation of a critical ScreenConnect vulnerability between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-06
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** Between 2026-09-16 and 2026-09-23, the US Senate will pass a resolution to ban social media use for users under 13 in the European Union.
- **Resolution criterion:** The US Senate passes a resolution to ban social media use for users under 13 in the European Union between 2026-09-16 and 2026-09-23.
- **Failure condition:** The US Senate does not pass a resolution to ban social media use for users under 13 in the European Union between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-07
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-16 and 2026-09-23, a building collapse in Gaza City will result in at least 15 fatalities, as confirmed by at least two corroborating reports.
- **Resolution criterion:** At least two corroborating reports confirm that a building collapse in Gaza City results in at least 15 fatalities between 2026-09-16 and 2026-09-23.
- **Failure condition:** No corroborating reports confirm a building collapse in Gaza City resulting in at least 15 fatalities between 2026-09-16 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-64
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-17 and 2026-10-01, an aftershock of magnitude 5.0 or greater occurs within 200 km of the M6.5 earthquake 165 km west of Nikolski, Alaska (USGS event us7000ti1p), per the USGS Earthquake Catalog.
- **Resolution criterion:** TRUE if the USGS Earthquake Catalog records an M5.0-or-greater event within 200 km of the Nikolski mainshock, dated 2026-09-17 to 2026-10-01; adjudicated 2026-10-05. FALSE otherwise.
- **Failure condition:** The USGS Earthquake Catalog records no M5.0-or-greater event within 200 km of the Nikolski mainshock by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-02
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a magnitude 6.0 or higher earthquake will be recorded by the USGS in the Pacific Northwest.
- **Resolution criterion:** The USGS Significant Quakes database records a magnitude 6.0 or higher earthquake in the Pacific Northwest between 2026-09-21 and 2026-09-24.
- **Failure condition:** No magnitude 6.0 or higher earthquake is recorded in the Pacific Northwest by the USGS during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184613ZZ - sha256 e41b6f9c4ac48339...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-21&endtime=2026-09-24&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260918-03
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a cyberattack exploiting CVE-2025-39964 will be reported by at least two independent sources (e.g., BleepingComputer, The Hacker News).
- **Resolution criterion:** At least two independent sources (e.g., BleepingComputer, The Hacker News) report a cyberattack exploiting CVE-2025-39964 between 2026-09-21 and 2026-09-24.
- **Failure condition:** No report from two independent sources confirms a cyberattack exploiting CVE-2025-39964 during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-04
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** crime/security
- **Claim:** Between 2026-09-21 and 2026-09-24, a school shooting in the Philippines resulting in at least three fatalities will be confirmed by two independent sources (e.g., Al Jazeera, BBC World).
- **Resolution criterion:** Two independent sources (e.g., Al Jazeera, BBC World) confirm a school shooting in the Philippines between 2026-09-21 and 2026-09-24 resulting in at least three fatalities.
- **Failure condition:** No school shooting in the Philippines with at least three fatalities is confirmed by two independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-05
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new statement by Iran's IRGC regarding a blockade in the Strait of Hormuz will be confirmed by at least two independently biased sources (AXIS and WEST).
- **Resolution criterion:** At least two independently biased sources (one from AXIS, one from WEST) confirm a new statement by Iran's IRGC regarding a blockade in the Strait of Hormuz between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such statement is confirmed by both AXIS and WEST sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-06
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a major forest fire in South Africa will be reported by GDACS Alerts with a green alert level.
- **Resolution criterion:** GDACS Alerts reports a green forest fire notification in South Africa between 2026-09-21 and 2026-09-24.
- **Failure condition:** No green forest fire notification in South Africa is reported by GDACS Alerts during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-07
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a new vulnerability in Microsoft 365 will be exploited in a supply-chain attack, confirmed by BleepingComputer and The Hacker News.
- **Resolution criterion:** BleepingComputer and The Hacker News confirm a supply-chain attack exploiting a new vulnerability in Microsoft 365 between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such supply-chain attack exploiting a new Microsoft 365 vulnerability is confirmed by both BleepingComputer and The Hacker News during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-31
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-05
- **Domain:** political
- **Claim:** United Russia receives 50.00 percent or more of the federal party-list vote in the State Duma election held 2026-09-18 to 2026-09-20, per final results certified by the Russian Central Election Commission between 2026-09-21 and 2026-10-02.
- **Resolution criterion:** TRUE if final results certified by the Russian Central Election Commission between 2026-09-21 and 2026-10-02 give United Russia 50.00 percent or more of the federal party-list vote.
- **Failure condition:** The certified United Russia share of the federal party-list vote is below 50.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-09
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-20 and 2026-09-26, at least one new exploit for CVE-2026-53266 will be publicly disclosed.
- **Resolution criterion:** At least one public exploit for CVE-2026-53266 is disclosed in a credible source by 2026-09-26.
- **Failure condition:** No public exploit for CVE-2026-53266 is disclosed in a credible source by 2026-09-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-10
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-27, a new vulnerability in the Linux kernel will be publicly disclosed and listed in the CISA KEV catalog.
- **Resolution criterion:** A new Linux kernel vulnerability is publicly disclosed and listed in the CISA KEV catalog between 2026-09-21 and 2026-09-27.
- **Failure condition:** No new Linux kernel vulnerability is publicly disclosed and listed in the CISA KEV catalog between 2026-09-21 and 2026-09-27.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184615ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Linux'] with dateAdded in [2026-09-21..2026-09-27] across 1739 catalog rows

### KKR-20260921-12
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-27 and 2026-10-01, a cyberattack targeting a U.S. federal agency will be confirmed by two or more independent sources (one from a Western outlet, one from a non-Western outlet), with the attack involving a PowerShell backdoor.
- **Resolution criterion:** Two or more independent sources (one from a Western outlet, one from a non-Western outlet) confirm a cyberattack on a U.S. federal agency involving a PowerShell backdoor between 2026-09-27 and 2026-10-01.
- **Failure condition:** No such attack involving a PowerShell backdoor on a U.S. federal agency is confirmed by two or more independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-45
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Typhoon Dujuan causes 10 or more confirmed deaths in Japan between 2026-09-21 and 2026-09-30.
- **Resolution criterion:** Japan Fire and Disaster Management Agency or NHK reports a cumulative Dujuan death toll in Japan of 10 or more for deaths occurring 2026-09-21 through 2026-09-30.
- **Failure condition:** The confirmed Japan death toll attributed to Dujuan for the window is 9 or fewer.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-01
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-09-28, at least one report from a hostile side confirms a drone strike on Kyiv with casualties reported.
- **Resolution criterion:** At least one report from a hostile side (RU or UA) confirms a drone strike on Kyiv during the window with casualties stated in the corroborating report.
- **Failure condition:** No report from a hostile side confirms a drone strike on Kyiv during the window with casualties stated.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-03
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** Between 2026-09-22 and 2026-09-28, the USGS reports a significant earthquake (M ≥ 6.0) in the Pacific Northwest.
- **Resolution criterion:** The USGS Significant Quakes feed reports an earthquake with magnitude ≥ 6.0 in the Pacific Northwest region during the window.
- **Failure condition:** The USGS Significant Quakes feed does not report an earthquake with magnitude ≥ 6.0 in the Pacific Northwest during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-05
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-05
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-09-28, the Houthis launch a coordinated attack on a Red Sea port in Yemen resulting in at least one casualty.
- **Resolution criterion:** At least one report from a hostile side confirms a coordinated attack by the Houthis on a Red Sea port in Yemen during the window with at least one casualty stated.
- **Failure condition:** No report from a hostile side confirms a coordinated attack by the Houthis on a Red Sea port in Yemen during the window with at least one casualty stated.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-07
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-05
- **Domain:** cyber
- **Claim:** Between 2026-09-22 and 2026-09-28, a new vulnerability with CVSS score 10.0 is added to the CISA KEV catalog.
- **Resolution criterion:** The CISA KEV catalog includes a new vulnerability with a CVSS score of 10.0 during the window.
- **Failure condition:** The CISA KEV catalog does not include a new vulnerability with a CVSS score of 10.0 during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-49
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-05
- **Domain:** disaster_infrastructure
- **Claim:** Between 2026-09-25 and 2026-10-02, the National Weather Service issues a Coastal Flood Warning, High Wind Warning, or Storm Warning for a New York City or Boston metro forecast zone.
- **Resolution criterion:** The NWS public alerts archive shows at least one such warning issued for an NYC or Boston metro zone inside the window; no such warning issued is a MISS.
- **Failure condition:** No NWS Coastal Flood Warning, High Wind Warning, or Storm Warning is issued for an NYC or Boston metro zone between 2026-09-25 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-06
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-05
- **Domain:** disaster
- **Claim:** The Central Pacific Hurricane Center issues a Hurricane Warning (not merely a Watch) covering any part of Hawaii County for tropical cyclone Nolo in a public advisory dated between 2026-09-24 and 2026-10-01.
- **Resolution criterion:** TRUE if any NHC or CPHC public advisory for Nolo dated 2026-09-24 through 2026-10-01 (NHC text archive) lists a Hurricane Warning in effect for Hawaii County or any of its zones; otherwise FALSE.
- **Failure condition:** No NHC or CPHC public advisory for Nolo dated 2026-09-24 through 2026-10-01 carries a Hurricane Warning for any part of Hawaii County, a Tropical Storm Warning or continued Hurricane Watch alone being insufficient.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-12
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-05
- **Domain:** crime/security
- **Claim:** The State of Tennessee carries out the execution of Christa Pike on 2026-09-30 as scheduled.
- **Resolution criterion:** TRUE if the Tennessee Department of Correction confirms Christa Pike was executed on 2026-09-30 and the Death Penalty Information Center execution database records that date; a stay, reprieve, or commutation resolves FALSE.
- **Failure condition:** Christa Pike is alive at the deadline or was executed on any date other than 2026-09-30, whether by stay, clemency, reprieve, or rescheduling.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-28
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-05
- **Domain:** crime/security
- **Claim:** The State of Tennessee carries out the scheduled execution of Christa Pike between 2026-09-30 and 2026-10-02.
- **Resolution criterion:** TRUE if the Tennessee Department of Correction, or AP or Reuters citing it, confirms Pike was executed on a date between 2026-09-30 and 2026-10-02; FALSE on clemency, stay, reprieve, or postponement past 2026-10-02.
- **Failure condition:** Christa Pike is alive at the end of 2026-10-02 because of clemency, a court stay, a reprieve, or a rescheduled date.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260808-11
- **Issued:** 2026-08-08  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** The incumbent governor of Rhode Island is defeated in a gubernatorial primary held between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** Rhode Island Department of State results show the sitting governor losing a September 2026 gubernatorial primary; if the incumbent wins, is unopposed, is not a candidate, or no primary occurs, false.
- **Failure condition:** The incumbent wins or faces no September 2026 primary contest, including by not seeking reelection.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-28
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** Between 2026-08-23 and 2026-10-02 the governments of the United States and Iran both publicly confirm an agreement (ceasefire or settlement) whose announced terms include reopening the Strait of Hormuz to commercial shipping.
- **Resolution criterion:** Statements from both the US government and the government of Iran, dated 2026-08-23 to 2026-10-02, confirm one agreement whose published terms include reopening Hormuz to commercial shipping; confirmed by Reuters and AP.
- **Failure condition:** No agreement confirmed by both governments and providing for reopening of the Strait of Hormuz is announced between 2026-08-23 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-69
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** At least one civil complaint naming Carhartt Inc as defendant over the 2026 customer data breach is filed in a US federal district court between 2026-08-27 and 2026-10-02.
- **Resolution criterion:** PACER or CourtListener shows a complaint filed between 2026-08-27 and 2026-10-02 in any US federal district court that names Carhartt Inc as defendant and alleges harm from the 2026 data breach of about 12.9 million accounts.
- **Failure condition:** No complaint against Carhartt Inc arising from the breach appears on any federal docket with a filing date inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-77
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-06
- **Domain:** military_conflict
- **Claim:** Russian military forces conduct a strike, using missile, drone, or other kinetic means, that lands on the sovereign territory of a NATO member state, including the UK, between 2026-09-03 and 2026-10-03.
- **Resolution criterion:** At least two independently owned news organizations, or a NATO member government and NATO itself, confirm a Russian-origin strike landed on NATO member territory within the window, checked by 2026-10-06.
- **Failure condition:** No confirmed Russian-origin strike lands on NATO member territory within the window; verbal warnings, sabotage allegations short of a kinetic strike, or strikes confined to Ukrainian territory all count as a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-12
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a tropical storm makes landfall in Texas with a storm surge warning issued by the National Weather Service.
- **Resolution criterion:** The National Weather Service issues a storm surge warning for a tropical storm making landfall in Texas between 2026-09-21 and 2026-09-24.
- **Failure condition:** No storm surge warning is issued by the National Weather Service for a tropical storm making landfall in Texas between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-02
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** economics/markets
- **Claim:** The EIA daily WTI Cushing spot price (FRED series DCOILWTICO) is at or above 100.00 dollars per barrel on at least one observation date between 2026-09-03 and 2026-10-02. Reference: WTI 90.59 on the packet date 2026-09-02.
- **Resolution criterion:** TRUE if the FRED series DCOILWTICO (EIA Cushing WTI spot, daily) shows a value of 100.00 or higher for any observation date from 2026-09-03 through 2026-10-02 inclusive.
- **Failure condition:** Every DCOILWTICO observation from 2026-09-03 through 2026-10-02 is below 100.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-05
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** A lapse in US federal appropriations begins on 2026-10-01: no law providing FY2027 appropriations, full-year or continuing, for every federal department is enacted by the end of 2026-09-30, and OMB or at least one department issues lapse or shutdown guidance effective 2026-10-01.
- **Resolution criterion:** TRUE if Congress.gov shows no enacted law providing FY2027 appropriations, full-year or continuing, for every federal department by 2026-09-30, and OMB or at least one department publishes lapse or shutdown guidance effective 2026-10-01.
- **Failure condition:** A law providing FY2027 appropriations, full-year or continuing, for every federal department is enacted on or before 2026-09-30, so no department begins a lapse on 2026-10-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-16
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the Netherlands will publicly confirm the transfer of at least $5 billion in gold from the United States to Canada or the United Kingdom.
- **Resolution criterion:** The Netherlands publicly confirms the transfer of at least $5 billion in gold from the United States to Canada or the United Kingdom between 2026-09-21 and 2026-09-24.
- **Failure condition:** The Netherlands does not publicly confirm the transfer of at least $5 billion in gold from the U.S. to Canada or the U.K. during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-33
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** The US Department of Defense announces the death of at least one US service member from hostile action in the CENTCOM area of responsibility, with a date of death between 2026-09-04 and 2026-10-01.
- **Resolution criterion:** A casualty release on defense.gov identifies at least one US service member whose death is attributed to hostile action or enemy attack in the CENTCOM area of responsibility, with date of death 2026-09-04 through 2026-10-01 inclusive.
- **Failure condition:** No DoD casualty release attributes any US service member death in the CENTCOM area of responsibility to hostile action with a date of death between 2026-09-04 and 2026-10-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-37
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** Between 2026-09-04 and 2026-10-02, Ukrainian forces strike at least one target inside internationally recognized Russian territory 200 km or more from the Russia-Ukraine border, acknowledged by both a Russian official source and a Ukrainian official or military-intelligence source.
- **Resolution criterion:** Resolves TRUE if a strike meeting the statement, occurring in the window, is acknowledged by at least one Russian official source (MoD or regional governor) and one Ukrainian official source; otherwise FALSE.
- **Failure condition:** No strike 200 km or deeper inside Russia occurring within the window is acknowledged by both a Russian official source and a Ukrainian official source by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-42
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry whose vendor, product, or vulnerability name field contains Elementor, with a dateAdded value between 2026-09-03 and 2026-10-02 inclusive.
- **Resolution criterion:** Resolves TRUE if the public CISA KEV JSON feed contains an entry naming Elementor with a dateAdded value between 2026-09-03 and 2026-10-02 inclusive; otherwise FALSE.
- **Failure condition:** No KEV entry naming Elementor carries a dateAdded value within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-28
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** Houthi forces take control of the Yemeni port city of Mokha (al-Mukha), Taiz governorate, between 2026-09-04 and 2026-10-02.
- **Resolution criterion:** Either the internationally recognized Yemeni government acknowledges loss of Mokha, or at least two of Reuters, AP and AFP report Houthi forces control the city center and port, for an event dated within the window.
- **Failure condition:** Government-aligned forces retain control of Mokha city and port on every day from 2026-09-04 through 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-35
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** The USGS ComCat catalog records at least one earthquake of magnitude 5.0 or greater within 150 km of the 2026-09-04 M6.3 epicenter near Nikolski, Alaska, with origin time between 2026-09-05 and 2026-10-02.
- **Resolution criterion:** TRUE if a ComCat query centered on the M6.3 event coordinates, radius 150 km, minimum magnitude 5.0, returns at least one event with origin time inside the window.
- **Failure condition:** The specified ComCat query returns zero events of magnitude 5.0 or greater with origin time between 2026-09-05 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-16
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry for the Citrix NetScaler ADC or NetScaler Gateway authentication bypass with a dateAdded value between 2026-09-05 and 2026-10-02.
- **Resolution criterion:** The public CISA KEV catalog contains an entry naming Citrix NetScaler ADC or NetScaler Gateway with an authentication bypass description and dateAdded between 2026-09-05 and 2026-10-02.
- **Failure condition:** The CISA KEV catalog contains no Citrix NetScaler authentication bypass entry with dateAdded between 2026-09-05 and 2026-10-02.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184619ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Citrix NetScaler ADC', 'NetScaler Gateway'] with dateAdded in [2026-09-05..2026-10-02] across 1739 catalog rows

### KKR-20260906-55
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** Between 2026-09-22 and 2026-09-29, a cyberattack exploiting an unpatched vulnerability in a critical infrastructure system is confirmed by CISA KEV catalog with a date-added value in that window.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-22 and 2026-09-29 for a vulnerability exploited in a critical infrastructure system.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-09-22 and 2026-09-29 for a vulnerability exploited in a critical infrastructure system.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-79
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** Between 2026-09-07 and 2026-10-02 inclusive, CISA adds to its Known Exploited Vulnerabilities catalog at least one CVE whose product is Adobe Commerce or Magento Open Source, with a dateAdded value in that range.
- **Resolution criterion:** True if the CISA KEV JSON feed contains an entry with vendorProject Adobe or Magento, product Commerce, Adobe Commerce, or Magento, and dateAdded between 2026-09-07 and 2026-10-02 inclusive.
- **Failure condition:** No CISA KEV entry for an Adobe Commerce or Magento vulnerability carries a dateAdded between 2026-09-07 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-26
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** The Iraqi government or the US Department of Defense announces, between 2026-09-08 and 2026-10-02, that US military forces will remain stationed at bases in Iraq, including the Kurdistan Region, beyond 2026-09-30.
- **Resolution criterion:** An official statement from the Iraqi PM office, Iraqi Armed Forces spokesperson, CENTCOM, CJTF-OIR, or US DoD, dated 2026-09-08 to 2026-10-02, announces US forces remaining at Iraqi bases past 2026-09-30. Embassy security and security-cooperation staff excluded.
- **Failure condition:** US forces complete their withdrawal, or no continuation of US basing in Iraq past 2026-09-30 is announced by either government by 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-01
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-29, the CISA KEV catalog includes at least one new vulnerability with a CVSS score of 10.0 or higher.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-23 and 2026-09-29 for a vulnerability with a CVSS score of 10.0 or higher.
- **Failure condition:** No new vulnerability with CVSS 10.0 or higher is added to the CISA KEV catalog between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-25
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** Between 2026-09-10 and 2026-10-02, German Chancellor Friedrich Merz and US President Donald Trump hold a phone call or in-person bilateral meeting, as confirmed by an official German or US government readout.
- **Resolution criterion:** The German federal government (bundesregierung.de or the government spokesperson) or the White House publishes a readout or statement confirming a Merz-Trump call or bilateral meeting held between 2026-09-10 and 2026-10-02.
- **Failure condition:** No Merz-Trump call or bilateral meeting held between 2026-09-10 and 2026-10-02 is confirmed by either government.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-04
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-06
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield will exceed 4.92% at market close.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 4.92% on the close of any trading day between 2026-09-21 and 2026-09-24.
- **Failure condition:** The 10-year U.S. Treasury yield does not exceed 4.92% on any trading day between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261011T184623ZZ - sha256 4dcf56a3652624c8...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 4.92; 4 day(s) satisfying

### KKR-20260913-08
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-06
- **Domain:** military_conflict
- **Claim:** Between 2026-09-20 and 2026-10-04, at least one additional commercial or military vessel will be struck, hit, or attacked while transiting the Strait of Hormuz.
- **Resolution criterion:** UKMTO issues an advisory, or two independent wire services such as Reuters, AP, or AFP report, that a vessel was struck, hit, or attacked while transiting the Strait of Hormuz between 2026-09-20 and 2026-10-04.
- **Failure condition:** No commercial or military vessel is struck, hit, or attacked while transiting the Strait of Hormuz at any point during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-37
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** The Swedish Election Authority certifies the 2026 Riksdag result between 2026-09-15 and 2026-10-02 with the Social Democrats, Left Party, Greens, and Centre Party holding a combined 175 or more of 349 seats.
- **Resolution criterion:** Valmyndigheten final certified seat allocation, published between 2026-09-15 and 2026-10-02, gives the Social Democrats, Left, Greens, and Centre combined at least 175 of 349 seats.
- **Failure condition:** The certified allocation gives the four listed parties 174 or fewer combined seats, or no certified result is published by 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-37
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** Between 2026-09-17 and 2026-10-02, an official Sudanese source reports a death toll of at least 100 from the West Kordofan gold mine collapse reported on 2026-09-16.
- **Resolution criterion:** True if Reuters, AFP, or Al Jazeera reports in the window a death toll of at least 100 for that collapse, attributed to the Sudanese Mineral Resources Company, a state government, or a Sudanese health authority.
- **Failure condition:** Through 2026-10-02 the highest official toll reported for the collapse by Reuters, AFP, or Al Jazeera remains below 100.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-50
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** USGS records at least one aftershock of magnitude 5.0 or greater within 300 km of the M6.5 earthquake 169 km west of Nikolski, Alaska, event us7000ti1p, between 2026-09-18 and 2026-10-02.
- **Resolution criterion:** TRUE if the USGS earthquake catalog lists a magnitude 5.0-plus event within 300 km of event us7000ti1p between 2026-09-18 and 2026-10-02; checked 2026-10-06 via earthquake.usgs.gov.
- **Failure condition:** No magnitude 5.0-plus earthquake within 300 km of event us7000ti1p is recorded by USGS between 2026-09-18 and 2026-10-02.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184623ZZ - sha256 a490c0788fe3ae45...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-02&endtime=2026-10-06&latitude=32.69&longitude=130.66&maxradiuskm=300&minmagnitude=5.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260918-51
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** GDACS raises its alert level above Green, to Orange or Red, for the Italy forest fire logged as event 1032034, already in its 59th day of coverage as of 2026-09-18, between 2026-09-18 and 2026-10-02.
- **Resolution criterion:** TRUE if the GDACS report page for event 1032034 shows an Orange or Red alert level at any point between 2026-09-18 and 2026-10-02; checked 2026-10-06 via gdacs.org.
- **Failure condition:** GDACS event 1032034 remains at Green alert level, or is closed at Green, throughout 2026-09-18 to 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-52
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-06
- **Domain:** crime/security
- **Claim:** Pakistani government, police, or military (ISPR) officials publicly name a specific militant organization as responsible for the September 18, 2026 blast at a police-complex mosque in Pakistan, between 2026-09-18 and 2026-10-02.
- **Resolution criterion:** TRUE if Reuters, AP, Al Jazeera, or Dawn quote a Pakistani official naming a specific militant group for the blast between 2026-09-18 and 2026-10-02; checked 2026-10-06.
- **Failure condition:** No Pakistani official is quoted naming a specific militant group as responsible for the blast by 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-21
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** United Russia wins at least 300 of 450 State Duma seats in the election held 2026-09-18 to 2026-09-20, per final results the Central Election Commission approves between 2026-09-21 and 2026-10-02.
- **Resolution criterion:** TRUE if final results approved by the Russian Central Election Commission (cikrf.ru) between 2026-09-21 and 2026-10-02 allocate United Russia 300 or more of 450 seats, list and single-mandate combined; otherwise FALSE.
- **Failure condition:** United Russia holds fewer than 300 seats in the CEC-approved final results, or no final allocation is approved between 2026-09-21 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-18
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** The CISA KEV catalog gains an entry with a date-added value between 2026-09-21 and 2026-10-02 for a vulnerability whose product field names an npm package, the npm CLI, or the Node.js runtime.
- **Resolution criterion:** True if the CISA KEV JSON feed contains an entry with dateAdded in the window and a product or vendor field matching npm or Node.js.
- **Failure condition:** No KEV entry dated in the window names npm, the npm CLI, or Node.js in its product or vendor field.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-13
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** Between 2026-09-30 and 2026-10-04, a major flood event in the U.S. Midwest will be confirmed by the National Weather Service, with at least one flood warning or watch issued for a county in Iowa or Ohio.
- **Resolution criterion:** The National Weather Service issues at least one flood warning or watch for a county in Iowa or Ohio between 2026-09-30 and 2026-10-04.
- **Failure condition:** No flood warning or watch is issued by the National Weather Service for any county in Iowa or Ohio between 2026-09-30 and 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-08
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-09-29, at least one report from a hostile side in the Iran Theatre will confirm a drone or missile strike on Tehran with casualties exceeding 5.
- **Resolution criterion:** At least one corroborated report from a hostile side (AXIS, IL, WEST) confirms a drone or missile strike on Tehran during the event window with casualties exceeding 5.
- **Failure condition:** No corroborated report from a hostile side confirms a drone or missile strike on Tehran during the event window with casualties exceeding 5.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-09
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** Between 2026-09-22 and 2026-09-29, at least one report from a hostile side in the Iran Theatre will confirm a cyberattack on a critical infrastructure system in the United States.
- **Resolution criterion:** At least one corroborated report from a hostile side (AXIS, WEST) confirms a cyberattack on a critical infrastructure system in the United States during the event window.
- **Failure condition:** No corroborated report from a hostile side confirms a cyberattack on a critical infrastructure system in the United States during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-04
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** Between 2026-09-26 and 2026-10-02, a new tropical cyclone will be designated as a Category 3 or higher storm by the National Hurricane Center.
- **Resolution criterion:** The National Hurricane Center designates a new tropical cyclone as Category 3 or higher between 2026-09-26 and 2026-10-02.
- **Failure condition:** The National Hurricane Center does not designate any new tropical cyclone as Category 3 or higher between 2026-09-26 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-06
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-10-06
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-10-02, a new military escalation in the Russia-Ukraine conflict will be confirmed by at least two hostile sides.
- **Resolution criterion:** At least two hostile sides confirm a new military escalation in the Russia-Ukraine conflict between 2026-09-26 and 2026-10-02.
- **Failure condition:** Fewer than two hostile sides confirm a new military escalation in the Russia-Ukraine conflict between 2026-09-26 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-44
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** Pakistani authorities will arrest or detain at least one PTI member or supporter in connection with the Islamabad march, between 2026-09-26 and 2026-10-04.
- **Resolution criterion:** Two independent outlets (e.g. Dawn, Reuters, Al Jazeera, AP) report the arrest or detention of at least one PTI member, supporter, or organizer tied to the Islamabad march, with an arrest date between 2026-09-26 and 2026-10-04.
- **Failure condition:** No two independent outlets report a PTI-affiliated arrest or detention tied to the Islamabad march within 2026-09-26 to 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-47
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-06
- **Domain:** political
- **Claim:** No candidate will win an outright majority in Brazil's first-round presidential election on 2026-10-04, forcing an October 25 runoff.
- **Resolution criterion:** True if Brazil's Tribunal Superior Eleitoral (TSE) results portal shows no candidate above 50 percent of valid votes and schedules the runoff; false if one candidate exceeds 50 percent.
- **Failure condition:** A single candidate is certified with more than 50 percent of valid first-round votes.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-20
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-06
- **Domain:** disaster
- **Claim:** Hurricane Polo makes landfall on the Baja California Peninsula between 2026-09-28 and 2026-10-04 with National Hurricane Center operational products stating maximum sustained winds of at least 111 mph at landfall.
- **Resolution criterion:** TRUE if an NHC Tropical Cyclone Update or Public Advisory issued between 2026-09-28 and 2026-10-04 reports the center of Polo crossing the Baja California Peninsula coast with maximum sustained winds of 111 mph or greater.
- **Failure condition:** NHC reports the Baja California Peninsula landfall of Polo with maximum sustained winds below 111 mph, or no landfall on the peninsula occurs inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-01
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-06
- **Domain:** cyber
- **Claim:** On 2026-09-30, the CISA KEV catalog will include CVE-2026-86950 with a date-added value of 2026-09-29.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value of 2026-09-29 for CVE-2026-86950.
- **Failure condition:** CVE-2026-86950 is not listed in the CISA KEV catalog with a date-added value of 2026-09-29.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184625ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-86950'] with dateAdded in [2026-09-29..2026-09-30] across 1739 catalog rows - CVE-2026-86950

### KKR-20260929-13
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-06
- **Domain:** crime/security
- **Claim:** The State of Tennessee carries out the scheduled execution of Christa Gail Pike on 2026-09-30, the date set by the Tennessee Supreme Court.
- **Resolution criterion:** TRUE if the Tennessee Department of Correction confirms Pike was executed on 2026-09-30 and the Death Penalty Information Center execution database records it; FALSE if stayed, delayed past that date, or commuted.
- **Failure condition:** The execution does not take place on 2026-09-30 for any reason, including a stay, reprieve, commutation, or rescheduling.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-28
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-06
- **Domain:** crime/security
- **Claim:** Tennessee carries out the execution of Christa Gail Pike on her scheduled execution date, 2026-09-30.
- **Resolution criterion:** True if the Tennessee Department of Correction or AP reports Christa Gail Pike was executed on 2026-09-30, Central Time. False if a stay, reprieve, commutation or halted procedure prevents execution that day.
- **Failure condition:** Christa Gail Pike is not executed on 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-46
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** A single Russian missile or drone strike will kill 10 or more people in Kyiv, Ukraine, between 2026-09-05 and 2026-10-05.
- **Resolution criterion:** TRUE if Ukrainian officials and at least one of Reuters, AP, or AFP report 10 or more deaths from one strike on Kyiv in the window; checked 2026-10-07; FALSE otherwise.
- **Failure condition:** No single strike on Kyiv in this window is confirmed by Ukrainian officials and a wire service to have killed 10 or more people.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-11
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, at least one report from a hostile side confirms a drone strike on Kyiv with casualties claimed by Ukrainian sources.
- **Resolution criterion:** At least one report from a hostile side (RU or UA) confirms a drone strike on Kyiv during the window, with casualties claimed in at least one corroborating report.
- **Failure condition:** No report from a hostile side confirms a drone strike on Kyiv during the window with casualties claimed in any corroborating report.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-13
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a cyberattack exploiting CVE-2026-81578 results in unauthorized access to a critical infrastructure system.
- **Resolution criterion:** A confirmed cyberattack exploiting CVE-2026-81578 results in unauthorized access to a critical infrastructure system, as reported by a public source.
- **Failure condition:** No confirmed cyberattack exploiting CVE-2026-81578 results in unauthorized access to a critical infrastructure system during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-15
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a major wildfire in France causes damage to a wine-producing region as confirmed by Al Jazeera.
- **Resolution criterion:** Al Jazeera publishes a report confirming a major wildfire in France that causes damage to a wine-producing region between 2026-09-21 and 2026-09-24.
- **Failure condition:** Al Jazeera does not publish a report confirming a major wildfire in France causing damage to a wine-producing region during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-37
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-09-28, at least one drone strike will be confirmed by two or more independently biased sources in the Kyiv region of Ukraine.
- **Resolution criterion:** At least one drone strike event in Kyiv, Ukraine, is confirmed by two or more sources from distinct hostile sides (RU, UA) with no single side carrying more than 60% of the volume.
- **Failure condition:** No drone strike in Kyiv is confirmed by two or more independently biased sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-17
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a magnitude 6.0 or higher earthquake will be recorded by the USGS in the South Sandwich Islands region.
- **Resolution criterion:** The USGS records a magnitude 6.0 or higher earthquake in the South Sandwich Islands region between 2026-09-21 and 2026-09-24.
- **Failure condition:** No magnitude 6.0 or higher earthquake is recorded by the USGS in the South Sandwich Islands region during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-21
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a magnitude 5.5 or higher earthquake will be recorded by the USGS in China.
- **Resolution criterion:** The USGS records a magnitude 5.5 or higher earthquake in China between 2026-09-21 and 2026-09-24.
- **Failure condition:** No magnitude 5.5 or higher earthquake is recorded by the USGS in China during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-34
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** The USGS catalog records an earthquake of magnitude 6.0 or greater with epicenter within 300 km of the 2026-09-03 M6.3 event 84 km SSW of Nikolski, Alaska (us7000tdvt), with origin time between 2026-09-04 and 2026-10-03.
- **Resolution criterion:** The USGS earthquake catalog (earthquake.usgs.gov) lists an event with magnitude 6.0 or greater, epicenter within 300 km of event us7000tdvt, and origin time from 2026-09-04 00:00 UTC through 2026-10-03 23:59 UTC.
- **Failure condition:** No USGS catalog event of magnitude 6.0 or greater with epicenter within 300 km of us7000tdvt has an origin time between 2026-09-04 and 2026-10-03.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184626ZZ - sha256 f6bfc551a894643a...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-04&endtime=2026-10-03&latitude=32.69&longitude=130.66&maxradiuskm=300&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260903-38
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-04 and 2026-10-04, the government or state news agency of Qatar (QNA) or Bahrain (BNA) confirms an Iranian missile or drone striking, or being intercepted over, its national territory.
- **Resolution criterion:** Resolves TRUE on official Qatari or Bahraini government or state-agency confirmation of an Iranian projectile striking or intercepted over its territory within the window, corroborated by at least one international wire service; otherwise FALSE.
- **Failure condition:** Neither Qatar nor Bahrain officially confirms any Iranian strike on or interception over its territory occurring within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-21
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Houthi forces will be reported to have gained physical control of coastal territory directly on the Bab el-Mandeb Strait, beyond their existing inland and Hodeida-area positions, with the advance occurring between 2026-09-05 and 2026-10-05.
- **Resolution criterion:** TRUE if two or more of Reuters, AP, AFP, or Al Jazeera report Houthi control of strait-front territory, not just Hodeida or inland areas, between 2026-09-05 and 2026-10-05; otherwise FALSE.
- **Failure condition:** Houthi forces remain confined to Hodeida and inland positions, without confirmed strait-front territory, through 2026-10-05.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-08
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-05 and 2026-10-03, the governments of Russia and Ukraine both publicly confirm a general ceasefire or cessation-of-hostilities agreement covering the entire front line.
- **Resolution criterion:** TRUE if, between 2026-09-05 and 2026-10-03, official statements from both the Kremlin and the Ukrainian presidency confirm a front-wide ceasefire agreement, reported by Reuters or AP. Partial truces (energy, Black Sea, humanitarian pauses) do not count.
- **Failure condition:** No front-wide ceasefire agreement is confirmed by both the Russian and Ukrainian governments between 2026-09-05 and 2026-10-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-21
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** USGS ComCat lists at least one earthquake of magnitude 6.0 or greater with epicenter between 50N and 55N latitude and 175W and 164W longitude, with origin time between 2026-09-06 and 2026-10-05 UTC.
- **Resolution criterion:** The public USGS ComCat catalog contains at least one M6.0 or greater event inside the stated latitude-longitude box with origin time between 2026-09-06 and 2026-10-05 UTC.
- **Failure condition:** USGS ComCat contains no M6.0 or greater event inside the stated box with origin time between 2026-09-06 and 2026-10-05 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-56
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-23 and 2026-09-30, a volcanic eruption in Indonesia causes flight cancellations at Jakarta International Airport, confirmed by at least two independent sources (one from BBC, one from Guardian).
- **Resolution criterion:** The GDACS Alerts system carries a report with eventtype=ER between 2026-09-23 and 2026-09-30 for a volcanic eruption in Indonesia causing flight cancellations at Jakarta International Airport, confirmed by at least two independent sources (one from BBC, one from Guardian).
- **Failure condition:** No GDACS report with eventtype=ER between 2026-09-23 and 2026-09-30 confirms a volcanic eruption in Indonesia causing flight cancellations at Jakarta International Airport, confirmed by at least two independent sources (one from BBC, one from Guardian).
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-81
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-07 and 2026-10-04 inclusive, the USGS earthquake catalog records at least one earthquake of magnitude 6.5 or greater with epicenter within 300 km of the 2026 M6.3 event 84 km SSW of Nikolski, Alaska (USGS event id us7000tdvt).
- **Resolution criterion:** True if a USGS ComCat search returns at least one event of magnitude 6.5 or greater with origin time between 2026-09-07 00:00 UTC and 2026-10-04 23:59 UTC located within 300 km of USGS event us7000tdvt.
- **Failure condition:** No earthquake of magnitude 6.5 or greater occurs within 300 km of USGS event us7000tdvt between 2026-09-07 and 2026-10-04, as adjudicated by the USGS catalog.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184626ZZ - sha256 72d2ae528992b366...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-07&endtime=2026-10-04&latitude=32.69&longitude=130.66&maxradiuskm=300&minmagnitude=6.5
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260908-01
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-07
- **Domain:** economics/markets
- **Claim:** Between 2026-09-22 and 2026-09-25, Brent crude oil exceeds $100 per barrel at the close of a trading day on a major exchange (e.g., ICE Futures Europe).
- **Resolution criterion:** The ICE Futures Europe settlement price for Brent crude oil futures on any trading day between 2026-09-22 and 2026-09-25 is equal to or greater than $100.00 per barrel.
- **Failure condition:** Brent crude oil never reaches or exceeds $100 per barrel at the close of any trading day in the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-05
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, the Houthis will seize control of the port city of Mocha in Yemen.
- **Resolution criterion:** At least two independent, hostile-side reports confirm the Houthis have seized control of Mocha port between 2026-09-21 and 2026-09-24.
- **Failure condition:** No two independent, hostile-side reports confirm the Houthis seized control of Mocha port between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-01
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-22 and 2026-09-29, the USGS Significant Quakes feed will report a magnitude 6.0 or higher earthquake in Indonesia with a depth of less than 100 km.
- **Resolution criterion:** The USGS Significant Quakes feed reports a magnitude 6.0 or higher earthquake in Indonesia with a depth of less than 100 km between 2026-09-22 and 2026-09-29.
- **Failure condition:** No magnitude 6.0 or higher earthquake with depth less than 100 km is reported in Indonesia between 2026-09-22 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-24
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-14 and 2026-10-04, a merchant vessel is struck by a projectile, hit by an uncrewed surface craft, boarded, or seized in the Red Sea, Bab al-Mandeb, or Gulf of Aden.
- **Resolution criterion:** TRUE if UKMTO publishes an incident dated 2026-09-14 to 2026-10-04 reporting a merchant vessel struck by a projectile, hit by an uncrewed craft, boarded, or seized in the Red Sea, Bab al-Mandeb, or Gulf of Aden; FALSE otherwise.
- **Failure condition:** No merchant vessel is struck, hit by an uncrewed craft, boarded, or seized in the Red Sea, Bab al-Mandeb, or Gulf of Aden between 2026-09-14 and 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-01
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, at least one drone strike will be reported in Gaza City by two or more independently biased sources across hostile sides.
- **Resolution criterion:** At least one drone strike in Gaza City is reported by two or more independently biased sources across hostile sides (AXIS, IL, PS) within the event window.
- **Failure condition:** No drone strike in Gaza City is reported by two or more independently biased sources across hostile sides during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-04
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a major flood warning will be issued by the US National Weather Service for at least one county in Iowa.
- **Resolution criterion:** The US National Weather Service issues a major flood warning for at least one county in Iowa between 2026-09-21 and 2026-09-24.
- **Failure condition:** No major flood warning is issued by the US National Weather Service for any county in Iowa during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-05
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, the US Supreme Court will issue a ruling rejecting a challenge to mail-in voting procedures.
- **Resolution criterion:** The US Supreme Court issues a ruling rejecting a challenge to mail-in voting procedures between 2026-09-21 and 2026-09-24.
- **Failure condition:** The US Supreme Court does not issue a ruling rejecting a challenge to mail-in voting procedures between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-07
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, Iran will announce a new diplomatic initiative involving China and the United States.
- **Resolution criterion:** Iran announces a new diplomatic initiative involving China and the United States between 2026-09-21 and 2026-09-24.
- **Failure condition:** Iran does not announce a new diplomatic initiative involving China and the United States between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-08
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-19 and 2026-09-25, a new ransomware variant exploiting the Acronis cPanel Backup Plugin vulnerability (CVE-2026-58704) is observed in at least 15 distinct organizations across Europe and North America, as confirmed by BleepingComputer and The Hacker News.
- **Resolution criterion:** BleepingComputer and The Hacker News publish reports between 2026-09-19 and 2026-09-25 confirming that a new ransomware variant exploiting the Acronis cPanel Backup Plugin vulnerability (CVE-2026-58704) has affected at least 15 distinct organizations in Europe and North America.
- **Failure condition:** No public report from BleepingComputer or The Hacker News confirms that a new ransomware variant exploiting CVE-2026-58704 affected at least 15 organizations in Europe and North America between 2026-09-19 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-10
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-27, a military escalation in the Russia-Ukraine Theatre will result in a confirmed drone strike on Kyiv with at least one casualty.
- **Resolution criterion:** At least one report from two hostile sides (RU, UA) will confirm a drone strike on Kyiv during the window, with at least one casualty reported in a corroborating source.
- **Failure condition:** No report from two hostile sides confirms a drone strike on Kyiv with at least one casualty between 2026-09-21 and 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-11
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-27, a natural disaster in the U.S. will trigger a federal emergency declaration by the President.
- **Resolution criterion:** The President of the United States will issue a federal emergency declaration for a natural disaster occurring in the U.S. between 2026-09-21 and 2026-09-27, as confirmed by a public statement from the White House.
- **Failure condition:** No federal emergency declaration is issued by the President for a natural disaster in the U.S. between 2026-09-21 and 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-13
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-27, a political scandal involving a U.S. federal official will result in a formal indictment by a grand jury.
- **Resolution criterion:** A U.S. federal grand jury will formally indict a sitting or former federal official for a crime related to official conduct, with the indictment publicly announced between 2026-09-21 and 2026-09-27.
- **Failure condition:** No formal indictment by a U.S. federal grand jury is announced for a federal official between 2026-09-21 and 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-14
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-10-04, the Russian Ministry of Defense or the Moscow mayor reports 100 or more Ukrainian UAVs intercepted over Moscow city or Moscow Oblast on a single calendar day.
- **Resolution criterion:** True if a Russian MoD or Moscow mayoral statement, carried by Reuters or AP, gives a single-day Moscow-region intercept count of 100 or more for any day 2026-09-21 to 2026-10-04.
- **Failure condition:** No single-day Moscow-region intercept figure of 100 or more is issued by Russian officials for any day in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-15
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-10-04, the Saudi Ministry of Defense announces the interception or impact of at least one Houthi-claimed drone or missile directed at Riyadh. Reference: Riyadh airport smoke and Houthi claim on 2026-09-19.
- **Resolution criterion:** True if Saudi Press Agency publishes a MoD statement on a drone or missile aimed at Riyadh in the window and Reuters or AP carries it.
- **Failure condition:** No Saudi MoD statement on a drone or missile directed at Riyadh appears for the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-30
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-07
- **Domain:** crime_security
- **Claim:** South Africa's NPA will file formal charges against at least one of the three men held in the murder case, between 2026-09-21 and 2026-10-05.
- **Resolution criterion:** True if the NPA or a South African court record, per Reuters/BBC, shows charges filed against at least one man in that window.
- **Failure condition:** No formal charges are filed against any of the three men within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-02
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-07
- **Domain:** economics/markets
- **Claim:** Between 2026-09-22 and 2026-09-28, the 10-year Treasury yield falls below 4.90 percent.
- **Resolution criterion:** The 10-year Treasury yield closes below 4.90 percent on the last trading day of the window.
- **Failure condition:** The 10-year Treasury yield closes at or above 4.90 percent on the last trading day of the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261011T184628ZZ - sha256 4dcf56a3652624c8...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 5 business days in window; min BC_10YEAR 4.96 on 2026-09-22; threshold < 4.90; 0 day(s) satisfying

### KKR-20260922-04
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-22 and 2026-09-28, Iran's delegation to the UN General Assembly delivers a statement asserting that the Strait of Hormuz is open and secure.
- **Resolution criterion:** Iran's delegation to the UN General Assembly delivers a statement during the window asserting that the Strait of Hormuz is open and secure.
- **Failure condition:** Iran's delegation does not deliver a statement during the window asserting that the Strait of Hormuz is open and secure.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-06
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-09-28, the US government announces a new military base in Greenland with a public statement from the White House.
- **Resolution criterion:** The White House issues a public statement during the window announcing the establishment of a new military base in Greenland.
- **Failure condition:** The White House does not issue a public statement during the window announcing the establishment of a new military base in Greenland.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-01
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-23 and 2026-09-24, at least one drone strike will be reported in Kyiv, Ukraine, with cross-bias corroboration from at least two hostile sides.
- **Resolution criterion:** At least one drone strike is reported in Kyiv, Ukraine, between 2026-09-23 and 2026-09-24, with corroborating reports from at least two hostile sides (RU, UA).
- **Failure condition:** No drone strike is reported in Kyiv, Ukraine, between 2026-09-23 and 2026-09-24 with corroborating reports from at least two hostile sides.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-02
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-23 and 2026-09-24, a confirmed earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific Northwest.
- **Resolution criterion:** The USGS records an earthquake of magnitude 6.0 or higher in the Pacific Northwest between 2026-09-23 and 2026-09-24.
- **Failure condition:** No earthquake of magnitude 6.0 or higher is recorded by the USGS in the Pacific Northwest between 2026-09-23 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184629ZZ - sha256 93749229c59fb72b...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-23&endtime=2026-09-24&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260923-03
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-94127 will be reported by at least two independent sources.
- **Resolution criterion:** A confirmed cyberattack exploiting CVE-2026-94127 is reported by at least two independent sources between 2026-09-23 and 2026-09-24.
- **Failure condition:** No confirmed cyberattack exploiting CVE-2026-94127 is reported by at least two independent sources between 2026-09-23 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-04
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** crime/security
- **Claim:** Between 2026-09-23 and 2026-09-24, a mass shooting resulting in four or more fatalities will be reported in South Africa with corroboration from at least two independent outlets.
- **Resolution criterion:** A mass shooting resulting in four or more fatalities is reported in South Africa between 2026-09-23 and 2026-09-24, with corroboration from at least two independent outlets.
- **Failure condition:** No mass shooting resulting in four or more fatalities is reported in South Africa between 2026-09-23 and 2026-09-24 with corroboration from at least two independent outlets.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-05
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-23 and 2026-09-24, a tropical cyclone named SURIGAE-26 will make landfall in Southeast Asia with a population of at least 1 million affected.
- **Resolution criterion:** A tropical cyclone named SURIGAE-26 makes landfall in Southeast Asia between 2026-09-23 and 2026-09-24, with a population of at least 1 million affected, as confirmed by GDACS.
- **Failure condition:** SURIGAE-26 does not make landfall in Southeast Asia between 2026-09-23 and 2026-09-24, or the affected population is less than 1 million.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-06
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-23 and 2026-09-24, the UN General Assembly will adopt a resolution calling for a ceasefire in the Israel-Gaza conflict, with support from at least three permanent members.
- **Resolution criterion:** The UN General Assembly adopts a resolution calling for a ceasefire in the Israel-Gaza conflict between 2026-09-23 and 2026-09-24, with support from at least three permanent members.
- **Failure condition:** No UN General Assembly resolution calling for a ceasefire in the Israel-Gaza conflict is adopted between 2026-09-23 and 2026-09-24, or it lacks support from at least three permanent members.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-07
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-24, a confirmed ransomware attack using the Ryuk variant will be reported by a major cybersecurity firm.
- **Resolution criterion:** A confirmed ransomware attack using the Ryuk variant is reported by a major cybersecurity firm between 2026-09-23 and 2026-09-24.
- **Failure condition:** No confirmed ransomware attack using the Ryuk variant is reported by a major cybersecurity firm between 2026-09-23 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-08
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-23 and 2026-09-29, at least one drone strike will be confirmed in Kyiv by two or more independently biased sources.
- **Resolution criterion:** At least one drone strike in Kyiv is confirmed by two or more independently biased sources between 2026-09-23 and 2026-09-29.
- **Failure condition:** No drone strike in Kyiv is confirmed by two or more independently biased sources between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-09
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-29, at least one cyberattack exploiting CVE-2026-94127 will be reported by a third-party security firm.
- **Resolution criterion:** A third-party security firm reports a cyberattack exploiting CVE-2026-94127 between 2026-09-23 and 2026-09-29.
- **Failure condition:** No third-party security firm reports a cyberattack exploiting CVE-2026-94127 between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-10
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-23 and 2026-09-29, a major flood warning will be issued by the USGS for a location in Iowa.
- **Resolution criterion:** The USGS issues a major flood warning for a location in Iowa between 2026-09-23 and 2026-09-29.
- **Failure condition:** The USGS does not issue a major flood warning for any location in Iowa between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-11
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-29, at least one major cyberattack will be attributed to Chinese state-linked actors by a U.S. government agency.
- **Resolution criterion:** A U.S. government agency attributes a major cyberattack to Chinese state-linked actors between 2026-09-23 and 2026-09-29.
- **Failure condition:** No U.S. government agency attributes a major cyberattack to Chinese state-linked actors between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-12
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Between 2026-09-23 and 2026-09-29, Iran will issue a public statement claiming a blockade of the Strait of Hormuz is underway.
- **Resolution criterion:** Iran issues a public statement claiming a blockade of the Strait of Hormuz is underway between 2026-09-23 and 2026-09-29.
- **Failure condition:** Iran does not issue a public statement claiming a blockade of the Strait of Hormuz is underway between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-01
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-07
- **Domain:** cyber
- **Claim:** On 2026-10-05, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in a critical infrastructure attack between 2026-09-24 and 2026-10-04.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-24 and 2026-10-04 for a vulnerability that was actively exploited in a confirmed attack on a critical infrastructure system.
- **Failure condition:** No entry in the CISA KEV catalog has a date-added value within the event window and is linked to a confirmed exploitation in a critical infrastructure attack.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-01
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-07
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-10-03, at least one Grade A or Grade B kinetic event will be reported in the Russia-Ukraine Theatre involving a missile strike on Kyiv.
- **Resolution criterion:** At least one Grade A or Grade B kinetic event involving a missile strike on Kyiv will be reported in the Russia-Ukraine Theatre between 2026-09-26 and 2026-10-03.
- **Failure condition:** No Grade A or Grade B kinetic event involving a missile strike on Kyiv is reported in the Russia-Ukraine Theatre between 2026-09-26 and 2026-10-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-03
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-07
- **Domain:** disaster
- **Claim:** Between 2026-09-26 and 2026-10-03, Bangkok will report at least one confirmed flood-related fatality.
- **Resolution criterion:** At least one confirmed flood-related fatality will be reported in Bangkok between 2026-09-26 and 2026-10-03.
- **Failure condition:** No confirmed flood-related fatality is reported in Bangkok between 2026-09-26 and 2026-10-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-24
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Luiz Inacio Lula da Silva receives more valid votes than Flavio Bolsonaro in the first round of the Brazilian presidential election held on 2026-10-04.
- **Resolution criterion:** TRUE if the TSE official first-round totals for 2026-10-04 show Luiz Inacio Lula da Silva with more valid votes than Flavio Bolsonaro.
- **Failure condition:** Flavio Bolsonaro receives at least as many first-round valid votes as Lula on 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-33
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-07
- **Domain:** political
- **Claim:** Luiz Inacio Lula da Silva finishes first in valid votes in the first round of the Brazilian presidential election on 2026-10-04.
- **Resolution criterion:** TRUE if final first-round results published by the Tribunal Superior Eleitoral show Lula with more valid votes than any other presidential candidate; FALSE otherwise.
- **Failure condition:** TSE first-round results show any candidate other than Lula with the most valid votes on 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-15
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-08
- **Domain:** crime_security
- **Claim:** A second person is charged over the 2026-08-15 Virginia State University shooting, with the charges filed between 2026-08-17 and 2026-10-05.
- **Resolution criterion:** Chesterfield County Police, the Commonwealth Attorney, or Virginia online court records show charges against a second defendant filed inside that range, checked 2026-10-08.
- **Failure condition:** Only the single person taken into custody on 2026-08-15 stands charged at the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-14
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-08
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield exceeds 4.85 percent on a weekday.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 4.85 percent on a weekday between 2026-09-21 and 2026-09-24.
- **Failure condition:** The 10-year U.S. Treasury yield is at or below 4.85 percent on every weekday between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261011T184630ZZ - sha256 4dcf56a3652624c8...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 4.85; 4 day(s) satisfying

### KKR-20260901-16
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a cyberattack attributed to Russia-aligned actors targets a U.S. government agency using a previously unreported exploit.
- **Resolution criterion:** A cyberattack attributed to Russia-aligned actors targets a U.S. government agency using a previously unreported exploit, confirmed by at least two independent sources.
- **Failure condition:** No cyberattack attributed to Russia-aligned actors targets a U.S. government agency using a previously unreported exploit during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-17
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-08
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new political summit involving Russia, Iran, and the U.S. is confirmed by at least two hostile sides.
- **Resolution criterion:** At least two hostile sides (e.g., RU, WEST, AXIS) confirm the existence of a new political summit involving Russia, Iran, and the U.S. between 2026-09-21 and 2026-09-24.
- **Failure condition:** No two hostile sides confirm the existence of a new political summit involving Russia, Iran, and the U.S. during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-38
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-08
- **Domain:** economics/markets
- **Claim:** Between 2026-09-23 and 2026-09-29, the S&P 500 index will close above 7,700 points on at least one trading day.
- **Resolution criterion:** The S&P 500 closes at or above 7,700.00 on at least one weekday between 2026-09-23 and 2026-09-29, based on the official market close from a public exchange.
- **Failure condition:** The S&P 500 closes below 7,700.00 on every trading day between 2026-09-23 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-15
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, at least one confirmed cyberattack exploiting CVE-2026-83548 will be reported by two or more independent sources.
- **Resolution criterion:** At least one confirmed cyberattack exploiting CVE-2026-83548 is reported by two or more independent sources between 2026-09-21 and 2026-09-24.
- **Failure condition:** No confirmed cyberattack exploiting CVE-2026-83548 is reported by two or more independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-20
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-48710 will be reported by two or more independent sources.
- **Resolution criterion:** A confirmed cyberattack exploiting CVE-2026-48710 is reported by two or more independent sources between 2026-09-21 and 2026-09-24.
- **Failure condition:** No confirmed cyberattack exploiting CVE-2026-48710 is reported by two or more independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-22
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting CVE-2026-9586 will be reported by two or more independent sources.
- **Resolution criterion:** A confirmed cyberattack exploiting CVE-2026-9586 is reported by two or more independent sources between 2026-09-21 and 2026-09-24.
- **Failure condition:** No confirmed cyberattack exploiting CVE-2026-9586 is reported by two or more independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-45
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-08
- **Domain:** military_conflict
- **Claim:** Between 2026-09-04 and 2026-10-04, at least one additional munition impact on the sovereign territory of Kuwait, Bahrain, Qatar, Saudi Arabia, or the United Arab Emirates is publicly attributed to Iran or Iran-aligned forces by the host government.
- **Resolution criterion:** MET if two of Reuters, AP, AFP report a munition impact on one of those five states dated inside the window, and that host government publicly attributes the impact to Iran or Iran-aligned forces.
- **Failure condition:** No munition impact inside the five named states during the window carries a host-government attribution to Iran or Iran-aligned forces.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-15
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-08
- **Domain:** military/conflict
- **Claim:** Iranian military or IRGC forces attack, board, or seize a commercial merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman between 2026-09-06 and 2026-10-05.
- **Resolution criterion:** At least two of Reuters, AP, BBC, Al Jazeera report Iranian military or IRGC forces attacking, boarding, or seizing a commercial merchant vessel in those waters between 2026-09-06 and 2026-10-05.
- **Failure condition:** Iranian state forces conduct no attack, boarding, or seizure of a commercial merchant vessel in the named waters between 2026-09-06 and 2026-10-05.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-02
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-23 and 2026-09-30, the CISA KEV catalog adds at least one new vulnerability with a CVSS score of 9.0 or higher that is actively exploited in the wild.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-23 and 2026-09-30 for a vulnerability with a CVSS score of 9.0 or higher and a 'Status' of 'Exploited in the Wild'.
- **Failure condition:** No new vulnerability with CVSS ≥9.0 and 'Exploited in the Wild' status is added to the CISA KEV catalog during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-06
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-08
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a tropical cyclone named NORBERT-26 will cause a green alert in GDACS with population affected exceeding 100,000.
- **Resolution criterion:** GDACS issues a green alert for tropical cyclone NORBERT-26 between 2026-09-21 and 2026-09-24 with a population affected estimate exceeding 100,000.
- **Failure condition:** GDACS does not issue a green alert for tropical cyclone NORBERT-26 between 2026-09-21 and 2026-09-24 with a population affected estimate exceeding 100,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-07
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-08
- **Domain:** military_conflict
- **Claim:** Russia conducts another missile or drone strike hitting rail infrastructure within 50 kilometers of the Ukraine-Poland border between 2026-09-15 and 2026-10-05, following the strike near that border reported on 14 September 2026.
- **Resolution criterion:** TRUE if at least two of Reuters, AP, Ukrzaliznytsia (Ukrainian state railways), or a Polish government statement confirm a Russian missile or drone strike hit rail infrastructure (track, station, or rolling stock) within 50 km of the Ukraine-Poland border at any point between 2026-09-15 and 2026-10-05. FALSE otherwise.
- **Failure condition:** No confirmed Russian strike on rail infrastructure within 50 km of the Ukraine-Poland border occurs between 2026-09-15 and 2026-10-05.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-08
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry for the GitLab vulnerability reported as under active exploitation on 14 September 2026, with a dateAdded value between 2026-09-15 and 2026-10-06.
- **Resolution criterion:** TRUE if the CISA KEV catalog (cisa.gov known_exploited_vulnerabilities JSON feed) contains an entry for a GitLab product vulnerability with a dateAdded value between 2026-09-15 and 2026-10-06. FALSE otherwise.
- **Failure condition:** The CISA KEV catalog shows no GitLab entry with a dateAdded value between 2026-09-15 and 2026-10-06.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184632ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['GitLab'] with dateAdded in [2026-09-15..2026-10-06] across 1739 catalog rows

### KKR-20260915-02
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-08
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year Treasury yield will exceed 5.00 percent at the close of any trading day.
- **Resolution criterion:** The 10-year Treasury yield exceeds 5.00 percent at the close of any trading day between 2026-09-21 and 2026-09-24.
- **Failure condition:** The 10-year Treasury yield never exceeds 5.00 percent at the close of any trading day between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261011T184635ZZ - sha256 4dcf56a3652624c8...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.00; 2 day(s) satisfying

### KKR-20260915-03
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a confirmed cyberattack exploiting the VMware vCenter RCE flaw (CVE-2026-76461) will be reported by two or more independent sources.
- **Resolution criterion:** Two or more independent sources report a confirmed cyberattack exploiting CVE-2026-76461 in the wild between 2026-09-21 and 2026-09-24.
- **Failure condition:** No independent source confirms a cyberattack exploiting CVE-2026-76461 between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-06
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a confirmed attack on a critical infrastructure system in the United States will be reported by two or more independent sources.
- **Resolution criterion:** Two or more independent sources report a confirmed attack on a critical infrastructure system in the United States between 2026-09-21 and 2026-09-24.
- **Failure condition:** No confirmed attack on a critical infrastructure system in the United States is reported by two or more independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-08
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a confirmed cyberattack using the BambooToken malware will be reported by two or more independent sources.
- **Resolution criterion:** Two or more independent sources report a confirmed cyberattack using BambooToken malware between 2026-09-21 and 2026-09-24.
- **Failure condition:** No independent source confirms a cyberattack using BambooToken malware between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-55
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-08
- **Domain:** military_conflict
- **Claim:** A NATO member state government attributes an intercepted, engaged, or shot-down aircraft or drone violating its airspace to Russia or a Russia-aligned actor, between 2026-09-16 and 2026-10-06.
- **Resolution criterion:** TRUE if a NATO member government or Reuters/AP/BBC reports the state intercepted or engaged an aircraft or drone violating its airspace and attributed it to Russia between 2026-09-16 and 2026-10-06, checked by 2026-10-08.
- **Failure condition:** No NATO member government attributes an intercepted airspace violation to Russia or a Russia-aligned actor within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-09
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-08
- **Domain:** economics/markets
- **Claim:** Between 2026-09-18 and 2026-09-25, the 10-year U.S. Treasury yield exceeds 5.0% on at least three consecutive trading days, as confirmed by the prior-session close data from MarketWatch.
- **Resolution criterion:** MarketWatch reports that the 10-year U.S. Treasury yield exceeded 5.0% on at least three consecutive trading days between 2026-09-18 and 2026-09-25.
- **Failure condition:** MarketWatch reports that the 10-year U.S. Treasury yield did not exceed 5.0% on three consecutive trading days between 2026-09-18 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-19
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-10-05, OpenAI publishes a security advisory, changelog entry, or blog post acknowledging a Codex sandbox escape and stating a fix or mitigation.
- **Resolution criterion:** True if a page on an openai.com domain dated in the window references a Codex sandbox escape and a fix, and BleepingComputer or The Hacker News reports the publication.
- **Failure condition:** No OpenAI-published acknowledgment with a stated fix for the Codex sandbox escape appears in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-26
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** The CISA KEV catalog will add a Cisco-vendor entry with dateAdded between 2026-09-21 and 2026-10-05.
- **Resolution criterion:** True if CISA's KEV catalog lists an entry with vendorProject Cisco and dateAdded between 2026-09-21 and 2026-10-05, checked 2026-10-08.
- **Failure condition:** No Cisco-vendor entry with dateAdded in that window appears in the CISA KEV catalog by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184638ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Cisco'] with dateAdded in [2026-09-21..2026-10-05] across 1739 catalog rows - CVE-2026-76504

### KKR-20260922-11
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds an entry for the VeloCloud Orchestrator vulnerability with a date-added value between 2026-09-22 and 2026-10-06.
- **Resolution criterion:** True if the CISA KEV catalog contains an entry whose product field references VeloCloud Orchestrator or VeloCloud SD-WAN Orchestrator and whose dateAdded is between 2026-09-22 and 2026-10-06 inclusive.
- **Failure condition:** No KEV entry referencing VeloCloud Orchestrator carries a dateAdded between 2026-09-22 and 2026-10-06.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261011T184641ZZ - sha256 fb1621beec7db19d...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['VeloCloud Orchestrator', 'VeloCloud SD-WAN Orchestrator'] with dateAdded in [2026-09-22..2026-10-06] across 1739 catalog rows - CVE-2026-93952

### KKR-20260922-17
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-08
- **Domain:** disaster
- **Claim:** Between 2026-09-22 and 2026-10-06, the confirmed death toll in Japan attributed to Typhoon Dujuan reaches at least 10, per Japan Fire and Disaster Management Agency figures or two of Reuters, AP, AFP, and NHK.
- **Resolution criterion:** True if the FDMA or two of Reuters, AP, AFP, NHK report, dated 2026-09-22 to 2026-10-06, a confirmed Typhoon Dujuan death toll in Japan of 10 or more.
- **Failure condition:** The confirmed Japan death toll attributed to Typhoon Dujuan remains below 10 through the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-02
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-08
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-10-03, the Strait of Hormuz will be closed to commercial shipping for at least 48 hours due to a confirmed Iranian military action.
- **Resolution criterion:** A confirmed Iranian military action will result in the Strait of Hormuz being closed to commercial shipping for at least 48 consecutive hours between 2026-09-26 and 2026-10-03.
- **Failure condition:** The Strait of Hormuz remains open to commercial shipping for more than 48 consecutive hours during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-10
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-08
- **Domain:** political
- **Claim:** In the Brazilian presidential election first round held on 2026-10-04 no candidate wins more than 50 percent of valid votes, so a second round on 2026-10-25 is required.
- **Resolution criterion:** Official TSE results (tse.jus.br) for the 2026-10-04 presidential first round show no candidate above 50 percent of valid votes and the TSE proceeds to a 2026-10-25 second round between the top two candidates.
- **Failure condition:** A candidate wins more than 50 percent of valid votes in the 2026-10-04 first round and no second round is held.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-32
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-08
- **Domain:** disaster
- **Claim:** Hurricane Polo makes landfall on the Baja California peninsula at hurricane intensity between 2026-09-28 and 2026-10-06.
- **Resolution criterion:** NHC public advisories or tropical cyclone updates for Polo state a landfall on the Baja California peninsula with maximum sustained winds of 64 knots or higher, dated within the window.
- **Failure condition:** Polo does not make landfall on the Baja California peninsula at hurricane intensity within the window per NHC products.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-02
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-29 and 2026-10-06, a new vulnerability in the OpenAI GPT-6.1 Astra model is publicly disclosed and exploited in at least one real-world attack.
- **Resolution criterion:** A new vulnerability in the OpenAI GPT-6.1 Astra model is publicly disclosed and exploited in at least one real-world attack between 2026-09-29 and 2026-10-06.
- **Failure condition:** No public disclosure or real-world exploitation of a vulnerability in the OpenAI GPT-6.1 Astra model occurs between 2026-09-29 and 2026-10-06.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-03
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-08
- **Domain:** cyber
- **Claim:** Between 2026-09-29 and 2026-10-06, a new cyberattack using the JadePuffer agentic AI framework targets Azure cloud infrastructure.
- **Resolution criterion:** A new cyberattack using the JadePuffer agentic AI framework targets Azure cloud infrastructure between 2026-09-29 and 2026-10-06.
- **Failure condition:** No cyberattack using the JadePuffer agentic AI framework targeting Azure cloud infrastructure occurs between 2026-09-29 and 2026-10-06.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-04
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-08
- **Domain:** political
- **Claim:** Between 2026-09-29 and 2026-10-06, a new political scandal involving a US senator and a foreign government is reported by two independent wire services.
- **Resolution criterion:** A new political scandal involving a US senator and a foreign government is reported by two independent wire services (e.g., Reuters, AP, Bloomberg) between 2026-09-29 and 2026-10-06.
- **Failure condition:** No such scandal is reported by two independent wire services during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-60
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-09
- **Domain:** political
- **Claim:** No candidate wins a majority of valid votes in the first round of the Brazilian presidential election held on 2026-10-04, sending the contest to a second round per official TSE results.
- **Resolution criterion:** True if official TSE first-round results for the 2026-10-04 Brazilian presidential election show no candidate above 50 percent of valid votes, requiring a second round.
- **Failure condition:** A candidate wins more than 50 percent of valid first-round votes, deciding the presidency without a runoff.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-18
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-09
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, Iran will launch a missile strike against a target in Kuwait City, confirmed by at least two independent sources.
- **Resolution criterion:** Iran launches a missile strike against a target in Kuwait City, confirmed by at least two independent sources between 2026-09-21 and 2026-09-24.
- **Failure condition:** No missile strike against a target in Kuwait City is confirmed by at least two independent sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-30
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-09
- **Domain:** economics/markets
- **Claim:** Brent crude trades above 110.00 US dollars per barrel on at least one trading day between 2026-09-04 and 2026-10-02. Reference: 96.70 on the packet date.
- **Resolution criterion:** The FRED series DCOILBRENTEU (EIA Brent Europe spot) reports a daily value strictly above 110.00 for at least one observation dated 2026-09-04 through 2026-10-02 inclusive. Reference: 96.70 on the packet date.
- **Failure condition:** No DCOILBRENTEU observation dated 2026-09-04 through 2026-10-02 exceeds 110.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-57
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-09
- **Domain:** political
- **Claim:** Between 2026-09-25 and 2026-10-02, a new political development in the U.S. involves a public statement by Jared Kushner or Steve Witkoff on Ukraine peace talks, confirmed by at least two independent sources (one from Guardian, one from BBC).
- **Resolution criterion:** A public statement by Jared Kushner or Steve Witkoff on Ukraine peace talks is confirmed by at least two independent sources (one from Guardian, one from BBC) between 2026-09-25 and 2026-10-02.
- **Failure condition:** No public statement by Jared Kushner or Steve Witkoff on Ukraine peace talks is confirmed by at least two independent sources (one from Guardian, one from BBC) between 2026-09-25 and 2026-10-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-85
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-09
- **Domain:** military/conflict
- **Claim:** Between 2026-09-07 and 2026-10-07 at least one commercial vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman is attacked, struck, or seized in an incident attributed to US or Iranian forces.
- **Resolution criterion:** A CENTCOM release, or reports from at least two of Reuters, AP, AFP, identify a specific vessel attacked or seized in the named waters within the window, attributed to US or Iranian forces.
- **Failure condition:** No incident meeting the vessel, location, attribution, and window criteria occurs during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-03
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-09
- **Domain:** disaster
- **Claim:** Between 2026-09-24 and 2026-10-01, a major earthquake of magnitude 6.0 or higher occurs in the Pacific Northwest region (Washington, Oregon, or Northern California).
- **Resolution criterion:** The USGS Significant Quakes feed records an earthquake with magnitude ≥6.0 and location within the Pacific Northwest (latitude 39.0-49.0, longitude -124.0 to -116.0) between 2026-09-24 and 2026-10-01.
- **Failure condition:** No earthquake of magnitude 6.0 or higher is recorded in the Pacific Northwest during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-02
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-09
- **Domain:** disaster
- **Claim:** Between 2026-09-26 and 2026-10-02, a new earthquake of magnitude 6.0 or higher is recorded by the USGS in the Pacific Northwest.
- **Resolution criterion:** The USGS Significant Quakes feed records an earthquake of magnitude 6.0 or higher in the Pacific Northwest (e.g., Washington, Oregon, Alaska) between 2026-09-26 and 2026-10-02.
- **Failure condition:** No earthquake of magnitude 6.0 or higher is recorded in the Pacific Northwest by the USGS between 2026-09-26 and 2026-10-02.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261011T184644ZZ - sha256 20fc3ffed799efd5...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-26&endtime=2026-10-02&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260910-07
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-09
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, Trump will publicly promise a $5,000 dividend to all U.S. adults if the GOP wins the 2026 midterm elections.
- **Resolution criterion:** A public statement by Donald Trump between 2026-09-21 and 2026-09-24 confirms a $5,000 dividend for all U.S. adults contingent on a GOP midterm victory.
- **Failure condition:** Donald Trump does not make a public statement between 2026-09-21 and 2026-09-24 promising a $5,000 dividend to all U.S. adults contingent on a GOP midterm victory.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-02
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-09
- **Domain:** political
- **Claim:** Between 2026-09-24 and 2026-10-01, the Federal Register will publish a rulemaking notice related to AI safety or regulation.
- **Resolution criterion:** The Federal Register publishes a rulemaking notice related to AI safety or regulation between 2026-09-24 and 2026-10-01.
- **Failure condition:** No rulemaking notice related to AI safety or regulation is published in the Federal Register between 2026-09-24 and 2026-10-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-54
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-09
- **Domain:** military_conflict
- **Claim:** A Ukrainian strike damages a named Russian oil refinery between 2026-09-15 and 2026-10-06, notwithstanding US pressure to stop refinery strikes.
- **Resolution criterion:** TRUE if a Russian federal or regional official confirms a strike on a named refinery dated between 2026-09-15 and 2026-10-06, and Reuters or AFP reports the same strike.
- **Failure condition:** MISS if no strike on a named Russian refinery inside the window is confirmed by both a Russian official and a major wire service.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-11
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-09
- **Domain:** cyber
- **Claim:** Between 2026-09-17 and 2026-09-24, a cyberattack targeting the U.S. power grid using a previously unknown exploit is confirmed by CISA to have disrupted at least one regional grid operator, as reported by BleepingComputer and The Hacker News.
- **Resolution criterion:** CISA confirms via the KEV catalog that a previously unknown exploit was used in a cyberattack between 2026-09-17 and 2026-09-24 to disrupt at least one regional U.S. power grid operator, as confirmed by BleepingComputer and The Hacker News.
- **Failure condition:** CISA does not confirm a previously unknown exploit used in a cyberattack on the U.S. power grid between 2026-09-17 and 2026-09-24, or no report from BleepingComputer or The Hacker News confirms disruption of a regional grid operator.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-30
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-09
- **Domain:** economics/markets
- **Claim:** Tesla Q3 2026 total vehicle deliveries, published in its production and deliveries release between 2026-10-01 and 2026-10-06, come in below the Q3 2025 record of 497,099. Reference: Q2 2026 deliveries were 480,126.
- **Resolution criterion:** True if the total deliveries figure in the Tesla Q3 2026 production and deliveries release (ir.tesla.com or SEC Form 8-K) issued between 2026-10-01 and 2026-10-06 is 497,098 or lower; false otherwise.
- **Failure condition:** Tesla reports Q3 2026 total deliveries of 497,099 or more, or issues no Q3 2026 deliveries release between 2026-10-01 and 2026-10-06.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-07
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-10
- **Domain:** economics/markets
- **Claim:** The United States will announce a new or expanded tariff action targeting Canadian goods, explicitly framed as a response to Canada's 2026-08-25 announcement of retaliatory tariffs on about 20 billion dollars of US goods, between 2026-08-27 and 2026-10-08.
- **Resolution criterion:** The White House, USTR, or Commerce Department announces new or increased tariffs on Canada linked to the Aug 25 Canadian tariffs, dated between 2026-08-27 and 2026-10-08, per at least two wire or business outlets.
- **Failure condition:** The US announces no new or expanded tariff action targeting Canada linked to the Aug 25 Canadian tariffs by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-07
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-10
- **Domain:** disaster
- **Claim:** A major flash flood in Nepal results in at least 50 confirmed deaths between 2026-10-01 and 2026-10-08.
- **Resolution criterion:** At least 50 confirmed deaths from a flash flood in Nepal are reported by at least two independent sources from different hostile sides (PS, WEST, RU) within the event window, with the first report appearing no later than 2026-10-08.
- **Failure condition:** No report from at least two independently biased sources confirms 50 or more confirmed deaths from a flash flood in Nepal during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-39
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-10
- **Domain:** disaster
- **Claim:** Between 2026-09-25 and 2026-10-01, a new earthquake of magnitude 6.0 or greater will be recorded by the USGS in the Pacific Ring of Fire region.
- **Resolution criterion:** The USGS Significant Quakes feed records a new earthquake event with magnitude ≥6.0 and depth ≤100km in the Pacific Ring of Fire between 2026-09-25 and 2026-10-01.
- **Failure condition:** No earthquake of magnitude 6.0 or greater is recorded by the USGS in the Pacific Ring of Fire during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-58
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-10
- **Domain:** disaster
- **Claim:** Between 2026-09-26 and 2026-10-03, a new earthquake of magnitude 5.5 or higher is recorded in the Solomon Islands, confirmed by USGS Significant Quakes.
- **Resolution criterion:** The USGS Significant Quakes system carries a report with magnitude ≥5.5 and location in the Solomon Islands between 2026-09-26 and 2026-10-03.
- **Failure condition:** The USGS Significant Quakes system does not carry a report with magnitude ≥5.5 and location in the Solomon Islands between 2026-09-26 and 2026-10-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-04
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-10
- **Domain:** political
- **Claim:** Between 2026-09-25 and 2026-10-02, a new political scandal involving a U.S. federal official is confirmed by at least two independent news outlets (e.g., Guardian, BBC, Al Jazeera) and results in a formal investigation by a congressional committee.
- **Resolution criterion:** At least two independent news outlets (Guardian World, BBC World, Al Jazeera) report a new political scandal involving a U.S. federal official, and a U.S. congressional committee publicly announces a formal investigation into the matter between 2026-09-25 and 2026-10-02.
- **Failure condition:** No such scandal is confirmed by two independent outlets or no formal congressional investigation is announced during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-03
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-10
- **Domain:** political
- **Claim:** Between 2026-09-27 and 2026-10-03, a new political scandal involving a U.S. federal official is confirmed by two independent outlets (e.g., Guardian World, NPR News).
- **Resolution criterion:** Two independent outlets (e.g., Guardian World, NPR News) confirm a political scandal involving a U.S. federal official between 2026-09-27 and 2026-10-03.
- **Failure condition:** No political scandal involving a U.S. federal official is confirmed by two independent outlets between 2026-09-27 and 2026-10-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-08
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-10
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a cyberattack on a U.S. federal agency will be confirmed by CISA involving the exploitation of a zero-day vulnerability in Google Chromium V8.
- **Resolution criterion:** CISA issues a public advisory confirming a cyberattack on a U.S. federal agency between 2026-09-21 and 2026-09-24 involving the exploitation of a zero-day vulnerability in Google Chromium V8.
- **Failure condition:** CISA does not issue a public advisory confirming a cyberattack on a U.S. federal agency between 2026-09-21 and 2026-09-24 involving the exploitation of a zero-day vulnerability in Google Chromium V8.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-10
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-10
- **Domain:** political
- **Claim:** On 2026-09-23, the European Union formally invites Canada to become its first associate member, as confirmed by two independent outlets (BBC World and Al Jazeera) reporting the same announcement.
- **Resolution criterion:** Two independent outlets (BBC World and Al Jazeera) report on 2026-09-23 that the European Union formally invited Canada to become its first associate member.
- **Failure condition:** No two independent outlets confirm that the European Union formally invited Canada to become its first associate member on 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-02
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-07, a drone strike will be confirmed by at least two hostile sides in the Gaza City area.
- **Resolution criterion:** At least two hostile sides (IL, PS, AXIS) will independently report a drone strike in Gaza City between 2026-10-01 and 2026-10-07, with corroborating reports from distinct channels.
- **Failure condition:** No drone strike is confirmed by two or more hostile sides in Gaza City during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-04
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-07, a missile attack will be confirmed by at least two hostile sides in Kyiv.
- **Resolution criterion:** At least two hostile sides (RU, UA) will independently report a missile attack in Kyiv between 2026-10-01 and 2026-10-07, with corroborating reports from distinct channels.
- **Failure condition:** No missile attack is confirmed by two or more hostile sides in Kyiv during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-05
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-10
- **Domain:** political
- **Claim:** Between 2026-10-01 and 2026-10-07, a new round of sanctions will be announced by the U.S. and EU targeting Iran's energy sector.
- **Resolution criterion:** On or before 2026-10-07, the U.S. and EU jointly announce new sanctions targeting Iran's energy sector, confirmed by at least two independent news outlets from different geopolitical blocs.
- **Failure condition:** No joint U.S.-EU announcement of new sanctions targeting Iran's energy sector is confirmed by two independent outlets from different geopolitical blocs during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-49
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-10
- **Domain:** disaster
- **Claim:** The GDACS wildfire alert for event ID 1032372 in Brazil will be upgraded from Green to Orange or Red, between 2026-09-24 and 2026-10-08.
- **Resolution criterion:** The GDACS report page for eventid=1032372 at gdacs.org shows an Orange or Red alert level at any point between 2026-09-24 and 2026-10-08, checked 2026-10-10.
- **Failure condition:** The GDACS event page for 1032372 never shows an Orange or Red alert level in the stated window; it stays Green or is closed out.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-04
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-10
- **Domain:** cyber
- **Claim:** Between 2026-10-01 and 2026-10-08, at least one confirmed cyberattack exploiting the Citrix NetScaler RCE vulnerability (CVE-2026-XXXX) will be reported by two or more independent sources.
- **Resolution criterion:** At least one cyberattack exploiting the Citrix NetScaler RCE vulnerability (CVE-2026-XXXX) will be reported by two or more sources from distinct hostile sides (e.g., RU, WEST, IL) during the event window.
- **Failure condition:** No such attack is confirmed by two or more independently biased sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-05
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-07, at least one report from a hostile side will confirm that a drone strike occurred in Jabalia, Gaza City, with casualties claimed by at least one side.
- **Resolution criterion:** At least one report from a hostile side (IL, PS, or AXIS) will confirm a drone strike in Jabalia, Gaza City, during the window, with casualties claimed in at least one corroborating report
- **Failure condition:** No report from a hostile side confirms a drone strike in Jabalia, Gaza City, during the window, or no casualty claim is made in any corroborating report
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-10
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** On 2026-10-02, a drone attack targeting a civilian facility in Kyiv, Ukraine, results in at least one confirmed fatality, as verified by at least two independent outlets from hostile sides (RU, UA) reporting the event with casualty details.
- **Resolution criterion:** At least one confirmed fatality is reported in a drone attack on a civilian facility in Kyiv, Ukraine, between 2026-10-02 and 2026-10-08, as confirmed by at least two independent outlets from hostile sides (RU, UA) in corroborating reports that include casualty counts.
- **Failure condition:** No report from two or more independent outlets across hostile sides (RU, UA) confirms a fatality in a drone attack on a civilian facility in Kyiv between 2026-10-02 and 2026-10-08.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-11
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** cyber
- **Claim:** Between 2026-10-01 and 2026-10-07, at least one verified cyberattack exploiting CVE-2026-76504 will be reported in public sources from at least two independent outlets across hostile sides (WEST, RU).
- **Resolution criterion:** At least one verified cyberattack exploiting CVE-2026-76504 is reported in public sources from at least two independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07.
- **Failure condition:** No verified cyberattack exploiting CVE-2026-76504 is reported in public sources from two or more independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-12
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-07, a confirmed attack using a Shahed drone will be reported in the Gaza City area, with at least one casualty, as verified by at least two independent outlets from hostile sides (IL, PS).
- **Resolution criterion:** A confirmed attack using a Shahed drone in Gaza City is reported with at least one casualty, as verified by at least two independent outlets from hostile sides (IL, PS) between 2026-10-01 and 2026-10-07.
- **Failure condition:** No attack using a Shahed drone in Gaza City with at least one casualty is confirmed by two or more independent outlets from hostile sides (IL, PS) between 2026-10-01 and 2026-10-07.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-13
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** cyber
- **Claim:** On 2026-10-08, the Metamask security incident will result in the permanent exit of at least 500 Ethereum validators from the network, as confirmed by a public blockchain analytics report.
- **Resolution criterion:** The Metamask security incident results in the permanent exit of at least 500 Ethereum validators from the network, as confirmed by a public blockchain analytics report on 2026-10-08.
- **Failure condition:** Fewer than 500 Ethereum validators permanently exit the network due to the Metamask security incident, as confirmed by a public blockchain analytics report on 2026-10-08.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-14
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** cyber
- **Claim:** Between 2026-10-01 and 2026-10-07, a confirmed cyberattack using the RedFlick technique will be reported in public sources from at least two independent outlets across hostile sides (WEST, RU).
- **Resolution criterion:** A confirmed cyberattack using the RedFlick technique is reported in public sources from at least two independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07.
- **Failure condition:** No cyberattack using the RedFlick technique is reported in public sources from two or more independent outlets across hostile sides (WEST, RU) between 2026-10-01 and 2026-10-07.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-15
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-10
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-07, a confirmed drone strike on a civilian facility in Tehran, Iran, will result in at least one fatality, as verified by at least two independent outlets from hostile sides (AXIS, WEST).
- **Resolution criterion:** A confirmed drone strike on a civilian facility in Tehran, Iran, results in at least one fatality, as verified by at least two independent outlets from hostile sides (AXIS, WEST) between 2026-10-01 and 2026-10-07.
- **Failure condition:** No drone strike on a civilian facility in Tehran, Iran, with at least one fatality is confirmed by two or more independent outlets from hostile sides (AXIS, WEST) between 2026-10-01 and 2026-10-07.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).
