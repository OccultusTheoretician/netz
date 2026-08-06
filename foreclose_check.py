#!/usr/bin/env python3
# foreclose_check.py -- the already-decided gate (v1)
#
# PRINCIPLE. A forecast must be open at seal. If the elicitation packet the
# arm just read already decides the claim -- in either direction -- the row
# is not a forecast and must not seal as one. Instances on the book:
#   KKR-20260805-01: packet stated CVE-2026-9198 dateAdded 2026-08-04; row
#       required a dateAdded in 08-05..08-12. Foreclosed at seal. Priced 85%.
#   KKR-20260805-02: packet carried the Sarangani M6.3 depth-10km quake,
#       05 Aug 14:31 UTC, inside the row's window. Satisfied at seal, 32
#       minutes before sealing. Priced 30%.
# The class recurred within 24 hours of being logged (board #2's "keyed hit
# whose condition was already true at issue"). This gate kills the class at
# generation instead of logging its instances.
#
# SCOPE (v1, stated honestly). Two mechanically-stated packet sources:
#   1. CISA KEV section entries:  "**CVE-YYYY-NNNNN** ... (added YYYY-MM-DD)"
#      - dateAdded already inside the row's window  -> REJECT_SATISFIED
#      - dateAdded already BEFORE the row's window  -> REJECT_FORECLOSED
#        (dateAdded is single-valued; the only path to a fresh in-window
#        value is removal-and-relisting. Removals are documented -- CISA
#        removed CVE-2022-28958 on 2023-12-01 after NVD revoked it -- but
#        no removal-and-relist producing a new dateAdded has a documented
#        precedent. The reject reason prints that caveat.)
#   2. Earthquake items (USGS "M x.x - ... , Country" lines and GDACS
#      "(Magnitude x.xM, Depth:ykm) in Country DD/MM/YYYY" lines):
#      - a packet quake meeting ALL of the row's parsed predicates
#        (magnitude floor, depth ceiling, country) with its event date
#        inside the row's window -> REJECT_SATISFIED
#      - no foreclosure direction exists for quakes (one can still occur).
# Everything else: PASS. Market prints and other feeds are v2.
#
# FAILURE POSTURE: fail OPEN. Any parse ambiguity -> PASS with a printed
# NOTE, never a rejection. A gate that rejects live forecasts on parse
# errors punishes the careful arm; a gate that misses a foreclosure is the
# status quo. Asymmetric by design.
#
# INTEGRATION (two hook points, unified since KK21c):
#   from foreclose_check import check_row
#   verdict, reason = check_row(row, packet_text)
#   if verdict.startswith("REJECT"): treat as a gate rejection, print reason
#   if verdict == "NOTE":            seal, but print the note in the report
# Hook wherever the citation gate runs for both cmd_generate and --ingest.
#
# CLI:
#   python foreclose_check.py --packet kkr_packet_X.md --projections raw.json
#   python foreclose_check.py --selftest
#
# Windows-safe: stdlib only, ASCII output.

import argparse
import json
import re
import sys
from datetime import date

REASON = ("the packet already decides this claim; "
          "a forecast must be open at seal")

DATE_ISO = r"(\d{4}-\d{2}-\d{2})"

# ---------------------------------------------------------------- packet side

KEV_LINE = re.compile(
    r"\*\*(CVE-\d{4}-\d{4,7})\*\*.*?\(added\s+" + DATE_ISO + r"\)",
    re.IGNORECASE)

USGS_LINE = re.compile(
    r"\bM\s+(\d+(?:\.\d+)?)\s*-\s*(?:[^,\n]*?,\s*)?([A-Za-z][A-Za-z .'-]+?)"
    r"(?:\s*\u00b7|\s*$)",
    re.MULTILINE)

GDACS_LINE = re.compile(
    r"Magnitude\s+(\d+(?:\.\d+)?)M,\s*Depth:\s*(\d+(?:\.\d+)?)\s*km\)\s*"
    r"in\s+([A-Za-z][A-Za-z .'-]+?)\s+(\d{2})/(\d{2})/(\d{4})",
    re.IGNORECASE)


def parse_kev(packet_text):
    """CVE id -> dateAdded (ISO string) as stated by the packet."""
    return {cve.upper(): added for cve, added in KEV_LINE.findall(packet_text)}


def parse_quakes(packet_text):
    """List of quake dicts parsed from packet item lines.

    GDACS lines carry magnitude, depth, country, and event date -- complete.
    USGS lines carry magnitude and place only; depth and date are NOT parsed
    from them, so a USGS-only event can satisfy a row only if the row states
    no depth predicate (fail-open principle: an unparsed field never counts
    AGAINST a match requirement -- it only means the requirement cannot be
    confirmed, hence no rejection on that event).
    """
    quakes = []
    for mag, depth, country, dd, mm, yyyy in GDACS_LINE.findall(packet_text):
        try:
            evdate = date(int(yyyy), int(mm), int(dd)).isoformat()
        except ValueError:
            continue
        quakes.append({"mag": float(mag), "depth": float(depth),
                       "country": country.strip().lower(), "date": evdate,
                       "src": "gdacs"})
    for mag, place in USGS_LINE.findall(packet_text):
        quakes.append({"mag": float(mag), "depth": None,
                       "country": place.strip().lower(), "date": None,
                       "src": "usgs"})
    return quakes

# ------------------------------------------------------------------- row side

WINDOW = re.compile(r"between\s+" + DATE_ISO + r"\s+and\s+" + DATE_ISO,
                    re.IGNORECASE)
CVE_ID = re.compile(r"(CVE-\d{4}-\d{4,7})", re.IGNORECASE)
MAG_FLOOR = re.compile(r"magnitude\s+(\d+(?:\.\d+)?)\s+or\s+greater",
                       re.IGNORECASE)
DEPTH_CEIL = re.compile(r"depth\s+of\s+less\s+than\s+(\d+(?:\.\d+)?)\s*km",
                        re.IGNORECASE)


def row_text(row):
    return " ".join(str(row.get(k, "")) for k in
                    ("statement", "resolution", "failure_condition"))


def parse_window(row):
    """Earliest window stated on the row (statement or resolution)."""
    m = WINDOW.search(row_text(row))
    return (m.group(1), m.group(2)) if m else None

# ---------------------------------------------------------------------- gate


def check_row(row, packet_text, kev=None, quakes=None, items=None):
    """Return (verdict, reason). Verdicts:
    PASS | NOTE | REJECT_SATISFIED | REJECT_FORECLOSED
    """
    kev = parse_kev(packet_text) if kev is None else kev
    quakes = parse_quakes(packet_text) if quakes is None else quakes
    items = parse_packet_items(packet_text) if items is None else items
    text = row_text(row)
    win = parse_window(row)

    # ---- KEV direction -----------------------------------------------------
    cves = {c.upper() for c in CVE_ID.findall(text)}
    low = text.lower()
    # v1.1: bare "KEV" is NOT enough -- a KEV claim about a non-dateAdded
    # field (ransomware flag, product field) must not trip the dateAdded
    # foreclosure. Caught live 2026-08-05 on a sonnet-5 row.
    kev_claim = ("date-added" in low or "dateadded" in low)
    if cves and kev_claim:
        if win is None:
            return ("NOTE", "KEV-shaped claim but no parseable "
                    "'between A and B' window; gate cannot test it "
                    "(fail-open)")
        lo, hi = win
        for cve in cves:
            added = kev.get(cve)
            if added is None:
                continue  # packet does not decide this CVE
            if lo <= added <= hi:
                return ("REJECT_SATISFIED",
                        REASON + " -- the packet states %s dateAdded %s, "
                        "already inside the claimed window %s..%s"
                        % (cve, added, lo, hi))
            if added < lo:
                return ("REJECT_FORECLOSED",
                        REASON + " -- the packet states %s dateAdded %s, "
                        "before the claimed window %s..%s; dateAdded is "
                        "single-valued and a fresh in-window value would "
                        "require removal-and-relisting, which has no "
                        "documented precedent (removals exist: "
                        "CVE-2022-28958, removed 2023-12-01)"
                        % (cve, added, lo, hi))

    # ---- quake direction (satisfied only) ----------------------------------
    mfl = MAG_FLOOR.search(text)
    if mfl and win:
        floor = float(mfl.group(1))
        dce = DEPTH_CEIL.search(text)
        ceil = float(dce.group(1)) if dce else None
        lo, hi = win
        for q in quakes:
            if q["mag"] < floor:
                continue
            if ceil is not None:
                if q["depth"] is None:
                    continue  # unparsed depth never satisfies a depth claim
                if q["depth"] >= ceil:
                    continue
            worldwide = re.search(r"anywhere in the world|globally|"
                                  r"worldwide", text, re.IGNORECASE)
            if not worldwide and q["country"] not in text.lower():
                continue
            if q["date"] is None or not (lo <= q["date"] <= hi):
                continue
            return ("REJECT_SATISFIED",
                    REASON + " -- the packet carries a %s M%.1f depth "
                    "%skm quake in %s dated %s, inside the claimed window "
                    "%s..%s"
                    % (q["src"].upper(), q["mag"],
                       ("%.0f" % q["depth"]) if q["depth"] is not None
                       else "?", q["country"].title(), q["date"], lo, hi))

    echo = check_citation_echo(row, items)
    if echo:
        return echo

    return ("PASS", "")



# ---- v1.1 citation-echo: cited item already reports the asserted toll ----

ITEM_LINE = re.compile(r"^\s*(\d+)\.\s+(.*)$", re.MULTILINE)
ITEM_DATE = re.compile(r"(\d{2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|"
                       r"Oct|Nov|Dec)\s+\d{2}:\d{2}\s*UTC", re.IGNORECASE)
MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun",
     "jul", "aug", "sep", "oct", "nov", "dec"])}
KILL_NUM = [re.compile(p, re.IGNORECASE) for p in (
    r"kill(?:s|ed)?[-\s](?:at[-\s]least[-\s])?(\d+)",
    r"at[-\s]least[-\s](\d+)[-\s](?:killed|dead|people)",
    r"(\d+)[-\s](?:people[-\s])?(?:killed|dead)")]
ROW_TOLL = [re.compile(p, re.IGNORECASE) for p in (
    r"kill(?:s|ed)?\s+(\d+)\s+or\s+more",
    r"kill(?:s|ed)?\s+at\s+least\s+(\d+)",
    r"(\d+)\s+or\s+more\s+people")]


def parse_packet_items(packet_text):
    """index -> (line_text, iso_date_or_None). Year taken from the first
    ISO date appearing in the packet; falls back to 2026."""
    ym = re.search(r"\b(20\d\d)-\d\d-\d\d", packet_text)
    year = int(ym.group(1)) if ym else 2026
    items = {}
    for num, line in ITEM_LINE.findall(packet_text):
        dm = ITEM_DATE.search(line)
        iso = None
        if dm:
            iso = date(year, MONTHS[dm.group(2).lower()],
                       int(dm.group(1))).isoformat()
        items[int(num)] = (line, iso)
    return items


def max_num(patterns, text):
    vals = [int(g) for p in patterns for g in p.findall(text)]
    return max(vals) if vals else None


def check_citation_echo(row, items):
    """REJECT_SATISFIED if a packet item the row itself cites already
    reports a death toll >= the row's threshold, dated inside the row's
    window. Conservative: only the row's OWN citations are checked --
    citing the deciding item is the smoking gun. Fail-open otherwise."""
    text = row_text(row)
    toll = max_num(ROW_TOLL, text)
    win = parse_window(row)
    if toll is None or win is None:
        return None
    lo, hi = win
    for c in (row.get("citations") or []):
        try:
            line, iso = items.get(int(c), (None, None))
        except (TypeError, ValueError):
            continue
        if not line or not iso or not (lo <= iso <= hi):
            continue
        reported = max_num(KILL_NUM, line)
        if reported is not None and reported >= toll:
            return ("REJECT_SATISFIED",
                    REASON + " -- the row's own citation [%s], dated %s "
                    "inside the claimed window %s..%s, already reports "
                    "%d killed against the row's threshold of %d"
                    % (c, iso, lo, hi, reported, toll))
    return None

# ------------------------------------------------------------------ selftest


SELFTEST_PACKET = """
83. [B3] Zelenskyy calls for more air defences as Russian attack on ... \
Guardian World (single-source) - 05 Aug 13:47 UTC - \
[link](https://example.org/2026/aug/05/russia-kyiv-attack-kills-at-least-14-people)
## VIII. CISA KEV -- NEWLY CATALOGUED EXPLOITED VULNERABILITIES
- **CVE-2026-9198** -- IBM Langflow: IBM Langflow Code Injection \
Vulnerability (added 2026-08-04). Langflow contains a code injection \
vulnerability.
43. [B3] Green earthquake (Magnitude 6.3M, Depth:10km) in Philippines \
05/08/2026 04:14 UTC
"""

SELFTEST_ROWS = [
    {"id": "T-FORECLOSED",
     "statement": "The CISA KEV catalog includes CVE-2026-9198 as actively "
                  "exploited between 2026-08-05 and 2026-08-12.",
     "resolution": "The CISA KEV catalog carries a date-added value between "
                   "2026-08-05 and 2026-08-12 for CVE-2026-9198.",
     "expect": "REJECT_FORECLOSED"},
    {"id": "T-SATISFIED",
     "statement": "A magnitude 6.0 or greater earthquake with a depth of "
                  "less than 100km occurs in the Philippines between "
                  "2026-08-05 and 2026-08-12.",
     "resolution": "The USGS Significant Quakes feed reports a magnitude "
                   "6.0 or greater earthquake with a depth of less than "
                   "100km in the Philippines between 2026-08-05 and "
                   "2026-08-12.",
     "expect": "REJECT_SATISFIED"},
    {"id": "T-ECHO-SATISFIED",
     "statement": "Between 2026-08-05 and 2026-08-19, Russia will conduct "
                  "a strike on Kyiv that killed 10 or more people in that "
                  "single strike.",
     "resolution": "True if reported between 2026-08-05 and 2026-08-21.",
     "citations": [83],
     "expect": "REJECT_SATISFIED"},
    {"id": "T-ECHO-WINDOW-OPEN",
     "statement": "A strike on Kyiv between 2026-08-06 and 2026-09-15 "
                  "kills 10 or more people.",
     "resolution": "Official toll of 10 or more in the window "
                   "between 2026-08-06 and 2026-09-15.",
     "citations": [83],
     "expect": "PASS"},
    {"id": "T-KEV-FIELD-NOT-DATEADDED",
     "statement": "Between 2026-08-05 and 2026-09-19 the KEV catalog "
                  "changes the ransomware field for CVE-2026-9198 to "
                  "Known.",
     "resolution": "KEV page for CVE-2026-9198 shows the field as Known.",
     "expect": "PASS"},
    {"id": "T-OPEN",
     "statement": "A magnitude 7.5 or greater earthquake with a depth of "
                  "less than 50km occurs in Chile between 2026-08-05 and "
                  "2026-08-12.",
     "resolution": "The USGS Significant Quakes feed reports it.",
     "expect": "PASS"},
]


def selftest():
    fails = 0
    for r in SELFTEST_ROWS:
        v, reason = check_row(r, SELFTEST_PACKET)
        ok = (v == r["expect"])
        print("[%s] %s -> %s%s" % ("ok" if ok else "FAIL", r["id"], v,
                                   ("  (%s)" % reason) if reason else ""))
        fails += 0 if ok else 1
    sys.exit(1 if fails else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--packet")
    ap.add_argument("--projections")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
        return
    if not (a.packet and a.projections):
        ap.error("--packet and --projections required (or --selftest)")
    packet_text = open(a.packet, encoding="utf-8", errors="replace").read()
    raw = open(a.projections, encoding="utf-8", errors="replace").read()
    fenced = re.search(r"```(?:json)?\s*(\[.*\])\s*```", raw, re.DOTALL)
    rows = json.loads(fenced.group(1) if fenced else raw)
    kev, quakes = parse_kev(packet_text), parse_quakes(packet_text)
    items = parse_packet_items(packet_text)
    counts = {}
    for i, row in enumerate(rows):
        v, reason = check_row(row, packet_text, kev, quakes, items)
        counts[v] = counts.get(v, 0) + 1
        tag = row.get("id") or ("row %d" % i)
        line = "%-18s %s" % (v, tag)
        if reason:
            line += "\n    " + reason
        print(line)
    print("\nsummary:", " ".join("%s=%d" % kv for kv in sorted(counts.items())))


if __name__ == "__main__":
    main()
