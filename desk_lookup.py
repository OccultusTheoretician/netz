#!/usr/bin/env python3
"""
desk_lookup.py - reproducible lookups for resolving sealed rows. v1.2

WHAT IT DOES NOT DO

It does not resolve anything. It writes no file, touches no ledger, and
proposes no verdict it can act on. It fetches a published value at a named
date and prints it with the query that produced it, so the operator
adjudicates against evidence a stranger can re-fetch.

Across three probe rounds: two endpoints returned HTML shells that a lazy
content check scored as passing, one returned real data for the WRONG
INSTRUMENT, one is behind a bot challenge, and one wants an API key. The
lookup is mechanical. The judgement stays yours.

SOURCES - ALL KEYLESS, ALL PROBED

  treasury  US Treasury daily par yield curve, XML         PASS
  kev       CISA Known Exploited Vulnerabilities, JSON     PASS
  nvd       NIST CVE API 2.0 - severity, not catalogue     PASS
  quake     USGS FDSN event query, GeoJSON                 PASS
  gdacs     GDACS alerts - carries death tolls             PASS
  eonet     NASA EONET natural events                      PASS
  fema      OpenFEMA disaster declarations                 PASS
  fedreg    Federal Register documents API                 PASS
  ecb       ECB Data Portal, CSV                           PASS
  wire      GDELT article search + two-of-N outlet test    PASS
  wiki      Wikipedia page HTML                            see below

NOT HERE, AND WHY

  stooq     JavaScript bot challenge. Index and oil settlements have no
            keyless source - S&P, Nasdaq, Brent and WTI stay hand-adjudicated.
            This is the largest unresolved class on the book.
  UCDP      HTTP 401. The best conflict-event source available and it needs
            auth, so the military/conflict rows keep the `wire` test as their
            only mechanical basis.
  effis     JavaScript app, not an API.
  hhs       JSF page, not machine-queryable.
  wikidata  The SPARQL endpoint WORKS. The probe query returned zero bindings
            because the QID or property was wrong, not because the service
            failed. Worth adding once the right property for a military
            formation's commander is identified - it would beat `wiki`
            outright, since a rename, redirect or restructure all produce a
            false ABSENT under string matching and none touch a structured
            claim.
  fed funds NY Fed serves EFFR, the realised rate. The rows name the FOMC
            target upper bound. Right host, wrong instrument.
  FRED, N2YO, ACLED, NASA FIRMS, Congress.gov - all want a key. None is added.
            Every source in report_config.json is keyless, which is why that
            file sits tracked in a public repo, and publish.bat runs
            `git add -A`.

    python desk_lookup.py wire --query "iran strike" --days 7
    python desk_lookup.py wire --query "iran strike" --days 7 --outlets reuters.com,apnews.com,bbc.co.uk --threshold 2
    python desk_lookup.py nvd --cve CVE-2026-60137
    python desk_lookup.py fema --state CA --type Fire --since 2026-07-01
    python desk_lookup.py eonet --category wildfires --days 30

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

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) desk_lookup/1.2 "
      "(+https://retroprescientaudit.com)")
TIMEOUT = 30

TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/"
            "interest-rates/pages/xml?data=daily_treasury_yield_curve"
            "&field_tdr_date_value=%s")
KEV = ("https://www.cisa.gov/sites/default/files/feeds/"
       "known_exploited_vulnerabilities.json")
NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
USGS = "https://earthquake.usgs.gov/fdsnws/event/1/query"
GDACS = "https://www.gdacs.org/xml/rss.xml"
EONET = "https://eonet.gsfc.nasa.gov/api/v3/events"
FEMA = "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
FEDREG = "https://www.federalregister.gov/api/v1/documents.json"
ECB = ("https://data-api.ecb.europa.eu/service/data/FM/"
       "D.U2.EUR.4F.KR.MRR_FR.LEV?format=csvdata&lastNObservations=%d")
GDELT = "https://api.gdeltproject.org/api/v2/doc/doc"
WIKI = "https://en.wikipedia.org/api/rest_v1/page/html/%s"

# The wire services rows on this book actually name.
DEFAULT_OUTLETS = "reuters.com,apnews.com,bbc.co.uk,bbc.com,aljazeera.com"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        print("FETCH FAILED - HTTP %s %s" % (e.code, e.reason), file=sys.stderr)
        if e.code in (401, 403, 406):
            print("  the source rejected this client. Source-side decision.",
                  file=sys.stderr)
        if e.code == 429:
            print("  rate limited, not rejected. Wait and retry.", file=sys.stderr)
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


def strip_tags(html):
    html = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = (html.replace("&nbsp;", " ").replace("&amp;", "&")
            .replace("&lt;", "<").replace("&gt;", ">").replace("&#160;", " "))
    return re.sub(r"\s+", " ", html)


def ascii_only(s, n=90):
    return "".join(c if 32 <= ord(c) < 127 else "." for c in str(s))[:n]


# ---------------------------------------------------------------- wire test
def cmd_wire(a):
    """GDELT article search with an explicit two-of-N outlet test.

    This is the only mechanical basis on the desk for rows phrased 'reported
    by at least two of Reuters, the Associated Press and the BBC'. UCDP would
    have been better for the underlying events and returns 401.
    """
    q = {"query": a.query, "mode": "artlist", "format": "json",
         "maxrecords": str(min(a.max or 100, 250)),
         "timespan": "%dd" % (a.days or 7)}
    url = GDELT + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    try:
        arts = json.loads(body.decode("utf-8", errors="replace")).get("articles", [])
    except Exception as e:
        print("PARSE FAILED - %s. GDELT returned non-JSON; nothing asserted."
              % e, file=sys.stderr)
        return 1

    outlets = [o.strip().lower() for o in
               (a.outlets or DEFAULT_OUTLETS).split(",") if o.strip()]
    thresh = a.threshold or 2

    hits = {}
    for art in arts:
        dom = str(art.get("domain", "")).lower()
        for o in outlets:
            if dom == o or dom.endswith("." + o):
                hits.setdefault(o, []).append(art)

    print("")
    print("GDELT WIRE TEST")
    print("-" * 68)
    print("  query    : %s" % a.query)
    print("  window   : last %d day(s)" % (a.days or 7))
    print("  articles : %d returned" % len(arts))
    print("  outlets  : %s" % ", ".join(outlets))
    print("  threshold: %d" % thresh)
    print("")

    # BBC has two domains; count them as one outlet for the test.
    families = {}
    for o in hits:
        fam = "bbc" if o.startswith("bbc.") else o
        families.setdefault(fam, []).extend(hits[o])

    for fam in sorted(families):
        arts_f = families[fam]
        print("  COVERED  %-16s %d article(s)" % (fam, len(arts_f)))
        for art in arts_f[:3]:
            print("           %s  %s"
                  % (str(art.get("seendate", "?"))[:8],
                     ascii_only(art.get("title", ""), 62)))
    missing = [o for o in outlets
               if ("bbc" if o.startswith("bbc.") else o) not in families]
    for o in missing:
        print("  absent   %s" % o)

    n = len(families)
    print("")
    print("  %d of %d named outlet(s) covered this in the window."
          % (n, len({"bbc" if o.startswith("bbc.") else o for o in outlets})))
    print("  Threshold %d: %s" % (thresh, "MET" if n >= thresh else "NOT MET"))
    print("")
    print("  READ THE ROW BEFORE RULING. GDELT indexes what it indexes; an")
    print("  absent outlet may have covered the event under wording this query")
    print("  does not match. Absence here is weaker evidence than presence.")
    print("  Widen the query and re-run before recording a MISS on it.")
    cite(url)
    return 0


# ----------------------------------------------------------------------- nvd
def cmd_nvd(a):
    q = {}
    if a.cve:
        q["cveId"] = a.cve.upper()
    else:
        q["resultsPerPage"] = str(min(a.limit or 20, 100))
        if a.keyword:
            q["keywordSearch"] = a.keyword
        if getattr(a, "frm", None):
            q["pubStartDate"] = a.frm + "T00:00:00.000"
            q["pubEndDate"] = (a.to or dt.date.today().isoformat()) + "T23:59:59.999"
    url = NVD + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    d = json.loads(body.decode("utf-8", errors="replace"))
    vulns = d.get("vulnerabilities", [])
    print("")
    print("NIST NVD - CVE RECORDS")
    print("-" * 68)
    print("  %s total result(s), showing %d" % (d.get("totalResults", "?"),
                                                len(vulns)))
    print("")
    for v in vulns[:25]:
        c = v.get("cve", {})
        sev = base = "-"
        metrics = c.get("metrics", {})
        for k in ("cvssMetricV31", "cvssMetricV40", "cvssMetricV30"):
            if metrics.get(k):
                cd = metrics[k][0].get("cvssData", {})
                base = cd.get("baseScore", "-")
                sev = cd.get("baseSeverity", "-")
                break
        desc = ""
        for dsc in c.get("descriptions", []):
            if dsc.get("lang") == "en":
                desc = dsc.get("value", "")
                break
        print("  %-18s %-9s %-5s %s" % (c.get("id", "?"), sev, base,
                                        ascii_only(desc, 40)))
        if a.verbose:
            print("      published %s  modified %s"
                  % (str(c.get("published", "?"))[:10],
                     str(c.get("lastModified", "?"))[:10]))
    print("")
    print("  NVD gives SEVERITY. KEV gives whether CISA catalogued it as")
    print("  exploited. A row naming a CVSS threshold resolves here; a row")
    print("  naming KEV resolves there. They are not interchangeable.")
    print("  Rate limit without a key is 5 requests per 30 seconds.")
    cite(url)
    return 0


# ---------------------------------------------------------------------- fema
def cmd_fema(a):
    filters = []
    if a.state:
        filters.append("state eq '%s'" % a.state.upper())
    if a.type:
        filters.append("incidentType eq '%s'" % a.type)
    if getattr(a, "frm", None):
        filters.append("declarationDate ge '%sT00:00:00.000z'" % a.frm)
    if a.to:
        filters.append("declarationDate le '%sT23:59:59.999z'" % a.to)
    q = [("$top", str(min(a.limit or 20, 100))),
         ("$orderby", "declarationDate desc")]
    if filters:
        q.append(("$filter", " and ".join(filters)))
    url = FEMA + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    d = json.loads(body.decode("utf-8", errors="replace"))
    rows = d.get("DisasterDeclarationsSummaries", [])
    print("")
    print("OPENFEMA - DISASTER DECLARATIONS")
    print("-" * 68)
    print("  %d record(s)" % len(rows))
    print("")
    for r in rows[:30]:
        print("  %s  %-6s %-18s %s"
              % (str(r.get("declarationDate", "?"))[:10],
                 r.get("state", "?"), str(r.get("incidentType", ""))[:18],
                 ascii_only(r.get("declarationTitle", ""), 34)))
    print("")
    print("  A declaration is a dated administrative fact, which is the")
    print("  cleanest resolution basis available. US only - a row about")
    print("  France or Spain cannot be settled here.")
    cite(url)
    return 0


# --------------------------------------------------------------------- eonet
def cmd_eonet(a):
    q = {"limit": str(min(a.limit or 30, 200))}
    if a.days:
        q["days"] = str(a.days)
    if a.category:
        q["category"] = a.category
    if a.status:
        q["status"] = a.status
    url = EONET + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    # NASA serves this as application/rss+xml while the body is JSON.
    # Do not trust the content-type header here.
    try:
        d = json.loads(body.decode("utf-8", errors="replace"))
    except Exception as e:
        print("PARSE FAILED - %s. Note EONET mislabels JSON as rss+xml; if the"
              " body is genuinely XML the API has changed." % e, file=sys.stderr)
        return 1
    evs = d.get("events", [])
    print("")
    print("NASA EONET - NATURAL EVENTS")
    print("-" * 68)
    print("  %d event(s)" % len(evs))
    print("")
    for e in evs[:30]:
        cats = ", ".join(c.get("title", "") for c in e.get("categories", []))
        geo = e.get("geometry") or []
        when = str(geo[0].get("date", "?"))[:10] if geo else "?"
        print("  %s  %-14s %s" % (when, cats[:14], ascii_only(e.get("title", ""), 42)))
    print("")
    print("  EONET catalogues that an event occurred. It does not carry")
    print("  hectares burned, death tolls, or evacuation counts - a row")
    print("  naming any of those is only partly served here.")
    cite(url)
    return 0


# ------------------------------------------------------------------ treasury
def cmd_treasury(a):
    years = sorted({d[:4] for d in
                    [a.date, getattr(a, "frm", None), a.to] if d})
    if not years:
        years = [str(dt.date.today().year)]
    rows, last_url = [], None
    for y in years:
        last_url = TREASURY % y
        body = fetch(last_url)
        if body is None:
            return 1
        text = body.decode("utf-8", errors="replace")
        for ent in re.findall(r"<entry>.*?</entry>", text, re.S):
            dm = re.search(r"<d:NEW_DATE[^>]*>([^<]+)<", ent)
            ym = re.search(r"<d:BC_10YEAR[^>]*>([^<]+)<", ent)
            if dm and ym:
                rows.append((dm.group(1)[:10], float(ym.group(1))))
    rows.sort()
    if not rows:
        print("NO ROWS PARSED - the XML shape may have changed.", file=sys.stderr)
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
            mark = ("  ABOVE %.2f" % a.above if v > a.above
                    else "  at or below %.2f" % a.above)
        print("  %s  %5.2f%%%s" % (d, v, mark))
    if a.above is not None and sel:
        h = [d for d, v in sel if v > a.above]
        print("")
        print("  %d of %d business day(s) closed above %.2f%%"
              % (len(h), len(sel), a.above))
        if h:
            print("  first: %s   last: %s" % (h[0], h[-1]))
    print("  %d business day(s) in range, %d parsed for the year(s)"
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
        sel = [v for v in sel if any(t in json.dumps(v).lower() for t in terms)]
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
    print("")
    print("  dateAdded settles a windowed claim. Presence in the catalog is")
    print("  NOT a hit if the entry predates the row's window.")
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
    feats = json.loads(body.decode("utf-8")).get("features", [])
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
    print("  USGS carries no fatality field. Try `gdacs` for that half.")
    cite(url)
    return 0


# --------------------------------------------------------------------- gdacs
def cmd_gdacs(a):
    body = fetch(GDACS)
    if body is None:
        return 1
    text = body.decode("utf-8", errors="replace")
    items = re.findall(r"<item>(.*?)</item>", text, re.S)

    def g(blk, tag):
        m = re.search(r"<%s[^>]*>(.*?)</%s>" % (tag, tag), blk, re.S)
        if not m:
            return ""
        v = re.sub(r"<!\[CDATA\[(.*?)\]\]>", r"\1", m.group(1), flags=re.S)
        return re.sub(r"\s+", " ", strip_tags(v)).strip()

    rows = [{"title": g(b, "title"), "date": g(b, "pubDate"),
             "level": g(b, "gdacs:alertlevel") or g(b, "alertlevel"),
             "country": g(b, "gdacs:country") or g(b, "country"),
             "etype": g(b, "gdacs:eventtype") or g(b, "eventtype"),
             "sev": g(b, "gdacs:severity") or g(b, "severity"),
             "link": g(b, "link")} for b in items]
    sel = rows
    if a.country:
        c = a.country.lower()
        sel = [r for r in sel
               if c in r["country"].lower() or c in r["title"].lower()]
    if a.level:
        sel = [r for r in sel if r["level"].lower() == a.level.lower()]
    if a.type:
        sel = [r for r in sel if r["etype"].upper() == a.type.upper()]
    print("")
    print("GDACS GLOBAL DISASTER ALERTS")
    print("-" * 68)
    print("  %d item(s) in feed, %d match" % (len(rows), len(sel)))
    print("")
    for r in sel[:40]:
        print("  %-6s %-5s %-16s %s" % (r["level"][:6], r["etype"][:5],
                                        r["country"][:16], r["title"][:44]))
        if a.verbose and r["sev"]:
            print("        severity: %s" % r["sev"][:88])
        if a.verbose and r["link"]:
            print("        %s" % r["link"][:88])
    print("")
    print("  GDACS is a CURRENT feed, not an archive. A row with a deadline")
    print("  months out cannot be resolved from a snapshot taken today.")
    cite(GDACS)
    return 0


# -------------------------------------------------------------------- fedreg
def cmd_fedreg(a):
    q = [("per_page", str(min(a.limit or 20, 100))), ("order", "newest")]
    if a.term:
        q.append(("conditions[term]", a.term))
    if a.agency:
        q.append(("conditions[agencies][]", a.agency))
    if getattr(a, "frm", None):
        q.append(("conditions[publication_date][gte]", a.frm))
    if a.to:
        q.append(("conditions[publication_date][lte]", a.to))
    for f in ("document_number", "publication_date", "title", "type",
              "agencies", "html_url"):
        q.append(("fields[]", f))
    url = FEDREG + "?" + urllib.parse.urlencode(q)
    body = fetch(url)
    if body is None:
        return 1
    d = json.loads(body.decode("utf-8"))
    res = d.get("results", [])
    print("")
    print("FEDERAL REGISTER")
    print("-" * 68)
    print("  %s total match, showing %d" % (d.get("count", "?"), len(res)))
    print("")
    for r in res:
        ags = ", ".join(x.get("name", "") for x in (r.get("agencies") or []))[:28]
        print("  %s  %-10s %-28s %s"
              % (r.get("publication_date", "?"), str(r.get("type", ""))[:10],
                 ags, ascii_only(r.get("title", ""), 44)))
        if a.verbose:
            print("        %s" % r.get("html_url", ""))
    print("")
    print("  publication_date settles a windowed claim.")
    cite(url)
    return 0


# ----------------------------------------------------------------------- ecb
def cmd_ecb(a):
    url = ECB % (a.last or 10)
    body = fetch(url)
    if body is None:
        return 1
    lines = body.decode("utf-8", errors="replace").splitlines()
    if not lines:
        print("EMPTY RESPONSE", file=sys.stderr)
        return 1
    hdr = lines[0].split(",")
    try:
        it, iv = hdr.index("TIME_PERIOD"), hdr.index("OBS_VALUE")
    except ValueError:
        print("HEADER SHAPE CHANGED. Nothing asserted.", file=sys.stderr)
        print("  header: %s" % lines[0][:200], file=sys.stderr)
        return 1
    print("")
    print("ECB - main refinancing operations, fixed rate (MRR_FR)")
    print("-" * 68)
    obs = []
    for ln in lines[1:]:
        c = ln.split(",")
        if len(c) > max(it, iv) and c[it]:
            obs.append((c[it], c[iv]))
    for t, v in obs:
        print("  %s  %s%%" % (t, v))
    if len(obs) > 1:
        print("")
        print("  %s across the %d observations shown"
              % ("CHANGED" if obs[0][1] != obs[-1][1] else "unchanged", len(obs)))
    print("")
    print("  MRR_FR is the main refinancing rate. Confirm the row names THIS")
    print("  instrument - the NY Fed probe passed and served EFFR instead.")
    cite(url)
    return 0


# ---------------------------------------------------------------------- wiki
def cmd_wiki(a):
    url = WIKI % urllib.parse.quote(a.page.replace(" ", "_"))
    body = fetch(url)
    if body is None:
        return 1
    text = strip_tags(body.decode("utf-8", errors="replace"))
    print("")
    print("WIKIPEDIA - %s" % a.page)
    print("-" * 68)
    print("  %d bytes fetched, %d characters of text" % (len(body), len(text)))
    if not a.name:
        print("")
        print("  no --name given; nothing tested.")
        cite(url)
        return 0
    needle = a.name.strip()
    idx = text.lower().find(needle.lower())
    print("")
    if idx >= 0:
        lo, hi = max(0, idx - 90), min(len(text), idx + len(needle) + 90)
        n = len(re.findall(re.escape(needle), text, re.I))
        print("  PRESENT  %s appears in the page text." % needle)
        print("           ...%s..." % text[lo:hi])
        print("           %d occurrence(s)" % n)
    else:
        print("  ABSENT   %s does not appear in the page text." % needle)
        print("           A rename, a redirect or a page restructure produces")
        print("           the same result as a change of command. Read the page.")
    print("")
    print("  STRING MATCHING IS THE WEAKNESS HERE. The Wikidata SPARQL")
    print("  endpoint is live and would test a structured claim instead;")
    print("  it is not wired in because the right property for a military")
    print("  formation's commander has not been identified yet.")
    cite(url)
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="keyless lookups for resolving sealed rows. Writes nothing.")
    sub = ap.add_subparsers(dest="cmd")

    w = sub.add_parser("wire", help="GDELT search + two-of-N outlet test")
    w.add_argument("--query", required=True)
    w.add_argument("--days", type=int, help="lookback, default 7")
    w.add_argument("--outlets", help="comma-separated domains")
    w.add_argument("--threshold", type=int, help="outlets required, default 2")
    w.add_argument("--max", type=int)

    n = sub.add_parser("nvd", help="NIST CVE records and severity")
    n.add_argument("--cve")
    n.add_argument("--keyword")
    n.add_argument("--from", dest="frm")
    n.add_argument("--to")
    n.add_argument("--limit", type=int)
    n.add_argument("--verbose", action="store_true")

    fm = sub.add_parser("fema", help="OpenFEMA disaster declarations")
    fm.add_argument("--state")
    fm.add_argument("--type", help="e.g. Fire, Flood, Severe Storm")
    fm.add_argument("--from", dest="frm")
    fm.add_argument("--to")
    fm.add_argument("--limit", type=int)

    eo = sub.add_parser("eonet", help="NASA natural event catalogue")
    eo.add_argument("--category", help="e.g. wildfires, severeStorms, volcanoes")
    eo.add_argument("--days", type=int)
    eo.add_argument("--status", help="open or closed")
    eo.add_argument("--limit", type=int)

    t = sub.add_parser("treasury", help="10-year par yield")
    t.add_argument("--date")
    t.add_argument("--from", dest="frm")
    t.add_argument("--to")
    t.add_argument("--above", type=float)

    k = sub.add_parser("kev", help="CISA Known Exploited Vulnerabilities")
    k.add_argument("--cve")
    k.add_argument("--since")
    k.add_argument("--until")
    k.add_argument("--match")
    k.add_argument("--verbose", action="store_true")

    q = sub.add_parser("quake", help="USGS events")
    q.add_argument("--from", dest="frm")
    q.add_argument("--to")
    q.add_argument("--minmag", type=float)
    q.add_argument("--lat", type=float)
    q.add_argument("--lon", type=float)
    q.add_argument("--radius", type=float)
    q.add_argument("--minlat", type=float)
    q.add_argument("--maxlat", type=float)
    q.add_argument("--minlon", type=float)
    q.add_argument("--maxlon", type=float)

    g = sub.add_parser("gdacs", help="GDACS alerts - carries death tolls")
    g.add_argument("--country")
    g.add_argument("--level")
    g.add_argument("--type")
    g.add_argument("--verbose", action="store_true")

    f = sub.add_parser("fedreg", help="Federal Register documents")
    f.add_argument("--term")
    f.add_argument("--agency")
    f.add_argument("--from", dest="frm")
    f.add_argument("--to")
    f.add_argument("--limit", type=int)
    f.add_argument("--verbose", action="store_true")

    e = sub.add_parser("ecb", help="ECB main refinancing rate")
    e.add_argument("--last", type=int)

    wk = sub.add_parser("wiki", help="is a name still on a page?")
    wk.add_argument("--page", required=True)
    wk.add_argument("--name")

    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return 0
    return {"wire": cmd_wire, "nvd": cmd_nvd, "fema": cmd_fema,
            "eonet": cmd_eonet, "treasury": cmd_treasury, "kev": cmd_kev,
            "quake": cmd_quake, "gdacs": cmd_gdacs, "fedreg": cmd_fedreg,
            "ecb": cmd_ecb, "wiki": cmd_wiki}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
