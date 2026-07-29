#!/usr/bin/env python3
"""
desk_lookup.py - reproducible lookups for resolving sealed rows.

WHAT IT DOES NOT DO

It does not resolve anything. It writes no file, touches no ledger, and
proposes no verdict it can act on. It fetches a published value at a named
date and prints it with the query that produced it, so the operator
adjudicates against evidence a stranger can re-fetch.

That division is deliberate. The colophon says resolution and publication are
the operator's. A tool that writes a verdict into a permanent record from a
field it parsed wrong is worse than the manual work it saves - and across two
probe rounds, two endpoints returned HTML shells that a lazy content check
scored as passing, one returns real data for the wrong instrument, and one is
behind a bot challenge. The lookup is mechanical. The judgement stays yours.

SOURCES - ALL KEYLESS, ALL PROBED

  treasury  US Treasury daily par yield curve, XML       PROBED PASS
  kev       CISA Known Exploited Vulnerabilities, JSON   PROBED PASS
  quake     USGS FDSN event query, GeoJSON               PROBED PASS
  gdacs     GDACS global disaster alerts, RSS            PROBED PASS
  fedreg    Federal Register documents API, JSON         PROBED PASS
  ecb       ECB Data Portal, CSV                         PROBED PASS
  wiki      Wikipedia page HTML                          SEE WARNING BELOW

WARNING ON `wiki`

Round two probed the REST *summary* endpoint, which returns only the lead
extract. A formation's commanding officer lives in the infobox, not the lead,
so this subcommand uses the page HTML endpoint instead - which was NOT probed.
The first run is the probe. If it fails, that is the finding.

And the deeper caution: the kfk/halflife rows say "in the source of record".
Confirm WHICH source each row named before treating a wiki result as
dispositive. The NY Fed endpoint passed cleanly and served the wrong
instrument; a PASS is not a licence.

WHAT IS NOT HERE, AND WHY

  stooq     BLOCKED by a JavaScript bot challenge. Index and oil settlements
            have no keyless source, which leaves S&P, Nasdaq, Brent and WTI
            hand-adjudicated. This is the largest unresolved class.
  effis     HTML shell of a JavaScript app, not an API.
  hhs       JSF page, not machine-queryable.
  gdelt     429 rate-limited on probe, not rejected. Retry with a delay.
  fed funds NY Fed serves EFFR, the realised rate. The rows name the FOMC
            target upper bound. Right host, wrong instrument.
  FRED      needs an API key. No key belongs in this repo - publish.bat runs
            git add -A, and every source in report_config.json is keyless,
            which is why that file can sit tracked in public.

    python desk_lookup.py treasury --from 2026-07-01 --to 2026-07-29 --above 4.80
    python desk_lookup.py kev --cve CVE-2026-16812
    python desk_lookup.py kev --since 2026-07-27 --match fastjson,gitlab
    python desk_lookup.py quake --from 2026-07-30 --to 2026-09-30 --minmag 5.5
    python desk_lookup.py gdacs --country Japan --level Red
    python desk_lookup.py fedreg --agency treasury-department --term Iran
    python desk_lookup.py ecb --last 8
    python desk_lookup.py wiki --page XVIII_Airborne_Corps --name "Gregory K. Anderson"

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

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) desk_lookup/1.1 "
      "(+https://retroprescientaudit.com)")
TIMEOUT = 30

TREASURY = ("https://home.treasury.gov/resource-center/data-chart-center/"
            "interest-rates/pages/xml?data=daily_treasury_yield_curve"
            "&field_tdr_date_value=%s")
KEV = ("https://www.cisa.gov/sites/default/files/feeds/"
       "known_exploited_vulnerabilities.json")
USGS = "https://earthquake.usgs.gov/fdsnws/event/1/query"
GDACS = "https://www.gdacs.org/xml/rss.xml"
FEDREG = "https://www.federalregister.gov/api/v1/documents.json"
ECB = ("https://data-api.ecb.europa.eu/service/data/FM/"
       "D.U2.EUR.4F.KR.MRR_FR.LEV?format=csvdata&lastNObservations=%d")
WIKI = "https://en.wikipedia.org/api/rest_v1/page/html/%s"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT,
                                    context=ssl.create_default_context()) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        print("FETCH FAILED - HTTP %s %s" % (e.code, e.reason), file=sys.stderr)
        if e.code in (403, 406):
            print("  the edge rejected a programmatic client. Source-side.",
                  file=sys.stderr)
        if e.code == 429:
            print("  rate-limited, not rejected. Wait and retry.", file=sys.stderr)
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
            mark = ("  ABOVE %.2f" % a.above if v > a.above
                    else "  at or below %.2f" % a.above)
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
    print("  dateAdded is what settles a windowed claim. Presence in the")
    print("  catalog is NOT a hit if the entry predates the row's window.")
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
    print("  USGS carries no fatality field. A row requiring a death toll is")
    print("  only PARTIALLY served here - try `gdacs` for the other half.")
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

    rows = []
    for blk in items:
        rows.append({
            "title": g(blk, "title"),
            "date": g(blk, "pubDate"),
            "level": g(blk, "gdacs:alertlevel") or g(blk, "alertlevel"),
            "country": g(blk, "gdacs:country") or g(blk, "country"),
            "etype": g(blk, "gdacs:eventtype") or g(blk, "eventtype"),
            "sev": g(blk, "gdacs:severity") or g(blk, "severity"),
            "link": g(blk, "link"),
        })

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
        print("  %-6s %-5s %-16s %s"
              % (r["level"][:6], r["etype"][:5], r["country"][:16],
                 r["title"][:44]))
        if a.verbose and r["sev"]:
            print("        severity: %s" % r["sev"][:88])
        if a.verbose and r["link"]:
            print("        %s" % r["link"][:88])
    if len(sel) > 40:
        print("  ... %d more not shown" % (len(sel) - 40))
    print("")
    print("  GDACS is a CURRENT feed, not an archive - it carries active and")
    print("  recent events only. A row with a deadline months out cannot be")
    print("  resolved from a snapshot taken today. Check at the deadline.")
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
              % (r.get("publication_date", "?"),
                 str(r.get("type", ""))[:10], ags,
                 str(r.get("title", ""))[:44]))
        if a.verbose:
            print("        %s" % r.get("html_url", ""))
    print("")
    print("  publication_date is what settles a windowed claim.")
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
        print("HEADER SHAPE CHANGED - TIME_PERIOD or OBS_VALUE missing. "
              "Nothing asserted.", file=sys.stderr)
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
        chg = obs[0][1] != obs[-1][1]
        print("")
        print("  %s across the %d observations shown"
              % ("CHANGED" if chg else "unchanged", len(obs)))
    print("")
    print("  MRR_FR is the main refinancing rate. Confirm the row names THIS")
    print("  instrument - the NY Fed probe passed cleanly and served EFFR,")
    print("  which is a different number from the one those rows asked about.")
    cite(url)
    return 0


# ---------------------------------------------------------------------- wiki
def cmd_wiki(a):
    url = WIKI % urllib.parse.quote(a.page.replace(" ", "_"))
    body = fetch(url)
    if body is None:
        print("  NOTE: round two probed the REST summary endpoint, not this",
              file=sys.stderr)
        print("  HTML endpoint. A failure here is a finding, not a bug.",
              file=sys.stderr)
        return 1
    text = strip_tags(body.decode("utf-8", errors="replace"))
    print("")
    print("WIKIPEDIA - %s" % a.page)
    print("-" * 68)
    print("  %d bytes fetched, %d characters of text" % (len(body), len(text)))
    if not a.name:
        print("")
        print("  no --name given; nothing tested. Pass the officer's name.")
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
        print("           For a row asking whether an officer is NO LONGER")
        print("           named, absence is the condition being tested - but")
        print("           read the page yourself before ruling. A rename, a")
        print("           redirect, or a restructure produces the same result")
        print("           as a change of command.")
    print("")
    print("  This endpoint was NOT in the probe round. Treat the first run as")
    print("  the probe. And the rows say 'in the source of record' - confirm")
    print("  which source each row named before treating this as dispositive.")
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
    t.add_argument("--above", type=float)

    k = sub.add_parser("kev", help="CISA Known Exploited Vulnerabilities")
    k.add_argument("--cve")
    k.add_argument("--since")
    k.add_argument("--until")
    k.add_argument("--match")
    k.add_argument("--verbose", action="store_true")

    q = sub.add_parser("quake", help="USGS events in a window and area")
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
    g.add_argument("--level", help="Green, Orange or Red")
    g.add_argument("--type", help="EQ, TC, FL, DR, WF, VO")
    g.add_argument("--verbose", action="store_true")

    f = sub.add_parser("fedreg", help="Federal Register documents")
    f.add_argument("--term")
    f.add_argument("--agency", help="slug, e.g. treasury-department")
    f.add_argument("--from", dest="frm")
    f.add_argument("--to")
    f.add_argument("--limit", type=int)
    f.add_argument("--verbose", action="store_true")

    e = sub.add_parser("ecb", help="ECB main refinancing rate")
    e.add_argument("--last", type=int, help="observations, default 10")

    w = sub.add_parser("wiki", help="is a name still on a page?")
    w.add_argument("--page", required=True)
    w.add_argument("--name")

    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return 0
    return {"treasury": cmd_treasury, "kev": cmd_kev, "quake": cmd_quake,
            "gdacs": cmd_gdacs, "fedreg": cmd_fedreg, "ecb": cmd_ecb,
            "wiki": cmd_wiki}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
