# KKR RESOLUTION AUDIT PACKET
Generated 061718Z NOV 26 · 209 projections (part 4 of 4; packet total 1268) past deadline, awaiting adjudication.

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

### KKR-20260911-59
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** The United States and Iran each publicly accept a mutual ceasefire or cessation of hostilities announced between 2026-09-12 and 2026-10-31.
- **Resolution criterion:** True if, between 2026-09-12 and 2026-10-31, both the US government and the Iranian government publicly confirm a mutual ceasefire, as reported by at least two of Reuters, AP, and AFP.
- **Failure condition:** No mutual ceasefire or cessation of hostilities is agreed and publicly confirmed by both the US and Iranian governments between 2026-09-12 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-54
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field names Check Point, with a date-added value between 2026-09-14 and 2026-10-31.
- **Resolution criterion:** TRUE if the CISA KEV catalog contains an entry whose vendorProject or product names Check Point with dateAdded between 2026-09-14 and 2026-10-31 inclusive.
- **Failure condition:** No KEV entry naming Check Point carries a dateAdded inside 2026-09-14 to 2026-10-31.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171755ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 3 matching entries for ['Check Point'] with dateAdded in [2026-09-14..2026-10-31] across 1768 catalog rows - CVE-2026-76418, CVE-2026-85102, CVE-2026-93616

### KKR-20260913-13
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Between 2026-09-20 and 2026-11-01, the UK Electoral Commission or another UK regulator will open, or confirm it has opened, a formal investigation into the GBP72 million in Reform UK donations from Christopher Harborne and Ben Delo.
- **Resolution criterion:** The Electoral Commission publishes, or the BBC, Guardian, or Financial Times report, confirmation that a UK regulator opened a formal investigation into the GBP72 million Reform UK donations between 2026-09-20 and 2026-11-01.
- **Failure condition:** Neither the Electoral Commission nor another UK regulator opens or confirms a formal investigation into the GBP72 million Reform UK donations during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-36
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 125.00 USD per barrel on at least one trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 at packet seal.
- **Resolution criterion:** ICE settlement data show a Brent front-month daily settlement at or above 125.00 on any trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 at packet seal.
- **Failure condition:** No Brent front-month settlement between 2026-09-15 and 2026-10-30 reaches 125.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-55
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-11-03
- **Domain:** economics
- **Claim:** ICE front-month Brent settles at or above 120.00 USD per barrel on at least one trading day between 2026-09-15 and 2026-10-30. Reference: 108.29 on the packet date.
- **Resolution criterion:** TRUE if the official ICE Brent front-month settlement price is 120.00 USD or higher on any trading day from 2026-09-15 through 2026-10-30. Reference level 108.29 at seal.
- **Failure condition:** MISS if every ICE Brent front-month settlement inside the window prints below 120.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-18
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury constant maturity yield closes at or above 5.00 percent on at least one business day between 2026-09-16 and 2026-10-30. Reference: 4.99 percent at packet seal on 2026-09-15.
- **Resolution criterion:** True if the Treasury par yield curve or FRED series DGS10 records a value of 5.00 or higher for any business day from 2026-09-16 through 2026-10-30 inclusive.
- **Failure condition:** Every DGS10 daily value in the window is below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-14
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry for an Acronis product vulnerability with a dateAdded between 2026-09-16 and 2026-10-30.
- **Resolution criterion:** The CISA KEV JSON feed contains at least one entry whose vendorProject or product field contains Acronis and whose dateAdded falls between 2026-09-16 and 2026-10-30 inclusive.
- **Failure condition:** No KEV entry naming Acronis carries a dateAdded from 2026-09-16 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-52
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds the exploited Acronis backup plugin for cPanel vulnerability to its Known Exploited Vulnerabilities catalog between 2026-09-17 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA KEV catalog carries an entry with vendorProject Acronis whose product or vulnerabilityName references cPanel and whose dateAdded falls between 2026-09-17 and 2026-10-30; otherwise FALSE.
- **Failure condition:** CISA added no Acronis cPanel-related vulnerability to the KEV catalog with a dateAdded between 2026-09-17 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171757ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Acronis'] with dateAdded in [2026-09-17..2026-10-30] across 1768 catalog rows

### KKR-20260916-53
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds a WSO2 vulnerability to its Known Exploited Vulnerabilities catalog between 2026-09-17 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA KEV catalog carries an entry with vendorProject WSO2 whose dateAdded falls between 2026-09-17 and 2026-10-30; otherwise FALSE.
- **Failure condition:** CISA added no WSO2 vulnerability to the KEV catalog with a dateAdded between 2026-09-17 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171757ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['WSO2'] with dateAdded in [2026-09-17..2026-10-30] across 1768 catalog rows - CVE-2026-5430

### KKR-20260917-20
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry for an Issabel product with a dateAdded value between 2026-09-17 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA KEV catalog JSON contains at least one entry whose vendorProject or product field names Issabel, with dateAdded between 2026-09-17 and 2026-10-30 inclusive.
- **Failure condition:** No CISA KEV entry naming Issabel carries a dateAdded value between 2026-09-17 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171800ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Issabel'] with dateAdded in [2026-09-17..2026-10-30] across 1768 catalog rows

### KKR-20260917-38
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** The Riksdag elects Magdalena Andersson prime minister of Sweden in a vote held between 2026-09-18 and 2026-10-30.
- **Resolution criterion:** Riksdagen.se records a prime-ministerial vote held between 2026-09-18 and 2026-10-30 in which the Speaker proposal of Magdalena Andersson is not rejected, meaning fewer than 175 members vote no.
- **Failure condition:** Magdalena Andersson has not been confirmed as prime minister by any Riksdag vote held from 2026-09-18 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-32
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** US forces strike at least one target on Iranian land territory, including Iranian islands, between 2026-09-21 and 2026-10-31; strikes limited to vessels at sea do not count.
- **Resolution criterion:** TRUE if the Pentagon or CENTCOM confirms, or both Reuters and AP report, a US strike on a target on Iranian land territory, islands included, occurring between 2026-09-21 and 2026-10-31.
- **Failure condition:** No US strike hit a target on Iranian land territory, islands included, between 2026-09-21 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-33
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** A Chinese coast guard, navy, or maritime militia vessel fires a water cannon at, rams, or collides with a Philippine government vessel in the South China Sea between 2026-09-21 and 2026-10-31.
- **Resolution criterion:** TRUE if the Philippine Coast Guard or Armed Forces of the Philippines reports a Chinese water-cannon, ramming or collision incident against a Philippine government vessel dated 2026-09-21 to 2026-10-31, carried by Reuters or AP.
- **Failure condition:** No Chinese vessel fired a water cannon at, rammed, or collided with a Philippine government vessel in the South China Sea between 2026-09-21 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-34
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-11-03
- **Domain:** crime/security
- **Claim:** A single non-state militant attack in Pakistan kills at least 10 people, not counting the attackers, between 2026-09-21 and 2026-10-31.
- **Resolution criterion:** TRUE if Reuters or AP reports a non-state militant attack in Pakistan, occurring between 2026-09-21 and 2026-10-31, with a death toll from officials of at least 10 excluding attackers.
- **Failure condition:** No single non-state militant attack in Pakistan between 2026-09-21 and 2026-10-31 killed 10 or more people excluding attackers.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-13
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant-maturity yield closes at or above 5.25 percent on at least one business day between 2026-09-21 and 2026-10-30. Reference: 5.00 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 (Treasury H.15) records a value of 5.25 or higher for any date between 2026-09-21 and 2026-10-30 inclusive.
- **Failure condition:** Every DGS10 observation dated 2026-09-21 through 2026-10-30 is below 5.25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-17
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant-maturity yield (FRED series DGS10) closes at or above 5.25 percent on at least one day between 2026-09-21 and 2026-10-30. Reference: 5.00 percent on the packet date.
- **Resolution criterion:** True if any DGS10 daily value dated 2026-09-21 to 2026-10-30 is 5.25 or higher.
- **Failure condition:** No DGS10 daily value in the window reaches 5.25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-41
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury constant-maturity yield (FRED DGS10) closes below 4.60 percent on at least one day between 2026-09-22 and 2026-10-30. Reference: 4.96 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows a daily value below 4.60 for any date 2026-09-22 through 2026-10-30.
- **Failure condition:** No DGS10 daily value from 2026-09-22 through 2026-10-30 is below 4.60.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-16
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-11-03
- **Domain:** crime/security
- **Claim:** Between 2026-09-22 and 2026-10-30, a Sri Lankan court hands down sentences to at least one of the 15 men convicted on 2026-09-22 over the 2019 Easter Sunday bombings, as reported by at least two of Reuters, AP, AFP, and BBC.
- **Resolution criterion:** True if at least two of Reuters, AP, AFP, BBC report, dated 2026-09-22 to 2026-10-30, a sentence pronounced on at least one of the 15 convicted defendants.
- **Failure condition:** No sentence for any of the 15 convicted defendants is reported by two of the named outlets within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-09
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Between 2026-09-24 and 2026-10-30 the Ethiopian Council of Ministers declares a federal state of emergency whose scope includes Tigray Region, in response to the TPLF and allied rebel offensive.
- **Resolution criterion:** TRUE if between 2026-09-24 and 2026-10-30 the Ethiopian Council of Ministers declares a federal state of emergency whose stated scope includes Tigray Region, reported by ENA or Fana and by Reuters or AP; FALSE otherwise.
- **Failure condition:** No federal state of emergency whose scope includes Tigray is declared between 2026-09-24 and 2026-10-30, a regional emergency, military operation order, or terrorist designation alone being insufficient.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-12
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Between 2026-09-25 and 2026-10-30 the US District Court for the District of Columbia enters an order holding the government or any official in contempt, or imposing sanctions, for violating the 2026-09-24 temporary restraining order restoring White House access for CNN, MS NOW and Politico.
- **Resolution criterion:** TRUE if between 2026-09-25 and 2026-10-30 the D.D.C. docket in the CNN, MS NOW and Politico hard-pass suit shows an order holding any defendant in contempt or imposing sanctions for TRO noncompliance; show-cause orders alone are FALSE.
- **Failure condition:** No contempt or sanctions order for TRO noncompliance is entered on the docket between 2026-09-25 and 2026-10-30, with orders to show cause, compliance directives, or oral warnings not counting.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-29
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** NYMEX WTI crude front-month futures settle at or above 100.00 dollars per barrel on at least one trading day between 2026-09-28 and 2026-10-30. Reference: 92.41 on the packet date (2026-09-25 settlement).
- **Resolution criterion:** TRUE if the CME NYMEX WTI front-month daily settlement is 100.00 or higher on any trading day from 2026-09-28 through 2026-10-30. Reference: 92.41 settlement on the packet date.
- **Failure condition:** WTI front-month settles below 100.00 on every trading day from 2026-09-28 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-11
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** Between 2026-10-25 and 2026-11-01, the U.S. Federal Reserve will announce a 50 basis point rate hike.
- **Resolution criterion:** The U.S. Federal Reserve announces a 50 basis point rate hike between 2026-10-25 and 2026-11-01.
- **Failure condition:** The U.S. Federal Reserve does not announce a 50 basis point rate hike during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-47
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Between 2026-09-30 and 2026-10-30, Estonia formally expels, or declares persona non grata, at least one Russian diplomat accredited in Estonia.
- **Resolution criterion:** The Estonian Ministry of Foreign Affairs, or two of Reuters, AP and ERR, confirm that at least one Russian diplomat was expelled or declared persona non grata by Estonia between 2026-09-30 and 2026-10-30.
- **Failure condition:** Estonia neither expels a Russian diplomat nor declares one persona non grata between 2026-09-30 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-12
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Ukrenergo imposes scheduled or emergency power outages on Kyiv city on at least one day between 2026-10-08 and 2026-10-31.
- **Resolution criterion:** True if Ukrenergo announces scheduled or emergency outages applying to Kyiv city on any day between 2026-10-08 and 2026-10-31, as carried by at least two of Reuters, Kyiv Independent and Ukrinform; otherwise false.
- **Failure condition:** Kyiv city goes every day between 2026-10-08 and 2026-10-31 with neither scheduled nor emergency outages imposed by Ukrenergo.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-14
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant maturity yield closes at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date.
- **Resolution criterion:** True if FRED series DGS10 prints 5.50 or higher for any date between 2026-10-01 and 2026-10-30 inclusive; otherwise false. Reference: 5.27 percent on the packet date.
- **Failure condition:** DGS10 stays below 5.50 percent on every business day between 2026-10-01 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-15
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The ICE Brent December 2026 futures contract settles below 90.00 dollars a barrel on at least one trading day between 2026-10-01 and 2026-10-30. Reference: 99.12 on the packet date.
- **Resolution criterion:** True if the ICE Brent December 2026 contract daily settlement is below 90.00 on any trading day between 2026-10-01 and 2026-10-30 inclusive; otherwise false. Reference: 99.12 on the packet date.
- **Failure condition:** The December 2026 Brent contract settles at or above 90.00 on every trading day between 2026-10-01 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-27
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack at least once between 2026-10-01 and 2026-10-31.
- **Resolution criterion:** True if a Ukrainian Air Force daily report, as carried by Reuters or AP, records 500 or more drones and missiles combined launched in one overnight attack between 2026-10-01 and 2026-10-31; otherwise false.
- **Failure condition:** Russia launches fewer than 500 drones and missiles combined in every overnight attack on Ukraine between 2026-10-01 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-31
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date.
- **Resolution criterion:** True if FRED series DGS10 shows 5.50 or higher for any date between 2026-10-01 and 2026-10-30; otherwise false. Reference: 5.27 percent on 2026-09-30 per the packet market snapshot.
- **Failure condition:** The 10-year Treasury constant-maturity yield closes below 5.50 percent on every business day from 2026-10-01 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-17
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant maturity yield stands at or above 5.50 percent on 2026-10-30. Reference: 5.25 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows 5.50 or higher for 2026-10-30. Reference: 5.25 percent on the packet date.
- **Failure condition:** The 10-year constant maturity yield for 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-18
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds at least 40 vulnerabilities to its Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-10-31. Reference: 43 entries carry a September 2026 date-added value in catalog version 2026.09.30.
- **Resolution criterion:** The CISA KEV catalog feed carries 40 or more entries with a dateAdded value between 2026-10-01 and 2026-10-31 inclusive.
- **Failure condition:** CISA adds fewer than 40 vulnerabilities to the KEV catalog between 2026-10-01 and 2026-10-31.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171802ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 36 entries with dateAdded in [2026-10-01..2026-10-31] against a floor of 40 across 1768 catalog rows

### KKR-20261001-19
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds at least one Zammad vulnerability to its Known Exploited Vulnerabilities catalog between 2026-10-01 and 2026-10-31.
- **Resolution criterion:** The CISA KEV catalog feed carries at least one entry naming Zammad in vendorProject or product with a dateAdded value between 2026-10-01 and 2026-10-31 inclusive.
- **Failure condition:** CISA adds no Zammad vulnerability to the KEV catalog between 2026-10-01 and 2026-10-31.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171802ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['Zammad'] with dateAdded in [2026-10-01..2026-10-31] across 1768 catalog rows - CVE-2026-102489, CVE-2026-102490

### KKR-20261001-21
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Ethiopian federal forces or allied militias enter Mekelle city between 2026-10-02 and 2026-10-31.
- **Resolution criterion:** Reuters, AP or AFP reports, citing the Ethiopian government or independent sources, that federal or allied forces entered Mekelle city on a date between 2026-10-02 and 2026-10-31.
- **Failure condition:** Ethiopian federal and allied forces do not enter Mekelle city between 2026-10-02 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-45
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury constant maturity yield (FRED series DGS10) closes at or above 5.50 percent on at least one business day between 2026-10-02 and 2026-10-30. Reference: 5.25 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows at least one daily value of 5.50 or higher dated between 2026-10-02 and 2026-10-30 inclusive. Reference: 5.25 percent on the packet date.
- **Failure condition:** Every FRED DGS10 daily value dated between 2026-10-02 and 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-38
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Between 2026-10-05 and 2026-10-30, Ethiopian and Eritrean state forces will fight each other directly, including cross-border fire or air strikes on each other.
- **Resolution criterion:** At least two of Reuters, AP, AFP, BBC report Ethiopian and Eritrean state forces fought each other directly between 2026-10-05 and 2026-10-30, beyond one government accusing the other of backing rebels.
- **Failure condition:** Ethiopian and Eritrean state forces do not fight each other directly between 2026-10-05 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-40
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent December 2026 futures will settle below 90.00 USD per barrel on at least one trading day between 2026-10-05 and 2026-10-30. Reference: 100.27 in the packet market snapshot.
- **Resolution criterion:** ICE published settlement for Brent December 2026 futures is below 90.00 USD per barrel on at least one trading day between 2026-10-05 and 2026-10-30 inclusive. Reference: 100.27 on the packet date.
- **Failure condition:** ICE Brent December 2026 futures settle at or above 90.00 USD per barrel on every trading day between 2026-10-05 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-44
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** Between 2026-10-05 and 2026-10-30, Congolese health authorities will report a cumulative Ebola death toll of at least 4,700 in the ongoing outbreak. Reference: 4,018 deaths reported on 2026-10-02.
- **Resolution criterion:** Reuters, AP, or WHO publish a Congolese government cumulative Ebola death count of at least 4,700, dated between 2026-10-05 and 2026-10-30. Reference: 4,018 deaths reported on 2026-10-02.
- **Failure condition:** No Congolese government cumulative Ebola death count dated between 2026-10-05 and 2026-10-30 reaches 4,700.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-20
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The ICE Brent December 2026 crude futures contract settles at or above 110.00 dollars per barrel on at least one trading day between 2026-10-05 and 2026-10-30. Reference: 102.25 dollars on the packet date.
- **Resolution criterion:** TRUE if any daily ICE settlement of the Brent December 2026 contract between 2026-10-05 and 2026-10-30 is 110.00 dollars or higher. Reference: 102.25 dollars, the prior-session close on the packet date.
- **Failure condition:** Every daily settlement of the Brent December 2026 contract between 2026-10-05 and 2026-10-30 is below 110.00 dollars.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-45
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-03
- **Domain:** crime/security
- **Claim:** Japanese prosecutors formally indict the US Marine arrested in Okinawa in October 2026 over the killing of a woman in Naha, on any charge arising from her death, between 2026-10-06 and 2026-10-30.
- **Resolution criterion:** NHK, Kyodo, Reuters, or AP reports that Naha prosecutors filed an indictment against the arrested Marine on any charge arising from the death of the woman, dated between 2026-10-06 and 2026-10-30.
- **Failure condition:** The arrested Marine is not indicted on any charge arising from the death of the woman between 2026-10-06 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-01
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, the CISA KEV catalog will carry a date-added value for a vulnerability in Rejetto HFS servers with a critical RCE flaw.
- **Resolution criterion:** The CISA KEV catalog will list a vulnerability with a date-added value between 2026-10-21 and 2026-10-28 that is related to Rejetto HFS and involves a critical remote code execution flaw.
- **Failure condition:** The CISA KEV catalog does not list any vulnerability related to Rejetto HFS with a critical RCE flaw added between 2026-10-21 and 2026-10-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171805ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Rejetto HFS'] with dateAdded in [2026-10-21..2026-10-28] across 1768 catalog rows

### KKR-20261007-25
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Russian air, missile or drone strikes kill at least 10 people in Ukraine on a single calendar day between 2026-10-09 and 2026-10-29.
- **Resolution criterion:** At least two of Reuters, AP, AFP and BBC report Ukrainian officials attributing 10 or more deaths to Russian air, missile or drone strikes on one calendar day between 2026-10-09 and 2026-10-29.
- **Failure condition:** No calendar day between 2026-10-09 and 2026-10-29 sees Russian air, missile or drone strikes kill 10 or more people in Ukraine.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-05
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** Between 2026-10-23 and 2026-10-30, a new earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific Ring of Fire.
- **Resolution criterion:** The USGS Significant Quakes database records at least one earthquake with magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-23 and 2026-10-30.
- **Failure condition:** The USGS database records no earthquake of magnitude 6.0 or higher in the Pacific Ring of Fire between 2026-10-23 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-04
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-10-29 and 2026-11-01, a cyberattack exploiting CVE-2016-3081 will be reported by at least two independent sources, with the attack targeting a U.S. government system.
- **Resolution criterion:** At least two independent sources report a cyberattack exploiting CVE-2016-3081 targeting a U.S. government system between 2026-10-29 and 2026-11-01.
- **Failure condition:** No cyberattack exploiting CVE-2016-3081 targeting a U.S. government system is reported by two independent sources within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-29
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-10-12 and 2026-10-30. Reference: 104.81 on the packet date 2026-10-09.
- **Resolution criterion:** True if any daily ICE Brent front-month settlement from 2026-10-12 through 2026-10-30 is 110.00 USD or higher; otherwise false. Reference level at seal: 104.81.
- **Failure condition:** Every ICE Brent front-month settlement from 2026-10-12 through 2026-10-30 is below 110.00 USD per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-29
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** The USGS catalog records at least one earthquake of magnitude 6.0 or greater within 200 km of the epicenter of the M 7.7 Panama mainshock (USGS event us6000u18k) with origin time between 2026-10-11 and 2026-10-31 UTC.
- **Resolution criterion:** TRUE if a USGS ComCat query (minimum magnitude 6.0, 200 km radius around event us6000u18k, origin times 2026-10-11 through 2026-10-31 UTC) returns at least one event; otherwise FALSE.
- **Failure condition:** No earthquake of magnitude 6.0 or greater occurs within 200 km of the mainshock epicenter between 2026-10-11 and 2026-10-31 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-30
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** The US National Hurricane Center names at least one new Atlantic-basin tropical or subtropical storm (any name after Isaias on the 2026 list) between 2026-10-11 and 2026-10-31 UTC.
- **Resolution criterion:** TRUE if the NHC Atlantic advisory archive shows a storm first receiving a name after Isaias on the 2026 list in an advisory issued between 2026-10-11 and 2026-10-31 UTC; otherwise FALSE.
- **Failure condition:** No Atlantic-basin tropical or subtropical storm is first named between 2026-10-11 and 2026-10-31 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-10
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-03
- **Domain:** economics
- **Claim:** The 10-year US Treasury yield closes above 5.50 percent at least once between 2026-10-27 and 2026-11-02.
- **Resolution criterion:** The 10-year US Treasury yield closes above 5.50 percent on at least one trading day within the event window.
- **Failure condition:** The 10-year US Treasury yield closes at or below 5.50 percent on every trading day within the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261106T171806ZZ - sha256 9cee4a11cad003f6...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 5 business days in window; max BC_10YEAR 5.05 on 2026-10-28; threshold > 5.50; 0 day(s) satisfying

### KKR-20261014-12
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-03
- **Domain:** economics
- **Claim:** Brent crude oil closes above 115.00 dollars per barrel at least once between 2026-10-27 and 2026-11-02.
- **Resolution criterion:** Brent crude oil closes above 115.00 dollars per barrel on at least one trading day within the event window.
- **Failure condition:** Brent crude oil closes at or below 115.00 dollars per barrel on every trading day within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-24
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Between 2026-10-15 and 2026-10-31, at least one merchant vessel is struck by a projectile, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman, as logged by UKMTO.
- **Resolution criterion:** A UKMTO incident notice or advisory records a merchant vessel struck, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman with an incident date between 2026-10-15 and 2026-10-31.
- **Failure condition:** No merchant vessel is struck, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman on any date between 2026-10-15 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-60
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** A Ukrainian drone or missile strike causes a fire or damage at an oil refinery inside Russia on at least one day between 2026-10-15 and 2026-10-31.
- **Resolution criterion:** Reuters or AP report a strike attributed to Ukraine by Ukrainian or Russian officials that caused fire or damage at an oil refinery in Russia, excluding occupied Ukraine, occurring between 2026-10-15 and 2026-10-31.
- **Failure condition:** No Ukrainian-attributed strike causes fire or damage at any oil refinery in Russia between 2026-10-15 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-61
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Between 2026-10-16 and 2026-10-31, a Ukrainian drone or missile attack causes a fire or physical damage at one or more oil refineries in Russia.
- **Resolution criterion:** TRUE if Reuters or AP reports a Ukrainian drone or missile attack causing fire or damage at a named oil refinery in Russia between 2026-10-16 and 2026-10-31 inclusive, confirmed by a Russian official or the Ukrainian military.
- **Failure condition:** No oil refinery in Russia suffers fire or physical damage from a Ukrainian drone or missile attack between 2026-10-16 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261019-02
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-10-22 and 2026-10-28, a cyberattack exploiting the NGINX vulnerability CVE-2026-XXXX is confirmed in at least three distinct government or critical infrastructure systems.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-22 and 2026-10-28, and at least three distinct government or critical infrastructure systems report exploitation of the NGINX vulnerability CVE-2026-XXXX.
- **Failure condition:** No entry in the CISA KEV catalog between 2026-10-22 and 2026-10-28 confirms exploitation of the NGINX vulnerability CVE-2026-XXXX in three or more government or critical infrastructure systems.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261024-05
- **Issued:** 2026-10-24  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-10-26 and 2026-11-01, the CISA KEV catalog will include at least one new entry for a vulnerability in a widely deployed open-source software component that is actively exploited in the wild.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-26 and 2026-11-01 for a vulnerability in a widely deployed open-source software component that is actively exploited in the wild.
- **Failure condition:** No new entry in the CISA KEV catalog between 2026-10-26 and 2026-11-01 for a vulnerability in a widely deployed open-source software component that is actively exploited in the wild.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261025-07
- **Issued:** 2026-10-25  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Lula wins the Brazilian presidential election runoff in October 2026.
- **Resolution criterion:** Lula is declared the winner of the Brazilian presidential election runoff in October 2026.
- **Failure condition:** Bolsonaro or another candidate is declared the winner of the Brazilian presidential election runoff in October 2026.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260806-10
- **Issued:** 2026-08-06  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A Russian missile or drone strike on Kyiv city kills at least 5 people in a single attack between 2026-08-06 and 2026-10-31, per Ukrainian official casualty statements.
- **Resolution criterion:** TRUE if Ukrainian authorities state at least 5 killed in one strike on Kyiv city within the window, reported by at least two international news outlets; FALSE otherwise.
- **Failure condition:** No single strike on Kyiv city within the window carries an official Ukrainian death toll of 5 or more.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260809-04
- **Issued:** 2026-08-09  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** An attack on or seizure of a commercial vessel in the Strait of Hormuz or Gulf of Oman, attributed to Iran or Iran-aligned forces, occurs between 2026-08-10 and 2026-10-31.
- **Resolution criterion:** At least two of Reuters, AP, AFP, BBC report an in-window attack on or seizure of a commercial vessel in those waters, attributing it to Iran or Iran-aligned forces.
- **Failure condition:** No commercial vessel in the Strait of Hormuz or Gulf of Oman is attacked or seized by Iran or Iran-aligned forces within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260810-20
- **Issued:** 2026-08-10  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** The Israeli cabinet or security cabinet formally approves the United States 15-point Gaza plan between 2026-08-11 and 2026-10-31.
- **Resolution criterion:** TRUE if the Israeli Prime Minister Office or Government Press Office announces cabinet approval of that plan within the window and both Reuters and AP report the approval.
- **Failure condition:** No Israeli cabinet vote approving the 15-point plan is announced during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260811-14
- **Issued:** 2026-08-11  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one Microsoft SharePoint vulnerability with a dateAdded value between 2026-08-12 and 2026-10-31.
- **Resolution criterion:** TRUE if the CISA KEV catalog contains at least one entry whose product field references SharePoint and whose dateAdded falls between 2026-08-12 and 2026-10-31.
- **Failure condition:** No KEV entry referencing SharePoint carries a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171807ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['SharePoint'] with dateAdded in [2026-08-12..2026-10-31] across 1768 catalog rows - CVE-2026-55040, CVE-2026-65660

### KKR-20260817-70
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** US forces conduct a military strike on Omani territory or Omani territorial waters between 2026-08-18 and 2026-10-31.
- **Resolution criterion:** The US Defense Department or CENTCOM acknowledges a strike on Omani territory or territorial waters occurring in that window, and both Reuters and Agence France-Presse report it.
- **Failure condition:** No US strike on Omani territory or Omani territorial waters occurs inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-16
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** The United States conducts at least one military strike on Omani territory between 2026-08-19 and 2026-10-31.
- **Resolution criterion:** At least two of Reuters, AP, AFP, and BBC report a US strike on Omani soil dated between 2026-08-19 and 2026-10-31, or US Central Command confirms one.
- **Failure condition:** No US munition impacts Omani territory within the stated window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-15
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** At least one earthquake of magnitude 7.0 or greater occurs worldwide with origin time in the window 2026-08-26 to 2026-10-31 UTC.
- **Resolution criterion:** The USGS ComCat catalog lists at least one event of magnitude 7.0 or greater with origin time between 2026-08-26T00:00Z and 2026-10-31T23:59Z.
- **Failure condition:** The USGS catalog holds no event of magnitude 7.0 or greater with origin time inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-43
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog gains at least one entry with vendorProject Microsoft and a dateAdded between 2026-08-24 and 2026-10-31.
- **Resolution criterion:** The CISA KEV catalog JSON contains at least one record where vendorProject is Microsoft and dateAdded falls between 2026-08-24 and 2026-10-31.
- **Failure condition:** The KEV catalog holds no Microsoft record with a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171808ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 5 matching entries for ['Microsoft'] with dateAdded in [2026-08-24..2026-10-31] across 1768 catalog rows - CVE-2019-1068, CVE-2026-65660, CVE-2026-81963, CVE-2026-85880, CVE-2026-96951

### KKR-20260825-10
- **Issued:** 2026-08-25  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Between 2026-08-25 and 2026-10-31, the HHS Office for Civil Rights breach portal posts an entry naming Nutex Health or a Nutex-affiliated hospital with 500 or more individuals affected.
- **Resolution criterion:** TRUE if the HHS OCR breach portal lists an entry whose covered-entity name contains Nutex or names a hospital Nutex Health publicly identifies as its facility, with submission date 2026-08-25 through 2026-10-31 and 500 or more individuals affected.
- **Failure condition:** No qualifying Nutex-linked entry with 500 or more individuals affected and a submission date inside the window appears on the HHS OCR breach portal.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-16
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** CISA catalogues a Microsoft SharePoint vulnerability as actively exploited, with a KEV date-added value between 2026-08-27 and 2026-10-31.
- **Resolution criterion:** The CISA KEV catalog JSON holds an entry with vendorProject Microsoft, a product string naming SharePoint, and a dateAdded value between 2026-08-27 and 2026-10-31.
- **Failure condition:** No SharePoint entry in the KEV catalog carries a dateAdded value inside that range.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171809ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 4 matching entries for ['Microsoft', 'SharePoint'] with dateAdded in [2026-08-27..2026-10-31] across 1768 catalog rows - CVE-2026-65660, CVE-2026-81963, CVE-2026-85880, CVE-2026-96951

### KKR-20260827-83
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-04
- **Domain:** crime_security
- **Claim:** At least one individual arrested in the TeamPCP supply-chain hacking case is formally charged by an Australian prosecutorial authority or a foreign partner agency, between 2026-09-03 and 2026-10-31.
- **Resolution criterion:** An AFP, CDPP, DOJ, or equivalent prosecutorial press release, or a court filing, confirms formal charges were laid against at least one TeamPCP suspect within the window, checked by 2026-11-04.
- **Failure condition:** No formal charges are confirmed laid against any TeamPCP suspect within the window; continued investigation, bail conditions without charges, or release without charge all count as a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-85
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The Federal Register will publish at least one presidential proclamation or executive order imposing new or increased US tariff rates, dated between 2026-09-01 and 2026-10-31.
- **Resolution criterion:** A Federal Register presidential document published between 2026-09-01 and 2026-10-31 newly imposes or raises US duty rates on imported goods. Pure extensions of existing rates resolve FALSE.
- **Failure condition:** No presidential document dated inside the window newly imposes or raises a US tariff rate.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-86
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** The United States and Iran will hold publicly acknowledged direct bilateral talks between 2026-09-01 and 2026-10-31.
- **Resolution criterion:** A US executive branch spokesperson and the Iranian foreign ministry each acknowledge that officials of the two states met directly between 2026-09-01 and 2026-10-31. Mediated contact alone resolves FALSE.
- **Failure condition:** US and Iranian officials do not meet face to face inside the window, or all contact runs through third-party mediators.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-88
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** King Harald V of Norway will die between 2026-08-28 and 2026-10-31 and Crown Prince Haakon will succeed him as king.
- **Resolution criterion:** The Royal House of Norway announces the death of King Harald V on a date between 2026-08-28 and 2026-10-31, and Haakon is proclaimed king or takes the oath before the Storting.
- **Failure condition:** King Harald V is alive at the close of 2026-10-31, or the crown passes to someone other than Haakon.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-21
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Combined confirmed deaths from the Nepal-Tibet glacial outburst flood reach 1,000 or more at some point between 2026-08-29 and 2026-10-31.
- **Resolution criterion:** Nepal Police and Chinese authority tolls, as reported by two of Reuters, AP, and AFP, sum to 1,000 or more confirmed dead on any date inside the window.
- **Failure condition:** The highest combined confirmed toll reported inside the window remains below 1,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-50
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Stolen City of Berlin administrative data is published on an extortion leak site between 2026-08-29 and 2026-10-31.
- **Resolution criterion:** TRUE if at least two of BBC, Reuters, dpa, Tagesspiegel or Heise report that data taken from Berlin city systems was published by the extortion group in that window.
- **Failure condition:** No publication of Berlin municipal data by the extortionists is reported by two of the named outlets by 2026-11-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-54
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** The confirmed death toll in Nepal from the 2026-08-26 Rasuwa flood reaches at least 1000 between 2026-08-30 and 2026-10-31.
- **Resolution criterion:** TRUE if Nepal Police or the NDRRMA give a confirmed Nepal death toll of 1000 or more inside that window, carried by two of Reuters, AP, AFP or BBC.
- **Failure condition:** The official Nepal death toll stays below 1000 through 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-60
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-11-04
- **Domain:** disaster_infrastructure
- **Claim:** Ukrenergo or DTEK announces emergency or rolling power cuts affecting Kyiv city on at least one day between 2026-09-15 and 2026-10-31.
- **Resolution criterion:** An Ukrenergo or DTEK notice dated inside the window states that emergency or rolling outage schedules apply to consumers in Kyiv city.
- **Failure condition:** Kyiv city consumers face no announced emergency or rolling outage schedule on any day inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-08
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Commercial shipping transit through the Strait of Hormuz is suspended for at least 48 consecutive hours at any point between 2026-09-01 and 2026-10-31.
- **Resolution criterion:** True if at least two international wire services, citing shipping authorities or maritime insurers, report a suspension of commercial Strait of Hormuz transits lasting 48 or more consecutive hours between 2026-09-01 and 2026-10-31.
- **Failure condition:** Commercial Strait of Hormuz transits continue between 2026-09-01 and 2026-10-31 without any suspension reaching 48 consecutive hours.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-02
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-09-02 and 2026-10-31, Donald Trump and Vladimir Putin meet in person, with the meeting confirmed by both the White House and the Kremlin.
- **Resolution criterion:** True if whitehouse.gov and kremlin.ru both carry official confirmation or readouts of an in-person Trump-Putin meeting held between 2026-09-02 and 2026-10-31; phone or video calls do not count.
- **Failure condition:** Trump and Putin do not meet in person on any date between 2026-09-02 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-04
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant maturity yield closes at or above 5.00 percent on at least one trading day between 2026-09-02 and 2026-10-30. Reference: 4.77 percent on 2026-09-01.
- **Resolution criterion:** True if FRED series DGS10 shows a daily value of 5.00 or higher for any date from 2026-09-02 through 2026-10-30; the Treasury daily par yield curve is the tiebreaker if FRED is unavailable.
- **Failure condition:** Every daily DGS10 value from 2026-09-02 through 2026-10-30 is below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-05
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The WTI crude oil spot price at Cushing settles at or above 100.00 dollars per barrel on at least one trading day between 2026-09-02 and 2026-10-30. Reference: 88.02 dollars on 2026-09-01.
- **Resolution criterion:** True if FRED series DCOILWTICO (EIA Cushing WTI spot) shows a daily value of 100.00 or higher for any date from 2026-09-02 through 2026-10-30; the EIA daily spot price table is the tiebreaker.
- **Failure condition:** Every daily DCOILWTICO value from 2026-09-02 through 2026-10-30 is below 100.00 dollars per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-48
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A continuous suspension of laden tanker transits through the Strait of Hormuz lasting at least 72 hours begins between 2026-09-03 and 2026-10-31.
- **Resolution criterion:** At least two of Reuters, AP, Bloomberg, AFP report, citing AIS or tracking data, a continuous 72-hour halt of laden tanker transits beginning inside the window.
- **Failure condition:** Laden tanker transits of the strait continue throughout the window without any continuous 72-hour suspension beginning in it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-36
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-11-04
- **Domain:** crime/security
- **Claim:** UK Home Office figures record 900 or more people arriving in the UK by small boat on at least one single day between 2026-09-04 and 2026-10-31.
- **Resolution criterion:** The Home Office small boat arrivals dataset on gov.uk (migrants detected crossing the English Channel in small boats) shows a daily arrivals figure of 900 or more for at least one date from 2026-09-04 through 2026-10-31 inclusive.
- **Failure condition:** No single day between 2026-09-04 and 2026-10-31 has a Home Office recorded small boat arrivals figure of 900 or more.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-39
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-09-04 and 2026-10-31, a decree published on the official website of the President of Ukraine removes the serving head of the SBU or the serving head of the GUR from that post.
- **Resolution criterion:** Resolves TRUE if a presidential decree dated within the window and published at president.gov.ua removes the incumbent SBU chief or GUR chief; reassignment to another post counts as removal; otherwise FALSE.
- **Failure condition:** No presidential decree dated within the window removes the incumbent head of the SBU or the GUR.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-33
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant maturity yield prints at or above 5.00 percent on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.78 percent on the packet date.
- **Resolution criterion:** TRUE if FRED series DGS10 records a value of 5.00 or higher for any date between 2026-09-08 and 2026-10-30. Reference: 4.78 at seal.
- **Failure condition:** All DGS10 values for dates between 2026-09-08 and 2026-10-30 remain below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-77
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-09-07 and 2026-10-31 inclusive, Donald Trump and Vladimir Putin hold an in-person meeting, confirmed by both the White House and the Kremlin.
- **Resolution criterion:** True if both whitehouse.gov and kremlin.ru publish confirmation that Trump and Putin met in person on a date between 2026-09-07 and 2026-10-31 inclusive; video or telephone contact does not count.
- **Failure condition:** No in-person meeting between Trump and Putin takes place between 2026-09-07 and 2026-10-31, or any claimed meeting lacks confirmation from either the White House or the Kremlin.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-21
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury constant maturity yield closes at or above 5.00 percent on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.78 percent on the packet date 2026-09-07.
- **Resolution criterion:** FRED series DGS10 (Treasury 10-year constant maturity) shows a daily value of 5.00 or higher for at least one date from 2026-09-08 through 2026-10-30 inclusive. Reference: 4.78 on 2026-09-07. No such value resolves false.
- **Failure condition:** The DGS10 daily value never reaches 5.00 percent on any business day from 2026-09-08 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-25
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Official Russian and Ukrainian government delegations hold a direct in-person negotiating session, bilateral or with third-party mediation, between 2026-09-08 and 2026-10-30.
- **Resolution criterion:** Both the Kremlin or Russian MFA and the Ukrainian Presidential Office or MFA confirm the same in-person delegation session held 2026-09-08 through 2026-10-30. Video calls, prisoner-exchange contacts, and meetings with US officials only do not count.
- **Failure condition:** No in-person Russian-Ukrainian delegation session takes place between 2026-09-08 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-29
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** The NTSB publishes a preliminary report on the 2026-09-06 cargo aircraft accident at Miami International Airport between 2026-09-08 and 2026-10-30.
- **Resolution criterion:** TRUE if an NTSB preliminary report for the 2026-09-06 Miami cargo aircraft accident appears in the NTSB public investigation database dated between 2026-09-08 and 2026-10-30.
- **Failure condition:** No NTSB preliminary report for the 2026-09-06 Miami cargo aircraft accident is publicly available dated on or before 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-37
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A commercial vessel is struck by weapons fire, forcibly boarded, or seized in the Strait of Hormuz or the Gulf of Oman between 2026-09-14 and 2026-10-31.
- **Resolution criterion:** TRUE if two or more of Reuters, AP, and Bloomberg report a commercial vessel hit by weapons fire, forcibly boarded, or seized in the Strait of Hormuz or Gulf of Oman, dated inside the window.
- **Failure condition:** No commercial vessel is struck, forcibly boarded, or seized in those waters inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-33
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** The UN Security Council adopts a resolution addressing Iran between 2026-09-11 and 2026-10-30.
- **Resolution criterion:** The UN Security Council 2026 resolutions list on un.org shows a resolution adopted between 2026-09-11 and 2026-10-30 with Iran in its title or with operative paragraphs on the Iranian nuclear programme or the US-Iran conflict.
- **Failure condition:** No Security Council resolution addressing Iran, its nuclear programme or the US-Iran conflict is adopted between 2026-09-11 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-49
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least 20 new entries with dateAdded values between 2026-09-11 and 2026-10-31 inclusive.
- **Resolution criterion:** The public CISA KEV JSON feed, fetched on the deadline date, contains 20 or more entries whose dateAdded field falls between 2026-09-11 and 2026-10-31 inclusive.
- **Failure condition:** Fewer than 20 KEV entries carry dateAdded values inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-50
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Houthi forces take control of at least one additional named town or port on the Red Sea coast of Yemen beyond Mocha between 2026-09-11 and 2026-10-31.
- **Resolution criterion:** At least two of Reuters, AP, AFP, or BBC report Houthi control of a named Red Sea coastal town or port other than Mocha, with the change of control occurring inside the window.
- **Failure condition:** Houthi forces gain control of no additional named Red Sea coastal town or port beyond Mocha inside the window under the stated corroboration standard.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-36
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-09-16 and 2026-10-31, the governments of the United States and Iran both publicly commit to a ceasefire or cessation of hostilities between the two countries.
- **Resolution criterion:** TRUE if, between 2026-09-16 and 2026-10-31, the US President or White House and the Iranian government each publicly confirm a US-Iran ceasefire or cessation of hostilities, as reported by Reuters or AP.
- **Failure condition:** The United States and Iran do not both publicly commit to a ceasefire or cessation of hostilities at any point between 2026-09-16 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-40
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant-maturity yield (FRED series DGS10) is 5.50 percent or higher on at least one observation date between 2026-09-16 and 2026-10-30. Reference: 10-year yield 4.99 percent in the 2026-09-15 packet market snapshot.
- **Resolution criterion:** TRUE if FRED series DGS10 shows a daily value of 5.50 or higher for any observation date between 2026-09-16 and 2026-10-30; otherwise FALSE. Reference: 4.99 percent on 2026-09-15.
- **Failure condition:** The 10-year Treasury constant-maturity yield stays below 5.50 percent on every observation date from 2026-09-16 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-42
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** CISA issues at least one new Emergency Directive between 2026-09-16 and 2026-10-30.
- **Resolution criterion:** TRUE if the Cybersecurity Directives listing on cisa.gov shows an Emergency Directive with an issue date between 2026-09-16 and 2026-10-30; otherwise FALSE.
- **Failure condition:** CISA issues no new Emergency Directive between 2026-09-16 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-51
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The S&P 500 closes at or below 7046.19, a 7.5 percent decline from the packet reference, on at least one trading day between 2026-09-17 and 2026-10-30. Reference: 7617.50 on the packet date.
- **Resolution criterion:** TRUE if FRED series SP500 shows a daily close at or below 7046.19 for any date between 2026-09-17 and 2026-10-30; otherwise FALSE. Reference: 7617.50 on the packet date.
- **Failure condition:** The S&P 500 closed above 7046.19 on every trading day from 2026-09-17 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-15
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-09-18 and 2026-10-31, the United States and Iran announce a ceasefire or cessation-of-hostilities agreement covering combat between US and Iranian forces, confirmed publicly by both governments.
- **Resolution criterion:** TRUE if, between 2026-09-18 and 2026-10-31, the US government and the Iranian government each publicly confirm a ceasefire or cessation-of-hostilities agreement covering US-Iran combat operations, reported by at least two of Reuters, AP, AFP.
- **Failure condition:** No ceasefire or cessation-of-hostilities agreement covering US-Iran combat operations is publicly confirmed by both governments with an agreement date between 2026-09-18 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-26
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-11-04
- **Domain:** military_conflict
- **Claim:** Russian authorities report drone interceptions over Moscow city or Moscow oblast on at least three separate calendar days between 2026-09-27 and 2026-10-31.
- **Resolution criterion:** TRUE if drone interception over Moscow city or oblast is reported on three or more distinct dates between 2026-09-27 and 2026-10-31 by a Russian official source and carried by at least one Ukrainian or Western outlet.
- **Failure condition:** Fewer than three distinct dates inside the window carry a Moscow-area drone interception event.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-48
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** The US and Iranian governments announce a ceasefire or cessation-of-hostilities agreement, confirmed by both governments, between 2026-09-22 and 2026-10-31.
- **Resolution criterion:** Official statements from both the White House or State Department and the Iranian presidency or foreign ministry confirm a ceasefire agreement dated 2026-09-22 through 2026-10-31, reported by Reuters and Al Jazeera.
- **Failure condition:** No ceasefire agreement is confirmed by both governments within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-28
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-11-04
- **Domain:** economic
- **Claim:** The S&P 500 sets a new all-time closing high on at least one session between 2026-09-23 and 2026-10-30. Reference: 7,764.88 close on the packet date, up 2.36 percent.
- **Resolution criterion:** TRUE if S&P 500 daily close data show a close above the all-time closing high standing on 2026-09-22, on any session from 2026-09-23 through 2026-10-30; otherwise FALSE.
- **Failure condition:** Every S&P 500 close inside the window sits at or below the all-time closing high that stood on 2026-09-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-17
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-09-24 and 2026-10-31, Russia and Ukraine each publicly announce acceptance of a mutual halt to strikes on energy infrastructure, the energy truce pushed by Trump and endorsed by Zelensky at the UN.
- **Resolution criterion:** Within the window, a Kremlin statement on kremlin.ru or via TASS quoting Putin or Peskov, and a Ukrainian presidential statement on president.gov.ua or by Zelensky, each confirm agreement to a mutual energy-strike moratorium.
- **Failure condition:** By 2026-10-31 at least one of the two governments has not publicly confirmed agreement to a mutual halt on energy-infrastructure strikes.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-19
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-09-24 and 2026-10-31, at least one air or drone strike hits Mekelle (Mekele) city, capital of the Tigray region of Ethiopia, amid the mutual offensive accusations between Addis Ababa and the TPLF.
- **Resolution criterion:** At least two of Reuters, AP, AFP and BBC report, citing residents, hospital staff, humanitarian or UN sources, an air or drone strike impacting inside Mekelle city on a date inside the window.
- **Failure condition:** No air or drone strike impacting inside Mekelle city during the window is established by two of the named outlets.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-07
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year Treasury constant maturity yield (FRED series DGS10) records a daily value of 5.50 percent or higher on at least one business day between 2026-09-25 and 2026-10-30. Reference: 5.14 percent on the packet date.
- **Resolution criterion:** TRUE if FRED series DGS10 shows any observation dated 2026-09-25 through 2026-10-30 with a value of 5.50 or higher; FALSE otherwise. Reference: 5.14 percent on the packet date.
- **Failure condition:** Every DGS10 observation dated 2026-09-25 through 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-27
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Government delegations of the United States, Russia and Ukraine meet in person in a trilateral negotiating session between 2026-09-28 and 2026-10-31.
- **Resolution criterion:** TRUE if at least two of AP, Reuters and AFP report that US, Russian and Ukrainian government delegations met together in person in one session between 2026-09-28 and 2026-10-31; otherwise FALSE.
- **Failure condition:** No in-person session attended jointly by US, Russian and Ukrainian government delegations takes place between 2026-09-28 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-08
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose vendorProject or product field names Kiteworks or Accellion, with a dateAdded value between 2026-09-26 and 2026-10-31.
- **Resolution criterion:** The CISA KEV JSON feed (known_exploited_vulnerabilities.json) contains an entry whose vendorProject or product field includes Kiteworks or Accellion and whose dateAdded is between 2026-09-26 and 2026-10-31 inclusive.
- **Failure condition:** No KEV entry naming Kiteworks or Accellion carries a dateAdded between 2026-09-26 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-09
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry whose product field names Elementor (the WordPress plugin), with a dateAdded value between 2026-09-26 and 2026-10-31.
- **Resolution criterion:** The CISA KEV JSON feed contains an entry whose vendorProject or product field includes Elementor and whose dateAdded is between 2026-09-26 and 2026-10-31 inclusive; entries for WordPress core or other plugins do not count.
- **Failure condition:** No KEV entry naming Elementor carries a dateAdded between 2026-09-26 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-08
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** The United States and Iran publicly confirm a ceasefire, truce, or halt-to-hostilities agreement that takes effect on a date between 2026-09-28 and 2026-10-31.
- **Resolution criterion:** TRUE if both the White House or State Department and the Iran Foreign Ministry publicly confirm a ceasefire, truce, or halt to hostilities taking effect between 2026-09-28 and 2026-10-31, as reported by at least two of Reuters, AP, AFP.
- **Failure condition:** No ceasefire, truce, or halt-to-hostilities agreement between the United States and Iran is confirmed by both governments as taking effect between 2026-09-28 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-13
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-04
- **Domain:** crime/security
- **Claim:** At least one suspect appears in a South African court charged in connection with the 2026-09-26 Wedela tavern mass shooting near Johannesburg, with the first appearance dated between 2026-09-28 and 2026-10-30.
- **Resolution criterion:** TRUE if SAPS or the National Prosecuting Authority publicly confirms, or two of Reuters, AP, AFP report, a court appearance by at least one accused charged for the Wedela shooting, dated between 2026-09-28 and 2026-10-30.
- **Failure condition:** No person charged for the Wedela tavern shooting makes a first court appearance between 2026-09-28 and 2026-10-30; arrests without a court appearance do not satisfy.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-16
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The S&P 500 records at least one close-to-close daily decline of 2.00 percent or more on a trading day between 2026-09-28 and 2026-10-30. Reference: 7743.41 close on the packet date.
- **Resolution criterion:** TRUE if FRED series SP500 shows any observation dated 2026-09-28 through 2026-10-30 whose close is at least 2.00 percent below the immediately preceding trading day close. Reference level 7743.41 on the packet date.
- **Failure condition:** Every S&P 500 close-to-close daily change from 2026-09-28 through 2026-10-30 is better than minus 2.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-17
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant maturity yield (FRED DGS10) prints 5.50 percent or higher on at least one observation dated between 2026-09-28 and 2026-10-30. Reference: 5.18 percent on the packet date.
- **Resolution criterion:** TRUE if FRED series DGS10 contains any observation dated 2026-09-28 through 2026-10-30 with value 5.50 or greater. Reference level 5.18 percent on the packet date.
- **Failure condition:** Every DGS10 observation dated 2026-09-28 through 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-19
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The official NYMEX WTI crude oil front-month futures settlement price on 2026-10-30 is above 100.00 dollars per barrel. Reference: 95.60 dollars per barrel on the packet date.
- **Resolution criterion:** TRUE if the CME Group official settlement for the front-month NYMEX WTI crude oil futures contract on 2026-10-30, as also recorded in the EIA daily futures price series, is strictly greater than 100.00 dollars per barrel.
- **Failure condition:** The front-month WTI settlement on 2026-10-30 is at or below 100.00 dollars per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-41
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** Between 2026-10-01 and 2026-10-30, the FRED series DGS10 (10-year Treasury constant maturity yield) records a value at or above 5.50 percent on at least one business day. Reference: 5.27 percent per the packet market snapshot; FRED DGS10 was 5.18 percent on 2026-09-24.
- **Resolution criterion:** At least one FRED DGS10 observation dated between 2026-10-01 and 2026-10-30 is 5.50 or higher. Reference: 5.27 percent per the packet market snapshot on 2026-09-28.
- **Failure condition:** Every FRED DGS10 observation dated between 2026-10-01 and 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-43
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-10-01 and 2026-10-31, OFAC designates at least one entity located outside Iran for supporting Iranian airlines or the Iranian aviation sector.
- **Resolution criterion:** A US Treasury press release or OFAC Recent Actions SDN list update dated between 2026-10-01 and 2026-10-31 designates an entity located outside Iran and cites support to Iranian airlines or the Iranian aviation sector.
- **Failure condition:** No OFAC designation dated between 2026-10-01 and 2026-10-31 of an entity located outside Iran cites support to Iranian airlines or the Iranian aviation sector.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-17
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The ICE Brent crude front-month futures contract settles at or below 85.00 US dollars per barrel on at least one trading day between 2026-10-01 and 2026-10-30. Reference: 97.04 on the packet date, after an 8.97 percent one-day fall (section V).
- **Resolution criterion:** TRUE if any official ICE Brent front-month settlement price dated 2026-10-01 through 2026-10-30 is at or below 85.00; FALSE if every settlement in the window is above 85.00.
- **Failure condition:** Every ICE Brent front-month settlement from 2026-10-01 to 2026-10-30 is above 85.00 dollars per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-18
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant maturity yield (FRED series DGS10) prints at or above 5.50 percent on at least one business day between 2026-10-01 and 2026-10-30. Reference: 5.26 percent on the packet date (section V).
- **Resolution criterion:** TRUE if any DGS10 observation dated 2026-10-01 through 2026-10-30 is greater than or equal to 5.50; FALSE if all observations in the window are below 5.50.
- **Failure condition:** Every DGS10 observation in the window is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-44
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-01 and 2026-10-31, the United States government and the Iranian government both publicly confirm an agreed arrangement under which Iran reopens the Strait of Hormuz to commercial shipping.
- **Resolution criterion:** Official statements from both Washington and Tehran dated 2026-10-01 through 2026-10-31, corroborated by at least two of Reuters, AP and AFP, confirm an agreed arrangement for Iran to reopen the Strait of Hormuz to commercial shipping.
- **Failure condition:** The two governments do not both confirm an agreed arrangement for Iran to reopen the Strait of Hormuz between 2026-10-01 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-49
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** FRED series DGS10 records a 10-year Treasury constant maturity yield of 5.50 percent or higher on at least one date between 2026-10-01 and 2026-10-30. Reference: 5.26 percent in the packet market snapshot dated 2026-09-29.
- **Resolution criterion:** FRED series DGS10 shows a daily value of 5.50 or higher for any date from 2026-10-01 through 2026-10-30 inclusive. Reference level: 5.26 percent on the packet date 2026-09-29.
- **Failure condition:** Every FRED DGS10 daily value from 2026-10-01 through 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-47
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-04
- **Domain:** economic
- **Claim:** The US 10-year Treasury constant-maturity yield closes at or above 5.50 percent on at least one date between 2026-10-01 and 2026-10-30. Reference: 5.27 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows a value of 5.50 percent or higher for at least one date between 2026-10-01 and 2026-10-30 inclusive. Reference: 5.27 percent on the packet date.
- **Failure condition:** The US 10-year Treasury constant-maturity yield stays below 5.50 percent on every date between 2026-10-01 and 2026-10-30 inclusive.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-48
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-04
- **Domain:** economic
- **Claim:** The S&P 500 index closes at or below 7,300 on at least one date between 2026-10-01 and 2026-10-30. Reference: 7,712.13 on the packet date.
- **Resolution criterion:** The official S&P 500 closing value, per S&P Dow Jones Indices or FRED series SP500, is 7,300.00 or lower on at least one date between 2026-10-01 and 2026-10-30 inclusive. Reference: 7,712.13 on the packet date.
- **Failure condition:** The S&P 500 closes above 7,300.00 on every date between 2026-10-01 and 2026-10-30 inclusive.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-45
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-04
- **Domain:** disaster_infrastructure
- **Claim:** Between 2026-10-05 and 2026-11-01, the National Hurricane Center classifies at least one Atlantic tropical cyclone at hurricane intensity, meaning maximum sustained winds of at least 74 mph.
- **Resolution criterion:** An NHC advisory issued between 2026-10-05 and 2026-11-01 lists an Atlantic tropical cyclone with maximum sustained winds of at least 74 mph.
- **Failure condition:** Every Atlantic tropical cyclone in NHC advisories issued from 2026-10-05 through 2026-11-01 stays below 74 mph maximum sustained winds.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-25
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-11-04
- **Domain:** crime/security
- **Claim:** Japanese prosecutors indict the US Marine arrested in Okinawa on 2026-10-04 on a charge of murder or robbery resulting in death between 2026-10-05 and 2026-10-30.
- **Resolution criterion:** TRUE if the Naha District Public Prosecutors Office indicts the arrested Marine for murder or robbery-murder between 2026-10-05 and 2026-10-30, as reported by Kyodo, NHK, AP or Stars and Stripes.
- **Failure condition:** By 2026-10-30 the Marine has not been indicted for murder or robbery-murder, whether because he is held for psychiatric evaluation, charged with a lesser offence, or released.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-01
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, a cyberattack exploiting CVE-2026-88779 will be reported by two or more independent sources in the CISA KEV or The Hacker News.
- **Resolution criterion:** A cyberattack exploiting CVE-2026-88779 is reported by two or more independent sources in the CISA KEV catalog or The Hacker News between 2026-10-21 and 2026-10-28.
- **Failure condition:** No such attack is reported by two or more independent sources in the specified sources during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171811ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-88779'] with dateAdded in [2026-10-21..2026-10-28] across 1768 catalog rows

### KKR-20261005-02
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-10-21 and 2026-10-28, Iran will publicly announce a toll for oil transit through the Strait of Hormuz.
- **Resolution criterion:** Iran publicly announces a toll for oil transit through the Strait of Hormuz between 2026-10-21 and 2026-10-28.
- **Failure condition:** Iran does not publicly announce a toll for oil transit through the Strait of Hormuz during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-03
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Between 2026-10-21 and 2026-10-28, a new earthquake of magnitude 4.0 or higher will be recorded by USGS in the Pacific Northwest.
- **Resolution criterion:** A new earthquake of magnitude 4.0 or higher is recorded by USGS in the Pacific Northwest between 2026-10-21 and 2026-10-28.
- **Failure condition:** No such earthquake is recorded by USGS in the Pacific Northwest during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171811ZZ - sha256 9aba2a40d612cd03...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-21&endtime=2026-10-29&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=4.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261005-04
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Between 2026-10-21 and 2026-10-28, a new tropical cyclone named KOGUMA-26 will be reported by GDACS with a population affected of over 100,000.
- **Resolution criterion:** A new tropical cyclone named KOGUMA-26 is reported by GDACS with a population affected of over 100,000 between 2026-10-21 and 2026-10-28.
- **Failure condition:** KOGUMA-26 is not reported by GDACS with a population affected of over 100,000 during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-05
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, a new cyberattack targeting a financial institution in South Korea will be confirmed by BleepingComputer and The Hacker News.
- **Resolution criterion:** A new cyberattack targeting a financial institution in South Korea is confirmed by BleepingComputer and The Hacker News between 2026-10-21 and 2026-10-28.
- **Failure condition:** No such attack is confirmed by both BleepingComputer and The Hacker News during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-34
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** At least one more commercial vessel is struck by an aerial or naval drone inside the exclusive economic zone or territorial sea of Bulgaria or Romania between 2026-10-08 and 2026-10-31.
- **Resolution criterion:** Bulgarian or Romanian authorities state that a commercial vessel was struck by a drone inside the exclusive economic zone or territorial sea of either country between 2026-10-08 and 2026-10-31, as reported by Reuters or AP.
- **Failure condition:** No commercial vessel is struck by a drone inside the exclusive economic zone or territorial sea of Bulgaria or Romania between 2026-10-08 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-06
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Between 2026-10-24 and 2026-10-31, a major cyberattack on a U.S. financial institution will be confirmed by the FBI.
- **Resolution criterion:** The FBI issues a public statement between 2026-10-24 and 2026-10-31 confirming a cyberattack on a U.S. financial institution that resulted in data compromise or service disruption.
- **Failure condition:** The FBI does not issue a public statement confirming a cyberattack on a U.S. financial institution during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-59
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** CISA will add at least one Fortinet vulnerability to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-10-12 and 2026-11-01.
- **Resolution criterion:** The CISA KEV catalog JSON carries at least one entry with vendorProject Fortinet and dateAdded between 2026-10-12 and 2026-11-01 inclusive.
- **Failure condition:** As of the deadline, CISA had added no Fortinet vulnerability to the KEV catalog with a dateAdded value between 2026-10-12 and 2026-11-01.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171812ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Fortinet'] with dateAdded in [2026-10-12..2026-11-01] across 1768 catalog rows - CVE-2025-61624

### KKR-20261009-05
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Between 2026-10-30 and 2026-11-02, a forest fire will be reported in Australia with a green alert issued by GDACS, and the fire will be confirmed by at least two independent sources.
- **Resolution criterion:** A forest fire in Australia is reported with a green alert by GDACS, and confirmed by at least two independent sources between 2026-10-30 and 2026-11-02.
- **Failure condition:** No forest fire in Australia is reported with a green alert by GDACS, or is not confirmed by two independent sources, within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-61
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A Russian missile or drone strike damages a Ukrainian thermal or hydroelectric power plant or gas-production facility between 2026-10-19 and 2026-11-01.
- **Resolution criterion:** TRUE if Reuters or AP reports, citing Ukrainian officials or the operator, Russian strike damage to a Ukrainian thermal or hydroelectric power plant or gas-production facility occurring between 2026-10-19 and 2026-11-01.
- **Failure condition:** No Russian strike damages any Ukrainian thermal or hydroelectric power plant or gas-production facility between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-63
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Ukraine strikes a refinery, oil depot, oil terminal, or power plant in Russia or Russian-occupied territory with drones or missiles between 2026-10-13 and 2026-10-31.
- **Resolution criterion:** YES if Ukrainian military or security officials claim, and Russian federal, regional, or occupation officials acknowledge, an attack on the same refinery, oil depot, oil terminal, or power plant dated between 2026-10-13 and 2026-10-31.
- **Failure condition:** No Ukrainian drone or missile attack hit a refinery, oil depot, oil terminal, or power plant in Russia or Russian-occupied territory between 2026-10-13 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-48
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** ICE Brent front-month futures settle below 100.00 USD per barrel on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 105.86 on the packet date, 2026-10-13.
- **Resolution criterion:** ICE Brent front-month daily settlement price, as published by ICE or reported by Reuters, is below 100.00 USD per barrel on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 105.86 on 2026-10-13.
- **Failure condition:** Every ICE Brent front-month daily settlement between 2026-10-14 and 2026-10-30 is at or above 100.00 USD per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-49
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** The S&P 500 closes at least 2.0 percent below its prior close on at least one trading day between 2026-10-14 and 2026-10-30. Reference: 7,796.70 on the packet date, 2026-10-13.
- **Resolution criterion:** FRED series SP500 or S&P Dow Jones Indices shows a daily close at least 2.0 percent below the prior trading day close on at least one date between 2026-10-14 and 2026-10-30. Reference: 7,796.70 on 2026-10-13.
- **Failure condition:** On every trading day between 2026-10-14 and 2026-10-30 the S&P 500 closes less than 2.0 percent below its prior close.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-21
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** economics
- **Claim:** The S&P 500 closes below 7,700 on at least one trading day between 2026-10-26 and 2026-11-02
- **Resolution criterion:** The S&P 500 closes below 7,700 on at least one trading day between 2026-10-26 and 2026-11-02. Reference: 7,726.84 on the packet date
- **Failure condition:** The S&P 500 closes at or above 7,700 on every trading day between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-22
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A USGS Significant Quake with magnitude 6.0 or higher occurs between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A USGS Significant Quake with magnitude 6.0 or higher occurs between 2026-10-26 and 2026-11-02
- **Failure condition:** No USGS Significant Quake with magnitude 6.0 or higher occurs between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-23
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** economics
- **Claim:** The 10Y US Treasury Yield closes above 5.10 on at least one trading day between 2026-10-26 and 2026-11-02
- **Resolution criterion:** The 10Y US Treasury Yield closes above 5.10 on at least one trading day between 2026-10-26 and 2026-11-02. Reference: 5.05 on the packet date
- **Failure condition:** The 10Y US Treasury Yield closes at or below 5.10 on every trading day between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-24
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** military
- **Claim:** A kinetic event involving a drone occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A kinetic event involving a drone occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **Failure condition:** No kinetic event involving a drone occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-25
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A USGS Significant Quake with magnitude 7.0 or higher occurs between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A USGS Significant Quake with magnitude 7.0 or higher occurs between 2026-10-26 and 2026-11-02
- **Failure condition:** No USGS Significant Quake with magnitude 7.0 or higher occurs between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-26
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** economics
- **Claim:** The Nasdaq closes below 26,000 on at least one trading day between 2026-10-26 and 2026-11-02
- **Resolution criterion:** The Nasdaq closes below 26,000 on at least one trading day between 2026-10-26 and 2026-11-02. Reference: 26,611.73 on the packet date
- **Failure condition:** The Nasdaq closes at or above 26,000 on every trading day between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-27
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** military
- **Claim:** A kinetic event involving a missile occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A kinetic event involving a missile occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **Failure condition:** No kinetic event involving a missile occurs in the Russia-Ukraine Theatre between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-28
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** military
- **Claim:** A kinetic event involving a missile occurs in the Israel-Gaza-Levant Theatre between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A kinetic event involving a missile occurs in the Israel-Gaza-Levant Theatre between 2026-10-26 and 2026-11-02
- **Failure condition:** No kinetic event involving a missile occurs in the Israel-Gaza-Levant Theatre between 2026-10-26 and 2026-11-02
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-29
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-16 and 2026-10-31 the Ukrainian General Staff publicly claims a strike on at least one oil refinery inside the Russian Federation, and a Russian regional governor or the Russian Ministry of Defence acknowledges a drone attack on, or fire at, that refinery or its locality on the same date.
- **Resolution criterion:** True if, for a date between 2026-10-16 and 2026-10-31, the Ukrainian General Staff claims a strike on a refinery inside Russia and a Russian governor or MoD acknowledges a drone attack or fire at that refinery or its locality.
- **Failure condition:** No date between 2026-10-16 and 2026-10-31 carries both a Ukrainian General Staff refinery strike claim and a matching Russian governor or MoD acknowledgment of a drone attack or fire at that refinery or its locality.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-48
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A merchant vessel is struck by a drone, missile or naval mine inside Romanian territorial waters or the Romanian exclusive economic zone between 2026-10-19 and 2026-11-01, not counting the vessels reported on fire on 2026-10-15.
- **Resolution criterion:** Romanian authorities state, or two of Reuters, AP, BBC and DW report, a new drone, missile or mine strike on a merchant ship inside Romanian waters or exclusive economic zone between 2026-10-19 and 2026-11-01.
- **Failure condition:** No merchant ship other than the vessels hit on 2026-10-15 is struck by a drone, missile or naval mine inside Romanian waters or its exclusive economic zone between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-47
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A California wildfire that starts between 2026-10-17 and 2026-10-30 reaches at least 10,000 acres burned by 2026-11-04.
- **Resolution criterion:** CAL FIRE incident records or the NIFC WFIGS interagency fire perimeters list a California wildfire with start date from 2026-10-17 through 2026-10-30 and reported size of at least 10,000 acres by the deadline.
- **Failure condition:** No California wildfire that started between 2026-10-17 and 2026-10-30 has reached 10,000 acres by 2026-11-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-36
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-18 and 2026-10-31 UKMTO or the Joint Maritime Information Center publishes an incident advisory stating that a merchant vessel in the Persian Gulf, Strait of Hormuz, or Gulf of Oman was struck by a projectile, mine, or uncrewed system.
- **Resolution criterion:** The UKMTO or JMIC incident list carries an advisory dated 2026-10-18 to 2026-10-31 describing a merchant vessel struck by a projectile, mine, or uncrewed system in the Persian Gulf, Strait of Hormuz, or Gulf of Oman.
- **Failure condition:** No merchant vessel is recorded by UKMTO or JMIC as struck by a projectile, mine, or uncrewed system in the Persian Gulf, Strait of Hormuz, or Gulf of Oman within the 2026-10-18 to 2026-10-31 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-48
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-18 and 2026-11-01, Russia launches at least 600 drones and missiles combined against Ukraine in a single overnight attack, as tallied by the Ukrainian Air Force.
- **Resolution criterion:** A Ukrainian Air Force tally, repeated by Reuters or AP, gives at least 600 drones and missiles combined for one overnight attack with a report date between 2026-10-18 and 2026-11-01 inclusive.
- **Failure condition:** No single overnight Russian attack of at least 600 drones and missiles combined occurred between 2026-10-18 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-49
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-18 and 2026-10-31, at least one merchant vessel is struck by a projectile, drone, missile, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman.
- **Resolution criterion:** UKMTO or JMIC incident reports list at least one merchant vessel struck by a projectile, drone, missile, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman, dated between 2026-10-18 and 2026-10-31 inclusive.
- **Failure condition:** No merchant vessel was struck by a projectile, drone, missile, or mine in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-10-18 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-50
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-10-18 and 2026-10-31, Egypt formally authorises defence assistance to Saudi Arabia, through a vote of its House of Representatives or an announcement by its presidency or cabinet.
- **Resolution criterion:** At least two of Reuters, AP, and Al-Ahram report that the Egyptian House of Representatives voted to approve, or the presidency or cabinet announced, authorisation of defence assistance to Saudi Arabia, dated between 2026-10-18 and 2026-10-31 inclusive.
- **Failure condition:** Neither the Egyptian House of Representatives, the presidency, nor the cabinet authorised defence assistance to Saudi Arabia between 2026-10-18 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-51
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** Between 2026-10-19 and 2026-10-30, the front-month ICE Brent crude futures contract settles above 120.00 USD per barrel on at least one trading day. Reference: 109.86 USD per barrel on the packet date.
- **Resolution criterion:** ICE Futures Europe daily settlement for front-month Brent exceeds 120.00 USD per barrel on at least one trading day between 2026-10-19 and 2026-10-30 inclusive. Reference: 109.86 USD per barrel on the packet date.
- **Failure condition:** Front-month Brent futures settled at or below 120.00 USD per barrel on every trading day between 2026-10-19 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-52
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** economics/markets
- **Claim:** Between 2026-10-19 and 2026-10-30, the 10-year US Treasury yield is above 5.25 percent on at least one trading day. Reference: 5.10 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows a value above 5.25 for at least one date between 2026-10-19 and 2026-10-30 inclusive. Reference: 5.10 percent on the packet date.
- **Failure condition:** The 10-year US Treasury yield stayed at or below 5.25 percent on every trading day between 2026-10-19 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-55
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Between 2026-10-18 and 2026-11-01 UTC, at least one earthquake of magnitude 7.0 or greater occurs anywhere in the world.
- **Resolution criterion:** The USGS ComCat earthquake catalog lists at least one event with magnitude 7.0 or greater and origin time between 2026-10-18T00:00Z and 2026-11-01T23:59Z, using magnitudes as listed at the deadline.
- **Failure condition:** No earthquake of magnitude 7.0 or greater occurred anywhere in the world between 2026-10-18 and 2026-11-01 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-10
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** Between 2026-10-27 and 2026-11-02, a new diplomatic crisis will emerge between Iran and the U.S. over the Strait of Hormuz, confirmed by a public statement from both sides and corroborated by at least two independent news outlets.
- **Resolution criterion:** A public statement from Iran and the U.S. regarding a crisis over the Strait of Hormuz is issued between 2026-10-27 and 2026-11-02, and the event is independently corroborated by at least two independent news outlets (e.g., BBC, Al Jazeera).
- **Failure condition:** No public statement from both Iran and the U.S. is issued on the Strait of Hormuz crisis, or no two independent outlets confirm the event within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-11
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military_conflict
- **Claim:** A drone strike hits a Russian military base in Belgorod Oblast between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** A drone strike hits a Russian military base in Belgorod Oblast between 2026-10-26 and 2026-11-02.
- **Failure condition:** No drone strike hits a Russian military base in Belgorod Oblast between 2026-10-26 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-12
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A forest fire in South Africa causes GDACS to issue a Red alert between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** A forest fire in South Africa causes GDACS to issue a Red alert between 2026-10-26 and 2026-11-02.
- **Failure condition:** A forest fire in South Africa does not cause GDACS to issue a Red alert between 2026-10-26 and 2026-11-02.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - gdacs - fetched 20261106T171817ZZ - sha256 c91935d33880d41c...
  - instrument: https://www.gdacs.org/xml/rss.xml
  - observed: no live match in 234 feed items — the RSS is a current-state feed; absence now does not adjudicate the whole window. Archive check is the operator's.

### KKR-20261018-14
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** A US court docket records an indictment of a senior Iranian official for cyber operations between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** A US court docket records an indictment of a senior Iranian official for cyber operations between 2026-10-26 and 2026-11-02.
- **Failure condition:** A US court docket does not record an indictment of a senior Iranian official for cyber operations between 2026-10-26 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-15
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A M6.0+ earthquake occurs in Pakistan between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** A M6.0+ earthquake occurs in Pakistan between 2026-10-26 and 2026-11-02.
- **Failure condition:** A M6.0+ earthquake does not occur in Pakistan between 2026-10-26 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-16
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Microsoft issues a critical security update for a zero-day exploit in Windows between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** Microsoft issues a critical security update for a zero-day exploit in Windows between 2026-10-26 and 2026-11-02.
- **Failure condition:** Microsoft does not issue a critical security update for a zero-day exploit in Windows between 2026-10-26 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-17
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds an entry for the SiteGuard WAF flaw between 2026-10-26 and 2026-11-02
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-26 and 2026-11-02 for the SiteGuard WAF flaw
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-10-26 and 2026-11-02 for the SiteGuard WAF flaw
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171818ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SiteGuard WAF'] with dateAdded in [2026-10-26..2026-11-02] across 1768 catalog rows

### KKR-20261018-19
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A major power outage affects more than 100,000 customers in France between 2026-10-26 and 2026-11-02
- **Resolution criterion:** EDF or RTE reports a power outage affecting more than 100,000 customers in France
- **Failure condition:** EDF or RTE does not report a power outage affecting more than 100,000 customers in France
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-20
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** A US federal judge issues a preliminary injunction against the EPA PFAS rule between 2026-10-26 and 2026-11-02
- **Resolution criterion:** A US federal court docket records the issuance of a preliminary injunction against the EPA PFAS rule
- **Failure condition:** A US federal court docket does not record the issuance of a preliminary injunction against the EPA PFAS rule
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-21
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** A significant earthquake (M6.0+) occurs in the Pacific Ring of Fire between 2026-10-26 and 2026-11-02
- **Resolution criterion:** The USGS catalog records an earthquake with magnitude 6.0 or greater in the Pacific Ring of Fire
- **Failure condition:** The USGS catalog does not record an earthquake with magnitude 6.0 or greater in the Pacific Ring of Fire
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-22
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Microsoft releases a security update for the ConnectWise supply-chain vulnerability between 2026-10-26 and 2026-11-02
- **Resolution criterion:** Microsoft releases a security update for the ConnectWise supply-chain vulnerability
- **Failure condition:** Microsoft does not release a security update for the ConnectWise supply-chain vulnerability
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-23
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Russia launches a major drone attack on Kyiv between 2026-10-26 and 2026-11-02
- **Resolution criterion:** Ukrainian or Russian sources report a major drone attack on Kyiv
- **Failure condition:** Ukrainian or Russian sources do not report a major drone attack on Kyiv
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-31
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** crime/security
- **Claim:** French authorities announce a cumulative arrest total of at least 3,000 for the student-led protest wave that began in October 2026, for a period ending on or before 2026-11-01. Reference: 1,800 arrests announced as of 2026-10-18.
- **Resolution criterion:** An official statement or post by the French Interior Ministry or the Paris Prefecture de Police gives a cumulative arrest figure of 3,000 or more for the protest wave, covering a period ending on or before 2026-11-01.
- **Failure condition:** The highest cumulative arrest total announced by French authorities for the protest wave, for periods ending by 2026-11-01, is below 3,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-32
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A Ukrainian drone strike hits an oil refinery, oil terminal, or fuel depot in St Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-01, acknowledged by Russian officials and claimed by Ukrainian officials.
- **Resolution criterion:** Russian officials (regional governor or MoD) and Ukrainian officials (General Staff, SBU, or Unmanned Systems Forces) both acknowledge the same strike on an oil or fuel facility in St Petersburg or Leningrad Oblast dated 2026-10-19 to 2026-11-01.
- **Failure condition:** No strike on an oil or fuel facility in St Petersburg or Leningrad Oblast dated 2026-10-19 to 2026-11-01 is acknowledged by both Russian and Ukrainian officials.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-33
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** A merchant vessel is attacked, hit by an explosion, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-10-19 and 2026-11-01, as recorded by UKMTO.
- **Resolution criterion:** UKMTO records an attack, explosion, boarding, or seizure of a merchant vessel in the Strait of Hormuz, Persian Gulf, or Gulf of Oman dated 2026-10-19 to 2026-11-01; suspicious approaches or hailing alone do not count.
- **Failure condition:** No merchant vessel is attacked, hit by an explosion, boarded, or seized in the Strait of Hormuz, Persian Gulf, or Gulf of Oman between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-40
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** Between 2026-10-19 and 2026-11-01, CISA adds a SiteGuard WAF vulnerability to its Known Exploited Vulnerabilities catalog.
- **Resolution criterion:** The CISA KEV catalog JSON carries an entry whose vendorProject, product, or shortDescription field contains SiteGuard, with a dateAdded value between 2026-10-19 and 2026-11-01 inclusive.
- **Failure condition:** No SiteGuard vulnerability is added to the CISA KEV catalog with a dateAdded value between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171818ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['SiteGuard'] with dateAdded in [2026-10-19..2026-11-01] across 1768 catalog rows - CVE-2026-106931

### KKR-20261018-43
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-19 and 2026-11-01, a Ukrainian drone attack damages an energy facility in Saint Petersburg or Leningrad Oblast.
- **Resolution criterion:** At least two of Reuters, AP, BBC, and Al Jazeera report a Ukrainian drone attack that damaged an oil, fuel, port, or power facility in Saint Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-01.
- **Failure condition:** No Ukrainian drone attack damages an energy facility in Saint Petersburg or Leningrad Oblast between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-44
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-19 and 2026-11-01, Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack.
- **Resolution criterion:** The Ukrainian Air Force reports at least 500 drones and missiles combined launched in one overnight attack between 2026-10-19 and 2026-11-01, confirmed by at least two of Reuters, AP, BBC, and Al Jazeera.
- **Failure condition:** No single overnight Russian attack launches 500 or more drones and missiles combined at Ukraine between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-45
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** military/conflict
- **Claim:** Between 2026-10-19 and 2026-11-01, United States or Israeli forces strike a target inside Iran and the US or Israeli government publicly acknowledges the strike.
- **Resolution criterion:** At least two of Reuters, AP, BBC, and Al Jazeera report an air, missile, or drone strike on a target inside Iran between 2026-10-19 and 2026-11-01, acknowledged by the US or Israeli government.
- **Failure condition:** No strike on a target inside Iran is carried out and acknowledged by the US or Israeli government between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-46
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** disaster
- **Claim:** Between 2026-10-19 and 2026-11-01, an earthquake of magnitude 5.0 or greater strikes within 100 km of Khuzdar, Pakistan.
- **Resolution criterion:** The USGS ComCat catalog lists an earthquake of magnitude 5.0 or greater with epicenter within 100 km of 27.80 N 66.62 E and origin time between 2026-10-19 00:00 UTC and 2026-11-01 23:59 UTC.
- **Failure condition:** No earthquake of magnitude 5.0 or greater occurs within 100 km of Khuzdar, Pakistan between 2026-10-19 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-48
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-04
- **Domain:** crime/security
- **Claim:** Between 2026-10-19 and 2026-11-01, an official French figure puts cumulative arrests in the student-led protest wave at 3,000 or more. Reference: 1,800 arrests reported by 2026-10-18.
- **Resolution criterion:** A French Interior Ministry, police, or prosecutor figure published between 2026-10-19 and 2026-11-01 and relayed by two of Reuters, AP, AFP, and the Guardian puts cumulative protest-related arrests at 3,000 or more. Reference: 1,800 on 2026-10-18.
- **Failure condition:** Cumulative arrests in the French student-led protest wave remain below 3,000 through 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261019-03
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries a date-added value for a critical NGINX vulnerability between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** The CISA KEV catalog entry for the NGINX vulnerability has a date_added value falling within the event window.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value for the NGINX vulnerability within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261019-12
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-11-04
- **Domain:** political
- **Claim:** The French government imposes a national state of emergency between 2026-10-25 and 2026-11-01.
- **Resolution criterion:** The French Journal Officiel publishes an order declaring a national state of emergency during the event window.
- **Failure condition:** The French Journal Officiel does not publish an order declaring a national state of emergency during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261024-06
- **Issued:** 2026-10-24  ·  **Deadline:** 2026-11-04
- **Domain:** cyber
- **Claim:** On 2026-10-27, a cyberattack exploiting CVE-2026-110447 in Collabora Online will result in a confirmed breach of at least one government or critical infrastructure system, as verified by a third-party cybersecurity firm.
- **Resolution criterion:** A confirmed breach of at least one government or critical infrastructure system due to exploitation of CVE-2026-110447 in Collabora Online occurs between 2026-10-27 and 2026-10-28, as verified by a third-party cybersecurity firm.
- **Failure condition:** No confirmed breach of a government or critical infrastructure system due to exploitation of CVE-2026-110447 in Collabora Online between 2026-10-27 and 2026-10-28, as verified by a third-party cybersecurity firm.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260722-01
- **Issued:** 2026-07-22  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Andy Biggs wins the Arizona gubernatorial general election on 2026-11-05, defeating Katie Hobbs in a recount that confirms his victory by 1,200 votes.
- **Resolution criterion:** The Arizona Secretary of State's official election results page confirms Andy Biggs as the winner of the 2026 gubernatorial election with a final vote margin of at least 1,200 votes over Katie Hobbs, as of 2026-11-05.
- **Failure condition:** the condition stated in this entry's resolution basis — The Arizona Secretary of State's official election results page confirms Andy Biggs as the winner of the 2026 gubernatorial election with a final vote margin of at least 1,200 votes over Katie Hobbs, as of 2026-11-05 — is not met on or before 2026-11-05; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-47
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** The US President or the Government of Iran publicly announces a ceasefire, truce or cessation of hostilities between the United States and Iran between 2026-09-17 and 2026-11-02.
- **Resolution criterion:** TRUE if AP and Reuters both report that the US President or the Government of Iran announced a ceasefire, truce or cessation of US-Iran hostilities between 2026-09-17 and 2026-11-02; otherwise FALSE.
- **Failure condition:** Neither the US President nor the Government of Iran announced a ceasefire, truce or cessation of US-Iran hostilities between 2026-09-17 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-07
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-11-02, the United States government and the government of Iran each publicly confirm acceptance of an agreement under which the Strait of Hormuz is reopened to commercial shipping.
- **Resolution criterion:** TRUE if, between 2026-09-26 and 2026-11-02, both the White House or State Department and the Iranian Foreign Ministry publicly confirm an agreement providing for reopening the Strait of Hormuz, as reported by Reuters and AP.
- **Failure condition:** MISS if, by 2026-11-05, no agreement to reopen the Strait of Hormuz was publicly confirmed by both the US government and the Iranian government within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-30
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** The US and Iranian governments both announce, between 2026-09-28 and 2026-11-03, an agreement or memorandum under which Iran commits to reopening the Strait of Hormuz.
- **Resolution criterion:** TRUE if the White House or State Department and the Iranian Foreign Ministry each publicly confirm, between 2026-09-28 and 2026-11-03, an agreement that includes Iran reopening the Strait of Hormuz, per Reuters, AP or AFP.
- **Failure condition:** No agreement including Iranian reopening of the Strait of Hormuz is confirmed by both the US and Iranian governments between 2026-09-28 and 2026-11-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-31
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** The United States and Iran both publicly confirm a ceasefire or agreement providing for reopening of the Strait of Hormuz between 2026-09-28 and 2026-11-02.
- **Resolution criterion:** TRUE if the White House or State Department and the Iranian foreign ministry each confirm an agreed ceasefire or Hormuz reopening deal between 2026-09-28 and 2026-11-02, reported by both Reuters and AP.
- **Failure condition:** By the end of 2026-11-02 no ceasefire or Hormuz reopening agreement has been confirmed by both the US and Iranian governments.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-46
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Vivek Ramaswamy will win the 2026 Ohio gubernatorial general election held on 2026-11-03.
- **Resolution criterion:** True if the Ohio Secretary of State certified result or an AP race call names Ramaswamy the winner by the deadline; false if Acton wins or the race is uncalled.
- **Failure condition:** Amy Acton is certified or called the winner, or the race remains uncalled at the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-10
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** Between 2026-10-25 and 2026-10-31, at least one report from a hostile side will confirm that a new military mobilization order was issued by Russia.
- **Resolution criterion:** At least one report from a hostile side (RU or UA) will confirm a new military mobilization order issued by Russia during the window
- **Failure condition:** No report from a hostile side confirms a new military mobilization order issued by Russia during the window
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-22
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** In the Knesset election scheduled for 2026-10-27, the lists of the outgoing Netanyahu coalition (Likud, Shas, United Torah Judaism, Otzma Yehudit, Religious Zionism) win a combined 61 seats or more.
- **Resolution criterion:** Israeli Central Elections Committee final results for the 2026-10-27 election give the lists of Likud, Shas, United Torah Judaism, Otzma Yehudit and Religious Zionism, including joint lists containing them, a combined 61 seats or more.
- **Failure condition:** The five listed parties win a combined 60 seats or fewer, or no Knesset election is held on 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-01
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** Between 2026-10-21 and 2026-10-28, a drone strike with reported casualties of 955 will be confirmed by at least three independent sources across hostile sides in the Kyiv theatre.
- **Resolution criterion:** At least three independent sources from distinct hostile sides (RU, UA, AXIS) will report a drone strike in Kyiv with claimed casualties of 955, corroborated by at least one additional source outside the initial reporting cluster.
- **Failure condition:** No such strike with claimed casualties of 955 is confirmed by three or more independent sources across hostile sides within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-02
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** Between 2026-10-21 and 2026-10-28, a magnitude 5.0 or greater earthquake will be recorded in the USGS Significant Quakes database with a depth of less than 50km and epicenter within 100km of Washington state.
- **Resolution criterion:** The USGS Significant Quakes database will list an event with magnitude ≥ 5.0, depth < 50km, and epicenter within 100km of Washington state between 2026-10-21 and 2026-10-28.
- **Failure condition:** No such earthquake is recorded in the USGS Significant Quakes database within the specified window and criteria.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-03
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Between 2026-10-21 and 2026-10-28, the US Treasury will release a public notice announcing the launch of a new savings account program for children under 18, with a minimum initial deposit of $100.
- **Resolution criterion:** The US Treasury publishes a public notice on a government website confirming the launch of a new savings account program for children under 18, with a minimum initial deposit of $100.
- **Failure condition:** No such public notice is published by the US Treasury during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-04
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, a cyberattack exploiting CVE-2026-102489 will be reported by at least two independent sources in the CISA KEV or The Hacker News feed.
- **Resolution criterion:** At least two independent sources (e.g., CISA KEV, The Hacker News) report a cyberattack exploiting CVE-2026-102489 between 2026-10-21 and 2026-10-28.
- **Failure condition:** No such cyberattack is reported by two independent sources within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-05
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, a ransomware attack targeting a water utility or telecom operator will be confirmed by BleepingComputer with a public report detailing the use of Warlock ransomware.
- **Resolution criterion:** BleepingComputer publishes a report between 2026-10-21 and 2026-10-28 confirming a ransomware attack on a water utility or telecom operator using Warlock ransomware.
- **Failure condition:** No such report is published by BleepingComputer during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-06
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Between 2026-10-21 and 2026-10-28, a political scandal involving a US federal official will be reported by both the Guardian World and BBC World with a claim of misuse of public funds.
- **Resolution criterion:** Both Guardian World and BBC World publish a report between 2026-10-21 and 2026-10-28 confirming a political scandal involving a US federal official, including a claim of misuse of public funds.
- **Failure condition:** No such report is published by both outlets during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-07
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-28, a new cyberattack campaign targeting AI gateway services will be confirmed by The Hacker News with a report citing GitLab's AI Gateway vulnerability as the entry point.
- **Resolution criterion:** The Hacker News publishes a report between 2026-10-21 and 2026-10-28 confirming a new cyberattack campaign targeting AI gateway services, citing GitLab's AI Gateway vulnerability as the entry point.
- **Failure condition:** No such report is published by The Hacker News during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-07
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Between 2026-10-25 and 2026-11-01, a new political scandal involving a U.S. government official will be reported by at least two independent outlets with differing political affiliations.
- **Resolution criterion:** At least two independent news outlets with differing political affiliations (e.g., BBC, Guardian, CNBC, NPR) publish a report between 2026-10-25 and 2026-11-01 confirming a political scandal involving a U.S. government official.
- **Failure condition:** No report from two independent outlets with differing political affiliations confirms a political scandal involving a U.S. government official between 2026-10-25 and 2026-11-01.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-36
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** The United States carries out at least one military strike on a target on Iranian land territory, islands included and vessels at sea excluded, between 2026-10-09 and 2026-11-02 UTC.
- **Resolution criterion:** US Central Command, the Pentagon or the White House publicly confirms a US strike on a target on Iranian land territory, islands included, conducted between 2026-10-09 and 2026-11-02 UTC, as carried by Reuters or AP.
- **Failure condition:** No US military strike hits a target on Iranian land territory between 2026-10-09 and 2026-11-02 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-32
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** The United States carries out an air, missile or drone strike on targets located on Iranian land territory, mainland or islands, between 2026-10-10 and 2026-11-02.
- **Resolution criterion:** True if US Central Command or the Pentagon confirms, or at least two of Reuters, AP and AFP report, a US strike on Iranian land territory occurring between 2026-10-10 and 2026-11-02; otherwise false.
- **Failure condition:** US forces strike no target on Iranian land territory between 2026-10-10 and 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-28
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-11-05
- **Domain:** economics/markets
- **Claim:** A major US bank reports a quarterly net loss between 2026-10-26 and 2026-11-02.
- **Resolution criterion:** A US bank with assets over 100 billion reports a net loss for the quarter ending in October 2026.
- **Failure condition:** All major US banks report a net profit for the quarter ending in October 2026.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-08
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-05
- **Domain:** military_conflict
- **Claim:** A Houthi missile or drone successfully strikes a target inside Saudi Arabia between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** A public report confirms a Houthi projectile struck a target inside Saudi Arabia within the event window.
- **Failure condition:** No Houthi projectile successfully strikes a target inside Saudi Arabia during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-09
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** The USGS reports a magnitude 7.0 or greater earthquake between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude 7.0 or higher within the event window.
- **Failure condition:** No magnitude 7.0 or greater earthquake is recorded by the USGS during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-11
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** Turkey halts live broadcasts of a major opposition TV station between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** A public report confirms Turkish authorities halted live broadcasts of a major opposition TV station within the event window.
- **Failure condition:** No major opposition TV station in Turkey has its live broadcasts halted by authorities during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-13
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** The USGS reports a magnitude 6.5 or greater earthquake between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude 6.5 or higher within the event window.
- **Failure condition:** No magnitude 6.5 or greater earthquake is recorded by the USGS during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-52
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** USGS records an earthquake of magnitude 6.0 or greater with Panama in its place name and an origin time between 2026-10-19 and 2026-11-01 UTC.
- **Resolution criterion:** A USGS ComCat query for magnitude 6.0 or greater with origin time from 2026-10-19T00:00Z through 2026-11-01T23:59Z returns at least one event whose place field contains Panama.
- **Failure condition:** No earthquake of magnitude 6.0 or greater with Panama in its USGS place name has an origin time between 2026-10-19 and 2026-11-01 UTC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-03
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** A drone strike on a civilian facility in Gaza City, Palestine, results in at least five confirmed casualties between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** Two independent wire services (e.g., Al Jazeera, BBC World) report at least five confirmed casualties from a drone strike on a civilian facility in Gaza City between 2026-10-27 and 2026-11-03.
- **Failure condition:** Fewer than five confirmed casualties are reported by two independent wire services by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261020-08
- **Issued:** 2026-10-20  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** Between 2026-10-21 and 2026-10-27, at least one confirmed F-35 aircraft will be reported as involved in a military operation in the Iran Theatre.
- **Resolution criterion:** At least one report from a cross-bias confirmed source (Grade A or B) will state that an F-35 aircraft was used in a military operation in the Iran Theatre during the event window.
- **Failure condition:** No cross-bias confirmed report (Grade A or B) states that an F-35 was used in a military operation in the Iran Theatre during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261020-09
- **Issued:** 2026-10-20  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-27, a cyberattack exploiting the ClickFix platform will be confirmed by at least two independent sources across hostile sides.
- **Resolution criterion:** At least two reports from distinct channels across two hostile sides (RU, IL, UA, WEST, AXIS) will confirm a cyberattack using the ClickFix platform during the event window.
- **Failure condition:** No cross-bias confirmed report (Grade A or B) confirms a cyberattack using the ClickFix platform during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261020-10
- **Issued:** 2026-10-20  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-27, a cyberattack on a critical infrastructure provider will result in a service disruption affecting at least 100,000 users in the US or Europe.
- **Resolution criterion:** At least two independent sources (e.g., BleepingComputer, The Hacker News) will confirm a cyberattack on a critical infrastructure provider causing service disruption to 100,000 or more users in the US or Europe during the event window.
- **Failure condition:** No cyberattack on a critical infrastructure provider is confirmed to have caused service disruption to 100,000 or more users in the US or Europe during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-02
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-11-05
- **Domain:** military/conflict
- **Claim:** Between 2026-10-21 and 2026-10-24, at least one report from a hostile side will confirm a drone strike on Kyiv with casualties claimed by Ukrainian sources.
- **Resolution criterion:** At least one report from a hostile side (UA, IL, WEST, AXIS) confirms a drone strike on Kyiv between 2026-10-21 and 2026-10-24, with casualties claimed in at least one corroborating report.
- **Failure condition:** No report from a hostile side confirms a drone strike on Kyiv with casualties claimed between 2026-10-21 and 2026-10-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-03
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-21 and 2026-10-24, the SafePay ransomware will be reported to have compromised at least one additional critical infrastructure organization beyond the 600 already reported.
- **Resolution criterion:** CISA or FBI public advisories confirm that SafePay ransomware has compromised at least one additional critical infrastructure organization beyond the 600 reported on 2026-10-21.
- **Failure condition:** No public advisory confirms SafePay ransomware compromised any new critical infrastructure organization beyond the 600 reported on 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261022-05
- **Issued:** 2026-10-22  ·  **Deadline:** 2026-11-05
- **Domain:** cyber
- **Claim:** Between 2026-10-24 and 2026-10-31, a coordinated cyberattack exploiting the PHP2Shell vulnerability disables at least three critical government systems in the United States, as verified by CISA KEV catalog entries with date-added values in that window.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-24 and 2026-10-31 for at least three vulnerabilities linked to the PHP2Shell exploit.
- **Failure condition:** The CISA KEV catalog does not carry any date-added entries between 2026-10-24 and 2026-10-31 for vulnerabilities tied to the PHP2Shell exploit.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171820ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['PHP2Shell'] with dateAdded in [2026-10-24..2026-10-31] across 1768 catalog rows

### KKR-20261024-07
- **Issued:** 2026-10-24  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** On 2026-10-29, a wildfire in the Four Corners region of the United States will result in at least one fatality, as confirmed by two independent news outlets reporting from the area.
- **Resolution criterion:** At least one fatality occurs due to a wildfire in the Four Corners region of the United States between 2026-10-29 and 2026-10-30, as confirmed by two independent news outlets reporting from the area.
- **Failure condition:** No fatality occurs due to a wildfire in the Four Corners region of the United States between 2026-10-29 and 2026-10-30, as confirmed by two independent news outlets reporting from the area.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261024-58
- **Issued:** 2026-10-24  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** At least one earthquake of magnitude 7.0 or greater occurs anywhere on Earth between 2026-10-25 and 2026-11-02 inclusive, by UTC origin time.
- **Resolution criterion:** The USGS earthquake catalog lists at least one event of magnitude 7.0 or greater with origin time between 2026-10-25 and 2026-11-02 inclusive (UTC), using the magnitude shown at the deadline.
- **Failure condition:** No earthquake of magnitude 7.0 or greater had a UTC origin time between 2026-10-25 and 2026-11-02 inclusive.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261026-01
- **Issued:** 2026-10-26  ·  **Deadline:** 2026-11-05
- **Domain:** economics/markets
- **Claim:** Anthropic files a registration statement on SEC Form S-1 with the US Securities and Exchange Commission between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** The SEC EDGAR database contains a Form S-1 filed by Anthropic with a filing date between 2026-10-27 and 2026-11-03.
- **Failure condition:** Anthropic does not file a Form S-1 with the SEC by 2026-11-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261027-10
- **Issued:** 2026-10-27  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** The Netherlands withdraws from the Eurovision 2027 contest.
- **Resolution criterion:** The European Broadcasting Union confirms the Netherlands has withdrawn from the Eurovision 2027 contest.
- **Failure condition:** The European Broadcasting Union does not confirm the Netherlands has withdrawn from the Eurovision 2027 contest.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261027-11
- **Issued:** 2026-10-27  ·  **Deadline:** 2026-11-05
- **Domain:** disaster
- **Claim:** A forest fire notification is issued by GDACS for a location in Papua New Guinea between 2026-10-27 and 2026-11-03.
- **Resolution criterion:** The GDACS Alerts database carries a forest fire notification for a location in Papua New Guinea with a date between 2026-10-27 and 2026-11-03.
- **Failure condition:** The GDACS Alerts database does not carry a forest fire notification for a location in Papua New Guinea with a date between 2026-10-27 and 2026-11-03.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261027-12
- **Issued:** 2026-10-27  ·  **Deadline:** 2026-11-05
- **Domain:** political
- **Claim:** The CDC deputy director appointed by Trump resigns from office.
- **Resolution criterion:** The CDC confirms the resignation of the Trump-appointed deputy director.
- **Failure condition:** The CDC does not confirm the resignation of the Trump-appointed deputy director.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261027-13
- **Issued:** 2026-10-27  ·  **Deadline:** 2026-11-05
- **Domain:** crime
- **Claim:** A man is arrested for sending suspicious powder to the US Congress.
- **Resolution criterion:** The FBI or US Capitol Police confirms an arrest for sending suspicious powder to the US Congress.
- **Failure condition:** The FBI or US Capitol Police does not confirm an arrest for sending suspicious powder to the US Congress.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).
