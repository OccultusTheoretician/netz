# KKR RESOLUTION AUDIT PACKET
Generated 040320Z OCT 26 · 126 projections (part 2 of 4; packet total 502) past deadline, awaiting adjudication.

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

### KKR-20260822-09
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-19478, the GitLab CE/EE GraphQL code-injection flaw (CVSS 9.4) reported exploited in the wild on 2026-08-19, to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-21 and 2026-09-18.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry with cveID CVE-2026-19478 whose dateAdded field is a date from 2026-08-21 through 2026-09-18 inclusive.
- **Failure condition:** At the deadline the KEV catalog has no entry for CVE-2026-19478, or its dateAdded falls outside 2026-08-21 through 2026-09-18.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031934ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-19478'] with dateAdded in [2026-08-21..2026-09-18] across 1733 catalog rows

### KKR-20260822-10
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-69836, the Microsoft Entra ID deserialization remote code execution flaw (CVSS 10.0) that Microsoft says was exploited and is already mitigated server-side, to the KEV catalog with a dateAdded value between 2026-08-21 and 2026-09-18.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry with cveID CVE-2026-69836 whose dateAdded field is a date from 2026-08-21 through 2026-09-18 inclusive.
- **Failure condition:** At the deadline the KEV catalog has no entry for CVE-2026-69836, or its dateAdded falls outside 2026-08-21 through 2026-09-18.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031935ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-69836'] with dateAdded in [2026-08-21..2026-09-18] across 1733 catalog rows

### KKR-20260822-12
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds an entry for CVE-2026-19478, the GitLab remote code execution flaw reported under active exploitation on 2026-08-21.
- **Resolution criterion:** Resolves YES if the CISA KEV catalog (kev.cisa.gov or its published JSON feed) lists CVE-2026-19478 with a dateAdded value between 2026-08-21 and 2026-09-18; resolves NO if no such entry exists by the deadline.
- **Failure condition:** The CISA KEV catalog carries no entry for CVE-2026-19478 with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031937ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-19478'] with dateAdded in [2026-08-21..2026-09-18] across 1733 catalog rows

### KKR-20260822-13
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** Between 2026-08-21 and 2026-09-18, the CISA Known Exploited Vulnerabilities catalog adds at least one entry for a Microsoft Entra ID product vulnerability, corresponding to the maximum-severity flaw Microsoft disclosed as under active exploitation on 2026-08-21.
- **Resolution criterion:** Resolves YES if the CISA KEV catalog lists at least one CVE with vendorProject Microsoft and a product field containing Entra, with a dateAdded value between 2026-08-21 and 2026-09-18; resolves NO if no such entry exists by the deadline.
- **Failure condition:** No Microsoft Entra ID product entry appears in the CISA KEV catalog with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031938ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 4 matching entries for ['Microsoft', 'Entra'] with dateAdded in [2026-08-21..2026-09-18] across 1733 catalog rows - CVE-2019-1068, CVE-2026-81963, CVE-2026-85880, CVE-2026-86218

### KKR-20260822-14
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** military_conflict
- **Claim:** Between 2026-08-21 and 2026-09-18, United States military forces carry out a kinetic strike on a target inside Iranian sovereign territory, including territorial waters.
- **Resolution criterion:** Resolves YES if the strike is corroborated under the two-independent-side standard used in this record (for example, both Iranian and Western or Gulf-state sources) reporting a U.S. strike on Iranian territory within the window; resolves NO otherwise.
- **Failure condition:** No corroborated report meeting the two-side standard describes a U.S. strike on Iranian territory in the window; sanctions, troop repositioning, or rhetorical threats alone do not satisfy this condition.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-15
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-22
- **Domain:** crime_security
- **Claim:** Between 2026-08-21 and 2026-09-18, Swedish police or prosecutors publicly classify the August 21, 2026 sword attack at a Swedish school as a terrorist offense under Swedish law.
- **Resolution criterion:** Resolves YES if Polisen or the Swedish Prosecution Authority states, per reporting from BBC, Reuters, AP, TT, or a major Swedish outlet, that the attack is being investigated or charged as a terrorist offense under the Swedish Act on Criminal Responsibility for Terrorist Offences; resolves NO if authorities charge it solely as attempted murder, aggravated assault, or a similar non-terrorism offense, or make no such classification by the deadline.
- **Failure condition:** By the deadline, Swedish authorities have made no statement classifying the attack as terrorism; the case remains charged or investigated only under ordinary criminal offenses.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-11
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** The confirmed death toll from the Nepal-Tibet border flash floods and avalanche first reported 2026-08-26 will reach at least 50, as stated by Nepal's Ministry of Home Affairs or a wire service, between 2026-08-27 and 2026-09-20.
- **Resolution criterion:** Nepal's Ministry of Home Affairs or a report from at least two of Reuters, AP, AFP, or Al Jazeera states a confirmed death toll of 50 or more, dated between 2026-08-27 and 2026-09-20.
- **Failure condition:** The highest confirmed death toll on record by the deadline remains below 50.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-43
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** The confirmed death toll from the Nepal-Tibet border flash floods and avalanche first reported 2026-08-26 will reach at least 50, as stated by Nepal's Ministry of Home Affairs or a wire service, between 2026-08-27 and 2026-09-20.
- **Resolution criterion:** Nepal's Ministry of Home Affairs or a report from at least two of Reuters, AP, AFP, or Al Jazeera states a confirmed death toll of 50 or more, dated between 2026-08-27 and 2026-09-20.
- **Failure condition:** The highest confirmed death toll on record by the deadline remains below 50.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-48
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** The confirmed death toll from the 26 August 2026 Nepal-Tibet glacial flood disaster will exceed 1,000 people at some point between 2026-09-05 and 2026-09-19.
- **Resolution criterion:** TRUE if the National Disaster Risk Reduction and Management Authority of Nepal or two of Reuters, AP, and AFP report a confirmed toll above 1,000 in the window; checked 2026-09-22; FALSE otherwise.
- **Failure condition:** No NDRRMA update or two-wire-service report states a confirmed death toll above 1,000 for this disaster by 2026-09-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-67
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** The confirmed death toll from the 26 August 2026 Nepal-Tibet glacial flood disaster will exceed 1,000 people at some point between 2026-09-05 and 2026-09-19.
- **Resolution criterion:** TRUE if the National Disaster Risk Reduction and Management Authority of Nepal or two of Reuters, AP, and AFP report a confirmed toll above 1,000 in the window; checked 2026-09-22; FALSE otherwise.
- **Failure condition:** No NDRRMA update or two-wire-service report states a confirmed death toll above 1,000 for this disaster by 2026-09-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-29
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-22
- **Domain:** economics/markets
- **Claim:** The Bank of Japan raises its short-term policy interest rate at the Monetary Policy Meeting concluding 2026-09-18, to a level above the rate in effect on 2026-09-03.
- **Resolution criterion:** The Statement on Monetary Policy published on boj.or.jp for the MPM concluding 2026-09-18 sets the uncollateralized overnight call rate guideline above the level in effect on 2026-09-03.
- **Failure condition:** The BoJ statement for the meeting concluding 2026-09-18 leaves the policy rate unchanged or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-60
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-22
- **Domain:** economics/markets
- **Claim:** The Bank of Japan raises its short-term policy interest rate at the Monetary Policy Meeting concluding 2026-09-18, to a level above the rate in effect on 2026-09-03.
- **Resolution criterion:** The Statement on Monetary Policy published on boj.or.jp for the MPM concluding 2026-09-18 sets the uncollateralized overnight call rate guideline above the level in effect on 2026-09-03.
- **Failure condition:** The BoJ statement for the meeting concluding 2026-09-18 leaves the policy rate unchanged or lowers it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-17
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** economics/markets
- **Claim:** Treasury/OFAC will publish at least one additional Iran-related sanctions designation under Operation Economic Outcast between 2026-09-05 and 2026-09-19, continuing the near-weekly cadence announced by Secretary Bessent.
- **Resolution criterion:** TRUE if OFAC's Recent Actions page lists a new Iran-related designation dated between 2026-09-05 and 2026-09-19; otherwise FALSE.
- **Failure condition:** No new Iran-related OFAC designation is dated within that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-18
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** GDACS will upgrade at least one of its four Green forest-fire alerts logged 2026-09-04 (Mozambique event 1031563, DR Congo event 1031500, Zambia event 1031562, Ethiopia event 1031529) to Orange or Red between 2026-09-05 and 2026-09-19.
- **Resolution criterion:** TRUE if the GDACS page for any of the four listed events shows Orange or Red level between 2026-09-05 and 2026-09-19; otherwise FALSE.
- **Failure condition:** All four listed GDACS events stay at Green, or expire without upgrade, through 2026-09-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-31
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium V8 entry with a dateAdded value between 2026-09-04 and 2026-09-18.
- **Resolution criterion:** Fetch the CISA KEV JSON at the deadline; TRUE if any entry lists vendorProject Google, a product containing Chrome or Chromium V8, and dateAdded between 2026-09-04 and 2026-09-18.
- **Failure condition:** The KEV JSON fetched at the deadline contains no Google Chrome or Chromium V8 entry with dateAdded between 2026-09-04 and 2026-09-18.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-47
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** economics/markets
- **Claim:** Treasury/OFAC will publish at least one additional Iran-related sanctions designation under Operation Economic Outcast between 2026-09-05 and 2026-09-19, continuing the near-weekly cadence announced by Secretary Bessent.
- **Resolution criterion:** TRUE if OFAC's Recent Actions page lists a new Iran-related designation dated between 2026-09-05 and 2026-09-19; otherwise FALSE.
- **Failure condition:** No new Iran-related OFAC designation is dated within that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-48
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** disaster
- **Claim:** GDACS will upgrade at least one of its four Green forest-fire alerts logged 2026-09-04 (Mozambique event 1031563, DR Congo event 1031500, Zambia event 1031562, Ethiopia event 1031529) to Orange or Red between 2026-09-05 and 2026-09-19.
- **Resolution criterion:** TRUE if the GDACS page for any of the four listed events shows Orange or Red level between 2026-09-05 and 2026-09-19; otherwise FALSE.
- **Failure condition:** All four listed GDACS events stay at Green, or expire without upgrade, through 2026-09-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-61
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium V8 entry with a dateAdded value between 2026-09-04 and 2026-09-18.
- **Resolution criterion:** Fetch the CISA KEV JSON at the deadline; TRUE if any entry lists vendorProject Google, a product containing Chrome or Chromium V8, and dateAdded between 2026-09-04 and 2026-09-18.
- **Failure condition:** The KEV JSON fetched at the deadline contains no Google Chrome or Chromium V8 entry with dateAdded between 2026-09-04 and 2026-09-18.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-01
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-22
- **Domain:** military_conflict
- **Claim:** Cumulative fatalities from the Yemen government-Houthi fighting referenced in the 2026-09-05 packet (ground combat, missile strikes) exceed 100 people, tallied at any point between 2026-09-06 and 2026-09-20.
- **Resolution criterion:** TRUE if at least two of Reuters, AP, Al Jazeera, or BBC report a cumulative Yemen fatality count above 100 for this conflict phase between 2026-09-06 and 2026-09-20, confirmed as of 2026-09-22; FALSE otherwise.
- **Failure condition:** MISS if no two named outlets report a cumulative fatality count above 100 for this conflict phase by 2026-09-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-28
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-22
- **Domain:** military_conflict
- **Claim:** Cumulative fatalities from the Yemen government-Houthi fighting referenced in the 2026-09-05 packet (ground combat, missile strikes) exceed 100 people, tallied at any point between 2026-09-06 and 2026-09-20.
- **Resolution criterion:** TRUE if at least two of Reuters, AP, Al Jazeera, or BBC report a cumulative Yemen fatality count above 100 for this conflict phase between 2026-09-06 and 2026-09-20, confirmed as of 2026-09-22; FALSE otherwise.
- **Failure condition:** MISS if no two named outlets report a cumulative fatality count above 100 for this conflict phase by 2026-09-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-78
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-22
- **Domain:** crime/security
- **Claim:** Between 2026-09-06 and 2026-09-20 inclusive, Victoria Police announce that a person has been arrested and charged over the alleged axe attack in Victoria, Australia, reported by the Guardian on 2026-09-06, that left three people with life-threatening injuries.
- **Resolution criterion:** True if a Victoria Police media release, or two of ABC News, The Age, and Guardian Australia, report a person arrested and charged over that attack, with the charge laid between 2026-09-06 and 2026-09-20 inclusive.
- **Failure condition:** No person is charged over the attack by the end of 2026-09-20, including if the suspect is located dead or remains at large.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-104
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-22
- **Domain:** crime/security
- **Claim:** Between 2026-09-06 and 2026-09-20 inclusive, Victoria Police announce that a person has been arrested and charged over the alleged axe attack in Victoria, Australia, reported by the Guardian on 2026-09-06, that left three people with life-threatening injuries.
- **Resolution criterion:** True if a Victoria Police media release, or two of ABC News, The Age, and Guardian Australia, report a person arrested and charged over that attack, with the charge laid between 2026-09-06 and 2026-09-20 inclusive.
- **Failure condition:** No person is charged over the attack by the end of 2026-09-20, including if the suspect is located dead or remains at large.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-66
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-09-22
- **Domain:** political
- **Claim:** The Liberals win at least 4.00 percent of valid national votes in the Swedish Riksdag election held 2026-09-13, clearing the parliamentary threshold.
- **Resolution criterion:** TRUE if the Valmyndigheten final result (slutligt valresultat) for the 2026-09-13 Riksdag election shows the Liberals at 4.00 percent or more of valid national votes. FALSE if below 4.00 percent.
- **Failure condition:** The Liberals received less than 4.00 percent of valid national votes in the final result of the 2026-09-13 Riksdag election.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-72
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-09-22
- **Domain:** political
- **Claim:** The Liberals win at least 4.00 percent of valid national votes in the Swedish Riksdag election held 2026-09-13, clearing the parliamentary threshold.
- **Resolution criterion:** TRUE if the Valmyndigheten final result (slutligt valresultat) for the 2026-09-13 Riksdag election shows the Liberals at 4.00 percent or more of valid national votes. FALSE if below 4.00 percent.
- **Failure condition:** The Liberals received less than 4.00 percent of valid national votes in the final result of the 2026-09-13 Riksdag election.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-08
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-22
- **Domain:** cyber
- **Claim:** Between 2026-09-13 and 2026-09-19, at least one major cyberattack on a U.S. financial institution will be reported by two or more independent outlets with hostile bias.
- **Resolution criterion:** Between 2026-09-13 and 2026-09-19, at least one major cyberattack on a U.S. financial institution is reported by two or more independent outlets with hostile bias (e.g., RU, WEST, AXIS).
- **Failure condition:** No major cyberattack on a U.S. financial institution between 2026-09-13 and 2026-09-19 is reported by two or more independent outlets with hostile bias.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-59
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-22
- **Domain:** political
- **Claim:** A US Senate roll call on the CLARITY Act or a motion directly on it is held between 2026-09-15 and 2026-09-18 and records fewer than 60 yea votes.
- **Resolution criterion:** TRUE if Senate.gov roll call records show a vote on the CLARITY Act or a related cloture or passage motion between 2026-09-15 and 2026-09-18 with fewer than 60 yeas.
- **Failure condition:** MISS if no such roll call occurs inside the window, or if the yea count reaches 60 or more.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-68
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-09-22
- **Domain:** political
- **Claim:** A US Senate roll call on the CLARITY Act or a motion directly on it is held between 2026-09-15 and 2026-09-18 and records fewer than 60 yea votes.
- **Resolution criterion:** TRUE if Senate.gov roll call records show a vote on the CLARITY Act or a related cloture or passage motion between 2026-09-15 and 2026-09-18 with fewer than 60 yeas.
- **Failure condition:** MISS if no such roll call occurs inside the window, or if the yea count reaches 60 or more.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260812-11
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** North Korea conducts at least one further ballistic missile launch between 2026-08-13 and 2026-09-20.
- **Resolution criterion:** True if South Korea's Joint Chiefs of Staff confirm a North Korean ballistic missile launch dated between 2026-08-13 and 2026-09-20, carried by at least two of Yonhap, Reuters, and Associated Press.
- **Failure condition:** North Korea launches no ballistic missile during that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260812-28
- **Issued:** 2026-08-12  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** North Korea conducts at least one further ballistic missile launch between 2026-08-13 and 2026-09-20.
- **Resolution criterion:** True if South Korea's Joint Chiefs of Staff confirm a North Korean ballistic missile launch dated between 2026-08-13 and 2026-09-20, carried by at least two of Yonhap, Reuters, and Associated Press.
- **Failure condition:** North Korea launches no ballistic missile during that window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-09
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** At least one missile or drone strike on United Arab Emirates territory attributed to Iran or Iran-aligned forces occurs between 2026-08-20 and 2026-09-20.
- **Resolution criterion:** At least two of Reuters, AP, AFP, or BBC report a strike on UAE territory within the window attributed to Iran or Iran-aligned forces; no machine-readable register exists for this class.
- **Failure condition:** No strike on UAE territory attributable to Iran or Iran-aligned forces occurs within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-30
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** At least one missile or drone strike on United Arab Emirates territory attributed to Iran or Iran-aligned forces occurs between 2026-08-20 and 2026-09-20.
- **Resolution criterion:** At least two of Reuters, AP, AFP, or BBC report a strike on UAE territory within the window attributed to Iran or Iran-aligned forces; no machine-readable register exists for this class.
- **Failure condition:** No strike on UAE territory attributable to Iran or Iran-aligned forces occurs within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-14
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** A Russian missile or drone strike on the city of Kyiv occurring between 2026-08-21 and 2026-09-20 kills five or more people.
- **Resolution criterion:** At least two of Reuters, AP, AFP report a single Russian strike on Kyiv city between 2026-08-21 and 2026-09-20 with an officially stated death toll of five or more.
- **Failure condition:** No single strike on Kyiv in the window reaches an officially stated death toll of five under the corroboration standard.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-21
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-23
- **Domain:** political
- **Claim:** Between 2026-08-20 and 2026-09-20, Zelenskyy or the Ukrainian government will officially announce a specific date for a wartime presidential election, confirmed by two or more major wire services.
- **Resolution criterion:** TRUE if the Ukrainian presidency or Central Election Commission announces a specific wartime presidential election date between 2026-08-20 and 2026-09-20, confirmed by two or more of Reuters, AP, or AFP.
- **Failure condition:** No official announcement of a specific wartime presidential election date is confirmed by two or more wire services before the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-29
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-23
- **Domain:** disaster_infrastructure
- **Claim:** USGS catalogs an earthquake of magnitude 6.0 or greater within 300 km of the 2026-08-20 Ende, Indonesia M7.7 epicenter, with origin time between 2026-08-21 and 2026-09-20.
- **Resolution criterion:** A USGS ComCat query for magnitude 6.0 or greater, radius 300 km from the Ende mainshock epicenter, across the stated window, returns one or more events.
- **Failure condition:** The ComCat query returns zero qualifying events for the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-39
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-23
- **Domain:** disaster
- **Claim:** Between 2026-08-24 and 2026-09-21, an aftershock of magnitude 6.0 or greater will occur within 250 km of the August 21, 2026 magnitude 6.7 earthquake near Aniso, Peru.
- **Resolution criterion:** TRUE if the USGS earthquake catalog lists an event of magnitude 6.0 or greater within 250 km of the Aniso Peru mainshock within the stated window; FALSE otherwise.
- **Failure condition:** No aftershock of magnitude 6.0 or greater is recorded within 250 km of the Aniso, Peru mainshock between 2026-08-24 and 2026-09-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-70
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-23
- **Domain:** economic
- **Claim:** ICE Brent crude front-month futures settle at or above USD 95.00 per barrel on any session between 2026-09-01 and 2026-09-21.
- **Resolution criterion:** Resolves true if ICE, Reuters, or Bloomberg data show a Brent front-month settlement at or above USD 95.00 on any trading day in the window; false if no such settlement occurs.
- **Failure condition:** Brent front-month crude does not settle at or above USD 95.00 per barrel on any trading day between 2026-09-01 and 2026-09-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-74
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-23
- **Domain:** political
- **Claim:** German federal or state authorities publicly name a suspect or announce charges in the Leipzig drone attack on a Ukrainian-linked aircraft, between 2026-09-01 and 2026-09-21.
- **Resolution criterion:** Resolves true if German federal or state prosecutors or police publicly name a suspect or announce charges in the Leipzig drone-attack case within the window; false if no naming occurs.
- **Failure condition:** No German federal or state authority publicly names a suspect or announces charges in the Leipzig drone-attack case between 2026-09-01 and 2026-09-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-77
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-23
- **Domain:** economic
- **Claim:** ICE Brent crude front-month futures settle at or above USD 95.00 per barrel on any session between 2026-09-01 and 2026-09-21.
- **Resolution criterion:** Resolves true if ICE, Reuters, or Bloomberg data show a Brent front-month settlement at or above USD 95.00 on any trading day in the window; false if no such settlement occurs.
- **Failure condition:** Brent front-month crude does not settle at or above USD 95.00 per barrel on any trading day between 2026-09-01 and 2026-09-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-81
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-23
- **Domain:** political
- **Claim:** German federal or state authorities publicly name a suspect or announce charges in the Leipzig drone attack on a Ukrainian-linked aircraft, between 2026-09-01 and 2026-09-21.
- **Resolution criterion:** Resolves true if German federal or state prosecutors or police publicly name a suspect or announce charges in the Leipzig drone-attack case within the window; false if no naming occurs.
- **Failure condition:** No German federal or state authority publicly names a suspect or announces charges in the Leipzig drone-attack case between 2026-09-01 and 2026-09-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-36
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-09-23
- **Domain:** disaster
- **Claim:** GDACS raises tropical cyclone NORBERT-26 (eventid 1001320) to Orange or Red alert level at some point between 2026-09-10 and 2026-09-20.
- **Resolution criterion:** The GDACS event page for tropical cyclone NORBERT-26 (eventtype TC, eventid 1001320) lists at least one episode dated between 2026-09-10 and 2026-09-20 with alert level Orange or Red.
- **Failure condition:** Every GDACS episode for NORBERT-26 dated 2026-09-10 to 2026-09-20 carries a Green alert level.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-46
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-09-23
- **Domain:** disaster
- **Claim:** GDACS raises tropical cyclone NORBERT-26 (eventid 1001320) to Orange or Red alert level at some point between 2026-09-10 and 2026-09-20.
- **Resolution criterion:** The GDACS event page for tropical cyclone NORBERT-26 (eventtype TC, eventid 1001320) lists at least one episode dated between 2026-09-10 and 2026-09-20 with alert level Orange or Red.
- **Failure condition:** Every GDACS episode for NORBERT-26 dated 2026-09-10 to 2026-09-20 carries a Green alert level.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-09
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-23
- **Domain:** economics/markets
- **Claim:** Between 2026-09-14 and 2026-09-20, the 10-year U.S. Treasury yield will exceed 5.0% on at least one weekday.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 5.0% on at least one weekday between 2026-09-14 and 2026-09-20.
- **Failure condition:** The 10-year U.S. Treasury yield never exceeds 5.0% on any weekday between 2026-09-14 and 2026-09-20.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T031940ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 5 business days in window; max BC_10YEAR 5.01 on 2026-09-16; threshold > 5.00; 2 day(s) satisfying

### KKR-20260912-06
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-23
- **Domain:** military/conflict
- **Claim:** Between 2026-09-13 and 2026-09-19, at least one of the following will be reported in two or more independent wire services: a drone strike on a Ukrainian military target in Kyiv or a missile strike on a Russian military installation in Moscow.
- **Resolution criterion:** At least one of the following will be reported in two or more independent wire services: a drone strike on a Ukrainian military target in Kyiv or a missile strike on a Russian military installation in Moscow, with the event window falling between 2026-09-13 and 2026-09-19.
- **Failure condition:** No such event is reported in two or more independent wire services during the specified window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-07
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-23
- **Domain:** disaster
- **Claim:** Between 2026-09-15 and 2026-09-22, the USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Indonesia.
- **Resolution criterion:** The USGS Significant Quakes catalog will record a magnitude 6.0 or greater earthquake in Indonesia between 2026-09-15 and 2026-09-22.
- **Failure condition:** No magnitude 6.0 or greater earthquake is recorded in Indonesia between 2026-09-15 and 2026-09-22 in the USGS Significant Quakes catalog.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261004T031940ZZ - sha256 4e5864f0e5fc1359...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-15&endtime=2026-09-22&minlatitude=-11.0&maxlatitude=6.0&minlongitude=95.0&maxlongitude=141.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260809-07
- **Issued:** 2026-08-09  ·  **Deadline:** 2026-09-24
- **Domain:** military/conflict
- **Claim:** Iran and Oman publicly announce a concluded arrangement governing commercial transit through the Strait of Hormuz, announced between 2026-08-11 and 2026-09-20.
- **Resolution criterion:** An Iranian government or IRGC source and an Omani government source both describe a concluded transit arrangement, carried by Reuters plus one of AP, AFP, or Oman News Agency.
- **Failure condition:** No concluded Iran-Oman arrangement governing Strait of Hormuz transit is announced by either government inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-24
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-09-24
- **Domain:** military_conflict
- **Claim:** Between 2026-08-17 and 2026-09-20, Iranian forces seize, board, or detain at least one commercial vessel in the Strait of Hormuz or the Gulf of Oman.
- **Resolution criterion:** UKMTO issues an incident advisory and Reuters or Lloyds List reports an Iranian seizure, boarding, or detention of a commercial vessel in those waters occurring inside the window.
- **Failure condition:** No Iranian seizure, boarding, or detention of a commercial vessel occurs in those waters inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-29
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-09-24
- **Domain:** military_conflict
- **Claim:** Between 2026-08-17 and 2026-09-20, Iranian forces seize, board, or detain at least one commercial vessel in the Strait of Hormuz or the Gulf of Oman.
- **Resolution criterion:** UKMTO issues an incident advisory and Reuters or Lloyds List reports an Iranian seizure, boarding, or detention of a commercial vessel in those waters occurring inside the window.
- **Failure condition:** No Iranian seizure, boarding, or detention of a commercial vessel occurs in those waters inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-33
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-09-24
- **Domain:** cyber
- **Claim:** A specific victim organization of the City-Forum data-theft campaign against Salesforce Experience Cloud and ServiceNow portals will be publicly named, by the victim, by Reco, or by another named security-research firm, between 2026-08-13 and 2026-09-22.
- **Resolution criterion:** A named security vendor, the victim itself, or a wire service publicly identifies a specific organization as a confirmed City-Forum campaign victim, in reporting dated between 2026-08-13 and 2026-09-24.
- **Failure condition:** No specific organization has been publicly named as a City-Forum campaign victim, as of 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260813-37
- **Issued:** 2026-08-13  ·  **Deadline:** 2026-09-24
- **Domain:** cyber
- **Claim:** A specific victim organization of the City-Forum data-theft campaign against Salesforce Experience Cloud and ServiceNow portals will be publicly named, by the victim, by Reco, or by another named security-research firm, between 2026-08-13 and 2026-09-22.
- **Resolution criterion:** A named security vendor, the victim itself, or a wire service publicly identifies a specific organization as a confirmed City-Forum campaign victim, in reporting dated between 2026-08-13 and 2026-09-24.
- **Failure condition:** No specific organization has been publicly named as a City-Forum campaign victim, as of 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-11
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-09-24
- **Domain:** military_conflict
- **Claim:** Ukrainian long-range strikes halt loadings at a named Russian crude export terminal - Novorossiysk, Tuapse, Primorsk, or Ust-Luga - with the strike occurring between 2026-08-24 and 2026-09-21.
- **Resolution criterion:** Reuters or Bloomberg reports suspended loadings at one of those four terminals attributed to a strike inside the window, and a Russian federal or regional official confirms the attack, by 2026-09-24.
- **Failure condition:** No suspension of loadings at any of the four named terminals follows a strike occurring inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-16
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-09-24
- **Domain:** military_conflict
- **Claim:** Ukrainian long-range strikes halt loadings at a named Russian crude export terminal - Novorossiysk, Tuapse, Primorsk, or Ust-Luga - with the strike occurring between 2026-08-24 and 2026-09-21.
- **Resolution criterion:** Reuters or Bloomberg reports suspended loadings at one of those four terminals attributed to a strike inside the window, and a Russian federal or regional official confirms the attack, by 2026-09-24.
- **Failure condition:** No suspension of loadings at any of the four named terminals follows a strike occurring inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-25
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-24
- **Domain:** military_conflict
- **Claim:** A single Russian strike on Kyiv city occurring between 2026-08-21 and 2026-09-20 kills at least 10 people according to Ukrainian official figures.
- **Resolution criterion:** At least two of Reuters, AP, BBC and Guardian report one strike event in Kyiv city inside the window carrying an official Ukrainian death toll of 10 or more.
- **Failure condition:** The highest official Ukrainian toll attributed to any single Kyiv strike inside the window is nine or fewer.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-02
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-24
- **Domain:** cyber
- **Claim:** The CISA KEV catalog includes at least one new exploited vulnerability with a public exploit between 2026-09-15 and 2026-09-22.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-15 and 2026-09-22 for at least one vulnerability that is marked as actively exploited in the wild.
- **Failure condition:** The CISA KEV catalog does not contain any new entries with a date-added value in the specified window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-63
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-24
- **Domain:** cyber
- **Claim:** On 2026-09-22, the CISA KEV catalog will include at least one new entry for a vulnerability exploited in the wild, with a date-added value between 2026-09-17 and 2026-09-21.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-09-17 and 2026-09-21 for at least one new entry.
- **Failure condition:** The CISA KEV catalog contains no new entries with a date-added value in the specified window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-10
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-24
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-09-21, at least one confirmed airstrike in the Khan Younis area will be reported by three or more independent outlets with hostile bias.
- **Resolution criterion:** Between 2026-09-15 and 2026-09-21, at least one confirmed airstrike in the Khan Younis area is reported by three or more independent outlets with hostile bias (AXIS, IL, PS).
- **Failure condition:** No airstrike in the Khan Younis area between 2026-09-15 and 2026-09-21 is reported by three or more independent outlets with hostile bias.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-10
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** economics/markets
- **Claim:** Between 2026-09-15 and 2026-09-22, the 10-year U.S. Treasury yield will exceed 5.00 percent at any point during the window.
- **Resolution criterion:** The 10-year U.S. Treasury yield, as reported by FRED or the U.S. Department of the Treasury, reaches or exceeds 5.00 percent at any point between 2026-09-15 and 2026-09-22.
- **Failure condition:** The 10-year U.S. Treasury yield never reaches or exceeds 5.00 percent during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T031940ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 6 business days in window; max BC_10YEAR 5.01 on 2026-09-16; threshold > 5.00; 2 day(s) satisfying

### KKR-20260915-11
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-09-22, a drone strike will be reported in Kyiv with at least one casualty confirmed by two independent sources.
- **Resolution criterion:** A drone strike in Kyiv is confirmed by two or more independent sources (e.g., Al Jazeera, BBC World, Deutsche Welle) with at least one casualty reported in corroborating reports.
- **Failure condition:** No drone strike in Kyiv is confirmed by two independent sources, or no casualty is reported in corroborating reports.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-12
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** disaster
- **Claim:** Between 2026-09-15 and 2026-09-22, a major oil pipeline disruption in the Panama Canal region will be confirmed by two independent sources due to drought.
- **Resolution criterion:** A major disruption to oil pipeline traffic in the Panama Canal region is confirmed by two independent sources (e.g., Guardian World, BBC World) due to drought conditions linked to El Niño.
- **Failure condition:** No major oil pipeline disruption in the Panama Canal region is confirmed by two independent sources due to drought.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-13
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-09-22, a U.S. military statement will confirm the deployment of weapons in space, verified by two independent sources.
- **Resolution criterion:** A U.S. military statement confirming the deployment of weapons in space is reported by two or more independent sources (e.g., BBC World, Al Jazeera, Guardian World) with no contradictory denial.
- **Failure condition:** No U.S. military statement confirming deployment of weapons in space is confirmed by two independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-14
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** cyber
- **Claim:** Between 2026-09-15 and 2026-09-22, a cyberattack targeting a U.S. federal agency will be attributed to a China-linked group by CISA.
- **Resolution criterion:** CISA issues a public advisory attributing a cyberattack on a U.S. federal agency to a China-linked threat actor during the event window.
- **Failure condition:** CISA does not issue a public advisory attributing a cyberattack on a U.S. federal agency to a China-linked group.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-15
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-09-22, the Strait of Hormuz will see a confirmed tanker attack with at least one casualty, verified by two independent sources.
- **Resolution criterion:** A confirmed tanker attack in the Strait of Hormuz with at least one casualty is reported by two or more independent sources (e.g., BBC World, Al Jazeera).
- **Failure condition:** No tanker attack in the Strait of Hormuz with at least one casualty is confirmed by two independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-16
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** political
- **Claim:** Between 2026-09-15 and 2026-09-22, a political statement by Zelenskyy will be confirmed by two independent sources stating Ukraine will pause attacks if Russia spares infrastructure.
- **Resolution criterion:** A statement by Zelenskyy confirming Ukraine will pause attacks if Russia spares infrastructure is reported by two or more independent sources (e.g., Al Jazeera, BBC World).
- **Failure condition:** No such statement by Zelenskyy is confirmed by two independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-17
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-09-24
- **Domain:** disaster
- **Claim:** Between 2026-09-15 and 2026-09-22, a major forest fire in Australia will be reported by GDACS Alerts with a green alert level.
- **Resolution criterion:** GDACS Alerts issues a green forest fire notification for Australia during the event window.
- **Failure condition:** GDACS Alerts does not issue a green forest fire notification for Australia during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-02
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Major General Brandon R. Tegtmeier will no longer be named as commanding officer of the 82nd Airborne Division in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://www.army.mil/82ndairborne : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-05
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Lieutenant General Benedikt Roos will no longer be named as commanding officer of the Swiss Armed Forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://www.vtg.admin.ch/en/chief-of-the-armed-forces-roos : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-06
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Lieutenant General Sullay Ibrahim Sesay will no longer be named as commanding officer of the Sierra Leone - national armed forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://en.wikipedia.org/wiki/Chief_of_the_Defence_Staff_(Sierra_Leone) : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-07
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** General Olufemi Oluyede will no longer be named as commanding officer of the Nigeria - national armed forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://en.wikipedia.org/wiki/Chief_of_Defence_Staff_(Nigeria) : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-08
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Army corps general Lassina Doumbia will no longer be named as commanding officer of the Ivory Coast - national armed forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://en.wikipedia.org/wiki/Chief_of_the_Defence_Staff_(Ivory_Coast) : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-09
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Air Chief Marshal Richard Knighton will no longer be named as commanding officer of the United Kingdom - national armed forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://en.wikipedia.org/wiki/Chief_of_the_Defence_Staff_(United_Kingdom) : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260727-10
- **Issued:** 2026-07-27  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** General Luciano Portolano will no longer be named as commanding officer of the Italy - national armed forces in the source of record on 2026-09-25.
- **Resolution criterion:** Resolved on 2026-09-25 by inspecting https://en.wikipedia.org/wiki/Chief_of_the_Defence_Staff_(Italy) : hit if a different officer is named, miss if the same officer is named.
- **Failure condition:** the same officer is named, as read from the resolution basis on 2026-09-25; that reading scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260801-19
- **Issued:** 2026-08-01  ·  **Deadline:** 2026-09-25
- **Domain:** crime/security
- **Claim:** The Department of Justice will publicly release the Epstein-related documents subject to the New Mexico deadline noted in reporting as of 2026-08-01, on or before 2026-09-25.
- **Resolution criterion:** Resolved from justice.gov releases and the docket of the underlying New Mexico court matter on 2026-09-25. Yes if DOJ has publicly released the documents subject to that deadline.
- **Failure condition:** the condition stated in this entry's resolution basis — DOJ has publicly released the documents subject to that deadline — is not met on or before 2026-09-25 as read from justice.gov releases and the docket of the underlying New Mexico court matter; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-26
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-09-25
- **Domain:** disaster
- **Claim:** USGS records an earthquake of magnitude 5.5 or greater within 100 km of the 2026-08-20 M6.7 Aniso, Peru epicenter (14.641 S, 73.524 W) with origin time between 2026-08-24 and 2026-09-23.
- **Resolution criterion:** The USGS ComCat catalog lists an event of magnitude 5.5 or greater, any depth, within 100 km of 14.641 S 73.524 W, origin time 2026-08-24 00:00 UTC to 2026-09-23 23:59 UTC.
- **Failure condition:** No USGS ComCat event of magnitude 5.5 or greater within 100 km of the epicenter has an origin time between 2026-08-24 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-23
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-09-25
- **Domain:** cyber
- **Claim:** CISA adds at least one new Microsoft Exchange Server vulnerability to the Known Exploited Vulnerabilities catalog between 2026-09-02 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog shows a dateAdded value in the window for a CVE with vendorProject Microsoft and a product field containing Exchange. FALSE otherwise.
- **Failure condition:** No Microsoft Exchange Server CVE is added to the CISA KEV catalog during the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031942ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['Microsoft', 'Exchange'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows - CVE-2026-81963, CVE-2026-85880

### KKR-20260902-20
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-25
- **Domain:** cyber
- **Claim:** CISA adds at least one new Microsoft Exchange Server vulnerability to the Known Exploited Vulnerabilities catalog between 2026-09-02 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog shows a dateAdded value in the window for a CVE with vendorProject Microsoft and a product field containing Exchange. FALSE otherwise.
- **Failure condition:** No Microsoft Exchange Server CVE is added to the CISA KEV catalog during the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031944ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['Microsoft', 'Exchange'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows - CVE-2026-81963, CVE-2026-85880

### KKR-20260903-25
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-25
- **Domain:** economic
- **Claim:** ICE Brent crude front-month futures settle at or above 90.00 USD/bbl on 2026-09-25. Reference: 96.70 on the packet date (2026-09-03).
- **Resolution criterion:** ICE Brent front-month futures daily settlement price on 2026-09-25 is 90.00 USD/bbl or higher, per exchange settlement data.
- **Failure condition:** The 2026-09-25 ICE Brent front-month settlement price closes below 90.00 USD/bbl.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-26
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-25
- **Domain:** economic
- **Claim:** COMEX gold front-month futures settle at or above 4300.00 USD/oz on 2026-09-25. Reference: 4546.20 on the packet date (2026-09-03).
- **Resolution criterion:** COMEX gold front-month futures daily settlement price on 2026-09-25 is 4300.00 USD/oz or higher, per exchange settlement data.
- **Failure condition:** The 2026-09-25 COMEX gold front-month settlement price closes below 4300.00 USD/oz.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-56
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-25
- **Domain:** economic
- **Claim:** ICE Brent crude front-month futures settle at or above 90.00 USD/bbl on 2026-09-25. Reference: 96.70 on the packet date (2026-09-03).
- **Resolution criterion:** ICE Brent front-month futures daily settlement price on 2026-09-25 is 90.00 USD/bbl or higher, per exchange settlement data.
- **Failure condition:** The 2026-09-25 ICE Brent front-month settlement price closes below 90.00 USD/bbl.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-57
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-09-25
- **Domain:** economic
- **Claim:** COMEX gold front-month futures settle at or above 4300.00 USD/oz on 2026-09-25. Reference: 4546.20 on the packet date (2026-09-03).
- **Resolution criterion:** COMEX gold front-month futures daily settlement price on 2026-09-25 is 4300.00 USD/oz or higher, per exchange settlement data.
- **Failure condition:** The 2026-09-25 COMEX gold front-month settlement price closes below 4300.00 USD/oz.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-20
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-09-25
- **Domain:** cyber
- **Claim:** CISA adds the Chrome V8 zero-day CVE-2026-87491, disclosed by Google on 2026-09-08 as exploited in the wild, to its Known Exploited Vulnerabilities catalog between 2026-09-09 and 2026-09-23.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry for CVE-2026-87491 with a dateAdded value between 2026-09-09 and 2026-09-23 inclusive.
- **Failure condition:** CVE-2026-87491 is absent from the KEV catalog at the deadline, or its dateAdded value falls outside 2026-09-09 to 2026-09-23.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031946ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-87491'] with dateAdded in [2026-09-09..2026-09-23] across 1733 catalog rows - CVE-2026-87491

### KKR-20260909-28
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-09-25
- **Domain:** cyber
- **Claim:** CISA adds the Chrome V8 zero-day CVE-2026-87491, disclosed by Google on 2026-09-08 as exploited in the wild, to its Known Exploited Vulnerabilities catalog between 2026-09-09 and 2026-09-23.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry for CVE-2026-87491 with a dateAdded value between 2026-09-09 and 2026-09-23 inclusive.
- **Failure condition:** CVE-2026-87491 is absent from the KEV catalog at the deadline, or its dateAdded value falls outside 2026-09-09 to 2026-09-23.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031948ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-87491'] with dateAdded in [2026-09-09..2026-09-23] across 1733 catalog rows - CVE-2026-87491

### KKR-20260911-11
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-25
- **Domain:** economics/markets
- **Claim:** Between 2026-09-16 and 2026-09-22, the U.S. dollar will trade above 1.17 against the euro on at least one weekday.
- **Resolution criterion:** The EUR/USD exchange rate is below 1.17 on at least one weekday between 2026-09-16 and 2026-09-22.
- **Failure condition:** The EUR/USD exchange rate never trades below 1.17 on any weekday between 2026-09-16 and 2026-09-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-08
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-25
- **Domain:** military/conflict
- **Claim:** Between 2026-09-16 and 2026-09-23, at least one of the following will be reported in two or more independent outlets: a Houthi attack on a commercial vessel in the Red Sea or a Saudi-led coalition airstrike on a Houthi position in Yemen.
- **Resolution criterion:** At least one of the following will be reported in two or more independent outlets: a Houthi attack on a commercial vessel in the Red Sea or a Saudi-led coalition airstrike on a Houthi position in Yemen, with the event window falling between 2026-09-16 and 2026-09-23.
- **Failure condition:** No such event is reported in two or more independent outlets during the specified window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-09
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-25
- **Domain:** economics/markets
- **Claim:** Between 2026-09-17 and 2026-09-24, the 10-year U.S. Treasury yield will close above 5.0 percent on at least one weekday.
- **Resolution criterion:** The 10-year U.S. Treasury yield will close above 5.0 percent on at least one weekday between 2026-09-17 and 2026-09-24.
- **Failure condition:** The 10-year U.S. Treasury yield closes at or below 5.0 percent on every weekday between 2026-09-17 and 2026-09-24.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T031949ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 6 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold > 5.00; 3 day(s) satisfying

### KKR-20260827-06
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-09-26
- **Domain:** cyber
- **Claim:** Norway's National Security Authority or Police Security Service will publicly name a specific threat actor, group, or state as responsible for the 2026-08-25 DDoS attack on Norwegian government digital services, in a statement dated between 2026-08-27 and 2026-09-24.
- **Resolution criterion:** NSM, PST, or the Norwegian government issues a statement naming a specific actor for the Aug 25 DDoS attack, dated between 2026-08-27 and 2026-09-24, per at least one national or wire outlet.
- **Failure condition:** No Norwegian government body names a specific actor for the Aug 25 DDoS attack by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-38
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-09-26
- **Domain:** cyber
- **Claim:** Norway's National Security Authority or Police Security Service will publicly name a specific threat actor, group, or state as responsible for the 2026-08-25 DDoS attack on Norwegian government digital services, in a statement dated between 2026-08-27 and 2026-09-24.
- **Resolution criterion:** NSM, PST, or the Norwegian government issues a statement naming a specific actor for the Aug 25 DDoS attack, dated between 2026-08-27 and 2026-09-24, per at least one national or wire outlet.
- **Failure condition:** No Norwegian government body names a specific actor for the Aug 25 DDoS attack by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-64
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-26
- **Domain:** military/conflict
- **Claim:** Between 2026-09-21 and 2026-09-24, a drone strike will be confirmed by at least two hostile sides in the Kyiv theater, with weapons reported as drone and casualties stated in at least one corroborating report.
- **Resolution criterion:** At least two hostile sides (RU, UA, AXIS, WEST) report a drone strike in Kyiv between 2026-09-21 and 2026-09-24, with weapons reported as drone and casualties stated in at least one corroborating report.
- **Failure condition:** No drone strike is confirmed by two hostile sides in Kyiv between 2026-09-21 and 2026-09-24, or no casualties are stated in corroborating reports.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-02
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-26
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a Green flood alert is issued for Spain by GDACS and remains active through 2026-09-24.
- **Resolution criterion:** The GDACS Alerts system carries a Green flood alert for Spain with a status of active on 2026-09-24.
- **Failure condition:** No Green flood alert for Spain is active on GDACS on 2026-09-24.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-04
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-26
- **Domain:** disaster
- **Claim:** Between 2026-09-21 and 2026-09-24, a new earthquake of magnitude 5.0 or higher is recorded in Indonesia with a depth less than 100 km, as confirmed by USGS.
- **Resolution criterion:** The USGS Significant Quakes system records an earthquake with magnitude ≥5.0 and depth <100 km in Indonesia between 2026-09-21 and 2026-09-24.
- **Failure condition:** No such earthquake is recorded by USGS in Indonesia during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-12
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-26
- **Domain:** cyber
- **Claim:** Between 2026-09-17 and 2026-09-23, at least one new cyberattack exploiting CVE-2026-67277 will be reported by two or more independent outlets.
- **Resolution criterion:** Between 2026-09-17 and 2026-09-23, at least one cyberattack exploiting CVE-2026-67277 is reported by two or more independent outlets.
- **Failure condition:** No cyberattack exploiting CVE-2026-67277 is reported by two or more independent outlets between 2026-09-17 and 2026-09-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-19
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-26
- **Domain:** disaster_infrastructure
- **Claim:** Indonesia's BNPB or BMKG attributes at least 1 fatality to the 12 September 2026 M6.5 earthquake near Teluknaga (USGS event us7000tgrk), in a report published by 2026-09-26
- **Resolution criterion:** TRUE if BNPB, BMKG, or a wire service attributes at least one fatality to this earthquake by the deadline; FALSE otherwise
- **Failure condition:** No fatality is attributed to this earthquake by the deadline
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-25
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-26
- **Domain:** disaster_infrastructure
- **Claim:** Indonesia's BNPB or BMKG attributes at least 1 fatality to the 12 September 2026 M6.5 earthquake near Teluknaga (USGS event us7000tgrk), in a report published by 2026-09-26
- **Resolution criterion:** TRUE if BNPB, BMKG, or a wire service attributes at least one fatality to this earthquake by the deadline; FALSE otherwise
- **Failure condition:** No fatality is attributed to this earthquake by the deadline
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-04
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-09-26
- **Domain:** political
- **Claim:** On 2026-09-23, a new political coalition in Sweden is formed following the general election, with the far-right party securing a ministerial role, as confirmed by the Swedish government's official website and two international news agencies.
- **Resolution criterion:** The Swedish government's official website and two international news agencies (e.g., BBC, Al Jazeera) confirm the formation of a new coalition government with a far-right minister on 2026-09-23.
- **Failure condition:** No confirmation from the Swedish government or two international agencies that a far-right minister was included in the new coalition by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-07
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** disaster
- **Claim:** Between 2026-09-18 and 2026-09-24, the USGS Significant Quakes feed will report a magnitude 6.5 or higher earthquake in the Fox Islands, Aleutian Islands, with a depth of 100 km or more.
- **Resolution criterion:** The USGS Significant Quakes feed reports a magnitude 6.5 or higher earthquake in the Fox Islands, Aleutian Islands, with a depth of 100 km or more.
- **Failure condition:** No magnitude 6.5 or higher earthquake with a depth of 100 km or more is reported in the Fox Islands, Aleutian Islands, by the USGS Significant Quakes feed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-08
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** military/conflict
- **Claim:** Between 2026-09-18 and 2026-09-24, at least one of the following will occur: a drone strike on Kyiv confirmed by two hostile sides, or a ballistic missile attack on Kharkiv confirmed by two hostile sides.
- **Resolution criterion:** At least one of the following occurs: a drone strike on Kyiv confirmed by two hostile sides, or a ballistic missile attack on Kharkiv confirmed by two hostile sides.
- **Failure condition:** No drone strike on Kyiv or ballistic missile attack on Kharkiv is confirmed by two hostile sides within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-09
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** cyber
- **Claim:** Between 2026-09-18 and 2026-09-24, a new vulnerability in Cisco Identity Services Engine (ISE) will be exploited in at least one confirmed cyberattack, as reported by two independent sources.
- **Resolution criterion:** A new vulnerability in Cisco Identity Services Engine (ISE) is exploited in at least one confirmed cyberattack, as reported by two independent sources.
- **Failure condition:** No confirmed cyberattack exploiting a new Cisco ISE vulnerability is reported by two independent sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-10
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** political
- **Claim:** Between 2026-09-18 and 2026-09-24, the European Union will formally propose associate membership for Canada, as confirmed by two independent news outlets.
- **Resolution criterion:** The European Union formally proposes associate membership for Canada, as confirmed by two independent news outlets.
- **Failure condition:** The European Union does not formally propose associate membership for Canada, or the proposal is not confirmed by two independent news outlets.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-11
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** disaster
- **Claim:** Between 2026-09-18 and 2026-09-24, at least one of the following will occur: a flood warning issued in the Upper Rio Grande Valley, or a flash flood warning issued in the Eastern San Juan Mountains.
- **Resolution criterion:** At least one of the following occurs: a flood warning issued in the Upper Rio Grande Valley, or a flash flood warning issued in the Eastern San Juan Mountains.
- **Failure condition:** No flood warning in the Upper Rio Grande Valley and no flash flood warning in the Eastern San Juan Mountains is issued during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-12
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** economics/markets
- **Claim:** Between 2026-09-18 and 2026-09-24, the Bank of England will leave interest rates unchanged, as confirmed by a press release from the Bank.
- **Resolution criterion:** The Bank of England leaves interest rates unchanged, as confirmed by a press release from the Bank.
- **Failure condition:** The Bank of England changes interest rates or does not issue a press release confirming unchanged rates.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-13
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** political
- **Claim:** Between 2026-09-18 and 2026-09-24, the U.S. House will vote to hold billionaire Epstein associate Leon Black in contempt of Congress, as confirmed by a roll call vote on Congress.gov.
- **Resolution criterion:** The U.S. House votes to hold billionaire Epstein associate Leon Black in contempt of Congress, as confirmed by a roll call vote on Congress.gov.
- **Failure condition:** The U.S. House does not vote to hold Leon Black in contempt of Congress, or the vote is not recorded on Congress.gov.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-14
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-09-26
- **Domain:** cyber
- **Claim:** Between 2026-09-18 and 2026-09-24, a new AI-powered data breach will be reported in Spain, as confirmed by a public statement from Spain's data agency.
- **Resolution criterion:** A new AI-powered data breach is reported in Spain, as confirmed by a public statement from Spain's data agency.
- **Failure condition:** No AI-powered data breach is reported in Spain, or Spain's data agency does not issue a public statement confirming one.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-06
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-09-27
- **Domain:** cyber
- **Claim:** A cyberattack exploiting a known vulnerability in Cisco routers, confirmed by CISA, occurs between 2026-09-18 and 2026-09-25.
- **Resolution criterion:** The CISA KEV catalog includes a vulnerability with a public exploit that is confirmed to have been used in a cyberattack against Cisco routers, with the first report of exploitation appearing between 2026-09-18 and 2026-09-25.
- **Failure condition:** No confirmed cyberattack exploiting a known Cisco router vulnerability is reported by CISA or two independent sources within the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031950ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Cisco'] with dateAdded in [2026-09-18..2026-09-25] across 1733 catalog rows

### KKR-20260906-65
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-27
- **Domain:** disaster
- **Claim:** Between 2026-09-22 and 2026-09-25, a volcanic eruption will cause flight cancellations at Jakarta International Airport, with at least 100,000 passengers stranded, as confirmed by two independent sources.
- **Resolution criterion:** Between 2026-09-22 and 2026-09-25, a volcanic eruption causes flight cancellations at Jakarta International Airport, with at least 100,000 passengers stranded, as confirmed by two independent sources.
- **Failure condition:** No volcanic eruption causes flight cancellations at Jakarta International Airport with at least 100,000 passengers stranded between 2026-09-22 and 2026-09-25, or no two independent sources confirm it.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-66
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-27
- **Domain:** political
- **Claim:** Between 2026-09-21 and 2026-09-25, Iran will issue a public statement via a hostile side (AXIS or WEST) claiming a 'more painful' response to U.S. attacks, with the statement confirmed by two independent sources.
- **Resolution criterion:** Between 2026-09-21 and 2026-09-25, Iran issues a public statement via a hostile side (AXIS or WEST) claiming a 'more painful' response to U.S. attacks, confirmed by two independent sources.
- **Failure condition:** No public statement by Iran claiming a 'more painful' response to U.S. attacks is confirmed by two independent sources between 2026-09-21 and 2026-09-25.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-67
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-09-27
- **Domain:** cyber
- **Claim:** Between 2026-09-21 and 2026-09-25, a cyberattack exploiting a zero-day vulnerability in Magento or Adobe Commerce will be confirmed by two independent sources, with the attack resulting in data exfiltration.
- **Resolution criterion:** Between 2026-09-21 and 2026-09-25, a cyberattack exploiting a zero-day vulnerability in Magento or Adobe Commerce is confirmed by two independent sources, with the attack resulting in data exfiltration.
- **Failure condition:** No cyberattack exploiting a zero-day vulnerability in Magento or Adobe Commerce is confirmed by two independent sources between 2026-09-21 and 2026-09-25, or no data exfiltration is confirmed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-13
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-09-27
- **Domain:** political
- **Claim:** Between 2026-09-18 and 2026-09-24, at least one major political statement about Iran's nuclear program will be made by a U.S. or EU official and confirmed by cross-bias agreement across two hostile sides.
- **Resolution criterion:** Between 2026-09-18 and 2026-09-24, at least one major political statement about Iran's nuclear program is made by a U.S. or EU official and confirmed by cross-bias agreement across two hostile sides (AXIS, WEST).
- **Failure condition:** No major political statement about Iran's nuclear program made by a U.S. or EU official between 2026-09-18 and 2026-09-24 is confirmed by cross-bias agreement across two hostile sides.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-10
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-09-27
- **Domain:** disaster
- **Claim:** Between 2026-09-18 and 2026-09-25, the GDACS Alerts system will issue a Red or Orange alert for a forest fire in Russia or Kazakhstan.
- **Resolution criterion:** The GDACS Alerts system will issue a Red or Orange alert for a forest fire in Russia or Kazakhstan between 2026-09-18 and 2026-09-25.
- **Failure condition:** No Red or Orange forest fire alert is issued by GDACS Alerts for Russia or Kazakhstan between 2026-09-18 and 2026-09-25.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - gdacs - fetched 20261004T031952ZZ - sha256 0eea3e071c29c190...
  - instrument: https://www.gdacs.org/xml/rss.xml
  - observed: no live match in 172 feed items — the RSS is a current-state feed; absence now does not adjudicate the whole window. Archive check is the operator's.

### KKR-20260726-17
- **Issued:** 2026-07-26  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** A major cyberattack on a U.S. state government website results in public data exposure between 2026-09-25 and 2026-09-28.
- **Resolution criterion:** A U.S. state government website suffers a confirmed data breach resulting in public exposure of personal data, as reported by at least two independent news sources between 2026-09-25 and 2026-09-28.
- **Failure condition:** the condition stated in this entry's resolution basis — A U.S. state government website suffers a confirmed data breach resulting in public exposure of personal data, as reported by at least two independent news sources between 2026-09-25 and 2026-09-28 — is not met on or before 2026-09-28; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-23
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-09-28
- **Domain:** crime/security
- **Claim:** A jury will return a verdict, guilty or not guilty, in the Duane Keffe D Davis murder trial in Clark County, Nevada, between 2026-09-07 and 2026-09-25.
- **Resolution criterion:** TRUE if Clark County District Court or at least two independent wire services report a jury verdict in the Davis trial inside the window; a hung jury counts as FALSE; adjudicated 2026-09-28.
- **Failure condition:** No jury verdict is delivered in the Davis trial during the window, whether from delay, extended deliberation, or a mistrial.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-39
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-09-28
- **Domain:** crime/security
- **Claim:** A jury will return a verdict, guilty or not guilty, in the Duane Keffe D Davis murder trial in Clark County, Nevada, between 2026-09-07 and 2026-09-25.
- **Resolution criterion:** TRUE if Clark County District Court or at least two independent wire services report a jury verdict in the Davis trial inside the window; a hung jury counts as FALSE; adjudicated 2026-09-28.
- **Failure condition:** No jury verdict is delivered in the Davis trial during the window, whether from delay, extended deliberation, or a mistrial.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-22
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-09-28
- **Domain:** crime_security
- **Claim:** Between 2026-08-20 and 2026-09-24, Jewel Howard-Taylor, former Vice President of Liberia charged 2026-08-19 with drug trafficking and money laundering, will make a first court appearance in Liberia, reported by Reuters, AP, or BBC.
- **Resolution criterion:** TRUE if Reuters, AP, or BBC report a first court appearance, arraignment, or bail hearing for Jewel Howard-Taylor in a Liberian court between 2026-08-20 and 2026-09-24.
- **Failure condition:** No Reuters, AP, or BBC report of a Liberian court appearance for Howard-Taylor exists within the window as of the deadline check.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-58
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** economic
- **Claim:** The 10-year US Treasury note yield closes at or above 5.00 percent on any trading day between 2026-09-03 and 2026-09-25. Reference: 4.80 percent on the packet date, 2026-09-02.
- **Resolution criterion:** TRUE if the Treasury.gov daily par yield curve or FRED series DGS10 records a 10-year close at or above 5.00 percent on any date in the window; FALSE otherwise.
- **Failure condition:** FRED or Treasury daily yield data shows no 10-year close at or above 5.00 percent within the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T031953ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 17 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold >= 5.00; 6 day(s) satisfying

### KKR-20260902-59
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** CISA adds a SonicWall SMA1000 vulnerability tied to the zero-days reported as actively exploited on 2026-09-02 to the Known Exploited Vulnerabilities catalog, with dateAdded between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a SonicWall SMA1000 CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline.
- **Failure condition:** The CISA KEV catalog carries no SonicWall SMA1000 entry with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031955ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['SonicWall SMA1000'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows - CVE-2026-83548, CVE-2026-83549

### KKR-20260902-60
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** CISA adds a GeoNetwork remote-code-execution vulnerability, the unauthenticated RCE chain reported affecting government geoportal backends on 2026-09-02, to the KEV catalog, with dateAdded between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a GeoNetwork-related CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline.
- **Failure condition:** The CISA KEV catalog carries no GeoNetwork-related entry with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031956ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['GeoNetwork'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows

### KKR-20260902-62
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** disaster_infrastructure
- **Claim:** Nepal's National Disaster Risk Reduction and Management Authority reports a confirmed death toll of at least 1,500 from the August-September 2026 Nepal-Tibet floods, reported between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if NDRRMA, Nepal's Home Ministry, or two independent wire services report a confirmed death toll of 1,500 or more within the window; FALSE if the reported toll stays below 1,500 throughout.
- **Failure condition:** NDRRMA or wire reporting shows the confirmed Nepal-Tibet flood death toll remains below 1,500 through the end of the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260902-77
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** economic
- **Claim:** The 10-year US Treasury note yield closes at or above 5.00 percent on any trading day between 2026-09-03 and 2026-09-25. Reference: 4.80 percent on the packet date, 2026-09-02.
- **Resolution criterion:** TRUE if the Treasury.gov daily par yield curve or FRED series DGS10 records a 10-year close at or above 5.00 percent on any date in the window; FALSE otherwise.
- **Failure condition:** FRED or Treasury daily yield data shows no 10-year close at or above 5.00 percent within the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261004T031957ZZ - sha256 b03a0a9d334d99d7...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 17 business days in window; max BC_10YEAR 5.18 on 2026-09-24; threshold >= 5.00; 6 day(s) satisfying

### KKR-20260902-78
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** CISA adds a SonicWall SMA1000 vulnerability tied to the zero-days reported as actively exploited on 2026-09-02 to the Known Exploited Vulnerabilities catalog, with dateAdded between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a SonicWall SMA1000 CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline.
- **Failure condition:** The CISA KEV catalog carries no SonicWall SMA1000 entry with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T031959ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['SonicWall SMA1000'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows - CVE-2026-83548, CVE-2026-83549

### KKR-20260902-79
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-09-28
- **Domain:** cyber
- **Claim:** CISA adds a GeoNetwork remote-code-execution vulnerability, the unauthenticated RCE chain reported affecting government geoportal backends on 2026-09-02, to the KEV catalog, with dateAdded between 2026-09-03 and 2026-09-23.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a GeoNetwork-related CVE with dateAdded inside the window; FALSE if no such entry appears by the deadline.
- **Failure condition:** The CISA KEV catalog carries no GeoNetwork-related entry with a dateAdded value inside the window by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261004T032000ZZ - sha256 d2c8c6cb23291b46...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['GeoNetwork'] with dateAdded in [2026-09-02..2026-09-23] across 1733 catalog rows

### KKR-20260902-81
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

### KKR-20260910-21
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

