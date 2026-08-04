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
    v = params["vendor"].lower()
    s, e_ = params["window"]
    hits = [x for x in vulns
            if v in (str(x.get("vendorProject", "")) + " " +
                     str(x.get("product", ""))).lower()
            and s <= str(x.get("dateAdded", "")) <= e_]
    verdict = "YES" if hits else "NO"
    detail = (f"{len(hits)} matching entr{'y' if len(hits)==1 else 'ies'} "
              f"for '{params['vendor']}' with dateAdded in [{s}..{e_}] "
              f"across {len(vulns)} catalog rows")
    return _evidence(row_id, "kev", KEV_URL, raw, params, verdict, detail,
                     keep_raw)


# ---------------------------------------------------------------- USGS FDSN
def resolve_usgs(row_id, params, keep_raw=False):
    """params: lat, lon, radius_km, min_mag, window (start,end).
    confidence: HIGH — FDSN is a versioned public API; schema unverified here."""
    s, e_ = params["window"]
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
        for props in root.iter("{%s}properties" % ns["m"]):
            date = props.findtext("{%s}NEW_DATE" % ns["d"], "")[:10]
            val = props.findtext("{%s}BC_10YEAR" % ns["d"], "")
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
    hits = [(d, v) for d, v in inwin if v >= params["threshold"]]
    verdict = "YES" if hits else "NO"
    hi = max(inwin, key=lambda x: x[1])
    detail = (f"{len(inwin)} business days in window; max BC_10YEAR "
              f"{hi[1]:.2f} on {hi[0]}; threshold {params['threshold']:.2f}; "
              f"{len(hits)} day(s) at or above")
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
        items = [(i.findtext("title", ""),
                  "".join(i.itertext()).lower())
                 for i in root.iter("item")]
    except Exception as e:
        return _evidence(row_id, "gdacs", GDACS_URL, raw, params,
                         "INDETERMINATE", f"RSS parse failed: {e}", keep_raw)
    want_c = params["country"].lower()
    want_a = params["alertlevel"].lower()
    hits = [t for t, blob in items if want_c in blob and want_a in blob]
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
