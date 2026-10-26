# KKR RESOLUTION AUDIT PACKET
Generated 260002Z OCT 26 · 250 projections (part 2 of 2; packet total 709) past deadline, awaiting adjudication.

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

### KKR-20260815-18
- **Issued:** 2026-08-15  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** NATO or a Baltic national air force kinetically shoots down or intercepts a drone or unmanned aerial vehicle inside Estonian, Latvian, or Lithuanian airspace, distinct from the August 14, 2026 Balvi incident, between 2026-08-21 and 2026-10-15.
- **Resolution criterion:** NATO, a Baltic Ministry of Defence, or two of Reuters, AP, and Bloomberg confirm a kinetic drone shoot-down in Baltic airspace within the window, distinct from the Aug 14 Balvi incident.
- **Failure condition:** No kinetic shoot-down or destructive intercept of a drone occurs inside Estonian, Latvian, or Lithuanian airspace, distinct from the Aug 14 Balvi incident, between 2026-08-21 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-40
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** WTI crude oil settles at or above 90.00 USD per barrel on any trading day between 2026-08-17 and 2026-10-15.
- **Resolution criterion:** TRUE if the CME/NYMEX WTI front-month settlement price is at or above 90.00 USD per barrel on any trading day between 2026-08-17 and 2026-10-15; FALSE otherwise.
- **Failure condition:** WTI crude oil never settles at or above 90.00 USD per barrel between 2026-08-17 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260817-58
- **Issued:** 2026-08-17  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** A CVE identifier for the Microsoft Defender vulnerability publicly tracked as ShieldBreak is added to the CISA Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-08-18 and 2026-10-16.
- **Resolution criterion:** True if the CISA KEV catalog gains an entry for a Microsoft Defender vulnerability, identified in vendor or CISA documentation as ShieldBreak, with dateAdded between 2026-08-18 and 2026-10-16.
- **Failure condition:** No KEV entry attributable to the ShieldBreak Defender vulnerability carries a dateAdded value within the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000224ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Microsoft Defender', 'ShieldBreak'] with dateAdded in [2026-08-18..2026-10-16] across 1756 catalog rows

### KKR-20260819-16
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-10-19
- **Domain:** military/conflict
- **Claim:** The UAE government publicly attributes a missile or drone impact on UAE territory or territorial waters to Iran, for an impact in the window 2026-08-26 to 2026-10-15.
- **Resolution criterion:** Reuters and Agence France-Presse both report a UAE government statement attributing a missile or drone impact on UAE territory or territorial waters to Iran within the window.
- **Failure condition:** No UAE government statement in the window attributes a missile or drone impact on its territory or waters to Iran.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-25
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** Between 2026-08-19 and 2026-10-17, Ukraine's Verkhovna Rada or Central Election Commission formally schedules a date for a presidential election, following the sacked defence minister's public call for one.
- **Resolution criterion:** TRUE if the Verkhovna Rada or Ukraine's Central Election Commission issues an official act setting a presidential election date, reported by two of Reuters, AP, or Ukrainska Pravda, by 2026-10-19.
- **Failure condition:** Ukraine's Verkhovna Rada and Central Election Commission do not schedule a presidential election date during the window; the wartime suspension of elections remains in effect.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260819-26
- **Issued:** 2026-08-19  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Between 2026-08-19 and 2026-10-17, the WHO Director-General declares the Democratic Republic of Congo Ebola outbreak, which reached 5,000 cases this window, a Public Health Emergency of International Concern.
- **Resolution criterion:** TRUE if WHO's Director-General issues a formal PHEIC declaration covering the DRC Ebola outbreak between 2026-08-19 and 2026-10-17, per WHO statement and two wire services, by 2026-10-19.
- **Failure condition:** WHO's Director-General does not declare a PHEIC covering the DRC Ebola outbreak during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-26
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** United States forces conduct an officially acknowledged strike on targets inside Iranian territory between 2026-08-21 and 2026-10-15.
- **Resolution criterion:** The Department of Defense or the White House publicly confirms US munitions struck targets inside Iran, the strike dated inside the window, carried by both Reuters and AP.
- **Failure condition:** No US government confirmation places American munitions on Iranian soil inside the stated window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-37
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** Between 2026-08-24 and 2026-10-15, the Government of Canada will formally impose new tariffs on US goods, described by Canadian officials as a dollar for dollar or matching response to the US tariff increase reported on 2026-08-22.
- **Resolution criterion:** TRUE if Finance Canada or the Canadian government announces new tariffs on US goods described as a dollar for dollar or matching response, confirmed by Reuters or CBC; FALSE otherwise.
- **Failure condition:** Canada does not formally impose new tariffs on US goods framed as a dollar for dollar response between 2026-08-24 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260825-12
- **Issued:** 2026-08-25  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** On at least one day between 2026-08-26 and 2026-10-15, the Singapore National Environment Agency 24-hour PSI for at least one of the five reporting regions reaches 101 or higher.
- **Resolution criterion:** TRUE if NEA published 24-hour PSI data (data.gov.sg historical PSI or NEA haze page) shows a value of 101 or higher for any region on any day 2026-08-26 through 2026-10-15.
- **Failure condition:** Every NEA 24-hour regional PSI reading for every day in the window is 100 or below.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-78
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog entry for CVE-2026-8452, the Citrix NetScaler ADC and Gateway flaw added 2026-08-26, has its knownRansomwareCampaignUse field changed to Yes between 2026-09-03 and 2026-10-15.
- **Resolution criterion:** The public CISA KEV catalog feed at cisa.gov shows knownRansomwareCampaignUse equal to Yes for CVE-2026-8452, with the change falling inside the window, checked by 2026-10-19.
- **Failure condition:** The CISA KEV catalog entry for CVE-2026-8452 still reads Unknown, or never changes to Yes within the window, at the time of the deadline check.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000225ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['CVE-2026-8452'] with dateAdded in [2026-08-26..2026-10-15] across 1756 catalog rows - CVE-2026-8452

### KKR-20260827-120
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** The official confirmed death toll from the late-August 2026 Nepal-Tibet flash floods will stand at 750 or more at some point between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** Between 2026-09-01 and 2026-10-15, figures from the National Disaster Risk Reduction and Management Authority of Nepal plus official Chinese tallies for Tibet total 750 or more confirmed dead.
- **Failure condition:** The combined official confirmed death toll stands below 750 at the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-13
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** The combined confirmed death toll from the Nepal-Tibet flash floods reaches at least 1000 between 2026-08-29 and 2026-10-15.
- **Resolution criterion:** Official Nepali government figures or OCHA reporting state a combined Nepal and Tibet confirmed death toll of at least 1000 from the August 2026 flash floods, on or before 2026-10-15.
- **Failure condition:** Combined confirmed deaths acknowledged by Nepali authorities or OCHA remain below 1000 through 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-53
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-19
- **Domain:** military
- **Claim:** The Ukrainian Air Force reports at least 500 Russian drones and missiles launched in one overnight attack between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** TRUE if a Ukrainian Air Force overnight air-situation report covering a night inside that window states a combined launch total of 500 or more munitions.
- **Failure condition:** Every Ukrainian Air Force overnight tally in the window stays below 500 combined drones and missiles.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-10
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** A commercial vessel transiting the Strait of Hormuz will be attacked, seized, or forcibly diverted, as reported by UKMTO, Reuters, or AP, between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** TRUE if UKMTO, Reuters, or AP report an attack, seizure, or forced diversion of a commercial vessel in the Strait of Hormuz within the window; otherwise FALSE.
- **Failure condition:** No commercial vessel is attacked, seized, or forcibly diverted in the Strait of Hormuz between 2026-09-01 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-30
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** Manchester Airports Group confirms unauthorized access to its systems in an attributable statement issued between 2026-08-31 and 2026-10-16.
- **Resolution criterion:** TRUE if a named Manchester Airports Group spokesperson or an official company statement acknowledging unauthorized access to its systems or theft of its data is carried by at least two of BBC News, Reuters, and BleepingComputer, dated between 2026-08-31 and 2026-10-16, and verifiable by 2026-10-19.
- **Failure condition:** Manchester Airports Group does not confirm unauthorized access in the window; a denial, or a statement that only notes a third-party claim without confirming access, is a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-32
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** The confirmed cumulative death toll for the August 2026 Nepal-Tibet flood event reaches 1,000 or more in official figures issued between 2026-09-07 and 2026-10-16.
- **Resolution criterion:** TRUE if a cumulative confirmed toll of 1,000 or more for this event, attributed to the National Disaster Risk Reduction and Management Authority of Nepal, the Nepali Ministry of Home Affairs, or Chinese state authorities, is carried by at least two of Reuters, AFP, Al Jazeera, and the Guardian, dated on or before 2026-10-16 and verifiable by 2026-10-19. Missing-persons counts do not count toward the total.
- **Failure condition:** The highest official cumulative confirmed death toll for this event as of 2026-10-16 remains below 1,000.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-71
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** CISA or the FBI publishes an advisory formally attributing the Fire Ant intrusion campaign against Cisco network devices to a China-linked actor, between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** Resolves true if CISA.gov or FBI.gov publishes an advisory naming a China-linked actor as responsible for the Fire Ant Cisco-targeting campaign within the window; false if no such advisory appears.
- **Failure condition:** Neither CISA nor the FBI publishes an advisory formally attributing the Fire Ant Cisco-router campaign to a China-linked actor between 2026-09-01 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260901-22
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury yield closes at or above 5.00 percent on any trading day between 2026-09-02 and 2026-10-15. Reference: 4.77 percent on the packet date, 2026-09-01.
- **Resolution criterion:** TRUE if the US 10-year Treasury constant maturity yield, per the Treasury daily par yield curve or the FRED DGS10 series, closes at or above 5.00 percent on any date in the window. FALSE otherwise.
- **Failure condition:** The 10-year Treasury yield never closes at or above 5.00 percent on any trading day in the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261026T000225ZZ - sha256 890511968396b7d9...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 31 business days in window; max BC_10YEAR 5.31 on 2026-10-05; threshold >= 5.00; 19 day(s) satisfying

### KKR-20260902-53
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one SonicWall vulnerability with a dateAdded value between 2026-09-03 and 2026-10-15.
- **Resolution criterion:** TRUE if the CISA KEV catalog JSON contains at least one entry with vendorProject SonicWall and dateAdded from 2026-09-03 through 2026-10-15 inclusive.
- **Failure condition:** The KEV catalog holds no SonicWall entry with a dateAdded inside that range when fetched at the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000226ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SonicWall'] with dateAdded in [2026-09-03..2026-10-15] across 1756 catalog rows

### KKR-20260902-56
- **Issued:** 2026-09-02  ·  **Deadline:** 2026-10-19
- **Domain:** disaster_infrastructure
- **Claim:** A UN OCHA or Nepal NDRRMA report published between 2026-09-03 and 2026-10-15 states a confirmed death toll of 1,500 or more from the 2026 Nepal-Tibet floods.
- **Resolution criterion:** TRUE if an OCHA situation report on ReliefWeb or an NDRRMA bulletin, published in that window, states 1,500 or more confirmed deaths from the 2026 Nepal flood event.
- **Failure condition:** Every OCHA or NDRRMA report published in that window states a confirmed toll below 1,500.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-07
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** The combined official confirmed death toll (excluding missing) from the Nepal-Tibet flood disaster reported from late August 2026 reaches at least 1,500 on any date between 2026-09-03 and 2026-10-15. Reference: reported passing 1,000 on 2026-09-01.
- **Resolution criterion:** TRUE if Nepal NDRRMA figures, or two of Reuters, AP, AFP citing officials, put the combined confirmed death toll (excluding missing) for the late-August 2026 Nepal-Tibet floods at 1,500 or more on any date from 2026-09-03 through 2026-10-15.
- **Failure condition:** Official confirmed death counts (excluding missing) for the disaster remain below 1,500 combined on every date through 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260903-28
- **Issued:** 2026-09-03  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** Leon Black either appears for a rescheduled House Oversight Committee deposition or is formally held in contempt of Congress in connection with the Epstein-probe subpoena, between 2026-09-05 and 2026-10-17.
- **Resolution criterion:** House Oversight Committee records or a wire-service report confirm either a completed Leon Black deposition or a committee contempt vote or referral occurring between 2026-09-05 and 2026-10-17, checked by 2026-10-19.
- **Failure condition:** Neither a completed Leon Black deposition nor a formal contempt vote or referral occurs in the 2026-09-05 to 2026-10-17 window as of 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-42
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** USGS catalogs an earthquake of magnitude 6.0 or greater within 300 km of event us7000tdvt with origin time between 2026-09-05 and 2026-10-15.
- **Resolution criterion:** TRUE if a USGS ComCat query returns an M6.0 or greater event within 300 km of the us7000tdvt epicenter with origin time in that window. Adjudicated 2026-10-19.
- **Failure condition:** No USGS-catalogued M6.0 or greater event occurs within 300 km of us7000tdvt inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-02
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** Russia and Ukraine, or their authorized representatives, publicly announce a signed ceasefire or peace agreement covering the active front line, following the 2026-09-05 arrival of US envoys Witkoff and Kushner in Moscow, at any point between 2026-09-06 and 2026-10-15.
- **Resolution criterion:** TRUE if at least two of Reuters, AP, BBC, or a joint Russian-Ukrainian government statement confirm a signed ceasefire between 2026-09-06 and 2026-10-15, confirmed as of 2026-10-19; FALSE otherwise.
- **Failure condition:** MISS if no signed ceasefire or peace agreement is confirmed by two of the named sources between 2026-09-06 and 2026-10-15, as checked on 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-17
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** Anthropic or another frontier AI developer discloses a new AI-orchestrated hacking incident, distinct from the Claude Opus 4.6 incident reported 2026-09-10, between 2026-09-17 and 2026-10-17.
- **Resolution criterion:** TRUE if a frontier AI developer's official disclosure, or two outlets among Reuters, Bloomberg, The Hacker News, and BleepingComputer, report a new incident in the window distinct from the 2026-09-10 one.
- **Failure condition:** No materially distinct new AI-orchestrated hacking incident is disclosed by a frontier AI developer within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260910-19
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** A court order or legislative action reinstates the 2025 Republican-redrawn congressional map for Missouri's November 2026 election, occurring between 2026-09-17 and 2026-10-15 (Reference: the US Supreme Court twice declined to reinstate that map, on 2026-09-08 and 2026-09-10).
- **Resolution criterion:** TRUE if the Missouri Secretary of State, or two wire services among AP and Reuters, confirm a reinstatement of the 2025 map for the November election within the window.
- **Failure condition:** No court order or legislative action reinstates the 2025 map within the window; the pre-2025 map remains in effect.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-26
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-19
- **Domain:** military/conflict
- **Claim:** Between 2026-09-15 and 2026-10-15 foreign ministers or higher-ranking officials of Iran and at least three Gulf Cooperation Council member states attend the same in-person meeting with Strait of Hormuz transit on its stated agenda, as reported by two of Reuters, AP, AFP, Al Jazeera.
- **Resolution criterion:** True if two of Reuters, AP, AFP, or Al Jazeera report an in-person meeting dated 2026-09-15 to 2026-10-15 of foreign ministers or above from Iran and three or more GCC states with Hormuz on the stated agenda. Otherwise false.
- **Failure condition:** Through 2026-10-15 no in-person meeting with Hormuz on its agenda brings together foreign ministers or higher from Iran and at least three GCC states.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-39
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** Microsoft ships a fix dated between 2026-09-15 and 2026-10-15 for the September 2026 update issue causing Remote Desktop Services failures on Windows Server, reflected as resolved on Windows release health.
- **Resolution criterion:** Microsoft Windows release health documentation lists the September Windows Server RDS failure issue as resolved by an update released between 2026-09-15 and 2026-10-15.
- **Failure condition:** The RDS issue lacks a resolved status tied to a fix released within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-38
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** military/conflict
- **Claim:** Between 2026-09-16 and 2026-10-15, at least one NATO member state formally requests consultations under Article 4 of the North Atlantic Treaty.
- **Resolution criterion:** TRUE if NATO or the requesting government publicly confirms a formal Article 4 consultation request made between 2026-09-16 and 2026-10-15; otherwise FALSE.
- **Failure condition:** No NATO member state makes a formal Article 4 consultation request between 2026-09-16 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-60
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** The Trump administration or DOJ files a petition for rehearing or a new emergency application with the Supreme Court on the mail ballot ruling from items 102, 103, and 124, between 2026-09-16 and 2026-10-15.
- **Resolution criterion:** TRUE if the Supreme Court docket shows a rehearing petition or new emergency application from the Trump administration or DOJ on this specific ruling, filed between 2026-09-16 and 2026-10-15, checked 2026-10-19.
- **Failure condition:** No rehearing petition or new emergency application on this ruling appears on the Supreme Court docket within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-61
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** The UK government publishes a new or expanded sanctions measure targeting Israeli individuals, entities, or settlement-linked goods, between 2026-09-16 and 2026-10-15.
- **Resolution criterion:** TRUE if gov.uk publishes a new Statutory Instrument or Foreign Office notice expanding sanctions on Israeli individuals, entities, or settlement goods, dated between 2026-09-16 and 2026-10-15, checked 2026-10-19.
- **Failure condition:** No new UK sanctions measure targeting Israel is published within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-70
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** Between 2026-09-16 and 2026-10-15 at least one merchant vessel is attacked, boarded, hijacked, or seized in the Strait of Hormuz, Gulf of Oman, or Persian Gulf, and UKMTO records the incident.
- **Resolution criterion:** The UKMTO incidents list (ukmto.org) shows an incident dated between 2026-09-16 and 2026-10-15 in the Strait of Hormuz, Gulf of Oman, or Persian Gulf classified as an attack, boarding, hijack, or seizure of a merchant vessel.
- **Failure condition:** No merchant vessel is attacked, boarded, hijacked, or seized in the Strait of Hormuz, Gulf of Oman, or Persian Gulf between 2026-09-16 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-73
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** Between 2026-09-16 and 2026-10-15 a round of talks between United States and Iranian government officials, direct or mediated, is held and publicly confirmed by both governments.
- **Resolution criterion:** At least two of Reuters, AP, AFP report that the United States government and the Iranian Foreign Ministry each confirmed a round of US-Iran talks, direct or mediated, held between 2026-09-16 and 2026-10-15.
- **Failure condition:** No round of US-Iran talks held between 2026-09-16 and 2026-10-15 is confirmed by both governments.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-76
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** Between 2026-09-16 and 2026-10-15 CISA adds to the Known Exploited Vulnerabilities catalog at least one entry with vendorProject Google and a product field containing Chrome or Chromium.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry with vendorProject Google, a product field containing Chrome or Chromium, and a dateAdded between 2026-09-16 and 2026-10-15 inclusive.
- **Failure condition:** No KEV entry with vendorProject Google and a Chrome or Chromium product carries a dateAdded between 2026-09-16 and 2026-10-15.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000227ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Google', 'Chrome', 'Chromium'] with dateAdded in [2026-09-16..2026-10-15] across 1756 catalog rows - CVE-2026-58704

### KKR-20260915-77
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-19
- **Domain:** crime_security
- **Claim:** Between 2026-09-16 and 2026-10-15 Dutch authorities announce the arrest of at least one suspect in connection with the suspected sabotage that disrupted Netherlands rail traffic on 2026-09-15.
- **Resolution criterion:** At least two of Reuters, AP, AFP, NOS report that the Netherlands Public Prosecution Service or Dutch police announced, between 2026-09-16 and 2026-10-15, the arrest of a suspect for the 2026-09-15 rail sabotage.
- **Failure condition:** No arrest of a suspect for the 2026-09-15 Netherlands rail sabotage is announced by Dutch authorities between 2026-09-16 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-23
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Between 2026-09-18 00:00 UTC and 2026-10-15 23:59 UTC, an earthquake of magnitude 5.5 or greater occurs with epicenter within 150 km of USGS event us7000ti1p (M6.5, Fox Islands, Alaska, 2026-09-17).
- **Resolution criterion:** TRUE if the USGS earthquake catalog lists at least one event of magnitude 5.5 or greater with epicenter within 150 km of USGS event us7000ti1p and origin time between 2026-09-18 00:00 UTC and 2026-10-15 23:59 UTC.
- **Failure condition:** No USGS-catalogued earthquake of magnitude 5.5 or greater with epicenter within 150 km of us7000ti1p has origin time between 2026-09-18 00:00 UTC and 2026-10-15 23:59 UTC.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000227ZZ - sha256 e4be6ade1f783bc4...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-09-18&endtime=2026-10-16&latitude=52.8796&longitude=-171.3965&maxradiuskm=150&minmagnitude=5.5
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20260917-55
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-19
- **Domain:** military/conflict
- **Claim:** Between 2026-09-17 and 2026-10-15, the United States and Iran announce a ceasefire, truce, or formal end to hostilities, confirmed by a government statement or by at least two of Reuters, AP, or AFP.
- **Resolution criterion:** TRUE if Reuters, AP, or AFP report a US-Iran ceasefire, truce, or hostilities-end announcement dated between 2026-09-17 and 2026-10-15; adjudicated 2026-10-19. FALSE otherwise.
- **Failure condition:** No US-Iran ceasefire, truce, or hostilities-end announcement dated within the window is confirmed by Reuters, AP, or AFP as of the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-61
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-19
- **Domain:** political
- **Claim:** Between 2026-09-17 and 2026-10-15, the Riksdag holds a formal vote confirming a new Swedish prime minister following Ulf Kristersson's resignation, recorded in the Riksdag's own vote record.
- **Resolution criterion:** TRUE if the Riksdag's vote record shows a confirmation vote for a new prime minister dated 2026-09-17 to 2026-10-15; adjudicated 2026-10-19. FALSE otherwise.
- **Failure condition:** The Riksdag's vote record shows no confirmation vote for a new prime minister by the deadline, or Sweden remains under a caretaker government.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-33
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** CISA will add at least one Linux Kernel entry to its Known Exploited Vulnerabilities catalog with dateAdded between 2026-09-26 and 2026-10-17.
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a Linux Kernel entry with dateAdded in 2026-09-26 to 2026-10-17, checked 2026-10-19; else FALSE.
- **Failure condition:** No Linux Kernel entry is added to the CISA KEV catalog with dateAdded between 2026-09-26 and 2026-10-17.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000227ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Linux Kernel'] with dateAdded in [2026-09-26..2026-10-19] across 1756 catalog rows

### KKR-20260919-37
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** The Polish Ministry of National Defence, its Operational Command, or NATO will confirm a Russian-origin drone or missile entered Polish airspace between 2026-09-26 and 2026-10-17.
- **Resolution criterion:** TRUE if Polish authorities or NATO officially confirm a Russian-origin airspace incursion dated 2026-09-26 to 2026-10-17, wire-reported by 2026-10-19; else FALSE.
- **Failure condition:** No official Polish or NATO confirmation of a Russian-origin airspace incursion is issued for 2026-09-26 to 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-29
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-19
- **Domain:** cyber
- **Claim:** CISA adds at least one new Citrix NetScaler ADC or Gateway CVE to the KEV catalog between 2026-09-28 and 2026-10-16.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed carries an entry with vendorProject Citrix, product naming NetScaler, a CVE other than CVE-2026-19490 or CVE-2026-19489, and dateAdded between 2026-09-28 and 2026-10-16.
- **Failure condition:** No Citrix NetScaler KEV entry other than CVE-2026-19490 and CVE-2026-19489 has a dateAdded value between 2026-09-28 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-49
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-10-19
- **Domain:** military_conflict
- **Claim:** Russia launches at least 500 drones and missiles combined against Ukraine in a single overnight attack, per the Ukrainian Air Force, on a date between 2026-10-01 and 2026-10-14.
- **Resolution criterion:** Reuters or AP reports, citing the Ukrainian Air Force, that Russia launched at least 500 drones and missiles combined in one overnight attack occurring between 2026-10-01 and 2026-10-14.
- **Failure condition:** No single overnight Russian attack on Ukraine between 2026-10-01 and 2026-10-14 involves 500 or more drones and missiles launched combined.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-20
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-19
- **Domain:** military/conflict
- **Claim:** Ukrainian forces strike at least one oil refinery on internationally recognized Russian territory between 2026-10-02 and 2026-10-15.
- **Resolution criterion:** Reuters, AP or the Kyiv Independent reports a Ukrainian strike on a named oil refinery on Russian territory occurring between 2026-10-02 and 2026-10-15, confirmed by the General Staff of Ukraine, the SBU or Russian officials.
- **Failure condition:** No Ukrainian strike hits an oil refinery on internationally recognized Russian territory between 2026-10-02 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-10
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Between 2026-10-09 and 2026-10-16, a major flood event will be reported in Bangkok, Thailand, with at least one official source confirming water levels exceeding 1.5 meters in central districts.
- **Resolution criterion:** At least one official source confirms water levels exceeding 1.5 meters in central districts of Bangkok, Thailand, due to flooding between 2026-10-09 and 2026-10-16.
- **Failure condition:** No official source confirms water levels exceeding 1.5 meters in central districts of Bangkok, Thailand, due to flooding between 2026-10-09 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-12
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Kenya confirms a second Ebola death between 2026-10-10 and 2026-10-17.
- **Resolution criterion:** The WHO or Kenya Ministry of Health confirms a second Ebola death in Kenya within the event window.
- **Failure condition:** No second Ebola death is confirmed in Kenya by the WHO or Kenya Ministry of Health within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-14
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-19
- **Domain:** economics
- **Claim:** Anduril Industries receives a final Navy contract award exceeding 2.9 billion USD for a submarine shipyard project between 2026-10-10 and 2026-10-17.
- **Resolution criterion:** The US Department of Defense publishes a contract award notice for Anduril Industries exceeding 2.9 billion USD for a submarine shipyard project.
- **Failure condition:** The US Department of Defense does not publish a contract award notice for Anduril Industries exceeding 2.9 billion USD for a submarine shipyard project.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-16
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** A significant earthquake (magnitude 6.0 or higher) occurs in Indonesia between 2026-10-10 and 2026-10-17.
- **Resolution criterion:** The USGS or EMSC reports a magnitude 6.0 or higher earthquake in Indonesia within the event window.
- **Failure condition:** No magnitude 6.0 or higher earthquake is reported in Indonesia by the USGS or EMSC within the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000228ZZ - sha256 8737df57ea0ba4da...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-10&endtime=2026-10-18&minlatitude=-11.0&maxlatitude=6.0&minlongitude=95.0&maxlongitude=141.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261007-07
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** On 2026-10-15, the 10-year U.S. Treasury yield exceeds 5.35 percent, based on the close of the U.S. Treasury auction on that date.
- **Resolution criterion:** The 10-year U.S. Treasury note yield, as reported by the U.S. Department of the Treasury at the close of the auction on 2026-10-15, is greater than 5.35 percent.
- **Failure condition:** The 10-year U.S. Treasury note yield at the close of the auction on 2026-10-15 is 5.35 percent or lower.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261026T000228ZZ - sha256 890511968396b7d9...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 8 business days in window; max BC_10YEAR 5.28 on 2026-10-07; threshold > 5.35; 0 day(s) satisfying

### KKR-20261007-31
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** A hurricane makes landfall in Louisiana, Mississippi, Alabama or Florida between 2026-10-08 and 2026-10-15.
- **Resolution criterion:** National Hurricane Center advisories or tropical cyclone updates report a landfall in Louisiana, Mississippi, Alabama or Florida between 2026-10-08 and 2026-10-15 with maximum sustained winds of at least 74 mph at landfall.
- **Failure condition:** No tropical cyclone makes landfall in Louisiana, Mississippi, Alabama or Florida with maximum sustained winds of at least 74 mph between 2026-10-08 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-13
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** On 2026-10-15, the Brent crude oil price will exceed $110 per barrel, based on the closing price from the ICE Futures Europe exchange.
- **Resolution criterion:** The Brent crude oil price, as reported by ICE Futures Europe on the settlement date, is greater than $110 per barrel.
- **Failure condition:** The Brent crude oil price on the settlement date is $110 per barrel or lower.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-21
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** The US Treasury 10-year yield closes above 5.50 percent on any US trading day between 2026-10-13 and 2026-10-16.
- **Resolution criterion:** The closing yield of the US Treasury 10-year note exceeds 5.50 percent on the specified dates.
- **Failure condition:** The US Treasury 10-year yield closes at or below 5.50 percent on every US trading day between 2026-10-13 and 2026-10-16.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261026T000228ZZ - sha256 890511968396b7d9...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 4 business days in window; max BC_10YEAR 5.21 on 2026-10-13; threshold > 5.50; 0 day(s) satisfying

### KKR-20261008-33
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Hurricane Isaias makes its first US Gulf Coast landfall between 2026-10-08 and 2026-10-15 with maximum sustained winds of at least 96 mph, Category 2 or stronger.
- **Resolution criterion:** A National Hurricane Center advisory or tropical cyclone update issued between 2026-10-08 and 2026-10-15 UTC reports Isaias maximum sustained winds of at least 96 mph at its first US Gulf Coast landfall.
- **Failure condition:** Isaias makes its first US Gulf Coast landfall with maximum sustained winds below 96 mph, or makes no US landfall between 2026-10-08 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-72
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-19
- **Domain:** disaster
- **Claim:** Hurricane Isaias makes at least one US landfall with maximum sustained winds of 96 mph (Category 2) or higher between 2026-10-08 and 2026-10-15.
- **Resolution criterion:** True if an NHC public advisory or tropical cyclone update issued between 2026-10-08 and 2026-10-15 reports the center of Isaias crossing the US coastline with maximum sustained winds of 96 mph or higher.
- **Failure condition:** Isaias did not cross the US coastline with maximum sustained winds of 96 mph or higher at any time between 2026-10-08 and 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-04
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** On 2026-10-17, the S&P 500 closes below 7,750 points for the first time since 2026-09-20, as confirmed by the Dow Jones Market Data feed.
- **Resolution criterion:** The Dow Jones Market Data feed confirms that the S&P 500 closed below 7,750 points on 2026-10-17, with the closing value recorded at or below 7,749.99.
- **Failure condition:** The S&P 500 closes at or above 7,750 points on 2026-10-17, as confirmed by the Dow Jones Market Data feed.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-30
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-19
- **Domain:** economics/markets
- **Claim:** The BLS release scheduled for 2026-10-14 shows the September 2026 CPI-U all-items 12-month change at or above 3.7 percent. Reference: 3.4 percent for August 2026, the latest reading on the packet date.
- **Resolution criterion:** TRUE if the BLS Consumer Price Index release of 2026-10-14 (FRED CPIAUCNS) shows September 2026 all-items CPI-U up 3.7 percent or more over 12 months, not seasonally adjusted. Reference: 3.4 percent for August 2026.
- **Failure condition:** The September 2026 CPI-U all-items 12-month change is 3.6 percent or lower, or BLS has not published the September figure by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-03
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-20
- **Domain:** disaster
- **Claim:** On or before 2026-10-20, a major earthquake of magnitude 7.0 or higher strikes Japan, resulting in over 1,000 fatalities.
- **Resolution criterion:** A magnitude 7.0 or higher earthquake occurs in Japan and results in at least 1,000 confirmed fatalities, as reported by USGS and BBC World.
- **Failure condition:** the condition stated in this entry's resolution basis — A magnitude 7.0 or higher earthquake occurs in Japan and results in at least 1,000 confirmed fatalities, as reported by USGS and BBC World — is not met on or before 2026-10-20; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260804-60
- **Issued:** 2026-08-04  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** The United States Senate confirms Todd Blanche as Attorney General in a recorded floor vote held between 2026-08-05 and 2026-10-16.
- **Resolution criterion:** TRUE if a Congress.gov Senate roll call vote dated between 2026-08-05 and 2026-10-16 records confirmation of the Blanche nomination to be Attorney General.
- **Failure condition:** No Senate roll call inside the window records Blanche confirmed as Attorney General.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260811-19
- **Issued:** 2026-08-11  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds at least one new Microsoft SharePoint Server CVE, with dateAdded between 2026-08-12 and 2026-10-16.
- **Resolution criterion:** TRUE if a KEV entry whose product field names SharePoint carries a dateAdded between 2026-08-12 and 2026-10-16 inclusive and was absent from the catalog on 2026-08-11.
- **Failure condition:** The KEV catalog gains no SharePoint entry with a dateAdded inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260818-19
- **Issued:** 2026-08-18  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** In the Disney and ABC First Amendment suit against the FCC, the FCC files a motion to dismiss or an answer between 2026-08-19 and 2026-10-15.
- **Resolution criterion:** The federal docket for the ABC or Disney suit against the FCC records a motion to dismiss or an answer filed by the FCC between 2026-08-19 and 2026-10-15.
- **Failure condition:** No FCC motion to dismiss or answer appears on that docket by 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260820-10
- **Issued:** 2026-08-20  ·  **Deadline:** 2026-10-20
- **Domain:** disaster
- **Claim:** The USGS ComCat catalog records an earthquake of magnitude 6.0 or greater with epicenter within 150 km of USGS event us6000tkt2 near Ende, Indonesia, with origin time between 2026-08-21 and 2026-10-16.
- **Resolution criterion:** A USGS ComCat query centered on event us6000tkt2 with a 150 km radius returns at least one magnitude 6.0 or greater event with origin time between 2026-08-21 and 2026-10-16 UTC.
- **Failure condition:** ComCat records no magnitude 6.0 or greater event inside that radius and origin-time window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-17
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** A named extortion group publicly claims the Boston Scientific intrusion by listing the company on a leak site between 2026-08-27 and 2026-10-15.
- **Resolution criterion:** At least two of BleepingComputer, Cybersecurity Dive, Reuters, and The Record report a named group listing Boston Scientific on an extortion leak site inside the window.
- **Failure condition:** No named extortion group lists Boston Scientific on a leak site on or before 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260829-49
- **Issued:** 2026-08-29  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds CVE-2026-82078 or CVE-2026-81578 with a date_added value between 2026-08-29 and 2026-10-16.
- **Resolution criterion:** TRUE if the CISA KEV catalog contains an entry for CVE-2026-82078 or CVE-2026-81578 carrying a dateAdded value between 2026-08-29 and 2026-10-16 inclusive.
- **Failure condition:** Neither PaperCut CVE carries a KEV dateAdded value inside that window when the catalog is fetched on 2026-10-20.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000229ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['CVE-2026-82078', 'CVE-2026-81578'] with dateAdded in [2026-08-29..2026-10-16] across 1756 catalog rows - CVE-2026-81578, CVE-2026-82078

### KKR-20260831-54
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-20
- **Domain:** military_conflict
- **Claim:** A US or Gulf state authority publicly reports a naval mine detected, struck, or cleared in the Strait of Hormuz or its approaches between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** CENTCOM, the US Navy, or a Gulf state navy states that a mine was found, struck, or cleared in the strait or its approaches within the window.
- **Failure condition:** No mine is found, struck, or cleared in the strait or its approaches during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-58
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-20
- **Domain:** disaster_infrastructure
- **Claim:** The Nepal disaster authority puts the confirmed death toll from the August 2026 Nepal-Tibet floods at 1500 or more, at some point between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** An NDRRMA situation report or Nepal government figure dated inside the window states 1500 or more confirmed flood deaths in Nepal.
- **Failure condition:** The official Nepal confirmed toll stays below 1500 through 2026-10-15.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260831-59
- **Issued:** 2026-08-31  ·  **Deadline:** 2026-10-20
- **Domain:** crime_security
- **Claim:** German authorities name a suspect, announce an arrest, or announce a warrant in the Leipzig drone attack between 2026-09-01 and 2026-10-15.
- **Resolution criterion:** The Generalbundesanwalt, the BKA, or Saxony police state that a suspect is named, arrested, or subject to a warrant in the Leipzig drone case within the window.
- **Failure condition:** No suspect is named, arrested, or made subject to an announced warrant in the case during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-34
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** The governments of Russia and Ukraine both announce a ceasefire or a mutual halt of long-range strikes with an effective date between 2026-09-05 and 2026-10-16.
- **Resolution criterion:** TRUE if Reuters and AP each carry statements from both the Kremlin and the Ukrainian presidential office confirming the same ceasefire or strike-halt agreement effective within the window.
- **Failure condition:** No agreement confirmed by both governments and carried by both wire services has an effective date between 2026-09-05 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260904-36
- **Issued:** 2026-09-04  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** Argentina publishes in the Boletin Oficial a decree or resolution imposing sanctions or restrictive economic measures aimed at the Falkland Islands, companies operating there, or UK entities over the islands, dated between 2026-09-05 and 2026-10-16.
- **Resolution criterion:** TRUE if the Boletin Oficial de la Republica Argentina carries such an instrument with publication date inside the window; verbal threats without a published instrument do not count.
- **Failure condition:** No qualifying decree or resolution appears in the Boletin Oficial with a publication date between 2026-09-05 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-82
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry for the Adobe Commerce or Magento vulnerability disclosed 2026-09-05, with a dateAdded value between 2026-09-07 and 2026-10-16.
- **Resolution criterion:** The public CISA KEV JSON feed contains an entry naming Adobe Commerce or Magento with dateAdded between 2026-09-07 and 2026-10-16 inclusive.
- **Failure condition:** No KEV entry naming Adobe Commerce or Magento carries a dateAdded value inside the 2026-09-07 to 2026-10-16 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-21
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Following the public ShieldCrash proof-of-concept, CISA adds at least one Microsoft Defender or Malware Protection Engine vulnerability to the Known Exploited Vulnerabilities catalog with a date-added between 2026-09-09 and 2026-10-16.
- **Resolution criterion:** The CISA KEV catalog JSON feed contains an entry with vendorProject Microsoft whose product or vulnerabilityName names Defender or Malware Protection Engine, with dateAdded between 2026-09-09 and 2026-10-16 inclusive.
- **Failure condition:** No KEV entry naming Microsoft Defender or Malware Protection Engine carries a dateAdded value between 2026-09-09 and 2026-10-16.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000229ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['Microsoft', 'Defender', 'Malware'] with dateAdded in [2026-09-09..2026-10-16] across 1756 catalog rows - CVE-2026-65660, CVE-2026-96951

### KKR-20260909-41
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** At least one Microsoft CVE from the scheduled October 2026 Patch Tuesday release of 2026-10-13 is added to the CISA KEV catalog with a dateAdded value between 2026-10-13 and 2026-10-16.
- **Resolution criterion:** TRUE if the public CISA KEV JSON shows a Microsoft-vendor CVE published 2026-10-13 with dateAdded between 2026-10-13 and 2026-10-16 inclusive; otherwise FALSE.
- **Failure condition:** The October release contains no CVE that CISA catalogs as exploited with a dateAdded value inside the stated span.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-15
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-20
- **Domain:** military_conflict
- **Claim:** The Royal Saudi Air Force conducts a direct airstrike on Houthi-held positions at Mocha, Dhubab, or Perim Island on the Red Sea coast of Yemen between 2026-09-18 and 2026-10-16.
- **Resolution criterion:** Two of Reuters, AP, AFP, or Al Jazeera report a Saudi strike specifically on Mocha, Dhubab, or Perim Island between 2026-09-18 and 2026-10-16; strikes elsewhere in Yemen do not qualify.
- **Failure condition:** No two of the named outlets report a Saudi strike specifically on Mocha, Dhubab, or Perim Island within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-18
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** CISA adds a Cisco Secure Firewall Management Center vulnerability to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-18 and 2026-10-16.
- **Resolution criterion:** The CISA KEV catalog JSON feed lists a Cisco Secure Firewall Management Center CVE with dateAdded between 2026-09-18 and 2026-10-16.
- **Failure condition:** No Cisco Secure Firewall Management Center CVE appears in the CISA KEV catalog with dateAdded inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000230ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Cisco Firewall'] with dateAdded in [2026-09-18..2026-10-16] across 1756 catalog rows

### KKR-20260911-33
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** CISA adds CVE-2026-85706 (GitLab repository commits API path traversal) to the Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-09-12 and 2026-10-16.
- **Resolution criterion:** TRUE if the CISA KEV catalog JSON contains an entry for CVE-2026-85706 whose dateAdded is between 2026-09-12 and 2026-10-16 inclusive; otherwise FALSE.
- **Failure condition:** CVE-2026-85706 is absent from the CISA KEV catalog at the deadline, or carries a dateAdded outside 2026-09-12 to 2026-10-16.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000231ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['CVE-2026-85706'] with dateAdded in [2026-09-12..2026-10-16] across 1756 catalog rows

### KKR-20260911-43
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** WTI crude front-month futures record at least one daily settlement price at or above 110.00 USD per barrel on NYMEX between 2026-09-14 and 2026-10-16. Reference: 99.63 USD on the packet date.
- **Resolution criterion:** CME Group official daily settlement data for front-month WTI crude shows any settlement at or above 110.00 USD between 2026-09-14 and 2026-10-16 inclusive; otherwise MISS.
- **Failure condition:** Every front-month WTI daily settlement inside the window is below 110.00 USD.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-14
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** economic
- **Claim:** WTI crude front-month futures settle at or above 110.00 USD per barrel on any trading day between 2026-09-19 and 2026-10-17. Reference: 100.05 USD per barrel on 2026-09-12, the packet date
- **Resolution criterion:** TRUE if any NYMEX WTI front-month settlement or EIA daily spot price in the window is 110.00 USD per barrel or higher; FALSE otherwise
- **Failure condition:** No WTI settlement or EIA spot print in the window reaches 110.00 USD per barrel
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-15
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** CISA adds at least one Check Point-vendor CVE to the Known Exploited Vulnerabilities catalog with a date-added value between 2026-09-19 and 2026-10-17
- **Resolution criterion:** TRUE if the CISA KEV catalog lists a Check Point-vendor CVE with dateAdded in the window; FALSE otherwise
- **Failure condition:** The CISA KEV catalog contains no Check Point-vendor entry dated in the window
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000231ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 2 matching entries for ['Check Point'] with dateAdded in [2026-09-19..2026-10-17] across 1756 catalog rows - CVE-2026-85102, CVE-2026-93616

### KKR-20260912-16
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** OpenAI, Google DeepMind, or Meta issues an official statement or a named spokesperson is quoted by a major outlet addressing Dario Amodei's proposal to slow AI development, between 2026-09-19 and 2026-10-17
- **Resolution criterion:** TRUE if Reuters, AP, Bloomberg, CNBC, Guardian, or BBC quotes an official OpenAI, Google DeepMind, or Meta statement addressing the proposal in the window; FALSE otherwise
- **Failure condition:** None of OpenAI, Google DeepMind, or Meta formally addresses the proposal within the window
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-17
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** Ireland's Taoiseach or the Department of Foreign Affairs issues an on-record statement addressing Donald Trump's 12 September 2026 unified-Ireland remarks, between 2026-09-19 and 2026-10-17
- **Resolution criterion:** TRUE if RTE, Irish Times, or a wire service reports an on-record statement from the Taoiseach's office or Department of Foreign Affairs addressing the remarks in the window; FALSE otherwise
- **Failure condition:** Irish officials issue no on-record statement addressing the remarks within the window
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-18
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** crime_security
- **Claim:** Spanish or Catalan authorities confirm 5 or more arrests connected to the 12 September 2026 Barcelona Catalan national day clashes, in a statement or report between 2026-09-19 and 2026-10-17
- **Resolution criterion:** TRUE if a Spanish government, Catalan regional police, or wire-service report in the window states 5 or more arrests tied to the incident; FALSE otherwise
- **Failure condition:** Fewer than 5 arrests tied to the incident are confirmed within the window
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260912-55
- **Issued:** 2026-09-12  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** Saudi Aramco or the Saudi energy ministry announces resumption of flows on the pipeline shut after the 2026-09-12 drone attack, with the announcement falling between 2026-09-14 and 2026-10-16.
- **Resolution criterion:** TRUE if Reuters and at least one of BBC or Al Jazeera report an official Saudi announcement of resumed flows on that pipeline dated 2026-09-14 through 2026-10-16.
- **Failure condition:** Flows on that pipeline are not officially announced as resumed at any point inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-10
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-20
- **Domain:** economics_markets
- **Claim:** WTI crude oil, reference 100.05 dollars per barrel at the prior-session close reported in the 2026-09-13 packet, will settle at or above 112.00 dollars per barrel on any NYMEX trading day between 2026-09-21 and 2026-10-19.
- **Resolution criterion:** The NYMEX front-month WTI settlement price, reference 100.05 dollars per barrel on the 2026-09-13 packet date, is 112.00 dollars per barrel or higher on at least one trading day between 2026-09-21 and 2026-10-19.
- **Failure condition:** NYMEX front-month WTI settlement never reaches 112.00 dollars per barrel on any trading day in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-29
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Between 2026-09-14 and 2026-10-16, CISA adds a Tencent vulnerability (including Sogou Input Method, CVE-2026-51990) to the Known Exploited Vulnerabilities catalog.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed carries an entry whose vendorProject is Tencent or whose product includes Sogou, with dateAdded between 2026-09-14 and 2026-10-16; FALSE otherwise.
- **Failure condition:** The CISA KEV catalog carries no Tencent or Sogou entry with dateAdded between 2026-09-14 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260913-52
- **Issued:** 2026-09-13  ·  **Deadline:** 2026-10-20
- **Domain:** disaster
- **Claim:** Indonesian authorities state a death toll of 50 or more from the Java Sea passenger ship that capsized on 2026-09-13, with the statement issued between 2026-09-14 and 2026-10-14.
- **Resolution criterion:** TRUE if Basarnas or another Indonesian government body states a confirmed or recovered toll of at least 50 dead for this vessel, corroborated by two independent wire services.
- **Failure condition:** The official death toll for this vessel stands below 50 throughout the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-35
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** The FRED DGS10 10-year US Treasury constant maturity yield prints 5.00 percent or higher on at least one business day between 2026-09-15 and 2026-10-16. Reference: 4.99 percent at packet seal.
- **Resolution criterion:** FRED series DGS10 shows a daily value of 5.00 or higher for at least one business day between 2026-09-15 and 2026-10-16 inclusive. Reference: 4.99 at packet seal.
- **Failure condition:** Every DGS10 daily value from 2026-09-15 through 2026-10-16 is below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-53
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-20
- **Domain:** military_conflict
- **Claim:** Commercial traffic through the Strait of Hormuz is halted for more than 24 consecutive hours at some point between 2026-09-15 and 2026-10-15.
- **Resolution criterion:** TRUE if Reuters or Lloyds List Intelligence and Iranian state media both report a halt of commercial Hormuz transits exceeding 24 consecutive hours occurring between 2026-09-15 and 2026-10-15.
- **Failure condition:** MISS if no continuous halt of commercial Hormuz transits exceeding 24 hours occurs inside the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260914-58
- **Issued:** 2026-09-14  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Microsoft resolves the September 2026 Windows Server RDS connection failure with a shipped update between 2026-09-15 and 2026-10-16.
- **Resolution criterion:** TRUE if the Windows release health entry for the September 2026 RDS failure shows status Resolved by an out-of-band update, Known Issue Rollback, or cumulative update dated between 2026-09-15 and 2026-10-16.
- **Failure condition:** MISS if the RDS regression is not fixed by a shipped Microsoft update inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-20
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one Google Chrome or Chromium CVE with dateAdded between 2026-09-16 and 2026-10-16.
- **Resolution criterion:** True if the public CISA KEV JSON contains an entry whose vendor or product field names Google Chrome or Chromium with dateAdded between 2026-09-16 and 2026-10-16 inclusive.
- **Failure condition:** No Chrome or Chromium entry in the KEV catalog carries a dateAdded within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-44
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-20
- **Domain:** crime/security
- **Claim:** Between 2026-09-16 and 2026-10-16, Dutch police or prosecutors announce at least one arrest in connection with the suspected sabotage that disrupted Netherlands rail services, reported on 2026-09-15.
- **Resolution criterion:** TRUE if Dutch police (politie.nl) or the Public Prosecution Service (om.nl) announce an arrest, made between 2026-09-16 and 2026-10-16, linked to the rail sabotage reported on 2026-09-15; otherwise FALSE.
- **Failure condition:** No person is arrested in connection with the Netherlands rail sabotage reported on 2026-09-15 between 2026-09-16 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-75
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-20
- **Domain:** economic
- **Claim:** The 10-year Treasury constant maturity yield (FRED series DGS10) prints 5.00 percent or higher on at least one observation dated 2026-09-16 through 2026-10-16. Reference: 4.99 percent on the packet date.
- **Resolution criterion:** FRED series DGS10 shows at least one observation dated 2026-09-16 through 2026-10-16 with a value of 5.00 or greater. Reference: 4.99 percent on the packet date.
- **Failure condition:** Every DGS10 observation dated 2026-09-16 through 2026-10-16 is below 5.00 percent.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-30
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one entry for an Acronis product with a dateAdded value between 2026-09-17 and 2026-10-16.
- **Resolution criterion:** True if the CISA KEV JSON feed contains at least one entry whose vendorProject or product field contains Acronis, case-insensitive, with dateAdded between 2026-09-17 and 2026-10-16 inclusive.
- **Failure condition:** On 2026-10-20 the KEV feed holds no Acronis entry with a dateAdded value inside 2026-09-17 to 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-48
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** Russia and Ukraine complete at least one exchange of prisoners of war, announced by both governments, between 2026-09-17 and 2026-10-16.
- **Resolution criterion:** TRUE if both the Russian Defence Ministry and the Ukrainian government (the President or the POW Coordination Headquarters) announce a completed prisoner-of-war exchange that took place between 2026-09-17 and 2026-10-16.
- **Failure condition:** No exchange of prisoners of war between Russia and Ukraine was completed between 2026-09-17 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-16
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** Between 2026-09-18 and 2026-10-16, India or Pakistan officially acknowledges at least one of its own uniformed personnel killed by fire from the forces of the other country.
- **Resolution criterion:** TRUE if, between 2026-09-18 and 2026-10-16, the Indian Ministry of Defence, Indian Army, Pakistan ISPR, or Pakistan Navy officially acknowledges at least one of its own uniformed personnel killed by fire from the forces of the other country.
- **Failure condition:** Neither government acknowledges a death of its own uniformed personnel caused by fire from the forces of the other country between 2026-09-18 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-21
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Between 2026-09-18 and 2026-10-16, Microsoft releases a fix and marks the Windows 11 domain trust and domain login issue introduced by update KB5124008 as Resolved.
- **Resolution criterion:** TRUE if Microsoft Windows release health or the KB5124008 support article shows the domain trust or domain login known issue with status Resolved and a resolution date between 2026-09-18 and 2026-10-16, on the live page or an archive.org capture.
- **Failure condition:** The KB5124008 domain trust or domain login issue carries no Resolved status with a resolution date between 2026-09-18 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-16
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The critical Check Point root code-execution flaw reported 18 Sep 2026 is added to the CISA KEV catalog with a date-added value between 2026-09-18 and 2026-10-16.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed lists a Check Point entry with dateAdded between 2026-09-18 and 2026-10-16 inclusive matching the flaw in item 12; FALSE otherwise.
- **Failure condition:** No Check Point entry appears in the CISA KEV feed with a dateAdded value between 2026-09-18 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-17
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** A Russian presidential decree placing Nestle Russian assets under temporary state management is published on the official legal portal publication.pravo.gov.ru between 2026-09-18 and 2026-10-16.
- **Resolution criterion:** TRUE if publication.pravo.gov.ru or kremlin.ru carries a decree dated 2026-09-18 to 2026-10-16 inclusive naming Nestle entities for temporary management or asset transfer; FALSE otherwise.
- **Failure condition:** No decree naming Nestle Russian assets for temporary management is published on the official portals in the 2026-09-18 to 2026-10-16 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-18
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** The Philippine Coast Guard publicly reports a new collision, ramming, or water-cannon incident involving a Chinese government vessel in the South China Sea between 2026-09-19 and 2026-10-16.
- **Resolution criterion:** TRUE if an official Philippine Coast Guard statement describes such an incident occurring 2026-09-19 to 2026-10-16 inclusive and at least one wire service (Reuters, AP, or AFP) reports it; FALSE otherwise.
- **Failure condition:** No Philippine Coast Guard statement describes a new collision, ramming, or water-cannon incident with a Chinese vessel dated within 2026-09-19 to 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-19
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** UKMTO or JMIC issues an incident advisory for an attack on a merchant vessel in the Red Sea, Bab al-Mandeb, or Gulf of Aden occurring between 2026-09-19 and 2026-10-16.
- **Resolution criterion:** TRUE if the UKMTO or JMIC public advisory feed records a projectile, drone, or boarding attack on a merchant vessel in those waters dated 2026-09-19 to 2026-10-16 inclusive; FALSE otherwise.
- **Failure condition:** The UKMTO and JMIC advisory feeds record no attack on a merchant vessel in the Red Sea, Bab al-Mandeb, or Gulf of Aden dated within 2026-09-19 to 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-46
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** The United States military conducts a direct kinetic strike (missile, air, or naval gunfire) against Houthi forces or positions at or near the Bab el-Mandeb strait between 2026-09-25 and 2026-10-16.
- **Resolution criterion:** TRUE if Reuters, AP, or BBC report a confirmed US strike on Houthi targets at or near Bab el-Mandeb in the stated window; checked 2026-10-20 using wire-service and CENTCOM reporting.
- **Failure condition:** No US strike on Houthi forces or positions at or near Bab el-Mandeb is reported by Reuters, AP, or BBC between 2026-09-25 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-47
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** WTI crude oil (NYMEX front-month futures) settles at or above 100.00 USD per barrel on any trading day between 2026-09-21 and 2026-10-16. Reference: 96.92 on the packet date, 2026-09-18.
- **Resolution criterion:** TRUE if CME/NYMEX front-month WTI settlement data show a close at or above 100.00 USD/bbl on any session between 2026-09-21 and 2026-10-16; checked 2026-10-20 against exchange records.
- **Failure condition:** WTI NYMEX front-month settlement stays below 100.00 USD/bbl on every trading day from 2026-09-21 through 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260918-48
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** The Nasdaq index closes at or above 27717.70, five percent above the packet reference, on any trading day between 2026-09-21 and 2026-10-16. Reference: 26397.81 on the packet date, 2026-09-18.
- **Resolution criterion:** TRUE if Nasdaq closing data show a close at or above 27717.70 on any session between 2026-09-21 and 2026-10-16; checked 2026-10-20 against exchange or major financial-data-provider records.
- **Failure condition:** Nasdaq closes below 27717.70 on every trading day from 2026-09-21 through 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-12
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds the SolarWinds ARM hard-coded key vulnerability disclosed 2026-09-19, with a date-added value between 2026-09-19 and 2026-10-16.
- **Resolution criterion:** The CISA KEV JSON feed contains an entry with vendorProject SolarWinds and product Access Rights Manager or ARM whose dateAdded falls between 2026-09-19 and 2026-10-16 inclusive.
- **Failure condition:** The KEV feed carries no SolarWinds Access Rights Manager entry with dateAdded inside the 2026-09-19 to 2026-10-16 window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-14
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** The Federal Register publishes an executive order or OFAC notice terminating or removing Eritrea-related sanctions with a publication date between 2026-09-19 and 2026-10-16.
- **Resolution criterion:** federalregister.gov shows a document whose title or abstract names Eritrea and terminates, revokes or removes sanctions authorities or designations, with publication_date between 2026-09-19 and 2026-10-16 inclusive.
- **Failure condition:** No Federal Register document published 2026-09-19 through 2026-10-16 terminates or removes Eritrea-related sanctions.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-16
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** The NYMEX WTI front-month contract settles below 90.00 dollars on at least one trading day between 2026-09-21 and 2026-10-16. Reference: 96.08 on the packet date after a 9.21 percent one-day fall.
- **Resolution criterion:** True if the CME Group official settlement for front-month WTI is below 90.00 on any trading day 2026-09-21 to 2026-10-16.
- **Failure condition:** Every front-month WTI settlement in the window is at or above 90.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-40
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** NYMEX front-month WTI crude settles below 85.00 USD per barrel on at least one trading day between 2026-09-22 and 2026-10-16. Reference: 92.25 on the packet date.
- **Resolution criterion:** CME NYMEX official daily settlement for the front-month CL contract prints below 85.00 on any trading day 2026-09-22 through 2026-10-16.
- **Failure condition:** Every front-month WTI settlement from 2026-09-22 through 2026-10-16 is 85.00 or higher.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260925-42
- **Issued:** 2026-09-25  ·  **Deadline:** 2026-10-20
- **Domain:** military_conflict
- **Claim:** At least two independent outlets will report a specific clash, casualty event, or territorial change involving Ethiopian federal forces and Tigrayan (TPLF-aligned) forces occurring between 2026-10-02 and 2026-10-16.
- **Resolution criterion:** Two independent outlets (e.g. Reuters, AP, BBC, Al Jazeera, Addis Standard) report a specific clash, casualty event, or territorial change involving Ethiopian federal and Tigrayan forces, dated within 2026-10-02 to 2026-10-16.
- **Failure condition:** No two independent outlets report a specific Tigray-region clash, casualty event, or territorial change involving Ethiopian federal and Tigrayan forces occurring within 2026-10-02 to 2026-10-16; general tension or blockade-fear reporting alone does not satisfy this.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-01
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** Between 2026-10-10 and 2026-10-17, at least one drone strike using a Shahed-type UAV will be reported by two or more independently biased sources in the Odesa region of Ukraine.
- **Resolution criterion:** At least one drone strike using a Shahed-type UAV in the Odesa region will be reported by two or more sources from distinct hostile sides (RU, UA, WEST) with no overlap in channel ownership.
- **Failure condition:** No such drone strike is reported by two or more independently biased sources in the Odesa region during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-11
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** CISA issues an Emergency Directive naming Citrix NetScaler ADC or NetScaler Gateway, with an issue date between 2026-09-27 and 2026-10-16.
- **Resolution criterion:** TRUE if the CISA directives page lists an Emergency Directive (any ED number) naming NetScaler ADC or NetScaler Gateway, dated between 2026-09-27 and 2026-10-16. Binding Operational Directives, alerts, and KEV additions do not count.
- **Failure condition:** No CISA Emergency Directive naming Citrix NetScaler is issued with a date between 2026-09-27 and 2026-10-16; alerts, advisories, or KEV additions alone do not satisfy.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-43
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Microsoft will document a resumed rollout or a replacement fix for the KB5002907 Office license-deactivation issue between 2026-09-28 and 2026-10-18.
- **Resolution criterion:** True if Microsoft's Release Health dashboard or a support.microsoft.com KB article confirms KB5002907, or its direct successor patch, is fixed and redistributed inside the window; false otherwise.
- **Failure condition:** Microsoft has not documented a fix or resumed rollout for the KB5002907 issue by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-08
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Between 2026-10-10 and 2026-10-17, at least one confirmed cyberattack exploiting CVE-2026-88771 or CVE-2026-88772 will be reported by two independent sources with hostile bias.
- **Resolution criterion:** At least one confirmed cyberattack exploiting CVE-2026-88771 or CVE-2026-88772 is reported by two independent sources with hostile bias between 2026-10-10 and 2026-10-17.
- **Failure condition:** No cyberattack exploiting CVE-2026-88771 or CVE-2026-88772 is reported by two independent sources with hostile bias during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-45
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** Between 2026-09-29 and 2026-10-16, the Australian Greens party room elects a new federal parliamentary leader to replace Larissa Waters, who announced on 2026-09-28 that she is stepping down.
- **Resolution criterion:** The Greens or two of ABC, Guardian Australia, and AAP report a party room vote choosing a new federal leader between 2026-09-29 and 2026-10-16; acting or interim appointments do not count.
- **Failure condition:** No new federal leader of the Australian Greens has been chosen by party room vote between 2026-09-29 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-09
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** Between 2026-10-08 and 2026-10-15, the UK diesel price exceeds £2.10 per litre, as reported by the Guardian World and BBC World.
- **Resolution criterion:** The Guardian World and BBC World report the UK diesel price exceeding £2.10 per litre on a weekday between 2026-10-08 and 2026-10-15.
- **Failure condition:** The UK diesel price does not exceed £2.10 per litre on any weekday between 2026-10-08 and 2026-10-15 according to the two sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-11
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** Between 2026-10-10 and 2026-10-17, a political scandal involving a U.S. federal official will be reported by at least two major wire services (e.g., Reuters, AP, Bloomberg) with a public resignation or indictment by the deadline.
- **Resolution criterion:** At least two major wire services report a political scandal involving a U.S. federal official with a public resignation or indictment by 2026-10-17.
- **Failure condition:** No political scandal involving a U.S. federal official is reported by at least two major wire services with a public resignation or indictment by 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-18
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** A Russian strike hits a Kyiv bridge over the Dnipro other than the Pivdennyi (Southern) and Pivnichnyi (Northern) bridges between 2026-10-04 and 2026-10-17.
- **Resolution criterion:** True if at least two of BBC, Reuters, AP and Kyiv Independent report a Russian drone or missile strike damaging a third Kyiv Dnipro bridge on a date between 2026-10-04 and 2026-10-17.
- **Failure condition:** No Kyiv crossing of the Dnipro other than the Pivdennyi and Pivnichnyi bridges is struck by Russian fire between 2026-10-04 and 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-27
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** Between 2026-10-04 and 2026-10-17, a Russian drone or missile strike damages at least one Kyiv Dnipro road bridge other than Pivdennyi and Pivnichnyi, namely the Paton, Metro, Darnytskyi or Podilskyi bridge.
- **Resolution criterion:** TRUE if Reuters, AP or BBC, citing Kyiv city authorities, report a Russian strike damaging the Paton, Metro, Darnytskyi or Podilskyi bridge between 2026-10-04 and 2026-10-17; otherwise FALSE.
- **Failure condition:** None of the Paton, Metro, Darnytskyi or Podilskyi bridges in Kyiv is damaged by a Russian strike between 2026-10-04 and 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-41
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-20
- **Domain:** military_conflict
- **Claim:** Between 2026-10-05 and 2026-10-18, Russian drone or missile strikes hit or damage a Dnipro River bridge in Kyiv on at least three separate calendar dates.
- **Resolution criterion:** Kyiv Mayor Klitschko or the Kyiv City Military Administration, or two of Reuters, AP and BBC, report strikes hitting a Kyiv Dnipro bridge on three or more separate dates between 2026-10-05 and 2026-10-18.
- **Failure condition:** Fewer than three separate calendar dates between 2026-10-05 and 2026-10-18 have a Russian drone or missile strike hitting a Dnipro River bridge in Kyiv.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-05
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-20
- **Domain:** cyber
- **Claim:** Between 2026-10-12 and 2026-10-18, a confirmed cyberattack will compromise the Danish population registry, resulting in the exposure of personal data for at least 8.8 million individuals.
- **Resolution criterion:** At least one report from two or more hostile sides (DEN, WEST) confirms a cyberattack on the Danish population registry between 2026-10-12 and 2026-10-18, with exposure of personal data affecting at least 8.8 million individuals.
- **Failure condition:** No report from two or more hostile sides confirms a cyberattack on the Danish population registry between 2026-10-12 and 2026-10-18, or the number of affected individuals is less than 8.8 million.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-12
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** On 2026-10-17, the UK government will announce a new sanctions regime targeting Russian energy exports, with the policy published in the UK Government's official register.
- **Resolution criterion:** The UK Government's official register (https://www.legislation.gov.uk) contains a new sanctions order targeting Russian energy exports, published on or before 2026-10-17.
- **Failure condition:** No such sanctions order is published in the UK Government's official register by 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-52
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-20
- **Domain:** disaster
- **Claim:** Between 2026-10-08 and 2026-10-16, Hurricane Isaias will make landfall along the US Gulf Coast from Louisiana through Apalachee Bay, Florida, with sustained winds of 74 mph or more.
- **Resolution criterion:** Between 2026-10-08 and 2026-10-16, National Hurricane Center advisories state the center of Isaias made landfall along the US Gulf Coast from Louisiana through Apalachee Bay, Florida, with sustained winds of 74 mph or more.
- **Failure condition:** As of the deadline, the center of Isaias had not made landfall along the US Gulf Coast from Louisiana through Apalachee Bay, Florida, with sustained winds of 74 mph or more between 2026-10-08 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-26
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-20
- **Domain:** disaster
- **Claim:** Hurricane Isaias makes landfall on the US Gulf Coast between 2026-10-09 and 2026-10-16 with a National Hurricane Center landfall intensity of at least 111 mph maximum sustained winds (Category 3 or stronger).
- **Resolution criterion:** True if the NHC advisory archive for Isaias (Tropical Cyclone Update or public advisory) gives maximum sustained winds of 111 mph or more at a US Gulf Coast landfall between 2026-10-09 and 2026-10-16; otherwise false.
- **Failure condition:** Isaias reaches the US Gulf Coast with landfall winds below 111 mph, or makes no US Gulf Coast landfall between 2026-10-09 and 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-18
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-20
- **Domain:** economics/markets
- **Claim:** WTI Crude futures settle above 95.00 USD per barrel on at least one trading day between 2026-10-13 and 2026-10-16.
- **Resolution criterion:** A settlement price for WTI Crude futures exceeding 95.00 USD per barrel on a weekday in the window.
- **Failure condition:** WTI Crude futures settle at or below 95.00 USD per barrel on all trading days in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-01
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-20
- **Domain:** military/conflict
- **Claim:** On 2026-10-12, a missile strike confirmed by at least two hostile sides (RU, UA) occurred in Kyiv, resulting in at least one casualty and damage to a civilian infrastructure site.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-12 and 2026-10-18, and the event is corroborated by at least two independent sources from hostile sides (RU, UA) reporting a missile strike in Kyiv with at least one casualty and confirmed infrastructure damage.
- **Failure condition:** No corroborated report from at least two hostile sides (RU, UA) confirms a missile strike in Kyiv on or between 2026-10-12 and 2026-10-18, or no casualty or infrastructure damage is confirmed by any source.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-09
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-20
- **Domain:** political
- **Claim:** On 2026-10-17, the U.S. Department of State will issue a formal statement condemning Iran for threatening to disrupt maritime traffic in the Strait of Hormuz, citing a prior intelligence assessment.
- **Resolution criterion:** The U.S. Department of State will issue a formal statement on or before 2026-10-17 condemning Iran for threatening to disrupt maritime traffic in the Strait of Hormuz, referencing a prior intelligence assessment, as confirmed by a transcript on the State Department website.
- **Failure condition:** The U.S. Department of State does not issue a formal statement on or before 2026-10-17 condemning Iran for threatening to disrupt maritime traffic in the Strait of Hormuz, referencing a prior intelligence assessment.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-41
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** A complaint challenging the lawfulness of the Section 338 tariffs on Canadian goods is filed in a US federal court between 2026-08-24 and 2026-10-16.
- **Resolution criterion:** A US Court of International Trade or federal district court docket shows a complaint filed in that window seeking to invalidate or enjoin the Section 338 duties on Canadian imports.
- **Failure condition:** No complaint attacking the Section 338 Canadian tariffs appears on a federal docket with a filing date inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260822-45
- **Issued:** 2026-08-22  ·  **Deadline:** 2026-10-21
- **Domain:** crime_security
- **Claim:** A jury returns a guilty verdict on the murder count against Duane Davis in the Clark County, Nevada prosecution over the 1996 killing of Tupac Shakur, between 2026-08-24 and 2026-10-16.
- **Resolution criterion:** The Clark County District Court docket records a jury verdict of guilty on the murder count, entered inside that window.
- **Failure condition:** The jury acquits, hangs, a mistrial is declared, or no verdict is entered before the window closes.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260827-79
- **Issued:** 2026-08-27  ·  **Deadline:** 2026-10-21
- **Domain:** cyber
- **Claim:** Boston Scientific files a Form 8-K Item 1.05 material cybersecurity incident disclosure with the SEC regarding the cyberattack disclosed 2026-08-26, between 2026-09-03 and 2026-10-17.
- **Resolution criterion:** SEC EDGAR shows a Boston Scientific Form 8-K containing Item 1.05 filed within the window, checked by 2026-10-21.
- **Failure condition:** No Boston Scientific Form 8-K containing Item 1.05 appears on EDGAR within the window; disclosure only through press release, a different 8-K item number, or routine risk-factor language in a periodic report all count as a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-91
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-21
- **Domain:** military_conflict
- **Claim:** US and Iranian forces exchange at least one further direct kinetic strike on a vessel or maritime target in the Persian Gulf, Gulf of Oman, or Strait of Hormuz, occurring between 2026-09-07 and 2026-10-16.
- **Resolution criterion:** TRUE if a strike in that window is reported by at least two of Reuters, AP, AFP, and BBC, and is acknowledged by either US Central Command or Iranian state media.
- **Failure condition:** No US or Iranian strike on a maritime target in those waters occurs inside the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260909-23
- **Issued:** 2026-09-09  ·  **Deadline:** 2026-10-21
- **Domain:** economics/markets
- **Claim:** Brent crude spot reaches 110.00 dollars per barrel or higher on at least one trading day between 2026-09-10 and 2026-10-09. Reference: Brent 101.13 on the packet date.
- **Resolution criterion:** FRED series DCOILBRENTEU (EIA Europe Brent spot price FOB) records a daily value at or above 110.00 for at least one date between 2026-09-10 and 2026-10-09 inclusive.
- **Failure condition:** Every DCOILBRENTEU daily value dated 2026-09-10 through 2026-10-09 is below 110.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260911-34
- **Issued:** 2026-09-11  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** The DRC Ministry of Health, WHO, or ECDC reports a cumulative total of at least 10,000 confirmed Bundibugyo Ebola cases in the DRC for a data date on or before 2026-10-16. Reference: 6,942 confirmed cases as of 2026-09-09 on the packet date.
- **Resolution criterion:** TRUE if a DRC Ministry of Health, WHO, or ECDC report states DRC cumulative confirmed Bundibugyo Ebola cases of 10,000 or more with data through a date no later than 2026-10-16; otherwise FALSE.
- **Failure condition:** DRC cumulative confirmed Bundibugyo Ebola cases remain below 10,000 for every data date on or before 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-18
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** Saudi official channels acknowledge at least one Houthi-attributed drone or missile impact or interception over Saudi territory occurring between 2026-09-17 and 2026-10-17.
- **Resolution criterion:** Saudi Press Agency, the Saudi defense ministry, or Saudi civil defense acknowledges an impact or interception dated 2026-09-17 through 2026-10-17, and Reuters, AP, or AFP carries the acknowledgment by the deadline.
- **Failure condition:** By the deadline no Saudi official acknowledgment carried by Reuters, AP, or AFP covers any Houthi-attributed impact or interception over Saudi territory dated in the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-35
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-21
- **Domain:** economics/markets
- **Claim:** The FRED series DCOILWTICO (WTI spot, Cushing) observation dated 2026-10-16 is at or above 110.00 USD per barrel. Reference: WTI 101.87 on the packet date.
- **Resolution criterion:** True if the FRED DCOILWTICO observation dated 2026-10-16 is 110.00 or higher; if no observation exists for that date, use the next posted trading-day observation.
- **Failure condition:** The DCOILWTICO observation dated 2026-10-16, or the next posted trading day, is below 110.00.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-41
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** A formal ceasefire or truce between the United States and Iran, confirmed by matching statements from the US State Department or White House and the Iranian Foreign Ministry, is announced between 2026-09-21 and 2026-10-19.
- **Resolution criterion:** Official US and Iranian government channels each issue a statement describing a ceasefire, truce, or armistice ending hostilities between 2026-09-21 and 2026-10-19, corroborated by a wire service.
- **Failure condition:** No matching US and Iranian government statement announcing a ceasefire, truce, or armistice appears between 2026-09-21 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260920-44
- **Issued:** 2026-09-20  ·  **Deadline:** 2026-10-21
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds an entry, with dateAdded between 2026-09-21 and 2026-10-19, for a vulnerability in the class of AI coding-agent sandbox escapes or malicious npm package supply-chain compromise, matching the techniques reported 20 September 2026.
- **Resolution criterion:** The CISA KEV catalog lists a CVE with dateAdded between 2026-09-21 and 2026-10-19 whose description matches sandbox-escape or npm supply-chain compromise techniques.
- **Failure condition:** No CISA KEV entry with dateAdded between 2026-09-21 and 2026-10-19 matches sandbox-escape or npm supply-chain compromise techniques.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-05
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** Between 2026-10-12 and 2026-10-19, the White House will issue a formal statement rejecting Iran's proposal to reopen the Strait of Hormuz within seven days.
- **Resolution criterion:** A formal statement issued by the White House on or before 2026-10-19 will explicitly reject Iran's seven-day peace proposal to reopen the Strait of Hormuz.
- **Failure condition:** No such formal White House statement rejecting the proposal is issued during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261001-48
- **Issued:** 2026-10-01  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** A Ukrainian drone or missile strike damages an oil refinery in Russia or Russian-occupied territory on a date between 2026-10-05 and 2026-10-18.
- **Resolution criterion:** Reuters or AP reports that a Ukrainian drone or missile strike damaged an oil refinery in Russia or Russian-occupied territory on a date between 2026-10-05 and 2026-10-18, citing Ukrainian or Russian officials.
- **Failure condition:** No oil refinery in Russia or Russian-occupied territory is damaged by a Ukrainian drone or missile strike between 2026-10-05 and 2026-10-18.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-37
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** Between 2026-10-05 and 2026-10-18, Russia will launch at least 500 drones and missiles combined against Ukraine in a single overnight attack, as tallied by the Ukrainian Air Force.
- **Resolution criterion:** A Ukrainian Air Force tally of Russian drones plus missiles launched in one overnight attack, dated between 2026-10-05 and 2026-10-18, is at least 500, reported by at least two of Reuters, AP, Kyiv Independent.
- **Failure condition:** Every Russian overnight aerial attack on Ukraine between 2026-10-05 and 2026-10-18 involves fewer than 500 drones and missiles combined.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261004-52
- **Issued:** 2026-10-04  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** Between 2026-10-05 and 2026-10-18, at least one bridge within the city limits of Kyiv is struck by a Russian drone or missile, following the Kyiv bridge strikes reported on 2026-10-04.
- **Resolution criterion:** Ukrainian authorities (Kyiv city military administration, mayor, or Infrastructure Ministry) report a Russian drone or missile strike on a Kyiv bridge dated between 2026-10-05 and 2026-10-18, carried by Reuters or AP.
- **Failure condition:** No bridge within the city limits of Kyiv is struck by a Russian drone or missile on any date between 2026-10-05 and 2026-10-18.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-11
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** GDACS issues a Yellow or Red alert for a tropical cyclone affecting a populated area between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** The GDACS alert database records a Yellow or Red alert for a tropical cyclone affecting a populated area between 2026-10-12 and 2026-10-19.
- **Failure condition:** The GDACS alert database does not record a Yellow or Red alert for a tropical cyclone affecting a populated area between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-12
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** A confirmed case of pneumonic plague is reported in Russia between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** A public health authority (e.g., WHO, Russian Ministry of Health) or a major wire service confirms a case of pneumonic plague in Russia between 2026-10-12 and 2026-10-19.
- **Failure condition:** No public health authority or major wire service confirms a case of pneumonic plague in Russia between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-13
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** crime/security
- **Claim:** A US federal court issues an indictment against the alleged developer of Ploutus ATM malware between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** A US federal court issues an indictment against the alleged developer of Ploutus ATM malware on any date between 2026-10-12 and 2026-10-19.
- **Failure condition:** A US federal court does not issue an indictment against the alleged developer of Ploutus ATM malware on any date between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-14
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** The US Supreme Court hears oral arguments in the case involving big oil's bid to block climate damage lawsuits between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** The US Supreme Court hears oral arguments in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19.
- **Failure condition:** The US Supreme Court does not hear oral arguments in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-15
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** A forest fire notification is issued by GDACS for Brazil between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** A forest fire notification is issued by GDACS for Brazil on any date between 2026-10-12 and 2026-10-19.
- **Failure condition:** A forest fire notification is not issued by GDACS for Brazil on any date between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-16
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** The US Supreme Court issues a ruling in the case involving big oil's bid to block climate damage lawsuits between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** The US Supreme Court issues a ruling in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19.
- **Failure condition:** The US Supreme Court does not issue a ruling in the case involving big oil's bid to block climate damage lawsuits on any date between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-17
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** A flood alert is issued by GDACS for France between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** A flood alert is issued by GDACS for France on any date between 2026-10-12 and 2026-10-19.
- **Failure condition:** A flood alert is not issued by GDACS for France on any date between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-08
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-21
- **Domain:** cyber
- **Claim:** On 2026-10-18, a cyberattack exploiting the Atlassian Jira and Confluence file-access flaw (CVE-2026-XXXX) is confirmed by at least two independent sources, including one from a government cybersecurity agency and one from a private security firm.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-18, and at least one report from a government cybersecurity agency and one from a private security firm independently confirm a cyberattack exploiting the Atlassian Jira and Confluence file-access flaw (CVE-2026-XXXX) during that window.
- **Failure condition:** No report from a government cybersecurity agency or a private security firm independently confirms a cyberattack exploiting the Atlassian Jira and Confluence file-access flaw (CVE-2026-XXXX) between 2026-10-15 and 2026-10-18.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000232ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Atlassian Jira', 'Confluence'] with dateAdded in [2026-10-15..2026-10-18] across 1756 catalog rows

### KKR-20261011-15
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-21
- **Domain:** military/conflict
- **Claim:** A Houthi missile or drone strike hits a target inside Saudi Arabia between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** Two wire services report a kinetic strike by Houthi forces on Saudi territory within the window.
- **Failure condition:** No Houthi kinetic strikes on Saudi territory are reported through the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-16
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** A magnitude 7.0 or greater earthquake occurs in Panama between 2026-10-12 and 2026-10-19.
- **Resolution criterion:** The USGS catalog carries a date-added value for an event with magnitude 7.0 or higher in Panama.
- **Failure condition:** No magnitude 7.0 or greater earthquakes are recorded in Panama through the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-46
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-21
- **Domain:** disaster
- **Claim:** Hurricane Simon makes landfall on the Mexican coast with sustained winds of at least 74 mph between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** US National Hurricane Center advisories or best-track data record the center of Simon crossing the Mexican coast with maximum sustained winds of at least 74 mph between 2026-10-11 and 2026-10-18.
- **Failure condition:** Simon does not cross the Mexican coast with sustained winds of at least 74 mph between 2026-10-11 and 2026-10-18, either weakening first or staying offshore.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-47
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** Pope Leo XIV undergoes surgery on his lung between 2026-10-12 and 2026-10-18.
- **Resolution criterion:** The Holy See Press Office or Vatican News confirms that Pope Leo XIV underwent lung surgery dated between 2026-10-12 and 2026-10-18 inclusive.
- **Failure condition:** Pope Leo XIV undergoes no lung surgery between 2026-10-12 and 2026-10-18 because it is postponed or cancelled.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-48
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-21
- **Domain:** political
- **Claim:** Between 2026-10-11 and 2026-10-18, both the Kremlin and the Ukrainian presidential office publicly say their side has agreed to or will observe a halt on strikes on energy infrastructure.
- **Resolution criterion:** Reuters or AP reports statements dated 2026-10-11 to 2026-10-18 in which both a Kremlin official and Zelensky or his office say their side agreed to or will observe a halt on strikes on energy infrastructure.
- **Failure condition:** At least one of the Kremlin and the Ukrainian presidential office denies or does not affirm, between 2026-10-11 and 2026-10-18, that its side agreed to or will observe a halt on strikes on energy infrastructure.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260729-10
- **Issued:** 2026-07-29  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** Between 2026-10-15 and 2026-10-22, a major wildfire in California burns over 100,000 acres and causes at least 20 fatalities.
- **Resolution criterion:** A wildfire in California burns over 100,000 acres and causes at least 20 fatalities between 2026-10-15 and 2026-10-22, as confirmed by Cal Fire or BBC World.
- **Failure condition:** the condition stated in this entry's resolution basis — A wildfire in California burns over 100,000 acres and causes at least 20 fatalities between 2026-10-15 and 2026-10-22, as confirmed by Cal Fire or BBC World — is not met on or before 2026-10-22; absence at the deadline scores this entry a MISS.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-24
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-22
- **Domain:** military_conflict
- **Claim:** Yemeni government or Saudi-led coalition forces announce the capture of a named district in Houthi-held Hodeidah, al-Jawf, or Saada governorate, between 2026-09-08 and 2026-10-19.
- **Resolution criterion:** TRUE if a government or coalition claim of capturing a named district in those three governorates in the window is corroborated by Houthi-aligned media or by Reuters, AFP, or AP.
- **Failure condition:** No named district in those three governorates changes hands by announced capture during the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260907-16
- **Issued:** 2026-09-07  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** Following the report of a Telerik UI padding-oracle bug chained to unauthenticated remote code execution, the CISA Known Exploited Vulnerabilities catalog will add a Telerik UI entry between 2026-09-14 and 2026-10-19.
- **Resolution criterion:** TRUE if the CISA KEV catalog carries a dateAdded value for a Telerik UI CVE falling within the window; else FALSE.
- **Failure condition:** No Telerik UI CVE is added to the CISA KEV catalog with a dateAdded value inside the window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000232ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Telerik UI'] with dateAdded in [2026-09-14..2026-10-19] across 1756 catalog rows

### KKR-20260910-61
- **Issued:** 2026-09-10  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** CISA adds at least one Microsoft vulnerability to the Known Exploited Vulnerabilities catalog between 2026-10-13, October Patch Tuesday, and 2026-10-20.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed lists at least one entry with vendorProject Microsoft and a dateAdded value between 2026-10-13 and 2026-10-20 inclusive. FALSE otherwise.
- **Failure condition:** No KEV entry with vendorProject Microsoft carries a dateAdded value between 2026-10-13 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260915-41
- **Issued:** 2026-09-15  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** The CISA Known Exploited Vulnerabilities catalog adds at least one Microsoft Windows vulnerability with a dateAdded value between 2026-10-13 and 2026-10-19, the week of the October 2026 Patch Tuesday.
- **Resolution criterion:** TRUE if the CISA KEV JSON feed lists at least one entry with vendorProject Microsoft, a product field containing Windows or Win32k, and dateAdded between 2026-10-13 and 2026-10-19; otherwise FALSE.
- **Failure condition:** CISA adds no Microsoft Windows or Win32k vulnerability to the KEV catalog with a dateAdded value between 2026-10-13 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-67
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-22
- **Domain:** economics/markets
- **Claim:** WTI crude oil (NYMEX front-month futures) will record a settlement price at or above 110.00 USD per barrel on at least one trading day between 2026-09-23 and 2026-10-21. Reference: 101.87 USD per barrel on the packet date, 2026-09-16.
- **Resolution criterion:** TRUE if the NYMEX WTI front-month futures settlement price (as published by CME Group or the US Energy Information Administration) equals or exceeds 110.00 USD per barrel on any trading day from 2026-09-23 through 2026-10-21 inclusive; FALSE otherwise.
- **Failure condition:** The NYMEX WTI front-month settlement price stays below 110.00 USD per barrel on every trading day from 2026-09-23 through 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260916-68
- **Issued:** 2026-09-16  ·  **Deadline:** 2026-10-22
- **Domain:** economics/markets
- **Claim:** The US 10-year Treasury note yield will close at or above 5.10 percent on at least one trading day between 2026-09-23 and 2026-10-21. Reference: 4.96 percent on the packet date, 2026-09-16.
- **Resolution criterion:** TRUE if the US Treasury Daily Par Yield Curve Rates (treasury.gov) or a major financial data provider (Bloomberg, Reuters) shows the 10-year Treasury yield closing at or above 5.10 percent on any trading day from 2026-09-23 through 2026-10-21 inclusive; FALSE otherwise.
- **Failure condition:** The 10-year Treasury yield closes below 5.10 percent on every trading day from 2026-09-23 through 2026-10-21.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261026T000233ZZ - sha256 890511968396b7d9...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 20 business days in window; max BC_10YEAR 5.31 on 2026-10-05; threshold >= 5.10; 19 day(s) satisfying

### KKR-20260918-20
- **Issued:** 2026-09-18  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** The US government files a notice of appeal against the district court ruling blocking demolition of the Kennedy Center, docketed between 2026-09-18 and 2026-10-19.
- **Resolution criterion:** TRUE if the relevant federal district court docket on PACER or CourtListener shows a notice of appeal by the federal defendants entered 2026-09-18 to 2026-10-19 inclusive; FALSE otherwise.
- **Failure condition:** No notice of appeal by the federal defendants appears on the docket with an entry date between 2026-09-18 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260919-15
- **Issued:** 2026-09-19  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** Cuba suffers another full collapse of its national electrical grid between 2026-09-20 and 2026-10-20, publicly acknowledged by the Union Electrica or the Ministry of Energy and Mines.
- **Resolution criterion:** Union Electrica or Cuba's Ministry of Energy and Mines acknowledges a total disconnection of the Sistema Electroenergetico Nacional occurring between 2026-09-20 and 2026-10-20 inclusive, corroborated by at least two of Reuters, AP, AFP and EFE.
- **Failure condition:** No Cuban official acknowledgment of a total national grid disconnection dated inside the 2026-09-20 to 2026-10-20 window exists, or no two wire services corroborate one.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260922-13
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds an entry for a Microsoft Defender or Windows Defender vulnerability with a date-added value between 2026-09-22 and 2026-10-20.
- **Resolution criterion:** True if the CISA KEV catalog contains an entry whose product field references Microsoft Defender or Windows Defender and whose dateAdded is between 2026-09-22 and 2026-10-20 inclusive.
- **Failure condition:** No KEV entry referencing Microsoft Defender or Windows Defender carries a dateAdded between 2026-09-22 and 2026-10-20.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000234ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Microsoft Defender', 'Windows Defender'] with dateAdded in [2026-09-22..2026-10-20] across 1756 catalog rows

### KKR-20260922-14
- **Issued:** 2026-09-22  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** Between 2026-09-22 and 2026-10-20, at least two of Reuters, AP, AFP, and BBC report that Houthi forces have taken control of the Kahboub Mountains in Yemen.
- **Resolution criterion:** True if at least two of Reuters, AP, AFP, BBC publish reports dated 2026-09-22 to 2026-10-20 stating Houthi forces control the Kahboub Mountains or Kahboub heights.
- **Failure condition:** Fewer than two of the named outlets report Houthi control of the Kahboub Mountains within the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260926-11
- **Issued:** 2026-09-26  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** Between 2026-09-27 and 2026-10-19 the Israeli Supreme Court reverses the Central Elections Committee disqualifications of both the Joint List (Hadash, Taal, Balad) and the United Arab List (Raam), clearing both to run in the 2026-10-27 Knesset election.
- **Resolution criterion:** Supreme Court rulings dated between 2026-09-27 and 2026-10-19 overturn the CEC disqualification of both the Joint List and the United Arab List, and both appear on the official candidate lists for 2026-10-27; either still barred is false.
- **Failure condition:** At least one of the Joint List or the United Arab List remains disqualified from the 2026-10-27 election as of 2026-10-19, or no reversal is issued in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-40
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** Between 2026-09-29 and 2026-10-20, the CISA Known Exploited Vulnerabilities catalog adds at least one further Citrix NetScaler vulnerability, beyond the two Citrix NetScaler entries added on 2026-09-27.
- **Resolution criterion:** CISA KEV JSON contains an entry with vendorProject Citrix, product referencing NetScaler, dateAdded between 2026-09-29 and 2026-10-20 inclusive, and a cveID different from the two Citrix entries dated 2026-09-27.
- **Failure condition:** On 2026-10-22 the CISA KEV catalog holds no Citrix NetScaler entry, other than the two dated 2026-09-27, with dateAdded between 2026-09-29 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260930-01
- **Issued:** 2026-09-30  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** Between 2026-10-10 and 2026-10-17, at least one report from a hostile side in the Iran Theatre will corroborate a missile launch from Tehran toward the Strait of Hormuz.
- **Resolution criterion:** At least one report from a hostile side in the Iran Theatre corroborates a missile launch from Tehran toward the Strait of Hormuz between 2026-10-10 and 2026-10-17.
- **Failure condition:** No report from a hostile side in the Iran Theatre corroborates a missile launch from Tehran toward the Strait of Hormuz between 2026-10-10 and 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-10
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** Between 2026-10-10 and 2026-10-17, a cyberattack using autonomous AI agents targets a U.S. federal government website, confirmed by BleepingComputer and The Hacker News.
- **Resolution criterion:** BleepingComputer and The Hacker News report a cyberattack using autonomous AI agents targeting a U.S. federal government website between 2026-10-10 and 2026-10-17.
- **Failure condition:** No such attack is reported by either BleepingComputer or The Hacker News during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261003-12
- **Issued:** 2026-10-03  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** Between 2026-10-12 and 2026-10-19, a military escalation in the Israel-Gaza-Levant Theatre will result in a confirmed airstrike on Gaza City with casualties reported by at least two hostile sides.
- **Resolution criterion:** A confirmed airstrike on Gaza City in the Israel-Gaza-Levant Theatre with casualties reported by at least two hostile sides occurs between 2026-10-12 and 2026-10-19.
- **Failure condition:** No confirmed airstrike on Gaza City in the Israel-Gaza-Levant Theatre with casualties reported by at least two hostile sides occurs between 2026-10-12 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-43
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** CISA adds at least one Atlassian product vulnerability to its Known Exploited Vulnerabilities catalog with a dateAdded value between 2026-10-07 and 2026-10-20.
- **Resolution criterion:** The CISA KEV catalog JSON contains at least one entry with vendorProject Atlassian and a dateAdded value between 2026-10-07 and 2026-10-20 inclusive.
- **Failure condition:** CISA designates no Atlassian vulnerability as known exploited with a dateAdded value between 2026-10-07 and 2026-10-20 inclusive.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000234ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 1 matching entry for ['Atlassian'] with dateAdded in [2026-10-07..2026-10-20] across 1756 catalog rows - CVE-2026-21589

### KKR-20261007-44
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** Donald Trump and Vladimir Putin hold a direct phone call or in-person meeting between 2026-10-07 and 2026-10-20.
- **Resolution criterion:** A White House or Kremlin official readout, or reports by at least two of Reuters, AP, and BBC, confirm a direct Trump-Putin call or meeting held between 2026-10-07 and 2026-10-20.
- **Failure condition:** No direct phone call or in-person meeting between Trump and Putin takes place between 2026-10-07 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-03
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** Between 2026-10-12 and 2026-10-18, a Russian glide bomb attack on Zaporizhzhia will result in at least 15 confirmed fatalities.
- **Resolution criterion:** At least 15 confirmed fatalities are reported in the aftermath of a Russian glide bomb attack on Zaporizhzhia between 2026-10-12 and 2026-10-18.
- **Failure condition:** Fewer than 15 confirmed fatalities are reported in the aftermath of a Russian glide bomb attack on Zaporizhzhia between 2026-10-12 and 2026-10-18.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-17
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** The CISA KEV catalog carries a date-added value between 2026-10-11 and 2026-10-18 for a vulnerability exploited in the wild to deploy webshells or mine crypto.
- **Resolution criterion:** A new entry in the CISA KEV catalog with a date-added value in the window and description matching webshell deployment or crypto mining.
- **Failure condition:** No such entry appears in the CISA KEV catalog by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-19
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** military/conflict
- **Claim:** A Russian glide bomb or missile strike hits a populated area in Ukraine causing at least 10 fatalities between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** Two wire services report a Russian strike on a populated area in Ukraine with 10 or more fatalities in the window.
- **Failure condition:** No such strike with 10 or more fatalities is reported by two wire services in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-20
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** India detains at least 500 individuals in New Delhi during protests between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** Two wire services report the detention of at least 500 individuals in New Delhi during protests in the window.
- **Failure condition:** Detentions in New Delhi during protests in the window are reported as fewer than 500 individuals by two wire services.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-21
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** A magnitude 7.0 or greater earthquake occurs in Panama between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** The USGS catalog carries a date-added value in the window for a magnitude 7.0 or greater earthquake in Panama.
- **Failure condition:** No magnitude 7.0 or greater earthquake in Panama appears in the USGS catalog in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-22
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** A tropical storm or hurricane makes landfall in the United States between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** The NWS or NOAA issues a landfall warning or report for a tropical storm or hurricane in the United States in the window.
- **Failure condition:** No tropical storm or hurricane makes landfall in the United States as reported by the NWS or NOAA in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-23
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** A major cyberattack disrupts the power grid of a NATO member state between 2026-10-11 and 2026-10-18.
- **Resolution criterion:** Two wire services report a major cyberattack disrupting the power grid of a NATO member state in the window.
- **Failure condition:** No major cyberattack disrupting the power grid of a NATO member state is reported by two wire services in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-02
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** Between 2026-10-14 and 2026-10-20, a cyberattack exploiting a vulnerability in the Nippon Columbia karaoke database results in the exfiltration of at least 8 million user records, as confirmed by a third-party security audit.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-14 and 2026-10-20, and a third-party security audit confirms that at least 8 million user records were exfiltrated from the Nippon Columbia database due to a known vulnerability.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-10-14 and 2026-10-20, or no third-party audit confirms the exfiltration of at least 8 million user records.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000235ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['Nippon Columbia'] with dateAdded in [2026-10-14..2026-10-20] across 1756 catalog rows

### KKR-20261011-14
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** economics/markets
- **Claim:** The S&P 500 index closes below 7,500 on at least one trading day between 2026-10-16 and 2026-10-20.
- **Resolution criterion:** A market close recorded below 7,500. Reference: 7,811.54 on the packet date.
- **Failure condition:** The S&P 500 remains above 7,500 on all trading days through the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-19
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** military_conflict
- **Claim:** Houthi forces launch a kinetic strike on Riyadh airport between 2026-10-12 and 2026-10-19
- **Resolution criterion:** Al Jazeera or BBC World reports a confirmed Houthi strike on Riyadh airport within the window
- **Failure condition:** No Al Jazeera or BBC World report confirms a Houthi strike on Riyadh airport between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-20
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** A magnitude 6.0 or greater earthquake occurs in Panama between 2026-10-12 and 2026-10-19
- **Resolution criterion:** USGS Significant Quakes reports a magnitude 6.0 or greater earthquake in Panama between 2026-10-12 and 2026-10-19
- **Failure condition:** USGS Significant Quakes reports no magnitude 6.0 or greater earthquakes in Panama between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-21
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** Pope Leo XIV undergoes lung surgery between 2026-10-12 and 2026-10-19
- **Resolution criterion:** NPR News or BBC World reports that Pope Leo XIV has undergone lung surgery between 2026-10-12 and 2026-10-19
- **Failure condition:** NPR News and BBC World do not report that Pope Leo XIV has undergone lung surgery between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-22
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** Polish police confirm a plot to assassinate Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19
- **Resolution criterion:** Al Jazeera or Guardian World reports that Polish police have confirmed a plot to assassinate Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19
- **Failure condition:** Al Jazeera and Guardian World do not report that Polish police have confirmed a plot to assassinate Prime Minister Donald Tusk between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-23
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** A migrant boat capsizes off Djibouti with at least 100 dead between 2026-10-12 and 2026-10-19
- **Resolution criterion:** Al Jazeera or BBC World reports a migrant boat capsizing off Djibouti with at least 100 dead between 2026-10-12 and 2026-10-19
- **Failure condition:** Al Jazeera and BBC World do not report a migrant boat capsizing off Djibouti with at least 100 dead between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-24
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-22
- **Domain:** cyber
- **Claim:** Nippon Columbia malware incident exposes at least 8 million records between 2026-10-12 and 2026-10-19
- **Resolution criterion:** BleepingComputer reports that the Nippon Columbia malware incident has exposed at least 8 million records between 2026-10-12 and 2026-10-19
- **Failure condition:** BleepingComputer does not report that the Nippon Columbia malware incident has exposed at least 8 million records between 2026-10-12 and 2026-10-19
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-10
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** On 2026-10-19, the U.S. Federal Aviation Administration will issue a new safety advisory for flights over Saudi Arabia, citing increased risk from Houthi attacks, as published in the FAA's official advisory database.
- **Resolution criterion:** The FAA's official advisory database will publish a new safety advisory for flights over Saudi Arabia on or before 2026-10-19, citing increased risk from Houthi attacks, as confirmed by the FAA's official website.
- **Failure condition:** The FAA does not publish a new safety advisory for flights over Saudi Arabia on or before 2026-10-19 citing increased risk from Houthi attacks.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-09
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-22
- **Domain:** political
- **Claim:** Kimberly Guilfoyle resigns as US Ambassador to Greece between 2026-10-13 and 2026-10-20
- **Resolution criterion:** Kimberly Guilfoyle submits her resignation as US Ambassador to Greece between 2026-10-13 and 2026-10-20
- **Failure condition:** Kimberly Guilfoyle does not submit her resignation as US Ambassador to Greece between 2026-10-13 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-11
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-22
- **Domain:** disaster
- **Claim:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2026-10-13 and 2026-10-20
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama between 2026-10-13 and 2026-10-20
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 6.0 or greater earthquake in Panama between 2026-10-13 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-12
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-22
- **Domain:** military
- **Claim:** Yemeni government forces advance into or capture Taiz between 2026-10-13 and 2026-10-20
- **Resolution criterion:** Yemeni government forces advance into or capture Taiz between 2026-10-13 and 2026-10-20
- **Failure condition:** Yemeni government forces do not advance into or capture Taiz between 2026-10-13 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-16
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-22
- **Domain:** economics/markets
- **Claim:** Six Flags stock closes below 10.00 on at least one trading day between 2026-10-14 and 2026-10-21.
- **Resolution criterion:** Six Flags stock closes below 10.00 on at least one trading day between 2026-10-14 and 2026-10-21.
- **Failure condition:** Six Flags stock does not close below 10.00 on any trading day between 2026-10-14 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261014-05
- **Issued:** 2026-10-14  ·  **Deadline:** 2026-10-22
- **Domain:** economics/markets
- **Claim:** On 2026-10-20, the 10-year U.S. Treasury yield exceeds 5.3% at the close of trading, as reported by FRED.
- **Resolution criterion:** The 10-year U.S. Treasury yield exceeds 5.3% at the close of trading on 2026-10-20, as reported by FRED.
- **Failure condition:** The 10-year U.S. Treasury yield is at or below 5.3% at the close of trading on 2026-10-20.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - treasury10y - fetched 20261026T000235ZZ - sha256 890511968396b7d9...
  - instrument: https://home.treasury.gov/resource-center/data-chart-center/interest-rates/pages/xml?data=daily_treasury_yield_curve&field_tdr_date_value=2026
  - observed: 7 business days in window; max BC_10YEAR 5.19 on 2026-10-14; threshold > 5.30; 0 day(s) satisfying

### KKR-20260901-09
- **Issued:** 2026-09-01  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** Between 2026-08-31 and 2026-10-16, Manchester Airports Group or a UK government body publicly confirms unauthorized access to MAG systems in connection with the FulcrumSec claim.
- **Resolution criterion:** TRUE if at least two of BBC, Reuters, BleepingComputer, or The Record report an official MAG, NCSC, or ICO statement confirming unauthorized access to MAG systems, dated between 2026-08-31 and 2026-10-16.
- **Failure condition:** The confirmation condition is not met: no official statement confirming unauthorized access, dated inside the window, exists under the stated corroboration standard at the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260906-27
- **Issued:** 2026-09-06  ·  **Deadline:** 2026-10-23
- **Domain:** disaster_infrastructure
- **Claim:** The USGS earthquake catalog records at least two events of magnitude 7.0 or greater worldwide between 2026-09-08 and 2026-10-19.
- **Resolution criterion:** TRUE if a USGS ComCat query bounded by 2026-09-08 and 2026-10-19 returns two or more events of magnitude 7.0 or greater.
- **Failure condition:** The USGS catalog shows fewer than two magnitude 7.0 or greater events in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260917-40
- **Issued:** 2026-09-17  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** The Russia sanctions and secondary-tariff bill named for the late Senator Lindsey Graham, which cleared the House 262-159 on 2026-09-16, becomes public law between 2026-09-17 and 2026-10-16.
- **Resolution criterion:** Congress.gov shows the bill passed by the House 262-159 on 2026-09-16 with a Signed by President or Became Public Law action dated between 2026-09-17 and 2026-10-16.
- **Failure condition:** The bill is vetoed or has not been enacted by the end of 2026-10-16.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-16
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** US forces carry out at least one strike on a target located on Iranian land territory between 2026-09-22 and 2026-10-21.
- **Resolution criterion:** TRUE if CENTCOM or the Pentagon announces, or two of Reuters, AP and AFP report, a US strike on a target on Iranian soil conducted between 2026-09-22 and 2026-10-21. Strikes on vessels at sea do not count.
- **Failure condition:** No US strike hits a target on Iranian land territory between 2026-09-22 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260921-46
- **Issued:** 2026-09-21  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** USGS records at least one earthquake of magnitude 7.0 or greater anywhere on Earth between 2026-09-22 and 2026-10-21.
- **Resolution criterion:** The USGS earthquake catalog lists an event with reviewed magnitude 7.0 or greater and origin time 2026-09-22 through 2026-10-21 UTC.
- **Failure condition:** No USGS event in the window has a reviewed magnitude of 7.0 or greater.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260929-46
- **Issued:** 2026-09-29  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** Between 2026-10-06 and 2026-10-20, US forces strike at least one target on Iranian land territory or on an Iranian island, as publicly confirmed by US Central Command or the US Department of Defense.
- **Resolution criterion:** US Central Command or the US Department of Defense publicly confirms US strikes on targets in Iran, on land or on Iranian islands and not solely on vessels at sea, dated 2026-10-06 through 2026-10-20.
- **Failure condition:** No US strike hits a target on Iranian land or on an Iranian island from 2026-10-06 through 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-11
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** Between 2026-10-11 and 2026-10-18, France's parliament passes a new housing decree, as confirmed by Al Jazeera and BBC World.
- **Resolution criterion:** Al Jazeera and BBC World report that France's parliament passes a new housing decree between 2026-10-11 and 2026-10-18.
- **Failure condition:** No such housing decree is passed and confirmed by both Al Jazeera and BBC World during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261005-46
- **Issued:** 2026-10-05  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** Russian federal or Irkutsk regional health authorities, or WHO, officially confirm plague infection in at least one human case in Irkutsk Oblast between 2026-10-06 and 2026-10-19.
- **Resolution criterion:** Rospotrebnadzor, the Russian health ministry, the Irkutsk regional government, or WHO publishes a statement dated between 2026-10-06 and 2026-10-19 naming laboratory-confirmed plague in a human case in Irkutsk Oblast.
- **Failure condition:** Plague is not officially confirmed in any human case in Irkutsk Oblast between 2026-10-06 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-44
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** Between 2026-10-07 and 2026-10-21, at least one commercial vessel is struck by a drone, missile or other projectile in the Strait of Hormuz or the Gulf of Oman.
- **Resolution criterion:** UKMTO, US Central Command, or two of Reuters, AP and AFP report a commercial vessel struck by a drone, missile or projectile in the Strait of Hormuz or Gulf of Oman between 2026-10-07 and 2026-10-21.
- **Failure condition:** No commercial vessel is struck by a drone, missile or projectile in the Strait of Hormuz or Gulf of Oman between 2026-10-07 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-58
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** At least one merchant vessel is struck by a projectile, drone, mine or explosive in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-08 and 2026-10-21.
- **Resolution criterion:** YES if UKMTO reports a merchant vessel struck by a projectile, drone, mine or explosive in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-08 and 2026-10-21; NO otherwise.
- **Failure condition:** No merchant vessel is struck by a projectile, drone, mine or explosive in the Strait of Hormuz, Persian Gulf or Gulf of Oman between 2026-10-08 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-09
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** On 2026-10-20, a tropical cyclone named ISAIAS-26 causes a flood event in the U.S. Gulf Coast region, resulting in at least one fatality confirmed by the National Weather Service.
- **Resolution criterion:** The National Weather Service (NWS) issues a final report confirming that a flood event caused by tropical cyclone ISAIAS-26 resulted in at least one fatality on the U.S. Gulf Coast between 2026-10-18 and 2026-10-20.
- **Failure condition:** The National Weather Service does not issue a final report confirming a flood event caused by tropical cyclone ISAIAS-26 with at least one fatality on the U.S. Gulf Coast between 2026-10-18 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-18
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-23
- **Domain:** economics/markets
- **Claim:** The S&P 500 closes above 7,900 on at least one trading day between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** True if the index closes above 7,900 on any day in the window; False if it remains at or below 7,900 for the entire window. Reference: 7,777.51 on the packet date.
- **Failure condition:** The S&P 500 closes at or below 7,900 on every trading day in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-01
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** On 2026-10-15, the CISA KEV catalog will include at least one new entry for a vulnerability with CVSS score 10.0 or higher.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-21, and the vulnerability has a CVSS score of 10.0 or higher.
- **Failure condition:** The CISA KEV catalog contains no new entries with CVSS score 10.0 or higher between 2026-10-15 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-14
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** A new critical vulnerability with a CVSS score of 10.0 is added to the CISA Known Exploited Vulnerabilities catalog between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-20 for a vulnerability with a CVSS score of 10.0
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-10-15 and 2026-10-20 for a vulnerability with a CVSS score of 10.0
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-15
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** Hurricane Isaias makes landfall in the United States with sustained winds of at least 74 mph between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The National Hurricane Center issues a public advisory confirming Hurricane Isaias makes landfall in the United States with sustained winds of at least 74 mph between 2026-10-15 and 2026-10-20
- **Failure condition:** The National Hurricane Center does not issue a public advisory confirming Hurricane Isaias makes landfall in the United States with sustained winds of at least 74 mph between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-16
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** Russia conducts a kinetic strike using a ballistic missile on a civilian target in Kyiv between 2026-10-15 and 2026-10-20
- **Resolution criterion:** Three or more independent hostile sides confirm a Russian ballistic missile strike on a civilian target in Kyiv between 2026-10-15 and 2026-10-20
- **Failure condition:** Three or more independent hostile sides do not confirm a Russian ballistic missile strike on a civilian target in Kyiv between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-17
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** The UK House of Commons votes to approve German participation in the GCAP fighter jet programme between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The UK House of Commons passes a motion or bill approving German participation in the GCAP fighter jet programme between 2026-10-15 and 2026-10-20
- **Failure condition:** The UK House of Commons does not pass a motion or bill approving German participation in the GCAP fighter jet programme between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-18
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** crime/security
- **Claim:** The FBI issues a public indictment against a major cybercrime market operator for ransomware activities between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The US Department of Justice or FBI publishes a public indictment naming a major cybercrime market operator for ransomware activities between 2026-10-15 and 2026-10-20
- **Failure condition:** The US Department of Justice or FBI does not publish a public indictment naming a major cybercrime market operator for ransomware activities between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-19
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** A magnitude 7.0 or greater earthquake occurs in the Pacific Ring of Fire between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with a magnitude of 7.0 or greater in the Pacific Ring of Fire between 2026-10-15 and 2026-10-20
- **Failure condition:** The USGS Significant Quakes catalog does not record an event with a magnitude of 7.0 or greater in the Pacific Ring of Fire between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-20
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** South Korea test-fires a hypersonic missile with a range exceeding 1,000 km between 2026-10-15 and 2026-10-20
- **Resolution criterion:** The South Korean Ministry of National Defense or a major international news agency confirms a test-fire of a hypersonic missile with a range exceeding 1,000 km between 2026-10-15 and 2026-10-20
- **Failure condition:** The South Korean Ministry of National Defense or a major international news agency does not confirm a test-fire of a hypersonic missile with a range exceeding 1,000 km between 2026-10-15 and 2026-10-20
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-22
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** A maritime vessel is hit by projectiles or mines in the Strait of Hormuz or Gulf of Oman between 2026-10-13 and 2026-10-20.
- **Resolution criterion:** A vessel is confirmed hit by projectiles or mines in the Strait of Hormuz or Gulf of Oman.
- **Failure condition:** No vessel is hit by projectiles or mines in the Strait of Hormuz or Gulf of Oman between 2026-10-13 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-04
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** Between 2026-10-13 and 2026-10-19, a cyberattack exploiting unpatched AhsayCBS flaws will result in the deployment of webshells on at least one critical infrastructure system.
- **Resolution criterion:** At least one critical infrastructure system reports the deployment of a webshell via exploitation of unpatched AhsayCBS flaws between 2026-10-13 and 2026-10-19.
- **Failure condition:** No critical infrastructure system reports the deployment of a webshell via exploitation of unpatched AhsayCBS flaws between 2026-10-13 and 2026-10-19.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-07
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** On 2026-10-15, the CISA KEV catalog will include at least one vulnerability with a CVSS score of 10.0 that has been exploited in at least three distinct public attacks between 2026-10-12 and 2026-10-18.
- **Resolution criterion:** The CISA KEV catalog will carry a date-added value between 2026-10-12 and 2026-10-18 for a vulnerability with a CVSS score of 10.0 that has been exploited in at least three distinct public attacks, as confirmed by at least two independent sources (e.g., BleepingComputer, The Hacker News, or CISA advisories).
- **Failure condition:** The CISA KEV catalog does not contain any CVSS 10.0 vulnerability added between 2026-10-12 and 2026-10-18 that has been exploited in at least three distinct public attacks.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-08
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** Between 2026-10-15 and 2026-10-21, at least one major military strike will be confirmed by cross-bias corroboration (Grade A or B) in the Russia-Ukraine Theatre, involving the use of a cruise missile or drone, resulting in at least one casualty.
- **Resolution criterion:** At least one military strike in the Russia-Ukraine Theatre between 2026-10-15 and 2026-10-21, involving a cruise missile or drone, will be confirmed by cross-bias corroboration (Grade A or B) and result in at least one casualty, as verified by at least two independent sources (e.g., Al Jazeera, BBC World, Guardian World).
- **Failure condition:** No military strike in the Russia-Ukraine Theatre between 2026-10-15 and 2026-10-21 involving a cruise missile or drone is confirmed by cross-bias corroboration (Grade A or B) and results in at least one casualty.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-12
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** economics
- **Claim:** WTI Crude closes above 100.00 USD per barrel on at least one trading day between 2026-10-19 and 2026-10-22.
- **Resolution criterion:** A public market data feed shows WTI Crude closing above 100.00 USD on a day within the event window.
- **Failure condition:** WTI Crude closes at or below 100.00 USD on every trading day within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-17
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** cyber
- **Claim:** Between 2026-10-14 and 2026-10-21, the CISA KEV catalog carries a date-added value for a critical remote code execution vulnerability in the SonicWall SMA 1000, confirming the exploitation trend noted in item 18.
- **Resolution criterion:** The CISA KEV catalog lists the specific SonicWall SMA 1000 flaw as an exploited vulnerability.
- **Failure condition:** The CISA KEV catalog does not list the SonicWall SMA 1000 flaw as an exploited vulnerability by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000235ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['SonicWall SMA'] with dateAdded in [2026-10-14..2026-10-21] across 1756 catalog rows

### KKR-20261012-18
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama, following the M7.7 event in item 22.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Panama.
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 6.0 or greater earthquake in Panama by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-19
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** Between 2026-10-14 and 2026-10-21, the Federal Register publishes a notice of a new US sanctions regime targeting Iranian entities related to the Strait of Hormuz, as discussed in item 70.
- **Resolution criterion:** The Federal Register publishes a notice of a new US sanctions regime targeting Iranian entities related to the Strait of Hormuz.
- **Failure condition:** The Federal Register does not publish a notice of a new US sanctions regime targeting Iranian entities related to the Strait of Hormuz by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - fedreg - fetched 20261026T000236ZZ - sha256 b0233dbfad0cfa73...
  - instrument: https://www.federalregister.gov/api/v1/documents.json?per_page=20&conditions[term]=Iranian&conditions[publication_date][gte]=2026-10-14&conditions[publication_date][lte]=2026-10-21&conditions[agencies][]=treasury-department
  - observed: 1 document(s) for term 'Iranian' in window; ['Notice of OFAC Sanctions Actions']

### KKR-20261012-20
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Tonga, following the M5.5 event in item 36.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Tonga.
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 6.0 or greater earthquake in Tonga by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000236ZZ - sha256 a70545a0c356da81...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-14&endtime=2026-10-22&minlatitude=-23.0&maxlatitude=-15.0&minlongitude=-177.0&maxlongitude=-173.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261012-21
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** Between 2026-10-14 and 2026-10-21, the Federal Register publishes a notice of a new US sanctions regime targeting Russian entities related to the energy ceasefire, as discussed in item 34.
- **Resolution criterion:** The Federal Register publishes a notice of a new US sanctions regime targeting Russian entities related to the energy ceasefire.
- **Failure condition:** The Federal Register does not publish a notice of a new US sanctions regime targeting Russian entities related to the energy ceasefire by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-22
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** Between 2026-10-14 and 2026-10-21, the USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Alaska, following the M5.5 event in item 41.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake in Alaska.
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 6.0 or greater earthquake in Alaska by the deadline.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000236ZZ - sha256 bf21cc5e8b0feaed...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-14&endtime=2026-10-22&minlatitude=51.0&maxlatitude=72.0&minlongitude=-170.0&maxlongitude=-130.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261013-08
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-23
- **Domain:** political
- **Claim:** Between 2026-10-13 and 2026-10-20, a new political scandal involving a U.S. ambassador leads to their resignation, confirmed by at least two independent outlets from hostile political camps.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-13 and 2026-10-20.
- **Failure condition:** No public report confirms the resignation of a U.S. ambassador due to a political scandal, with confirmation from at least two independent outlets from hostile political camps, between 2026-10-13 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-15
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 6.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 6.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-17
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-23
- **Domain:** disaster
- **Claim:** The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **Resolution criterion:** The USGS Significant Quakes catalog records a magnitude 7.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **Failure condition:** The USGS Significant Quakes catalog does not record a magnitude 7.0 or greater earthquake between 2026-10-14 and 2026-10-21.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261016-04
- **Issued:** 2026-10-16  ·  **Deadline:** 2026-10-23
- **Domain:** military/conflict
- **Claim:** On 2026-10-17, a drone strike targeting a military installation in Kyiv, Ukraine, results in at least one confirmed casualty, as reported by two independent sources from hostile sides (UA and WEST) with no conflicting reports.
- **Resolution criterion:** At least one confirmed casualty from a drone strike in Kyiv, Ukraine, between 2026-10-17 and 2026-10-20, verified by two independent sources from hostile sides (UA and WEST) with no conflicting reports in corroborating outlets by 2026-10-23.
- **Failure condition:** No confirmed casualty is reported from a drone strike in Kyiv, Ukraine, between 2026-10-17 and 2026-10-20, or no two independent sources from hostile sides (UA and WEST) corroborate the event by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260927-07
- **Issued:** 2026-09-27  ·  **Deadline:** 2026-10-24
- **Domain:** economics/markets
- **Claim:** Between 2026-10-15 and 2026-10-22, the European Central Bank will announce a 0.5 percentage point increase in the main refinancing rate.
- **Resolution criterion:** The European Central Bank will announce a 0.5 percentage point increase in the main refinancing rate during the event window, as confirmed by ECB press release.
- **Failure condition:** The ECB does not announce a rate hike of 0.5 percentage points during the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20260928-01
- **Issued:** 2026-09-28  ·  **Deadline:** 2026-10-24
- **Domain:** military/conflict
- **Claim:** At least one major military strike or drone attack will be confirmed in Kyiv, Ukraine, between 2026-10-15 and 2026-10-22, with casualties reported by at least two independent sources from hostile sides (RU, UA).
- **Resolution criterion:** At least one report from a source in RU or UA, and one from the other side, confirms a military strike or drone attack in Kyiv during the window, with at least one casualty explicitly stated in both reports.
- **Failure condition:** No report from both RU and UA sides confirms a military strike or drone attack in Kyiv during the window, or no casualty is reported in both sources.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261006-11
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-24
- **Domain:** military_conflict
- **Claim:** Ukraine launches a drone attack resulting in confirmed casualties in Moscow between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** Two independent hostile sides report confirmed casualties from a Ukrainian drone attack in Moscow within the event window.
- **Failure condition:** No drone attack in Moscow results in confirmed casualties reported by two independent hostile sides within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-14
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-24
- **Domain:** disaster
- **Claim:** The USGS Significant Quakes catalog records an earthquake with magnitude 6.0 or greater between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** True if a magnitude 6.0+ event is recorded in the catalog within the window; False if no such event is recorded.
- **Failure condition:** No magnitude 6.0+ earthquake is recorded by the USGS in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-15
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-24
- **Domain:** political
- **Claim:** The UK Conservative Party leadership election concludes with a winner announced between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** True if a winner is publicly announced by a wire service within the window; False if the contest is still ongoing or unresolved.
- **Failure condition:** No winner is announced by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-16
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-24
- **Domain:** disaster
- **Claim:** A major power outage lasting more than 24 hours occurs in France between 2026-10-15 and 2026-10-22, confirmed by RTE or a major wire service.
- **Resolution criterion:** True if RTE or a wire service confirms a >24h outage; False if no such event is reported.
- **Failure condition:** No major power outage is reported by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-17
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-24
- **Domain:** cyber
- **Claim:** A new CVE is added to the NVD database with a CVSS score of 9.0 or higher for a vulnerability exploited in the wild, with a date_added between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** True if such a CVE exists in the NVD with the specified date_added; False if no such entry is found.
- **Failure condition:** No such CVE is found in the NVD by the deadline.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261007-19
- **Issued:** 2026-10-07  ·  **Deadline:** 2026-10-24
- **Domain:** disaster
- **Claim:** A tropical cyclone makes landfall in the United States between 2026-10-15 and 2026-10-22, confirmed by the NHC.
- **Resolution criterion:** True if the NHC confirms a landfall within the window; False if no landfall occurs.
- **Failure condition:** No tropical cyclone makes landfall in the US in the window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261010-05
- **Issued:** 2026-10-10  ·  **Deadline:** 2026-10-24
- **Domain:** disaster
- **Claim:** Between 2026-10-14 and 2026-10-20, a tropical storm will cause at least one fatality in the U.S. Gulf Coast region.
- **Resolution criterion:** At least one fatality is reported in the U.S. Gulf Coast region due to a tropical storm between 2026-10-14 and 2026-10-20.
- **Failure condition:** No fatalities are reported in the U.S. Gulf Coast region due to a tropical storm between 2026-10-14 and 2026-10-20.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261011-03
- **Issued:** 2026-10-11  ·  **Deadline:** 2026-10-24
- **Domain:** military/conflict
- **Claim:** Between 2026-10-16 and 2026-10-22, Saudi Arabia launches a retaliatory airstrike on a Houthi-controlled airfield in Yemen, confirmed by at least two independent sources from hostile sides (IL, AXIS).
- **Resolution criterion:** At least two independent sources from hostile sides (IL, AXIS) report a Saudi airstrike on a Houthi-controlled airfield in Yemen between 2026-10-16 and 2026-10-22, with no conflicting reports denying the event.
- **Failure condition:** No report from at least two independent sources from hostile sides (IL, AXIS) confirms a Saudi airstrike on a Houthi-controlled airfield in Yemen between 2026-10-16 and 2026-10-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-11
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-24
- **Domain:** military_conflict
- **Claim:** Houthi forces strike a commercial airport in Saudi Arabia between 2026-10-19 and 2026-10-22.
- **Resolution criterion:** Two wire services report a Houthi strike on a Saudi commercial airport with a date of impact falling within the event window.
- **Failure condition:** No wire service reports a Houthi strike on a Saudi commercial airport with an impact date within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-13
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-24
- **Domain:** political
- **Claim:** The European Commission imposes a final anti-dumping tariff on Chinese hybrid vehicles between 2026-10-19 and 2026-10-22.
- **Resolution criterion:** The European Commission publishes an official regulation or press release imposing a final anti-dumping tariff on Chinese hybrid vehicles with a date within the event window.
- **Failure condition:** The European Commission does not publish a regulation or press release imposing a final anti-dumping tariff on Chinese hybrid vehicles with a date within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-14
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-24
- **Domain:** disaster
- **Claim:** A magnitude 6.0 or greater earthquake occurs in Panama between 2026-10-19 and 2026-10-22.
- **Resolution criterion:** The USGS catalog records an earthquake with magnitude 6.0 or greater in Panama with a date within the event window.
- **Failure condition:** The USGS catalog records no earthquake with magnitude 6.0 or greater in Panama with a date within the event window.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261012-15
- **Issued:** 2026-10-12  ·  **Deadline:** 2026-10-24
- **Domain:** cyber
- **Claim:** A critical zero-day vulnerability is added to the CISA KEV catalog between 2026-10-19 and 2026-10-22.
- **Resolution criterion:** A public query of the CISA KEV catalog shows a record with a date-added value falling within the event window.
- **Failure condition:** The CISA KEV catalog is queried on the deadline date and no record with a date-added value within the event window is found.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261002-12
- **Issued:** 2026-10-02  ·  **Deadline:** 2026-10-25
- **Domain:** disaster
- **Claim:** Between 2026-10-12 and 2026-10-19, a major earthquake of magnitude 5.0 or higher occurs in the Pacific Northwest, as reported by USGS Significant Quakes.
- **Resolution criterion:** The USGS Significant Quakes catalog reports an earthquake of magnitude 5.0 or higher in the Pacific Northwest between 2026-10-12 and 2026-10-19.
- **Failure condition:** No earthquake of magnitude 5.0 or higher is reported in the Pacific Northwest by USGS during the event window.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000236ZZ - sha256 10efa9c1ba0f73f0...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-12&endtime=2026-10-20&minlatitude=42.0&maxlatitude=49.5&minlongitude=-125.0&maxlongitude=-116.5&minmagnitude=5.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261006-06
- **Issued:** 2026-10-06  ·  **Deadline:** 2026-10-25
- **Domain:** cyber
- **Claim:** Between 2026-10-16 and 2026-10-22, a major cyberattack will be confirmed on a critical infrastructure system in the United States, resulting in a disruption to essential services lasting more than 24 hours.
- **Resolution criterion:** At least one report from two or more hostile sides (US, WEST) confirms a cyberattack on a critical infrastructure system in the United States between 2026-10-16 and 2026-10-22, resulting in a disruption to essential services lasting more than 24 hours.
- **Failure condition:** No report from two or more hostile sides confirms a cyberattack on a critical infrastructure system in the United States between 2026-10-16 and 2026-10-22, or the disruption lasts 24 hours or less.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-23
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-25
- **Domain:** cyber
- **Claim:** The CISA KEV catalog adds an entry for a critical vulnerability in the FortiGate VPN appliance between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** The CISA KEV catalog carries a date-added value between 2026-10-15 and 2026-10-22 for a FortiGate vulnerability.
- **Failure condition:** The CISA KEV catalog does not carry a date-added value between 2026-10-15 and 2026-10-22 for a FortiGate vulnerability.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - kev - fetched 20261026T000236ZZ - sha256 97a6e54bc74c651a...
  - instrument: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
  - observed: 0 matching entries for ['FortiGate'] with dateAdded in [2026-10-15..2026-10-22] across 1756 catalog rows

### KKR-20261008-24
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-25
- **Domain:** disaster
- **Claim:** A magnitude 6.0 or greater earthquake occurs in the Philippines between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude 6.0 or greater in the Philippines.
- **Failure condition:** The USGS Significant Quakes catalog does not record an event with magnitude 6.0 or greater in the Philippines between 2026-10-15 and 2026-10-22.
- **PYTHON-HELD EVIDENCE** (rule 6 applies) - usgs - fetched 20261026T000236ZZ - sha256 9b831ee44183166a...
  - instrument: https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2026-10-15&endtime=2026-10-23&minlatitude=4.5&maxlatitude=21.0&minlongitude=116.0&maxlongitude=127.0&minmagnitude=6.0
  - observed: 0 event(s) returned; top magnitudes []

### KKR-20261008-25
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-25
- **Domain:** political
- **Claim:** South Korea formally recalls its ambassador to Ukraine from duty between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** The South Korean Ministry of Foreign Affairs formally recalls its ambassador to Ukraine from duty.
- **Failure condition:** The South Korean Ministry of Foreign Affairs does not formally recall its ambassador to Ukraine from duty between 2026-10-15 and 2026-10-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-26
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-25
- **Domain:** crime/security
- **Claim:** The owner of the Empire cybercrime market is sentenced to prison between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** A court docket records a prison sentence for the owner of the Empire cybercrime market.
- **Failure condition:** A court docket does not record a prison sentence for the owner of the Empire cybercrime market between 2026-10-15 and 2026-10-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261008-27
- **Issued:** 2026-10-08  ·  **Deadline:** 2026-10-25
- **Domain:** political
- **Claim:** The UK House of Commons passes a vote to join the GCAP fighter jet programme between 2026-10-15 and 2026-10-22.
- **Resolution criterion:** The UK House of Commons passes a vote to join the GCAP fighter jet programme.
- **Failure condition:** The UK House of Commons does not pass a vote to join the GCAP fighter jet programme between 2026-10-15 and 2026-10-22.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-06
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-25
- **Domain:** cyber
- **Claim:** Between 2026-10-16 and 2026-10-23, at least one new cyberattack exploiting CVE-2016-3081 in Apache Struts will be reported in at least two independent public sources.
- **Resolution criterion:** At least two independent public sources (e.g., BleepingComputer, The Hacker News, or CISA) report a confirmed cyberattack exploiting CVE-2016-3081 in Apache Struts between 2026-10-16 and 2026-10-23.
- **Failure condition:** No independent public report confirms a cyberattack exploiting CVE-2016-3081 in Apache Struts between 2026-10-16 and 2026-10-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-07
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-25
- **Domain:** disaster
- **Claim:** Between 2026-10-16 and 2026-10-23, at least one new tropical storm or hurricane will make landfall in the United States with a storm surge warning in effect.
- **Resolution criterion:** At least one tropical storm or hurricane makes landfall in the United States between 2026-10-16 and 2026-10-23, with a storm surge warning issued by the National Hurricane Center (NHC) for the affected area.
- **Failure condition:** No tropical storm or hurricane makes landfall in the United States between 2026-10-16 and 2026-10-23 with a storm surge warning issued by the NHC.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261009-08
- **Issued:** 2026-10-09  ·  **Deadline:** 2026-10-25
- **Domain:** cyber
- **Claim:** Between 2026-10-16 and 2026-10-23, at least one new cyberattack exploiting a zero-day vulnerability in a widely used open-source project will be reported in at least two independent public sources.
- **Resolution criterion:** At least two independent public sources (e.g., BleepingComputer, The Hacker News, or CISA) report a confirmed cyberattack exploiting a zero-day vulnerability in a widely used open-source project between 2026-10-16 and 2026-10-23.
- **Failure condition:** No independent public report confirms a cyberattack exploiting a zero-day vulnerability in a widely used open-source project between 2026-10-16 and 2026-10-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261013-07
- **Issued:** 2026-10-13  ·  **Deadline:** 2026-10-25
- **Domain:** disaster
- **Claim:** On 2026-10-17, a major earthquake of magnitude 6.5 or higher occurs in the Mid-Atlantic Ridge, with a depth of less than 20 km, as confirmed by the USGS Significant Quakes database.
- **Resolution criterion:** The USGS Significant Quakes database carries an event with magnitude ≥6.5 and depth <20 km in the Mid-Atlantic Ridge between 2026-10-13 and 2026-10-17.
- **Failure condition:** No USGS Significant Quakes event with magnitude ≥6.5 and depth <20 km in the Mid-Atlantic Ridge is recorded between 2026-10-13 and 2026-10-17.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-17
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-10-25
- **Domain:** disaster
- **Claim:** A magnitude 6.0 or greater earthquake occurs between 2026-10-16 and 2026-10-23.
- **Resolution criterion:** The USGS Significant Quakes catalog records an event with magnitude >= 6.0 between 2026-10-16 and 2026-10-23.
- **Failure condition:** No events with magnitude >= 6.0 are recorded in the USGS Significant Quakes catalog between 2026-10-16 and 2026-10-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).

### KKR-20261015-18
- **Issued:** 2026-10-15  ·  **Deadline:** 2026-10-25
- **Domain:** military
- **Claim:** A new major offensive operation begins in the Russia-Ukraine theatre between 2026-10-16 and 2026-10-23.
- **Resolution criterion:** Two independent wire services report a new major offensive operation in the Russia-Ukraine theatre between 2026-10-16 and 2026-10-23.
- **Failure condition:** No new major offensive operations are reported by two independent wire services in the Russia-Ukraine theatre between 2026-10-16 and 2026-10-23.
- **PYTHON-HELD EVIDENCE:** NONE - no keyless instrument maps this criterion (rule 6: a juror without search returns ABSTAIN here).
