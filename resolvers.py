#!/usr/bin/env python3
"""
resolvers.py — fetchers and predicate evaluators for the named public
instruments this desk's resolution bases cite. The mechanical half of blind
adjudication: a resolver sees neither the forecaster arm nor the stated
probability, only the instrument and the predicate.

DISCIPLINE, printed here because it governs everything below:

  * SCHEMA-UNVERIFIED. Every resolver carries a confidence tag. None of these
    parsers has touched its live endpoint from this desk yet; the first live
    run is --dry-run by policy, and a parse that does not find exactly what it
    expects returns INDETERMINATE — a resolver never guesses, and a fetch or
    parse failure proposes nothing.
  * EVIDENCE OR IT DIDN'T HAPPEN. Every fetch writes a meta record (url,
    UTC timestamp, SHA-256 of the raw bytes, resolver, params, verdict) to
    evidence/; raw bytes are kept alongside with --keep-raw. The meta is the
    dated proof a resolution can cite.
  * PROPOSE, NEVER RESOLVE. Nothing here writes the ledger. The operator's
    `kkr --resolve` remains the only resolution path; this library feeds it
    a verdict proposal and an evidence hash.

Verdicts: YES (predicate satisfied), NO (predicate checked and unsatisfied),
INDETERMINATE (could not be checked — with the reason).
"""

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen, Request

HERE = Path(__file__).resolve().parent
EVIDENCE = HERE / "evidence"
UA = {"User-Agent": "prescient-desk-resolver/1.0 (retroprescientaudit.com)"}


def _fetch(url: str, timeout: int = 45) -> bytes:
    req = Request(url, headers=UA)
    with urlopen(req, timeout=timeout) as r:
        return r.read()


# KK21i: row context, set by the caller before a resolver runs. Without it an
# evidence record cannot say whether it was taken to RESOLVE a row or merely
# to test that the parser works — and those two files looked identical.
_ROW_CTX = {"deadline": None, "probe": False}


def set_row_context(deadline=None, probe: bool = False):
    """Declare what this fetch is. A fetch before the row's deadline is a
    probe: it proves the parser reads the endpoint, and it is not evidence of
    anything about the row, because the window had not closed."""
    _ROW_CTX["deadline"] = deadline
    _ROW_CTX["probe"] = bool(probe)


def _evidence(row_id: str, resolver: str, url: str, raw: bytes,
              params: dict, verdict: str, detail: str,
              keep_raw: bool = False) -> dict:
    EVIDENCE.mkdir(exist_ok=True)
    now = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    sha = hashlib.sha256(raw).hexdigest()
    dl = _ROW_CTX.get("deadline")
    probe = bool(_ROW_CTX.get("probe")) or (
        dl is not None and now[:8] < str(dl).replace("-", ""))
    meta = {"row": row_id, "resolver": resolver, "url": url,
            "fetched_at": now, "sha256_raw": sha, "bytes": len(raw),
            "params": params, "detail": detail,
            "row_deadline": dl,
            "probe": probe}
    # A verdict reached before the deadline is not a proposal about the row.
    # It is what the instrument read on the day, and it is labelled as that.
    meta["verdict_if_resolved_now" if probe else "verdict_proposed"] = verdict
    if probe:
        meta["not_resolving_evidence"] = (
            "Fetched before the row's deadline. The window had not closed, so "
            "this record proves the parser reads its endpoint and nothing "
            "about the row. Do not cite it in a resolution note.")
    stem = f"{row_id}_{now}" + ("_probe" if probe else "")
    (EVIDENCE / f"{stem}.meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    if keep_raw:
        (EVIDENCE / f"{stem}.bin").write_bytes(raw)
    return meta


# ---------------------------------------------------------------- CISA KEV
KEV_URL = ("https://www.cisa.gov/sites/default/files/feeds/"
           "known_exploited_vulnerabilities.json")

def resolve_kev(row_id, params, keep_raw=False):
    """params: vendor (str), window (start,end ISO dates).
    confidence: MEDIUM — documented public feed, schema unverified here."""
    raw = _fetch(KEV_URL)
    try:
        vulns = json.loads(raw.decode("utf-8")).get("vulnerabilities", [])
    except Exception as e:
        return _evidence(row_id, "kev", KEV_URL, raw, params, "INDETERMINATE",
                         f"feed parse failed: {e}", keep_raw)
    # MAPWIDE-2026-09-15: any of several names, matched against vendorProject, product and vulnerabilityName.
    s, e_ = params["window"]
    if params.get("min_count"):
        inwin = [x for x in vulns if s <= str(x.get("dateAdded", "")) <= e_]
        verdict = "YES" if len(inwin) >= int(params["min_count"]) else "NO"
        detail = (f"{len(inwin)} entries with dateAdded in [{s}..{e_}] against a floor of "
                  f"{params['min_count']} across {len(vulns)} catalog rows")
        return _evidence(row_id, "kev", KEV_URL, raw, params, verdict, detail, keep_raw)
    names = [str(n).lower() for n in (params.get("vendors") or [params["vendor"]]) if n]
    hits = [x for x in vulns
            if any(v in (str(x.get("vendorProject", "")) + " " + str(x.get("product", "")) + " " +
                         str(x.get("vulnerabilityName", "")) + " " + str(x.get("cveID", ""))).lower() for v in names)
            and s <= str(x.get("dateAdded", "")) <= e_]
    verdict = "YES" if hits else "NO"
    matched = sorted({str(x.get("cveID", "")) for x in hits})[:6]
    detail = (f"{len(hits)} matching entr{'y' if len(hits)==1 else 'ies'} "
              f"for {params.get('vendors') or [params['vendor']]} with dateAdded in [{s}..{e_}] "
              f"across {len(vulns)} catalog rows{(' - ' + ', '.join(matched)) if matched else ''}")
    return _evidence(row_id, "kev", KEV_URL, raw, params, verdict, detail,
                     keep_raw)


# ---------------------------------------------------------------- USGS FDSN
def resolve_usgs(row_id, params, keep_raw=False):
    """params: lat, lon, radius_km, min_mag, window (start,end).
    confidence: HIGH — FDSN is a versioned public API; schema unverified here."""
    s, e_ = params["window"]
    # EVENTID-2026-09-16: an event id resolves to its epicentre in ComCat before the radius
    # query runs. A failed lookup is INDETERMINATE naming the id - never a guessed coordinate.
    _eid_note = ""
    if params.get("event_id") and not (params.get("lat") and params.get("lon")):
        _eid = params["event_id"]
        _durl = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&eventid=%s" % _eid)
        try:
            _draw = _fetch(_durl)
            _d = json.loads(_draw.decode("utf-8"))
            _feat = _d if _d.get("type") == "Feature" else (_d.get("features") or [None])[0]
            _lon, _lat = _feat["geometry"]["coordinates"][0], _feat["geometry"]["coordinates"][1]
            _title = str(_feat.get("properties", {}).get("title", ""))[:60]
            _otime = _feat.get("properties", {}).get("time")
            params = dict(params, lat=float(_lat), lon=float(_lon))
            _eid_note = (" [epicentre from %s: lat %.4f lon %.4f, %s, lookup sha256 %s]"
                         % (_eid, float(_lat), float(_lon), _title,
                            hashlib.sha256(_draw).hexdigest()[:16]))
        except Exception as ex:
            return _evidence(row_id, "usgs", _durl, b"", params, "INDETERMINATE",
                             "event id %s could not be resolved to an epicentre: %r" % (_eid, ex), keep_raw)
    if params.get("bbox"):
        # MAPWIDE-2026-09-15: a regional bounding box instead of a radius (coarse; the proposal says so).
        b0, b1, b2, b3 = params["bbox"]
        url = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
               f"&starttime={s}&endtime={e_}&minlatitude={b0}&maxlatitude={b1}"
               f"&minlongitude={b2}&maxlongitude={b3}&minmagnitude={params['min_mag']}")
    else:
        url = ("https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"
               f"&starttime={s}&endtime={e_}&latitude={params['lat']}"
               f"&longitude={params['lon']}&maxradiuskm={params['radius_km']}"
               f"&minmagnitude={params['min_mag']}")
    raw = _fetch(url)
    try:
        feats = json.loads(raw.decode("utf-8")).get("features", [])
    except Exception as e:
        return _evidence(row_id, "usgs", url, params and url and params,
                         "INDETERMINATE", f"parse failed: {e}", keep_raw)
    verdict = "YES" if feats else "NO"
    mags = sorted((f.get("properties", {}).get("mag") for f in feats),
                  reverse=True)[:3]
    detail = f"{len(feats)} event(s) returned; top magnitudes {mags}"
    return _evidence(row_id, "usgs", url, raw, params, verdict, detail,
                     keep_raw)


# ---------------------------------------------------------------- Treasury
def resolve_treasury_10y(row_id, params, keep_raw=False):
    """params: threshold (float), window (start,end), direction ('>=' only v1).
    confidence: MEDIUM — the desk's own rows name this XML and the BC_10YEAR
    field; year-scoped URL; schema unverified here."""
    year = params["window"][0][:4]
    url = ("https://home.treasury.gov/resource-center/data-chart-center/"
           "interest-rates/pages/xml?data=daily_treasury_yield_curve"
           f"&field_tdr_date_value={year}")
    raw = _fetch(url)
    try:
        root = ET.fromstring(raw)
        ns = {"m": "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata",
              "d": "http://schemas.microsoft.com/ado/2007/08/dataservices"}
        days = []
        # MAPWIDE-2026-09-15: the tenor's field (BC_2YEAR, BC_5YEAR, BC_10YEAR, BC_30YEAR); 10-year by default.
        field = "BC_%sYEAR" % str(params.get("tenor") or "10")
        for props in root.iter("{%s}properties" % ns["m"]):
            date = props.findtext("{%s}NEW_DATE" % ns["d"], "")[:10]
            val = props.findtext("{%s}%s" % (ns["d"], field), "")
            if date and val:
                days.append((date, float(val)))
    except Exception as e:
        return _evidence(row_id, "treasury10y", url, raw, params,
                         "INDETERMINATE", f"XML parse failed: {e}", keep_raw)
    s, e_ = params["window"]
    inwin = [(d, v) for d, v in days if s <= d <= e_]
    if not inwin:
        return _evidence(row_id, "treasury10y", url, raw, params,
                         "INDETERMINATE",
                         f"no business days parsed inside [{s}..{e_}] "
                         f"({len(days)} days in year file)", keep_raw)
    # MAPWIDE-2026-09-15: the direction the row states; ">=" by default as before.
    direction = params.get("direction") or ">="
    op = {">=": lambda v: v >= params["threshold"], ">": lambda v: v > params["threshold"],
          "<=": lambda v: v <= params["threshold"], "<": lambda v: v < params["threshold"]}[direction]
    hits = [(d, v) for d, v in inwin if op(v)]
    verdict = "YES" if hits else "NO"
    ext = max(inwin, key=lambda x: x[1]) if direction in (">=", ">") else min(inwin, key=lambda x: x[1])
    detail = (f"{len(inwin)} business days in window; {'max' if direction in ('>=', '>') else 'min'} {field} "
              f"{ext[1]:.2f} on {ext[0]}; threshold {direction} {params['threshold']:.2f}; "
              f"{len(hits)} day(s) satisfying")
    return _evidence(row_id, "treasury10y", url, raw, params, verdict, detail,
                     keep_raw)


# ---------------------------------------------------------------- ECB SDW
def resolve_ecb_series(row_id, params, keep_raw=False):
    """params: flow_series (e.g. 'FM/D.U2.EUR.4F.KR.MRR_FR.LEV'),
    compare_date, baseline_date, predicate ('unchanged' v1).
    confidence: LOW — SDMX-JSON layout assumed; INDETERMINATE on any surprise."""
    flow, series = params["flow_series"].split("/", 1)
    lo = min(params["baseline_date"], params["compare_date"])
    hi = max(params["baseline_date"], params["compare_date"])
    url = (f"https://data-api.ecb.europa.eu/service/data/{flow}/{series}"
           f"?format=jsondata&startPeriod={lo}&endPeriod={hi}")
    raw = _fetch(url)
    try:
        j = json.loads(raw.decode("utf-8"))
        sets = j["dataSets"][0]["series"]
        obs = next(iter(sets.values()))["observations"]
        dims = j["structure"]["dimensions"]["observation"][0]["values"]
        byday = {dims[int(k)]["id"]: v[0] for k, v in obs.items()}
    except Exception as e:
        return _evidence(row_id, "ecb", url, raw, params, "INDETERMINATE",
                         f"SDMX parse failed (schema-unverified): {e}",
                         keep_raw)
    b = byday.get(params["baseline_date"])
    c = byday.get(params["compare_date"])
    if b is None or c is None:
        return _evidence(row_id, "ecb", url, raw, params, "INDETERMINATE",
                         f"missing observation: baseline={b} compare={c} "
                         f"(have {sorted(byday)[:4]}…)", keep_raw)
    verdict = "YES" if float(b) == float(c) else "NO"
    detail = (f"{params['flow_series']}: {params['baseline_date']}={b} vs "
              f"{params['compare_date']}={c} — "
              f"{'unchanged' if verdict == 'YES' else 'changed'}")
    return _evidence(row_id, "ecb", url, raw, params, verdict, detail,
                     keep_raw)


# ------------------------------------------------------- Federal Register
def resolve_fedreg(row_id, params, keep_raw=False):
    """params: term, agencies (list of api slugs), window (start,end).
    confidence: HIGH — documented public API; schema unverified here."""
    s, e_ = params["window"]
    ag = "".join(f"&conditions[agencies][]={a}" for a in params["agencies"])
    url = ("https://www.federalregister.gov/api/v1/documents.json?per_page=20"
           f"&conditions[term]={params['term']}"
           f"&conditions[publication_date][gte]={s}"
           f"&conditions[publication_date][lte]={e_}{ag}")
    raw = _fetch(url)
    try:
        j = json.loads(raw.decode("utf-8"))
        n = int(j.get("count", 0))
    except Exception as e:
        return _evidence(row_id, "fedreg", url, raw, params, "INDETERMINATE",
                         f"parse failed: {e}", keep_raw)
    verdict = "YES" if n > 0 else "NO"
    titles = [d.get("title", "")[:70] for d in j.get("results", [])[:3]]
    detail = f"{n} document(s) for term '{params['term']}' in window; {titles}"
    return _evidence(row_id, "fedreg", url, raw, params, verdict, detail,
                     keep_raw)


# ---------------------------------------------------------------- GDACS
GDACS_URL = "https://www.gdacs.org/xml/rss.xml"

def resolve_gdacs(row_id, params, keep_raw=False):
    """params: country, alertlevel, window (start,end).
    confidence: LOW — RSS carries current alerts, not a windowed archive; a NO
    here means 'not currently listed', so v1 returns YES on a live match and
    INDETERMINATE otherwise rather than a false NO."""
    raw = _fetch(GDACS_URL)
    try:
        root = ET.fromstring(raw)
        items = []
        for i in root.iter("item"):
            title = i.findtext("title", "") or ""
            # KK21k: the level is read STRUCTURALLY. The previous matcher
            # tested `want_a in blob` against every string in the item
            # flattened together, so "red" matched a legend, a URL fragment,
            # or the word "hundred" — and on 2026-08-04 it returned YES on an
            # item whose own title says Green. Namespaced element first, then
            # the title's opening word, then nothing.
            lvl = None
            for el in i.iter():
                if el.tag.rsplit("}", 1)[-1].lower() == "alertlevel" and el.text:
                    lvl = el.text.strip().lower()
                    break
            if lvl is None:
                first = title.strip().split(" ", 1)[0].lower()
                if first in ("green", "orange", "red"):
                    lvl = first
            items.append((title, "".join(i.itertext()).lower(), lvl))
    except Exception as e:
        return _evidence(row_id, "gdacs", GDACS_URL, raw, params,
                         "INDETERMINATE", f"RSS parse failed: {e}", keep_raw)
    want_c = params["country"].lower()
    want_a = params["alertlevel"].lower()
    if items and not any(lvl for _, _, lvl in items):
        return _evidence(row_id, "gdacs", GDACS_URL, raw, params,
                         "INDETERMINATE",
                         f"no alert level readable on any of {len(items)} feed "
                         f"items — neither a namespaced alertlevel element nor "
                         f"a level-prefixed title. Refusing to infer the level "
                         f"from item body text; that produced a false YES on "
                         f"2026-08-04.", keep_raw)
    hits = [t for t, blob, lvl in items if want_c in blob and lvl == want_a]
    if hits:
        return _evidence(row_id, "gdacs", GDACS_URL, raw, params, "YES",
                         f"live {params['alertlevel']} alert matching "
                         f"{params['country']}: {hits[:2]}", keep_raw)
    return _evidence(row_id, "gdacs", GDACS_URL, raw, params, "INDETERMINATE",
                     f"no live match in {len(items)} feed items — the RSS is "
                     f"a current-state feed; absence now does not adjudicate "
                     f"the whole window. Archive check is the operator's.",
                     keep_raw)


REGISTRY = {"kev": resolve_kev, "usgs": resolve_usgs,
            "treasury10y": resolve_treasury_10y, "ecb": resolve_ecb_series,
            "fedreg": resolve_fedreg, "gdacs": resolve_gdacs}
