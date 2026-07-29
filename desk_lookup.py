#!/usr/bin/env python3
"""
desk_lookup.py - reproducible lookups for resolving sealed rows.

WHAT IT DOES NOT DO

It does not resolve anything. It writes no file, touches no ledger, and
proposes no verdict it can act on. It fetches a published number at a named
date and prints it with the query that produced it, so the operator
adjudicates against evidence a stranger can re-fetch.

That division is deliberate. The colophon says resolution and publication are
the operator's. A tool that writes a verdict into a permanent record from a
field it parsed wrong is worse than the manual work it saves - and every
source below was probed, two of them returned HTML shells that a lazy content
check scored as passing, and one returns real data for the wrong instrument.
The lookup is mechanical. The judgement stays yours.

SOURCES - ALL KEYLESS, ALL PROBED

  treasury  US Treasury daily par yield curve, XML
            PROBED PASS: 221KB, BC_10YEAR and NEW_DATE present
            serves the 10-year yield rows

  kev       CISA Known Exploited Vulnerabilities catalog, JSON
            PROBED PASS: 1.5MB, catalogVersion 2026.07.27, dateAdded present
            serves the "CISA adds X to KEV" rows

  quake     USGS FDSN event query, GeoJSON, date-ranged
            PROBED PASS: returns FeatureCollection for a bounded query
            serves the magnitude rows. NOTE: USGS does not carry a fatality
            field, so any row requiring "with at least one fatality" is only
            PARTIALLY served - the magnitude and location resolve here, the
            fatality does not.

WHAT IS NOT HERE, AND WHY

  stooq     BLOCKED. Returns a JavaScript bot challenge to programmatic
            clients. Index and oil settlements have no keyless source, which
            leaves the S&P, Nasdaq, Brent and WTI rows hand-adjudicated.
  effis     HTML shell of a JavaScript app, not an API.
  hhs       JSF page, not machine-queryable.
  fed funds NY Fed serves EFFR, the realised rate. The rows name the FOMC
            target upper bound. Right host, wrong instrument.
  FRED      needs an API key. No key is added to this repo.

    python desk_lookup.py treasury --date 2026-07-29
    python desk_lookup.py treasury --from 2026-07-01 --to 2026-07-29 --above 4.80
    python desk_lookup.py kev --cve CVE-2026-16812
    python desk_lookup.py kev --since 2026-07-28 --match fastjson,gitlab
    python desk_lookup.py quake --from 2026-08-02 --to 2027-01-15 --minmag 4.5 \\
        --lat 36.19 --lon -101.19 --radius 100

Standard library only. ASCII-only output. Writes nothing.
"""

import argparse
import datetime as dt
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) desk_lookup/1.0 "
      "(+https://retroprescientaudit.com)")
TIMEOUT = 30

TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/"
            "interest-rates/pages/xml?data=daily_treasury_yield_curve"
            "&field_tdr_date_value=%s")
KEV = ("https://www.cisa.gov/sites/default/files/feeds/"
       "known_exploited_vulnerabilities.json")
USGS = "https://earthquake.usgs.gov/fdsnws/event/1/query"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        print("FETCH FAILED - HTTP %s %s" % (e.code, e.reason), file=sys.stderr)
        if e.code in (403, 406):
            print("  the edge rejected a programmatic client. This is a "
                  "source-side decision, not a bug here.", file=sys.stderr)
        return None
    except Exception as e:
        print("FETCH FAILED - %s: %s" % (type(e).__name__, e), file=sys.stderr)
        return None


def cite(url):
    print("")
    print("  query   : %s" % url)
    print("  fetched : %sZ" % dt.datetime.now(dt.timezone.utc)
          .strftime("%Y-%m-%dT%H:%M:%S"))
    print("  Paste the query into the resolution_basis. A resolution nobody")
    print("  can re-run is an assertion, not a resolution.")
    print("")


# ------------------------------------------------------------------ treasury
def cmd_treasury(a):
    years = sorted({d[:4] for d in filter(None, [a.date, getattr(a, "frm", None),
                                                 a.to]) if d})
    if not years:
        years = [str(dt.date.today().year)]
    rows = []
    for y in years:
        url = TREASURY % y
        body = fetch(url)
        if body is None:
            return 1
        text = body.decode("utf-8", errors="replace")
        # Atom entries carry m:properties with d:NEW_DATE and d:BC_10YEAR
        for ent in re.findall(r"<entry>.*?</entry>", text, re.S):
            dm = re.search(r"<d:NEW_DATE[^>]*>([^<]+)<", ent)
            ym = re.search(r"<d:BC_10YEAR[^>]*>([^<]+)<", ent)
            if dm and ym:
                rows.append((dm.group(1)[:10], float(ym.group(1))))
        last_url = url
    rows.sort()
    if not rows:
        print("NO ROWS PARSED - the XML shape may have changed. Nothing is "
              "asserted.", file=sys.stderr)
        return 1

    sel = rows
    if a.date:
        sel = [r for r in rows if r[0] == a.date]
    else:
        if getattr(a, "frm", None):
            sel = [r for r in sel if r[0] >= a.frm]
        if a.to:
            sel = [r for r in sel if r[0] <= a.to]

    print("")
    print("US TREASURY - daily par yield curve, 10-year")
    print("-" * 68)
    if not sel:
        print("  no published value for that date or window.")
        print("  Treasury posts after the close, so a same-day query before")
        print("  roughly 18:00Z returns nothing yet - wait, do not resolve.")
        print("  A weekend or holiday deadline has no value at all, and that")
        print("  is a row defect rather than a lookup failure.")
    for d, v in sel:
        mark = ""
        if a.above is not None:
            mark = "  ABOVE %.2f" % a.above if v > a.above else "  at or below %.2f" % a.above
        print("  %s  %5.2f%%%s" % (d, v, mark))
    if a.above is not None and sel:
        hits = [d for d, v in sel if v > a.above]
        print("")
        print("  %d of %d business day(s) closed above %.2f%%"
              % (len(hits), len(sel), a.above))
        if hits:
            print("  first: %s   last: %s" % (hits[0], hits[-1]))
    print("  %d business day(s) in range, %d total parsed for the year(s)"
          % (len(sel), len(rows)))
    cite(last_url)
    return 0


# ----------------------------------------------------------------------- kev
def cmd_kev(a):
    body = fetch(KEV)
    if body is None:
        return 1
    d = json.loads(body.decode("utf-8"))
    vulns = d.get("vulnerabilities", [])
    print("")
    print("CISA KEV CATALOG")
    print("-" * 68)
    print("  catalogVersion %s . dateReleased %s . %d entries"
          % (d.get("catalogVersion", "?"), d.get("dateReleased", "?")[:10],
             len(vulns)))

    sel = vulns
    if a.cve:
        want = a.cve.upper()
        sel = [v for v in sel if v.get("cveID", "").upper() == want]
        if not sel:
            print("")
            print("  %s is NOT in the catalog as of the version above." % want)
            print("  For a row claiming CISA adds it by a deadline, absence")
            print("  today is not a MISS until the deadline passes.")
            cite(KEV)
            return 0
    if a.since:
        sel = [v for v in sel if v.get("dateAdded", "") >= a.since]
    if a.until:
        sel = [v for v in sel if v.get("dateAdded", "") <= a.until]
    if a.match:
        terms = [t.strip().lower() for t in a.match.split(",") if t.strip()]
        sel = [v for v in sel
               if any(t in json.dumps(v).lower() for t in terms)]

    print("  %d entr(ies) match" % len(sel))
    print("")
    for v in sorted(sel, key=lambda x: x.get("dateAdded", ""))[:40]:
        print("  %s  %-18s %s / %s"
              % (v.get("dateAdded", "?"), v.get("cveID", "?"),
                 v.get("vendorProject", "?")[:20], v.get("product", "?")[:24]))
        if a.verbose:
            print("      %s" % v.get("vulnerabilityName", "")[:96])
    if len(sel) > 40:
        print("  ... %d more not shown" % (len(sel) - 40))
    cite(KEV)
    return 0


# --------------------------------------------------------------------- quake
def cmd_quake(a):
    q = {"format": "geojson", "orderby": "time"}
    if getattr(a, "frm", None):
        q["starttime"] = a.frm
    if a.to:
        q["endtime"] = a.to
    if a.minmag is not None:
        q["minmagnitude"] = a.minmag
    if a.lat is not None and a.lon is not None:
        q["latitude"] = a.lat
        q["longitude"] = a.lon
        q["maxradiuskm"] = a.radius if a.radius else 100
    for k, v in (("minlatitude", a.minlat), ("maxlatitude", a.maxlat),
                 ("minlongitude", a.minlon), ("maxlongitude", a.maxlon)):
        if v is not None:
            q[k] = v
    url = USGS + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    d = json.loads(body.decode("utf-8"))
    feats = d.get("features", [])
    print("")
    print("USGS FDSN EVENT QUERY")
    print("-" * 68)
    print("  %d event(s)" % len(feats))
    print("")
    for f in feats[:40]:
        p = f.get("properties", {})
        t = p.get("time")
        when = (dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc)
                .strftime("%Y-%m-%d %H:%M") if t else "?")
        print("  %s  M%-4s %s" % (when, p.get("mag", "?"),
                                  str(p.get("place", ""))[:52]))
    if len(feats) > 40:
        print("  ... %d more not shown" % (len(feats) - 40))
    print("")
    print("  USGS carries no fatality field. A row requiring a death toll is")
    print("  only PARTIALLY served here: magnitude, place and time resolve;")
    print("  the fatality does not, and needs a separate cited source.")
    cite(url)
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="keyless lookups for resolving sealed rows. Writes nothing.")
    sub = ap.add_subparsers(dest="cmd")

    t = sub.add_parser("treasury", help="10-year par yield at a date or window")
    t.add_argument("--date")
    t.add_argument("--from", dest="frm")
    t.add_argument("--to")
    t.add_argument("--above", type=float, help="flag closes above this percent")

    k = sub.add_parser("kev", help="CISA Known Exploited Vulnerabilities")
    k.add_argument("--cve")
    k.add_argument("--since", help="dateAdded >= YYYY-MM-DD")
    k.add_argument("--until", help="dateAdded <= YYYY-MM-DD")
    k.add_argument("--match", help="comma-separated substrings, any match")
    k.add_argument("--verbose", action="store_true")

    q = sub.add_parser("quake", help="USGS events in a window and area")
    q.add_argument("--from", dest="frm")
    q.add_argument("--to")
    q.add_argument("--minmag", type=float)
    q.add_argument("--lat", type=float)
    q.add_argument("--lon", type=float)
    q.add_argument("--radius", type=float, help="km, default 100 with lat/lon")
    q.add_argument("--minlat", type=float)
    q.add_argument("--maxlat", type=float)
    q.add_argument("--minlon", type=float)
    q.add_argument("--maxlon", type=float)

    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return 0
    return {"treasury": cmd_treasury, "kev": cmd_kev, "quake": cmd_quake}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
