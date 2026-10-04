# KKR RESOLUTION AUDIT PACKET
Generated 040320Z OCT 26 · 181 projections (part 2 of 2; packet total 502) past deadline, awaiting adjudication.

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

### KKR-20260902-62
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** disaster_infrastructure
- **Claim:** Nepal's National Disaster Risk Reduction and Management Authority reports a confirmed death toll of at least 1,500 from the August-September 2026 Nepal-Tibet floods, reported between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if NDRRMA, Nepal's Home Ministry, or two independent wire services report a confirmed death toll of 1,500 or more within the window; FALSE if the reported toll stays below 1,500 throughout.
- **Failure condition:** NDRRMA or wire reporting shows the confirmed Nepal-Tibet flood death toll remains below 1,500 through the end of the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-01
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the S&P 500 closes above 7,800 points on at least one trading day.
- **Resolution criterion:** The S&P 500 closes above 7,800 points on at least one trading day between 2026-09-21 and 2026-09-24, as reported by the Federal Reserve Economic Data (FRED) or Bloomberg.
- **Failure condition:** The S&P 500 never closes above 7,800 points during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-03
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a new cyberattack targets a U.S. federal agency using a previously unpatched vulnerability, as confirmed by a CISA KEV entry and a government press release.
- **Resolution criterion:** The CISA KEV catalog carries a new entry for a previously unpatched vulnerability exploited in a cyberattack against a U.S. federal agency, with a date-added value between 2026-09-21 and 2026-09-24, and a U.S. federal agency issues a public press release confirming the breach.
- **Failure condition:** No such KEV entry is added or no federal agency confirms a breach during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-15
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-09-28
- **Domain:** military_conflict
- **Claim:** The Saudi-led coalition conducts an airstrike on Houthi forces in or near Mocha, Yemen, between 2026-09-17 and 2026-09-24.
- **Resolution criterion:** TRUE if confirmed by one Saudi or coalition-aligned source and one Houthi-aligned source, or by two wire services among Reuters, AP, and AFP, reporting a strike near Mocha.
- **Failure condition:** No coalition or Saudi airstrike on Houthi positions at or near Mocha is confirmed within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-01
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield exceeds 5.0% on at least one weekday.
- **Resolution criterion:** The 10-year U.S. Treasury yield on a weekday between 2026-09-21 and 2026-09-24 is greater than 5.0%.
- **Failure condition:** The 10-year U.S. Treasury yield is at or below 5.0% on every weekday between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032001ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.00; 2 day(s) satisfying

### KKR-20260911-03
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the U.S. dollar strengthens to a 1.17 exchange rate against the euro on at least one weekday.
- **Resolution criterion:** The EUR/USD exchange rate on a weekday between 2026-09-21 and 2026-09-24 is less than or equal to 1.17.
- **Failure condition:** The EUR/USD exchange rate is above 1.17 on every weekday between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-05
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-28
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new political statement by a U.S. government official about Iran's nuclear program is confirmed by at least two independent news outlets (e.g., BBC, Guardian, Al Jazeera).
- **Resolution criterion:** Two or more independent news outlets report a public statement by a U.S. government official on Iran's nuclear program between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such statement is confirmed by two independent news outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-11
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-28
- **Domain:** political
- **Claim:** Between 2026-09-19 and 2026-09-26, the European Parliament will adopt a resolution calling for the immediate suspension of all EU military aid to Ukraine.
- **Resolution criterion:** The European Parliament will adopt a resolution calling for the immediate suspension of all EU military aid to Ukraine between 2026-09-19 and 2026-09-26.
- **Failure condition:** The European Parliament does not adopt a resolution calling for the immediate suspension of all EU military aid to Ukraine between 2026-09-19 and 2026-09-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-01
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-18 and 2026-09-25, the S&P 500 closes above 7,700 points on at least three trading days, with each close verified by the Dow Jones Market Data feed.
- **Resolution criterion:** The Dow Jones Market Data feed shows the S&P 500 closing above 7,700 on three or more days between 2026-09-18 and 2026-09-25.
- **Failure condition:** The S&P 500 closes below 7,700 on all days between 2026-09-18 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-07
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-28
- **Domain:** political
- **Claim:** On 2026-09-25, a new BRICS summit resolution is adopted calling for a joint peace initiative in the Middle East, as confirmed by the official BRICS website and two international news agencies.
- **Resolution criterion:** The official BRICS website and two international news agencies (e.g., Al Jazeera, BBC) confirm the adoption of a joint peace initiative resolution at the BRICS summit on 2026-09-25.
- **Failure condition:** No confirmation from the BRICS website or two international agencies that a peace initiative resolution was adopted on 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-01
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-22 and 2026-09-25, the S&P 500 closes below 7,500 points on at least one trading day, based on the official market close from the NYSE.
- **Resolution criterion:** The S&P 500 index closes below 7,500 points on at least one trading day between 2026-09-22 and 2026-09-25, as recorded by the NYSE official close.
- **Failure condition:** The S&P 500 closes at or above 7,500 points on all trading days between 2026-09-22 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-38
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-28
- **Domain:** political
- **Claim:** The US Senate records a cloture or passage roll call vote on the Clarity Act digital asset bill between 2026-09-15 and 2026-09-25 and the motion receives at least 60 yea votes.
- **Resolution criterion:** Senate.gov roll call records show a cloture or passage vote on the Clarity Act between 2026-09-15 and 2026-09-25 receiving 60 or more yeas.
- **Failure condition:** No cloture or passage vote on the bill reaches 60 yeas within the window, whether because no vote occurs or the motion falls short.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-09
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** Between 2026-09-18 and 2026-09-25, the 10-year Treasury yield will exceed 5.10 percent on at least one weekday.
- **Resolution criterion:** The 10-year Treasury yield exceeds 5.10 percent on at least one weekday between 2026-09-18 and 2026-09-25.
- **Failure condition:** The 10-year Treasury yield never exceeds 5.10 percent during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032002ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 6 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.10; 3 day(s) satisfying

### KKR-20260920-09
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** On 2026-09-25, the S&P 500 will close below 7,500.00 points.
- **Resolution criterion:** The closing price of the S&P 500 on 2026-09-25 will be less than 7,500.00 points, based on the official market close.
- **Failure condition:** The S&P 500 closes at or above 7,500.00 points on 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-12
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-09-28
- **Domain:** economics/markets
- **Claim:** On 2026-09-23, the 10-year U.S. Treasury yield will close above 5.10 percent.
- **Resolution criterion:** The closing yield of the 10-year U.S. Treasury note on 2026-09-23 will be greater than 5.10 percent, based on the official market close.
- **Failure condition:** The 10-year U.S. Treasury yield closes at or below 5.10 percent on 2026-09-23.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032003ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 6 business days in window; max BC_10YEAR 5.24 on 2026-09-28; threshold > 5.10; 4 day(s) satisfying

### KKR-20260809-11
- **Issued:** 2026-08-09  ·  **Deadline:** 2026-09-29
- **Domain:** crime/security
- **Claim:** Trial proceedings in the New York state prosecution of Luigi Mangione commence in open court between 2026-09-08 and 2026-09-25.
- **Resolution criterion:** The New York County Supreme Court docket or courtroom reporting records jury selection or opening statements in the state case beginning inside the window.
- **Failure condition:** Neither jury selection nor opening statements in the state case begin on or before 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260815-17
- **Issued:** 2026-08-15  ·  **Deadline:** 2026-09-29
- **Domain:** economic
- **Claim:** The 10-Year Treasury Constant Maturity Rate, FRED series DGS10, closes at or above 4.75 percent on at least one trading day between 2026-08-17 and 2026-09-25.
- **Resolution criterion:** The FRED DGS10 series shows a closing value of 4.75 or higher for at least one date between 2026-08-17 and 2026-09-25.
- **Failure condition:** DGS10 fails to close at or above 4.75 percent on every trading day between 2026-08-17 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-23
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** CISA adds at least one Zimbra Collaboration CVE to the Known Exploited Vulnerabilities catalog, with a date-added value between 2026-08-21 and 2026-09-25.
- **Resolution criterion:** The CISA KEV catalog JSON contains an entry whose vendorProject or product field names Zimbra and whose dateAdded falls between 2026-08-21 and 2026-09-25 inclusive.
- **Failure condition:** At the deadline no KEV entry naming Zimbra carries a dateAdded inside the stated window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032004ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Zimbra'] with dateAdded in [2026-08-21..2026-09-25] across 1733 catalog rows - CVE-2026-73570

### KKR-20260827-20
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-09-29
- **Domain:** military/conflict
- **Claim:** UKMTO publishes at least one incident advisory reporting a merchant vessel struck or damaged by a projectile, mine, or uncrewed system within 100 nautical miles of the Strait of Hormuz, anchor 26.5N 56.3E, between 2026-08-27 and 2026-09-25.
- **Resolution criterion:** A UKMTO advisory at ukmto.org dated 2026-08-27 through 2026-09-25 reports a vessel struck or damaged by a projectile, mine, or uncrewed system at a position within 100 nm of 26.5N 56.3E; otherwise false.
- **Failure condition:** No merchant vessel is struck or damaged by a projectile, mine, or uncrewed system within 100 nm of 26.5N 56.3E between 2026-08-27 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-12
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** Manchester Airports Group, the ICO, or two independent outlets will confirm a data breach matching FulcrumSec's claimed August 2026 theft of 86 GB of data, between 2026-08-31 and 2026-09-27.
- **Resolution criterion:** TRUE if MAG, the ICO, or two independent outlets confirm the breach, or verified stolen data surfaces on a leak marketplace, within the window; otherwise FALSE.
- **Failure condition:** MAG issues no confirmation, the ICO records no notification, and no verified sample of the claimed data surfaces between 2026-08-31 and 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-16
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-29
- **Domain:** disaster_infrastructure
- **Claim:** The confirmed death toll from the late-August 2026 Nepal-Tibet border floods and landslides, reported at approximately 750 with about 3000 still missing as of 2026-08-30, will exceed 900 per Nepali government or wire-service reporting, between 2026-08-31 and 2026-09-27.
- **Resolution criterion:** TRUE if Nepal's government, Reuters, AP, or AFP report a confirmed death toll above 900 from this flood and landslide event within the window; otherwise FALSE.
- **Failure condition:** The confirmed death toll from this flood and landslide event stays at or below 900 in all official and wire-service reporting through 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-19
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** The actively exploited Chrome V8 vulnerability CVE-2026-85046, patched by Google on 2026-09-03, will be added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-05 and 2026-09-25.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists CVE-2026-85046 with a dateAdded value between 2026-09-05 and 2026-09-25; otherwise FALSE.
- **Failure condition:** CVE-2026-85046 is absent from the CISA KEV catalog, or carries a dateAdded outside that window, as of the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032006ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-85046'] with dateAdded in [2026-09-05..2026-09-25] across 1733 catalog rows

### KKR-20260904-20
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-29
- **Domain:** political
- **Claim:** Sara Duterte will be held in physical government custody for more than 24 continuous hours under the Quezon City Regional Trial Court arrest warrant, at any point between 2026-09-05 and 2026-09-25.
- **Resolution criterion:** TRUE if two or more of AP, Reuters, or Al Jazeera report Duterte held in custody beyond 24 continuous hours between 2026-09-05 and 2026-09-25; otherwise FALSE.
- **Failure condition:** Duterte posts bail and is released within 24 hours, or is never taken into physical custody, within that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-22
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-85046, the Chrome V8 type confusion zero-day patched by Google on 2026-09-03, to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-04 and 2026-09-25.
- **Resolution criterion:** The CISA KEV JSON feed at the deadline contains an entry with cveID CVE-2026-85046 and a dateAdded value from 2026-09-04 through 2026-09-25 inclusive.
- **Failure condition:** At the deadline the KEV feed has no entry for CVE-2026-85046, or its dateAdded falls outside 2026-09-04 through 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-30
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-29
- **Domain:** crime/security
- **Claim:** Between 2026-09-11 and 2026-09-25 the NSW Supreme Court sentences Daniel Billings for the murder of Molly Ticehurst to life imprisonment or to a non-parole period of 30 years or more.
- **Resolution criterion:** The sentencing judgment (NSW Caselaw, R v Billings) or reporting by ABC and AAP shows a sentence handed down within the window that is life imprisonment or carries a non-parole period of at least 30 years.
- **Failure condition:** The sentence handed down carries a non-parole period under 30 years and is not life imprisonment, or no sentence is delivered from 2026-09-11 through 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-32
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds at least one entry with vendorProject CrowdStrike and a dateAdded value between 2026-09-04 and 2026-09-25, following the reported FalconFlank SYSTEM privilege zero-day.
- **Resolution criterion:** Fetch the CISA KEV JSON at the deadline; TRUE if any entry lists vendorProject CrowdStrike with dateAdded between 2026-09-04 and 2026-09-25; the entry need not be named FalconFlank.
- **Failure condition:** The KEV JSON fetched at the deadline contains no entry with vendorProject CrowdStrike and dateAdded between 2026-09-04 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-07
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-29
- **Domain:** military/conflict
- **Claim:** Between 2026-09-06 and 2026-09-26, US forces strike, disable, or destroy at least one additional Iranian oil tanker or crude carrier, as announced by US Central Command.
- **Resolution criterion:** TRUE if a US Central Command statement dated 2026-09-06 to 2026-09-26, carried by Reuters, AP, or AFP, reports a US strike on at least one Iranian oil tanker or crude carrier in that window, excluding the three struck 2026-09-05.
- **Failure condition:** No US strike on any Iranian oil tanker or crude carrier other than the three struck on 2026-09-05 occurs between 2026-09-06 and 2026-09-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-10
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-29
- **Domain:** economics/markets
- **Claim:** Between 2026-09-08 and 2026-09-25, the US Treasury Office of Foreign Assets Control publishes at least one Iran-related designation action.
- **Resolution criterion:** TRUE if the OFAC Recent Actions page (ofac.treasury.gov/recent-actions) lists at least one action dated 2026-09-08 through 2026-09-25 whose title contains Iran-related Designations or Iran-related Designation Updates.
- **Failure condition:** No OFAC Recent Actions entry dated between 2026-09-08 and 2026-09-25 carries an Iran-related Designations or Iran-related Designation Updates title.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-11
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-19490 (Citrix NetScaler ADC and Gateway authentication bypass) with a dateAdded value between 2026-09-05 and 2026-09-25.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed contains an entry for CVE-2026-19490 whose dateAdded field is between 2026-09-05 and 2026-09-25 inclusive.
- **Failure condition:** CVE-2026-19490 is absent from the KEV catalog at the deadline, or its dateAdded value falls outside 2026-09-05 through 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-13
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-29
- **Domain:** disaster
- **Claim:** Between 2026-09-06 and 2026-09-26, the USGS catalog records at least one earthquake of magnitude 6.0 or greater with epicenter within 300 km of USGS event us7000tdvt (M6.3, 84 km SSW of Nikolski, Alaska).
- **Resolution criterion:** TRUE if the USGS earthquake catalog (earthquake.usgs.gov) lists at least one event of magnitude 6.0 or greater, origin time 2026-09-06 through 2026-09-26 UTC, with epicenter within 300 km of event us7000tdvt.
- **Failure condition:** No magnitude 6.0 or greater earthquake with epicenter within 300 km of us7000tdvt has origin time between 2026-09-06 and 2026-09-26 UTC in the USGS catalog.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261004T032008ZZ - sha256 beb300cb15f4917d...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-06&endtime=2026-09-26&latitude=32.69&longitude=130.66&maxradiuskm=300&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260907-22
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds at least one N-able N-central vulnerability (CVE-2026-86218, CVE-2026-86207, or CVE-2026-86206) with a dateAdded between 2026-09-08 and 2026-09-25.
- **Resolution criterion:** The CISA Known Exploited Vulnerabilities JSON feed lists CVE-2026-86218, CVE-2026-86207, or CVE-2026-86206 with a dateAdded value from 2026-09-08 through 2026-09-25 inclusive. No entry, or entries dated outside that range only, resolves false.
- **Failure condition:** None of CVE-2026-86218, CVE-2026-86207, or CVE-2026-86206 carries a KEV dateAdded within 2026-09-08 to 2026-09-25.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032009ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-86218', 'CVE-2026-86207', 'CVE-2026-86206'] with dateAdded in [2026-09-08..2026-09-25] across 1733 catalog rows - CVE-2026-86218

### KKR-20260912-12
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-29
- **Domain:** cyber
- **Claim:** Between 2026-09-20 and 2026-09-27, at least one of the following will be reported in two or more independent outlets: a cyberattack on a U.S. federal agency using a vulnerability from the CISA KEV catalog or a ransomware attack on a U.S. hospital system.
- **Resolution criterion:** At least one of the following will be reported in two or more independent outlets: a cyberattack on a U.S. federal agency using a vulnerability from the CISA KEV catalog or a ransomware attack on a U.S. hospital system, with the event window falling between 2026-09-20 and 2026-09-27.
- **Failure condition:** No such cyber incident is reported in two or more independent outlets during the specified window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-05
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-29
- **Domain:** military/conflict
- **Claim:** Between 2026-09-19 and 2026-09-26, Iran conducts a ballistic missile test near the Strait of Hormuz, resulting in a confirmed alert from the UKMTO and two independent satellite tracking services.
- **Resolution criterion:** The UKMTO alert and two independent satellite tracking services confirm a ballistic missile test near the Strait of Hormuz between 2026-09-19 and 2026-09-26.
- **Failure condition:** No UKMTO alert or independent satellite confirmation of a missile test during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-15
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-29
- **Domain:** disaster
- **Claim:** Between 2026-09-14 and 2026-09-27, the confirmed death toll from the September 13, 2026 Java Sea ferry capsizing will reach or exceed 50.
- **Resolution criterion:** BASARNAS, Reuters, AP, or Al Jazeera report a confirmed death toll of 50 or more from the September 13, 2026 Java Sea ferry capsizing, dated between 2026-09-14 and 2026-09-27.
- **Failure condition:** The confirmed death toll from the September 13 Java Sea ferry disaster remains below 50 through the end of the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-61
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-29
- **Domain:** disaster
- **Claim:** GDACS raises the alert level for tropical cyclone FIFTEEN-E-26 to orange or red at some point between 2026-09-15 and 2026-09-25.
- **Resolution criterion:** TRUE if the GDACS event page for tropical cyclone FIFTEEN-E-26 shows an orange or red alert level assigned between 2026-09-15 and 2026-09-25.
- **Failure condition:** MISS if the GDACS alert level for that cyclone never exceeds green inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-57
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-29
- **Domain:** disaster_infrastructure
- **Claim:** GDACS upgrades its alert level for Tropical Cyclone TWENTYFOUR-26 from Green to Orange or Red, between 2026-09-16 and 2026-09-25.
- **Resolution criterion:** TRUE if gdacs.org shows an alert-level upgrade to Orange or Red for Tropical Cyclone TWENTYFOUR-26 dated between 2026-09-16 and 2026-09-25, checked 2026-09-29.
- **Failure condition:** GDACS's alert level for Tropical Cyclone TWENTYFOUR-26 stays Green, or the system is archived, without reaching Orange or Red in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260722-16
- **Issued:** 2026-07-22  ·  **Deadline:** 2026-09-30
- **Domain:** economics
- **Claim:** The United States 10-year Treasury yield closes above 4.80 percent on at least one trading day between 2026-07-23 and 2026-09-30
- **Resolution criterion:** US Treasury daily yield curve data or Bloomberg records show a 10-year constant maturity closing yield above 4.80 percent on any day in the window
- **Failure condition:** the condition stated in this entry's resolution basis — US Treasury daily yield curve data or Bloomberg records show a 10-year constant maturity closing yield above 4.80 percent on any day in the window — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032012ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 49 business days in window; max BC_10YEAR 5.29 on 2026-09-30; threshold > 4.80; 16 day(s) satisfying

### KKR-20260724-05
- **Issued:** 2026-07-24  ·  **Deadline:** 2026-09-30
- **Domain:** markets
- **Claim:** The S&P 500 index closes below 7000 on at least one trading day between 2026-07-27 and 2026-09-30.
- **Resolution criterion:** TRUE if the official S&P 500 closing level reported by major financial press is below 7000 on any trading day between 2026-07-27 and 2026-09-30; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if the official S&P 500 closing level reported by major financial press is below 7000 on any trading day between 2026-07-27 and 2026-09-30; else FALSE — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260724-06
- **Issued:** 2026-07-24  ·  **Deadline:** 2026-09-30
- **Domain:** military_conflict
- **Claim:** The United States and Iran publicly announce a ceasefire or formal cessation of hostilities between 2026-07-25 and 2026-09-30.
- **Resolution criterion:** TRUE if both governments, or a joint statement, publicly confirm a ceasefire or cessation of hostilities reported by major press between 2026-07-25 and 2026-09-30; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if both governments, or a joint statement, publicly confirm a ceasefire or cessation of hostilities reported by major press between 2026-07-25 and 2026-09-30; else FALSE — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260725-02
- **Issued:** 2026-07-25  ·  **Deadline:** 2026-09-30
- **Domain:** markets
- **Claim:** The S&P 500 closes at or below 7000 on at least one trading day between 2026-07-27 and 2026-09-30.
- **Resolution criterion:** TRUE if the official S&P 500 closing level reported by major financial press is 7000 or lower on any trading day between 2026-07-27 and 2026-09-30; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if the official S&P 500 closing level reported by major financial press is 7000 or lower on any trading day between 2026-07-27 and 2026-09-30; else FALSE — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260725-03
- **Issued:** 2026-07-25  ·  **Deadline:** 2026-09-30
- **Domain:** economics
- **Claim:** The United States 10-year Treasury yield closes at or above 5.00 percent on at least one trading day between 2026-07-27 and 2026-09-30.
- **Resolution criterion:** TRUE if the daily closing 10-year constant-maturity Treasury yield reported by the US Treasury or major financial press reaches 5.00 percent or higher on any trading day in the window; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if the daily closing 10-year constant-maturity Treasury yield reported by the US Treasury or major financial press reaches 5.00 percent or higher on any trading day in the window; else FALSE — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032013ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 47 business days in window; max BC_10YEAR 5.29 on 2026-09-30; threshold >= 5.00; 9 day(s) satisfying

### KKR-20260725-05
- **Issued:** 2026-07-25  ·  **Deadline:** 2026-09-30
- **Domain:** military_conflict
- **Claim:** The United States and Iran publicly announce a ceasefire or formal cessation of hostilities between 2026-07-27 and 2026-09-30.
- **Resolution criterion:** TRUE if both governments, or a joint statement, publicly confirm a ceasefire or cessation of hostilities reported by major press within the window; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if both governments, or a joint statement, publicly confirm a ceasefire or cessation of hostilities reported by major press within the window; else FALSE — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260726-09
- **Issued:** 2026-07-26  ·  **Deadline:** 2026-09-30
- **Domain:** disaster
- **Claim:** French authorities order a mandatory evacuation of any arrondissement inside Bordeaux city proper due to wildfire between 2026-07-26 and 2026-09-30.
- **Resolution criterion:** A prefectural or municipal mandatory evacuation order covering territory inside Bordeaux commune boundaries, attributed to wildfire, per two independent wire services.
- **Failure condition:** the condition stated in this entry's resolution basis — A prefectural or municipal mandatory evacuation order covering territory inside Bordeaux commune boundaries, attributed to wildfire, per two independent wire services — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-20
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** At least three separately published national voting-intention polls will place Reform UK ahead of Labour, each with fieldwork ending between 2026-07-28 and 2026-09-30.
- **Resolution criterion:** Counted from the pollsters' own published tables for that fieldwork window. Three distinct polling companies required; repeat waves by one company count once.
- **Failure condition:** the condition stated in this entry's resolution basis — Counted from the pollsters' own published tables for that fieldwork window — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-22
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** The United States Senate will confirm Jay Clayton to the intelligence post for which he was nominated, on or before 2026-09-30.
- **Resolution criterion:** Resolved by the roll-call record on congress.gov showing a completed confirmation vote in the affirmative on or before 2026-09-30.
- **Failure condition:** the condition stated in this entry's resolution basis — the roll-call record on congress.gov showing a completed confirmation vote in the affirmative on or before 2026-09-30 — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-24
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** The Israeli cabinet will publicly approve an expansion of ground operations in Gaza beyond the limited force approved in July 2026, on or before 2026-09-30.
- **Resolution criterion:** Resolved by an Israeli Prime Minister's Office statement or two wire services reporting a cabinet decision expanding the approved force, dated on or before 2026-09-30.
- **Failure condition:** the condition stated in this entry's resolution basis — an Israeli Prime Minister's Office statement or two wire services reporting a cabinet decision expanding the approved force, dated on or before 2026-09-30 — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-30
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** cyber
- **Claim:** OpenAI publishes a public incident report or postmortem covering the agent-related compromise reported on 2026-07-27, on or before 2026-09-30.
- **Resolution criterion:** Resolved by checking the OpenAI official blog and security pages on 2026-09-30. Yes if a dated public writeup of that specific incident is present.
- **Failure condition:** the condition stated in this entry's resolution basis — checking the OpenAI official blog and security pages — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-34
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** crime/security
- **Claim:** At least one person is formally charged with a homicide offense in connection with the 2026-07-26 Seattle festival shooting, on or before 2026-09-30.
- **Resolution criterion:** Resolved from King County Prosecuting Attorney charging documents or two major wire reports as of 2026-09-30. Yes if any homicide charge has been filed.
- **Failure condition:** the condition stated in this entry's resolution basis — King County Prosecuting Attorney charging documents or two major wire reports as of 2026-09-30 — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-35
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** CXMT shares close below their first-trading-day closing price on 2026-09-30.
- **Resolution criterion:** Resolved from the listing exchange official closing price on 2026-09-30 compared with the first-trading-day close. Yes if the 2026-09-30 close is lower.
- **Failure condition:** the condition stated in this entry's resolution basis — the listing exchange official closing price on 2026-09-30 compared with the first-trading-day close — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-13
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-09-30
- **Domain:** cyber
- **Claim:** CISA publishes an advisory, alert or advisory update that explicitly names the Minnesota water utility intrusions, on or before 2026-09-30.
- **Resolution criterion:** Resolved from the CISA cybersecurity advisories index on 2026-09-30. Yes if any item published after 2026-07-29 names Minnesota water utilities or that campaign.
- **Failure condition:** the condition stated in this entry's resolution basis — the CISA cybersecurity advisories index — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-15
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-09-30
- **Domain:** disaster
- **Claim:** USGS records at least one earthquake of magnitude 5.5 or greater within 100 km of the 2026-07-28 Uto epicentre between 2026-07-30 and 2026-09-30.
- **Resolution criterion:** Resolved from the USGS FDSN event query, radius 100 km on the Uto epicentre, minmagnitude 5.5, starttime 2026-07-30, endtime 2026-09-30. Yes if any event returns.
- **Failure condition:** the condition stated in this entry's resolution basis — the USGS FDSN event query, radius 100 km on the Uto epicentre, minmagnitude 5.5, starttime 2026-07-30, endtime 2026-09-30 — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261004T032013ZZ - sha256 2f263e4937447737...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-07-30&endtime=2026-09-30&latitude=32.69&longitude=130.66&maxradiuskm=100&minmagnitude=5.5
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260729-19
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** ICE Brent front-month crude settles at or above 100.00 US dollars per barrel on at least one trading day between 2026-07-30 and 2026-09-30.
- **Resolution criterion:** Resolved from the official ICE Brent front-month settlement series read on 2026-09-30. Yes if any settlement in the window is at or above 100.00.
- **Failure condition:** the condition stated in this entry's resolution basis — the official ICE Brent front-month settlement series read — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-01
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** The Strait of Hormuz is closed to commercial shipping for 24 or more consecutive hours between 2026-07-31 and 2026-09-30, as reported by at least two of Reuters, the Associated Press and Lloyds List.
- **Resolution criterion:** Resolved on 2026-09-30 by searching Reuters, AP and Lloyds List archives: hit if at least two report a closure or halt of commercial transits lasting 24 or more hours dated in the window, miss otherwise.
- **Failure condition:** No closure or halt of commercial Strait of Hormuz transits lasting 24 or more consecutive hours, dated 2026-07-31 through 2026-09-30, is reported by at least two of Reuters, AP and Lloyds List as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-02
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** NATO invokes Article 5 of the North Atlantic Treaty in response to the missile impact on Polish territory reported on 2026-07-30, with the invocation announced between 2026-07-31 and 2026-09-30.
- **Resolution criterion:** Resolved on 2026-09-30: hit if NATO or the North Atlantic Council announces an Article 5 invocation tied to the Poland missile impact, per nato.int or two major wires, dated in the window; miss otherwise.
- **Failure condition:** No Article 5 invocation tied to the 2026-07-30 Poland missile impact appears on nato.int or two major wires, dated in the window, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-03
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** The Federal Reserve announces a reduction of the federal funds target range at its September 2026 FOMC meeting, with the decision published between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** Resolved on 2026-09-30 from the FOMC statement at federalreserve.gov: hit if the September 2026 meeting statement announces a lower target range than the prior meeting, miss otherwise.
- **Failure condition:** The September 2026 FOMC statement at federalreserve.gov announces a target range equal to or higher than the prior meeting's, or no September statement exists by 2026-09-30; either reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-09
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** Ugandan authorities release Kizza Besigye from detention, including any transfer to house arrest or medical release abroad, between 2026-07-31 and 2026-09-30.
- **Resolution criterion:** Resolved on 2026-09-30: hit if at least two of BBC, Al Jazeera, Reuters or AP report Besigye released from detention in the window, miss otherwise.
- **Failure condition:** Fewer than two of BBC, Al Jazeera, Reuters and AP report Kizza Besigye released from detention (including house arrest or medical release abroad) dated in the window, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-11
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** military_conflict
- **Claim:** Between 2026-08-06 and 2026-09-30, US Central Command or the Department of Defense publicly confirms at least one new military strike on targets inside Iranian territory.
- **Resolution criterion:** True if an official US military or DoD statement, carried by two or more major outlets, confirms a strike inside Iran occurring between 2026-08-06 and 2026-09-30.
- **Failure condition:** No official US military or DoD statement confirming a new strike inside Iranian territory occurring 2026-08-06 through 2026-09-30 is carried by two or more major outlets, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-13
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** military_conflict
- **Claim:** NATO holds a formal Article 4 consultation at the request of a member state between 2026-08-06 and 2026-09-30.
- **Resolution criterion:** True if NATO or a member government publicly confirms an Article 4 consultation held between 2026-08-06 and 2026-09-30. Routine North Atlantic Council statements do not resolve this true.
- **Failure condition:** No formal Article 4 consultation requested by a member state and held 2026-08-06 through 2026-09-30 is publicly confirmed by NATO or a member government, as read on 2026-09-30 - routine North Atlantic Council statements not qualifying; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-27
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** The U.S. Senate will vote to confirm Todd Blanche as Attorney General between 2026-07-30 and 2026-09-30.
- **Resolution criterion:** True if the U.S. Senate holds a floor vote confirming Todd Blanche as Attorney General, as reported by a major outlet, between 2026-07-30 and 2026-09-30; otherwise false.
- **Failure condition:** No Senate floor vote confirming Todd Blanche as Attorney General between 2026-07-30 and 2026-09-30 is reported by a major outlet, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-02
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-09-30
- **Domain:** economic
- **Claim:** The September 2026 FOMC statement announces a federal funds target range higher than the July 2026 range, following three July dissents in favor of an increase
- **Resolution criterion:** The FOMC statement published at federalreserve.gov on or before 2026-09-30 announces a target range above the range set at the July 2026 meeting
- **Failure condition:** No FOMC statement dated on or before 2026-09-30 at federalreserve.gov announces a target range higher than the July 2026 range; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-20
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-09-30
- **Domain:** military_conflict
- **Claim:** The US Navy or Department of Defense publicly confirms a direct armed engagement between US forces and Iranian forces or Iranian-operated vessels or aircraft in or near the Strait of Hormuz between 2026-08-07 and 2026-09-30.
- **Resolution criterion:** True if an official US Navy, CENTCOM, or DoD statement carried by two or more major outlets confirms such an engagement occurring between 2026-08-07 and 2026-09-30.
- **Failure condition:** No official US Navy, CENTCOM or DoD statement carried by two or more major outlets confirms a direct armed engagement between US forces and Iranian forces or Iranian-operated vessels or aircraft in or near the Strait of Hormuz occurring 2026-08-07 through 2026-09-30, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-23
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-09-30
- **Domain:** economic
- **Claim:** Front-month WTI crude futures settle above 95.00 US dollars per barrel on at least one trading day between 2026-08-07 and 2026-09-30.
- **Resolution criterion:** True if NYMEX front-month WTI settlement exceeds 95.00 dollars on any session from 2026-08-07 through 2026-09-30, per exchange or major financial press data.
- **Failure condition:** No NYMEX front-month WTI settlement exceeds 95.00 USD on any session 2026-08-07 through 2026-09-30, per exchange or major financial press settlement data as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-24
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** Frontex or the European Commission publicly announces a deployment of personnel or emergency border funding to Spain in response to the Ceuta crossings between 2026-08-07 and 2026-09-30.
- **Resolution criterion:** True if Frontex or the European Commission issues a public statement in that window announcing personnel deployment or emergency funds to Spain for the Ceuta border.
- **Failure condition:** Neither Frontex nor the European Commission issues a public statement dated 2026-08-07 through 2026-09-30 announcing personnel deployment or emergency border funding to Spain for the Ceuta crossings, as read on 2026-09-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-04
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** At least one additional commercial vessel is struck by weapons in the Strait of Hormuz or Gulf of Oman between 2026-08-08 and 2026-09-30.
- **Resolution criterion:** Resolved from the UKMTO maritime incident report index on 2026-09-30. Yes if any advisory in the window records a commercial vessel struck by missile, drone or gunfire in those waters.
- **Failure condition:** the condition stated in this entry's resolution basis — any advisory in the window records a commercial vessel struck by missile, drone or gunfire in those waters — is not met on or before 2026-09-30 as read from the UKMTO maritime incident report index; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-06
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** NYMEX WTI front-month crude settles above 95.00 US dollars per barrel on at least one trading day between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** Resolved from the CME official NYMEX WTI front-month settlement series read on 2026-09-30. Yes if any settlement in the window is above 95.00.
- **Failure condition:** the condition stated in this entry's resolution basis — any settlement in the window is above 95.00 — is not met on or before 2026-09-30 as read from the CME official NYMEX WTI front-month settlement series read; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-07
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** An extraordinary European Council or Justice and Home Affairs Council session on the Ceuta migration crisis convenes between 2026-08-08 and 2026-09-30.
- **Resolution criterion:** Resolved from the Council of the EU meeting calendar on 2026-09-30. Yes if a special or extraordinary session in the window lists Ceuta or Spain-Morocco migration on its published agenda.
- **Failure condition:** the condition stated in this entry's resolution basis — a special or extraordinary session in the window lists Ceuta or Spain-Morocco migration on its published agenda — is not met on or before 2026-09-30 as read from the Council of the EU meeting calendar; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-16
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** WTI crude oil front-month futures will settle above 95.00 USD per barrel on at least one trading day between 2026-08-08 and 2026-09-30.
- **Resolution criterion:** Resolved from the CME official NYMEX WTI front-month settlement series read on 2026-09-30. Yes if any settlement in the window is above 95.00.
- **Failure condition:** the condition stated in this entry's resolution basis — any settlement in the window is above 95.00 — is not met on or before 2026-09-30 as read from the CME official NYMEX WTI front-month settlement series read; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-21
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** A commercial oil tanker will be attacked in the Strait of Hormuz or Gulf of Oman, reported by Reuters, AP, or a maritime security firm, between 2026-08-08 and 2026-09-30.
- **Resolution criterion:** Resolved from the UKMTO maritime incident report index on 2026-09-30. Yes if any advisory in the window records a commercial oil tanker struck by weapons in the Strait of Hormuz or Gulf of Oman.
- **Failure condition:** the condition stated in this entry's resolution basis — any advisory in the window records a commercial oil tanker struck by weapons in the Strait of Hormuz or Gulf of Oman — is not met on or before 2026-09-30 as read from the UKMTO maritime incident report index; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-23
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** US or Israeli forces strike Iranian oil or gas export infrastructure at Kharg Island, Bandar Abbas, or Asaluyeh between 2026-08-02 and 2026-09-30.
- **Resolution criterion:** YES if at least two major international news agencies report a US or Israeli strike on Iranian oil or gas export facilities at Kharg Island, Bandar Abbas, or Asaluyeh between 2026-08-02 and 2026-09-30; otherwise NO.
- **Failure condition:** the condition stated in this entry's resolution basis — at least two major international news agencies report a US or Israeli strike on Iranian oil or gas export facilities at Kharg Island, Bandar Abbas, or Asaluyeh between 2026-08-02 and 2026-09-30 — is not met on or before 2026-09-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-13
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** The OHCHR human rights monitoring mission monthly update covering August 2026 reports a Ukraine civilian-killed total lower than the July 2026 total it states.
- **Resolution criterion:** TRUE if the published OHCHR HRMMU update covering August 2026 states an August civilian-killed total strictly below its stated July 2026 total; FALSE if equal, higher, or no update is published by the deadline.
- **Failure condition:** The August update states a civilian-killed total equal to or above its July figure, or no update covering August 2026 exists by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-36
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-30
- **Domain:** economics_markets
- **Claim:** Between 2026-08-24 and 2026-09-30, COMEX front month gold futures will settle at or above 4800.00 USD per troy ounce on at least one trading day.
- **Resolution criterion:** TRUE if CME or COMEX publishes a front month gold futures settlement price of 4800.00 USD per ounce or higher on any trading day in the window; FALSE otherwise.
- **Failure condition:** COMEX front month gold futures never settle at or above 4800.00 USD per ounce on any trading day between 2026-08-24 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-27
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** A single Russian strike on Kyiv occurring between 2026-09-07 and 2026-09-27 produces an official Ukrainian death toll of 10 or more for that one attack.
- **Resolution criterion:** TRUE if, for one attack occurring between 2026-09-07 and 2026-09-27, the State Emergency Service of Ukraine or the Kyiv City Military Administration states a death toll of 10 or more for that attack, and Reuters or AFP carries that figure by 2026-09-30. Cumulative multi-day totals do not count.
- **Failure condition:** No individual Kyiv strike in the window reaches an officially stated toll of 10 or more dead.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-13
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-28, the Brent crude oil price will close above $105 per barrel on at least one weekday.
- **Resolution criterion:** The Brent crude oil price will close above $105 per barrel on at least one weekday between 2026-09-21 and 2026-09-28.
- **Failure condition:** The Brent crude oil price closes at or below $105 per barrel on every weekday between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-31
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-30
- **Domain:** disaster
- **Claim:** The confirmed death toll from the Virgo Transport 8 ferry capsizing in the Java Sea reaches at least 50 by 2026-09-27, per Basarnas or the Indonesian Ministry of Transportation.
- **Resolution criterion:** TRUE if Basarnas or the Indonesian Ministry of Transportation reports cumulative confirmed deaths of 50 or more on or before 2026-09-27; persons listed as missing do not count as confirmed deaths.
- **Failure condition:** Confirmed deaths reported by Basarnas or the Ministry of Transportation total fewer than 50 as of 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-02
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-30
- **Domain:** economics/markets
- **Claim:** Between 2026-09-25 and 2026-09-28, the 10-year U.S. Treasury yield exceeds 5.1% on at least one trading day, based on the official close from the U.S. Treasury.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 5.1% on at least one trading day between 2026-09-25 and 2026-09-28, as recorded by the U.S. Treasury's official daily yield data.
- **Failure condition:** The 10-year U.S. Treasury yield remains at or below 5.1% on all trading days between 2026-09-25 and 2026-09-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032014ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 2 business days in window; max BC_10YEAR 5.24 on 2026-09-28; threshold > 5.10; 2 day(s) satisfying

### KKR-20260920-40
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-09-30
- **Domain:** military/conflict
- **Claim:** Ukraine launches another single-wave strike of at least 100 drones toward the Moscow region between 2026-09-21 and 2026-09-28, matching the tempo of the 20 September attack described as the largest on Moscow to date.
- **Resolution criterion:** Two independently-biased channels (Russian, Ukrainian, or a wire service) report a single launch of at least 100 UAVs toward Moscow region between 2026-09-21 and 2026-09-28.
- **Failure condition:** No corroborated report describes a single-wave launch of 100 or more drones toward the Moscow region between 2026-09-21 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-43
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-09-30
- **Domain:** political
- **Claim:** Russia Central Election Commission official results confirm United Russia, party list plus single-mandate seats combined, retains an outright majority of State Duma seats following the election that concluded 20 September 2026, published by 2026-09-30.
- **Resolution criterion:** The Russian Central Election Commission (cikrf.ru) or a wire service reports United Russia holding more than 225 of 450 State Duma seats by 2026-09-30.
- **Failure condition:** Official or wire-corroborated results show United Russia holding 225 or fewer State Duma seats, or no results are published by 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-31
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-09-30
- **Domain:** crime_security
- **Claim:** NSW Police will announce an arrest in the shooting of the 11-year-old boy in Sydney, occurring between 2026-09-21 and 2026-09-28.
- **Resolution criterion:** True if NSW Police or a wire service (Guardian/BBC/AAP) reports an arrest in this case between 2026-09-21 and 2026-09-28.
- **Failure condition:** No arrest in this case is reported by NSW Police or wire services within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-32
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-09-30
- **Domain:** disaster_infrastructure
- **Claim:** Japanese authorities will confirm 10 or more fatalities from Typhoon Dujuan, for the period 2026-09-21 to 2026-09-28.
- **Resolution criterion:** True if Japan's FDMA, NHK, or a wire service (Kyodo/Reuters/AP) reports 10+ confirmed Dujuan-attributed deaths for that window.
- **Failure condition:** Confirmed Dujuan-attributed fatalities remain below 10 as of the deadline per Japanese authorities or wire reporting.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-23
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-10-01
- **Domain:** military_conflict
- **Claim:** Between 2026-08-17 and 2026-09-27, Ukrainian forces strike a Russian Black Sea port, oil terminal, or grain terminal, and both sides acknowledge the strike.
- **Resolution criterion:** A Russian regional governor or the Russian Defence Ministry and a Ukrainian military or intelligence source each describe a strike on a Russian Black Sea port facility occurring inside the window, carried by Reuters or AFP.
- **Failure condition:** No strike on a Russian Black Sea port facility inside the window draws acknowledgement from both a Russian and a Ukrainian official source.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-05
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** The S&P 500 index closes below 7,500.00 on at least one trading day between 2026-09-21 and 2026-09-28.
- **Resolution criterion:** The closing value of the S&P 500 index, as reported by the Federal Reserve Economic Data (FRED) or a major exchange, is below 7,500.00 on at least one trading day between 2026-09-21 and 2026-09-28.
- **Failure condition:** The S&P 500 index never closes below 7,500.00 on any trading day within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-93
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-01
- **Domain:** crime_security
- **Claim:** Victoria Police announce the arrest, charging, or confirmed death of the man sought over the alleged axe attack in Victoria, occurring between 2026-09-07 and 2026-09-27.
- **Resolution criterion:** TRUE if a Victoria Police media release or court listing, reported by two of ABC News, The Age, and Guardian Australia, records the suspect arrested, charged, or confirmed deceased within the window.
- **Failure condition:** The suspect remains at large and uncharged at the close of 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-02
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new political party in Germany gains more than 10% of the vote in a regional election, as confirmed by official election results from the German Federal Returning Officer.
- **Resolution criterion:** The German Federal Returning Officer publishes official election results showing a new political party receiving more than 10% of the vote in a regional election between 2026-09-21 and 2026-09-24.
- **Failure condition:** No new party receives over 10% of the vote in any regional election during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-16
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** CVE-2026-75650, the Adobe Commerce and Magento Open Source remote code execution flaw Adobe confirmed as actively exploited on 2026-09-08, is added to the CISA Known Exploited Vulnerabilities catalog between 2026-09-08 and 2026-09-29.
- **Resolution criterion:** The CISA KEV catalog lists CVE-2026-75650 with a dateAdded value between 2026-09-08 and 2026-09-29 inclusive.
- **Failure condition:** CVE-2026-75650 is absent from the CISA KEV catalog as of 2026-10-01, or its dateAdded value falls after 2026-09-29.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032016ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-75650'] with dateAdded in [2026-09-08..2026-09-29] across 1733 catalog rows - CVE-2026-75650

### KKR-20260908-19
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-01
- **Domain:** disaster_infrastructure
- **Claim:** A named humanitarian body publicly reports the closure or suspension of services at one or more specific Sudanese hospitals due to healthcare system collapse, between 2026-09-08 and 2026-09-29.
- **Resolution criterion:** MSF, WHO, or another named humanitarian or UN body states in public reporting that a specific named Sudanese hospital or facility suspended or ceased operating due to collapse, within the window.
- **Failure condition:** No named humanitarian body reports a specific hospital or facility closure in Sudan tied to system collapse by 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-01
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the European Central Bank will raise interest rates to 2.5%.
- **Resolution criterion:** The European Central Bank announces a rate hike to 2.5% during the event window.
- **Failure condition:** The European Central Bank does not announce a rate hike to 2.5% between 2026-09-21 and 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-02
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-20 and 2026-09-27, a cyberattack exploiting a vulnerability in a major cloud provider's API is confirmed by CISA KEV and two independent security firms.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-20 and 2026-09-27 for a vulnerability exploited in a cloud provider's API, with two independent security firms reporting the exploit.
- **Failure condition:** No entry in the CISA KEV catalog between 2026-09-20 and 2026-09-27 for a cloud API vulnerability, or no independent confirmation from two security firms.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-06
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** Between 2026-09-20 and 2026-09-27, the price of Brent crude oil exceeds $110 per barrel on at least two consecutive trading days, as verified by the FRED database.
- **Resolution criterion:** The FRED database shows Brent crude oil exceeding $110 per barrel on two or more consecutive trading days between 2026-09-20 and 2026-09-27.
- **Failure condition:** Brent crude oil fails to exceed $110 per barrel on any two consecutive trading days between 2026-09-20 and 2026-09-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-03
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-09-29, Iran announces a formal closure of the Strait of Hormuz to foreign shipping, as confirmed by a statement from the Iranian Foreign Ministry and at least two independent news outlets.
- **Resolution criterion:** A statement from the Iranian Foreign Ministry, published between 2026-09-26 and 2026-09-29, confirms the closure of the Strait of Hormuz to foreign shipping, and at least two independent news outlets (e.g., BBC, Al Jazeera, Guardian) report the closure.
- **Failure condition:** No official statement from the Iranian Foreign Ministry confirms a closure of the Strait of Hormuz, and no independent news outlet reports such a closure.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-09
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-15 and 2026-09-22, at least one major cyberattack exploiting CVE-2026-76461 will be confirmed by two independent sources.
- **Resolution criterion:** At least one confirmed cyberattack exploiting CVE-2026-76461 is reported by two or more independent sources (e.g., BleepingComputer, The Hacker News, CISA Advisories) with distinct reporting channels.
- **Failure condition:** No cyberattack exploiting CVE-2026-76461 is confirmed by two or more independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-01
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** On 2026-09-17, the CISA KEV catalog will include CVE-2026-58704 with a date-added value of 2026-09-16.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value of 2026-09-16 for CVE-2026-58704.
- **Failure condition:** The CISA KEV catalog does not list CVE-2026-58704 with a date-added value of 2026-09-16.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032019ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-58704'] with dateAdded in [2026-09-16..2026-09-17] across 1733 catalog rows - CVE-2026-58704

### KKR-20260918-01
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year Treasury yield will exceed 5.05 percent at the close of any trading day.
- **Resolution criterion:** The 10-year Treasury yield exceeds 5.05 percent at the close of any trading day between 2026-09-21 and 2026-09-24.
- **Failure condition:** The 10-year Treasury yield never exceeds 5.05 percent at the close of any trading day during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032020ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.05; 2 day(s) satisfying

### KKR-20260918-08
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Between 2026-09-18 and 2026-09-25, no reported casualties will be confirmed in any military or conflict event in the Russia-Ukraine Theatre.
- **Resolution criterion:** No third-party corroboration from at least two independent sources (e.g., BBC World, Al Jazeera, Reuters) confirms any casualties in any event in the Russia-Ukraine Theatre between 2026-09-18 and 2026-09-25.
- **Failure condition:** At least one third-party source confirms casualties in any event in the Russia-Ukraine Theatre during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-10
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-18 and 2026-09-25, a cyberattack exploiting CVE-2025-39964 will be confirmed by at least two independent sources.
- **Resolution criterion:** At least two independent sources (e.g., BleepingComputer, The Hacker News, CISA Advisories) confirm a cyberattack exploiting CVE-2025-39964 between 2026-09-18 and 2026-09-25.
- **Failure condition:** No independent source confirms a cyberattack exploiting CVE-2025-39964 during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-11
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** disaster
- **Claim:** Between 2026-09-18 and 2026-09-25, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in any region.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.5 or higher earthquake in any region between 2026-09-18 and 2026-09-25.
- **Failure condition:** The USGS Significant Quakes catalog does not record any magnitude 6.5 or higher earthquake during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-12
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Between 2026-09-18 and 2026-09-25, a new political scandal involving a U.S. federal official will be confirmed by at least two independent sources.
- **Resolution criterion:** At least two independent sources (e.g., Guardian World, CNBC Top News, NPR News) confirm a new political scandal involving a U.S. federal official between 2026-09-18 and 2026-09-25.
- **Failure condition:** No independent source confirms a new political scandal involving a U.S. federal official during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-13
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-18 and 2026-09-25, a new cyberattack targeting Microsoft 365 will be confirmed by at least two independent sources.
- **Resolution criterion:** At least two independent sources (e.g., BleepingComputer, The Hacker News) confirm a new cyberattack targeting Microsoft 365 between 2026-09-18 and 2026-09-25.
- **Failure condition:** No independent source confirms a new cyberattack targeting Microsoft 365 during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-14
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** disaster
- **Claim:** Between 2026-09-18 and 2026-09-25, a new flood warning will be issued by the USGS or GDACS for a region in the United States.
- **Resolution criterion:** The USGS Significant Quakes or GDACS Alerts catalog issues a new flood warning for a region in the United States between 2026-09-18 and 2026-09-25.
- **Failure condition:** No new flood warning for a U.S. region is issued by USGS or GDACS during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-15
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Between 2026-09-18 and 2026-09-25, a new political resignation or indictment involving a senior official in the European Union will be confirmed by at least two independent sources.
- **Resolution criterion:** At least two independent sources (e.g., Guardian World, BBC World, Al Jazeera) confirm a new political resignation or indictment involving a senior EU official between 2026-09-18 and 2026-09-25.
- **Failure condition:** No independent source confirms a new political resignation or indictment involving a senior EU official during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-01
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, the USGS Significant Quakes catalog will record a magnitude 6.5 or higher earthquake in the Kermadec Islands Region.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.5 or higher earthquake in the Kermadec Islands Region with a date within the event window.
- **Failure condition:** No magnitude 6.5 or higher earthquake is recorded in the Kermadec Islands Region in the USGS Significant Quakes catalog during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-02
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, at least one drone strike will be reported in Kyiv, Ukraine, with a corroborated report from both Russian and Ukrainian sources.
- **Resolution criterion:** At least one drone strike is reported in Kyiv, Ukraine, with a corroborated report from both Russian and Ukrainian sources during the event window.
- **Failure condition:** No drone strike is reported in Kyiv with corroborating reports from both Russian and Ukrainian sources during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-03
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** Between 2026-09-21 and 2026-09-24, the 10-year U.S. Treasury yield will exceed 5.10 percent at market close on at least one day.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 5.10 percent at market close on at least one day between 2026-09-21 and 2026-09-24.
- **Failure condition:** The 10-year U.S. Treasury yield never exceeds 5.10 percent at market close during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032021ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.10; 2 day(s) satisfying

### KKR-20260919-04
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a new exploit for CVE-2026-53266 will be publicly disclosed in a security advisory.
- **Resolution criterion:** A new public exploit for CVE-2026-53266 is disclosed in a security advisory between 2026-09-21 and 2026-09-24.
- **Failure condition:** No new public exploit for CVE-2026-53266 is disclosed in a security advisory during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-05
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, the European Union will issue a public statement urging the United States to lift the travel ban on the Palestinian delegation to the UN General Assembly.
- **Resolution criterion:** The European Union issues a public statement urging the United States to lift the travel ban on the Palestinian delegation to the UN General Assembly between 2026-09-21 and 2026-09-24.
- **Failure condition:** The European Union does not issue a public statement urging the U.S. to lift the travel ban on the Palestinian delegation during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-06
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** crime/security
- **Claim:** Between 2026-09-21 and 2026-09-24, Saudi Arabia will issue a second air raid alert for Riyadh, confirmed by at least two independent news outlets.
- **Resolution criterion:** Saudi Arabia issues a second air raid alert for Riyadh, confirmed by at least two independent news outlets between 2026-09-21 and 2026-09-24.
- **Failure condition:** Saudi Arabia does not issue a second air raid alert for Riyadh confirmed by at least two independent news outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-07
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a major cyberattack exploiting the Orkes Conductor Workflow Platform vulnerability (CVE-2025-39964) will be confirmed by CISA.
- **Resolution criterion:** CISA confirms a major cyberattack exploiting CVE-2025-39964 in the Orkes Conductor Workflow Platform between 2026-09-21 and 2026-09-24.
- **Failure condition:** CISA does not confirm a major cyberattack exploiting CVE-2025-39964 during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-08
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, the U.S. and Denmark will publicly announce the implementation of a new military presence in Greenland under the security deal.
- **Resolution criterion:** The U.S. and Denmark publicly announce the implementation of a new military presence in Greenland under the security deal between 2026-09-21 and 2026-09-24.
- **Failure condition:** The U.S. and Denmark do not publicly announce the implementation of a new military presence in Greenland during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-01
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Moscow was struck by a drone attack between 2026-09-21 and 2026-09-24, resulting in at least one confirmed casualty.
- **Resolution criterion:** At least one confirmed casualty from a drone attack on Moscow is reported by at least two independent, non-aligned news outlets (e.g., BBC, Al Jazeera, Reuters, AP) between 2026-09-21 and 2026-09-24.
- **Failure condition:** No report from at least two independent, non-aligned outlets confirms a drone attack on Moscow with at least one casualty during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-03
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Iran announces a new condition for ending its war with the U.S. between 2026-09-21 and 2026-09-24, confirmed by at least two independent news outlets.
- **Resolution criterion:** At least two independent, non-aligned news outlets (e.g., Al Jazeera, BBC, Reuters) report that Iran has announced a new condition for ending its war with the U.S. between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such announcement is confirmed by at least two independent, non-aligned news outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-04
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** A cyberattack targeting a U.S. federal agency is confirmed by CISA KEV between 2026-09-21 and 2026-09-24, with a public advisory issued.
- **Resolution criterion:** The CISA KEV catalog contains a new entry with a date-added value between 2026-09-21 and 2026-09-24, explicitly linking a vulnerability to a confirmed cyberattack on a U.S. federal agency.
- **Failure condition:** No such entry is added to the CISA KEV catalog during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-05
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** disaster
- **Claim:** A tropical cyclone with Category 3 or higher intensity makes landfall in the U.S. between 2026-09-21 and 2026-09-24, confirmed by the National Hurricane Center.
- **Resolution criterion:** The National Hurricane Center (NHC) issues a landfall advisory for a tropical cyclone with sustained winds of at least 111 mph (Category 3 or higher) in the United States between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such landfall advisory is issued by the NHC during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-06
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** A major offensive operation begins in the Gaza Strip between 2026-09-21 and 2026-09-24, confirmed by at least two independent news outlets.
- **Resolution criterion:** At least two independent, non-aligned news outlets (e.g., Al Jazeera, BBC, Reuters) report that a major offensive operation has begun in the Gaza Strip between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such report is confirmed by at least two independent, non-aligned outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-08
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-01
- **Domain:** cyber
- **Claim:** A new cyberattack on a critical infrastructure system in Europe is confirmed by the EU Agency for Cybersecurity (ENISA) between 2026-09-21 and 2026-09-24.
- **Resolution criterion:** ENISA issues a public advisory confirming a cyberattack on a critical infrastructure system in Europe between 2026-09-21 and 2026-09-24, with the event date within that window.
- **Failure condition:** No such advisory is issued by ENISA during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-09
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-01
- **Domain:** economics/markets
- **Claim:** On or before 2026-09-26, the U.S. Federal Reserve will announce a 25 basis point increase in the federal funds rate, as confirmed by the Federal Reserve's official press release.
- **Resolution criterion:** The Federal Reserve's official press release confirms a 25 basis point increase in the federal funds rate on or before 2026-09-26.
- **Failure condition:** The Federal Reserve does not issue a press release confirming a rate hike by 2026-09-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-14
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-01
- **Domain:** political
- **Claim:** Donald Trump and Masoud Pezeshkian meet in person between 2026-09-22 and 2026-09-29, when both are expected in New York for the UN General Assembly high-level week.
- **Resolution criterion:** TRUE if the White House or Iranian presidency confirms, or two of Reuters, AP and AFP report, a face-to-face Trump-Pezeshkian meeting held between 2026-09-22 and 2026-09-29. Phone calls, passing handshakes and intermediary talks do not count.
- **Failure condition:** Trump and Pezeshkian do not meet face to face at any point between 2026-09-22 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-47
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-01
- **Domain:** military/conflict
- **Claim:** Iranian President Pezeshkian delivers a speech in person at the UN General Assembly general debate in New York between 2026-09-22 and 2026-09-29.
- **Resolution criterion:** UN Web TV archive or UN Journal lists Pezeshkian speaking in person in the General Assembly Hall on a date 2026-09-22 through 2026-09-29.
- **Failure condition:** Pezeshkian does not appear in person at the UNGA general debate in the window, including a remote address or substitution by another official.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-19
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-02
- **Domain:** economic
- **Claim:** Front-month Brent crude settles at or below 75.00 US dollars per barrel on at least one trading day between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** True if front-month Brent futures post a settlement price at or below 75.00 US dollars per barrel on any trading day between 2026-08-10 and 2026-09-30.
- **Failure condition:** Every Brent front-month settlement in the window prints above 75.00 US dollars.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-21
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** CISA adds a CVE affecting N-able N-central to the Known Exploited Vulnerabilities catalog between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** True if the CISA KEV catalog contains an entry for a CVE in N-able N-central carrying a date-added value between 2026-08-10 and 2026-09-30.
- **Failure condition:** No N-able N-central CVE receives a KEV date-added value inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032022ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['N-able N-central'] with dateAdded in [2026-08-10..2026-09-30] across 1733 catalog rows - CVE-2026-86218

### KKR-20260804-22
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The UK Information Commissioners Office confirms a formal investigation or enforcement action over the PNLD breach between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** True if the ICO publishes a statement, case page, or enforcement notice confirming formal investigation or enforcement action regarding the PNLD breach, dated within the window.
- **Failure condition:** The ICO opens no formal investigation or enforcement action on PNLD in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-23
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** The US Senate confirms Todd Blanche as Attorney General between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** True if the Senate roll call record shows a confirmation vote approving Todd Blanche as Attorney General on a date between 2026-08-10 and 2026-09-30.
- **Failure condition:** No successful Senate confirmation vote on Blanche occurs within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-58
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-02
- **Domain:** economic
- **Claim:** The S&P 500 closes down 3.00 percent or more from the prior close on at least one session between 2026-08-05 and 2026-09-30.
- **Resolution criterion:** TRUE if official S&P 500 closing values show a single-session close-to-close decline of 3.00 percent or greater on any date between 2026-08-05 and 2026-09-30.
- **Failure condition:** No session in the window produces an S&P 500 close-to-close decline of 3.00 percent or more.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260807-05
- **Issued:** 2026-08-07  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** The US Senate confirms Todd Blanche as Attorney General by recorded roll call vote between 2026-08-07 and 2026-09-30.
- **Resolution criterion:** Congress.gov or senate.gov roll call record shows a Senate vote confirming Todd Blanche as United States Attorney General with a vote date between 2026-08-07 and 2026-09-30.
- **Failure condition:** The Senate holds no confirming vote on Blanche on or before 2026-09-30, whether through withdrawal of the nomination, failed cloture, or the vote never being scheduled.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260808-14
- **Issued:** 2026-08-08  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** A continuing appropriations act extending US federal funding past 2026-09-30 is enacted into law between 2026-08-09 and 2026-09-30.
- **Resolution criterion:** Congress.gov shows a continuing appropriations measure with status Became Public Law, enactment date between 2026-08-09 and 2026-09-30, funding agencies beyond 2026-09-30.
- **Failure condition:** No such measure carries Became Public Law status with an enactment date inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260808-16
- **Issued:** 2026-08-08  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** CISA adds at least 25 distinct CVE records to the Known Exploited Vulnerabilities catalog with date-added values between 2026-08-10 and 2026-09-30.
- **Resolution criterion:** Count of distinct cveID entries in the CISA KEV catalog with dateAdded between 2026-08-10 and 2026-09-30 inclusive is 25 or greater.
- **Failure condition:** That count is 24 or fewer.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260811-12
- **Issued:** 2026-08-11  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** NYMEX WTI crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-12 and 2026-09-30.
- **Resolution criterion:** TRUE if CME official settlement data show the WTI front-month contract settling at or above 100.00 USD on any trading day between 2026-08-12 and 2026-09-30.
- **Failure condition:** Every WTI front-month official settlement in the window is below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260811-22
- **Issued:** 2026-08-11  ·  **Deadline:** 2026-10-02
- **Domain:** economics
- **Claim:** NYMEX front-month WTI crude futures settle at or above 95.00 US dollars per barrel on at least one trading day between 2026-08-12 and 2026-09-30.
- **Resolution criterion:** TRUE if the CME published settlement price for the front-month WTI contract is 95.00 or higher on any trading day between 2026-08-12 and 2026-09-30 inclusive.
- **Failure condition:** Every front-month WTI settlement inside the window prints below 95.00 dollars.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260812-05
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** At least one attack on a commercial vessel occurs in the Red Sea, Bab el-Mandeb, or Gulf of Aden between 2026-08-13 and 2026-09-30.
- **Resolution criterion:** TRUE if UKMTO or US CENTCOM publicly reports at least one attack on a commercial vessel in the Red Sea, Bab el-Mandeb, or Gulf of Aden occurring between 2026-08-13 and 2026-09-30.
- **Failure condition:** No attack on a commercial vessel occurs in the Red Sea, Bab el-Mandeb, or Gulf of Aden between 2026-08-13 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260812-07
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** A Microsoft Defender vulnerability is added to the CISA KEV catalog with a date-added value between 2026-08-13 and 2026-09-30.
- **Resolution criterion:** TRUE if the CISA KEV catalog contains an entry whose product field names Microsoft Defender with dateAdded between 2026-08-13 and 2026-09-30 inclusive.
- **Failure condition:** The CISA KEV catalog contains no Microsoft Defender entry with dateAdded between 2026-08-13 and 2026-09-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032025ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Microsoft Defender'] with dateAdded in [2026-08-13..2026-09-30] across 1733 catalog rows

### KKR-20260813-08
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose affected product is Microsoft SharePoint, with a dateAdded value between 2026-08-14 and 2026-09-30.
- **Resolution criterion:** TRUE if a fetch of the CISA KEV JSON at the deadline shows any Microsoft SharePoint entry with dateAdded between 2026-08-14 and 2026-09-30 inclusive; otherwise FALSE.
- **Failure condition:** The KEV catalog fetched at the deadline contains no Microsoft SharePoint entry with a dateAdded value inside the 2026-08-14 to 2026-09-30 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-11
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** At least one reactor unit at Romania's Cernavoda nuclear plant records nonzero electricity output on the ENTSO-E transparency platform on at least one day between 2026-08-14 and 2026-09-30.
- **Resolution criterion:** TRUE if ENTSO-E actual generation per generation unit shows output above 0 MW for any Cernavoda unit on any date between 2026-08-14 and 2026-09-30; otherwise FALSE.
- **Failure condition:** ENTSO-E per-unit generation data show zero output from every Cernavoda unit on every day of the 2026-08-14 to 2026-09-30 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-05
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-02
- **Domain:** crime/security
- **Claim:** Authorities announce the arrest or charging of at least one suspect in the 2026-08-15 Virginia State shooting in which five people were shot, between 2026-08-17 and 2026-09-30.
- **Resolution criterion:** True if a law enforcement agency publicly announces an arrest or charges in the 2026-08-15 Virginia State five-victim shooting, reported by at least one national outlet, by 2026-09-30.
- **Failure condition:** No arrest or charges connected to the 2026-08-15 Virginia State shooting are announced by 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-55
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** Between 2026-08-18 and 2026-09-30 the United States conducts a military strike on targets inside the territory of Oman.
- **Resolution criterion:** True if at least two of Reuters, AP, AFP, or BBC report a US military strike on targets inside Omani territory occurring between 2026-08-18 and 2026-09-30.
- **Failure condition:** No US military strike on Omani territory occurs within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-10
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** United States forces conduct military strikes on targets inside Iranian territory between 2026-08-19 and 2026-09-30.
- **Resolution criterion:** The US Department of Defense or the President announces US strikes on targets inside Iran conducted between 2026-08-19 and 2026-09-30, and Iranian state media acknowledge strikes occurred.
- **Failure condition:** The window closes with no US military strike conducted against targets inside Iranian territory.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-06
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** CISA adds at least one new Microsoft-product vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-08-20 and 2026-09-30.
- **Resolution criterion:** The CISA KEV JSON feed contains at least one entry with vendorProject Microsoft and dateAdded between 2026-08-20 and 2026-09-30 inclusive; zero such entries grades MISS.
- **Failure condition:** No Microsoft entry with dateAdded in the 2026-08-20 to 2026-09-30 range exists in the KEV catalog at the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-01
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant-maturity yield (FRED series DGS10, 4.65 on 2026-08-19 after a 20-month high near 4.75 that week) records a daily value of 5.00 percent or higher on at least one day between 2026-08-24 and 2026-09-30.
- **Resolution criterion:** FRED series DGS10 shows at least one observation dated 2026-08-24 through 2026-09-30 inclusive with a value of 5.00 or greater.
- **Failure condition:** Every DGS10 observation dated 2026-08-24 through 2026-09-30 is below 5.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260825-14
- **Issued:** 2026-08-25  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** A New York state court issues any order or ruling, including on a preliminary motion, in the business-group lawsuit against the city-owned grocery store initiative, between 2026-08-26 and 2026-09-30.
- **Resolution criterion:** TRUE if the case docket in the New York court e-filing system shows a judicial order or ruling entered between 2026-08-26 and 2026-09-30 in this case; FALSE if no order is entered.
- **Failure condition:** The court docket shows no order or ruling entered in the case inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-01
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-63520, the Microsoft SharePoint Business Connectivity Services remote code execution flaw that completes the chain with CVE-2026-55040, to the Known Exploited Vulnerabilities catalog between 2026-08-27 and 2026-09-30.
- **Resolution criterion:** The CISA KEV JSON feed contains an entry for CVE-2026-63520 whose dateAdded value falls between 2026-08-27 and 2026-09-30 inclusive; otherwise false.
- **Failure condition:** The KEV catalog carries no entry for CVE-2026-63520, or the entry has a dateAdded outside 2026-08-27 through 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-04
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** United States and Iranian officials at the level of secretary of state, foreign minister, or presidential special envoy meet face to face for a negotiating session between 2026-08-27 and 2026-09-30, and both governments acknowledge the meeting.
- **Resolution criterion:** Both the US State Department or White House and the Iranian Foreign Ministry publicly confirm a face to face US-Iran session at that level held between 2026-08-27 and 2026-09-30; mediated exchanges through third parties do not count.
- **Failure condition:** No face to face US-Iran session at secretary of state, foreign minister, or special envoy level takes place between 2026-08-27 and 2026-09-30, or only one government acknowledges it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-08
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** The Kremlin or the White House will confirm a direct, in-person meeting between the CIA Director and Vladimir Putin, following the CIA Director's Russia visit reported 2026-08-26 in which the Kremlin said meetings involved Russian intelligence officials but not Putin, between 2026-08-27 and 2026-09-30.
- **Resolution criterion:** Peskov, the Kremlin press service, or the White House confirms a direct CIA Director-Putin meeting, dated between 2026-08-27 and 2026-09-30, per at least two of Reuters, AP, TASS, or Al Jazeera.
- **Failure condition:** No confirmed direct CIA Director-Putin meeting is on record by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-68
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** Nvidia or Hugging Face officially confirms a definitive agreement for Nvidia to acquire Hugging Face between 2026-08-27 and 2026-09-30.
- **Resolution criterion:** A press release, SEC filing by NVIDIA Corp, or official company blog post dated between 2026-08-27 and 2026-09-30 states that Nvidia has entered a definitive agreement to acquire Hugging Face.
- **Failure condition:** Neither company has issued an official confirmation of a definitive acquisition agreement dated inside the window, or either company states the talks ended without agreement.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-71
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** Official confirmed deaths from the 2026-08-26 Bhotekoshi-Trishuli flash flood, Nepal and Tibet combined, reach at least 1,000 by 2026-09-30.
- **Resolution criterion:** Reuters, AP, or AFP reports that official confirmed deaths from the 2026-08-26 flood, Nepal police or NDRRMA figures plus Chinese official figures for Gyirong county, total at least 1,000 as of a date no later than 2026-09-30.
- **Failure condition:** Combined official confirmed deaths remain below 1,000 in every wire-service report dated on or before 2026-09-30; missing or presumed-dead counts do not count.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-74
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** UKMTO publishes at least three separate incident reports of merchant vessels struck by a projectile, mine, or other weapon in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-08-28 and 2026-09-30.
- **Resolution criterion:** The UKMTO incidents page (ukmto.org) lists at least three distinct incident references dated 2026-08-28 to 2026-09-30, each stating a vessel was struck, hit, or impacted in the Strait of Hormuz, Gulf of Oman, or Persian Gulf.
- **Failure condition:** Fewer than three distinct UKMTO incident reports dated inside the window describe a vessel actually struck; approaches, warnings, and boardings do not count.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-03
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** A major earthquake with magnitude 6.5 or higher will be recorded by USGS in the Pacific Northwest between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** The USGS Significant Quakes feed records one or more events with magnitude ≥6.5 in the Pacific Northwest region between 2026-09-01 and 2026-09-30.
- **Failure condition:** The USGS Significant Quakes feed records no events with magnitude ≥6.5 in the Pacific Northwest region between 2026-09-01 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-04
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** The S&P 500 will close above 7,800 on at least one weekday between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** The S&P 500 closes at or above 7,800 on at least one weekday between 2026-09-01 and 2026-09-30, as reported by MarketWatch.
- **Failure condition:** The S&P 500 never closes at or above 7,800 on any weekday between 2026-09-01 and 2026-09-30, as reported by MarketWatch.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-06
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** The 10-year U.S. Treasury yield will exceed 4.8% on at least one weekday between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 4.8% on at least one weekday between 2026-09-01 and 2026-09-30, as reported by CNBC.
- **Failure condition:** The 10-year U.S. Treasury yield never exceeds 4.8% on any weekday between 2026-09-01 and 2026-09-30, as reported by CNBC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T032028ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 21 business days in window; max BC_10YEAR 5.29 on 2026-09-30; threshold > 4.80; 16 day(s) satisfying

### KKR-20260829-08
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** The European Union will report gas storage levels below 30% of capacity on at least one weekday between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** The Guardian Business reports that EU gas storage levels are below 30% of capacity on at least one weekday between 2026-09-01 and 2026-09-30.
- **Failure condition:** Guardian Business reports no weekday between 2026-09-01 and 2026-09-30 where EU gas storage levels are below 30% of capacity.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-10
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** Russian forces conduct at least one drone or missile strike on Kyiv between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** At least two of Reuters, AP, AFP, or BBC report a Russian drone or missile strike on Kyiv occurring between 2026-09-01 and 2026-09-30.
- **Failure condition:** No Russian drone or missile strike on Kyiv occurs at any point between 2026-09-01 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-14
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** The barrier lake at the Nepal-China border produces a further outburst or overflow causing new evacuations, damage, or deaths between 2026-08-29 and 2026-09-30.
- **Resolution criterion:** At least two of BBC, Guardian, Al Jazeera, Reuters, or AP report a new outburst or overflow from the Nepal-China barrier lake between 2026-08-29 and 2026-09-30 causing fresh evacuations, damage, or deaths.
- **Failure condition:** The barrier lake produces no further outburst or overflow causing evacuations, damage, or deaths during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-39
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** A PaperCut vulnerability is added to the CISA KEV catalog with a dateAdded value between 2026-08-29 and 2026-09-30.
- **Resolution criterion:** The CISA KEV catalog JSON contains at least one entry naming PaperCut with dateAdded between 2026-08-29 and 2026-09-30 inclusive.
- **Failure condition:** The KEV catalog fetched at the deadline contains no PaperCut entry with dateAdded inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032030ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['PaperCut'] with dateAdded in [2026-08-29..2026-09-30] across 1733 catalog rows - CVE-2026-81578, CVE-2026-82078

### KKR-20260831-75
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-02
- **Domain:** military_conflict
- **Claim:** A further attempt to seize power from Niger's sitting government by military or paramilitary action occurs between 2026-09-01 and 2026-09-30.
- **Resolution criterion:** Resolves true if AP, Reuters, AFP, or Niger state media report a further attempted seizure of power against the sitting government within the window; false if no such attempt is reported.
- **Failure condition:** No wire-service or Niger state-media report of a further coup attempt against the sitting government appears between 2026-09-01 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-21
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** WTI crude oil front-month futures settle at or above 95.00 USD per barrel on any trading day between 2026-09-02 and 2026-09-30. Reference: 88.02 USD per barrel on the packet date, 2026-09-01.
- **Resolution criterion:** TRUE if the NYMEX WTI front-month settlement price closes at or above 95.00 USD per barrel on any trading day from 2026-09-02 through 2026-09-30 inclusive, per EIA or NYMEX settlement data. FALSE otherwise.
- **Failure condition:** The WTI front-month settlement price never closes at or above 95.00 USD per barrel on any trading day in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-06
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** Between 2026-09-02 and 2026-09-30, CISA adds at least one Microsoft Exchange Server vulnerability to the Known Exploited Vulnerabilities catalog.
- **Resolution criterion:** True if the CISA KEV catalog JSON contains at least one entry with vendorProject Microsoft, product containing Exchange, and dateAdded between 2026-09-02 and 2026-09-30 inclusive.
- **Failure condition:** No KEV entry for a Microsoft Exchange Server product carries a dateAdded value between 2026-09-02 and 2026-09-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032033ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 3 matching entries for ['Microsoft', 'Exchange'] with dateAdded in [2026-09-02..2026-09-30] across 1733 catalog rows - CVE-2026-65660, CVE-2026-81963, CVE-2026-85880

### KKR-20260902-07
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-02
- **Domain:** crime/security
- **Claim:** Between 2026-09-01 and 2026-09-30, the [withheld] Fourth District Court orders Tyler Robinson bound over for trial on the aggravated murder charge in the killing of Charlie Kirk.
- **Resolution criterion:** True if the [withheld] Fourth District Court docket, or the [withheld] County Attorney office, records a bindover order on the aggravated murder count dated 2026-09-01 through 2026-09-30; dismissal of that count or no ruling by 2026-09-30 resolves false.
- **Failure condition:** No bindover order on the aggravated murder count against Tyler Robinson is entered between 2026-09-01 and 2026-09-30, whether because the count is dismissed or the ruling is delayed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-44
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendor or product fields reference SonicWall SMA1000, with a dateAdded value between 2026-09-03 and 2026-09-30.
- **Resolution criterion:** A fetch of the CISA KEV catalog on the deadline shows at least one SMA1000 entry with dateAdded between 2026-09-03 and 2026-09-30 inclusive.
- **Failure condition:** No KEV entry referencing SonicWall SMA1000 carries a dateAdded value inside the 2026-09-03 to 2026-09-30 window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032036ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SMA1000'] with dateAdded in [2026-09-03..2026-09-30] across 1733 catalog rows

### KKR-20260902-57
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-02
- **Domain:** economic
- **Claim:** WTI crude oil, NYMEX front-month contract, settles at or above 100.00 USD per barrel on any trading day between 2026-09-03 and 2026-09-30. Reference: 90.59 USD per barrel on the packet date, 2026-09-02.
- **Resolution criterion:** TRUE if CME/NYMEX settlement data or EIA daily spot price shows WTI at or above 100.00 USD per barrel on any date in the window; FALSE if no such settlement occurs.
- **Failure condition:** WTI settlement data shows no daily close at or above 100.00 USD per barrel at any point in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-31
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** CISA adds at least one CVE whose KEV vendorProject or product field names Elementor to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-09-03 and 2026-09-30.
- **Resolution criterion:** The CISA KEV JSON feed (cisa.gov known-exploited-vulnerabilities.json) contains an entry whose vendorProject or product field includes Elementor and whose dateAdded is from 2026-09-03 through 2026-09-30 inclusive.
- **Failure condition:** No KEV entry with dateAdded between 2026-09-03 and 2026-09-30 names Elementor in its vendorProject or product field.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-14
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** US forces conduct at least one additional military strike on Iranian military, IRGC, or Iranian state-owned assets between 2026-09-06 and 2026-09-30, following the 2026-09-05 strikes on three Iranian oil tankers.
- **Resolution criterion:** At least two of Reuters, AP, BBC, Al Jazeera report a US strike on Iranian military, IRGC, or state-owned assets occurring between 2026-09-06 and 2026-09-30.
- **Failure condition:** No US strike on Iranian military, IRGC, or Iranian state-owned assets occurs between 2026-09-06 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-24
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** The Israeli military conducts at least one airstrike inside Beirut municipality or its southern suburbs (Dahiyeh) between 2026-09-08 and 2026-09-30.
- **Resolution criterion:** An IDF statement claims a strike inside Beirut municipality or Dahiyeh (Haret Hreik, Burj al-Barajneh, Ghobeiry, Chiyah, Laylaki) and the Lebanese National News Agency reports the same strike, both dated 2026-09-08 to 2026-09-30. Strikes elsewhere do not count.
- **Failure condition:** No Israeli airstrike hits Beirut municipality or Dahiyeh at any time from 2026-09-08 through 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-26
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-75650, the Adobe Commerce and Magento Open Source StyleSmuggler flaw patched 2026-09-07, with a dateAdded value between 2026-09-08 and 2026-09-29.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed at the deadline contains an entry with cveID CVE-2026-75650 and dateAdded between 2026-09-08 and 2026-09-29 inclusive; FALSE otherwise.
- **Failure condition:** At the deadline the KEV catalog carries no entry for CVE-2026-75650 with a dateAdded on or before 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260908-29
- **Issued:** 2026-09-08  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** Between 2026-09-08 and 2026-09-30, the Russian Ministry of Foreign Affairs announces that at least one Hungarian diplomat is expelled from Russia or declared persona non grata, following the Hungarian expulsion of 10 Russian diplomats reported 2026-09-08.
- **Resolution criterion:** TRUE if a Russian MFA statement dated 2026-09-08 through 2026-09-30 announces expulsion or persona non grata status for at least one Hungarian diplomat, and Reuters or AFP reports it; FALSE otherwise.
- **Failure condition:** No Hungarian diplomat is expelled from Russia or declared persona non grata by the Russian MFA on any date from 2026-09-08 through 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-09
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The Chrome V8 zero-day reported on 2026-09-09 as exploited in the wild and enabling code execution will be added to the CISA Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-10 and 2026-09-30.
- **Resolution criterion:** The CISA KEV catalog at cisa.gov/known-exploited-vulnerabilities-catalog carries an entry for a Google Chrome or Chromium V8 vulnerability with a date-added value between 2026-09-10 and 2026-09-30 inclusive; checked 2026-10-02.
- **Failure condition:** MISS if no Chrome or Chromium V8 entry appears in the CISA KEV catalog with a date-added value inside the window by the check date.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032039ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Google Chrome', 'Chromium V8'] with dateAdded in [2026-09-10..2026-09-30] across 1733 catalog rows

### KKR-20260912-27
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-02
- **Domain:** economics/markets
- **Claim:** Between 2026-09-12 and 2026-09-30, Saudi Arabia publicly announces through its Energy Ministry, Saudi Aramco, or SPA that crude oil is again flowing through the East-West pipeline from Abqaiq to Yanbu, which was shut on 2026-09-11 after drone attacks launched from Iraq.
- **Resolution criterion:** A Saudi Energy Ministry, Saudi Aramco, or SPA statement dated 2026-09-12 to 2026-09-30 says East-West pipeline crude flows have resumed, or Reuters and Bloomberg both report resumption within that window citing Saudi officials or Aramco.
- **Failure condition:** The East-West pipeline remains shut through 2026-09-30, with no resumption of crude flows announced by Saudi authorities or confirmed by both named wires within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-03
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-28, a major forest fire in California spreads beyond 5,000 acres, as confirmed by the USGS Significant Quakes feed and two independent news outlets.
- **Resolution criterion:** The USGS Significant Quakes feed and two independent news outlets confirm a forest fire in California exceeding 5,000 acres between 2026-09-21 and 2026-09-28.
- **Failure condition:** No confirmation from the USGS feed or two independent outlets that the fire exceeded 5,000 acres during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-04
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** Between 2026-09-27 and 2026-09-30, a cyberattack on a U.S. federal agency results in the exposure of at least 1 million user records, as confirmed by a CISA KEV entry and a federal press release.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-27 and 2026-09-30, and a U.S. federal agency issues a public press release confirming the exposure of at least 1 million user records due to a cyberattack.
- **Failure condition:** No CISA KEV entry is published between 2026-09-27 and 2026-09-30 linking to a confirmed breach of a U.S. federal agency with 1 million or more records exposed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-24
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-09-30 a Ukrainian drone or missile strike causes fire or damage at an oil refinery inside internationally recognized Russian territory, acknowledged by a Russian governor, regional authority, or the operator, and claimed by the Ukrainian General Staff, SBU, or HUR.
- **Resolution criterion:** True if, for a strike dated 2026-09-15 to 2026-09-30, a Russian governor, regional authority, or the operator acknowledges fire or damage at a named refinery in Russia and a Ukrainian military or intelligence body claims it. Otherwise false.
- **Failure condition:** No Ukrainian strike between 2026-09-15 and 2026-09-30 produces Russian-acknowledged fire or damage at a refinery inside Russia.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-37
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** Between 2026-09-16 and 2026-09-29, at least one merchant vessel is attacked or seized by armed forces or armed attackers in the Persian Gulf, Strait of Hormuz, or Gulf of Oman.
- **Resolution criterion:** TRUE if UKMTO reports a merchant vessel struck by projectile, drone, mine, or explosive, fired upon, or seized in the Persian Gulf, Strait of Hormuz, or Gulf of Oman, with an incident date between 2026-09-16 and 2026-09-29.
- **Failure condition:** No merchant vessel is attacked or seized in the Persian Gulf, Strait of Hormuz, or Gulf of Oman on any date between 2026-09-16 and 2026-09-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-54
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-02
- **Domain:** military_conflict
- **Claim:** A Houthi-attributed strike hits Saudi Arabian oil or port infrastructure, or a vessel in the Red Sea or Gulf of Aden, between 2026-09-16 and 2026-09-30.
- **Resolution criterion:** TRUE if Reuters, AP, or Al Jazeera report and two of those outlets corroborate a Houthi-attributed strike on Saudi oil, port, or Red Sea shipping targets between 2026-09-16 and 2026-09-30, checked by 2026-10-02.
- **Failure condition:** No wire-corroborated Houthi-attributed strike on Saudi oil, port, or Red Sea/Gulf of Aden shipping occurs in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-56
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** The National Vulnerability Database lists a CVE entry for the Chrome zero-day used in the GRIMWEDGE deployment chain from item 25, published between 2026-09-16 and 2026-09-30.
- **Resolution criterion:** TRUE if nvd.nist.gov publishes a CVE entry referencing the Chrome zero-day exploited in the GRIMWEDGE chain from item 25, with a publication date between 2026-09-16 and 2026-09-30, checked 2026-10-02.
- **Failure condition:** No NVD CVE entry referencing this Chrome zero-day or the GRIMWEDGE chain carries a publication date in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-01
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a new flood warning for Marion County, Florida, will be issued by the National Weather Service and confirmed by at least two independent news outlets.
- **Resolution criterion:** The National Weather Service issues a flood warning for Marion County, Florida, between 2026-09-21 and 2026-09-24, and this is confirmed by at least two independent news outlets.
- **Failure condition:** No flood warning is issued for Marion County, Florida, during the event window, or no independent news outlet confirms it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-02
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new political scandal involving a U.S. government official will be reported by at least two major outlets with independent corroboration.
- **Resolution criterion:** At least two major outlets (e.g., Guardian, BBC, Al Jazeera, CNBC) report a new political scandal involving a U.S. government official, with corroboration from a third source.
- **Failure condition:** No such scandal is reported by two major outlets with independent corroboration during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-03
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a major earthquake of magnitude 6.5 or higher will be recorded by the USGS in the Aleutian Islands.
- **Resolution criterion:** The USGS records an earthquake of magnitude 6.5 or higher in the Aleutian Islands between 2026-09-21 and 2026-09-24.
- **Failure condition:** No earthquake of magnitude 6.5 or higher is recorded in the Aleutian Islands during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-04
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-24, a new cyberattack using the SparroWocky backdoor will be confirmed by at least two independent sources targeting government systems in Latin America.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-21 and 2026-09-24 for a vulnerability linked to the SparroWocky backdoor, and at least two independent sources confirm its use in attacks on government systems in Latin America.
- **Failure condition:** No such attack is confirmed by two independent sources during the event window, or the CISA KEV catalog does not list a relevant vulnerability.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032042ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SparroWocky', 'Latin America'] with dateAdded in [2026-09-21..2026-09-24] across 1733 catalog rows

### KKR-20260917-05
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-24, a new political resignation in a European country will be confirmed by at least two major news outlets.
- **Resolution criterion:** At least two major news outlets (e.g., BBC, Guardian, Al Jazeera) confirm a new political resignation in a European country between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such resignation is confirmed by two major news outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-06
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-02
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, a new military escalation in the Russia-Ukraine conflict will be confirmed by at least two hostile sides with cross-bias agreement.
- **Resolution criterion:** At least two hostile sides (e.g., RU, UA, WEST) confirm a new military escalation in the Russia-Ukraine conflict between 2026-09-21 and 2026-09-24, with cross-bias agreement.
- **Failure condition:** No such escalation is confirmed by two hostile sides with cross-bias agreement during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-45
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** USGS records at least one aftershock of magnitude 5.0 or greater within 150 km of the 20 September 2026 M6.5 Nikolski, Alaska mainshock, USGS event us7000ti1p, between 2026-09-21 and 2026-09-30.
- **Resolution criterion:** The USGS earthquake catalog lists an event of M5.0 or greater within 150 km of the Nikolski epicenter, origin time between 2026-09-21 and 2026-09-30.
- **Failure condition:** The USGS catalog lists no event of M5.0 or greater within 150 km of the Nikolski epicenter with origin time between 2026-09-21 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-15
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-02
- **Domain:** political
- **Claim:** The US and China announce agreement to establish or launch a dedicated intergovernmental AI dialogue, channel or hotline between 2026-09-23 and 2026-09-30, around the Trump-Xi White House summit.
- **Resolution criterion:** TRUE if a White House, PRC Foreign Ministry or Xinhua readout, fact sheet or joint statement issued between 2026-09-23 and 2026-09-30 says both sides agreed to establish or launch a dedicated government-to-government AI dialogue, channel or hotline.
- **Failure condition:** No agreement to establish or launch a dedicated intergovernmental AI dialogue, channel or hotline is announced by either government between 2026-09-23 and 2026-09-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-31
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-02
- **Domain:** disaster
- **Claim:** The National Weather Service issues a Hurricane Warning for at least one Hawaii zone between 2026-09-24 and 2026-09-30 UTC.
- **Resolution criterion:** TRUE if the NWS alert record, via the NWS API or the Iowa Environmental Mesonet VTEC archive, shows a Hurricane Warning (HU.W) issued by WFO Honolulu between 2026-09-24 and 2026-09-30 UTC.
- **Failure condition:** No Hurricane Warning is issued for any Hawaii zone between 2026-09-24 and 2026-09-30 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-82
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-03
- **Domain:** disaster
- **Claim:** The confirmed death toll from the August 2026 Nepal-Tibet flash flood and glacial lake outburst event reaches at least 800, as reported by the government of Nepal, Chinese authorities, or UN OCHA, between 2026-09-03 and 2026-09-30.
- **Resolution criterion:** A government of Nepal, Chinese government, or UN OCHA situation report states a confirmed fatality count of 800 or more tied to this event, dated within the window, checked by 2026-10-03.
- **Failure condition:** Confirmed fatality figures from Nepal, Chinese, or UN OCHA sources remain below 800 through the window; a large missing-persons count that is not converted into confirmed deaths does not count as a hit.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-02
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-03
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, a drone strike will be reported in Jabalia, Gaza, with at least one casualty claimed by a hostile side.
- **Resolution criterion:** At least one report from a hostile side confirms a drone strike in Jabalia, Gaza, with a claimed casualty count of one or more during the event window.
- **Failure condition:** No report from a hostile side confirms a drone strike in Jabalia, Gaza, with a claimed casualty during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-05
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-03
- **Domain:** political
- **Claim:** Between 2026-09-28 and 2026-10-01, the U.S. Congress passes the Clarity Act with a majority vote in both chambers, as confirmed by a roll call vote on Congress.gov.
- **Resolution criterion:** A roll call vote on Congress.gov confirms that the Clarity Act passed in both the House and Senate with a majority vote, as recorded by the official legislative database.
- **Failure condition:** The Clarity Act fails to pass in either the House or Senate, as confirmed by a roll call vote on Congress.gov.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-10
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-03
- **Domain:** disaster
- **Claim:** Between 2026-09-25 and 2026-09-28, a major earthquake of magnitude 6.5 or higher will be recorded in the Pacific Ring of Fire, as confirmed by the USGS Significant Quakes feed.
- **Resolution criterion:** The USGS Significant Quakes feed records a magnitude 6.5 or higher earthquake in the Pacific Ring of Fire between 2026-09-25 and 2026-09-28.
- **Failure condition:** No magnitude 6.5 or higher earthquake is recorded in the Pacific Ring of Fire between 2026-09-25 and 2026-09-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).
