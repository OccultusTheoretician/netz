#!/usr/bin/env python3
"""
build_compendium.py - who sets the rules, in every sector, in one file.

THE GAP THIS FILLS

Every regulated sector has bodies that set its standards, publish its rules and
hold its decision calendar. Every one of those bodies is documented. Nobody has
indexed them together in a machine-readable form. A person who wants to know
who sets fire-protection standards, who governs orbital slot allocation, and
who accredits medical laboratories has to know three separate worlds.

This is the index. It is a reference artifact in its own right, and it is also
the source list for a page-watch: a body that publishes a feed can be watched;
a body that does not is still worth knowing about.

EVERY ENTRY IS UNVERIFIED UNTIL PROBED

The names, sectors and jurisdictions below are written with confidence. The
DOMAINS ARE NOT. Writing 150 URLs from memory would produce a file that looks
authoritative and contains invented addresses - which is the exact failure mode
this desk has spent a day catching in its own tools. So every entry carries:

    "verified": false

and a probe flips it only on an HTTP response. An unverified entry is a lead,
not a fact, and the field says so on its face.

The two existing Spion sources that reject programmatic clients are the reason
this matters: at fifty bodies most will refuse, and a compendium that claims to
watch what it cannot reach is worse than one that separates the two.

PROVENANCE, AND THE PRIORITY CLOCK

The compendium is committed to a public repository whose history the committer
cannot rewrite without the rewrite being visible. That commit is the priority
evidence - the same mechanism the Kalls hashlog uses, and stronger than any
unfiled ritual. The file carries its own SHA-256 in a sidecar so a later
version can be shown to differ from an earlier one.

    python build_compendium.py
    python build_compendium.py --dry-run
    python build_compendium.py --stats

Writes spion_compendium.json and spion_compendium.sha256. Standard library
only. ASCII-only output.
"""

import argparse
import datetime as dt
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

OUT = Path("spion_compendium.json")
SUM = Path("spion_compendium.sha256")

# (sector, name, abbrev, jurisdiction, what it sets, domain-guess)
# Domain guesses are UNVERIFIED. The probe decides.
BODIES = [
    # --- accounting, audit, public finance ---------------------------------
    ("accounting", "Public Company Accounting Oversight Board", "PCAOB", "US", "audit standards for public company audits", "pcaobus.org"),
    ("accounting", "Financial Accounting Standards Board", "FASB", "US", "US GAAP for private and public entities", "fasb.org"),
    ("accounting", "Governmental Accounting Standards Board", "GASB", "US", "US GAAP for state and local government", "gasb.org"),
    ("accounting", "Federal Accounting Standards Advisory Board", "FASAB", "US", "US federal government accounting", "fasab.gov"),
    ("accounting", "International Accounting Standards Board", "IASB", "global", "IFRS accounting standards", "ifrs.org"),
    ("accounting", "International Auditing and Assurance Standards Board", "IAASB", "global", "international standards on auditing", "iaasb.org"),
    ("accounting", "International Ethics Standards Board for Accountants", "IESBA", "global", "the accountants' ethics code", "ethicsboard.org"),
    ("accounting", "International Public Sector Accounting Standards Board", "IPSASB", "global", "public sector accounting standards", "ipsasb.org"),
    ("accounting", "Government Accountability Office", "GAO", "US", "government auditing standards, the Yellow Book", "gao.gov"),
    ("accounting", "American Institute of CPAs", "AICPA", "US", "private company audit and attest standards", "aicpa-cima.com"),
    ("accounting", "Institute of Internal Auditors", "IIA", "global", "internal audit standards", "theiia.org"),
    # --- securities and markets --------------------------------------------
    ("securities", "Securities and Exchange Commission", "SEC", "US", "securities disclosure and market regulation", "sec.gov"),
    ("securities", "Financial Industry Regulatory Authority", "FINRA", "US", "broker-dealer conduct rules", "finra.org"),
    ("securities", "Commodity Futures Trading Commission", "CFTC", "US", "derivatives and futures markets", "cftc.gov"),
    ("securities", "Municipal Securities Rulemaking Board", "MSRB", "US", "municipal securities market rules", "msrb.org"),
    ("securities", "International Organization of Securities Commissions", "IOSCO", "global", "securities regulation principles", "iosco.org"),
    ("securities", "European Securities and Markets Authority", "ESMA", "EU", "EU securities markets", "esma.europa.eu"),
    ("securities", "Financial Conduct Authority", "FCA", "UK", "UK financial conduct", "fca.org.uk"),
    ("securities", "Financial Stability Board", "FSB", "global", "systemic financial stability recommendations", "fsb.org"),
    # --- banking -----------------------------------------------------------
    ("banking", "Board of Governors of the Federal Reserve System", "FRB", "US", "bank holding company supervision, monetary policy", "federalreserve.gov"),
    ("banking", "Office of the Comptroller of the Currency", "OCC", "US", "national bank supervision", "occ.gov"),
    ("banking", "Federal Deposit Insurance Corporation", "FDIC", "US", "deposit insurance and state bank supervision", "fdic.gov"),
    ("banking", "National Credit Union Administration", "NCUA", "US", "credit union regulation", "ncua.gov"),
    ("banking", "Basel Committee on Banking Supervision", "BCBS", "global", "bank capital and liquidity standards", "bis.org"),
    ("banking", "European Central Bank", "ECB", "EU", "euro area monetary policy and bank supervision", "ecb.europa.eu"),
    ("banking", "Bank of England", "BoE", "UK", "UK monetary policy and prudential regulation", "bankofengland.co.uk"),
    # --- insurance ---------------------------------------------------------
    ("insurance", "National Association of Insurance Commissioners", "NAIC", "US", "model insurance laws and statutory accounting", "naic.org"),
    ("insurance", "International Association of Insurance Supervisors", "IAIS", "global", "insurance supervision principles", "iaisweb.org"),
    ("insurance", "Actuarial Standards Board", "ASB", "US", "actuarial standards of practice", "actuarialstandardsboard.org"),
    # --- cyber and information security -----------------------------------
    ("cyber", "National Institute of Standards and Technology", "NIST", "US", "cybersecurity and AI risk frameworks, FIPS", "nist.gov"),
    ("cyber", "Cybersecurity and Infrastructure Security Agency", "CISA", "US", "federal cyber directives, the KEV catalog", "cisa.gov"),
    ("cyber", "ISO/IEC JTC 1/SC 27", "SC27", "global", "information security management standards", "iso.org"),
    ("cyber", "European Union Agency for Cybersecurity", "ENISA", "EU", "EU cybersecurity certification", "enisa.europa.eu"),
    ("cyber", "PCI Security Standards Council", "PCI SSC", "global", "payment card data security", "pcisecuritystandards.org"),
    ("cyber", "Center for Internet Security", "CIS", "global", "configuration benchmarks and controls", "cisecurity.org"),
    ("cyber", "Forum of Incident Response and Security Teams", "FIRST", "global", "CVSS, incident response practice", "first.org"),
    # --- internet and web --------------------------------------------------
    ("internet", "Internet Engineering Task Force", "IETF", "global", "internet protocol standards, RFCs", "ietf.org"),
    ("internet", "Internet Corporation for Assigned Names and Numbers", "ICANN", "global", "domain name system policy", "icann.org"),
    ("internet", "World Wide Web Consortium", "W3C", "global", "web platform standards", "w3.org"),
    ("internet", "Unicode Consortium", "Unicode", "global", "character encoding", "unicode.org"),
    ("internet", "Institute of Electrical and Electronics Engineers Standards Association", "IEEE-SA", "global", "networking, electrical and computing standards", "standards.ieee.org"),
    # --- telecom -----------------------------------------------------------
    ("telecom", "Federal Communications Commission", "FCC", "US", "spectrum, broadcast and carrier regulation", "fcc.gov"),
    ("telecom", "International Telecommunication Union", "ITU", "global", "spectrum allocation, orbital slots, telecom standards", "itu.int"),
    ("telecom", "3rd Generation Partnership Project", "3GPP", "global", "mobile network standards", "3gpp.org"),
    ("telecom", "European Telecommunications Standards Institute", "ETSI", "EU", "European telecom standards", "etsi.org"),
    # --- health and medicine ----------------------------------------------
    ("health", "Food and Drug Administration", "FDA", "US", "drugs, devices, food safety, tobacco", "fda.gov"),
    ("health", "Centers for Medicare and Medicaid Services", "CMS", "US", "reimbursement rules, CLIA, conditions of participation", "cms.gov"),
    ("health", "World Health Organization", "WHO", "global", "international health regulations, essential medicines", "who.int"),
    ("health", "International Council for Harmonisation", "ICH", "global", "pharmaceutical development and registration guidelines", "ich.org"),
    ("health", "Health Level Seven International", "HL7", "global", "health data interchange, FHIR", "hl7.org"),
    ("health", "United States Pharmacopeia", "USP", "US", "drug and supplement quality monographs", "usp.org"),
    ("health", "The Joint Commission", "TJC", "US", "hospital accreditation standards", "jointcommission.org"),
    ("health", "European Medicines Agency", "EMA", "EU", "EU medicine authorisation", "ema.europa.eu"),
    ("health", "Advisory Committee on Immunization Practices", "ACIP", "US", "US immunization schedules", "cdc.gov"),
    # --- aviation ----------------------------------------------------------
    ("aviation", "Federal Aviation Administration", "FAA", "US", "airworthiness, air traffic, commercial space launch", "faa.gov"),
    ("aviation", "European Union Aviation Safety Agency", "EASA", "EU", "EU airworthiness and operations", "easa.europa.eu"),
    ("aviation", "International Civil Aviation Organization", "ICAO", "global", "international aviation standards and recommended practices", "icao.int"),
    ("aviation", "RTCA", "RTCA", "US", "avionics technical standards", "rtca.org"),
    # --- maritime ----------------------------------------------------------
    ("maritime", "International Maritime Organization", "IMO", "global", "SOLAS, MARPOL, ship safety and pollution", "imo.org"),
    ("maritime", "International Association of Classification Societies", "IACS", "global", "ship classification unified requirements", "iacs.org.uk"),
    ("maritime", "United States Coast Guard", "USCG", "US", "US vessel inspection and marine safety", "uscg.mil"),
    # --- nuclear -----------------------------------------------------------
    ("nuclear", "Nuclear Regulatory Commission", "NRC", "US", "US reactor licensing and safety", "nrc.gov"),
    ("nuclear", "International Atomic Energy Agency", "IAEA", "global", "safeguards and nuclear safety standards", "iaea.org"),
    ("nuclear", "World Association of Nuclear Operators", "WANO", "global", "operator peer review", "wano.info"),
    # --- energy and utilities ---------------------------------------------
    ("energy", "Federal Energy Regulatory Commission", "FERC", "US", "interstate transmission, wholesale power markets", "ferc.gov"),
    ("energy", "North American Electric Reliability Corporation", "NERC", "NA", "bulk power system reliability standards", "nerc.com"),
    ("energy", "International Energy Agency", "IEA", "global", "energy statistics and policy analysis", "iea.org"),
    ("energy", "American Petroleum Institute", "API", "US", "oil and gas technical standards", "api.org"),
    # --- environment and climate ------------------------------------------
    ("environment", "Environmental Protection Agency", "EPA", "US", "air, water, chemicals, emissions rules", "epa.gov"),
    ("environment", "Intergovernmental Panel on Climate Change", "IPCC", "global", "climate assessment reports", "ipcc.ch"),
    ("environment", "Science Based Targets initiative", "SBTi", "global", "corporate emissions target validation", "sciencebasedtargets.org"),
    ("environment", "Greenhouse Gas Protocol", "GHGP", "global", "emissions accounting standards", "ghgprotocol.org"),
    ("environment", "European Chemicals Agency", "ECHA", "EU", "REACH and CLP chemical regulation", "echa.europa.eu"),
    # --- construction, fire, building -------------------------------------
    ("construction", "International Code Council", "ICC", "US", "model building, residential and fire codes", "iccsafe.org"),
    ("construction", "National Fire Protection Association", "NFPA", "US", "fire codes and the National Electrical Code", "nfpa.org"),
    ("construction", "ASHRAE", "ASHRAE", "global", "HVAC, refrigeration, building energy standards", "ashrae.org"),
    ("construction", "American Society for Testing and Materials", "ASTM", "global", "materials test methods and specifications", "astm.org"),
    ("construction", "American Concrete Institute", "ACI", "global", "concrete design and construction codes", "concrete.org"),
    ("construction", "American Institute of Steel Construction", "AISC", "US", "structural steel specifications", "aisc.org"),
    # --- electrical and product safety ------------------------------------
    ("electrical", "International Electrotechnical Commission", "IEC", "global", "electrotechnical standards", "iec.ch"),
    ("electrical", "UL Standards and Engagement", "UL", "global", "product safety standards", "ulse.org"),
    # --- automotive and rail ----------------------------------------------
    ("automotive", "National Highway Traffic Safety Administration", "NHTSA", "US", "federal motor vehicle safety standards", "nhtsa.gov"),
    ("automotive", "UNECE World Forum for Harmonization of Vehicle Regulations", "WP.29", "global", "vehicle regulation harmonisation", "unece.org"),
    ("automotive", "SAE International", "SAE", "global", "automotive and aerospace engineering standards", "sae.org"),
    ("rail", "Federal Railroad Administration", "FRA", "US", "US rail safety regulation", "railroads.dot.gov"),
    ("rail", "Association of American Railroads", "AAR", "NA", "interchange rules and equipment standards", "aar.org"),
    ("rail", "European Union Agency for Railways", "ERA", "EU", "EU rail interoperability and safety", "era.europa.eu"),
    # --- labour and occupational safety -----------------------------------
    ("labour", "Occupational Safety and Health Administration", "OSHA", "US", "workplace safety standards", "osha.gov"),
    ("labour", "Mine Safety and Health Administration", "MSHA", "US", "mine safety standards", "msha.gov"),
    ("labour", "National Institute for Occupational Safety and Health", "NIOSH", "US", "exposure limits and hazard research", "cdc.gov"),
    ("labour", "International Labour Organization", "ILO", "global", "labour conventions and recommendations", "ilo.org"),
    # --- food and agriculture ---------------------------------------------
    ("food", "Food Safety and Inspection Service", "FSIS", "US", "meat, poultry and egg product inspection", "fsis.usda.gov"),
    ("food", "Codex Alimentarius Commission", "Codex", "global", "international food standards", "fao.org"),
    ("food", "Global Food Safety Initiative", "GFSI", "global", "food safety scheme benchmarking", "mygfsi.com"),
    ("food", "World Organisation for Animal Health", "WOAH", "global", "animal health standards", "woah.org"),
    # --- trade and customs -------------------------------------------------
    ("trade", "World Trade Organization", "WTO", "global", "trade agreements and dispute settlement", "wto.org"),
    ("trade", "World Customs Organization", "WCO", "global", "the Harmonized System nomenclature", "wcoomd.org"),
    ("trade", "United States International Trade Commission", "USITC", "US", "trade injury determinations, the HTS", "usitc.gov"),
    # --- mining and extractives -------------------------------------------
    ("mining", "Committee for Mineral Reserves International Reporting Standards", "CRIRSCO", "global", "mineral reserve reporting", "crirsco.com"),
    ("mining", "International Council on Mining and Metals", "ICMM", "global", "mining performance expectations", "icmm.com"),
    # --- space -------------------------------------------------------------
    ("space", "UN Committee on the Peaceful Uses of Outer Space", "COPUOS", "global", "space law and debris mitigation guidelines", "unoosa.org"),
    ("space", "Inter-Agency Space Debris Coordination Committee", "IADC", "global", "debris mitigation guidelines", "iadc-home.org"),
    # --- artificial intelligence ------------------------------------------
    ("ai", "ISO/IEC JTC 1/SC 42", "SC42", "global", "artificial intelligence standards", "iso.org"),
    ("ai", "European AI Office", "AI Office", "EU", "EU AI Act implementation and codes of practice", "digital-strategy.ec.europa.eu"),
    # --- standards bodies proper ------------------------------------------
    ("standards", "International Organization for Standardization", "ISO", "global", "cross-sector management and technical standards", "iso.org"),
    ("standards", "American National Standards Institute", "ANSI", "US", "US standards accreditation", "ansi.org"),
    ("standards", "British Standards Institution", "BSI", "UK", "UK national standards", "bsigroup.com"),
    ("standards", "Deutsches Institut fuer Normung", "DIN", "DE", "German national standards", "din.de"),
    ("standards", "European Committee for Standardization", "CEN", "EU", "European standards", "cencenelec.eu"),
    # --- legal, professional, education -----------------------------------
    ("legal", "American Bar Association", "ABA", "US", "model rules of professional conduct, law school accreditation", "americanbar.org"),
    ("legal", "National Conference of Bar Examiners", "NCBE", "US", "bar examination content", "ncbex.org"),
    ("education", "Council for Higher Education Accreditation", "CHEA", "US", "recognition of accrediting bodies", "chea.org"),
    # --- sport -------------------------------------------------------------
    ("sport", "World Anti-Doping Agency", "WADA", "global", "the prohibited list and testing standards", "wada-ama.org"),
    ("sport", "Court of Arbitration for Sport", "CAS", "global", "sport dispute jurisprudence", "tas-cas.org"),
    ("sport", "International Olympic Committee", "IOC", "global", "the Olympic Charter", "olympic.org"),
]


# ---------------------------------------------------------------------------
# CADENCE. Keyed by abbrev. Two claims per entry and they have DIFFERENT
# reliability, which is why they are separate fields:
#
#   pattern   the structural cadence - "8 scheduled meetings per year", "three
#             year code cycle". Stable over decades. Asserted with confidence.
#   dates     whether the body PUBLISHES its schedule in advance. This is what
#             determines whether a sealed forecast can key off a known date, and
#             it is the field that matters to a ledger.
#
# A SPECIFIC next-meeting date is NOT recorded here. Those move, and a stale
# date in a reference file is worse than an absent one. The probe looks them up.
#
# An absent entry means unknown, not continuous. 115 bodies, and the gaps are
# informative: a body with no discoverable cadence is a body whose decisions
# cannot be anticipated, which is itself a finding about that sector.
CADENCE = {
    # fixed calendar, published ahead - the forecastable tier
    "FRB":    ("8 scheduled FOMC meetings per year", True, "high"),
    "ECB":    ("monetary policy decisions every six weeks", True, "high"),
    "BoE":    ("8 scheduled MPC meetings per year", True, "high"),
    "FERC":   ("monthly open meeting", True, "high"),
    "ACIP":   ("about three regular meetings per year", True, "high"),
    "NAIC":   ("three national meetings per year, spring summer fall", True, "high"),
    "IETF":   ("three plenary meetings per year", True, "high"),
    "ICANN":  ("three public meetings per year", True, "high"),
    "3GPP":   ("quarterly plenary meetings", True, "high"),
    "BCBS":   ("meets about quarterly", True, "medium"),
    "FSB":    ("plenary about twice yearly", True, "medium"),
    "IAEA":   ("General Conference annually in September", True, "high"),
    "Codex":  ("Commission session annually", True, "high"),
    "IOSCO":  ("annual meeting", True, "medium"),
    "FASB":   ("board meetings roughly weekly, continuous agenda", True, "high"),
    "GASB":   ("board meetings roughly monthly, continuous agenda", True, "high"),
    # fixed revision cycles - the most forecastable of all, years ahead
    "ICC":    ("three year code development cycle", True, "high"),
    "NFPA":   ("three to five year cycle per document, NEC every three years", True, "high"),
    "ASHRAE": ("three year cycle on 90.1 and 62.1", True, "high"),
    "WADA":   ("Prohibited List annually, published about September, effective 1 January", True, "high"),
    "ICAO":   ("Assembly every three years", True, "high"),
    "ITU":    ("World Radiocommunication Conference every three to four years", True, "high"),
    "WTO":    ("Ministerial Conference about every two years", True, "medium"),
    "IPCC":   ("assessment cycle of roughly six to eight years", True, "medium"),
    "ISO":    ("continuous, with systematic review of each standard every five years", True, "medium"),
    "IEC":    ("continuous, with systematic review cycles", True, "medium"),
    "CMS":    ("annual payment rule cycle, proposed spring and final summer", True, "high"),
    "IMO":    ("MSC and MEPC each meet roughly annually", True, "medium"),
    # continuous - no meeting to key off, but a dated publication stream
    "CISA":   ("continuous additions to the KEV catalog and advisories", False, "high"),
    "NIST":   ("continuous publication, draft and final comment windows", False, "medium"),
    "SEC":    ("continuous rulemaking, agenda in the semiannual Unified Agenda", True, "medium"),
    "FDA":    ("continuous, advisory committee meetings noticed in advance", True, "high"),
    "EPA":    ("continuous rulemaking, Unified Agenda", True, "medium"),
    "OSHA":   ("continuous rulemaking, Unified Agenda", True, "medium"),
    "FCC":    ("monthly open meeting, agenda published three weeks ahead", True, "high"),
    "PCAOB":  ("open meetings as needed, standard-setting agenda published", True, "medium"),
    "FINRA":  ("continuous rule filings with the SEC", False, "medium"),
    "NERC":   ("continuous standards development, ballot windows published", True, "medium"),
    "NRC":    ("continuous licensing and rulemaking", False, "low"),
    "ECHA":   ("continuous, with REACH deadline milestones", True, "medium"),
    "EMA":    ("CHMP meets monthly", True, "high"),
    "FSIS":   ("continuous rulemaking and directives", False, "low"),
    "IASB":   ("board meetings roughly monthly, work plan published", True, "high"),
    "IAASB":  ("meets about four times a year", True, "medium"),
    "IESBA":  ("meets about four times a year", True, "medium"),
    "IPSASB": ("meets about four times a year", True, "medium"),
    "GAO":    ("Yellow Book revised irregularly, roughly every three to five years", False, "low"),
    "AICPA":  ("continuous, ASB meets several times a year", True, "medium"),
    "MSRB":   ("board meets quarterly", True, "medium"),
    "CFTC":   ("continuous rulemaking, open meetings noticed", True, "medium"),
    "ESMA":   ("continuous, annual work programme published", True, "medium"),
    "FCA":    ("continuous, policy statements and annual business plan", True, "medium"),
    "USITC":  ("continuous, statutory investigation deadlines", True, "high"),
    "WCO":    ("Harmonized System revised every five years", True, "high"),
    "IAIS":   ("annual general meeting, continuous standard setting", True, "medium"),
    "NHTSA":  ("continuous rulemaking, Unified Agenda", True, "medium"),
    "SAE":    ("continuous, five year document review", False, "low"),
    "ASTM":   ("continuous, committee ballot cycles", False, "low"),
    "W3C":    ("continuous, annual TPAC", True, "medium"),
    "IEEE-SA": ("continuous, standards board meets several times a year", True, "medium"),
    "CAS":    ("continuous, awards published on decision", False, "medium"),
    "IOC":    ("Session annually, Executive Board several times a year", True, "medium"),
    "WOAH":   ("General Session annually in May", True, "high"),
    "ILO":    ("International Labour Conference annually in June", True, "high"),
    "WHO":    ("World Health Assembly annually in May", True, "high"),
    "COPUOS": ("Scientific and Technical Subcommittee annually in February", True, "medium"),
}

def main():
    ap = argparse.ArgumentParser(description="build the standard-setting compendium")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()

    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entries = []
    for i, (sector, name, abbr, juris, sets, domain) in enumerate(BODIES, 1):
        entries.append({
            "id": "SB-%03d" % i,
            "sector": sector,
            "name": name,
            "abbrev": abbr,
            "jurisdiction": juris,
            "sets": sets,
            "domain": domain,
            "verified": False,
            "reachable": None,
            "feed": None,
            "last_probed": None,
            "cadence": (CADENCE.get(abbr, (None, None, None))[0]
                        or "unknown - no cadence established for this body"),
            "calendar_published": CADENCE.get(abbr, (None, None, None))[1],
            "forecast_utility": CADENCE.get(abbr, (None, None, None))[2],
            "note": ("Name, sector and jurisdiction asserted with confidence. "
                     "Domain is an UNVERIFIED guess until a probe returns a "
                     "response. An unverified entry is a lead, not a fact."),
        })

    sectors = Counter(e["sector"] for e in entries)
    juris = Counter(e["jurisdiction"] for e in entries)

    doc = {
        "schema": "spion-compendium/0.2",
        "generated": now,
        "count": len(entries),
        "verified_count": 0,
        "schema_note": "v0.2 adds cadence. See digest_covers on the hash.",
        "disclosure": {
            "what_this_is": ("An index of bodies that set standards, publish "
                             "rules or hold decision calendars, across every "
                             "regulated sector. A reference artifact, and the "
                             "source list for a page-watch."),
            "verification": ("Every entry is verified:false on issue. Names, "
                             "sectors and jurisdictions are asserted from "
                             "domain knowledge. DOMAINS ARE UNVERIFIED "
                             "GUESSES. A probe flips verified only on an HTTP "
                             "response, and records whether a feed exists."),
            "reachability": ("Two of the five sources already watched by this "
                             "desk reject programmatic clients. At this scale "
                             "most will. A body that cannot be watched is "
                             "still worth indexing, and the file separates "
                             "indexed from watched rather than conflating "
                             "them."),
            "completeness": ("This is not exhaustive and does not claim to be. "
                             "Sub-national regulators, sectoral trade bodies "
                             "and most national mirrors of international "
                             "standards are absent. Additions are welcome "
                             "against the same verification rule."),
            "priority_evidence": ("This file is committed to a public "
                                  "repository whose history cannot be "
                                  "rewritten without the rewrite being "
                                  "visible to anyone holding an earlier "
                                  "clone. That commit is the dated record of "
                                  "first publication. A SHA-256 sidecar "
                                  "accompanies it so any later version can be "
                                  "shown to differ."),
        },
        "sectors": dict(sorted(sectors.items())),
        "jurisdictions": dict(sorted(juris.items())),
        "bodies": entries,
    }

    # The digest covers the BODIES ARRAY ONLY. v0.1 hashed the whole document
    # including its own `generated` timestamp, so two runs of identical content
    # produced different digests and the sidecar could answer "is this the same
    # file" but never "did the content change". This one answers the second.
    content = json.dumps(doc["bodies"], indent=2, ensure_ascii=False,
                         sort_keys=True)
    digest = hashlib.sha256(content.encode("utf-8")).hexdigest()
    doc["content_sha256"] = digest
    doc["digest_covers"] = ("the bodies array only, sorted by key, excluding "
                            "the generated timestamp - so two versions are "
                            "comparable on content rather than on when they "
                            "were built")
    blob = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"

    print("")
    print("STANDARD-SETTING BODY COMPENDIUM")
    print("=" * 70)
    print("  %d bodies across %d sectors, %d jurisdictions"
          % (len(entries), len(sectors), len(juris)))
    print("  all verified:false on issue - the probe decides")
    print("")
    print("  %-16s %s" % ("sector", "count"))
    for s, n in sorted(sectors.items(), key=lambda kv: -kv[1]):
        print("  %-16s %3d  %s" % (s, n, "#" * n))
    print("")
    print("  jurisdictions: %s"
          % ", ".join("%s %d" % (k, v) for k, v in
                      sorted(juris.items(), key=lambda kv: -kv[1])))
    print("")
    print("  sha256 %s" % digest)
    if a.stats:
        return 0
    if a.dry_run:
        print("")
        print("  DRY RUN - %d bytes would be written to %s" % (len(blob), OUT))
        return 0
    OUT.write_text(blob, encoding="utf-8", newline="\n")
    SUM.write_text("%s  %s\n" % (digest, OUT.name), encoding="utf-8", newline="\n")
    print("")
    print("  WROTE %s  (%d bytes)" % (OUT, len(blob)))
    print("  WROTE %s" % SUM)
    print("")
    print("  The commit is the priority clock. Ship it before probing, so the")
    print("  dated record of first publication precedes any enrichment.")
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
