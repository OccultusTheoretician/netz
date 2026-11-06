# KKR RESOLUTION AUDIT PACKET
Generated 061718Z NOV 26 · 212 projections (part 3 of 4; packet total 1268) past deadline, awaiting adjudication.

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

### KKR-20261018-47
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-10-29
- **Domain:** disaster
- **Claim:** Between 2026-10-19 and 2026-10-26, the center of Hurricane Trudy makes landfall on the Mexican coast with maximum sustained winds of at least 74 mph.
- **Resolution criterion:** NHC advisories or the NHC Tropical Cyclone Report for Trudy state that its center crossed the Mexican coast between 2026-10-19 and 2026-10-26 with maximum sustained winds of at least 74 mph.
- **Failure condition:** Trudy does not cross the Mexican coast as a hurricane with sustained winds of at least 74 mph between 2026-10-19 and 2026-10-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260724-04
- **Issued:** 2026-07-24  ·  **Deadline:** 2026-10-30
- **Domain:** economics
- **Claim:** The 30-year US Treasury yield closes at or above 6.00 percent on at least one trading day between 2026-07-27 and 2026-10-30.
- **Resolution criterion:** TRUE if the daily closing 30-year Treasury yield reported by the US Treasury or major financial press reaches 6.00 percent or higher on any trading day in the window; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if the daily closing 30-year Treasury yield reported by the US Treasury or major financial press reaches 6.00 percent or higher on any trading day in the window; else FALSE — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261106T171720ZZ - sha256 9cee4a11cad003f6...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 68 business days in window; max BC_30YEAR 5.67 on 2026-10-07; threshold >= 6.00; 0 day(s) satisfying

### KKR-20260726-04
- **Issued:** 2026-07-26  ·  **Deadline:** 2026-10-30
- **Domain:** crime_security
- **Claim:** German authorities announce the arrest or formal charging of a suspect in the Berlin Pride vehicle attack between 2026-07-26 and 2026-10-30.
- **Resolution criterion:** German police or prosecutors publicly confirm an arrest or charge tied to the Berlin Pride ramming, reported by two independent wire services in the window.
- **Failure condition:** the condition stated in this entry's resolution basis — German police or prosecutors publicly confirm an arrest or charge tied to the Berlin Pride ramming, reported by two independent wire services in the window — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-27
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The upper bound of the US federal funds target range is above 3.75 percent on 2026-10-30.
- **Resolution criterion:** Resolved from the FOMC implementation note in effect on 2026-10-30. Yes if the upper bound of the target range exceeds 3.75 percent on that date.
- **Failure condition:** the condition stated in this entry's resolution basis — the FOMC implementation note in effect — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-29
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds a vulnerability in the n8n workflow automation platform to its Known Exploited Vulnerabilities catalog between 2026-07-28 and 2026-10-30.
- **Resolution criterion:** Resolved from the CISA Known Exploited Vulnerabilities catalog on 2026-10-30. Yes if any entry naming n8n carries a date-added inside the window.
- **Failure condition:** the condition stated in this entry's resolution basis — the CISA Known Exploited Vulnerabilities catalog — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171721ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['n8n'] with dateAdded in [2026-07-28..2026-10-30] across 1768 catalog rows

### KKR-20260728-04
- **Issued:** 2026-07-28  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The upper bound of the US federal funds target range is above 3.75 percent on 2026-10-30.
- **Resolution criterion:** Resolved from the FOMC implementation note in effect on 2026-10-30. Yes if the upper bound exceeds 3.75 percent.
- **Failure condition:** the condition stated in this entry's resolution basis — the FOMC implementation note in effect — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260728-07
- **Issued:** 2026-07-28  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** A US healthcare or medical-billing breach affecting more than 5,000,000 individuals is posted to the HHS breach portal between 2026-07-29 and 2026-10-30.
- **Resolution criterion:** Resolved from the HHS Office for Civil Rights breach portal on 2026-10-30. Yes if any entry inside the window reports over 5,000,000 individuals affected.
- **Failure condition:** the condition stated in this entry's resolution basis — the HHS Office for Civil Rights breach portal — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260728-09
- **Issued:** 2026-07-28  ·  **Deadline:** 2026-10-30
- **Domain:** crime/security
- **Claim:** At least one person is charged in connection with either shooting near the United States consulate in Toronto, on or before 2026-10-30.
- **Resolution criterion:** Resolved from Toronto Police Service releases or concurrent reporting by two major wires as of 2026-10-30. Yes if any charge has been laid for either incident.
- **Failure condition:** the condition stated in this entry's resolution basis — Toronto Police Service releases or concurrent reporting by two major wires as of 2026-10-30 — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-11
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds a Gitea remote-code-execution vulnerability to its Known Exploited Vulnerabilities catalog between 2026-07-30 and 2026-10-30.
- **Resolution criterion:** Resolved from the CISA KEV catalog JSON on 2026-10-30. Yes if any entry has vendorProject or product matching Gitea and dateAdded between 2026-07-30 and 2026-10-30.
- **Failure condition:** the condition stated in this entry's resolution basis — the CISA KEV catalog JSON — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171722ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Gitea'] with dateAdded in [2026-07-30..2026-10-30] across 1768 catalog rows - CVE-2026-60004

### KKR-20260729-12
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds a vBulletin vulnerability to its Known Exploited Vulnerabilities catalog between 2026-07-30 and 2026-10-30.
- **Resolution criterion:** Resolved from the CISA KEV catalog JSON on 2026-10-30. Yes if any entry has vendorProject or product matching vBulletin and dateAdded inside the window.
- **Failure condition:** the condition stated in this entry's resolution basis — the CISA KEV catalog JSON — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171723ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['vBulletin'] with dateAdded in [2026-07-30..2026-10-30] across 1768 catalog rows

### KKR-20260729-16
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** GDACS issues a Red alert for any event located in Japan between 2026-07-30 and 2026-10-30.
- **Resolution criterion:** Resolved from the GDACS alert feed on 2026-10-30. Yes if any event with country Japan carries alertlevel Red and a date inside the window.
- **Failure condition:** the condition stated in this entry's resolution basis — the GDACS alert feed — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - gdacs - fetched 20261106T171725ZZ - sha256 c91935d33880d41c...
  - instrument: https://www.gdacs.org/xml/rss.xml
  - observed: no live match in 234 feed items — the RSS is a current-state feed; absence now does not adjudicate the whole window. Archive check is the operator's.

### KKR-20260729-17
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The United States 10-year Treasury par yield closes at or above 4.90 percent on at least one business day between 2026-07-30 and 2026-10-30.
- **Resolution criterion:** Resolved from the Treasury daily par yield curve XML, field BC_10YEAR, on 2026-10-30. Yes if any business day in the window closed at or above 4.90.
- **Failure condition:** the condition stated in this entry's resolution basis — the Treasury daily par yield curve XML, field BC_10YEAR, — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261106T171726ZZ - sha256 9cee4a11cad003f6...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 65 business days in window; max BC_10YEAR 5.31 on 2026-10-05; threshold >= 4.90; 36 day(s) satisfying

### KKR-20260729-18
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The ECB main refinancing operations rate on 2026-10-30 is unchanged from its level on 2026-07-29.
- **Resolution criterion:** Resolved from the ECB Data Portal series FM.D.U2.EUR.4F.KR.MRR_FR.LEV on 2026-10-30. Yes if OBS_VALUE on that date equals the 2026-07-29 value.
- **Failure condition:** the condition stated in this entry's resolution basis — the ECB Data Portal series FM.D.U2.EUR.4F.KR.MRR_FR.LEV — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-20
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** A United States sanctions action designating Iranian persons or entities is published in the Federal Register between 2026-07-30 and 2026-10-30.
- **Resolution criterion:** Resolved from the Federal Register documents API on 2026-10-30, agency Treasury or State. Yes if any document published in the window designates Iranian persons or entities.
- **Failure condition:** the condition stated in this entry's resolution basis — the Federal Register documents API on 2026-10-30, agency Treasury or State — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - fedreg - fetched 20261106T171726ZZ - sha256 591dcb4eae75447e...
  - instrument: https://www.federalregister.gov/api/v1/documents.json?per_page=20&conditions[term]=Iranian&conditions[publication_date][gte]=2026-07-30&conditions[publication_date][lte]=2026-10-30&conditions[agencies][]=treasury-department&conditions[agencies][]=state-department
  - observed: 29 document(s) for term 'Iranian' in window; ['Iranian Transactions and Sanctions Regulations', 'Iranian Transactions and Sanctions Regulations', 'Iranian Transactions and Sanctions Regulations']

### KKR-20260730-04
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** Situational Awareness LP or Leopold Aschenbrenner publicly announces that the fund is winding down, closing or returning external capital, between 2026-07-31 and 2026-10-30.
- **Resolution criterion:** Resolved on 2026-10-30: hit if at least two of Bloomberg, CNBC, FT or Reuters report an announced wind-down, closure or return of external capital for the fund, dated in the window; miss otherwise.
- **Failure condition:** Fewer than two of Bloomberg, CNBC, FT and Reuters report an announced wind-down, closure or return of external capital for Situational Awareness LP dated in the window, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-06
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** crime/security
- **Claim:** The Pakistani armed forces or ISPR publicly announce a new named military operation in Khyber Pakhtunkhwa or the former tribal districts between 2026-07-31 and 2026-10-30.
- **Resolution criterion:** Resolved on 2026-10-30: hit if ISPR or the Pakistani government announces a named operation in those areas within the window, per two major wires or ispr.gov.pk; miss otherwise.
- **Failure condition:** No named military operation in Khyber Pakhtunkhwa or the former tribal districts is announced by ISPR or the Pakistani government in the window, per ispr.gov.pk or two major wires, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-12
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** economic
- **Claim:** Front-month Brent crude futures settle above 100.00 US dollars per barrel on at least one trading day between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** True if ICE front-month Brent settlement exceeds 100.00 dollars on any session from 2026-08-06 through 2026-10-30, per exchange or major financial press data.
- **Failure condition:** No ICE front-month Brent settlement exceeds 100.00 USD on any session 2026-08-06 through 2026-10-30, per exchange or major financial press settlement data as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-15
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** Public reporting attributes exploitation of Cisco CVE-2026-20316 to a specifically named nation-state actor or tracked threat group between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** True if a report from Cisco Talos, CISA, or a major security vendor published between 2026-08-06 and 2026-10-30 names a specific state actor or tracked group exploiting CVE-2026-20316.
- **Failure condition:** No report from Cisco Talos, CISA, or a major security vendor published 2026-08-06 through 2026-10-30 names a specific state actor or tracked group exploiting CVE-2026-20316, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-17
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** economic
- **Claim:** The Federal Open Market Committee announces a reduction in the federal funds target range at a scheduled meeting held between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** True if an FOMC statement issued between 2026-08-06 and 2026-10-30 announces a lower target range for the federal funds rate.
- **Failure condition:** No FOMC statement issued 2026-08-06 through 2026-10-30 announces a lower federal funds target range, as read at federalreserve.gov on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-18
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** The US Senate confirms Todd Blanche as Attorney General between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** True if the Senate record shows a successful confirmation vote seating Todd Blanche as Attorney General between 2026-08-06 and 2026-10-30.
- **Failure condition:** The Senate record shows no successful confirmation vote seating Todd Blanche as Attorney General between 2026-08-06 and 2026-10-30, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260730-20
- **Issued:** 2026-07-30  ·  **Deadline:** 2026-10-30
- **Domain:** crime_security
- **Claim:** A single attack in Pakistan kills at least 10 police or military personnel between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** True if credible international reporting confirms one attack in Pakistan between 2026-08-06 and 2026-10-30 killing 10 or more police or military personnel.
- **Failure condition:** No single attack in Pakistan killing 10 or more police or military personnel between 2026-08-06 and 2026-10-30 is confirmed by credible international reporting, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-08
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** FIFA publicly suspends or withdraws the World Cup stake-sale investment plan between 2026-08-07 and 2026-10-30 amid UEFA opposition and senior adviser resignations
- **Resolution criterion:** Two of Reuters, AP, BBC, or the Guardian report FIFA suspending or withdrawing the World Cup investment or stake-sale plan, dated between 2026-08-07 and 2026-10-30
- **Failure condition:** Fewer than two of Reuters, AP, BBC and the Guardian report FIFA suspending or withdrawing the plan dated 2026-08-07 through 2026-10-30, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-10
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** crime_security
- **Claim:** The mayor of St Paul, Minnesota resigns or announces resignation between 2026-08-07 and 2026-10-30 following sexual harassment allegations by two police officials
- **Resolution criterion:** Two major outlets or an official city statement report the St Paul mayor resigning or announcing resignation, dated between 2026-08-07 and 2026-10-30
- **Failure condition:** No official city statement and no two-outlet reporting dated 2026-08-07 through 2026-10-30 confirms the St Paul mayor resigning or announcing resignation, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-16
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** Between 2026-07-31 and 2026-10-30, the Federal Reserve will announce an increase in the federal funds rate.
- **Resolution criterion:** True if the Federal Reserve announces an increase in the federal funds rate, as reported by a major financial outlet, between 2026-07-31 and 2026-10-30; otherwise false.
- **Failure condition:** No Federal Reserve announcement of an increase in the federal funds rate dated 2026-07-31 through 2026-10-30 is reported by a major financial outlet, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-21
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** military_conflict
- **Claim:** A named international monitor, the Gaza Board of Peace, or the US government publicly confirms that Hamas has physically handed over heavy weapons between 2026-08-07 and 2026-10-30.
- **Resolution criterion:** True if an official statement from the Board of Peace, a named international monitoring body, or the US government confirms a completed heavy-weapons handover in that window. Announcements of agreement alone do not resolve true.
- **Failure condition:** No official statement from the Gaza Board of Peace, a named international monitoring body, or the US government dated 2026-08-07 through 2026-10-30 confirms a completed physical handover of heavy weapons by Hamas; announcements of agreement alone do not resolve true; that reading on 2026-10-30 scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260731-26
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds the JetBrains TeamCity remote code execution vulnerability disclosed in late July 2026 to its Known Exploited Vulnerabilities catalog between 2026-08-07 and 2026-10-30.
- **Resolution criterion:** True if the CISA KEV catalog shows an entry for that TeamCity vulnerability with a date added between 2026-08-07 and 2026-10-30.
- **Failure condition:** The CISA KEV catalog shows no entry for the late July 2026 JetBrains TeamCity remote code execution vulnerability with a date added between 2026-08-07 and 2026-10-30, as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171727ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['TeamCity'] with dateAdded in [2026-08-07..2026-10-30] across 1768 catalog rows

### KKR-20260731-27
- **Issued:** 2026-07-31  ·  **Deadline:** 2026-10-30
- **Domain:** economic
- **Claim:** The CBOE Volatility Index closes above 35.00 on at least one trading day between 2026-08-07 and 2026-10-30.
- **Resolution criterion:** True if the official VIX close exceeds 35.00 on any session from 2026-08-07 through 2026-10-30, per CBOE or major financial press data.
- **Failure condition:** The official CBOE VIX close does not exceed 35.00 on any session 2026-08-07 through 2026-10-30, per CBOE or major financial press data as read on 2026-10-30; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-03
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** The US Department of Defense or the White House publicly confirms US military strikes on targets inside Iran between 2026-08-08 and 2026-10-30.
- **Resolution criterion:** Resolved from defense.gov news releases and whitehouse.gov briefing transcripts on 2026-10-30. Yes if any on-record item published in the window confirms US strikes on Iranian territory.
- **Failure condition:** the condition stated in this entry's resolution basis — any on-record item published in the window confirms US strikes on Iranian territory — is not met on or before 2026-10-30 as read from defense.gov news releases and whitehouse.gov briefing transcripts; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-05
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** ICE Brent front-month crude settles above 110.00 US dollars per barrel on at least one trading day between 2026-08-10 and 2026-10-30.
- **Resolution criterion:** Resolved from the official ICE Brent front-month settlement series read on 2026-10-30. Yes if any settlement in the window is above 110.00.
- **Failure condition:** the condition stated in this entry's resolution basis — any settlement in the window is above 110.00 — is not met on or before 2026-10-30 as read from the official ICE Brent front-month settlement series read; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-09
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds an Adobe Campaign Classic vulnerability to its Known Exploited Vulnerabilities catalog between 2026-08-08 and 2026-10-30.
- **Resolution criterion:** Resolved from the CISA KEV catalog JSON on 2026-10-30. Yes if any entry has vendorProject Adobe, product matching Campaign Classic, and dateAdded inside the window.
- **Failure condition:** the condition stated in this entry's resolution basis — any entry has vendorProject Adobe, product matching Campaign Classic, and dateAdded inside the window — is not met on or before 2026-10-30 as read from the CISA KEV catalog JSON; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171728ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 3 matching entries for ['Campaign Classic', 'Adobe'] with dateAdded in [2026-08-08..2026-10-30] across 1768 catalog rows - CVE-2026-48356, CVE-2026-71362, CVE-2026-75650

### KKR-20260801-22
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** Commercial vessel transit through the Strait of Hormuz is suspended for 48 or more consecutive hours between 2026-08-02 and 2026-10-30.
- **Resolution criterion:** YES if at least two major international wire services report suspension of commercial transit through the Strait of Hormuz lasting 48 or more consecutive hours between 2026-08-02 and 2026-10-30; otherwise NO.
- **Failure condition:** the condition stated in this entry's resolution basis — at least two major international wire services report suspension of commercial transit through the Strait of Hormuz lasting 48 or more consecutive hours between 2026-08-02 and 2026-10-30 — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-26
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds an Adobe Campaign Classic vulnerability first disclosed between 2026-07-28 and 2026-08-01 to the Known Exploited Vulnerabilities catalog between 2026-08-02 and 2026-10-30.
- **Resolution criterion:** YES if the CISA KEV catalog lists an Adobe Campaign Classic entry with dateAdded between 2026-08-02 and 2026-10-30; otherwise NO.
- **Failure condition:** the condition stated in this entry's resolution basis — the CISA KEV catalog lists an Adobe Campaign Classic entry with dateAdded between 2026-08-02 and 2026-10-30 — is not met on or before 2026-10-30; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171729ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Adobe Campaign Classic'] with dateAdded in [2026-08-02..2026-10-30] across 1768 catalog rows

### KKR-20260822-17
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog carries an entry for CVE-2026-19478 with a dateAdded value between 2026-08-21 and 2026-10-23.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed contains cveID CVE-2026-19478 with a dateAdded on or after 2026-08-21 and on or before 2026-10-23; otherwise FALSE.
- **Failure condition:** CVE-2026-19478 is absent from the KEV catalog at the deadline, or carries a dateAdded outside 2026-08-21 through 2026-10-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-11
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-30
- **Domain:** economics_markets
- **Claim:** The FOMC raises the federal funds target range at the meeting concluding 2026-09-16 or the meeting concluding 2026-10-28. Reference: target range 3.50 to 3.75 percent in effect at seal on 2026-09-01.
- **Resolution criterion:** The FOMC implementation note for 2026-09-16 or for 2026-10-28 sets a target range whose upper bound exceeds 3.75 percent; reference 3.50 to 3.75 at seal.
- **Failure condition:** Both implementation notes leave the target range upper bound at or below 3.75 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-16
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-30
- **Domain:** economic
- **Claim:** The Federal Reserve raises the federal funds target range above its current 3.50-3.75 percent level at the October 27-28, 2026 FOMC meeting. Reference: 3.50-3.75 percent, held since the July 2026 meeting.
- **Resolution criterion:** The FOMC post-meeting statement released 2026-10-28 sets the federal funds target range above 3.50-3.75 percent, per the Federal Reserve press release.
- **Failure condition:** The FOMC statement of 2026-10-28 holds the target range at 3.50-3.75 percent or cuts it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-35
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range above 3.75 to 4.00 percent at its scheduled meeting concluding 2026-10-28. Reference: upper limit 4.00 percent at seal on 2026-09-17.
- **Resolution criterion:** The Federal Reserve FOMC statement dated 2026-10-28 announces an increase to the federal funds target range; FRED DFEDTARU for 2026-10-29 exceeds 4.00. Reference: upper limit 4.00 percent at seal.
- **Failure condition:** The FOMC meeting concluding 2026-10-28 ends with the federal funds target range unchanged or lowered.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-14
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At its scheduled meeting concluding 2026-10-28, the FOMC raises the federal funds target range above the 3.75 to 4.00 percent range in effect on the packet date. Reference: upper limit 4.00 percent on 2026-09-23.
- **Resolution criterion:** The FOMC statement released 2026-10-28 on federalreserve.gov sets a target range upper limit of 4.25 percent or higher, and FRED series DFEDTARU shows 4.25 or higher effective 2026-10-29.
- **Failure condition:** The 2026-10-28 FOMC statement holds the target range at 3.75 to 4.00 percent or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-08
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At its scheduled meeting concluding 2026-10-28, the FOMC raises the federal funds target range above the 3.75 to 4.00 percent range in effect on the packet date.
- **Resolution criterion:** TRUE if the FOMC statement released 2026-10-28 on federalreserve.gov announces a target range whose upper bound exceeds 4.00 percent; FALSE if the range is held, lowered, or no decision is announced that day.
- **Failure condition:** The FOMC statement of 2026-10-28 leaves the target range at 3.75 to 4.00 percent or lowers it, or no decision is announced that day.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-10
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC statement released on 2026-10-28 raises the federal funds target range above 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** TRUE if the FOMC statement dated 2026-10-28 on federalreserve.gov sets a federal funds target range whose upper bound exceeds 4.00 percent; a hold or a cut resolves FALSE. Reference: 3.75 to 4.00 percent on the packet date.
- **Failure condition:** MISS if the 2026-10-28 FOMC statement leaves the target range at 3.75 to 4.00 percent or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-28
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range by at least 25 basis points at its meeting ending 2026-10-28. Reference: 4.00 percent upper bound on the packet date.
- **Resolution criterion:** TRUE if FRED series DFEDTARU reads 4.25 or higher for 2026-10-29, reflecting the 2026-10-28 FOMC decision. Reference: 4.00 percent upper bound on the packet date.
- **Failure condition:** The FOMC leaves the target range upper bound at or below 4.00 percent at the meeting ending 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-02
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** Between 2026-10-20 and 2026-10-27, the USGS will record a magnitude 6.0 or higher earthquake in the Pacific Northwest region (Washington, Oregon, or Northern California).
- **Resolution criterion:** The USGS Significant Quakes feed will list a magnitude 6.0 or higher earthquake with epicenter in Washington, Oregon, or Northern California between 2026-10-20 and 2026-10-27.
- **Failure condition:** No magnitude 6.0 or higher earthquake is recorded in the specified region during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171729ZZ - sha256 a46715e4f5335370...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-20&endtime=2026-10-28&minlatitude=32.5&maxlatitude=42.0&minlongitude=-124.5&maxlongitude=-114.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260927-15
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** The USGS earthquake catalog records an earthquake of magnitude 6.5 or greater with epicenter within 200 km of USGS event us6000txpi (the 2026-09-26 M6.6 near Tadine, New Caledonia) and origin time between 2026-09-28 and 2026-10-27 UTC.
- **Resolution criterion:** TRUE if a USGS FDSN event query returns at least one event with USGS preferred magnitude 6.5 or greater, epicenter within 200 km of event us6000txpi, and origin time from 2026-09-28T00:00Z through 2026-10-27T23:59Z.
- **Failure condition:** No USGS-cataloged event of magnitude 6.5 or greater occurs within 200 km of us6000txpi between 2026-09-28 and 2026-10-27 UTC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171729ZZ - sha256 e3b0c44298fc1c14...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&eventid=preferred
  - observed: event id preferred could not be resolved to an epicentre: <HTTPError 404: 'Not Found'>

### KKR-20260928-10
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** Between 2026-10-20 and 2026-10-27, a new volcanic eruption will be reported in the CISA KEV catalog as a confirmed event.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-20 and 2026-10-27 for a new volcanic eruption event.
- **Failure condition:** No new volcanic eruption is listed in the CISA KEV catalog with a date-added value between 2026-10-20 and 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-08
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** Between 2026-10-20 and 2026-10-26, at least one report from a hostile side will confirm that a cyberattack exploited CVE-2026-86950 in a real-world attack.
- **Resolution criterion:** At least one report from a hostile side (AXIS, WEST, RU, or IL) will confirm that CVE-2026-86950 was exploited in a real-world cyberattack during the window
- **Failure condition:** No report from a hostile side confirms exploitation of CVE-2026-86950 in a real-world cyberattack during the window
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-03
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** Between 2026-10-20 and 2026-10-27, the CISA KEV catalog will list at least one new exploited vulnerability with a severity rating of 'Critical' and a date-added value between 2026-10-20 and 2026-10-27.
- **Resolution criterion:** The CISA KEV catalog lists at least one new exploited vulnerability with a severity rating of 'Critical' and a date-added value between 2026-10-20 and 2026-10-27.
- **Failure condition:** The CISA KEV catalog does not list any new exploited vulnerability with a severity rating of 'Critical' and a date-added value between 2026-10-20 and 2026-10-27.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171730ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Critical'] with dateAdded in [2026-10-20..2026-10-27] across 1768 catalog rows

### KKR-20260930-13
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its scheduled meeting concluding 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** True if FRED series DFEDTARU reads 4.25 or higher for 2026-10-29; false if it reads 4.00 or lower. Reference: upper limit 4.00 percent on the packet date.
- **Failure condition:** The target range upper limit is still 4.00 percent or lower on 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-30
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC holds the federal funds target range at 3.75 to 4.00 percent at its meeting concluding 2026-10-28.
- **Resolution criterion:** True if FRED series DFEDTARU reads 4.00 for 2026-10-29, reflecting the 2026-10-28 decision; any other value is false. Reference: 4.00 percent upper bound held at seal on 2026-09-30.
- **Failure condition:** The FOMC raises or lowers the federal funds target range at its meeting concluding 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-44
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The Federal Open Market Committee raises the federal funds target range at its meeting concluding on 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** The FOMC statement released 2026-10-28 sets a target range whose upper bound is above 4.00 percent. Reference: range was 3.75 to 4.00 percent on the packet date.
- **Failure condition:** The FOMC statement released 2026-10-28 leaves the target range at 3.75 to 4.00 percent or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-39
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At its meeting of 2026-10-27 to 2026-10-28, the FOMC will raise the federal funds target range above 3.75 to 4.00 percent, with the decision announced on 2026-10-28. Reference: 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** The Federal Reserve FOMC statement released 2026-10-28 sets a federal funds target range above 3.75 to 4.00 percent. Reference: 3.75 to 4.00 percent on the packet date.
- **Failure condition:** The FOMC statement of 2026-10-28 leaves the target range at 3.75 to 4.00 percent or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-19
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding on 2026-10-28. Reference: target range of 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** TRUE if the FOMC statement of 2026-10-28 lifts the target range upper limit above 4.00 percent, so that FRED series DFEDTARU reads above 4.00 on 2026-10-29. Reference: 4.00 percent on the packet date.
- **Failure condition:** The upper limit of the federal funds target range is still 4.00 percent or lower after the 2026-10-28 decision.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-37
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range above 3.75 to 4.00 percent (Reference: upper bound 4.00 percent on the packet date).
- **Resolution criterion:** TRUE if the FOMC statement issued on 2026-10-28 sets the federal funds target range upper bound above 4.00 percent, per federalreserve.gov or FRED series DFEDTARU; otherwise FALSE. Reference: 4.00 percent at seal.
- **Failure condition:** The FOMC holds the target range at 3.75 to 4.00 percent, or lowers it, at the meeting concluding on 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-18
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** A USGS Significant Quake of magnitude 4.0 or higher occurs in Washington state between 2026-10-20 and 2026-10-27
- **Resolution criterion:** A USGS Significant Quake of magnitude 4.0 or higher occurs in Washington state between 2026-10-20 and 2026-10-27
- **Failure condition:** No USGS Significant Quake of magnitude 4.0 or higher occurs in Washington state between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-19
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** The US Supreme Court issues a ruling in the big oil climate damage lawsuit between 2026-10-20 and 2026-10-27
- **Resolution criterion:** The US Supreme Court issues a ruling in the big oil climate damage lawsuit between 2026-10-20 and 2026-10-27
- **Failure condition:** The US Supreme Court does not issue a ruling in the big oil climate damage lawsuit between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-20
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** military
- **Claim:** A drone or missile attack causes at least one confirmed casualty in Kyiv between 2026-10-20 and 2026-10-27
- **Resolution criterion:** A drone or missile attack causes at least one confirmed casualty in Kyiv between 2026-10-20 and 2026-10-27
- **Failure condition:** No drone or missile attack causes at least one confirmed casualty in Kyiv between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-21
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** military
- **Claim:** A breach of the Strait of Hormuz by Iranian forces is confirmed by two hostile sides between 2026-10-20 and 2026-10-27
- **Resolution criterion:** A breach of the Strait of Hormuz by Iranian forces is confirmed by two hostile sides between 2026-10-20 and 2026-10-27
- **Failure condition:** A breach of the Strait of Hormuz by Iranian forces is not confirmed by two hostile sides between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-22
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** A forest fire in Brazil is confirmed by GDACS between 2026-10-20 and 2026-10-27
- **Resolution criterion:** A forest fire in Brazil is confirmed by GDACS between 2026-10-20 and 2026-10-27
- **Failure condition:** A forest fire in Brazil is not confirmed by GDACS between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-26
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its meeting ending 2026-10-28. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** FRED series DFEDTARU, the target range upper limit, reads 4.25 or higher for 2026-10-29. Reference: 4.00 percent on the packet date.
- **Failure condition:** The federal funds target range upper limit is 4.00 percent or lower on 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-58
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At its meeting concluding on 2026-10-28, the FOMC raises the federal funds target range above the 3.75-4.00 percent range in force at seal.
- **Resolution criterion:** TRUE if the FOMC statement released on 2026-10-28 sets a target range upper bound above 4.00 percent, shown by FRED series DFEDTARU for 2026-10-29; otherwise FALSE. Reference: 3.75-4.00 percent on the packet date.
- **Failure condition:** The federal funds target range upper bound remains at or below 4.00 percent after the 2026-10-28 FOMC decision.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-08
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** Between 2026-10-22 and 2026-10-28, a confirmed earthquake of magnitude 5.0 or higher will be recorded by the USGS in the Pacific Northwest.
- **Resolution criterion:** The USGS Significant Quakes catalog will carry a date-added value between 2026-10-22 and 2026-10-28 for an earthquake of magnitude 5.0 or higher in the Pacific Northwest.
- **Failure condition:** The USGS Significant Quakes catalog contains no entry with a date-added value between 2026-10-22 and 2026-10-28 for an earthquake of magnitude 5.0 or higher in the Pacific Northwest.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171731ZZ - sha256 14cd4f6145088095...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-22&endtime=2026-10-29&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=5.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261006-30
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC statement released on 2026-10-28 leaves the federal funds target range unchanged at 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** The Federal Reserve statement of 2026-10-28, or FRED series DFEDTARU for 2026-10-29, shows the target range upper limit at 4.00 percent. Reference: 4.00 percent on the packet date.
- **Failure condition:** The FOMC raises or lowers the federal funds target range at its meeting concluding 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-46
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** Between 2026-10-07 and 2026-10-28, the CISA Known Exploited Vulnerabilities catalog gains at least one entry whose vendorProject is Rejetto.
- **Resolution criterion:** The CISA KEV catalog JSON carries at least one entry with vendorProject Rejetto and a dateAdded value between 2026-10-07 and 2026-10-28 inclusive.
- **Failure condition:** CISA adds no Rejetto entry to the KEV catalog with a dateAdded value between 2026-10-07 and 2026-10-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171732ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Rejetto'] with dateAdded in [2026-10-07..2026-10-28] across 1768 catalog rows

### KKR-20261006-47
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** Between 2026-10-07 and 2026-10-28, the Kenyan Ministry of Health or the WHO announces at least one further laboratory-confirmed Ebola case in Kenya beyond those announced on or before 2026-10-06.
- **Resolution criterion:** The Kenyan Ministry of Health or the WHO announces between 2026-10-07 and 2026-10-28 at least one new laboratory-confirmed Ebola case in Kenya beyond those already announced on or before 2026-10-06.
- **Failure condition:** No additional laboratory-confirmed Ebola case in Kenya, beyond those announced on or before 2026-10-06, is announced between 2026-10-07 and 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-60
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28, lifting the upper bound above 4.00 percent. Reference: 3.75 to 4.00 percent target range at seal on 2026-10-06.
- **Resolution criterion:** YES if the FOMC statement issued 2026-10-28 for the meeting of 2026-10-27 to 2026-10-28 sets an upper bound above 4.00 percent, per federalreserve.gov or FRED series DFEDTARU. Reference: 4.00 percent at seal.
- **Failure condition:** The target range announced on 2026-10-28 has an upper bound of 4.00 percent or lower.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-28
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** CISA adds at least one Atlassian vulnerability to its Known Exploited Vulnerabilities catalog with a date added between 2026-10-07 and 2026-10-28.
- **Resolution criterion:** The CISA KEV catalog carries at least one entry with vendorProject Atlassian and a dateAdded value between 2026-10-07 and 2026-10-28 inclusive.
- **Failure condition:** No Atlassian vulnerability is added to the CISA KEV catalog with a date added between 2026-10-07 and 2026-10-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171733ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Atlassian'] with dateAdded in [2026-10-07..2026-10-28] across 1768 catalog rows - CVE-2026-21589

### KKR-20261008-04
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** Between 2026-10-21 and 2026-10-28, the 10-year Treasury yield will exceed 5.5% on at least one trading day.
- **Resolution criterion:** The 10-year Treasury yield exceeds 5.5% on at least one weekday between 2026-10-21 and 2026-10-28, as reported by the U.S. Department of the Treasury or FRED.
- **Failure condition:** The 10-year Treasury yield never exceeds 5.5% on any weekday between 2026-10-21 and 2026-10-28.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261106T171735ZZ - sha256 9cee4a11cad003f6...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 6 business days in window; max BC_10YEAR 5.13 on 2026-10-21; threshold > 5.50; 0 day(s) satisfying

### KKR-20261008-34
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The Federal Open Market Committee raises the federal funds target range at its scheduled meeting concluding 2026-10-28. Reference: target range upper bound 4.00 percent on the packet date.
- **Resolution criterion:** FRED series DFEDTARU shows a value above 4.00 for 2026-10-29, reflecting a target range increase announced in the FOMC statement of 2026-10-28.
- **Failure condition:** The FOMC leaves the target range upper bound at or below 4.00 percent at the meeting concluding 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-01
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** Between 2026-10-25 and 2026-10-28, the FBI will publicly confirm the disruption of Chinese hacking tools used to breach critical infrastructure, citing the Flax Typhoon campaign.
- **Resolution criterion:** The FBI publicly confirms the disruption of Chinese hacking tools used to breach critical infrastructure, specifically referencing the Flax Typhoon campaign, between 2026-10-25 and 2026-10-28.
- **Failure condition:** The FBI does not publicly confirm the disruption of Chinese hacking tools used to breach critical infrastructure, or does not reference the Flax Typhoon campaign, within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-49
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** At least one person is killed inside Saudi Arabia by a Houthi missile or drone strike that occurs between 2026-10-12 and 2026-10-26.
- **Resolution criterion:** Reuters and AP both report that at least one person was killed inside Saudi Arabia by a Houthi missile or drone strike occurring between 2026-10-12 and 2026-10-26 inclusive.
- **Failure condition:** No person was killed inside Saudi Arabia by a Houthi missile or drone strike occurring between 2026-10-12 and 2026-10-26.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-08
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds a date-added value for a critical infrastructure vulnerability between 2026-10-20 and 2026-10-27
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-20 and 2026-10-27
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-10-20 and 2026-10-27
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-32
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** At least one earthquake of magnitude 6.0 or greater occurs within 200 km of the epicenter of the M 7.7 Panama earthquake (USGS event us6000u18k) between 2026-10-13 and 2026-10-27 UTC.
- **Resolution criterion:** True if the USGS earthquake catalog lists at least one event of magnitude 6.0 or greater within 200 km of the epicenter of event us6000u18k, with origin time between 2026-10-13 and 2026-10-27 UTC.
- **Failure condition:** No earthquake of magnitude 6.0 or greater occurs within 200 km of the us6000u18k epicenter from 2026-10-13 through 2026-10-27 UTC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171736ZZ - sha256 f0f2d3d4fb810030...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-13&endtime=2026-10-28&latitude=7.6069&longitude=-80.7566&maxradiuskm=200&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261013-18
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** Kimberly Guilfoyle resigns as ambassador between 2026-10-20 and 2026-10-27.
- **Resolution criterion:** Public reporting confirms Kimberly Guilfoyle has resigned as ambassador by 2026-10-27.
- **Failure condition:** Kimberly Guilfoyle has not resigned as ambassador by 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-28
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The ICE Brent crude futures contract for December 2026 settles below 100.00 USD per barrel on 2026-10-28. Reference: front-month Brent at 105.86 on the packet date 2026-10-13.
- **Resolution criterion:** TRUE if the official ICE settlement price of the Brent December 2026 contract on 2026-10-28 is below 100.00 USD per barrel; otherwise FALSE. Reference: 105.86 on the packet date.
- **Failure condition:** The Brent December 2026 contract settles at or above 100.00 USD per barrel on 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-44
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** Kimberly Guilfoyle resigns or is removed as US Ambassador to Greece, with the departure announced by her, the White House or the State Department between 2026-10-13 and 2026-10-27.
- **Resolution criterion:** A White House, State Department or Guilfoyle statement, or reports from at least two of AP, Reuters and BBC, confirm her resignation or removal as US Ambassador to Greece announced between 2026-10-13 and 2026-10-27.
- **Failure condition:** No resignation or removal of Kimberly Guilfoyle as US Ambassador to Greece takes place or is announced between 2026-10-13 and 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-46
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** USGS records an earthquake of magnitude 6.5 or greater with an epicenter within 250 km of the M7.7 Panama mainshock (USGS event us6000u18k) and origin time between 2026-10-14 and 2026-10-27 UTC.
- **Resolution criterion:** The USGS earthquake catalog (ComCat) lists at least one event of magnitude 6.5 or greater, origin time between 2026-10-14 and 2026-10-27 UTC, epicenter within 250 km of event us6000u18k.
- **Failure condition:** Every earthquake with an epicenter within 250 km of USGS event us6000u18k and origin time between 2026-10-14 and 2026-10-27 UTC has a USGS magnitude below 6.5.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171736ZZ - sha256 5df87a49a5a2f773...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-14&endtime=2026-10-28&latitude=7.6069&longitude=-80.7566&maxradiuskm=250&minmagnitude=6.5
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261013-47
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one SAP product vulnerability with a dateAdded value between 2026-10-14 and 2026-10-27.
- **Resolution criterion:** The CISA KEV catalog JSON carries at least one entry with vendorProject SAP and a dateAdded value between 2026-10-14 and 2026-10-27 inclusive.
- **Failure condition:** CISA adds no entry with vendorProject SAP to the KEV catalog with a dateAdded value between 2026-10-14 and 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-50
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** The Ukrainian Air Force reports that Russia launched at least 500 drones and missiles combined in a single overnight attack occurring between 2026-10-14 and 2026-10-27.
- **Resolution criterion:** The Ukrainian Air Force, as relayed by Reuters or AP, reports at least 500 drones and missiles combined launched by Russia in one overnight attack dated between 2026-10-14 and 2026-10-27.
- **Failure condition:** Every overnight Russian drone and missile attack on Ukraine between 2026-10-14 and 2026-10-27 involves fewer than 500 drones and missiles combined by Ukrainian Air Force count.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-23
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-10-30
- **Domain:** military/conflict
- **Claim:** Between 2026-10-15 and 2026-10-28, Saudi authorities or the Saudi-led coalition confirm at least one further Houthi missile or drone launched toward Saudi territory, following the 2026-10-14 Aramco building strike and the Riyadh interception.
- **Resolution criterion:** Reuters or AP carries an SPA, Saudi defence ministry, or coalition statement confirming a Houthi missile or drone intercepted over or impacting Saudi territory on a date between 2026-10-15 and 2026-10-28.
- **Failure condition:** No Houthi missile or drone reaches or is intercepted over Saudi territory on any date between 2026-10-15 and 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-30
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** The FOMC statement issued 2026-10-28 at the conclusion of the scheduled 2026-10-27 to 2026-10-28 meeting raises the federal funds target range above the 3.75 to 4.00 percent range in effect on 2026-10-17.
- **Resolution criterion:** The FOMC statement dated 2026-10-28 on federalreserve.gov sets a target range whose upper bound exceeds 4.00 percent. Reference: 3.75 to 4.00 percent in effect at seal on 2026-10-17. Hold or cut resolves false.
- **Failure condition:** The target range announced in the 2026-10-28 FOMC statement has an upper bound of 4.00 percent or lower.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-69
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At least one FOMC voting member dissents from the federal funds rate decision announced on 2026-10-28 at the close of the scheduled 2026-10-27 to 2026-10-28 meeting.
- **Resolution criterion:** TRUE if the FOMC statement published on federalreserve.gov on 2026-10-28 names at least one member voting against the policy action; FALSE if the recorded vote is unanimous.
- **Failure condition:** Every FOMC voting member votes in favor of the policy action announced on 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-18
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** France imposes a state of emergency or declares a national mourning period between 2026-10-26 and 2026-10-30
- **Resolution criterion:** A French government decree or official statement declares a state of emergency or national mourning period
- **Failure condition:** No French government decree or official statement declares a state of emergency or national mourning period
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-60
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range. Reference: target range upper bound 4.00 percent on the packet date.
- **Resolution criterion:** YES if FRED series DFEDTARU for 2026-10-29 is higher than its value for 2026-10-27, reflecting a target-range increase announced at the meeting concluding 2026-10-28.
- **Failure condition:** The FOMC leaves the federal funds target range unchanged or lowers it at the meeting concluding 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261019-11
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** A magnitude 6.0 or greater earthquake occurs in Vanuatu between 2026-10-20 and 2026-10-27.
- **Resolution criterion:** The USGS reports a magnitude 6.0 or greater earthquake in Vanuatu with an origin time within the event window.
- **Failure condition:** The USGS reports no magnitude 6.0 or greater earthquake in Vanuatu during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171736ZZ - sha256 6512b02d1176e38f...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-20&endtime=2026-10-28&minlatitude=-20.5&maxlatitude=-13.0&minlongitude=166.0&maxlongitude=170.5&minmagnitude=6.0
  - observed: 1 event(s) returned; top magnitudes [6.1]

### KKR-20261019-15
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-10-30
- **Domain:** disaster
- **Claim:** The Indonesian government declares a national disaster status for the Kalimantan forest fires between 2026-10-20 and 2026-10-27.
- **Resolution criterion:** The Indonesian National Disaster Management Authority (BNPB) issues a statement declaring national disaster status for Kalimantan forest fires during the event window.
- **Failure condition:** The Indonesian BNPB does not issue a statement declaring national disaster status for Kalimantan forest fires during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-08
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-10-30
- **Domain:** cyber
- **Claim:** The State Bank of India confirms a data leak affecting more than 4,000 customers between 2026-10-21 and 2026-10-28.
- **Resolution criterion:** The State Bank of India confirms a data leak affecting more than 4,000 customers between 2026-10-21 and 2026-10-28.
- **Failure condition:** The State Bank of India does not confirm a data leak affecting more than 4,000 customers between 2026-10-21 and 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-44
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-10-30
- **Domain:** economics/markets
- **Claim:** At the conclusion of its meeting on 2026-10-27 to 2026-10-28, the Federal Open Market Committee raises the federal funds target range above 3.75 to 4.00 percent. Reference: target range 3.75 to 4.00 percent on 2026-10-21.
- **Resolution criterion:** The FOMC policy statement released 2026-10-28 on federalreserve.gov sets a target range with an upper bound above 4.00 percent.
- **Failure condition:** The FOMC policy statement released 2026-10-28 keeps the target range upper bound at 4.00 percent or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261023-95
- **Issued:** 2026-10-23  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** Luiz Inacio Lula da Silva wins re-election as president of Brazil, defeating Flavio Bolsonaro in the runoff held on 2026-10-25.
- **Resolution criterion:** TSE official totals for the 2026-10-25 presidential runoff, as published on the TSE results site at the deadline, show Lula with more than 50 percent of valid votes. Flavio Bolsonaro above 50 percent resolves false.
- **Failure condition:** Lula did not receive more than 50 percent of valid votes in the 2026-10-25 runoff.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261023-107
- **Issued:** 2026-10-23  ·  **Deadline:** 2026-10-30
- **Domain:** political
- **Claim:** Flavio Bolsonaro receives more valid votes than Luiz Inacio Lula da Silva in the Brazilian presidential runoff held on 2026-10-25.
- **Resolution criterion:** The Superior Electoral Court (TSE) tally for the 2026-10-25 runoff, read on 2026-10-30, shows Flavio Bolsonaro with more valid votes than Lula; a Lula lead or tie resolves false.
- **Failure condition:** At the deadline, the TSE tally for the 2026-10-25 runoff shows Lula with at least as many valid votes as Flavio Bolsonaro.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260722-12
- **Issued:** 2026-07-22  ·  **Deadline:** 2026-10-31
- **Domain:** political
- **Claim:** At least one major social media platform (Meta, TikTok, Snap, or X) publicly announces an age-verification mechanism for French users between 2026-07-23 and 2026-10-31
- **Resolution criterion:** A company press release, official blog post, or two independent wire reports confirm a named platform announcing age verification for France in the window
- **Failure condition:** the condition stated in this entry's resolution basis — A company press release, official blog post, or two independent wire reports confirm a named platform announcing age verification for France in the window — is not met on or before 2026-10-31; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260725-10
- **Issued:** 2026-07-25  ·  **Deadline:** 2026-10-31
- **Domain:** political
- **Claim:** A US federal court or the Supreme Court issues a ruling in a challenge to Trump administration tariffs between 2026-07-27 and 2026-10-31.
- **Resolution criterion:** TRUE if a US federal court or the Supreme Court issues a merits ruling on the legality of any Trump administration tariff, reported by major press within the window; else FALSE.
- **Failure condition:** the condition stated in this entry's resolution basis — TRUE if a US federal court or the Supreme Court issues a merits ruling on the legality of any Trump administration tariff, reported by major press within the window; else FALSE — is not met on or before 2026-10-31; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-19
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-10-31
- **Domain:** political
- **Claim:** The German federal cabinet will approve a draft bill tightening extremism or weapons law that explicitly references the Berlin Pride attack, on or before 2026-10-31.
- **Resolution criterion:** Resolved by the Bundesregierung cabinet decisions page listing such a Gesetzentwurf on or before 2026-10-31, with the attack named in the accompanying release.
- **Failure condition:** the condition stated in this entry's resolution basis — the Bundesregierung cabinet decisions page listing such a Gesetzentwurf on or before 2026-10-31, with the attack named in the accompanying release — is not met on or before 2026-10-31; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-23
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-10-31
- **Domain:** military/conflict
- **Claim:** An official United States Department of Defense or service publication will report more than 900 US service members injured in the Iran conflict since February 2026, published on or before 2026-10-31.
- **Resolution criterion:** Resolved by a figure exceeding 900 appearing in a DoD, CENTCOM or service public-affairs release or congressional testimony transcript dated on or before 2026-10-31.
- **Failure condition:** the condition stated in this entry's resolution basis — a figure exceeding 900 appearing in a DoD, CENTCOM or service public-affairs release or congressional testimony transcript dated on or before 2026-10-31 — is not met on or before 2026-10-31; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-17
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-31
- **Domain:** cyber
- **Claim:** CISA, EPA, or FBI will issue an advisory, or Reuters or AP will report, that a cyberattack disrupted operational technology at a US water or wastewater utility, between 2026-08-08 and 2026-10-31.
- **Resolution criterion:** Resolved from the CISA cybersecurity advisories index on 2026-10-31. Yes if any advisory published in the window names a US water or wastewater utility with disrupted operations.
- **Failure condition:** the condition stated in this entry's resolution basis — any advisory published in the window names a US water or wastewater utility with disrupted operations — is not met on or before 2026-10-31 as read from the CISA cybersecurity advisories index; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-18
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-10-31
- **Domain:** cyber
- **Claim:** OpenAI, Anthropic, Google DeepMind, or xAI will disclose a new case, beyond incidents already public as of 2026-08-01, of one of its models autonomously breaching third-party systems, between 2026-08-08 and 2026-10-31.
- **Resolution criterion:** Resolved from openai.com, anthropic.com, deepmind.google, and x.ai safety disclosures, cross-checked against Reuters and AP, on 2026-10-31. Yes if any confirms a new case, beyond incidents public by 2026-08-01, of autonomous third-party system breach.
- **Failure condition:** the condition stated in this entry's resolution basis — any confirms a new case, beyond incidents public by 2026-08-01, of autonomous third-party system breach — is not met on or before 2026-10-31 as read from openai.com, anthropic.com, deepmind.google, and x.ai safety disclosures, cross-checked against Reuters and AP,; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-12
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-31
- **Domain:** disaster
- **Claim:** On 2026-10-28, a major earthquake of magnitude 6.0 or higher occurs in the Russian Far East, with at least 10 fatalities confirmed by the Russian Emergency Ministry.
- **Resolution criterion:** The Russian Emergency Ministry issues a final report on 2026-10-28 confirming that a magnitude 6.0 or higher earthquake occurred in the Russian Far East, resulting in at least 10 fatalities.
- **Failure condition:** The Russian Emergency Ministry does not issue a final report on 2026-10-28 confirming a magnitude 6.0 or higher earthquake in the Russian Far East with at least 10 fatalities.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-02
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-31
- **Domain:** cyber
- **Claim:** Between 2026-10-26 and 2026-10-29, a ransomware attack will disrupt a government agency's IT systems in Japan, with a public statement from the agency confirming the incident.
- **Resolution criterion:** A government agency in Japan publicly confirms a ransomware attack disrupting its IT systems between 2026-10-26 and 2026-10-29.
- **Failure condition:** No government agency in Japan publicly confirms a ransomware attack disrupting its IT systems between 2026-10-26 and 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-03
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-01
- **Domain:** disaster
- **Claim:** Between 2026-10-27 and 2026-10-30, a major earthquake of magnitude 6.0 or higher will be recorded by the USGS in the Pacific region, with a confirmed location in Vanuatu or Alaska.
- **Resolution criterion:** The USGS records a magnitude 6.0 or higher earthquake in the Pacific region, with a confirmed location in Vanuatu or Alaska, between 2026-10-27 and 2026-10-30.
- **Failure condition:** No magnitude 6.0 or higher earthquake is recorded by the USGS in Vanuatu or Alaska between 2026-10-27 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171737ZZ - sha256 0a3598c6535fcbf0...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-27&endtime=2026-10-31&minlatitude=-20.5&maxlatitude=-13.0&minlongitude=166.0&maxlongitude=170.5&minmagnitude=6.0
  - observed: 1 event(s) returned; top magnitudes [6.2]

### KKR-20260812-06
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** A vulnerability affecting VMware vCenter Server is added to the CISA KEV catalog with a date-added value between 2026-08-13 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA Known Exploited Vulnerabilities catalog contains an entry naming VMware vCenter Server with dateAdded between 2026-08-13 and 2026-10-30 inclusive.
- **Failure condition:** The CISA KEV catalog contains no VMware vCenter Server entry with dateAdded between 2026-08-13 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171737ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['VMware'] with dateAdded in [2026-08-13..2026-10-30] across 1768 catalog rows - CVE-2026-41709, CVE-2026-59310

### KKR-20260817-04
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-17 and 2026-10-30.
- **Resolution criterion:** True if the official ICE Brent front-month settlement price is at or above 100.00 USD on any trading day from 2026-08-17 through 2026-10-30, per ICE settlement data.
- **Failure condition:** Every ICE Brent front-month daily settlement from 2026-08-17 through 2026-10-30 is below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-12
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-11-02
- **Domain:** economic
- **Claim:** ICE Brent front-month futures settle at or above USD 100.00 per barrel on at least one trading session between 2026-08-24 and 2026-10-30.
- **Resolution criterion:** The ICE Futures Europe published daily settlement for the front-month Brent contract reaches 100.00 or higher on any session in that range, checked 2026-11-02.
- **Failure condition:** Every front-month Brent settlement inside the window prints below 100.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-13
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The USGS catalog records at least one magnitude 6.0 or greater earthquake within 250 km of event us6000tkt2 with origin time between 2026-08-20 and 2026-10-31 UTC.
- **Resolution criterion:** A USGS FDSN event query centered on the us6000tkt2 epicenter with 250 km radius, minimum magnitude 6.0, and the window dates returns at least one event; zero events grades MISS.
- **Failure condition:** The USGS query for M6.0 or greater within 250 km of the epicenter during the event window returns zero events.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-51
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-02
- **Domain:** economic
- **Claim:** ICE Brent front-month futures settle at or above 110.00 USD per barrel on at least one trading day between 2026-09-03 and 2026-10-30. Reference: 95.33 on the packet date 2026-09-02.
- **Resolution criterion:** TRUE if the ICE Brent front-month official settlement price equals or exceeds 110.00 on any trading day from 2026-09-03 through 2026-10-30. Reference level 95.33 at seal.
- **Failure condition:** Every ICE Brent front-month settlement from 2026-09-03 through 2026-10-30 prints below 110.00 USD per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-04
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Pete Hegseth leaves his Pentagon leadership role (resignation, removal, or reassignment), following the criticism referenced in the 2026-09-05 Guardian report, at any point between 2026-09-06 and 2026-10-31.
- **Resolution criterion:** TRUE if at least two of AP, Reuters, or BBC report that Hegseth has left his Pentagon leadership post between 2026-09-06 and 2026-10-31, confirmed as of 2026-11-02; FALSE otherwise.
- **Failure condition:** MISS if Hegseth remains in his Pentagon leadership post through 2026-10-31 with no departure confirmed by two named outlets as of 2026-11-02.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-12
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-11-02
- **Domain:** crime/security
- **Claim:** Between 2026-09-05 and 2026-10-30, the Plymouth County District Attorney announces that the Commonwealth will retry Lindsay Clancy on the murder charges, or the Plymouth Superior Court schedules a retrial date.
- **Resolution criterion:** TRUE if, between 2026-09-05 and 2026-10-30, the Plymouth County DA states that Clancy will be retried on the murder charges, or the court docket sets a retrial date, per AP or the Boston Globe.
- **Failure condition:** By 2026-10-30 the DA has not announced a retrial and no retrial date is on the docket, including if the charges are resolved by plea or dismissed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-72
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-11-02
- **Domain:** economic
- **Claim:** Between 2026-09-13 and 2026-11-01, Freddie Mac's Primary Mortgage Market Survey will report a weekly average 30-year fixed mortgage rate of 7.25 percent or higher on at least one release. Reference: approximately 7.00 percent as reported 2026-09-05.
- **Resolution criterion:** TRUE if any Freddie Mac PMMS release between 2026-09-13 and 2026-11-01 reports the 30-year fixed average at or above 7.25 percent. FALSE if every release in the window is below 7.25 percent.
- **Failure condition:** No Freddie Mac PMMS release between 2026-09-13 and 2026-11-01 reports a 30-year fixed average of 7.25 percent or higher.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-29
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The ECB Governing Council raises the deposit facility rate above 2.50 percent at its scheduled 2026-10-29 monetary policy meeting. Reference: 2.50 percent after the 2026-09-10 decision.
- **Resolution criterion:** The ECB monetary policy decisions press release dated 2026-10-29 on ecb.europa.eu states a deposit facility rate greater than 2.50 percent. Reference: 2.50 percent on 2026-09-10.
- **Failure condition:** The 2026-10-29 ECB decision leaves the deposit facility rate at or below 2.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-62
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-85102 or CVE-2026-85103, the Check Point VPN certificate flaws disclosed 2026-09-09, to the Known Exploited Vulnerabilities catalog between 2026-09-11 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed lists CVE-2026-85102 or CVE-2026-85103 with a dateAdded value between 2026-09-11 and 2026-10-30 inclusive. FALSE otherwise.
- **Failure condition:** Neither CVE-2026-85102 nor CVE-2026-85103 carries a KEV dateAdded value between 2026-09-11 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-65
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** Houthi forces take control of the town of Dhubab, Taiz governorate, on the southern Red Sea coast approach to the Bab al-Mandab strait, between 2026-09-11 and 2026-10-30.
- **Resolution criterion:** TRUE if Houthi forces take control of Dhubab town between 2026-09-11 and 2026-10-30, as reported by at least two of Reuters, AP, AFP citing Yemeni government or government-aligned military sources. Houthi claims alone do not count.
- **Failure condition:** Houthi forces did not take control of Dhubab town at any point between 2026-09-11 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-72
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-11-02
- **Domain:** military_conflict
- **Claim:** Between 2026-09-16 and 2026-10-31 the governments of Russia and Ukraine each publicly announce agreement to halt strikes on energy infrastructure of the other side.
- **Resolution criterion:** At least two of Reuters, AP, AFP report that both the Russian and Ukrainian governments announced, on dates between 2026-09-16 and 2026-10-31, agreement to halt strikes on energy infrastructure, bilateral or US-brokered.
- **Failure condition:** No agreement to halt strikes on energy infrastructure is announced by both the Russian and Ukrainian governments between 2026-09-16 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-36
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** At the FOMC meeting concluding 2026-10-28, the Committee raises the federal funds target range above the range in effect on 2026-10-27.
- **Resolution criterion:** True if the FRED series DFEDTARU (federal funds target range upper limit) observation dated 2026-10-29 is higher than its observation dated 2026-10-27.
- **Failure condition:** DFEDTARU dated 2026-10-29 equals or is below its 2026-10-27 value, meaning the range was held or cut at the 2026-10-28 meeting.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-50
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28.
- **Resolution criterion:** TRUE if FRED DFEDTARU for 2026-10-29 exceeds its 2026-10-27 value, i.e. a hike at the 2026-10-27 to 2026-10-28 meeting. Reference: relative to the 2026-10-27 upper bound; packet holds no funds-rate level.
- **Failure condition:** The FOMC left the federal funds target range unchanged or lowered it at its 2026-10-27 to 2026-10-28 meeting.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-18
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** At its scheduled October 2026 meeting (statement expected 2026-10-28), the FOMC raises the federal funds target range above the range set at its September 2026 meeting.
- **Resolution criterion:** TRUE if the FOMC statement released at the conclusion of its scheduled October 2026 meeting (expected 2026-10-28) sets a federal funds target range higher than the range set at the September 2026 meeting, per federalreserve.gov press releases.
- **Failure condition:** The October 2026 FOMC statement leaves the federal funds target range unchanged or lowers it relative to the range set in September 2026.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-57
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** WTI crude oil settles below 95.00 dollars per barrel on any NYMEX trading day between 2026-10-01 and 2026-10-30. Reference: 101.09 dollars per barrel on the packet date, 2026-09-17.
- **Resolution criterion:** TRUE if the CME/NYMEX WTI front-month settlement price closes below 95.00 dollars on any trading day from 2026-10-01 to 2026-10-30, per CME Group data; adjudicated 2026-11-02. FALSE otherwise.
- **Failure condition:** The CME/NYMEX WTI front-month settlement price never closes below 95.00 dollars on any trading day in the window, per CME Group data.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-22
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its scheduled 2026-10-27 to 2026-10-28 meeting. Reference: 3.75 to 4.00 percent at seal, FRED DFEDTARU 4.00.
- **Resolution criterion:** TRUE if FRED series DFEDTARU for 2026-10-29 exceeds 4.00, reflecting a target-range increase announced in the FOMC statement of 2026-10-28; otherwise FALSE.
- **Failure condition:** The FOMC held or cut the target range at its 2026-10-27 to 2026-10-28 meeting, leaving the upper limit at or below 4.00 percent on 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260923-15
- **Issued:** 2026-09-23  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** On at least one business day between 2026-09-24 and 2026-10-30, the 10-year Treasury constant maturity yield (FRED series DGS10) is at or above 5.50 percent. Reference: 10Y yield 5.06 percent in the packet market snapshot on 2026-09-23.
- **Resolution criterion:** FRED series DGS10 shows a daily value of 5.50 or higher for at least one date from 2026-09-24 through 2026-10-30 inclusive.
- **Failure condition:** Every DGS10 daily value dated 2026-09-24 through 2026-10-30 is below 5.50 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260924-43
- **Issued:** 2026-09-24  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog will list a new entry for a TeamCity CVE with a dateAdded value between 2026-09-24 and 2026-10-31.
- **Resolution criterion:** The public CISA KEV catalog (cisa.gov) shows a TeamCity-product CVE with dateAdded between 2026-09-24 and 2026-10-31, checked on 2026-11-02.
- **Failure condition:** No TeamCity CVE carries a KEV dateAdded value in that window when the catalog is checked on 2026-11-02.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171739ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['TeamCity-product'] with dateAdded in [2026-09-24..2026-10-31] across 1768 catalog rows

### KKR-20260925-11
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The ICE Brent crude front-month futures settlement price on 2026-10-30 is below 90.00 USD per barrel. Reference: 99.46 USD on the packet date.
- **Resolution criterion:** TRUE if the official ICE Futures Europe settlement price for the front-month Brent crude contract on 2026-10-30 is below 90.00 USD per barrel. Reference: 99.46 USD on the packet date.
- **Failure condition:** MISS if the front-month Brent settlement on 2026-10-30 is at or above 90.00 USD per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-26
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** Between 2026-09-26 and 2026-10-30, President Trump or the White House announces or confirms an agreement or ceasefire with Iran under which Iran is to reopen the Strait of Hormuz to commercial shipping.
- **Resolution criterion:** TRUE if AP and Reuters both report that the US president or White House announced or confirmed, between 2026-09-26 and 2026-10-30, an agreement or ceasefire with Iran including reopening of the Strait of Hormuz; otherwise FALSE.
- **Failure condition:** No US-Iran agreement or ceasefire providing for reopening of the Strait of Hormuz is announced or confirmed by the US president or White House between 2026-09-26 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-46
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds a new CVE for a Kiteworks, WSO2, or Adobe Commerce product, dateAdded between 2026-09-27 and 2026-10-31.
- **Resolution criterion:** The CISA KEV catalog lists a Kiteworks, WSO2, or Adobe Commerce CVE with a dateAdded value between 2026-09-27 and 2026-10-31.
- **Failure condition:** No Kiteworks, WSO2, or Adobe Commerce CVE appears in the CISA KEV catalog with a dateAdded in the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171741ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Kiteworks', 'WSO2', 'Adobe Commerce'] with dateAdded in [2026-09-27..2026-10-31] across 1768 catalog rows - CVE-2026-48356

### KKR-20260929-09
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** Between 2026-10-22 and 2026-10-28, the 10-year US Treasury yield will close above 5.50 percent on at least one weekday.
- **Resolution criterion:** The 10-year US Treasury yield will close above 5.50 percent on at least one weekday between 2026-10-22 and 2026-10-28, inclusive, as reported by FRED or Bloomberg
- **Failure condition:** The 10-year US Treasury yield closes at or below 5.50 percent on every weekday between 2026-10-22 and 2026-10-28
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261106T171742ZZ - sha256 9cee4a11cad003f6...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 5 business days in window; max BC_10YEAR 5.05 on 2026-10-28; threshold > 5.50; 0 day(s) satisfying

### KKR-20260930-35
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** The Spanish Congress of Deputies validates Royal Decree-law 26/2026 on housing and eviction protection in a plenary vote held between 2026-10-02 and 2026-10-29.
- **Resolution criterion:** True if the Congress of Deputies votes to convalidate Royal Decree-law 26/2026 between 2026-10-02 and 2026-10-29, per the Congress voting record or BOE convalidation notice; false if derogated or never voted.
- **Failure condition:** Royal Decree-law 26/2026 is not validated by the Congress of Deputies between 2026-10-02 and 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-50
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-11-02
- **Domain:** military_conflict
- **Claim:** Israeli strikes or gunfire kill at least 30 people in Gaza on a single calendar day between 2026-10-01 and 2026-10-28, per Gaza health officials.
- **Resolution criterion:** Reuters or AP reports, citing Gaza health officials, that at least 30 Palestinians were killed by Israeli strikes or fire in Gaza on one calendar day falling between 2026-10-01 and 2026-10-28.
- **Failure condition:** Israeli strikes or fire kill fewer than 30 people in Gaza on every calendar day between 2026-10-01 and 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-16
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its scheduled meeting of 2026-10-27 to 2026-10-28, lifting the upper limit to 4.25 percent or higher. Reference: upper limit 4.00 percent on the packet date.
- **Resolution criterion:** FRED series DFEDTARU shows 4.25 or higher for 2026-10-29, the day after the 2026-10-27 to 2026-10-28 meeting. Reference: 4.00 on the packet date.
- **Failure condition:** The FOMC leaves the target range upper limit at 4.00 percent or lower at its 2026-10-27 to 2026-10-28 meeting.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-15
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The ICE Brent December 2026 futures contract settles below 95.00 dollars per barrel on at least one trading day between 2026-10-05 and 2026-10-29. Reference: 100.27 on the packet date.
- **Resolution criterion:** The ICE daily settlement price for Brent December 2026 futures is below 95.00 on any trading day between 2026-10-05 and 2026-10-29. Reference: 100.27 on the packet date.
- **Failure condition:** Every ICE Brent December 2026 settlement from 2026-10-05 through 2026-10-29 is at or above 95.00 dollars per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-16
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** Ethiopian federal forces or the allied Tigray Peace Forces take control of Mekelle, the Tigray regional capital, on a date between 2026-10-03 and 2026-10-30.
- **Resolution criterion:** At least two of Reuters, AFP, AP and BBC report federal or allied forces holding Mekelle on a date between 2026-10-03 and 2026-10-30, citing residents, the TPLF or their own reporters rather than a government claim alone.
- **Failure condition:** Federal and allied forces do not hold Mekelle on any date from 2026-10-03 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-17
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The DR Congo health ministry cumulative death toll for the Ebola outbreak declared 2026-05-15 reaches 5,000 or more in figures published between 2026-10-03 and 2026-10-30. Reference: 4,018 in figures published 2026-10-01.
- **Resolution criterion:** At least two of AP, Reuters and AFP report a DR Congo health ministry cumulative Ebola death toll of 5,000 or more, published between 2026-10-03 and 2026-10-30. Reference: 4,018 on 2026-10-01.
- **Failure condition:** The health ministry cumulative death toll published through 2026-10-30 stays below 5,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-43
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-11-02
- **Domain:** economic
- **Claim:** ICE Brent December 2026 futures settle below 95.00 USD per barrel on 2026-10-29. Reference: 102.25 USD per barrel in the packet market snapshot dated 2026-10-03.
- **Resolution criterion:** The ICE official settlement price for Brent December 2026 futures on 2026-10-29 is below 95.00 USD per barrel.
- **Failure condition:** Brent December 2026 futures settle at or above 95.00 USD per barrel on 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-58
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** At the FOMC meeting held 2026-10-27 and 2026-10-28, the committee raises the federal funds target range above the range in effect on the packet date 2026-10-04.
- **Resolution criterion:** The Federal Reserve statement released on 2026-10-28 sets a federal funds target range above the range in effect on 2026-10-04, as shown by FRED series DFEDTARU. Reference: range in effect on the packet date.
- **Failure condition:** The Federal Reserve statement released on 2026-10-28 leaves the federal funds target range unchanged or lowers it relative to the range in effect on 2026-10-04.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-27
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** Nvidia shares close at or above 248.00 dollars on Nasdaq on at least one trading day between 2026-10-06 and 2026-10-30. Reference: 233.95 dollars at the 2026-10-02 close, about 237 intraday on the packet date.
- **Resolution criterion:** The Nasdaq official closing price of NVDA is 248.00 dollars or higher on at least one trading day between 2026-10-06 and 2026-10-30. Reference: 233.95 dollars at the 2026-10-02 close.
- **Failure condition:** NVDA closes below 248.00 dollars on every Nasdaq trading day between 2026-10-06 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-09
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Between 2026-10-24 and 2026-10-30, a confirmed political event will occur in France involving a national strike or protest that results in the closure of at least 500 schools.
- **Resolution criterion:** At least one report from two or more hostile sides (FR, WEST) confirms a national strike or protest in France between 2026-10-24 and 2026-10-30, resulting in the closure of at least 500 schools.
- **Failure condition:** No report from two or more hostile sides confirms a national strike or protest in France between 2026-10-24 and 2026-10-30, or the number of closed schools is less than 500.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-03
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** Between 2026-10-22 and 2026-10-29, a cyberattack exploiting a known vulnerability in Microsoft Teams will be confirmed by CISA.
- **Resolution criterion:** CISA issues a public advisory between 2026-10-22 and 2026-10-29 stating that a cyberattack exploited a vulnerability in Microsoft Teams, with the vulnerability listed in the KEV catalog.
- **Failure condition:** CISA does not issue a public advisory confirming a cyberattack exploiting a Microsoft Teams vulnerability during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171743ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Microsoft Teams'] with dateAdded in [2026-10-22..2026-10-29] across 1768 catalog rows

### KKR-20261008-35
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The ICE Brent December 2026 crude futures contract settles at or above 110.00 USD per barrel on at least one trading day between 2026-10-09 and 2026-10-29. Reference: 105.68 on the packet date.
- **Resolution criterion:** ICE end-of-day settlement data show the Brent December 2026 futures contract settling at or above 110.00 USD on at least one trading day between 2026-10-09 and 2026-10-29.
- **Failure condition:** Every daily settlement of the Brent December 2026 contract between 2026-10-09 and 2026-10-29 is below 110.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-16
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-11-02
- **Domain:** crime_security
- **Claim:** The FBI announces the disruption of a major ransomware gang operating out of Eastern Europe between 2026-10-16 and 2026-10-30.
- **Resolution criterion:** The FBI announces the disruption of a major ransomware gang operating out of Eastern Europe between 2026-10-16 and 2026-10-30.
- **Failure condition:** The FBI does not announce the disruption of a major ransomware gang operating out of Eastern Europe between 2026-10-16 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-50
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** Between 2026-10-12 and 2026-10-29, the front-month ICE Brent futures contract settles at or above 110.00 dollars per barrel on at least one trading day. Reference: 104.72 in the packet market snapshot of 2026-10-10, the prior-session close.
- **Resolution criterion:** ICE Futures Europe settlement data for the front-month Brent contract show a daily settlement of 110.00 dollars or more on at least one trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 in the packet snapshot of 2026-10-10.
- **Failure condition:** The front-month ICE Brent futures contract settles below 110.00 dollars per barrel on every trading day between 2026-10-12 and 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-27
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 110.00 dollars per barrel on at least one trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 on the packet date.
- **Resolution criterion:** True if the ICE Brent front-month futures settlement price is at or above 110.00 on any trading day between 2026-10-12 and 2026-10-29. Reference: 104.72 on the packet date.
- **Failure condition:** ICE Brent front-month futures settle below 110.00 on every trading day from 2026-10-12 through 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-66
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The ICE Brent December 2026 futures contract settles below 100.00 USD per barrel on 2026-10-29. Reference: 106.95 USD on the packet date.
- **Resolution criterion:** YES if the ICE Futures Europe settlement price for the Brent December 2026 contract on 2026-10-29 is below 100.00 USD per barrel. Reference: 106.95 USD on the packet date.
- **Failure condition:** The Brent December 2026 futures contract settles at or above 100.00 USD per barrel on 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-45
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Pope Leo XIV is discharged from hospital after the operation to remove a growth, with the discharge occurring between 2026-10-13 and 2026-10-27.
- **Resolution criterion:** The Holy See Press Office, or at least two of AP, Reuters and BBC, confirm Pope Leo XIV was discharged from hospital on a date between 2026-10-13 and 2026-10-27.
- **Failure condition:** Pope Leo XIV has not been discharged from hospital by the end of 2026-10-27.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-07
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries a date-added value for a new critical zero-day vulnerability between 2026-10-27 and 2026-10-30.
- **Resolution criterion:** A new entry appears in the CISA KEV catalog with a date-added value falling within the event window.
- **Failure condition:** No new entries are added to the CISA KEV catalog during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-14
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** A new critical zero-day vulnerability affecting major infrastructure is added to the CISA KEV catalog between 2026-10-27 and 2026-10-30.
- **Resolution criterion:** A new entry appears in the CISA KEV catalog with a date-added value falling within the event window.
- **Failure condition:** No new entries are added to the CISA KEV catalog during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-01
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** The European Parliament passes a resolution calling for the suspension of all EU military aid to Israel between 2026-10-25 and 2026-10-31.
- **Resolution criterion:** The European Parliament's official website (europarl.europa.eu) publishes a resolution titled 'Suspension of EU military aid to Israel' with a vote date between 2026-10-25 and 2026-10-31.
- **Failure condition:** No such resolution is published on the European Parliament's official website by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-02
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** A U.S. federal agency issues a public advisory warning of a coordinated cyberattack on critical infrastructure by a China-linked threat group between 2026-10-24 and 2026-10-31.
- **Resolution criterion:** The CISA Advisories page (cisa.gov) publishes a new advisory titled 'China-Linked Threat Group Targets Critical Infrastructure' with a publication date between 2026-10-24 and 2026-10-31.
- **Failure condition:** No such advisory is published on the CISA Advisories page by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-27
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry with vendorProject BeyondTrust and a dateAdded between 2026-10-16 and 2026-10-30, following the Remote Support zero-day disclosed on 2026-10-16.
- **Resolution criterion:** The KEV JSON feed at cisa.gov contains an entry whose vendorProject field is BeyondTrust and whose dateAdded is between 2026-10-16 and 2026-10-30 inclusive. Any BeyondTrust product qualifies.
- **Failure condition:** No KEV entry with vendorProject BeyondTrust carries a dateAdded in the 2026-10-16 to 2026-10-30 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-43
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** CISA adds the BeyondTrust zero-day reported as exploited since August 2026 to its Known Exploited Vulnerabilities catalog, with a BeyondTrust entry carrying a dateAdded value between 2026-10-16 and 2026-10-30.
- **Resolution criterion:** The CISA KEV catalog carries at least one entry with vendorProject BeyondTrust and a dateAdded value from 2026-10-16 through 2026-10-30 inclusive, as retrieved on or after the deadline.
- **Failure condition:** No BeyondTrust vulnerability receives a KEV dateAdded value between 2026-10-16 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171744ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['BeyondTrust'] with dateAdded in [2026-10-16..2026-10-30] across 1768 catalog rows - CVE-2026-102764

### KKR-20261016-46
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** At least one earthquake of magnitude 6.0 or greater strikes within 300 km of the epicenter of the magnitude 7.7 Panama mainshock (USGS event us6000u18k) between 2026-10-17 and 2026-10-30.
- **Resolution criterion:** The USGS ComCat catalog lists at least one earthquake with magnitude 6.0 or greater, origin time between 2026-10-17 and 2026-10-30 UTC, within 300 km of the epicenter of USGS event us6000u18k.
- **Failure condition:** No earthquake of magnitude 6.0 or greater strikes within 300 km of the us6000u18k epicenter between 2026-10-17 and 2026-10-30 UTC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171744ZZ - sha256 2438fcf172a39140...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-17&endtime=2026-10-31&latitude=7.6069&longitude=-80.7566&maxradiuskm=300&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261016-48
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** The Houthi movement launches at least one missile or drone attack on Saudi Arabian territory between 2026-10-17 and 2026-10-30, claimed by the Houthis or reported by Saudi Arabia or its military coalition.
- **Resolution criterion:** Reuters or AP reports a Houthi-claimed or Saudi-reported missile or drone attack on Saudi territory with an incident date from 2026-10-17 through 2026-10-30.
- **Failure condition:** The Houthis launch no missile or drone attack on Saudi territory at any time between 2026-10-17 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-61
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The FOMC raises the federal funds target range at its meeting concluding on 2026-10-28, lifting the upper limit above 4.00 percent. Reference: target range 3.75 to 4.00 percent on the packet date.
- **Resolution criterion:** Resolves true if FRED series DFEDTARU, the federal funds target range upper limit, reads above 4.00 for 2026-10-29 following the decision announced 2026-10-28. Reference: 4.00 percent on the packet date.
- **Failure condition:** The FOMC holds or lowers the target range at the meeting concluding 2026-10-28, leaving the upper limit at or below 4.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-63
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** CISA adds a BeyondTrust vulnerability to its Known Exploited Vulnerabilities catalog between 2026-10-16 and 2026-10-30, following the exploited Remote Support zero-day patched in October 2026.
- **Resolution criterion:** Resolves true if the CISA KEV catalog JSON contains an entry with vendorProject BeyondTrust and a dateAdded value between 2026-10-16 and 2026-10-30 inclusive; otherwise false.
- **Failure condition:** CISA adds no BeyondTrust vulnerability to the KEV catalog with a dateAdded value between 2026-10-16 and 2026-10-30.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171746ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['BeyondTrust'] with dateAdded in [2026-10-16..2026-10-30] across 1768 catalog rows - CVE-2026-102764

### KKR-20261017-01
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** Between 2026-10-17 and 2026-10-24, the USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Pakistan with a depth of less than 50 km.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude ≥6.0 and depth <50 km in Pakistan between 2026-10-17 and 2026-10-24.
- **Failure condition:** No magnitude 6.0 or greater earthquake with depth less than 50 km is recorded in Pakistan between 2026-10-17 and 2026-10-24 in the USGS Significant Quakes catalog.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-02
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** Between 2026-10-17 and 2026-10-24, at least one drone strike will be reported in Kyiv by two or more independently biased sources across hostile sides.
- **Resolution criterion:** At least one drone strike in Kyiv is reported by two or more independently biased sources across hostile sides (RU, UA, WEST) between 2026-10-17 and 2026-10-24.
- **Failure condition:** No drone strike in Kyiv is reported by two or more independently biased sources across hostile sides between 2026-10-17 and 2026-10-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-03
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Between 2026-10-17 and 2026-10-24, the Federal Register will publish a notice proposing new sanctions on Russian energy exports.
- **Resolution criterion:** The Federal Register publishes a notice proposing new sanctions on Russian energy exports between 2026-10-17 and 2026-10-24.
- **Failure condition:** No such notice is published in the Federal Register between 2026-10-17 and 2026-10-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-04
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** Between 2026-10-17 and 2026-10-24, the NVD will list a new vulnerability in the Drupal content management system with a CVSS score of 9.0 or higher.
- **Resolution criterion:** The National Vulnerability Database lists a new vulnerability in Drupal with a CVSS score ≥9.0 between 2026-10-17 and 2026-10-24.
- **Failure condition:** No new Drupal vulnerability with CVSS score ≥9.0 is listed in the NVD between 2026-10-17 and 2026-10-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-05
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** Between 2026-10-17 and 2026-10-24, the USGS Significant Quakes catalog will record a magnitude 5.5 or greater earthquake in Russia with a depth of less than 100 km.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude ≥5.5 and depth <100 km in Russia between 2026-10-17 and 2026-10-24.
- **Failure condition:** No magnitude 5.5 or greater earthquake with depth less than 100 km is recorded in Russia between 2026-10-17 and 2026-10-24 in the USGS Significant Quakes catalog.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261017-19
- **Issued:** 2026-10-17  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The USGS Significant Quakes catalog carries a date-added value for a magnitude 6.5 or larger earthquake between 2026-10-25 and 2026-10-31
- **Resolution criterion:** The USGS Significant Quakes catalog carries a date-added value for a magnitude 6.5 or larger earthquake between 2026-10-25 and 2026-10-31
- **Failure condition:** The USGS Significant Quakes catalog carries no date-added value for a magnitude 6.5 or larger earthquake between 2026-10-25 and 2026-10-31
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-01
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** A Ukrainian drone attack on a Russian energy facility in St Petersburg results in at least one fatality and damage to infrastructure between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** At least one fatality is confirmed by two independent wire services (e.g., Reuters, AP) or a government agency report, and physical damage to a Russian energy facility in St Petersburg is documented by satellite imagery or official source during the event window.
- **Failure condition:** No confirmed fatality or infrastructure damage is reported by two independent sources or verified via satellite imagery during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-02
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** France experiences a major civil unrest event resulting in over 1,500 arrests and at least 100 injuries between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** Two independent wire services (e.g., AFP, Reuters) report that over 1,500 people were arrested and at least 100 were injured in France during the event window, with injuries confirmed by medical or official sources.
- **Failure condition:** The number of arrests is below 1,500 or injuries are below 100, as confirmed by two independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-03
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** A wildfire in Alberta, Canada, spreads beyond 500 hectares and causes at least one fatality between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** The Canadian Interagency Forest Fire Centre (CIFFC) or a provincial fire agency confirms a wildfire in Alberta exceeding 500 hectares and causing at least one fatality during the event window.
- **Failure condition:** The fire does not exceed 500 hectares or no fatality is confirmed by a provincial or federal agency during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-04
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The S&P 500 index closes above 7,800 points on the final trading day of the event window, between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** The S&P 500 closes at or above 7,800.00 on the last trading day of the event window, as reported by the S&P Global Market Intelligence database.
- **Failure condition:** The S&P 500 closes below 7,800.00 on the last trading day of the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-05
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** military/conflict
- **Claim:** Iran announces a new military operational plan targeting shipping in the Strait of Hormuz between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** An official statement from Iran's Ministry of Defense or IRGC confirms a new operational plan targeting shipping in the Strait of Hormuz during the event window.
- **Failure condition:** No official Iranian government or IRGC statement confirms such a plan during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-06
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** The 10-year U.S. Treasury yield exceeds 5.3% on any trading day between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** The FRED database shows the 10-year U.S. Treasury yield surpassing 5.3% on at least one trading day during the event window.
- **Failure condition:** The 10-year U.S. Treasury yield never exceeds 5.3% during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261018-07
- **Issued:** 2026-10-18  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** A new outbreak of a respiratory illness with confirmed human-to-human transmission is reported in South Africa between 2026-10-18 and 2026-10-24.
- **Resolution criterion:** The World Health Organization (WHO) or South Africa's National Institute for Communicable Diseases (NICD) confirms a new respiratory illness with human-to-human transmission in South Africa during the event window.
- **Failure condition:** No official confirmation of a new respiratory illness with human-to-human transmission is issued by WHO or NICD during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261019-10
- **Issued:** 2026-10-19  ·  **Deadline:** 2026-11-02
- **Domain:** military_conflict
- **Claim:** The Houthi movement conducts a kinetic strike on a commercial vessel in the Red Sea or Gulf of Aden between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** Two independent wire services report a Houthi kinetic strike on a commercial vessel in the specified waters during the event window.
- **Failure condition:** No Houthi kinetic strike on a commercial vessel in the Red Sea or Gulf of Aden is reported by two independent wire services during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-30
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** Moodys lowers the long-term issuer rating of the Government of France by at least one notch in a rating action published between 2026-10-22 and 2026-10-30.
- **Resolution criterion:** A rating action on moodys.com, or the Agence France Tresor ratings page, shows a Moodys downgrade of France dated 2026-10-22 to 2026-10-30. An affirmation or outlook-only change resolves false.
- **Failure condition:** France holds the same Moodys long-term rating on 2026-10-30 that it held at the packet date.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261021-45
- **Issued:** 2026-10-21  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The eastern Pacific tropical cyclone listed by GDACS as TWENTY-TWO-E-26 (event TC 1001341), under any name NHC later assigns, is rated Category 3 or stronger (maximum sustained winds of at least 115 mph) in an NHC advisory issued between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** An NHC advisory issued from 2026-10-22 through 2026-10-29 for the system GDACS lists as TC 1001341 gives maximum sustained winds of at least 115 mph, or NHC best-track data confirm 100 knots or higher in that period.
- **Failure condition:** The system listed by GDACS as TC 1001341 never reaches maximum sustained winds of 115 mph or 100 knots between 2026-10-22 and 2026-10-29.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261022-10
- **Issued:** 2026-10-22  ·  **Deadline:** 2026-11-02
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries a date-added value for a critical PHP web vulnerability between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** The CISA KEV catalog lists the vulnerability with a date-added value within the window.
- **Failure condition:** The vulnerability is not added to the CISA KEV catalog by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261022-12
- **Issued:** 2026-10-22  ·  **Deadline:** 2026-11-02
- **Domain:** military_conflict
- **Claim:** A Houthi attack on a commercial shipping vessel in the Red Sea or Gulf of Aden results in at least one fatality between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** Two independent wire services report a Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden with at least one fatality.
- **Failure condition:** No Houthi attack on a commercial vessel in the Red Sea or Gulf of Aden results in at least one fatality by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261022-13
- **Issued:** 2026-10-22  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The USGS records a magnitude 6.0 or greater earthquake in China between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** The USGS earthquake catalog lists an event with magnitude 6.0 or greater in China within the window.
- **Failure condition:** The USGS earthquake catalog lists no event with magnitude 6.0 or greater in China within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261022-14
- **Issued:** 2026-10-22  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The USGS records a magnitude 7.0 or greater earthquake anywhere in the world between 2026-10-22 and 2026-10-29.
- **Resolution criterion:** The USGS earthquake catalog lists an event with magnitude 7.0 or greater within the window.
- **Failure condition:** The USGS earthquake catalog lists no event with magnitude 7.0 or greater within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261024-44
- **Issued:** 2026-10-24  ·  **Deadline:** 2026-11-02
- **Domain:** disaster
- **Claim:** The UK Met Office issues a red weather warning for wind or rain associated with Storm Boelo, for any part of the UK, between 2026-10-24 and 2026-10-31.
- **Resolution criterion:** TRUE if the Met Office issues any red National Severe Weather Warning for wind or rain linked to Storm Boelo between 2026-10-24 and 2026-10-31, per its warnings archive or official statements.
- **Failure condition:** The Met Office issues no red wind or rain warning linked to Storm Boelo between 2026-10-24 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261025-32
- **Issued:** 2026-10-25  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Luiz Inacio Lula da Silva defeats Flavio Bolsonaro in the Brazilian presidential runoff held on 2026-10-25.
- **Resolution criterion:** TRUE if the Superior Electoral Court (TSE) official totals for the 2026-10-25 presidential runoff give Lula da Silva more than 50 percent of valid votes; FALSE if Flavio Bolsonaro wins.
- **Failure condition:** Flavio Bolsonaro receives more than 50 percent of valid votes in the 2026-10-25 runoff.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261025-46
- **Issued:** 2026-10-25  ·  **Deadline:** 2026-11-02
- **Domain:** economics/markets
- **Claim:** At the FOMC meeting concluding on 2026-10-28, the Federal Reserve raises the federal funds target range above 3.75 to 4.00 percent. Reference: 3.75 to 4.00 percent, upper bound 4.00, in effect on the packet date.
- **Resolution criterion:** The Federal Reserve statement released on 2026-10-28 announces an increase in the federal funds target range above 3.75 to 4.00 percent, and FRED series DFEDTARU shows an upper bound above 4.00 on 2026-10-29.
- **Failure condition:** The FOMC leaves the target range at 3.75 to 4.00 percent or lowers it at the meeting concluding on 2026-10-28.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261025-47
- **Issued:** 2026-10-25  ·  **Deadline:** 2026-11-02
- **Domain:** political
- **Claim:** Luiz Inacio Lula da Silva receives more valid votes than Flavio Bolsonaro in the Brazilian presidential runoff held on 2026-10-25.
- **Resolution criterion:** The Superior Electoral Court (TSE) results portal shows Lula with more valid votes than Flavio Bolsonaro in the runoff held on 2026-10-25, at 100 percent of sections counted.
- **Failure condition:** Flavio Bolsonaro receives more valid votes than Lula in the runoff held on 2026-10-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260802-04
- **Issued:** 2026-08-02  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** Between 2026-11-01 and 2026-11-03, a new financial regulation in the European Union will be enacted requiring all banks to report real-time transaction data to a central authority.
- **Resolution criterion:** A new financial regulation enacted by the European Union between 2026-11-01 and 2026-11-03 mandates that all banks report real-time transaction data to a central authority.
- **Failure condition:** No new financial regulation enacted by the European Union between 2026-11-01 and 2026-11-03 mandates real-time transaction reporting by banks to a central authority.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-25
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** US and Iranian officials hold a confirmed direct bilateral meeting between 2026-08-10 and 2026-10-31.
- **Resolution criterion:** True if the US State Department and Iran's foreign ministry both confirm a direct bilateral meeting between US and Iranian officials held within the window.
- **Failure condition:** No direct US-Iran bilateral meeting occurs in the window, mediated contact only.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-59
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds a further N-able N-central vulnerability with a date-added value between 2026-08-05 and 2026-10-31.
- **Resolution criterion:** TRUE if the CISA KEV catalog contains an N-able N-central CVE other than CVE-2026-18577 and CVE-2026-18556 carrying a dateAdded value between 2026-08-05 and 2026-10-31.
- **Failure condition:** No further N-able N-central CVE carries a KEV date-added value inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260806-01
- **Issued:** 2026-08-06  ·  **Deadline:** 2026-11-03
- **Domain:** economics
- **Claim:** ICE Brent front-month crude futures settle at or below 70.00 USD per barrel on at least one settlement date between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** Any ICE-published front-month Brent settlement price with a settlement date between 2026-08-06 and 2026-10-30 is 70.00 or lower.
- **Failure condition:** Every ICE front-month Brent settlement inside the window prints above 70.00 USD per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260806-11
- **Issued:** 2026-08-06  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds at least one entry for Gitea, n8n, or TP-Link Omada with a date-added value between 2026-08-06 and 2026-10-30.
- **Resolution criterion:** TRUE if the public CISA KEV catalog contains an entry whose vendor or product names Gitea, n8n, or TP-Link Omada with dateAdded between 2026-08-06 and 2026-10-30; FALSE otherwise.
- **Failure condition:** The KEV catalog contains no Gitea, n8n, or TP-Link Omada entry with a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171748ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Gitea', 'TP-Link Omada'] with dateAdded in [2026-08-06..2026-10-30] across 1768 catalog rows - CVE-2026-60004

### KKR-20260810-12
- **Issued:** 2026-08-10  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** Intel prices or completes a common stock offering of at least 10 billion USD between 2026-08-11 and 2026-10-30, per filings on SEC EDGAR.
- **Resolution criterion:** SEC EDGAR shows an Intel Corporation prospectus supplement, 424B, or 8-K filed between 2026-08-11 and 2026-10-30 pricing or completing a common stock offering with gross proceeds of at least 10 billion USD.
- **Failure condition:** No Intel filing on SEC EDGAR in the window prices or completes a common stock offering of at least 10 billion USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260810-18
- **Issued:** 2026-08-10  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** NYMEX front-month WTI crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-08-11 and 2026-10-30.
- **Resolution criterion:** TRUE if CME official settlement data for the front-month NYMEX WTI light sweet crude contract shows a settlement price of 100.00 or higher on any trading day from 2026-08-11 through 2026-10-30.
- **Failure condition:** No front-month WTI settlement in that window reaches 100.00 dollars per barrel.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260811-18
- **Issued:** 2026-08-11  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendorProject is Fortinet or Schneider Electric, with dateAdded between 2026-08-12 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed holds at least one entry with vendorProject Fortinet or Schneider Electric and a dateAdded value between 2026-08-12 and 2026-10-30 inclusive.
- **Failure condition:** No KEV entry from either vendor carries a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260812-13
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog gains an entry naming Microsoft SharePoint Server or VMware vCenter Server with a date-added value between 2026-08-13 and 2026-10-30.
- **Resolution criterion:** True if the CISA KEV JSON feed contains an entry whose product field names SharePoint Server or vCenter Server with a dateAdded between 2026-08-13 and 2026-10-30 inclusive.
- **Failure condition:** The KEV catalog holds no SharePoint Server or vCenter Server entry with a dateAdded inside that range.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-09
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** The White House publicly names a specific individual as the next White House press secretary, acting or permanent, between 2026-08-14 and 2026-10-30.
- **Resolution criterion:** TRUE if AP or Reuters carries a White House announcement, dated between 2026-08-14 and 2026-10-30, naming a specific successor as press secretary; otherwise FALSE.
- **Failure condition:** As of the deadline, no White House announcement dated inside the window names any specific individual as the next press secretary.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-12
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** The United States and Iran both publicly confirm a ceasefire or framework agreement between them, with confirmations dated between 2026-08-14 and 2026-10-30.
- **Resolution criterion:** TRUE if statements from both the US and Iranian governments confirming a ceasefire or framework agreement, each carried by AP, Reuters, or AFP, are dated between 2026-08-14 and 2026-10-30; otherwise FALSE.
- **Failure condition:** By the deadline, at least one of the two governments has issued no confirmation of any such agreement dated inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-69
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds the exploited VMware vCenter flaw CVE-2026-59310 to the Known Exploited Vulnerabilities catalog between 2026-08-18 and 2026-10-31.
- **Resolution criterion:** The CISA KEV JSON feed contains an entry with cveID CVE-2026-59310 whose dateAdded value falls between 2026-08-18 and 2026-10-31 inclusive.
- **Failure condition:** CVE-2026-59310 is absent from the KEV catalog, or present with a dateAdded value outside that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-11
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** A vulnerability in a GitLab product is added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-19 and 2026-10-31.
- **Resolution criterion:** The CISA KEV catalog contains at least one entry listing GitLab as vendor or product with dateAdded between 2026-08-19 and 2026-10-31.
- **Failure condition:** No KEV entry naming GitLab carries a dateAdded value between 2026-08-19 and 2026-10-31.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171749ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['GitLab'] with dateAdded in [2026-08-19..2026-10-31] across 1768 catalog rows - CVE-2026-85706, CVE-2026-97229

### KKR-20260818-14
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** The USGS earthquake catalog records at least one earthquake of magnitude 6.5 or greater with an epicenter in Indonesia occurring between 2026-08-19 and 2026-10-31 UTC.
- **Resolution criterion:** The USGS ComCat catalog lists at least one event of magnitude 6.5 or greater located within Indonesia with origin time between 2026-08-19 and 2026-10-31 UTC.
- **Failure condition:** The USGS catalog contains no Indonesia event of magnitude 6.5 or greater with origin time between 2026-08-19 and 2026-10-31 UTC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261106T171750ZZ - sha256 cbbb663e3fbec759...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-08-19&endtime=2026-11-01&minlatitude=-11.0&maxlatitude=6.0&minlongitude=95.0&maxlongitude=141.0&minmagnitude=6.5
  - observed: 1 event(s) returned; top magnitudes [6.5]

### KKR-20260819-07
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 100.00 USD per barrel on at least one trading day between 2026-08-20 and 2026-10-30.
- **Resolution criterion:** The official ICE Brent front-month settlement price is at or above 100.00 USD on any trading day from 2026-08-20 through 2026-10-30; otherwise MISS.
- **Failure condition:** Every ICE Brent front-month settlement in the event window is below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-12
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures record an official daily settlement at or above 100.00 USD per barrel on at least one trading day between 2026-08-21 and 2026-10-30.
- **Resolution criterion:** Published ICE Brent front-month official settlement prices show at least one value at or above 100.00 USD between 2026-08-21 and 2026-10-30 inclusive.
- **Failure condition:** Every Brent front-month official settlement in the window prints below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-27
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-11-03
- **Domain:** economic
- **Claim:** ICE Brent front-month crude futures settle at or above 100.00 US dollars per barrel on at least one trading day between 2026-08-21 and 2026-10-30.
- **Resolution criterion:** ICE published front-month Brent settlement data shows a settlement price of 100.00 or higher on at least one session dated inside the window.
- **Failure condition:** Every Brent front-month settlement inside the window prints below 100.00 dollars.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-30
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** The 10-year US Treasury constant-maturity yield closes at or above 5.00 percent on at least one trading day between 2026-08-24 and 2026-10-30.
- **Resolution criterion:** FRED series DGS10 shows a value of 5.00 or higher for at least one observation dated between 2026-08-24 and 2026-10-30 inclusive.
- **Failure condition:** Every DGS10 observation dated 2026-08-24 through 2026-10-30 is below 5.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-38
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-08-24 and 2026-10-31, a named cybersecurity outlet will report a confirmed unauthorized access incident, data breach, or cloud resource abuse case attributed to the leaked AWS keys documented on 2026-08-21.
- **Resolution criterion:** TRUE if BleepingComputer, The Hacker News, or Krebs on Security reports a specific breach or resource abuse incident attributed to the leaked AWS keys by the deadline; FALSE otherwise.
- **Failure condition:** No confirmed unauthorized access incident or breach is publicly attributed to the leaked AWS keys between 2026-08-24 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260825-11
- **Issued:** 2026-08-25  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-08-26 and 2026-10-31, CISA adds to the Known Exploited Vulnerabilities catalog at least one Zimbra Collaboration vulnerability other than CVE-2026-73570.
- **Resolution criterion:** TRUE if the CISA KEV catalog JSON contains an entry whose vendorProject or product field includes Zimbra, with a dateAdded value 2026-08-26 through 2026-10-31, and a cveID other than CVE-2026-73570.
- **Failure condition:** The KEV catalog contains no Zimbra entry other than CVE-2026-73570 with a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-02
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Boston Scientific files a Form 8-K or 8-K/A with the SEC that includes Item 1.05, Material Cybersecurity Incidents, for the August 2026 cyberattack between 2026-08-27 and 2026-10-30, following its initial Item 8.01 disclosure.
- **Resolution criterion:** EDGAR filings for CIK 885725 show a Form 8-K or 8-K/A with filing date 2026-08-27 through 2026-10-30 whose listed items include 1.05; otherwise false.
- **Failure condition:** No Boston Scientific 8-K or 8-K/A filed 2026-08-27 through 2026-10-30 lists Item 1.05.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-70
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** CISA adds a vulnerability in the Avada WordPress theme to the Known Exploited Vulnerabilities catalog with a dateAdded between 2026-08-28 and 2026-10-30.
- **Resolution criterion:** The CISA KEV catalog JSON contains an entry whose vendorProject, product, or vulnerabilityName field includes Avada, with dateAdded between 2026-08-28 and 2026-10-30 inclusive.
- **Failure condition:** No KEV entry referencing Avada carries a dateAdded inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171751ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Avada'] with dateAdded in [2026-08-28..2026-10-30] across 1768 catalog rows

### KKR-20260827-73
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** The United States and Iran both publicly confirm signing a final agreement ending the war that began on 2026-02-28, with the signing occurring between 2026-08-28 and 2026-10-30.
- **Resolution criterion:** The White House or State Department and the Iranian Foreign Ministry or IRNA each confirm a signed final agreement ending the war, distinct from a ceasefire, memorandum, or framework, signed between 2026-08-28 and 2026-10-30.
- **Failure condition:** No accord described by both governments as a final or comprehensive war-ending agreement is signed inside the window; a ceasefire extension, interim MOU, or one-sided claim does not count.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-75
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-11-03
- **Domain:** crime/security
- **Claim:** Spanish authorities (Guardia Civil or Policia Nacional) announce at least one arrest in the 2026-08-27 Villena Treasure theft between 2026-08-27 and 2026-10-30.
- **Resolution criterion:** An official Guardia Civil or Policia Nacional communication, or Reuters, AP, AFP, or EFE citing such officials, reports at least one person arrested (detenido) for the Villena Museum theft, with the arrest dated between 2026-08-27 and 2026-10-30.
- **Failure condition:** No arrest attributed to the Villena Museum theft is announced by Spanish authorities with an arrest date inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-38
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** By 2026-10-30, the combined official confirmed death toll from the August 2026 Nepal-Tibet glacial outburst floods, per Nepali and Chinese authorities, reaches at least 1,000.
- **Resolution criterion:** AP, Reuters, AFP, or BBC report official Nepali plus Chinese confirmed-dead figures for the August 2026 flood totaling 1,000 or more, dated on or before 2026-10-30.
- **Failure condition:** The latest official combined confirmed toll reported on or before 2026-10-30 stands below 1,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-42
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-11-03
- **Domain:** crime/security
- **Claim:** Between 2026-08-29 and 2026-10-31, US authorities remove Milo Yiannopoulos from the United States.
- **Resolution criterion:** Two international outlets, citing DHS, ICE, or court records, report Yiannopoulos removed or deported from the US on a date between 2026-08-29 and 2026-10-31.
- **Failure condition:** Yiannopoulos remains in the United States, whether detained or released, through 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-56
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries at least 30 entries with a dateAdded value between 2026-09-01 and 2026-10-30.
- **Resolution criterion:** The CISA KEV JSON feed counts 30 or more entries whose dateAdded value falls between 2026-09-01 and 2026-10-30 inclusive.
- **Failure condition:** The KEV feed carries fewer than 30 entries with dateAdded inside that range.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-57
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries at least one entry naming Cisco as vendorProject with a dateAdded value between 2026-09-01 and 2026-10-30.
- **Resolution criterion:** The CISA KEV JSON feed contains an entry whose vendorProject is Cisco and whose dateAdded value falls inside that range.
- **Failure condition:** No KEV entry with vendorProject Cisco carries a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-84
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures settle at or above 95.00 USD per barrel on at least one trading day between 2026-09-01 and 2026-10-30.
- **Resolution criterion:** True if any official ICE Brent front-month daily settlement price between 2026-09-01 and 2026-10-30 is at or above 95.00 USD; exchange settlement records govern.
- **Failure condition:** Every ICE Brent front-month daily settlement between 2026-09-01 and 2026-10-30 is below 95.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-85
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-11-03
- **Domain:** disaster
- **Claim:** The Nepal government confirmed death toll from the August 2026 flood disaster reaches at least 300 at any point between 2026-08-31 and 2026-10-30.
- **Resolution criterion:** True if Nepali government statements carried by at least two international news agencies place the confirmed dead at 300 or more on any date between 2026-08-31 and 2026-10-30.
- **Failure condition:** The cumulative Nepal government confirmed death toll remains below 300 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-10
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-03
- **Domain:** economics_markets
- **Claim:** The US 10-year Treasury constant maturity yield reaches 5.00 percent or higher on at least one business day between 2026-09-08 and 2026-10-30. Reference: 4.77 percent at seal on 2026-09-01.
- **Resolution criterion:** FRED series DGS10 carries a daily observation at or above 5.00 for at least one business day from 2026-09-08 through 2026-10-30; reference 4.77 at seal.
- **Failure condition:** Every DGS10 daily observation inside the window prints below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-45
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** Front-month NYMEX WTI crude settles at or above 100.00 dollars per barrel on at least one trading day between 2026-09-03 and 2026-10-30. Reference: 90.59 on the packet date.
- **Resolution criterion:** CME official settlement data show any front-month CL settlement at or above 100.00 inside the window. Reference level at seal: 90.59.
- **Failure condition:** Every front-month WTI settlement in the window is below 100.00 dollars.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-01
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** Between 2026-09-03 and 2026-10-31 the United States government and the government of Iran each publicly confirm a ceasefire, truce, or mutual halt to strikes between the two states.
- **Resolution criterion:** TRUE if official statements from both the US government (White House, State Department, or Pentagon) and Iran (Foreign Ministry, SNSC, or Supreme Leader office) confirm a bilateral ceasefire or halt to strikes announced between 2026-09-03 and 2026-10-31.
- **Failure condition:** As of 2026-10-31 no ceasefire, truce, or mutual halt to strikes between the United States and Iran has been confirmed by both governments.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-06
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Between 2026-09-03 and 2026-10-30 the Council of the EU adopts a new numbered package of sanctions against Russia over the war in Ukraine, with the legal acts published in the Official Journal of the European Union.
- **Resolution criterion:** TRUE if the Official Journal (EUR-Lex) publishes Council legal acts, dated between 2026-09-03 and 2026-10-30, that the Council press release describes as a new numbered sanctions package against Russia; extensions or delistings alone do not count.
- **Failure condition:** The EU adopts no new numbered Russia sanctions package with Official Journal publication dated between 2026-09-03 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-40
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-11-03
- **Domain:** economics/markets
- **Claim:** ICE Brent crude front-month futures record a daily settlement at or above 100.00 USD per barrel on at least one trading day between 2026-09-04 and 2026-10-30. Reference: Brent 96.70 at packet seal on 2026-09-03.
- **Resolution criterion:** Resolves TRUE if any official ICE Brent front-month daily settlement between 2026-09-04 and 2026-10-30 is at or above 100.00 USD; otherwise FALSE.
- **Failure condition:** Every ICE Brent front-month daily settlement in the window is below 100.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-29
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** The Philippine Court of Appeals or Supreme Court issues a temporary restraining order, status quo ante order, or injunction halting the Quezon City RTC Branch 98 grave threats proceedings against Vice President Sara Duterte between 2026-09-04 and 2026-10-30.
- **Resolution criterion:** An order of the Court of Appeals or Supreme Court dated within the window suspends or enjoins the Branch 98 grave threats proceedings against Duterte, confirmed by the issuing court or by two of Rappler, Inquirer, Philstar, Reuters.
- **Failure condition:** No Court of Appeals or Supreme Court order suspending or enjoining the Branch 98 grave threats proceedings against Duterte is issued from 2026-09-04 through 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-41
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-11-03
- **Domain:** political
- **Claim:** Philippine Vice President Sara Duterte is taken into physical custody or surrenders to a Philippine court between 2026-09-04 and 2026-10-30.
- **Resolution criterion:** TRUE if Philippine authorities book or process her in custody, or she surrenders in court, in that window, per Reuters and the Philippine Daily Inquirer. Adjudicated 2026-11-03.
- **Failure condition:** She is neither booked into custody nor surrendered to a court on or before 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-80
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** Between 2026-09-07 and 2026-10-30 inclusive, CISA adds to its Known Exploited Vulnerabilities catalog at least one CVE whose product is VMware Workstation or VMware Fusion (vendor VMware or Broadcom), with a dateAdded value in that range.
- **Resolution criterion:** True if the CISA KEV JSON feed contains an entry whose product field names Workstation or Fusion under vendorProject VMware or Broadcom, with dateAdded between 2026-09-07 and 2026-10-30 inclusive.
- **Failure condition:** No CISA KEV entry naming VMware Workstation or Fusion carries a dateAdded between 2026-09-07 and 2026-10-30.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-35
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds at least one vulnerability with vendorProject N-able, carrying a dateAdded value between 2026-09-08 and 2026-10-30.
- **Resolution criterion:** TRUE if the CISA Known Exploited Vulnerabilities JSON feed contains an entry whose vendorProject field reads N-able and whose dateAdded falls between 2026-09-08 and 2026-10-30 inclusive. Entries carrying an earlier dateAdded do not count.
- **Failure condition:** No N-able entry in the KEV catalog carries a dateAdded inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261106T171753ZZ - sha256 273b7e449828f0af...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['N-able'] with dateAdded in [2026-09-08..2026-10-30] across 1768 catalog rows - CVE-2026-86218

### KKR-20260909-58
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-11-03
- **Domain:** economic
- **Claim:** The 10-year Treasury constant maturity rate closes at or above 5.00 percent on at least one business day between 2026-09-10 and 2026-10-30. Reference: 4.85 percent on the packet date.
- **Resolution criterion:** TRUE if FRED series DGS10 records a value of 5.00 or higher on any business day inside the window.
- **Failure condition:** Every DGS10 observation inside the window prints below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-63
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-11-03
- **Domain:** military/conflict
- **Claim:** US or Israeli forces strike the Pickaxe Mountain (Kuh-e Kolang Gaz La) tunnel complex near Natanz, Iran, between 2026-09-11 and 2026-10-31.
- **Resolution criterion:** TRUE if a strike on the site between 2026-09-11 and 2026-10-31 is confirmed by Pentagon, CENTCOM, White House or IDF, or by two of Reuters, AP, AFP citing US or Israeli officials. Iranian claims alone do not count.
- **Failure condition:** No US or Israeli strike hit the Pickaxe Mountain site between 2026-09-11 and 2026-10-31.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-47
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-11-03
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one CVE whose vendor or product field contains GitLab with a dateAdded value between 2026-09-12 and 2026-10-30.
- **Resolution criterion:** The public CISA KEV JSON feed contains an entry matching GitLab in vendorProject or product with dateAdded between 2026-09-12 and 2026-10-30 inclusive; otherwise MISS.
- **Failure condition:** No KEV entry matching GitLab carries a dateAdded value inside the 2026-09-12 to 2026-10-30 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

